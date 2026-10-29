"""Tests for the guard, the launcher's preparation, and the tool wrappers'
rules: the parts that keep "publish nothing, spend nothing, write only the
Candidate Package" true.

Run from Mandu's root: python3 -m unittest discover -s .claude/skills/gr0wthpilot/tests
"""

from __future__ import annotations

import contextlib
import datetime as dt
import importlib.machinery
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import tempfile
import types
import unittest
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from unittest import mock

import fixtures

import gp_common as gc
import gp_run
import guard
import journal


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
    state = tmp / "work.guard"
    env = tmp / "repo.env"
    env.write_text("OPENAI_API_KEY=sk-test-supersecret-123456\nSHORT=abc\n")
    robots = state / "robots"
    robots.mkdir(parents=True)
    for host, body in (("allowed.example.org", "User-agent: *\nDisallow: /private/\n"),
                       ("www.reddit.com", "User-agent: *\nDisallow: /\n")):
        (robots / (host + ".json")).write_text(json.dumps({"at": 9e12, "status": 200, "body": body}))
    (robots / "blocked.example.org.json").write_text(json.dumps({"at": 9e12, "status": 403, "body": ""}))
    return {
        "product": "Immerse", "package": str(pkg), "package_rel": "projects/Immerse/gtm", "work": str(work),
        "state": str(state), "build": str(state / "build"), "run_id": "immerse-run-2",
        "protected": [str(live)], "skill_dir": str(fixtures.SCRIPTS.parent),
        "env_files": [str(env)], "last30days_log": str(work / "last30days-log.jsonl"),
        "tool_log": str(state / "tool-log.jsonl"), "fetch_log": str(state / "fetch-log.jsonl"),
        "robots_dir": str(robots), "simulators": str(state / "simulators.json"), "repo": None,
    }


def http_get(url):
    """(status, body) of a GET straight to a local server, past any proxy."""
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(url, timeout=10) as response:
            return response.status, response.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")


def product_repo():
    """A git repository holding a minimal app project, committed."""
    repo = Path(tempfile.mkdtemp(prefix="gp-repo-"))
    (repo / "App.xcodeproj").mkdir()
    (repo / "App.xcodeproj" / "project.pbxproj").write_text("// the Founder's project\n")
    (repo / "Config.xcconfig").write_text("SWIFT_VERSION = 5.0\n")
    (repo / "Simulator.xcconfig").write_text('#include? "Config.xcconfig"\nSDKROOT = iphonesimulator // ok\n')
    (repo / "Device.xcconfig").write_text('#include "Config.xcconfig"\nSDKROOT[sdk=*] = iphoneos\n')
    (repo / "Outside.xcconfig").write_text('#include "../../elsewhere.xcconfig"\n')
    git = ["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.org", "-c", "commit.gpgsign=false"]
    for args in (["init", "-q"], ["add", "-A"], ["commit", "-q", "-m", "project"]):
        subprocess.run(git + args, check=True)
    return repo


