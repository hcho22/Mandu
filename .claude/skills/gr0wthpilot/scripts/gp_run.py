#!/usr/bin/env python3
"""Prepare a Gr0wthPilot run: pick its Candidate Package, start or resume its
run journal, and write the permission profile and guard config the launcher
starts Claude Code with.

Under the cache root, a run has two folders: `<Product>/`, its cache folder,
which the run writes (workflow copies, scratch, the source copy, builds, the
last30days log), and `<Product>.guard/`, the guard's own records (its config,
the permission profile, the robots.txt cache, the tool and fetch logs, and the
simulator ledger), which no tool of the run can write: it is outside the
sandbox's writable folders and the profile's edit rules, and the guard
refuses writes there. Only the guard hook and the unsandboxed wrappers write it.

The launcher (`bin/gr0wthpilot <Product>` at Mandu's root) calls `prepare`; the
skill calls `preflight` as its first step, which fails unless this run's guard
hook is live in the session.

Usage:
  gp_run.py prepare --mandu DIR --product NAME --cache DIR [--repo DIR] [--today YYYY-MM-DD]
  gp_run.py preflight [--config FILE]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gp_common as gc  # noqa: E402

PRODUCT_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}")
CANDIDATE_PREFIX = "gtm-candidate-"

# Bash reaches only the hosts last30days reads (ADR 0003 in decisions/log.md):
# its Reddit route, YouTube through yt-dlp, Hacker News, and Polymarket. The web
# is read through WebFetch, which is GET-only and checked against robots.txt by
# the guard. GitHub is left out on purpose: the gh token on this Mac can write.
BASH_NETWORK = [
    "reddit.com", "www.reddit.com", "old.reddit.com",
    "arctic-shift.photon-reddit.com",
    "youtube.com", "www.youtube.com", "m.youtube.com", "i.ytimg.com",
    "hn.algolia.com", "news.ycombinator.com",
    "gamma-api.polymarket.com", "polymarket.com",
]

# Tools a run never needs and that reach outside the Mac. A permission rule may
# name only the tools Claude Code's settings schema lists (RULE_RE below); a
# settings file with any other rule is dropped whole, silently in print mode.
# The guard refuses the tools no rule can name (AskUserQuestion, SendMessage,
# RemoteTrigger, PushNotification, CronCreate, ScheduleWakeup, ...).
DENIED_TOOLS = ["Artifact", "EnterWorktree", "mcp__*"]

# Shell commands denied by rule as well as by the guard (the guard is the
# primary check; these rules are a second, independent layer).
DENIED_BASH = [
    "git push", "git remote", "git send-email", "git commit", "git config",
    "gh", "hub", "glab", "wrangler", "vercel", "netlify", "firebase", "surge",
    "heroku", "flyctl", "fly", "railway", "aws", "gcloud", "gsutil", "az", "rclone",
    "scp", "sftp", "ssh", "rsync", "sendmail", "mail", "osascript", "open", "security",
    "npm publish", "npm login", "npm adduser", "yarn publish", "pnpm publish", "twine",
    "fastlane", "xcrun altool", "xcrun notarytool", "claude", "codex", "no-mistakes",
]

ALLOWED_TOOLS = [
    "Bash", "Read", "Glob", "Grep", "WebFetch", "WebSearch", "Agent", "Workflow",
    "ToolSearch", "TodoWrite", "TaskCreate", "TaskUpdate", "TaskList", "TaskGet",
    "TaskOutput", "TaskStop", "Monitor",
    "Skill(gr0wthpilot)", "Skill(customer-research)", "Skill(influencer-marketing)",
]

# The permission-rule pattern of Claude Code's settings schema
# (https://json.schemastore.org/claude-code-settings.json, $defs.permissionRule,
# read 2026-10-24 for Claude Code 2.1.284).
RULE_RE = re.compile(
    r"^((Agent|Artifact|Bash|Cd|Edit|EnterWorktree|ExitPlanMode|Glob|Grep|KillShell|LSP|Monitor|MultiEdit|"
    r"NotebookEdit|PowerShell|Read|ShareOnboardingGuide|Skill|TaskCreate|TaskGet|TaskList|TaskOutput|TaskStop|"
    r"TaskUpdate|TodoWrite|ToolSearch|WebFetch|WebSearch|Workflow|Write)(\([^)]+\))?|mcp__.*)$")
PERMISSION_KEYS = {"additionalDirectories", "allow", "ask", "defaultMode", "deny", "disableAutoMode",
                   "disableBypassPermissionsMode"}

# Copied from the Founder's own Claude Code settings, so a run uses his model
# and effort choice; nothing else is copied.
COPIED_USER_KEYS = ("model", "effortLevel")
EFFORT_LEVELS = ("low", "medium", "high", "xhigh")

# The workflow size guideline Claude Code sends Claude as advice. The session
# default is "medium" (fewer than 10 agents per workflow); "unrestricted" sends
# no guideline, so the run's own orchestration floor sets each workflow's size.
WORKFLOW_SIZE_GUIDELINE = "unrestricted"
WORKFLOW_SIZES = ("unrestricted", "small", "medium", "large")
PROFILE_KEYS = {"model", "effortLevel", "workflowSizeGuideline", "autoMemoryEnabled", "permissions",
                "sandbox", "hooks"}


class RunError(Exception):
    pass


def today_arg(text):
    if not text:
        return dt.date.today()
    return dt.datetime.strptime(text, "%Y-%m-%d").date()


def check_product(mandu: Path, product: str) -> Path:
    """The Product's folder in Mandu. The name must match the folder's name
    exactly, because the disk ignores case and every path rule does not."""
    if not PRODUCT_RE.fullmatch(product or ""):
        raise RunError("Product name must be letters, digits, '-' or '_': %r" % product)
    known = sorted(p.name for p in (mandu / "projects").iterdir() if p.is_dir())
    if product not in known:
        raise RunError(
            "projects/%s/ does not exist in %s. Gr0wthPilot runs only for a Product Mandu "
            "already tracks, named exactly as its folder: %s" % (product, mandu, ", ".join(known))
        )
    return mandu / "projects" / product


def journal_status(folder: Path):
    journal = gc.load_journal(folder)
    if not isinstance(journal, dict) or journal.get("gr0wthpilot_journal") != gc.JOURNAL_FORMAT:
        return None
    return journal.get("status")


def production_registry() -> Path:
    """gr0wthlab's product list in its production clone: ~/gr0wthlab, or the
    clone GR0WTHLAB_DIR names."""
    base = os.environ.get("GR0WTHLAB_DIR")
    return (Path(base).expanduser() if base else Path.home() / "gr0wthlab") / "config" / "products.json"


def registered_folder(package, product: str) -> str:
    """The folder in projects/<Product>/ a go_to_market_package's path names,
    or `gtm` when its path names none."""
    path = package.get("path") if isinstance(package, dict) else None
    parts = path.strip("/").split("/") if isinstance(path, str) else []
    if len(parts) == 3 and parts[:2] == ["projects", product] and parts[2] not in (".", ".."):
        return parts[2]
    return "gtm"


def handoff_status(registry: Path, product: str):
    """Whether the Product is handed off: (True, its live folder, why) when
    gr0wthlab's product list names a go_to_market_package for it, (False,
    None, why) when it does not, and (None, None, why) when the list cannot
    be read."""
    try:
        products = gc.read_json(registry).get("products")
    except (OSError, ValueError, AttributeError):
        products = None
    if not isinstance(products, list):
        return None, None, "gr0wthlab's product list (%s) could not be read" % registry
    for entry in products:
        if isinstance(entry, dict) and entry.get("name") == product and entry.get("go_to_market_package"):
            return (True, registered_folder(entry["go_to_market_package"], product),
                    "gr0wthlab's product list (%s) names a go_to_market_package for %s" % (registry, product))
    return False, None, "gr0wthlab's product list (%s) names no go_to_market_package for %s" % (registry, product)


def resolve_target(mandu: Path, product: str, today: dt.date, registry: Path) -> dict:
    """Decide which folder this run writes.

    A handed-off Product's live package is the folder gr0wthlab's product list
    names (`gtm/` when it names none), never written or resumed. When the list
    cannot be read, a `gtm/` holding a finished package, or one with no
    Gr0wthPilot journal, is treated as possibly live; an unfinished run in
    `gtm/` cannot have been handed off, so it still resumes. A folder holding
    an in-progress run journal is resumed unless it is live. Otherwise a new
    run writes `gtm/` when it does not exist and the Product is not handed off,
    or a dated `gtm-candidate-<date>/` beside it. Every other package folder
    is protected: never written.

    The kind is `beside-live` for any package beside a live or possibly live
    one, which cannot be handed off yet; otherwise `first-package` for `gtm/`
    and `candidate` for a dated folder.
    """
    product_dir = check_product(mandu, product)
    gtm = product_dir / "gtm"
    handed_off, registered, reason = handoff_status(registry, product)
    if handed_off:
        live = product_dir / registered
        reason += ", so %s/ is its live package" % live.relative_to(mandu)
    elif handed_off is None and gtm.exists() and journal_status(gtm) != "in-progress":
        live = gtm
        reason += ", so the existing %s/ is treated as possibly live" % gtm.relative_to(mandu)
    else:
        live = None
    folders = [gtm] if gtm.exists() else []
    folders.extend(sorted(p for p in product_dir.glob(CANDIDATE_PREFIX + "*") if p.is_dir()))
    if live is not None and live not in folders:
        folders.insert(0, live)
    in_progress = [f for f in folders if journal_status(f) == "in-progress" and f != live]
    if len(in_progress) > 1:
        raise RunError(
            "More than one in-progress Candidate Package for %s: %s. Mark the abandoned one "
            "complete or remove it before starting again."
            % (product, ", ".join(str(f.relative_to(mandu)) for f in in_progress))
        )
    if in_progress:
        target, mode = in_progress[0], "resume"
    elif not gtm.exists() and not handed_off:
        target, mode = gtm, "new"
    else:
        base = CANDIDATE_PREFIX + today.isoformat()
        target, n = product_dir / base, 2
        while target.exists() or target == live:
            target = product_dir / ("%s-%d" % (base, n))
            n += 1
        mode = "new"
    protected = [f for f in folders if f != target]
    if live is not None:
        kind = "beside-live"
    elif target == gtm:
        kind = "first-package"
    else:
        kind = "candidate"
    return {
        "product": product,
        "product_dir": str(product_dir),
        "package": str(target),
        "package_rel": str(target.relative_to(mandu)),
        "mode": mode,
        "kind": kind,
        "kind_reason": reason,
        "handoff_line": None if kind == "beside-live" else gc.handoff_line(product, target.name),
        "protected": [str(f) for f in protected],
    }


def find_repo(mandu: Path, product: str, explicit=None):
    """The Product's own repository, which a run only reads."""
    candidates = []
    if explicit:
        candidates.append(Path(explicit).expanduser())
    env = os.environ.get("GR0WTHPILOT_REPO")
    if env:
        candidates.append(Path(env).expanduser())
    home = Path.home()
    candidates.append(home / "Developer" / "FM_Private" / "firstmate-private" / "projects" / product)
    candidates.append(mandu / "projects" / product / "repo")
    for path in candidates:
        if (path / ".git").exists():
            return str(path.resolve())
    if explicit:
        raise RunError("--repo %s is not a git checkout" % explicit)
    return None


