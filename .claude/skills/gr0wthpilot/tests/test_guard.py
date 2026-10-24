"""Tests for the guard, the launcher's preparation, and the tool wrappers'
rules: the parts that keep "publish nothing, spend nothing, write only the
Candidate Package" true.

Run from Mandu's root: python3 -m unittest discover -s .claude/skills/gr0wthpilot/tests
"""

from __future__ import annotations

import datetime as dt
import importlib.machinery
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path

import fixtures

import gp_common as gc
import gp_run
import guard


def load_wrapper(name):
    loader = importlib.machinery.SourceFileLoader(name.replace("-", "_"), str(fixtures.BIN / name))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


def make_mandu(products=("Immerse",)):
    root = Path(tempfile.mkdtemp(prefix="gp-mandu-"))
    for p in products:
        (root / "projects" / p).mkdir(parents=True)
    return root


def config(tmp=None):
    tmp = Path(tmp or tempfile.mkdtemp(prefix="gp-cfg-"))
    pkg = tmp / "projects" / "Immerse" / "gtm"
    pkg.mkdir(parents=True)
    live = tmp / "projects" / "RepToday" / "gtm"
    live.mkdir(parents=True)
    work = tmp / "work"
    work.mkdir()
    env = tmp / "repo.env"
    env.write_text("OPENAI_API_KEY=sk-test-supersecret-123456\nSHORT=abc\n")
    robots = work / "robots"
    robots.mkdir()
    for host, body in (("allowed.example.org", "User-agent: *\nDisallow: /private/\n"),
                       ("www.reddit.com", "User-agent: *\nDisallow: /\n")):
        (robots / (host + ".json")).write_text(json.dumps({"at": 9e12, "status": 200, "body": body}))
    (robots / "blocked.example.org.json").write_text(json.dumps({"at": 9e12, "status": 403, "body": ""}))
    return {
        "product": "Immerse", "package": str(pkg), "package_rel": "projects/Immerse/gtm", "work": str(work),
        "protected": [str(live)], "skill_dir": str(fixtures.SCRIPTS.parent), "env_files": [str(env)],
        "tool_log": str(work / "tool-log.jsonl"), "fetch_log": str(work / "fetch-log.jsonl"),
        "robots_dir": str(robots), "simulators": str(work / "simulators.json"), "repo": None,
    }


