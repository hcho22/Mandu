#!/usr/bin/env python3
"""Gr0wthPilot's guard: the hook every tool call of a run passes through.

The launcher's permission profile runs it for every tool call, in the main
session and in every subagent and Workflow agent:

  guard.py session-start CONFIG   tells the session which run it is
  guard.py pre CONFIG             allows or denies a tool call (fails closed)
  guard.py post CONFIG            logs the call; logs each WebFetch's result

It is the first of three layers that keep a run from publishing, spending, or
writing outside its Candidate Package: this guard, the profile's permission
rules, and the macOS sandbox the profile turns on for every shell command.
What each layer covers, and what none of them can, is in
references/guardrails.md.
"""

from __future__ import annotations

import json
import os
import re
import shlex
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gp_common as gc  # noqa: E402

ROBOTS_AGENT = "Claude-User"
ROBOTS_TTL_SECONDS = 6 * 3600

WRAPPERS = {"gp-sim", "gp-xcodebuild", "gp-chrome"}

DENIED_TOOLS = {
    "Artifact", "ArtifactComments", "ArtifactData", "RemoteTrigger", "PushNotification",
    "SendMessage", "CronCreate", "CronDelete", "ScheduleWakeup", "EnterWorktree",
    "ExitWorktree", "DesignSync", "NotebookEdit",
}
ALLOWED_SKILLS = {"gr0wthpilot", "customer-research", "influencer-marketing"}
WRITE_TOOLS = {"Edit", "Write", "MultiEdit"}

# Programs a run never runs: they publish, deploy, upload, reach a remote host,
# send mail, read the keychain, start another agent, or drive the Founder's
# signed-in browser or apps.
DENIED_PROGRAMS = {
    "gh", "hub", "glab", "wrangler", "vercel", "netlify", "firebase", "surge", "heroku",
    "fly", "flyctl", "railway", "aws", "gcloud", "gsutil", "az", "doctl", "rclone",
    "s3cmd", "scp", "sftp", "ftp", "ssh", "rsync", "nc", "ncat", "netcat", "telnet", "socat",
    "sendmail", "mail", "mailx", "osascript", "open", "security", "twine", "pod",
    "fastlane", "altool", "notarytool", "iTMSTransporter", "xcrun", "xcodebuild",
    "chrome-devtools-axi", "lavish-axi", "gh-axi", "claude", "codex", "opencode",
    "no-mistakes", "treehouse", "docker", "podman", "pkill", "killall", "launchctl",
    "crontab", "at", "sudo", "su", "printenv", "Google Chrome", "chromium",
    "safaridriver", "shortcuts", "automator", "pbcopy",
}
PROGRAM_HINTS = {
    "xcrun": "use `gp-sim` for simulators; nothing else in xcrun is needed",
    "xcodebuild": "use `gp-xcodebuild`, which builds a copy of the Product for the simulator",
    "Google Chrome": "use `gp-chrome`, which runs headless Chrome on a throwaway profile",
    "chromium": "use `gp-chrome`",
    "chrome-devtools-axi": "it drives the Founder's signed-in Chrome; use `gp-chrome`",
    "printenv": "it can print secret values; list `.env` key names with scripts/env_keys.py",
    "open": "nothing is opened in the Founder's apps or browser during a run",
}
# git subcommands that only read.
GIT_READ = {
    "status", "log", "diff", "show", "archive", "ls-files", "ls-tree", "rev-parse",
    "describe", "blame", "cat-file", "grep", "shortlog", "for-each-ref", "rev-list",
    "show-ref", "name-rev", "merge-base", "version", "help",
}
NPM_DENIED = {"publish", "unpublish", "login", "logout", "adduser", "add-user", "token",
              "owner", "deprecate", "dist-tag", "access", "team", "org", "star", "hook"}
WRAPPER_PROGRAMS = {"env", "nohup", "time", "command", "exec", "nice", "timeout",
                    "caffeinate", "stdbuf", "xargs"}