def repo_commit(repo):
    if not repo:
        return None
    try:
        out = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], stdout=subprocess.PIPE,
                             stderr=subprocess.DEVNULL, universal_newlines=True, timeout=20)
        return out.stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


def env_files(mandu: Path, product_dir: Path, repo):
    files = [mandu / ".env", product_dir / ".env"]
    if repo:
        files.extend(sorted(Path(repo).glob(".env*")))
    return [str(f) for f in files]


def start_journal(target: dict, repo, mandu: Path, now: dt.datetime) -> dict:
    package = Path(target["package"])
    package.mkdir(parents=True, exist_ok=True)
    journal = gc.load_journal(package)
    session = {"started_at": gc.iso_z(now), "repo_commit": repo_commit(repo)}
    if target["mode"] == "new":
        stamp = now.strftime("%Y%m%d-%H%M%S")
        journal = {
            "gr0wthpilot_journal": gc.JOURNAL_FORMAT,
            "product": target["product"],
            "run_id": "%s-%s" % (target["product"].lower(), stamp),
            "status": "in-progress",
            "package": target["package_rel"],
            "repo": repo,
            "started_at": gc.iso_z(now),
            "sessions": [session],
            "gates": [],
            "phase_skills_read": [],
            "workflows": [],
            "decisions": 0,
            "notes": [],
        }
    else:
        journal.setdefault("sessions", []).append(session)
        if repo and not journal.get("repo"):
            journal["repo"] = repo
    journal.update(kind=target["kind"], kind_reason=target["kind_reason"])
    gc.write_json(package / gc.JOURNAL_NAME, journal)
    return journal