class GuardTest(unittest.TestCase):
    def setUp(self):
        self.cfg = config()

    def decide(self, tool, **tool_input):
        return guard.run_pre(self.cfg, {"tool_name": tool, "tool_input": tool_input})

    def denied(self, tool, **tool_input):
        out = self.decide(tool, **tool_input)
        return bool(out) and out["hookSpecificOutput"]["permissionDecision"] == "deny"

    def bash_denied(self, command):
        return self.denied("Bash", command=command)

    def test_publishing_commands_are_denied(self):
        for command in ("git push origin main", "git remote add x y", "git commit -m x", "gh pr create",
                        "wrangler pages deploy .", "vercel --prod", "netlify deploy", "firebase deploy",
                        "npm publish", "npx wrangler deploy", "scp a b:", "rsync -a . host:/x", "ssh host",
                        "open https://example.com", "osascript -e 'x'", "security find-generic-password",
                        "claude -p hi", "xcrun simctl list", "xcodebuild build", "chrome-devtools-axi open x",
                        "printenv", "env", "pkill -f x", "/usr/bin/git push", "sudo ls"):
            self.assertTrue(self.bash_denied(command), command)

    def test_publishing_hidden_in_compound_and_nested_commands(self):
        for command in ("ls && git push", "echo ok; gh repo view", "cat x | wrangler deploy",
                        "bash -c 'git push origin main'", "sh -c \"gh api x\"", "echo $(gh auth token)",
                        "echo `git push`", "env FOO=1 git push", "nohup vercel &", "timeout 5 gh pr list",
                        "find . -exec gh api {} \\;", "eval 'git push'", "(cd x && git push)",
                        "FOO=1 BAR=2 netlify deploy"):
            self.assertTrue(self.bash_denied(command), command)

    def test_uploads_are_denied_and_reads_allowed(self):
        for command in ("curl -X POST https://x.example", "curl -d a=b https://x.example", "curl -F f=@a https://x",
                        "curl --data-binary @f https://x", "curl -T f https://x", "curl --json '{}' https://x",
                        "wget --post-data a=b https://x", "curl -XPUT https://x"):
            self.assertTrue(self.bash_denied(command), command)
        for command in ("curl -sS https://example.com -o out.html", "curl -I https://example.com",
                        "git -C /repo log --oneline -5", "git -C /repo archive HEAD", "ls -la", "python3 -c 'print(1)'",
                        "ffmpeg -i a.mp4 b.png", "gp-sim list", "gp-chrome screenshot a.html b.png 390x844",
                        "gp-last30days film camera --out 01-research/last30days"):
            self.assertFalse(self.bash_denied(command), command)

    def test_the_skills_own_scripts_run(self):
        script = fixtures.SCRIPTS / "gp_run.py"
        self.assertFalse(self.bash_denied("GP_PREFLIGHT=abcdef123456 python3 %s preflight" % script))
        self.assertFalse(self.bash_denied("python3 %s/check_all.py . --product Immerse" % fixtures.SCRIPTS))

    def test_sending_code_is_denied(self):
        self.assertTrue(self.bash_denied("python3 -c 'import smtplib'"))
        self.assertTrue(self.bash_denied("python3 -c \"import requests; requests.post('https://x', data=1)\""))
        self.assertTrue(self.bash_denied("node -e \"fetch('https://x', {method: 'POST'})\""))
        script = Path(self.cfg["package"]) / "send.py"
        script.write_text("import subprocess\nsubprocess.run(['gh', 'api', 'x'])\n")
        self.assertTrue(self.bash_denied("python3 %s" % script))
        self.assertTrue(self.denied("Write", file_path=str(Path(self.cfg["package"]) / "x.py"),
                                    content="import ftplib\n"))
        self.assertFalse(self.denied("Write", file_path=str(Path(self.cfg["package"]) / "notes.md"),
                                     content="We will never use smtplib.\n"))

    def test_heredocs_are_data_unless_something_runs_them(self):
        self.assertFalse(self.bash_denied("cat >> decisions-log.md <<'EOF'\n- D-009 it's the Founder's call, isn't it\nEOF"))
        self.assertFalse(self.bash_denied("cat > a.md <<EOF\nWe won't push or deploy anything.\nEOF\nls"))
        self.assertTrue(self.bash_denied("python3 - <<'EOF'\nimport smtplib\nEOF"))
        self.assertTrue(self.bash_denied("bash <<EOF\ngit push origin main\nEOF"))
        self.assertTrue(self.bash_denied("cat > a.md <<'EOF'\nnotes\nEOF\ngh pr create"))
        self.assertFalse(self.bash_denied("cat <<-EOF\n\tit's indented\n\tEOF"))

    def test_wrappers_must_run_alone(self):
        self.assertTrue(self.bash_denied("gp-sim list | head -3"))
        self.assertTrue(self.bash_denied("gp-chrome dom a.html > /tmp/out.html"))
        self.assertTrue(self.bash_denied("cd x && gp-xcodebuild build"))
        self.assertTrue(self.bash_denied("bash -c 'gp-sim list'"))

    def test_last30days_only_through_its_wrapper(self):
        self.assertTrue(self.bash_denied("python3.12 ~/.claude/plugins/cache/last30days-skill/last30days/3.8.3/"
                                         "skills/last30days/scripts/last30days.py setup --github"))
        self.assertTrue(self.bash_denied("python3.12 /x/last30days.py topic --publish-html"))

    def test_secrets_never_leave_env_files(self):
        self.assertTrue(self.bash_denied("cat /repo/.env"))
        self.assertTrue(self.bash_denied("grep KEY .env.local"))
        self.assertTrue(self.denied("Read", file_path="/repo/.env"))
        self.assertTrue(self.bash_denied("echo sk-test-supersecret-123456"))
        self.assertTrue(self.denied("Write", file_path=str(Path(self.cfg["package"]) / "a.md"),
                                    content="key sk-test-supersecret-123456"))
        log = Path(self.cfg["tool_log"]).read_text()
        self.assertNotIn("sk-test-supersecret-123456", log)
        self.assertIn("<redacted>", log)

    def test_writes_only_inside_the_package_and_cache(self):
        pkg, work = Path(self.cfg["package"]), Path(self.cfg["work"])
        self.assertFalse(self.denied("Write", file_path=str(pkg / "02-brand" / "x.md"), content="x"))
        self.assertFalse(self.denied("Edit", file_path=str(work / "x.txt"), old_string="a", new_string="b"))
        self.assertTrue(self.denied("Write", file_path=str(pkg.parent / "README.md"), content="x"))
        self.assertTrue(self.denied("Write", file_path=str(Path(self.cfg["protected"][0]) / "angles.md"), content="x"))
        self.assertTrue(self.denied("Write", file_path="/Users/someone/Desktop/x.md", content="x"))
        self.assertTrue(self.denied("Write", file_path=str(pkg / ".." / ".." / "RepToday" / "gtm" / "a.md"), content="x"))

    def test_tools_that_reach_outside_are_denied(self):
        for tool in ("Artifact", "RemoteTrigger", "PushNotification", "SendMessage", "CronCreate",
                     "EnterWorktree", "mcp__claude_ai_Gmail__create_draft", "mcp__pencil__batch_design"):
            self.assertTrue(self.denied(tool), tool)
        self.assertTrue(self.denied("AskUserQuestion", questions=[]))
        self.assertTrue(self.denied("Skill", skill="no-mistakes"))
        self.assertFalse(self.denied("Skill", skill="customer-research"))
        self.assertTrue(self.denied("Agent", prompt="x", isolation="worktree"))
        self.assertTrue(self.denied("Workflow", script="agent('x', {isolation: 'worktree'})"))
        self.assertFalse(self.denied("Workflow", script="export const meta = {name: 'x'}"))

    def test_webfetch_follows_robots(self):
        self.assertFalse(self.denied("WebFetch", url="https://allowed.example.org/page", prompt="x"))
        self.assertTrue(self.denied("WebFetch", url="https://allowed.example.org/private/a", prompt="x"))
        self.assertTrue(self.denied("WebFetch", url="https://www.reddit.com/r/x/", prompt="x"))
        self.assertTrue(self.denied("WebFetch", url="https://blocked.example.org/", prompt="x"))
        self.assertTrue(self.denied("WebFetch", url="ftp://x.example.org/", prompt="x"))

    def test_robots_matching_rules(self):
        body = ("User-agent: *\nDisallow: /search\nAllow: /search/about\nDisallow: /*.pdf$\n\n"
                "User-agent: Claude-User\nDisallow: /claude-only/\n")
        self.assertTrue(guard.robots_allows(body, "https://x/search/about", agent="Other"))
        self.assertFalse(guard.robots_allows(body, "https://x/search?q=1", agent="Other"))
        self.assertFalse(guard.robots_allows(body, "https://x/a/file.pdf", agent="Other"))
        self.assertTrue(guard.robots_allows(body, "https://x/a/file.pdf?x", agent="Other"))
        self.assertFalse(guard.robots_allows(body, "https://x/claude-only/a"))
        self.assertTrue(guard.robots_allows(body, "https://x/search"))

    def test_logs_and_receipts(self):
        self.decide("Read", file_path=str(fixtures.SCRIPTS.parent / "marketingskills" / "copywriting" / "SKILL.md"))
        guard.run_post(self.cfg, {"tool_name": "WebFetch", "tool_input": {"url": "https://a.example/x"},
                                  "tool_response": {"code": 200, "bytes": 10, "result": "ok"}})
        entries = [json.loads(l) for l in Path(self.cfg["tool_log"]).read_text().splitlines()]
        self.assertEqual(entries[0]["phase_skill"], "copywriting")
        fetch = json.loads(Path(self.cfg["fetch_log"]).read_text().splitlines()[0])
        self.assertEqual((fetch["url"], fetch["code"]), ("https://a.example/x", 200))
        self.decide("Bash", command="GP_PREFLIGHT=abcdef123456 python3 gp_run.py preflight")
        self.assertTrue((Path(self.cfg["work"]) / "guard-receipt-abcdef123456").is_file())

    def test_guard_fails_closed(self):
        import io
        import sys
        stdin, stdout = sys.stdin, sys.stdout
        sys.stdin, sys.stdout = io.StringIO(json.dumps({"tool_name": "Bash", "tool_input": {"command": "ls"}})), io.StringIO()
        try:
            guard.main(["pre", "/nonexistent/config.json"])
            out = json.loads(sys.stdout.getvalue())
        finally:
            sys.stdin, sys.stdout = stdin, stdout
        self.assertEqual(out["hookSpecificOutput"]["permissionDecision"], "deny")