SHELLS = {"bash", "sh", "zsh", "dash", "ksh"}
INTERPRETERS = re.compile(r"^(python(\d(\.\d+)?)?|node|ruby|perl|osascript)$")
READERS = {"cat", "less", "more", "head", "tail", "bat", "grep", "egrep", "fgrep", "rg",
           "sed", "awk", "strings", "xxd", "od", "hexdump", "cut", "sort", "uniq", "tr",
           "base64", "diff", "cmp", "nl", "paste", "jq", "plutil"}
ENV_FILE_RE = re.compile(r"(^|/)\.env($|\.)")

CURL_SEND_FLAGS = {"-d", "--data", "--data-raw", "--data-binary", "--data-urlencode",
                   "--data-ascii", "-F", "--form", "--form-string", "-T", "--upload-file",
                   "--json", "-K", "--config", "-u", "--user", "--oauth2-bearer", "--mail-from",
                   "--mail-rcpt"}
WGET_SEND_FLAGS = {"--post-data", "--post-file", "--body-data", "--body-file", "--method",
                   "--ftp-user", "--ftp-password", "--http-user", "--http-password"}

# Code that sends: checked in inline `python -c` / `node -e` code, in scripts
# the run executes, and in code files the run writes. SPAWN_RE below covers
# code that runs a program.
NET_SEND_PATTERNS = [
    r"\bsmtplib\b", r"\bftplib\b", r"\bparamiko\b", r"\bboto3\b", r"\bpoplib\b",
    r"\brequests\.(post|put|patch|delete)\b", r"\bhttpx\.(post|put|patch|delete)\b",
    r"method\s*[=:]\s*['\"](POST|PUT|PATCH|DELETE)['\"]",
    r"\.request\(\s*['\"](POST|PUT|PATCH|DELETE)['\"]",
    r"\bsendBeacon\b", r"\bXMLHttpRequest\b", r"\bsocket\.socket\(",
    r"urlopen\([^)\n]*data\s*=", r"Request\([^)\n]*data\s*=",
    r"last30days\.py[^\n]*(--publish-html|\bsetup\b|--github)",
]
# A call that runs a program, with the program as its first string argument or
# the first element of the argv list it is passed, and the element after it:
# Python's subprocess and os.exec*/spawn*/system, Node's child_process, Bun,
# Deno, and system() in Ruby and Perl.
SPAWN_RE = re.compile(
    r"(?:\b(?:spawn|spawnSync|execFile|execFileSync|execSync|execa|execaSync|Popen|check_output|"
    r"check_call|getoutput|getstatusoutput|posix_spawnp?|exec[lv]p?e?|spawn[lv]p?e?)"
    r"|\b(?:subprocess|os|child_process|cp|Bun|Deno)\s*\.\s*(?:run|call|system|popen|exec|fork|spawn|Command)"
    r"|(?<![\w.])(?:system|exec))"
    r"\s*\(\s*\[?\s*(['\"`])([^'\"`\n]+)\1(?:\s*,\s*\[?\s*(['\"`])([^'\"`\n]*)\3)?")
CODE_SUFFIXES = {".py", ".sh", ".bash", ".zsh", ".js", ".mjs", ".cjs", ".ts", ".rb", ".pl",
                 ".command"}


class Deny(Exception):
    pass


# ---------------------------------------------------------------------------
# Config and logs

def load_config(path):
    return gc.read_json(Path(path))


def append_log(path, entry):
    try:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "a", encoding="utf-8") as handle:
            handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except OSError:
        pass


def secret_values(cfg):
    values = set()
    for name in cfg.get("env_files") or []:
        try:
            text = Path(name).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            _, _, value = line.partition("=")
            value = value.strip().strip("'\"")
            if len(value) >= 8:
                values.add(value)
    return values


def redact(text, secrets):
    for value in secrets:
        text = text.replace(value, "<redacted>")
    return text


# ---------------------------------------------------------------------------
# robots.txt (RFC 9309), for every page WebFetch reads

def parse_robots(body):
    groups, agents, rules, last_was_agent = [], [], [], False
    for raw in body.splitlines():
        line = raw.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip().lower(), value.strip()
        if key == "user-agent":
            if not last_was_agent and (agents or rules):
                groups.append((agents, rules))
                agents, rules = [], []
            agents.append(value.lower())
            last_was_agent = True
        elif key in ("allow", "disallow"):
            rules.append((key, value))
            last_was_agent = False
        else:
            last_was_agent = False
    if agents or rules:
        groups.append((agents, rules))
    return groups