def user_settings_subset():
    path = Path.home() / ".claude" / "settings.json"
    try:
        data = gc.read_json(path)
    except (OSError, ValueError):
        return {}
    out = {k: data[k] for k in COPIED_USER_KEYS if isinstance(data.get(k), str)}
    if out.get("effortLevel") not in EFFORT_LEVELS:
        out.pop("effortLevel", None)
    return out


def build_profile(cfg: dict) -> dict:
    guard = "%s %s" % (sh_quote(sys_python()), sh_quote(str(gc.SKILL_DIR / "scripts" / "guard.py")))
    config = sh_quote(cfg["config_path"])
    package, work = cfg["package"], cfg["work"]
    never_written = cfg["protected"] + [cfg["state"]]
    deny = list(DENIED_TOOLS)
    deny += ["Bash(%s)" % c for c in DENIED_BASH] + ["Bash(%s *)" % c for c in DENIED_BASH]
    deny += ["Read(**/.env)", "Read(**/.env.*)"]
    deny += ["Edit(/%s/**)" % p for p in never_written]
    profile = user_settings_subset()
    profile.update({
        "workflowSizeGuideline": WORKFLOW_SIZE_GUIDELINE,
        "autoMemoryEnabled": False,
        "permissions": {
            "defaultMode": "dontAsk",
            "disableBypassPermissionsMode": "disable",
            "disableAutoMode": "disable",
            "additionalDirectories": [work],
            "allow": ALLOWED_TOOLS + ["Edit(/%s/**)" % package, "Edit(/%s/**)" % work],
            "deny": deny,
        },
        "sandbox": {
            "enabled": True,
            "failIfUnavailable": True,
            "allowUnsandboxedCommands": False,
            "autoAllowBashIfSandboxed": True,
            "excludedCommands": ["gp-sim *", "gp-xcodebuild *", "gp-chrome *"],
            "filesystem": {"allowWrite": [work], "denyWrite": never_written},
            "network": {
                "allowedDomains": BASH_NETWORK,
                "strictAllowlist": True,
                "allowLocalBinding": True,
            },
        },
        "hooks": {
            "SessionStart": [{"hooks": [{"type": "command", "command": "%s session-start %s" % (guard, config)}]}],
            "PreToolUse": [{"matcher": "*", "hooks": [{"type": "command", "command": "%s pre %s" % (guard, config)}]}],
            "PostToolUse": [{"matcher": "*", "hooks": [{"type": "command", "command": "%s post %s" % (guard, config)}]}],
        },
    })
    return profile