class RunPrepTest(unittest.TestCase):
    def test_new_run_takes_gtm_then_a_dated_folder_beside_it(self):
        mandu = make_mandu(("Immerse",))
        today = dt.date(2026, 10, 24)
        first = gp_run.resolve_target(mandu, "Immerse", today)
        self.assertEqual((first["package_rel"], first["mode"], first["kind"]), ("projects/Immerse/gtm", "new", "first-package"))
        (mandu / "projects/Immerse/gtm").mkdir()
        second = gp_run.resolve_target(mandu, "Immerse", today)
        self.assertEqual(second["package_rel"], "projects/Immerse/gtm-candidate-2026-10-24")
        self.assertEqual(second["protected"], [str(mandu / "projects/Immerse/gtm")])
        (mandu / "projects/Immerse/gtm-candidate-2026-10-24").mkdir()
        third = gp_run.resolve_target(mandu, "Immerse", today)
        self.assertEqual(third["package_rel"], "projects/Immerse/gtm-candidate-2026-10-24-2")

    def test_in_progress_run_resumes(self):
        mandu = make_mandu(("RepToday",))
        (mandu / "projects/RepToday/gtm").mkdir()
        cand = mandu / "projects/RepToday/gtm-candidate-2026-10-20"
        cand.mkdir()
        gc.write_json(cand / gc.JOURNAL_NAME, {"gr0wthpilot_journal": 1, "status": "in-progress"})
        target = gp_run.resolve_target(mandu, "RepToday", dt.date(2026, 10, 24))
        self.assertEqual((target["package_rel"], target["mode"]), ("projects/RepToday/gtm-candidate-2026-10-20", "resume"))
        self.assertEqual(target["protected"], [str(mandu / "projects/RepToday/gtm")])

    def test_unknown_product_and_bad_name_refused(self):
        mandu = make_mandu(("Immerse",))
        with self.assertRaises(gp_run.RunError):
            gp_run.resolve_target(mandu, "Nope", dt.date(2026, 10, 24))
        with self.assertRaises(gp_run.RunError):
            gp_run.resolve_target(mandu, "../etc", dt.date(2026, 10, 24))

    def consent(self, mandu, trusted=True, imports=True):
        path = Path(tempfile.mkdtemp(prefix="gp-claude-")) / ".claude.json"
        gc.write_json(path, {"projects": {str(mandu.resolve()): {"hasTrustDialogAccepted": trusted,
                                                                  "hasClaudeMdExternalIncludesApproved": imports}}})
        return path

    def test_launcher_refuses_before_any_consent_dialog(self):
        mandu = make_mandu(("Immerse",)).resolve()
        gp_run.check_claude_consent(mandu, self.consent(mandu))
        with self.assertRaises(gp_run.RunError) as raised:
            gp_run.check_claude_consent(mandu, self.consent(mandu, trusted=False))
        self.assertIn("has not trusted", str(raised.exception))
        with self.assertRaises(gp_run.RunError) as raised:
            gp_run.check_claude_consent(mandu, self.consent(mandu, imports=False))
        self.assertIn("CLAUDE.md imports", str(raised.exception))
        parent = Path(tempfile.mkdtemp(prefix="gp-claude-")) / ".claude.json"
        gc.write_json(parent, {"projects": {str(mandu.parent): {"hasTrustDialogAccepted": True},
                                            str(mandu): {"hasClaudeMdExternalIncludesApproved": True}}})
        gp_run.check_claude_consent(mandu, parent)
        with self.assertRaises(gp_run.RunError):
            gp_run.check_claude_consent(mandu, "/nonexistent/.claude.json")

    def test_prepare_writes_journal_config_and_profile(self):
        mandu = make_mandu(("Immerse",))
        os.environ["CLAUDE_CONFIG_DIR"] = str(self.consent(mandu.resolve()).parent)
        self.addCleanup(os.environ.pop, "CLAUDE_CONFIG_DIR", None)
        work = Path(tempfile.mkdtemp(prefix="gp-work-"))
        args = type("A", (), {"mandu": str(mandu), "product": "Immerse", "work": str(work), "repo": None,
                              "today": "2026-10-24"})
        old = os.environ.pop("GR0WTHPILOT_REPO", None)
        try:
            cfg = gp_run.prepare(args)
        finally:
            if old:
                os.environ["GR0WTHPILOT_REPO"] = old
        copies = sorted(p.name for p in (work / "workflows").glob("*.js"))
        shipped = sorted(p.name for p in (fixtures.SCRIPTS.parent / "workflows").glob("*.js"))
        self.assertEqual(copies, shipped)
        self.assertEqual((work / "workflows" / "critic.js").read_text(),
                         (fixtures.SCRIPTS.parent / "workflows" / "critic.js").read_text())
        journal = gc.read_json(Path(cfg["package"]) / gc.JOURNAL_NAME)
        self.assertEqual((journal["status"], journal["product"]), ("in-progress", "Immerse"))
        profile = gc.read_json(Path(cfg["profile_path"]))
        perms = profile["permissions"]
        self.assertEqual(perms["defaultMode"], "dontAsk")
        self.assertIn("Edit(/%s/**)" % cfg["package"], perms["allow"])
        self.assertIn("Bash(git push *)", perms["deny"])
        self.assertIn("mcp__*", perms["deny"])
        self.assertEqual(gp_run.validate_profile(profile), [])
        self.assertTrue(profile["sandbox"]["enabled"])
        self.assertFalse(profile["sandbox"]["allowUnsandboxedCommands"])
        self.assertTrue(profile["sandbox"]["network"]["strictAllowlist"])
        self.assertNotIn("api.github.com", profile["sandbox"]["network"]["allowedDomains"])
        self.assertEqual(profile["workflowSizeGuideline"], gp_run.WORKFLOW_SIZE_GUIDELINE)
        for event in ("SessionStart", "PreToolUse", "PostToolUse"):
            self.assertIn("guard.py", profile["hooks"][event][0]["hooks"][0]["command"])
        again = gp_run.prepare(args)
        self.assertEqual(again["mode"], "resume")
        self.assertEqual(len(gc.read_json(Path(cfg["package"]) / gc.JOURNAL_NAME)["sessions"]), 2)

    def test_profile_rules_must_match_the_settings_schema(self):
        bad = {"permissions": {"allow": ["Bash", "LS"], "deny": ["AskUserQuestion", "Bash(git push *)"], "mode": "x"},
               "workflowSizeGuideline": 40, "modelSettings": {}}
        problems = gp_run.validate_profile(bad)
        self.assertTrue(any("workflowSizeGuideline" in p for p in problems))
        self.assertTrue(any("modelSettings" in p for p in problems))
        self.assertTrue(any("'LS'" in p for p in problems))
        self.assertTrue(any("'AskUserQuestion'" in p for p in problems))
        self.assertTrue(any("permissions.mode" in p for p in problems))

    def test_shared_project_settings_must_not_change_permissions(self):
        mandu = make_mandu(("Immerse",))
        (mandu / ".claude").mkdir()
        (mandu / ".claude" / "settings.json").write_text("{}")
        gp_run.check_project_settings(mandu)
        (mandu / ".claude" / "settings.json").write_text('{"permissions": {"allow": ["Bash(git push *)"]}}')
        with self.assertRaises(gp_run.RunError):
            gp_run.check_project_settings(mandu)

    def test_preflight_needs_a_guard_receipt(self):
        cfg = config()
        path = Path(cfg["work"]) / "guard-config.json"
        gc.write_json(path, cfg)
        args = type("A", (), {"config": str(path)})
        os.environ.pop("GP_PREFLIGHT", None)
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(gp_run.preflight(args), 2)
        os.environ["GP_PREFLIGHT"] = "abcdef123456"
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(gp_run.preflight(args), 2)
                (Path(cfg["work"]) / "guard-receipt-abcdef123456").write_text("seen")
                self.assertEqual(gp_run.preflight(args), 0)
        finally:
            del os.environ["GP_PREFLIGHT"]