def _pattern_matches(pattern, path):
    anchored = pattern.endswith("$")
    if anchored:
        pattern = pattern[:-1]
    regex = "^" + ".*".join(re.escape(part) for part in pattern.split("*"))
    if anchored:
        regex += "$"
    return re.match(regex, path) is not None


def robots_allows(body, url, agent=ROBOTS_AGENT):
    groups = parse_robots(body)
    token = agent.lower()
    chosen = [rules for agents, rules in groups if any(a != "*" and a in token for a in agents)]
    if not chosen:
        chosen = [rules for agents, rules in groups if "*" in agents]
    rules = [r for group in chosen for r in group]
    parsed = urllib.parse.urlsplit(url)
    path = parsed.path or "/"
    if parsed.query:
        path += "?" + parsed.query
    path = urllib.parse.unquote(path)
    best_len, verdict = -1, True
    for kind, pattern in rules:
        if kind == "disallow" and pattern == "":
            continue
        decoded = urllib.parse.unquote(pattern)
        if _pattern_matches(decoded, path):
            length = len(decoded)
            if length > best_len or (length == best_len and kind == "allow"):
                best_len, verdict = length, kind == "allow"
    return verdict


def robots_opener():
    """An opener that connects directly, with the system's CA bundle.

    The hook runs outside the sandbox but may inherit the sandbox's proxy
    variables, which refuse every host not on the shell's allowlist; and the
    Mac's default python3 (3.7 from python.org) ships no CA bundle of its own.
    """
    import ssl
    cafile = "/etc/ssl/cert.pem" if Path("/etc/ssl/cert.pem").is_file() else None
    context = ssl.create_default_context(cafile=cafile)
    return urllib.request.build_opener(urllib.request.ProxyHandler({}),
                                       urllib.request.HTTPSHandler(context=context))


def fetch_robots(cfg, scheme, host):
    """Return (status, body) for the host's robots.txt, cached for six hours."""
    import time
    cache_dir = Path(cfg["robots_dir"])
    cache = cache_dir / (re.sub(r"[^A-Za-z0-9.-]", "_", host) + ".json")
    try:
        cached = gc.read_json(cache)
        if time.time() - cached["at"] < ROBOTS_TTL_SECONDS:
            return cached["status"], cached["body"]
    except (OSError, ValueError, KeyError):
        pass
    url = "%s://%s/robots.txt" % (scheme, host)
    request = urllib.request.Request(url, headers={"User-Agent": ROBOTS_AGENT})
    try:
        with robots_opener().open(request, timeout=15) as response:
            status, body = response.status, response.read(512 * 1024).decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        status, body = exc.code, ""
    except (urllib.error.URLError, OSError, ValueError):
        status, body = 0, ""
    if status:
        gc.write_json(cache, {"at": time.time(), "status": status, "body": body})
    return status, body


def check_webfetch(cfg, url):
    parsed = urllib.parse.urlsplit(url or "")
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise Deny("WebFetch reads only http(s) pages")
    host = parsed.netloc.lower()
    status, body = fetch_robots(cfg, "https", host)
    if status in (401, 403):
        raise Deny("https://%s/robots.txt refuses automated readers (HTTP %d). Do not read this "
                   "site another way; use another source or drop the claim." % (host, status))
    if status == 0 or status >= 500:
        raise Deny("https://%s/robots.txt could not be read (%s), so the site's rules for "
                   "automated readers are unknown. Use another source or drop the claim."
                   % (host, status or "unreachable"))
    if status == 200 and not robots_allows(body, url):
        raise Deny("https://%s/robots.txt disallows %s for automated readers. Do not read it "
                   "through another route; use another source or drop the claim. (Reddit is "
                   "read only through gp-last30days.)" % (host, url))


# ---------------------------------------------------------------------------
# Shell commands

HEREDOC_RE = re.compile(r"<<(-?)\s*(?:'([^'\n]+)'|\"([^\"\n]+)\"|\\?([A-Za-z_][A-Za-z0-9_]*))")