def exported_copy(xb, cfg):
    """Export a Product repository with gp-xcodebuild source; return the copy."""
    cfg["repo"] = str(product_repo())
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        xb.cmd_source(cfg, [])
    return Path(json.loads(out.getvalue())["source"])


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
        self.assertFalse(self.bash_denied("python3 %s/journal.py status" % fixtures.SCRIPTS))

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

    def test_code_is_refused_only_for_programs_it_runs(self):
        site = Path(self.cfg["package"]) / "03-site"
        allowed = {
            "app.js": "menu.classList.toggle('open', expanded);\nconst topics = ['security', 'privacy'];\n"
                      "window.open('https://x.example/');\n/gh/.exec('gh');\n",
            "build.py": "import subprocess\nsubprocess.run(['ffmpeg', '-i', 'a.mp4', 'b.png'])\n"
                        "subprocess.run(['git', 'log'])\nsubprocess.run(['git', '-C', 'repo', 'log'])\n",
        }
        for name, code in allowed.items():
            self.assertFalse(self.denied("Write", file_path=str(site / name), content=code), name)
        refused = {
            "a.py": "import subprocess\nsubprocess.run(['/usr/bin/open', 'https://x.example'])\n",
            "b.py": "import os\nos.system('gh api repos')\n",
            "c.js": "const { execFileSync } = require('child_process');\nexecFileSync('git', ['push', 'origin']);\n",
            "d.js": "require('child_process').spawn('/usr/bin/security', ['find-generic-password']);\n",
            "e.py": "import subprocess\nsubprocess.Popen([\"xcrun\", \"simctl\", \"list\"])\n",
        }
        for name, code in refused.items():
            self.assertTrue(self.denied("Write", file_path=str(site / name), content=code), name)
        self.assertTrue(self.bash_denied("node -e \"require('child_process').execSync('open https://x.example')\""))

    def test_shell_scripts_are_checked_as_the_commands_they_run(self):
        pkg = Path(self.cfg["package"])
        scripts = {
            "serve.sh": "#!/bin/sh\n# it's the local server\nopen http://localhost:8000\n",
            "ok.sh": "#!/bin/sh\n# it's the local server\npython3 -m http.server 8000\n",
            "tool": "#!/usr/bin/env python3\nimport subprocess\nsubprocess.run(['gh', 'pr', 'create'])\n",
            "plain": "if true; then gh pr create; fi\n",
            "apple": "#!/usr/bin/osascript\ndisplay dialog \"x\"\n",
            "mod.py": "import smtplib\n",
            "send.ts": "fetch('https://x.example', {method: 'POST'})\n",
        }
        for name, text in scripts.items():
            (pkg / name).write_text(text)
        for command in ("bash serve.sh", "sh serve.sh", "zsh serve.sh", "source serve.sh", ". ./serve.sh",
                        "./serve.sh", "./tool", "./plain", "./apple", "bash < serve.sh", "cat serve.sh | sh",
                        "cat mod.py | python3", "python3 -m mod", "npx tsx send.ts", "bun run send.ts",
                        "if true; then gh pr create; fi", "for f in a; do open $f; done", "bash -lc 'open x'",
                        "python3 -Bc 'import smtplib'",
                        "node -p \"require('child_process').execSync('open x')\""):
            self.assertTrue(self.bash_denied(command), command)
        for command in ("bash ok.sh", "./ok.sh", "source ok.sh", "python3 -m http.server 8080",
                        "/bin/ls -la"):
            self.assertFalse(self.bash_denied(command), command)
        self.assertTrue(self.denied("Write", file_path=str(pkg / "deploy.sh"), content="#!/bin/sh\ngh pr create\n"))
        self.assertFalse(self.denied("Write", file_path=str(pkg / "serve2.sh"),
                                     content="#!/bin/sh\n# it's fine\npython3 -m http.server\n"))

    def test_options_after_the_script_are_the_scripts(self):
        pkg = Path(self.cfg["package"])
        (pkg / "build.py").write_text("import subprocess\nsubprocess.run(['open', 'x'])\n")
        (pkg / "render.js").write_text("require('child_process').execFileSync('open', ['x'])\n")
        (pkg / "serve.sh").write_text("open http://localhost:8000\n")
        (pkg / "ok.py").write_text("print(1)\n")
        for command in ("python3 build.py -c config.json", "python3 build.py -m fast", "node render.js -e prod",
                        "node render.js -p", "bash serve.sh -c x", "python3 build.py -p 8000",
                        "bash -euo pipefail serve.sh", "cat serve.sh | bash -euo pipefail", "python3 -X utf8 build.py",
                        "python3 -W ignore build.py", "node --import tsx render.js", "bun x wrangler deploy"):
            self.assertTrue(self.bash_denied(command), command)
        for command in ("python3 ok.py -c config.json", "python3 -X utf8 ok.py", "bash -euo pipefail -c 'ls -la'",
                        "python3 -m http.server 8000"):
            self.assertFalse(self.bash_denied(command), command)

    def test_scripts_are_found_from_the_commands_folder(self):
        pkg = Path(self.cfg["package"])
        site = pkg / "03-site"
        site.mkdir()
        (site / "serve.sh").write_text("open http://localhost:8000\n")
        (site / "build.py").write_text("import subprocess\nsubprocess.run(['open', 'x'])\n")
        (pkg / "serve.sh").write_text("ls\n")
        for command in ("cd 03-site && bash serve.sh", "cd 03-site && ./serve.sh", "cd 03-site && source serve.sh",
                        "cd 03-site && python3 build.py", "(cd 03-site; bash serve.sh)", "bash missing.sh",
                        "cd - && bash serve.sh"):
            self.assertTrue(self.bash_denied(command), command)
        self.assertFalse(self.bash_denied("bash serve.sh"))
        later = guard.run_pre(self.cfg, {"tool_name": "Bash", "tool_input": {"command": "./serve.sh"}, "cwd": str(site)})
        self.assertEqual(later["hookSpecificOutput"]["permissionDecision"], "deny")

    def test_a_trailing_comment_does_not_break_the_parse(self):
        pkg = Path(self.cfg["package"])
        self.assertFalse(self.denied("Write", file_path=str(pkg / "render.sh"),
                                     content="#!/bin/sh\nffmpeg -i a.mp4 b.mp4 # don't rescale\n"))
        self.assertFalse(self.bash_denied("ls -la # it's the package"))
        self.assertFalse(self.bash_denied("echo \"${HOME} #1\" && ls"))
        for command in ("ls # it's fine\ngh pr create", "echo ${#HOME}; gh pr create", "echo a#b; gh pr create",
                        "echo a\\;#b; gh pr create", "echo hi\\|#x; git push origin main",
                        "echo ${x:-a #b}; gh pr create", "echo ${x:-a #b}; open https://example.com",
                        "x=1#y gh pr create", "echo \"`gh pr create`\"", "cat > a.md <<EOF\n$(gh pr create)\nEOF",
                        "cat > a.md <<EOF\n`gh pr create`\nEOF", "$'\\x67h' pr create", "cat <<E\"O\"F\ngh\nEOF"):
            self.assertTrue(self.bash_denied(command), command)
        self.assertFalse(self.bash_denied("cat > a.md <<'EOF'\n$(not run) and `not run`\nEOF"))

    def test_code_from_standard_input_is_refused_whatever_the_flags(self):
        for command in ("echo 'gh pr create' | bash -v", "echo 'gh pr create' | bash -h",
                        "echo 'import os' | python3 -v", "echo 'gh pr create' | zsh -v", "bash --version",
                        "python3 <<< 'print(1)'", "bash <<< 'gh pr create'", "cat run.sh | bash -s x"):
            self.assertTrue(self.bash_denied(command), command)

    def test_options_and_variables_that_load_code_are_checked(self):
        pkg = Path(self.cfg["package"])
        (pkg / "pre.js").write_text("require('child_process').execFileSync('open', ['x'])\n")
        (pkg / "ok.js").write_text("console.log(1)\n")
        (pkg / "app.js").write_text("console.log(2)\n")
        (pkg / "pre.rb").write_text("system('open', 'x')\n")
        (pkg / "ok.rb").write_text("puts 1\n")
        (pkg / "evil.sh").write_text("open http://x\n")
        for command in ("node -r ./pre.js app.js", "node --import ./pre.js app.js", "node --require=./pre.js app.js",
                        "node --import tsx app.js", "ruby -r ./pre.rb ok.rb", "ruby -I lib ok.rb", "perl -Mstrict -e 1",
                        "bash --rcfile ./evil.sh -i -c ls", "BASH_ENV=./evil.sh bash -c 'ls'",
                        "export BASH_ENV=./evil.sh", "env ZDOTDIR=. zsh -c ls", "PS4='$(gh pr create)' bash -xc ls",
                        "NODE_OPTIONS=--require=./pre.js node app.js", "PYTHONPATH=. python3 ok.py",
                        "declare -n ref=BASH_ENV", "python3 -m evilmod", "python3 -m pip install x",
                        "python3 -W error::evil.Warning ok.py", "deno run --import-map=m.json x.ts"):
            self.assertTrue(self.bash_denied(command), command)
        for command in ("node -r ./ok.js app.js", "python3 -m json.tool data.json", "echo 'copy it to ENV'"):
            self.assertFalse(self.bash_denied(command), command)
        (pkg / "http").mkdir()
        (pkg / "http" / "__init__.py").write_text("import os\n")
        self.assertTrue(self.bash_denied("python3 -m http.server 8000"))

    def test_the_program_a_command_runs_must_be_plain(self):
        for command in ("X=gh; $X pr create", "$(echo gh) pr create", "\"$(which gh)\" pr create",
                        "env -S 'gh pr create'", "timeout -s KILL 5 gh pr create", "echo gh | xargs -I X X pr create",
                        "echo x | xargs -I{} sh -c {}", "ls | xargs bash", "builtin eval 'gh pr create'",
                        "noglob gh pr create", "alias g=gh", "trap 'gh pr create' EXIT", "hash -p /usr/bin/true g",
                        "/usr/bin/g? pr create"):
            self.assertTrue(self.bash_denied(command), command)
        for command in ("[ -f x ] && ls", "[[ -f x ]] && ls", "timeout 60 ls", "env -i HOME=/tmp ls",
                        "ls *.png | xargs -n1 ffprobe", "for f in a b; do ffprobe $f; done", "command -v ffmpeg"):
            self.assertFalse(self.bash_denied(command), command)

    def test_groups_functions_and_variable_names_stay_simple(self):
        pkg = Path(self.cfg["package"])
        (pkg / "ok.py").write_text("print(1)\n")
        for command in ("function f { open https://x.com; }; f", "f() { open https://x.com; }; f", "f() (ls); f",
                        "{ ls; }", "echo a.{png,jpg}", ">out.txt open https://x.com", "2>err.txt osascript -e x",
                        "=open https://x.com", "repeat 1 open https://x.com",
                        'x=BASH; export "${x}_ENV=./evil.txt"; bash -c ls',
                        "export {BASH,X}_ENV=./evil.txt; bash -c ls",
                        'printf -v "${x}_ENV" ./evil.txt; export "${x}_ENV"', "BASH_ENV+=./evil.txt bash -c ls",
                        "echo ${BASH_ENV:=./evil.txt}", "let BASH_ENV=1", "(( BASH_ENV = 1 ))",
                        "read -r BASH_ENV < f", "mapfile -t DYLD_INSERT_LIBRARIES < f", "declare -x PYTHONHOME=/tmp",
                        "getopts a BASH_ENV", "printf -vBASH_ENV x"):
            self.assertTrue(self.bash_denied(command), command)
        for command in ("grep -rn ENV .", "ls", "git -C /repo log", "ffmpeg -i a.mp4 b.mp4",
                        "python3 %s" % (pkg / "ok.py"), "cat >> notes.md <<'EOF'\nline\nEOF",
                        "export PATH=\"$PATH:/x\"", "read -r line < f", "printf '%s\\n' x",
                        "find . -name '*.md' -exec wc -l {} \\;", "echo \"{a,b}\""):
            self.assertFalse(self.bash_denied(command), command)
        self.assertTrue(self.denied("Write", file_path=str(pkg / "serve.sh"),
                                    content="function f { open https://x.com; }\nf\n"))

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
        for record in ("guard-config.json", "robots/www.g2.com.json", "fetch-log.jsonl"):
            self.assertTrue(self.denied("Write", file_path=str(Path(self.cfg["state"]) / record), content="{}"), record)

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
        entries = [json.loads(line) for line in Path(self.cfg["tool_log"]).read_text().splitlines()]
        self.assertEqual(entries[0]["phase_skill"], "copywriting")
        self.assertEqual({e["run_id"] for e in entries}, {"immerse-run-2"})
        fetch = json.loads(Path(self.cfg["fetch_log"]).read_text().splitlines()[0])
        self.assertEqual((fetch["url"], fetch["code"], fetch["run_id"]), ("https://a.example/x", 200, "immerse-run-2"))
        self.decide("Bash", command="GP_PREFLIGHT=abcdef123456 python3 %s preflight" % (fixtures.SCRIPTS / "gp_run.py"))
        self.assertTrue((Path(self.cfg["work"]) / "guard-receipt-abcdef123456").is_file())

    def test_guard_fails_closed(self):
        import sys
        stdin, stdout = sys.stdin, sys.stdout
        sys.stdin, sys.stdout = io.StringIO(json.dumps({"tool_name": "Bash", "tool_input": {"command": "ls"}})), io.StringIO()
        try:
            guard.main(["pre", "/nonexistent/config.json"])
            out = json.loads(sys.stdout.getvalue())
        finally:
            sys.stdin, sys.stdout = stdin, stdout
        self.assertEqual(out["hookSpecificOutput"]["permissionDecision"], "deny")