def validate_profile(profile: dict) -> list:
    """Problems that would make Claude Code drop the whole profile."""
    problems = []
    for key in profile:
        if key not in PROFILE_KEYS:
            problems.append("%s is not a key the profile may carry" % key)
    if profile.get("workflowSizeGuideline", "unrestricted") not in WORKFLOW_SIZES:
        problems.append("workflowSizeGuideline must be one of %s" % ", ".join(WORKFLOW_SIZES))
    if "effortLevel" in profile and profile["effortLevel"] not in EFFORT_LEVELS:
        problems.append("effortLevel must be one of %s" % ", ".join(EFFORT_LEVELS))
    perms = profile.get("permissions", {})
    for key in perms:
        if key not in PERMISSION_KEYS:
            problems.append("permissions.%s is not a settings key" % key)
    for kind in ("allow", "deny", "ask"):
        rules = perms.get(kind, [])
        if len(set(rules)) != len(rules):
            problems.append("permissions.%s repeats a rule" % kind)
        for rule in rules:
            if not RULE_RE.match(rule):
                problems.append("permissions.%s rule %r does not match the settings schema" % (kind, rule))
    return problems


# Mandu's shared project settings load into every run (they are what makes
# Claude Code load Mandu's skills); a key here would change the run's
# permissions, so the launcher refuses to start while one is present.
PROJECT_SETTINGS_FORBIDDEN = ("permissions", "hooks", "sandbox", "enabledPlugins", "env", "apiKeyHelper",
                              "defaultMode", "mcpServers", "enabledMcpjsonServers", "enableAllProjectMcpServers")