def split_top_level(command):
    """Split a shell command into simple commands at top-level operators, and
    pull out the contents of $(...), <(...), and backticks as their own
    commands. A heredoc's body is not shell text: it is kept beside the
    command it feeds, so a command that runs it (a shell or an interpreter)
    can be checked against it. Returns ([(command, heredoc body or None)],
    has_redirect, is_compound). Raises Deny on unbalanced quotes."""
    parts, nested, current = [], [], []
    bodies, pending = [], []
    i, n = 0, len(command)
    quote = None
    redirect = False

    def finish():
        text = "".join(current).strip()
        if text:
            parts.append(text)
            bodies.append(None)
        return []

    while i < n:
        ch = command[i]
        if quote:
            current.append(ch)
            if ch == quote:
                quote = None
            elif ch == "\\" and quote == '"' and i + 1 < n:
                current.append(command[i + 1])
                i += 1
            elif quote == '"' and command.startswith("$(", i):
                inner, end = _balanced(command, i + 2)
                nested.append(inner)
                current.append(command[i + 1:end + 1])
                i = end
            i += 1
            continue
        if command.startswith("<<", i) and not command.startswith("<<<", i):
            m = HEREDOC_RE.match(command, i)
            if m:
                pending.append((m.group(1) == "-", m.group(2) or m.group(3) or m.group(4)))
                current.append(m.group(0))
                redirect = True
                i = m.end()
                continue
        if ch == "\n" and pending:
            current = finish()
            owner = len(parts) - 1
            i += 1
            for strip_tabs, delimiter in pending:
                lines = []
                while i <= n:
                    end = command.find("\n", i)
                    line = command[i:] if end == -1 else command[i:end]
                    i = n + 1 if end == -1 else end + 1
                    if (line.lstrip("\t") if strip_tabs else line) == delimiter:
                        break
                    lines.append(line)
                if owner >= 0:
                    body = "\n".join(lines)
                    bodies[owner] = body if bodies[owner] is None else bodies[owner] + "\n" + body
            pending = []
            continue
        if ch in ("'", '"'):
            quote = ch
            current.append(ch)
        elif ch == "\\" and i + 1 < n:
            current.append(command[i:i + 2])
            i += 1
        elif command.startswith("$(", i) or command.startswith("<(", i) or command.startswith(">(", i):
            inner, end = _balanced(command, i + 2)
            nested.append(inner)
            current.append("__SUBST__")
            i = end
        elif ch == "`":
            end = command.find("`", i + 1)
            if end == -1:
                raise Deny("unbalanced backtick in the command")
            nested.append(command[i + 1:end])
            current.append("__SUBST__")
            i = end
        elif command.startswith("&&", i) or command.startswith("||", i):
            current = finish()
            i += 1
        elif ch in ";|&\n(){}":
            if ch in "&|" and current and current[-1].endswith(">"):
                current.append(ch)
            else:
                current = finish()
        else:
            if ch in "<>":
                redirect = True
            current.append(ch)
        i += 1
    if quote:
        raise Deny("unbalanced quotes in the command")
    finish()
    simple = list(zip(parts, bodies))
    for inner in nested:
        simple.extend(split_top_level(inner)[0])
    return simple, redirect, len(simple) > 1 or bool(nested)


def _balanced(text, start):
    depth, i, quote = 1, start, None
    while i < len(text):
        ch = text[i]
        if quote:
            if ch == quote:
                quote = None
        elif ch in ("'", '"'):
            quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return text[start:i], i
        i += 1
    raise Deny("unbalanced parentheses in the command")


def tokens_of(simple):
    try:
        return shlex.split(simple, comments=True)
    except ValueError:
        raise Deny("the command could not be parsed; write it more simply")