TODAY = dt.date(2026, 10, 24)


def registry(*handed_off, folder="gtm"):
    """gr0wthlab's product list naming a go_to_market_package in that folder
    for each Product given, plus a listening-only Product with none."""
    path = Path(tempfile.mkdtemp(prefix="gp-gr0wthlab-")) / "config" / "products.json"
    products = [{"name": n, "go_to_market_package": {"path": "projects/%s/%s/" % (n, folder)}} for n in handed_off]
    gc.write_json(path, {"products": products + [{"name": "Listening", "go_to_market_package": None}]})
    return path


def journal_at(folder, status):
    folder.mkdir(parents=True, exist_ok=True)
    gc.write_json(folder / gc.JOURNAL_NAME, {"gr0wthpilot_journal": 1, "status": status})


class RunPrepTest(unittest.TestCase):
    def test_new_run_takes_gtm_then_a_dated_folder_beside_it(self):
        mandu = make_mandu(("Immerse",))
        first = gp_run.resolve_target(mandu, "Immerse", TODAY, registry())
        self.assertEqual((first["package_rel"], first["mode"], first["kind"]), ("projects/Immerse/gtm", "new", "first-package"))
        (mandu / "projects/Immerse/gtm").mkdir()
        second = gp_run.resolve_target(mandu, "Immerse", TODAY, registry())
        self.assertEqual(second["package_rel"], "projects/Immerse/gtm-candidate-2026-10-24")
        self.assertEqual(second["protected"], [str(mandu / "projects/Immerse/gtm")])
        (mandu / "projects/Immerse/gtm-candidate-2026-10-24").mkdir()
        third = gp_run.resolve_target(mandu, "Immerse", TODAY, registry())
        self.assertEqual(third["package_rel"], "projects/Immerse/gtm-candidate-2026-10-24-2")

    def test_a_product_not_handed_off_keeps_its_package_and_writes_a_candidate(self):
        mandu = make_mandu(("Immerse",))
        listed = registry("RepToday")
        first = gp_run.resolve_target(mandu, "Immerse", TODAY, listed)
        self.assertEqual((first["package_rel"], first["mode"], first["kind"], first["handoff_line"]),
                         ("projects/Immerse/gtm", "new", "first-package", "Immerse - hand to gr0wthlab"))
        gtm = mandu / "projects/Immerse/gtm"
        journal_at(gtm, "in-progress")
        resumed = gp_run.resolve_target(mandu, "Immerse", TODAY, listed)
        self.assertEqual((resumed["package_rel"], resumed["mode"], resumed["kind"]),
                         ("projects/Immerse/gtm", "resume", "first-package"))
        journal_at(gtm, "complete")
        second = gp_run.resolve_target(mandu, "Immerse", TODAY, listed)
        self.assertEqual((second["package_rel"], second["mode"], second["kind"]),
                         ("projects/Immerse/gtm-candidate-2026-10-24", "new", "candidate"))
        self.assertEqual(second["handoff_line"], "Immerse - hand to gr0wthlab (gtm-candidate-2026-10-24)")
        self.assertEqual(second["protected"], [str(gtm)])
        self.assertIn("names no go_to_market_package", second["kind_reason"])

    def test_a_handed_off_product_writes_beside_its_live_package(self):
        mandu = make_mandu(("RepToday",))
        listed = registry("RepToday")
        live = mandu / "projects/RepToday/gtm"
        target = gp_run.resolve_target(mandu, "RepToday", TODAY, listed)
        self.assertEqual((target["package_rel"], target["kind"], target["handoff_line"]),
                         ("projects/RepToday/gtm-candidate-2026-10-24", "beside-live", None))
        self.assertEqual(target["protected"], [str(live)])
        journal_at(live, "in-progress")
        target = gp_run.resolve_target(mandu, "RepToday", TODAY, listed)
        self.assertEqual((target["package_rel"], target["mode"], target["kind"]),
                         ("projects/RepToday/gtm-candidate-2026-10-24", "new", "beside-live"))
        cand = mandu / "projects/RepToday/gtm-candidate-2026-10-20"
        journal_at(cand, "in-progress")
        target = gp_run.resolve_target(mandu, "RepToday", TODAY, listed)
        self.assertEqual((target["package_rel"], target["mode"], target["kind"]),
                         ("projects/RepToday/gtm-candidate-2026-10-20", "resume", "beside-live"))
        self.assertEqual(target["protected"], [str(live)])
        self.assertIn("names a go_to_market_package for RepToday", target["kind_reason"])

    def test_the_live_package_is_the_folder_gr0wthlab_names(self):
        mandu = make_mandu(("Immerse",))
        gtm = mandu / "projects/Immerse/gtm"
        handed = mandu / "projects/Immerse/gtm-candidate-2026-11-01"
        journal_at(gtm, "complete")
        journal_at(handed, "in-progress")
        listed = registry("Immerse", folder="gtm-candidate-2026-11-01")
        target = gp_run.resolve_target(mandu, "Immerse", TODAY, listed)
        self.assertEqual((target["package_rel"], target["mode"], target["kind"], target["handoff_line"]),
                         ("projects/Immerse/gtm-candidate-2026-10-24", "new", "beside-live", None))
        self.assertEqual(target["protected"], [str(gtm), str(handed)])
        self.assertIn("projects/Immerse/gtm-candidate-2026-11-01/ is its live package", target["kind_reason"])
        journal_at(gtm, "in-progress")
        resumed = gp_run.resolve_target(mandu, "Immerse", TODAY, listed)
        self.assertEqual((resumed["package_rel"], resumed["mode"], resumed["kind"]),
                         ("projects/Immerse/gtm", "resume", "beside-live"))
        self.assertEqual(resumed["protected"], [str(handed)])
        missing = gp_run.resolve_target(make_mandu(("Immerse",)), "Immerse", TODAY,
                                        registry("Immerse", folder="gtm-candidate-2026-10-24"))
        self.assertEqual(missing["package_rel"], "projects/Immerse/gtm-candidate-2026-10-24-2")
        self.assertTrue(missing["protected"][0].endswith("projects/Immerse/gtm-candidate-2026-10-24"))

    def test_an_unreadable_product_list_still_resumes_an_unfinished_gtm(self):
        mandu = make_mandu(("Immerse",))
        missing = Path(tempfile.mkdtemp(prefix="gp-gr0wthlab-")) / "config" / "products.json"
        first = gp_run.resolve_target(mandu, "Immerse", TODAY, missing)
        self.assertEqual((first["package_rel"], first["kind"]), ("projects/Immerse/gtm", "first-package"))
        journal_at(mandu / "projects/Immerse/gtm", "in-progress")
        again = gp_run.resolve_target(mandu, "Immerse", TODAY, missing)
        self.assertEqual((again["package_rel"], again["mode"], again["kind"], again["handoff_line"]),
                         ("projects/Immerse/gtm", "resume", "first-package", "Immerse - hand to gr0wthlab"))
        self.assertEqual(again["protected"], [])

    def test_an_unreadable_product_list_treats_a_finished_gtm_as_live(self):
        missing = Path(tempfile.mkdtemp(prefix="gp-gr0wthlab-")) / "config" / "products.json"
        for status in ("complete", None):
            mandu = make_mandu(("Immerse",))
            gtm = mandu / "projects/Immerse/gtm"
            if status:
                journal_at(gtm, status)
            else:
                gtm.mkdir()
            target = gp_run.resolve_target(mandu, "Immerse", TODAY, missing)
            self.assertEqual((target["package_rel"], target["mode"], target["kind"], target["handoff_line"]),
                             ("projects/Immerse/gtm-candidate-2026-10-24", "new", "beside-live", None), status)
            self.assertEqual(target["protected"], [str(gtm)], status)
            self.assertIn("could not be read", target["kind_reason"])
            self.assertIn("projects/Immerse/gtm/ is treated as possibly live", target["kind_reason"])

    def test_unknown_product_and_bad_name_refused(self):
        mandu = make_mandu(("Immerse",))
        with self.assertRaises(gp_run.RunError):
            gp_run.resolve_target(mandu, "Nope", TODAY, registry())
        with self.assertRaises(gp_run.RunError):
            gp_run.resolve_target(mandu, "../etc", TODAY, registry())

    def test_product_name_must_match_its_folder_exactly(self):
        mandu = make_mandu(("Immerse",))
        with self.assertRaises(gp_run.RunError) as raised:
            gp_run.resolve_target(mandu, "immerse", TODAY, registry())
        self.assertIn("Immerse", str(raised.exception))

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
        os.environ["GR0WTHLAB_DIR"] = str(registry().parent.parent)
        self.addCleanup(os.environ.pop, "GR0WTHLAB_DIR", None)
        cache = Path(tempfile.mkdtemp(prefix="gp-cache-"))
        work = cache / "Immerse"
        args = type("A", (), {"mandu": str(mandu), "product": "Immerse", "cache": str(cache), "repo": None,
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
        self.assertEqual((cfg["kind"], cfg["handoff_line"]), ("first-package", "Immerse - hand to gr0wthlab"))
        # The guard's records are where no tool of the run can write.
        state = Path(cfg["state"])
        writable = profile["sandbox"]["filesystem"]["allowWrite"] + [cfg["package"]]
        writable += [r[len("Edit(/"):-len("/**)")] for r in perms["allow"] if r.startswith("Edit(")]
        for key in ("config_path", "profile_path", "robots_dir", "tool_log", "fetch_log", "simulators"):
            self.assertTrue(guard.under(cfg[key], state), key)
            for root in writable:
                self.assertFalse(guard.under(cfg[key], root), (key, root))
            out = guard.run_pre(cfg, {"tool_name": "Write", "tool_input": {"file_path": cfg[key], "content": "{}"}})
            self.assertEqual(out["hookSpecificOutput"]["permissionDecision"], "deny", key)
        self.assertIn(cfg["state"], profile["sandbox"]["filesystem"]["denyWrite"])
        self.assertIn("Edit(/%s/**)" % cfg["state"], perms["deny"])
        self.assertTrue(guard.under(cfg["last30days_log"], work))
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
        path = Path(cfg["state"]) / "guard-config.json"
        gc.write_json(path, cfg)
        args = type("A", (), {"config": str(path)})
        os.environ.pop("GP_PREFLIGHT", None)
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


def consent_file(mandu):
    path = Path(tempfile.mkdtemp(prefix="gp-claude-")) / ".claude.json"
    gc.write_json(path, {"projects": {str(Path(mandu).resolve()): {"hasTrustDialogAccepted": True,
                                                                   "hasClaudeMdExternalIncludesApproved": True}}})
    return path


def renamable_mandu():
    """A Mandu whose Testprod package is an unfinished run past critic-1 that
    proposes the name Filmora."""
    mandu = make_mandu(("Testprod",))
    pkg = mandu / "projects/Testprod/gtm"
    fixtures.build(pkg, video=False)
    data = gc.read_json(pkg / gc.JOURNAL_NAME)
    data["gates"] = [{"id": g, "passed_at": "2026-10-25T05:00:00Z"} for g in journal.GATE_IDS[:6]]
    gc.write_json(pkg / gc.JOURNAL_NAME, data)
    (pkg / "02-brand/naming-decision.md").write_text("# Naming\n\nPropose Filmora. Clearance UNVERIFIED.\n")
    (pkg / "03-site/index.html").write_text("<h1>Filmora</h1><p>Join at getfilmora.app</p>\n")
    return mandu, pkg


class NameRerunPrepTest(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.dict(os.environ)
        patcher.start()
        self.addCleanup(patcher.stop)
        for key in ("GR0WTHPILOT_REPO", "GR0WTHPILOT_CONFIG"):
            os.environ.pop(key, None)
        os.environ["GR0WTHLAB_DIR"] = str(registry().parent.parent)
        self.mandu, self.pkg = renamable_mandu()
        os.environ["CLAUDE_CONFIG_DIR"] = str(consent_file(self.mandu).parent)
        self.cache = Path(tempfile.mkdtemp(prefix="gp-cache-")).resolve()

    def prepare(self, **flags):
        fields = {"mandu": str(self.mandu), "product": "Testprod", "cache": str(self.cache), "repo": None,
                  "today": "2026-10-28", "rename": None, "rule_out": None, "rule_out_root": None,
                  "accept_name": None}
        fields.update(flags)
        return gp_run.prepare(type("A", (), fields))

    def backups(self):
        folder = self.cache / "Testprod" / "backups"
        return sorted(p.name for p in folder.iterdir()) if folder.is_dir() else []

    def test_rerun_then_accept_keep_a_copy_before_each_change(self):
        before = (self.pkg / gc.JOURNAL_NAME).read_text()
        cfg = self.prepare(rename="Filmora", rule_out=["Shutterly"], rule_out_root=["Film"])
        self.assertEqual((cfg["mode"], cfg["rename_step"]), ("resume", "rerun"))
        self.assertIn("Name-only rerun from Filmora; ruled out: Filmora, Shutterly; roots: Film.", cfg["rename_summary"])
        copies = self.backups()
        self.assertEqual(len(copies), 1)
        self.assertTrue(copies[0].endswith("-before-rerun-from-filmora"))
        copy = self.cache / "Testprod" / "backups" / copies[0]
        self.assertEqual((copy / gc.JOURNAL_NAME).read_text(), before)
        self.assertTrue((copy / "02-brand/tournament/scorecard.md").is_file())
        self.assertIn(str(copy), cfg["rename_summary"])
        data = gc.read_json(self.pkg / gc.JOURNAL_NAME)
        self.assertEqual(journal.reopened_ids(data), ["tournament", "brand", "claims-1", "critic-1"])
        self.assertEqual(data["rename"]["backups"][0]["path"], str(copy))
        self.assertTrue(any(str(copy) in n["text"] for n in data["notes"]))
        self.assertEqual(len(data["sessions"]), 1)
        self.assertTrue((self.pkg / "02-brand/tournament-filmora/scorecard.md").is_file())

        with self.assertRaises(gp_run.RunError) as raised:
            self.prepare(accept_name="Cinewell")
        self.assertIn("has not recorded its shortlist", str(raised.exception))
        self.assertEqual(len(self.backups()), 1)

        data["gates"][2].pop("reopened_at")
        data["rename"].update(shortlist="02-brand/name-shortlist.md", shortlist_names=["Cinewell", "Rollbook"])
        gc.write_json(self.pkg / gc.JOURNAL_NAME, data)
        for name in ("Filmwise", "shutterly"):
            with self.assertRaises(gp_run.RunError):
                self.prepare(accept_name=name)
        self.assertEqual(len(self.backups()), 1)
        cfg = self.prepare(accept_name="Cinewell")
        self.assertEqual(cfg["rename_step"], "accept")
        self.assertEqual(len(self.backups()), 2)
        self.assertIn("<h1>Filmora</h1>", (self.cache / "Testprod/backups" / self.backups()[1] / "03-site/index.html")
                      .read_text())
        self.assertEqual((self.pkg / "03-site/index.html").read_text(), "<h1>Cinewell</h1><p>Join at getcinewell.app</p>\n")
        data = gc.read_json(self.pkg / gc.JOURNAL_NAME)
        self.assertEqual(data["rename"]["stage"], "swapped")
        self.assertTrue(Path(data["rename"]["swap"]["review"]).is_file())
        self.assertTrue(guard.under(data["rename"]["swap"]["review"], self.cache / "Testprod"))
        self.assertEqual(journal.next_gate(data)[0], "brand")

        resumed = self.prepare()
        self.assertEqual((resumed["mode"], resumed["rename_step"], resumed["rename_summary"]), ("resume", None, None))
        self.assertEqual(len(self.backups()), 2)
        self.assertEqual(gc.read_json(self.pkg / gc.JOURNAL_NAME)["rename"], data["rename"])

    def test_rerun_refusals_change_nothing(self):
        before = (self.pkg / gc.JOURNAL_NAME).read_text()
        for flags, message in (
                ({"rename": "Filmora", "accept_name": "Cinewell"}, "give one of them"),
                ({"rule_out": ["Shutterly"]}, "go with --rename"),
                ({"rename": "Filmora", "rule_out_root": ["F"]}, "2 to 40 letters"),
                ({"rename": "Flimora"}, "does not appear in"),
                ({"accept_name": "Cinewell"}, "no name-only rerun is waiting")):
            with self.assertRaises(gp_run.RunError) as raised:
                self.prepare(**flags)
            self.assertIn(message, str(raised.exception), flags)
        self.assertEqual((self.pkg / gc.JOURNAL_NAME).read_text(), before)
        self.assertEqual(self.backups(), [])
        data = gc.read_json(self.pkg / gc.JOURNAL_NAME)
        data["gates"] = data["gates"][:2]
        gc.write_json(self.pkg / gc.JOURNAL_NAME, data)
        with self.assertRaises(gp_run.RunError) as raised:
            self.prepare(rename="Filmora")
        self.assertIn("has not passed its tournament", str(raised.exception))
        data["status"] = "complete"
        gc.write_json(self.pkg / gc.JOURNAL_NAME, data)
        with self.assertRaises(gp_run.RunError) as raised:
            self.prepare(rename="Filmora")
        self.assertIn("reworks an unfinished run's Candidate Package", str(raised.exception))
        self.assertEqual(self.backups(), [])

    def test_preflight_reports_the_rename(self):
        cfg = self.prepare(rename="Filmora")
        os.environ["GP_PREFLIGHT"] = "abcdef123456"
        (Path(cfg["work"]) / "guard-receipt-abcdef123456").write_text("seen")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(gp_run.preflight(type("A", (), {"config": cfg["config_path"]})), 0)
        report = json.loads(out.getvalue())
        self.assertEqual((report["rename_step"], report["rename"]["stage"]), ("rerun", "shortlist"))
        self.assertEqual(report["gates_passed"], ["product-facts", "research"])
        self.assertEqual(report["gates_reopened"], ["tournament", "brand", "claims-1", "critic-1"])


class LauncherTest(unittest.TestCase):
    """bin/gr0wthpilot itself, with stand-ins for claude and caffeinate."""

    def setUp(self):
        self.mandu, self.pkg = renamable_mandu()
        self.mandu = self.mandu.resolve()
        (self.mandu / "bin").mkdir()
        shutil.copy(str(fixtures.SCRIPTS.parent.parent.parent.parent / "bin" / "gr0wthpilot"), str(self.mandu / "bin"))
        (self.mandu / ".claude" / "skills").mkdir(parents=True)
        os.symlink(str(fixtures.SCRIPTS.parent), str(self.mandu / ".claude/skills/gr0wthpilot"))
        stubs = Path(tempfile.mkdtemp(prefix="gp-stubs-"))
        self.calls = stubs / "claude-calls.txt"
        (stubs / "claude").write_text('#!/bin/sh\nprintf "%%s\\n" "$PWD" "$GR0WTHPILOT_CONFIG" "$@" > %s\n' % self.calls)
        (stubs / "caffeinate").write_text("#!/bin/sh\nexit 0\n")
        for stub in ("claude", "caffeinate"):
            os.chmod(str(stubs / stub), 0o755)
        self.cache = Path(tempfile.mkdtemp(prefix="gp-cache-"))
        self.env = {k: v for k, v in os.environ.items() if k not in ("GR0WTHPILOT_REPO", "GR0WTHPILOT_CONFIG")}
        self.env.update(PATH="%s:%s" % (stubs, os.environ["PATH"]), GR0WTHPILOT_WORK=str(self.cache),
                        GR0WTHLAB_DIR=str(registry().parent.parent),
                        CLAUDE_CONFIG_DIR=str(consent_file(self.mandu).parent))

    def launch(self, *args):
        return subprocess.run([str(self.mandu / "bin" / "gr0wthpilot")] + list(args), env=self.env,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, timeout=60)

    def test_rename_and_accept_reach_prepare_and_open_the_same_session(self):
        out = self.launch("Testprod", "--rename", "Filmora", "--rule-out", "Shutterly", "--rule-out-root", "Film")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("Name-only rerun from Filmora; ruled out: Filmora, Shutterly; roots: Film.", out.stdout)
        called = self.calls.read_text().splitlines()
        self.assertEqual(Path(called[0]).resolve(), self.pkg.resolve())
        self.assertEqual(called[-1], "/gr0wthpilot Testprod")
        self.assertIn("dontAsk", called)
        self.assertEqual(gc.read_json(Path(called[1]))["rename_step"], "rerun")
        self.assertEqual(gc.read_json(self.pkg / gc.JOURNAL_NAME)["rename"]["stage"], "shortlist")

        out = self.launch("Testprod", "--accept-name", "Cinewell")
        self.assertEqual(out.returncode, 2)
        self.assertIn("has not recorded its shortlist yet", out.stderr)

    def test_plain_resume_is_unchanged(self):
        out = self.launch("Testprod")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("Gr0wthPilot: Testprod (resume run, first-package)", out.stdout)
        self.assertNotIn("Name", out.stdout)
        cfg = gc.read_json(Path(self.calls.read_text().splitlines()[1]))
        self.assertIsNone(cfg["rename_step"])
        self.assertNotIn("rename", gc.read_json(self.pkg / gc.JOURNAL_NAME))
        self.assertFalse((self.cache / "Testprod" / "backups").exists())

    def test_bad_arguments_stop_before_anything_runs(self):
        for args, message in ((["Testprod", "--rename"], "Usage:"),
                              (["Testprod", "--bogus"], "unknown option --bogus"),
                              (["Testprod", "--rename", "Filmora", "--accept-name", "X"], "give one of them")):
            out = self.launch(*args)
            self.assertEqual(out.returncode, 2, args)
            self.assertIn(message, out.stdout + out.stderr, args)
        self.assertFalse(self.calls.exists())
        self.assertFalse((self.cache / "Testprod" / "backups").exists())


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

    def test_gp_chrome_rebuilds_local_urls_and_refuses_tricks(self):
        chrome = load_wrapper("gp-chrome")
        self.assertEqual(chrome.page_source(self.cfg, "http://LOCALHOST:8080/a/index.html?v=b#top"),
                         ("url", "http://localhost:8080/a/index.html?v=b", None))
        for bad in ("http://evil.example\\@localhost/", "http://user@localhost:8080/", "http://localhost.evil.example/",
                    "https://localhost/", "http://localhost:8080/a b", "http://localhost:99999/", "http://localhost:0/"):
            with self.assertRaises(chrome.ToolError, msg=bad):
                chrome.page_source(self.cfg, bad)

    def test_gp_chrome_measures_a_local_file_from_a_probe_in_the_cache(self):
        chrome = load_wrapper("gp-chrome")
        page = Path(self.cfg["package"]) / "index.html"
        page.write_text("<p>x</p>")
        seen = {}

        def run_chrome(cfg, extra, url, timeout=120):
            seen["extra"], seen["url"] = extra, url
            wrapper = http_get(url)[1]
            seen["copy_url"] = urllib.parse.urljoin(url, re.search(r'src="([^"]+)"', wrapper).group(1))
            seen["copy_text"] = http_get(seen["copy_url"])[1]
            return types.SimpleNamespace(stdout='<pre id="gp-measure">{"scrollWidth": 390, "innerWidth": 390, '
                                                '"innerHeight": 844}</pre>', stderr="")

        chrome.run_chrome = run_chrome
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            chrome.cmd_measure(self.cfg, [str(page), "390x844"])
        self.assertTrue(seen["url"].startswith("http://127.0.0.1:"))
        self.assertTrue(seen["copy_text"].startswith("<p>x</p>"))
        self.assertNotIn("--allow-file-access-from-files", seen["extra"])
        self.assertEqual(sorted(p.name for p in page.parent.iterdir()), ["index.html"])
        self.assertFalse(json.loads(out.getvalue())["overflows"])
        with self.assertRaises(chrome.ToolError):
            chrome.cmd_measure(self.cfg, ["http://localhost:8000/index.html", "390x844"])

    @unittest.skipUnless(Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome").is_file(),
                         "Google Chrome is not installed")
    def test_gp_chrome_measure_gives_a_page_no_access_to_local_files(self):
        chrome = load_wrapper("gp-chrome")
        secret = Path(tempfile.mkdtemp(prefix="gp-secret-")) / "hosts.yml"
        secret.write_text("TOKEN-123\n")
        page = Path(self.cfg["package"]) / "03-site" / "index.html"
        page.parent.mkdir()
        page.write_text("<!doctype html><html><body style=\"margin:0\"><div id=\"box\">x</div><script>\n"
                        "var ok = false;\ntry { var x = new XMLHttpRequest(); x.open('GET', '%s', false); x.send();\n"
                        "  ok = x.responseText.indexOf('TOKEN-123') >= 0; } catch (e) {}\n"
                        "document.getElementById('box').style.width = ok ? '3000px' : '100px';\n"
                        "</script></body></html>\n" % secret.as_uri())
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            chrome.cmd_measure(self.cfg, [str(page), "390x844"])
        measured = json.loads(out.getvalue())
        self.assertEqual((measured["scrollWidth"], measured["overflows"]), (390, False))

    def test_gp_chrome_opens_only_local_pages(self):
        chrome = load_wrapper("gp-chrome")
        page = Path(self.cfg["package"]) / "index.html"
        page.write_text("<p>x</p>")
        root = Path(self.cfg["package"]).resolve()
        self.assertEqual(chrome.page_source(self.cfg, str(page)), ("file", page.resolve(), root))
        self.assertEqual(chrome.page_source(self.cfg, page.resolve().as_uri()), ("file", page.resolve(), root))
        self.assertEqual(chrome.page_source(self.cfg, "http://localhost:8080/"),
                         ("url", "http://localhost:8080/", None))
        for bad in ("https://example.com", "http://192.168.1.2/", "/etc/hosts"):
            with self.assertRaises(chrome.ToolError):
                chrome.page_source(self.cfg, bad)

    def test_gp_chrome_serves_the_area_that_holds_the_page(self):
        chrome = load_wrapper("gp-chrome")
        outside = Path(tempfile.mkdtemp(prefix="gp-secret-")) / "secret.txt"
        outside.write_text("TOKEN-123\n")
        pkg = Path(self.cfg["package"])
        slide = pkg / "10-launch-set" / "carousel-1" / "slide-01.html"
        slide.parent.mkdir(parents=True)
        slide.write_text('<link rel="stylesheet" href="../shared.css"><p>slide</p>')
        (pkg / "10-launch-set" / "shared.css").write_text("body { color: red }")
        (pkg / "10-launch-set" / "leak.txt").symlink_to(outside)
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            with chrome.opened(self.cfg, str(slide)) as url:
                self.assertEqual(http_get(url)[0], 200)
                self.assertEqual(http_get(urllib.parse.urljoin(url, "../shared.css")), (200, "body { color: red }"))
                self.assertEqual(http_get(urllib.parse.urljoin(url, "../leak.txt"))[0], 403)
                self.assertEqual(http_get(urllib.parse.urljoin(url, "../missing.css"))[0], 404)
        self.assertIn("leak.txt (HTTP 403)", err.getvalue())
        self.assertIn("missing.css (HTTP 404)", err.getvalue())
        with self.assertRaises(OSError):
            http_get(url)
        (pkg / "old").mkdir()
        (pkg / "old" / "x.css").write_text("old")
        with contextlib.redirect_stderr(io.StringIO()):
            with chrome.served(pkg, [str(pkg / "old")]) as base:
                self.assertEqual(http_get(base + "old/x.css")[0], 403)
                self.assertEqual(http_get(base + "10-launch-set/shared.css")[0], 200)

    @unittest.skipUnless(Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome").is_file()
                         and shutil.which("ffmpeg"), "Google Chrome or ffmpeg is not installed")
    def test_gp_chrome_does_not_show_a_framed_local_file(self):
        chrome = load_wrapper("gp-chrome")
        secret = Path(tempfile.mkdtemp(prefix="gp-secret-")) / "secret.html"
        secret.write_text("<!doctype html><html><body style=\"margin:0;background:#ff0000\"></body></html>")
        site = Path(self.cfg["package"]) / "03-site"
        site.mkdir()
        (site / "leak.html").symlink_to(secret)
        frame = '<!doctype html><html><body style="margin:0;background:#ffffff"><iframe src="%s" ' \
                'style="position:fixed;top:0;left:0;width:100%%;height:100%%;border:0"></iframe></body></html>'
        for name, src in (("direct.html", secret.as_uri()), ("symlink.html", "leak.html")):
            (site / name).write_text(frame % src)
            shot = Path(self.cfg["work"]) / (name + ".png")
            with contextlib.redirect_stdout(io.StringIO()):
                chrome.cmd_screenshot(self.cfg, [str(site / name), str(shot), "390x844"])
            pixel = subprocess.run(["ffmpeg", "-v", "error", "-i", str(shot), "-vf", "crop=1:1:195:422", "-f",
                                    "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE, check=True).stdout
            self.assertNotEqual(tuple(pixel[:3]), (255, 0, 0), name)

    @unittest.skipUnless(Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome").is_file()
                         and shutil.which("ffmpeg"), "Google Chrome or ffmpeg is not installed")
    def test_gp_chrome_screenshot_lays_the_page_out_at_the_asked_size(self):
        chrome = load_wrapper("gp-chrome")
        page = Path(self.cfg["package"]) / "03-site" / "probe.html"
        page.parent.mkdir()
        # Two squares whose colors spell the page's innerWidth and innerHeight.
        page.write_text("<!doctype html><html><body style=\"margin:0\"><div id=\"w\"></div><div id=\"h\"></div><script>\n"
                        "function paint(id, n) { var s = document.getElementById(id).style;\n"
                        "  s.width = s.height = '20px'; s.background = 'rgb(' + (n >> 8) + ',' + (n & 255) + ',0)'; }\n"
                        "paint('w', innerWidth); paint('h', innerHeight);\n</script></body></html>\n")
        for width, height, scale in ((390, 844, "1"), (200, 200, "1"), (1440, 900, "1"), (390, 844, "2")):
            shot = Path(self.cfg["work"]) / ("probe-%dx%d@%s.png" % (width, height, scale))
            with contextlib.redirect_stdout(io.StringIO()):
                chrome.cmd_screenshot(self.cfg, [str(page), str(shot), "%dx%d" % (width, height), "--scale", scale])
            size = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=width,height", "-of",
                                   "csv=p=0", str(shot)], stdout=subprocess.PIPE, universal_newlines=True).stdout
            self.assertEqual(size.strip(), "%d,%d" % (width * int(scale), height * int(scale)))
            seen = []
            for y in (5, 25):
                pixel = subprocess.run(["ffmpeg", "-v", "error", "-i", str(shot), "-vf", "crop=1:1:5:%d" % (
                    y * int(scale)), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE,
                    check=True).stdout
                seen.append(pixel[0] * 256 + pixel[1])
            self.assertEqual(seen, [width, height], "%dx%d at scale %s" % (width, height, scale))
        self.assertEqual(sorted(p.name for p in page.parent.iterdir()), ["probe.html"])

    def test_gp_chrome_opens_only_local_pages_by_its_own_server(self):
        chrome = load_wrapper("gp-chrome")
        page = Path(self.cfg["package"]) / "index.html"
        page.write_text("<p>x</p>")
        seen = []
        chrome.run_chrome = lambda cfg, extra, url, timeout=120: seen.append(url) or types.SimpleNamespace(
            stdout="", stderr="")
        with contextlib.redirect_stdout(io.StringIO()):
            chrome.cmd_dom(self.cfg, [str(page)])
        self.assertTrue(seen[0].startswith("http://127.0.0.1:") and seen[0].endswith("/index.html"), seen)

    def test_gp_xcodebuild_builds_only_for_the_simulator(self):
        xb = load_wrapper("gp-xcodebuild")
        src = exported_copy(xb, self.cfg) / "App.xcodeproj"
        ok = ["-project", str(src), "-scheme", "App", "-destination", "generic/platform=iOS Simulator", "build"]
        xb.check_args(self.cfg, ok)
        for bad in (["archive"], ["-exportArchive"], ["-allowProvisioningUpdates"], ["DEVELOPMENT_TEAM=X"],
                    ["-destination", "generic/platform=iOS"], ["-sdk", "iphoneos"],
                    ["-destination", "platform=iOS Simulator,id=NOT-MINE"]):
            with self.assertRaises(xb.ToolError, msg=str(bad)):
                xb.check_args(self.cfg, ok[:4] + bad + ["build"])
        with self.assertRaises(xb.ToolError):
            xb.check_args(self.cfg, ["-project", "/Users/someone/Developer/App/App.xcodeproj", "build"])

    def test_gp_xcodebuild_confines_every_build_to_the_simulator_sdk(self):
        xb = load_wrapper("gp-xcodebuild")
        copy = exported_copy(xb, self.cfg)
        base = ["-project", str(copy / "App.xcodeproj"), "-scheme", "App"]
        for action in ("build", "build-for-testing", "analyze", "clean"):
            with self.assertRaises(xb.ToolError, msg=action):
                xb.check_args(self.cfg, base + [action])
        for implicit in ([], ["-target", "App"], ["-alltargets"], ["-configuration", "Debug", "-quiet"]):
            with self.assertRaises(xb.ToolError, msg=str(implicit)):
                xb.check_args(self.cfg, base + implicit)
            xb.check_args(self.cfg, base + implicit + ["-sdk", "iphonesimulator"])
        for sdk in ("iphonesimulator", "iphonesimulator26.0"):
            xb.check_args(self.cfg, base + ["-sdk", sdk, "build"])
        for bad in (["-sdk", "iphonesimulatorx"], ["-sdk", "iphoneos"], ["-sdk", "macosx"],
                    ["-sdk", "iphonesimulator", "SDKROOT=iphoneos"],
                    ["-destination", "generic/platform=iOS Simulator", "SDKROOT=macosx"],
                    ["-sdk", "iphonesimulator", "-xcconfig", str(copy / "Device.xcconfig")],
                    ["-sdk", "iphonesimulator", "-xcconfig", str(copy / "Outside.xcconfig")]):
            with self.assertRaises(xb.ToolError, msg=str(bad)):
                xb.check_args(self.cfg, base + bad + ["build"])
        for good in (["-sdk", "iphonesimulator", "SDKROOT=iphonesimulator"],
                     ["-sdk", "iphonesimulator", "-xcconfig", str(copy / "Simulator.xcconfig")]):
            xb.check_args(self.cfg, base + good + ["build"])
        for info in (["-showBuildSettings"], ["-showdestinations"], ["-showTestPlans", "-json"]):
            xb.check_args(self.cfg, base + info)
        config = Path(self.cfg["state"]) / "guard-config.json"
        gc.write_json(config, self.cfg)
        envs = []
        with mock.patch.dict(os.environ, {"GR0WTHPILOT_CONFIG": str(config), "XCODE_XCCONFIG_FILE": "/tmp/x.xcconfig"}), \
                mock.patch.object(xb.subprocess, "call", lambda argv, env=None: envs.append(env) or 0):
            self.assertEqual(xb.main(base + ["-sdk", "iphonesimulator", "build"]), 0)
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(xb.main(base + ["-sdk", "iphoneos", "build"]), 1)
                self.assertEqual(xb.main(base), 1)
        self.assertEqual(len(envs), 1)
        self.assertNotIn("XCODE_XCCONFIG_FILE", envs[0])

    def test_gp_xcodebuild_tests_only_on_a_run_simulator(self):
        xb = load_wrapper("gp-xcodebuild")
        src = exported_copy(xb, self.cfg) / "App.xcodeproj"
        gc.write_json(Path(self.cfg["simulators"]), {"devices": [{"udid": "MINE", "name": "Gr0wthPilot-Immerse-1"}]})
        base = ["-project", str(src), "-scheme", "App"]
        for dest in ("generic/platform=iOS Simulator", "platform=iOS Simulator", "platform=iOS Simulator,OS=26.0"):
            xb.check_args(self.cfg, base + ["-destination", dest, "build"])
            for action in ("test", "test-without-building"):
                with self.assertRaises(xb.ToolError, msg="%s %s" % (dest, action)):
                    xb.check_args(self.cfg, base + ["-destination", dest, action])
        with self.assertRaises(xb.ToolError):
            xb.check_args(self.cfg, base + ["test"])
        for dest in ("platform=iOS Simulator,id=MINE", "platform=iOS Simulator,name=Gr0wthPilot-Immerse-1"):
            xb.check_args(self.cfg, base + ["-destination", dest, "test"])

    def test_gp_xcodebuild_builds_only_a_verified_copy_in_the_guard_folder(self):
        xb = load_wrapper("gp-xcodebuild")
        copy = exported_copy(xb, self.cfg)
        self.assertTrue(guard.under(copy, self.cfg["build"]))
        project, work, build = copy / "App.xcodeproj", Path(self.cfg["work"]), Path(self.cfg["build"])
        base = ["-project", str(project), "-scheme", "App", "-destination", "generic/platform=iOS Simulator"]
        (project / "project.pbxproj").write_text("// a Run Script phase someone added\n")
        (copy / "extra.sh").write_text("open x\n")
        xb.check_args(self.cfg, base + ["build"])
        self.assertEqual((project / "project.pbxproj").read_text(), "// the Founder's project\n")
        self.assertFalse((copy / "extra.sh").exists())
        (work / "App.xcodeproj").mkdir()
        for bad in (["-project", str(work / "App.xcodeproj")], ["-xcconfig", str(work / "x.xcconfig")],
                    ["-derivedDataPath", str(work / "DD")], ["-clonedSourcePackagesDirPath", str(work)],
                    ["-testPlan", "../plan"], ["CONFIGURATION_BUILD_DIR=$(HOME)/out"], ["SYMROOT=${HOME}/out"],
                    ["SYMROOT=../../out"], ["OTHER_CFLAGS=-I%s" % work], ["SYMROOT=%s" % work],
                    ["-resultBundlePath", str(build / "r.xcresult")],
                    ["-resultStreamPath", str(Path(self.cfg["protected"][0]) / "recap.html")],
                    ["-archivePath", str(work / "a.xcarchive")], ["-someNewOption"], ["docbuild"],
                    ["-xctestrun", str(build / "x.xctestrun")], ["-downloadAllPlatforms"],
                    ["-resolvePackageDependencies"]):
            with self.assertRaises(xb.ToolError, msg=str(bad)):
                xb.check_args(self.cfg, base + bad + ["build"])
        for good in (["-xcconfig", str(copy / "Config.xcconfig")], ["-testPlan", "Smoke"], ["ONLY_ACTIVE_ARCH=YES"],
                     ["-resultBundlePath", str(work / "r.xcresult")], ["SYMROOT=%s" % (build / "out")]):
            xb.check_args(self.cfg, base + good + ["build"])
        config = Path(self.cfg["state"]) / "guard-config.json"
        gc.write_json(config, self.cfg)
        calls = []
        with mock.patch.dict(os.environ, {"GR0WTHPILOT_CONFIG": str(config)}), \
                mock.patch.object(xb.subprocess, "call", lambda argv, env=None: calls.append(argv) or 0):
            self.assertEqual(xb.main(base + ["build"]), 0)
            self.assertEqual(xb.main(["-project", str(project), "-scheme", "App", "-showBuildSettings"]), 0)
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(xb.main(["-project", str(project), "-resolvePackageDependencies"]), 1)
            # xcodebuild cannot run -list with a -derivedDataPath, so it is refused.
            for listing in (["-project", str(project), "-list"], ["-project", str(project), "-scheme", "App", "-list"]):
                err = io.StringIO()
                with contextlib.redirect_stderr(err):
                    self.assertEqual(xb.main(listing), 1)
                self.assertEqual(len(err.getvalue().splitlines()), 1, err.getvalue())
                self.assertIn("-list is not supported", err.getvalue())
                self.assertIn("references/app-screens.md", err.getvalue())
        self.assertEqual(len(calls), 2)
        for call in calls:
            self.assertEqual(call[call.index("-derivedDataPath") + 1], str(build / "DerivedData"))

    def test_gp_sim_installs_only_an_app_from_the_build_folder(self):
        sim = load_wrapper("gp-sim")
        gc.write_json(Path(self.cfg["simulators"]), {"devices": [{"udid": "MINE", "name": "Gr0wthPilot-Immerse-1"}]})
        sim.all_devices = lambda: {"MINE": {"udid": "MINE", "name": "Gr0wthPilot-Immerse-1", "state": "Booted"}}
        calls = []
        sim.simctl = lambda args, check=True, capture=True: calls.append(args) or types.SimpleNamespace(
            returncode=0, stdout="", stderr="")
        tampered = Path(self.cfg["work"]) / "App.app"
        tampered.mkdir()
        with self.assertRaises(sim.ToolError):
            sim.cmd_install(self.cfg, ["MINE", str(tampered)])
        built = Path(self.cfg["build"]) / "DerivedData" / "Build" / "App.app"
        built.mkdir(parents=True)
        with contextlib.redirect_stdout(io.StringIO()):
            sim.cmd_install(self.cfg, ["MINE", str(built)])
        self.assertEqual(calls[-1][:2], ["install", "MINE"])

    def test_gp_sim_cleanup_records_exactly_the_devices_that_are_gone(self):
        sim = load_wrapper("gp-sim")
        gc.write_json(Path(self.cfg["simulators"]), {"devices": [
            {"udid": "STUCK", "name": "Gr0wthPilot-Immerse-1"}, {"udid": "GONE", "name": "Gr0wthPilot-Immerse-2"},
            {"udid": "OK", "name": "Gr0wthPilot-Immerse-3"}], "recordings": {}})
        devices = {"STUCK": {"udid": "STUCK", "name": "Gr0wthPilot-Immerse-1", "state": "Booted"},
                   "OK": {"udid": "OK", "name": "Gr0wthPilot-Immerse-3", "state": "Shutdown"},
                   "THEIRS": {"udid": "THEIRS", "name": "iPhone 17 Pro", "state": "Booted"}}
        calls = []

        def simctl(args, check=True, capture=True):
            calls.append(args)
            if args == ["delete", "OK"]:
                del devices["OK"]
            return types.SimpleNamespace(returncode=0, stdout="", stderr="")

        sim.simctl = simctl
        sim.all_devices = lambda: {k: dict(v) for k, v in devices.items()}
        with contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(sim.ToolError):
                sim.cmd_cleanup(self.cfg, [])
        ledger = gc.read_json(Path(self.cfg["simulators"]))
        self.assertEqual({d["udid"]: bool(d.get("deleted_at")) for d in ledger["devices"]},
                         {"STUCK": False, "GONE": True, "OK": True})
        self.assertFalse([c for c in calls if "THEIRS" in c])
        devices.pop("STUCK")
        with contextlib.redirect_stdout(io.StringIO()):
            sim.cmd_cleanup(self.cfg, [])
        self.assertTrue(all(d.get("deleted_at") for d in gc.read_json(Path(self.cfg["simulators"]))["devices"]))

    def test_gp_last30days_keeps_paid_sources_off(self):
        l30 = load_wrapper("gp-last30days")
        os.environ["GR0WTHPILOT_CONFIG"] = str(Path(self.cfg["work"]) / "c.json")
        gc.write_json(Path(os.environ["GR0WTHPILOT_CONFIG"]), self.cfg)
        try:
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(l30.main(["film", "--out", str(Path(self.cfg["package"]) / "r"), "--sources", "reddit,tiktok"]), 1)
                self.assertEqual(l30.main(["film", "--out", "/tmp/elsewhere"]), 1)
        finally:
            del os.environ["GR0WTHPILOT_CONFIG"]


if __name__ == "__main__":
    unittest.main()