def check_project_settings(mandu: Path) -> None:
    path = mandu / ".claude" / "settings.json"
    if not path.is_file():
        return
    try:
        data = gc.read_json(path)
    except ValueError as exc:
        raise RunError("%s is not valid JSON: %s" % (path, exc))
    found = [k for k in PROJECT_SETTINGS_FORBIDDEN if k in data]
    if found:
        raise RunError("Mandu's shared %s sets %s, which would change a Gr0wthPilot run's permissions; "
                       "move them to .claude/settings.local.json, which runs do not load"
                       % (path.relative_to(mandu), ", ".join(found)))


def claude_config_path() -> Path:
    base = os.environ.get("CLAUDE_CONFIG_DIR")
    return Path(base).expanduser() / ".claude.json" if base else Path.home() / ".claude.json"


def check_claude_consent(mandu: Path, config=None) -> None:
    """Refuse to start a run that would open on one of Claude Code's own
    consent dialogs, which would leave the run waiting on the Founder.

    Claude Code records, per folder, whether the Founder trusts it (a trusted
    folder also covers the folders inside it) and, per repository root, whether
    he approved its CLAUDE.md importing files from outside the working folder,
    as Mandu's does. The launcher reads both and never writes them.
    """
    path = Path(config) if config else claude_config_path()
    advice = ("open Claude Code once in %s (cd %s && claude), approve its prompts, quit, and run "
              "bin/gr0wthpilot again" % (mandu, mandu))
    try:
        projects = gc.read_json(path).get("projects") or {}
    except (OSError, ValueError):
        raise RunError("cannot read %s to check that %s is trusted; %s" % (path, mandu, advice))
    entry = projects.get(str(mandu)) or {}
    trusted = any((projects.get(str(p)) or {}).get("hasTrustDialogAccepted") for p in [mandu] + list(mandu.parents))
    if not trusted:
        raise RunError("Claude Code has not trusted %s yet; %s" % (mandu, advice))
    if not entry.get("hasClaudeMdExternalIncludesApproved"):
        raise RunError("Claude Code has not approved %s's CLAUDE.md imports yet; %s" % (mandu, advice))


def sys_python() -> str:
    return sys.executable or "python3"


def sh_quote(text: str) -> str:
    if re.fullmatch(r"[A-Za-z0-9_./:@%+=,-]+", text):
        return text
    return "'" + text.replace("'", "'\"'\"'") + "'"