def strip_prefix(tokens):
    """Drop env assignments, redirections, and wrapper programs before the real program."""
    out = list(tokens)
    while out:
        tok = out[0]
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", tok):
            out.pop(0)
            continue
        if re.fullmatch(r"\d*[<>]+&?\d*", tok):
            out = out[2:] if len(out) > 1 and not re.fullmatch(r"\d*[<>]+&\d+", tok) else out[1:]
            continue
        name = os.path.basename(tok)
        if name in WRAPPER_PROGRAMS:
            out.pop(0)
            while out and (out[0].startswith("-") or re.fullmatch(r"\d+[smhd]?", out[0])
                           or re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", out[0])):
                out.pop(0)
            continue
        break
    return out


def program_name(tok):
    if tok.endswith("/Google Chrome") or tok == "Google Chrome":
        return "Google Chrome"
    return os.path.basename(tok)


def spawned_programs(text):
    """Yield (program, the argument after it) for each call in code that runs a
    program, the program compared by its basename."""
    for m in SPAWN_RE.finditer(text):
        first = m.group(2).strip()
        if program_name(first) == "Google Chrome":
            yield "Google Chrome", None
            continue
        words = first.split()
        if words:
            yield program_name(words[0]), words[1] if len(words) > 1 else m.group(4)


def check_code_text(text, where):
    for pattern in NET_SEND_PATTERNS:
        if re.search(pattern, text):
            raise Deny("%s contains code that sends data or runs a denied program (%s). A run only "
                       "reads; it publishes, uploads, and sends nothing." % (where, pattern))
    for prog, arg in spawned_programs(text):
        if prog in DENIED_PROGRAMS or (prog == "git" and arg and not arg.startswith("-") and arg not in GIT_READ):
            raise Deny("%s contains code that runs `%s%s`, which a run never runs. A run only reads; it "
                       "publishes, uploads, and sends nothing." % (where, prog, " " + arg if prog == "git" else ""))


def check_script_file(path, cfg):
    p = Path(path)
    if not p.is_absolute():
        p = Path(cfg["package"]) / p
    # The skill's own scripts list the denied programs by name, and a run can
    # never write there, so they are not scanned.
    if cfg.get("skill_dir") and under(p, cfg["skill_dir"]):
        return
    try:
        if p.is_file() and p.stat().st_size <= 2 * 1024 * 1024:
            check_code_text(p.read_text(encoding="utf-8", errors="replace"), "Script %s" % p.name)
    except OSError:
        pass


def check_simple(tokens, cfg, depth=0):
    if tokens and os.path.basename(tokens[0]) == "env" and all(
            t.startswith("-") or re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", t) for t in tokens[1:]):
        raise Deny("printing the environment can print secret values")
    tokens = strip_prefix(tokens)
    if not tokens or tokens[0] == "__SUBST__":
        return
    prog = program_name(tokens[0])
    args = tokens[1:]
    if prog in DENIED_PROGRAMS:
        hint = PROGRAM_HINTS.get(prog)
        raise Deny("`%s` is not available in a Gr0wthPilot run%s." % (prog, "; " + hint if hint else ""))
    if prog in SHELLS and "-c" in args:
        inner = args[args.index("-c") + 1] if args.index("-c") + 1 < len(args) else ""
        check_command(inner, cfg, depth + 1)
        return
    if prog == "eval":
        check_command(" ".join(args), cfg, depth + 1)
        return
    if prog == "find" and ("-exec" in args or "-execdir" in args or "-ok" in args):
        for flag in ("-exec", "-execdir", "-ok"):
            if flag in args:
                rest = args[args.index(flag) + 1:]
                end = next((i for i, t in enumerate(rest) if t in (";", "+", "\\;")), len(rest))
                check_simple(rest[:end], cfg, depth + 1)
    if prog == "git":
        sub = next((a for a in args if not a.startswith("-") and a not in _git_option_values(args)), None)
        if sub not in GIT_READ:
            raise Deny("`git %s` is not available in a run; a run only reads git history "
                       "(allowed: %s)." % (sub or "", ", ".join(sorted(GIT_READ))))
    if prog in ("npm", "pnpm", "yarn", "bun", "npx", "bunx"):
        if any(a in NPM_DENIED for a in args):
            raise Deny("`%s %s` publishes or signs in; a run does neither." % (prog, " ".join(args[:2])))
    # A package runner runs another program: check that program.
    runner_args = None
    if prog in ("npx", "bunx", "uvx", "pipx") or (prog in ("npm", "pnpm", "yarn") and args[:1] in (["exec"], ["dlx"], ["x"])):
        runner_args = args[1:] if prog in ("npm", "pnpm", "yarn") or (prog == "pipx" and args[:1] == ["run"]) else args
        while runner_args and runner_args[0].startswith("-"):
            runner_args = runner_args[1:]
        if runner_args:
            name = re.sub(r"@[^/]*$", "", runner_args[0].split("/")[-1]) if not runner_args[0].startswith("@") \
                else runner_args[0].split("/")[-1].split("@")[0]
            check_simple([name] + runner_args[1:], cfg, depth + 1)
    if prog == "curl":
        flags = {a.split("=", 1)[0] for a in args if a.startswith("-")}
        bad = flags & CURL_SEND_FLAGS
        method = _flag_value(args, ("-X", "--request"))
        if bad or (method and method.upper() not in ("GET", "HEAD")):
            raise Deny("curl may only read (GET or HEAD); %s sends data." % ", ".join(sorted(bad) or [method]))
    if prog == "wget":
        flags = {a.split("=", 1)[0] for a in args if a.startswith("-")}
        if flags & WGET_SEND_FLAGS:
            raise Deny("wget may only read; %s sends data." % ", ".join(sorted(flags & WGET_SEND_FLAGS)))
    if INTERPRETERS.match(prog):
        if "-c" in args or "-e" in args or "--eval" in args:
            flag = "-c" if "-c" in args else ("-e" if "-e" in args else "--eval")
            idx = args.index(flag) + 1
            if idx < len(args):
                check_code_text(args[idx], "Inline %s code" % prog)
        else:
            script = next((a for a in args if not a.startswith("-")), None)
            if script:
                check_script_file(script, cfg)
    if any("last30days.py" in a or "last30days/scripts" in a for a in tokens):
        raise Deny("run last30days through `gp-last30days`, which keeps its sign-up, publishing, "
                   "and cookie-reading paths off")
    if prog in READERS or prog in ("source", "."):
        for a in args:
            if ENV_FILE_RE.search(a) and prog not in ("source", "."):
                raise Deny("reading a .env file can print secret values; list its key names with "
                           "`python3 %s/scripts/env_keys.py`" % cfg["skill_dir"])
    if prog in ("env", "set", "export", "declare") and not args:
        raise Deny("printing the environment can print secret values")
    if prog in ("kill",):
        raise Deny("a run does not signal processes; stop a background task with TaskStop")


def _git_option_values(args):
    values = set()
    for i, a in enumerate(args[:-1]):
        if a in ("-C", "-c", "--git-dir", "--work-tree", "--namespace"):
            values.add(args[i + 1])
    return values


def _flag_value(args, names):
    for i, a in enumerate(args):
        for name in names:
            if a == name and i + 1 < len(args):
                return args[i + 1]
            if a.startswith(name + "="):
                return a.split("=", 1)[1]
            if name.startswith("-") and not name.startswith("--") and a.startswith(name) and len(a) > len(name):
                return a[len(name):]
    return None


def check_command(command, cfg, depth=0):
    if depth > 4:
        raise Deny("the command nests shells too deeply to check")
    simple, redirect, compound = split_top_level(command)
    for part, body in simple:
        tokens = tokens_of(part)
        stripped = strip_prefix(tokens)
        name = program_name(stripped[0]) if stripped else ""
        if name in WRAPPERS and (compound or redirect or depth):
            raise Deny("run `%s` on its own: no pipes, chains, redirections, or subshells, so it "
                       "runs outside the sandbox under its own rules" % name)
        check_simple(tokens, cfg, depth)
        if body is not None and name:
            if name in SHELLS or name in ("eval", "source", "."):
                check_command(body, cfg, depth + 1)
            elif INTERPRETERS.match(name):
                check_code_text(body, "Heredoc %s code" % name)


# ---------------------------------------------------------------------------
# Tool calls

def under(path, root):
    try:
        Path(path).resolve().relative_to(Path(root).resolve())
        return True
    except ValueError:
        return False


def check_write(cfg, tool_input, secrets):
    path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
    if not path:
        raise Deny("no file path given")
    for protected in cfg.get("protected") or []:
        if under(path, protected):
            raise Deny("%s is a package this run must never write; this run writes only %s"
                       % (protected, cfg["package_rel"]))
    if not (under(path, cfg["package"]) or under(path, cfg["work"])):
        raise Deny("a run writes only inside its Candidate Package (%s) and its cache folder (%s)"
                   % (cfg["package"], cfg["work"]))
    content = tool_input.get("content")
    if content is None:
        content = tool_input.get("new_string") or ""
        for edit in tool_input.get("edits") or []:
            content += "\n" + (edit.get("new_string") or "")
    for value in secrets:
        if value in content:
            raise Deny("the content holds a secret value from a .env file; never copy a key")
    if Path(path).suffix.lower() in CODE_SUFFIXES:
        check_code_text(content, "File %s" % Path(path).name)


def check_read(cfg, tool_input):
    path = tool_input.get("file_path") or tool_input.get("path") or ""
    if ENV_FILE_RE.search(path):
        raise Deny("reading a .env file can print secret values; list its key names with "
                   "`python3 %s/scripts/env_keys.py`" % cfg["skill_dir"])


def phase_skill_of(cfg, tool, tool_input):
    if tool != "Read":
        return None
    path = tool_input.get("file_path") or ""
    m = re.search(r"/(marketingskills/[^/]+|skills/(?:customer-research|influencer-marketing))/SKILL\.md$", path)
    return m.group(1).split("/")[-1] if m else None


def decide(cfg, data, secrets):
    tool = data.get("tool_name") or ""
    tool_input = data.get("tool_input") or {}
    if tool == "AskUserQuestion":
        raise Deny("Gr0wthPilot never asks the Founder anything. Decide, log it [DECIDED BY AGENT] "
                   "with the rejected alternative in decisions-log.md, and continue.")
    if tool in DENIED_TOOLS or tool.startswith("mcp__"):
        raise Deny("`%s` is not available in a Gr0wthPilot run: it reaches outside the Mac or "
                   "schedules work." % tool)
    if tool == "Skill":
        name = (tool_input.get("skill") or tool_input.get("command") or "").lstrip("/")
        if name.split(":")[-1] not in ALLOWED_SKILLS:
            raise Deny("only the gr0wthpilot, customer-research, and influencer-marketing skills "
                       "run here; read phase skills from gr0wthpilot/marketingskills/ by path")
    if tool == "Agent" and tool_input.get("isolation") == "worktree":
        raise Deny("worktree isolation writes outside the Candidate Package")
    if tool == "Workflow":
        script = tool_input.get("script") or ""
        path = tool_input.get("scriptPath")
        if path:
            try:
                script = Path(path).read_text(encoding="utf-8")
            except OSError:
                script = ""
        if re.search(r"isolation\s*:\s*['\"]worktree['\"]", script):
            raise Deny("worktree isolation writes outside the Candidate Package")
    if tool == "WebFetch":
        check_webfetch(cfg, tool_input.get("url"))
    if tool == "Bash":
        command = tool_input.get("command") or ""
        for value in secrets:
            if value in command:
                raise Deny("the command holds a secret value from a .env file")
        if tool_input.get("dangerouslyDisableSandbox"):
            raise Deny("every command in a run stays inside the sandbox")
        check_command(command, cfg)
        m = re.search(r"\bGP_PREFLIGHT=([A-Za-z0-9]{8,64})\b", command)
        if m:
            receipt = Path(cfg["work"]) / ("guard-receipt-%s" % m.group(1))
            receipt.write_text("seen\n", encoding="utf-8")
    if tool in WRITE_TOOLS:
        check_write(cfg, tool_input, secrets)
    if tool in ("Read", "Grep", "Glob"):
        check_read(cfg, tool_input)


def summarize(tool, tool_input):
    if tool == "Bash":
        return tool_input.get("command", "")[:400]
    if tool in WRITE_TOOLS or tool == "Read":
        return tool_input.get("file_path", "")
    if tool == "WebFetch":
        return tool_input.get("url", "")
    if tool == "Workflow":
        script = tool_input.get("script") or ""
        m = re.search(r"name\s*:\s*['\"]([^'\"]+)['\"]", script)
        return tool_input.get("scriptPath") or (m.group(1) if m else "inline")
    if tool == "Skill":
        return tool_input.get("skill") or tool_input.get("command") or ""
    if tool == "Agent":
        return (tool_input.get("description") or "")[:200]
    return json.dumps(tool_input)[:200]


def run_pre(cfg, data):
    secrets = secret_values(cfg)
    tool = data.get("tool_name") or ""
    tool_input = data.get("tool_input") or {}
    entry = {
        "at": gc.iso_z(gc.utc_now()), "event": "pre", "tool": tool,
        "agent_id": data.get("agent_id"), "agent_type": data.get("agent_type"),
        "input": redact(summarize(tool, tool_input), secrets),
    }
    skill = phase_skill_of(cfg, tool, tool_input)
    if skill:
        entry["phase_skill"] = skill
    try:
        decide(cfg, data, secrets)
    except Deny as exc:
        entry.update(decision="deny", reason=str(exc))
        append_log(cfg["tool_log"], entry)
        return {"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                       "permissionDecision": "deny",
                                       "permissionDecisionReason": "Gr0wthPilot guard: " + str(exc)}}
    entry["decision"] = "allow"
    append_log(cfg["tool_log"], entry)
    return None


def run_post(cfg, data):
    tool = data.get("tool_name") or ""
    tool_input = data.get("tool_input") or {}
    response = data.get("tool_response")
    now = gc.iso_z(gc.utc_now())
    if tool == "WebFetch":
        record = {"at": now, "url": tool_input.get("url"), "agent_id": data.get("agent_id")}
        if isinstance(response, dict):
            record.update(code=response.get("code"), bytes=response.get("bytes"),
                          redirect=bool(re.search(r"redirect", str(response.get("result", ""))[:300], re.I)))
        append_log(cfg["fetch_log"], record)
    append_log(cfg["tool_log"], {"at": now, "event": "post", "tool": tool,
                                 "agent_id": data.get("agent_id")})


def run_session_start(cfg, data):
    journal = gc.load_journal(Path(cfg["package"])) or {}
    passed = [g.get("id") for g in journal.get("gates", [])]
    lines = [
        "Gr0wthPilot run for %s, under the launcher's guarded profile." % cfg["product"],
        "Candidate Package (the only place this run writes, besides its cache folder %s): %s"
        % (cfg["work"], cfg["package"]),
        "Run journal: %s/%s; gates passed so far: %s." % (cfg["package"], gc.JOURNAL_NAME,
                                                          ", ".join(passed) or "none"),
        "Protected, never written: %s." % (", ".join(cfg.get("protected") or []) or "none"),
        "Package kind: %s, because %s." % (cfg.get("kind"), cfg.get("kind_reason")),
        "Handoff line for the recap and the last message: %s." % (
            cfg.get("handoff_line") or "none; a package beside a live one cannot be handed off yet"),
        "Product repository, read only: %s." % (cfg.get("repo") or "not found"),
        "Run the Workflow scripts from %s (fresh copies of the skill's workflows/)." % cfg.get("workflows_dir"),
        "Put scratch files in %s/scratch, not in Claude Code's scratchpad, which this run cannot write."
        % cfg["work"],
    ]
    append_log(cfg["tool_log"], {"at": gc.iso_z(gc.utc_now()), "event": "session-start",
                                 "source": data.get("source")})
    return {"hookSpecificOutput": {"hookEventName": "SessionStart",
                                   "additionalContext": "\n".join(lines)}}


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) != 2 or argv[0] not in ("pre", "post", "session-start"):
        print("usage: guard.py pre|post|session-start CONFIG", file=sys.stderr)
        return 2
    mode, config = argv
    try:
        data = json.load(sys.stdin)
    except ValueError:
        data = {}
    try:
        cfg = load_config(config)
        if mode == "pre":
            out = run_pre(cfg, data)
        elif mode == "post":
            out = run_post(cfg, data)
        else:
            out = run_session_start(cfg, data)
    except Exception as exc:  # fail closed for tool calls, open for logging
        if mode != "pre":
            return 0
        out = {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                      "permissionDecisionReason": "Gr0wthPilot guard error, so the "
                                      "call is refused: %s: %s" % (type(exc).__name__, exc)}}
    if out:
        print(json.dumps(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