class WrapperRulesTest(unittest.TestCase):
    def setUp(self):
        self.cfg = config()

    def test_gp_sim_touches_only_devices_it_created(self):
        sim = load_wrapper("gp-sim")
        gc.write_json(Path(self.cfg["simulators"]), {"devices": [{"udid": "MINE", "name": "Gr0wthPilot-Immerse-1"}]})
        sim.all_devices = lambda: {"MINE": {"udid": "MINE", "name": "Gr0wthPilot-Immerse-1", "state": "Shutdown"},
                                   "THEIRS": {"udid": "THEIRS", "name": "iPhone 17 Pro", "state": "Booted"},
                                   "RENAMED": {"udid": "RENAMED", "name": "Someone's phone", "state": "Booted"}}
        self.assertEqual(sim.owned(self.cfg, "MINE")["name"], "Gr0wthPilot-Immerse-1")
        with self.assertRaises(sim.ToolError):
            sim.owned(self.cfg, "THEIRS")
        gc.write_json(Path(self.cfg["simulators"]), {"devices": [{"udid": "RENAMED", "name": "Gr0wthPilot-Immerse-2"}]})
        with self.assertRaises(sim.ToolError):
            sim.owned(self.cfg, "RENAMED")

    def test_gp_sim_picks_the_newest_iphone_pro(self):
        sim = load_wrapper("gp-sim")
        types = [{"name": n, "identifier": "id-" + n, "productFamily": "iPhone"} for n in
                 ("iPhone 17 Pro", "iPhone 16e", "iPhone 11 Pro", "iPhone 17 Pro Max", "iPhone SE (3rd generation)")]
        self.assertEqual(sim.newest_iphone(types), "id-iPhone 17 Pro")
        self.assertEqual(sim.newest_iphone(types[1:2] + types[4:]), "id-iPhone 16e")

    def test_gp_sim_outputs_stay_inside(self):
        sim = load_wrapper("gp-sim")
        with self.assertRaises(sim.ToolError):
            sim.out_path(self.cfg, "/Users/someone/Desktop/shot.png")
        self.assertTrue(str(sim.out_path(self.cfg, str(Path(self.cfg["package"]) / "a.png"))).endswith("a.png"))

    def test_gp_chrome_opens_only_local_pages(self):
        chrome = load_wrapper("gp-chrome")
        page = Path(self.cfg["package"]) / "index.html"
        page.write_text("<p>x</p>")
        self.assertTrue(chrome.page_url(self.cfg, str(page)).startswith("file://"))
        self.assertEqual(chrome.page_url(self.cfg, "http://localhost:8080/"), "http://localhost:8080/")
        for bad in ("https://example.com", "http://192.168.1.2/", "/etc/hosts"):
            with self.assertRaises(chrome.ToolError):
                chrome.page_url(self.cfg, bad)

    def test_gp_xcodebuild_builds_only_for_the_simulator(self):
        xb = load_wrapper("gp-xcodebuild")
        src = Path(self.cfg["work"]) / "source" / "abc" / "App.xcodeproj"
        src.mkdir(parents=True)
        ok = ["-project", str(src), "-scheme", "App", "-destination", "generic/platform=iOS Simulator", "build"]
        xb.check_args(self.cfg, ok)
        for bad in (["archive"], ["-exportArchive"], ["-allowProvisioningUpdates"], ["DEVELOPMENT_TEAM=X"],
                    ["-destination", "generic/platform=iOS"], ["-sdk", "iphoneos"],
                    ["-destination", "platform=iOS Simulator,id=NOT-MINE"]):
            with self.assertRaises(xb.ToolError, msg=str(bad)):
                xb.check_args(self.cfg, ok[:4] + bad + ["build"])
        with self.assertRaises(xb.ToolError):
            xb.check_args(self.cfg, ["-project", "/Users/someone/Developer/App/App.xcodeproj", "build"])

    def test_gp_last30days_keeps_paid_sources_off(self):
        l30 = load_wrapper("gp-last30days")
        os.environ["GR0WTHPILOT_CONFIG"] = str(Path(self.cfg["work"]) / "c.json")
        gc.write_json(Path(os.environ["GR0WTHPILOT_CONFIG"]), self.cfg)
        import contextlib
        import io
        try:
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(l30.main(["film", "--out", str(Path(self.cfg["package"]) / "r"), "--sources", "reddit,tiktok"]), 1)
                self.assertEqual(l30.main(["film", "--out", "/tmp/elsewhere"]), 1)
        finally:
            del os.environ["GR0WTHPILOT_CONFIG"]


if __name__ == "__main__":
    unittest.main()