def prepare(args) -> dict:
    mandu = Path(args.mandu).resolve()
    product = args.product
    check_project_settings(mandu)
    check_claude_consent(mandu)
    target = resolve_target(mandu, product, today_arg(args.today), production_registry())
    cache = Path(args.cache).expanduser()
    work, state = cache / product, cache / (product + ".guard")
    for folder in (work, state):
        folder.mkdir(parents=True, exist_ok=True)
    work, state = work.resolve(), state.resolve()
    # The Workflow tool runs only scripts inside the session's working folders,
    # and the skill folder is not one, so every launch copies the shipped
    # workflow scripts into the cache folder fresh.
    workflows = work / "workflows"
    workflows.mkdir(exist_ok=True)
    for script in sorted((gc.SKILL_DIR / "workflows").glob("*.js")):
        shutil.copyfile(str(script), str(workflows / script.name))
    repo = find_repo(mandu, product, args.repo)
    journal = start_journal(target, repo, mandu, gc.utc_now())
    cfg = {
        "version": 1,
        "mandu": str(mandu),
        "product": product,
        "product_dir": target["product_dir"],
        "package": str(Path(target["package"]).resolve()),
        "package_rel": target["package_rel"],
        "mode": target["mode"],
        "kind": target["kind"],
        "kind_reason": target["kind_reason"],
        "handoff_line": target["handoff_line"],
        "protected": [str(Path(p).resolve()) for p in target["protected"]],
        "repo": repo,
        "run_id": journal["run_id"],
        "work": str(work),
        "state": str(state),
        "workflows_dir": str(work / "workflows"),
        "skill_dir": str(gc.SKILL_DIR),
        "env_files": env_files(mandu, Path(target["product_dir"]), repo),
        "last30days_log": str(work / "last30days-log.jsonl"),
        "tool_log": str(state / "tool-log.jsonl"),
        "fetch_log": str(state / "fetch-log.jsonl"),
        "robots_dir": str(state / "robots"),
        "simulators": str(state / "simulators.json"),
        "config_path": str(state / "guard-config.json"),
        "profile_path": str(state / "profile.json"),
    }
    profile = build_profile(cfg)
    problems = validate_profile(profile)
    if problems:
        raise RunError("the run's permission profile would be dropped by Claude Code: " + "; ".join(problems))
    gc.write_json(Path(cfg["config_path"]), cfg)
    gc.write_json(Path(cfg["profile_path"]), profile)
    return cfg


def preflight(args) -> int:
    """Fail unless this session runs under the launcher's profile.

    The guard hook writes a receipt for any Bash command that carries a
    `GP_PREFLIGHT=<nonce>` marker. The receipt can only exist if the guard ran
    for this very command, which proves the profile's hooks are live.
    """
    config_path = args.config or os.environ.get("GR0WTHPILOT_CONFIG")
    if not config_path or not Path(config_path).is_file():
        print("BLOCKED: no Gr0wthPilot run config. Start the run with `bin/gr0wthpilot <Product>` "
              "from Mandu's root; the skill does not run in an ordinary session.")
        return 2
    cfg = gc.read_json(Path(config_path))
    nonce = os.environ.get("GP_PREFLIGHT", "")
    receipt = Path(cfg["work"]) / ("guard-receipt-%s" % nonce)
    if not nonce or not receipt.is_file():
        print("BLOCKED: the guard hook did not see this command, so the launcher's permission "
              "profile is not active in this session. Start the run with `bin/gr0wthpilot %s`."
              % cfg["product"])
        return 2
    receipt.unlink()
    pkg = Path(cfg["package"])
    journal = gc.load_journal(pkg) or {}
    print(json.dumps({
        "guard": "live",
        "product": cfg["product"],
        "package": cfg["package"],
        "package_rel": cfg["package_rel"],
        "mode": cfg.get("mode"),
        "kind": cfg.get("kind"),
        "kind_reason": cfg.get("kind_reason"),
        "handoff_line": cfg.get("handoff_line"),
        "repo": cfg.get("repo"),
        "work": cfg["work"],
        "workflows_dir": cfg.get("workflows_dir"),
        "protected": cfg.get("protected") or [],
        "run_id": journal.get("run_id"),
        "gates_passed": [g.get("id") for g in journal.get("gates", [])],
    }, indent=2))
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd")
    p = sub.add_parser("prepare")
    p.add_argument("--mandu", required=True)
    p.add_argument("--product", required=True)
    p.add_argument("--cache", required=True)
    p.add_argument("--repo")
    p.add_argument("--today")
    f = sub.add_parser("preflight")
    f.add_argument("--config")
    args = parser.parse_args(argv)
    try:
        if args.cmd == "prepare":
            print(json.dumps(prepare(args), indent=2))
            return 0
        if args.cmd == "preflight":
            return preflight(args)
    except RunError as exc:
        print("gr0wthpilot: %s" % exc, file=sys.stderr)
        return 2
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
