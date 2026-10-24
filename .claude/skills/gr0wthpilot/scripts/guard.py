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
    # Shell builtins that run a command later or under another name.
    "alias", "hash", "enable", "trap", "bind", "complete", "compgen", "fc",
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
# Programs that run another program, with their options: those that take no
# value, and those that take one (as the next word, or attached). An option
# not listed could hide the program the wrapper runs, so it is refused.
WRAPPER_OPTIONS = {
    "env": ({"-i", "-", "--ignore-environment"}, {"-u", "--unset", "-C", "--chdir"}),
    "nohup": (set(), set()),
    "time": ({"-p", "-l"}, set()),
    "command": ({"-p", "-v", "-V"}, set()),
    "builtin": (set(), set()),
    "noglob": (set(), set()),
    "nocorrect": (set(), set()),
    "exec": ({"-c", "-l"}, {"-a"}),
    "nice": (set(), {"-n"}),
    "timeout": ({"--preserve-status", "--foreground", "-v", "--verbose"},
                {"-s", "--signal", "-k", "--kill-after"}),
    "caffeinate": ({"-d", "-i", "-m", "-s", "-u"}, {"-t", "-w"}),
    "stdbuf": (set(), {"-i", "-o", "-e", "--input", "--output", "--error"}),
    "xargs": ({"-0", "-t", "-r", "-x", "-o", "-p", "--null", "--no-run-if-empty"},
              {"-I", "-J", "-L", "-n", "-P", "-s", "-E", "-d", "-R", "-a"}),
}
# Shell reserved words that come before the command they run.
SHELL_KEYWORDS = {"if", "then", "else", "elif", "do", "while", "until", "!", "coproc", "{", "}"}
SHELLS = {"bash", "sh", "zsh", "dash", "ksh"}
SHELL_SUFFIXES = {".sh", ".bash", ".zsh", ".command"}
ASSIGNMENT_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*=.*")
# Variables that make a shell or interpreter load or run code the guard
# never sees. A run neither sets nor names them: a word that is one of them,
# assigns one, or points a name at one (`declare -n ref=BASH_ENV`) is refused.
CODE_ENV_RE = re.compile(
    r"(?:[A-Za-z_][A-Za-z0-9_]*=)?(BASH_ENV|ENV|ZDOTDIR|PS4|PROMPT_COMMAND|SHELLOPTS|BASHOPTS|NODE_OPTIONS|"
    r"NODE_PATH|PYTHONPATH|PYTHONSTARTUP|PYTHONHOME|PYTHONINSPECT|PERL5OPT|PERL5LIB|PERLLIB|RUBYOPT|RUBYLIB|"
    r"LD_PRELOAD|LD_LIBRARY_PATH|DYLD_INSERT_LIBRARIES|DYLD_LIBRARY_PATH|DYLD_FRAMEWORK_PATH)(?:=.*)?", re.S)
# The only modules `python -m` may run: the standard library's own.
PYTHON_MODULES = {"http.server", "json.tool"}
# How each family of shells and interpreters is told what to run: the short
# option letters that start inline code, name a module, load a code file, or
# take a value (attached, or as the next argument), and the long options
# that take inline code, load a code file (read and checked like a script),
# take a value, or are refused because they load code the guard cannot read.
# A shell's -c makes its first argument the code; -s makes it read stdin.
ARGV_RULES = {
    "shell": {"inline": "c", "valued": "oO", "load_options": {"--rcfile", "--init-file"}},
    "python": {"inline": "c", "module": "m", "valued": "XW"},
    "node": {"inline_options": {"-e", "--eval", "-p", "--print"},
             "load_options": {"-r", "--require", "--import", "--loader", "--experimental-loader", "--preload"},
             "valued_options": {"-C", "--conditions", "--input-type"},
             "refused_options": {"--import-map", "--config", "-c"}},
    "deno": {"refused_options": {"--import-map", "--config", "-c"}},
    "ruby": {"inline": "e", "load": "r", "refused": "I", "valued": "C"},
    "perl": {"inline": "eE", "refused": "IMm"},
}
SIMPLER = "the command holds %s, which the guard cannot follow with certainty; write it more simply"
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
    can be checked against it, and an unquoted heredoc's $(...) and
    backticks run like any other. A `#` that starts a word (at the start, or
    after unescaped whitespace, `;`, `|`, or `&`) starts a comment; an escaped
    character never ends a word. What the guard cannot follow with certainty
    (an escaped space or operator before `#`, `${...}` holding `#`, an operator,
    or a quote, ANSI-C quoting, an odd heredoc, unbalanced quotes) is refused.
    Returns ([(command, heredoc body or None)], has_redirect, is_compound)."""
    parts, nested, current = [], [], []
    bodies, pending = [], []
    i, n = 0, len(command)
    quote = None
    redirect = False
    word_start = True

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
            elif quote == '"' and ch == "`":
                end = command.find("`", i + 1)
                if end == -1:
                    raise Deny(SIMPLER % "an unbalanced backtick")
                nested.append(command[i + 1:end])
                current.append(command[i + 1:end + 1])
                i = end
            i += 1
            continue
        if command.startswith("<<", i) and not command.startswith("<<<", i):
            m = HEREDOC_RE.match(command, i)
            if not m or (m.end() < n and command[m.end()] not in " \t\n;|&<>()"):
                raise Deny(SIMPLER % "a heredoc whose delimiter is not one plain word")
            quoted = bool(m.group(2) or m.group(3)) or "\\" in m.group(0)
            pending.append((m.group(1) == "-", m.group(2) or m.group(3) or m.group(4), quoted))
            current.append(m.group(0))
            redirect = True
            word_start = False
            i = m.end()
            continue
        if ch == "\n" and pending:
            current = finish()
            owner = len(parts) - 1
            i += 1
            for strip_tabs, delimiter, quoted in pending:
                lines = []
                while i <= n:
                    end = command.find("\n", i)
                    line = command[i:] if end == -1 else command[i:end]
                    i = n + 1 if end == -1 else end + 1
                    if (line.lstrip("\t") if strip_tabs else line) == delimiter:
                        break
                    lines.append(line)
                body = "\n".join(lines)
                if not quoted:
                    nested.extend(substitutions(body))
                if owner >= 0:
                    bodies[owner] = body if bodies[owner] is None else bodies[owner] + "\n" + body
            pending = []
            word_start = True
            continue
        if ch == "#" and word_start:
            end = command.find("\n", i)
            i = n if end == -1 else end
            continue
        boundary = ch in " \t\n;|&"
        if ch in ("'", '"'):
            quote = ch
            current.append(ch)
        elif command.startswith("$'", i):
            raise Deny(SIMPLER % "ANSI-C quoting ($'...')")
        elif ch == "\\" and i + 1 < n:
            if command[i + 1] in " \t;|&()<>" and command[i + 2:i + 3] == "#":
                raise Deny(SIMPLER % "an escaped space or operator before #")
            current.append(command[i:i + 2])
            i += 1
        elif command.startswith("${", i):
            end = command.find("}", i + 2)
            if end == -1 or re.search(r"[#;|&()<>`'\"\\{$\n]", command[i + 2:end]):
                raise Deny(SIMPLER % "a ${...} expansion holding #, an operator, or a quote")
            current.append(command[i:end + 1])
            i = end
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
        elif ch in ";|&\n()":
            if ch in "&|" and current and current[-1].endswith(">"):
                current.append(ch)
            else:
                current = finish()
        else:
            if ch in "<>":
                redirect = True
            current.append(ch)
        word_start = boundary
        i += 1
    if quote:
        raise Deny(SIMPLER % "unbalanced quotes")
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


def substitutions(text):
    """The commands an unquoted heredoc body runs as the shell expands it:
    its $(...) and backticks."""
    found, i = [], 0
    while i < len(text):
        if text[i] == "\\":
            i += 2
        elif text.startswith("$(", i):
            inner, end = _balanced(text, i + 2)
            found.append(inner)
            i = end + 1
        elif text[i] == "`":
            end = text.find("`", i + 1)
            if end == -1:
                raise Deny(SIMPLER % "an unbalanced backtick in a heredoc")
            found.append(text[i + 1:end])
            i = end + 1
        else:
            i += 1
    return found


def tokens_of(simple):
    try:
        return shlex.split(simple)
    except ValueError:
        raise Deny("the command could not be parsed; write it more simply")


def strip_wrapper(name, args):
    """The words after a wrapper program's own options: the program it runs
    and that program's arguments."""
    flags, valued = WRAPPER_OPTIONS[name]
    replaced = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--":
            i += 1
            break
        if name == "env" and ASSIGNMENT_RE.fullmatch(a):
            i += 1
            continue
        if not a.startswith("-"):
            break
        option = a.split("=", 1)[0] if a.startswith("--") else a[:2]
        if a in flags or (name == "nice" and re.fullmatch(r"-\d+", a)):
            i += 1
        elif option in valued:
            attached = "=" in a if a.startswith("--") else len(a) > 2
            if name == "xargs" and option in ("-I", "-J"):
                replaced.append(a[2:] if attached else (args[i + 1] if i + 1 < len(args) else ""))
            i += 1 if attached else 2
        else:
            raise Deny("`%s %s` is an option the guard cannot follow; write the command without it" % (name, a))
    rest = args[i:]
    if rest and any(r and r in rest[0] for r in replaced):
        raise Deny("`xargs` would put its input in place of the program it runs; name the program")
    if name == "timeout":
        if not rest or not re.fullmatch(r"\d+(\.\d+)?[smhd]?", rest[0]):
            raise Deny("give `timeout` its duration as a plain number before the command")
        rest = rest[1:]
    return rest


def strip_prefix(tokens):
    """Drop env assignments, shell keywords, redirections, and wrapper
    programs before the real program."""
    out = list(tokens)
    while out:
        tok = out[0]
        if ASSIGNMENT_RE.fullmatch(tok) or tok in SHELL_KEYWORDS:
            out.pop(0)
            continue
        if re.fullmatch(r"\d*[<>]+&?\d*", tok):
            out = out[2:] if len(out) > 1 and not re.fullmatch(r"\d*[<>]+&\d+", tok) else out[1:]
            continue
        name = os.path.basename(tok)
        if name in WRAPPER_OPTIONS:
            out = strip_wrapper(name, out[1:])
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


def check_shell_text(text, cfg, depth, where, cwds):
    """Check a shell script as the commands it runs."""
    try:
        check_command(text, cfg, depth, cwds)
    except Deny as exc:
        raise Deny("%s: %s" % (where, exc))


def shebang_program(text):
    """The program a script's `#!` line runs it with, or None."""
    if not text.startswith("#!"):
        return None
    names = [os.path.basename(w) for w in text[2:].split("\n", 1)[0].split() if not w.startswith("-")]
    if names[:1] == ["env"]:
        names = names[1:]
    return names[0] if names else None


def candidate_paths(path, cwds):
    """Where a file a command names could be: the path itself when absolute,
    else that path under each folder the command could be in. None when the
    command's folder is not known yet (a file being written)."""
    p = Path(path).expanduser()
    if p.is_absolute():
        return [p]
    if cwds is None:
        return None
    if None in cwds:
        raise Deny("after that `cd`, the guard cannot tell which folder `%s` is in; give its absolute path" % path)
    return [Path(c) / p for c in cwds]


def check_script_file(path, cfg, depth=0, cwds=None, shell=None):
    """Check a script the run runs: as shell commands when a shell runs it, as
    code when an interpreter does, and by its `#!` line when it is run by its
    path (with none, the shell runs it). A binary is not a script. A script
    the guard cannot find is refused; one a written file names is checked
    when it runs."""
    paths = candidate_paths(path, cwds)
    if paths is None:
        return
    found = [p for p in paths if p.is_file()]
    if not found:
        raise Deny("`%s` is not a file the guard can find from %s, so it cannot be checked; give a path to it"
                   % (path, " or ".join(str(c) for c in (cwds or [])) or "here"))
    for p in found:
        # The skill's own scripts list the denied programs by name, and a run
        # can never write there, so they are not scanned.
        if cfg.get("skill_dir") and under(p, cfg["skill_dir"]):
            continue
        try:
            if p.stat().st_size > 2 * 1024 * 1024:
                continue
            data = p.read_bytes()
        except OSError:
            continue
        if b"\0" in data[:8192]:
            continue
        text = data.decode("utf-8", "replace")
        runs_as_shell = shell
        if runs_as_shell is None:
            program = shebang_program(text)
            if program in DENIED_PROGRAMS:
                raise Deny("Script %s runs under `%s`, which is not available in a Gr0wthPilot run."
                           % (p.name, program))
            runs_as_shell = program is None or program in SHELLS
        if runs_as_shell:
            check_shell_text(text, cfg, depth + 1, "Script %s" % p.name, cwds)
        else:
            check_code_text(text, "Script %s" % p.name)


def check_module(name, cfg, cwds):
    """`python -m` runs only the standard library's own modules, and only
    when no file in the command's folders would be imported in their place."""
    if name not in PYTHON_MODULES:
        raise Deny("`python -m %s` runs code the guard cannot read; a run uses only `python3 -m %s`, and runs "
                   "anything else as a script by its path" % (name, "` or `python3 -m ".join(sorted(PYTHON_MODULES))))
    top = name.split(".")[0]
    for folder in candidate_paths(".", cwds) or []:
        shadows = list(folder.glob(top + ".*")) + list((folder / top).glob("__init__.*"))
        if shadows:
            raise Deny("%s would run in place of the standard library's %s; remove it or run from another folder"
                       % (shadows[0], name))


def argv_family(prog):
    if prog in SHELLS:
        return "shell"
    if re.fullmatch(r"python(\d(\.\d+)?)?", prog):
        return "python"
    if prog in ("node", "tsx", "ts-node", "bun"):
        return "node"
    if prog in ("deno", "ruby", "perl"):
        return prog
    return None


def parse_argv(prog, args, loads=None, after_run=False):
    """How a shell or interpreter is told what to run, read from its own
    options up to its first argument that is not one: ("inline", code),
    ("module", name), ("script", path), ("stdin", None) when it reads its
    code from standard input (a pipe, a here-string, or a redirection), or
    ("subcommand", None) for a bun or deno subcommand that runs no file.
    Code files its options load are added to `loads` as (path, is_shell);
    an option that loads code the guard cannot read is refused."""
    family = argv_family(prog)
    rules = ARGV_RULES[family]
    loads = [] if loads is None else loads
    inline = stdin = False
    i = 0
    while i < len(args):
        a, following = args[i], args[i + 1] if i + 1 < len(args) else ""
        redirect = re.match(r"\d*[<>]+&?", a)
        if redirect:
            i += 2 if redirect.end() == len(a) else 1
            continue
        if a == "--":
            i += 1
            break
        name, attached = a.split("=", 1) if "=" in a else (a, None)
        if name in rules.get("refused_options", ()):
            raise Deny("`%s %s` loads code the guard cannot read; a run does not use it" % (prog, name))
        if name in rules.get("inline_options", ()):
            return "inline", attached if attached is not None else following, loads
        if name in rules.get("load_options", ()):
            loads.append((attached if attached is not None else following, family == "shell"))
            i += 1 if attached is not None else 2
            continue
        if name in rules.get("valued_options", ()):
            i += 1 if attached is not None else 2
            continue
        if a.startswith("--") or (a[:1] == "-" and family in ("node", "deno")):
            i += 1
            continue
        if len(a) > 1 and (a[0] == "-" or (a[0] == "+" and family == "shell")):
            consume = 0
            for j, letter in enumerate(a[1:]):
                rest = a[j + 2:]
                if family == "shell":
                    inline = inline or (letter == "c" and a[0] == "-")
                    stdin = stdin or (letter == "s" and a[0] == "-")
                    consume += letter in rules["valued"]
                elif letter in rules.get("inline", ""):
                    return "inline", rest or following, loads
                elif letter in rules.get("module", ""):
                    return "module", rest or following, loads
                elif letter in rules.get("refused", ""):
                    raise Deny("`%s -%s` loads code the guard cannot read; a run does not use it" % (prog, letter))
                elif letter in rules.get("load", "") or letter in rules.get("valued", ""):
                    value = rest or following
                    if letter in rules.get("load", ""):
                        loads.append((value, False))
                    if prog.startswith("python") and letter == "W" and "." in (value.split(":") + ["", "", ""])[2]:
                        raise Deny("`%s -W %s` imports a module to find its warning class; a run does not use it"
                                   % (prog, value))
                    consume = 0 if rest else 1
                    break
            i += 1 + consume
            continue
        break
    first = args[i] if i < len(args) else None
    if family == "shell":
        if inline:
            return "inline", first or "", loads
        return ("stdin", None, loads) if stdin or first in (None, "-") else ("script", first, loads)
    if first in (None, "-"):
        return "stdin", None, loads
    if prog in ("bun", "deno") and not after_run:
        if first == "run":
            return parse_argv(prog, args[i + 1:], loads, after_run=True)
        if prog == "deno" and first == "eval":
            return "inline", args[i + 1] if i + 1 < len(args) else "", loads
        if Path(first).suffix.lower() not in CODE_SUFFIXES and "/" not in first:
            return "subcommand", None, loads
    return "script", first, loads


def check_simple(tokens, cfg, depth=0, cwds=None):
    if tokens and os.path.basename(tokens[0]) == "env" and all(
            t.startswith("-") or ASSIGNMENT_RE.fullmatch(t) for t in tokens[1:]):
        raise Deny("printing the environment can print secret values")
    for token in tokens:
        m = CODE_ENV_RE.fullmatch(token)
        if m:
            raise Deny("`%s` makes a program load code the guard never sees; a run neither sets nor names it"
                       % m.group(1))
    original = tokens
    tokens = strip_prefix(tokens)
    if not tokens:
        return
    prog = program_name(tokens[0])
    args = tokens[1:]
    if prog in DENIED_PROGRAMS:
        hint = PROGRAM_HINTS.get(prog)
        raise Deny("`%s` is not available in a Gr0wthPilot run%s." % (prog, "; " + hint if hint else ""))
    if tokens[0] not in ("[", "[[") and (tokens[0] == "__SUBST__" or tokens[0].startswith("-")
                                          or re.search(r"[\s$`{}*?\[\]]", tokens[0])):
        raise Deny("the program a command runs must be written out as a plain word, not %r; write the "
                   "command more simply" % tokens[0])
    family = argv_family(prog)
    if family and "xargs" in [os.path.basename(t) for t in original[:len(original) - len(tokens)]]:
        raise Deny("`xargs` would hand `%s` code the guard cannot see; run it on a script by its path" % prog)
    if "/" in tokens[0] and not family:
        check_script_file(tokens[0], cfg, depth, cwds)
    if family:
        mode, value, loads = parse_argv(prog, args)
        for path, as_shell in loads:
            check_script_file(path, cfg, depth, cwds, shell=as_shell)
        if mode == "inline" and family == "shell":
            check_command(value, cfg, depth + 1, cwds)
        elif mode == "inline":
            check_code_text(value, "Inline %s code" % prog)
        elif mode == "module":
            check_module(value, cfg, cwds)
        elif mode == "script":
            check_script_file(value, cfg, depth, cwds, shell=family == "shell")
    if prog in ("source", ".") and args:
        check_script_file(args[0], cfg, depth, cwds, shell=True)
    if prog == "eval":
        check_command(" ".join(args), cfg, depth + 1, cwds)
        return
    if prog == "find" and ("-exec" in args or "-execdir" in args or "-ok" in args):
        for flag in ("-exec", "-execdir", "-ok"):
            if flag in args:
                rest = args[args.index(flag) + 1:]
                end = next((i for i, t in enumerate(rest) if t in (";", "+", "\\;")), len(rest))
                check_simple(rest[:end], cfg, depth + 1, cwds)
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
    if prog in ("npx", "bunx", "uvx", "pipx") or (prog in ("npm", "pnpm", "yarn") and args[:1] in (["exec"], ["dlx"], ["x"])) \
            or (prog == "bun" and args[:1] == ["x"]):
        runner_args = args[1:] if prog in ("npm", "pnpm", "yarn", "bun") or (prog == "pipx" and args[:1] == ["run"]) else args
        while runner_args and runner_args[0].startswith("-"):
            runner_args = runner_args[1:]
        if runner_args:
            name = re.sub(r"@[^/]*$", "", runner_args[0].split("/")[-1]) if not runner_args[0].startswith("@") \
                else runner_args[0].split("/")[-1].split("@")[0]
            check_simple([name] + runner_args[1:], cfg, depth + 1, cwds)
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


def changed_dirs(args, cwds):
    """The folders a `cd` or `pushd` could leave the command in, added to
    those it could already be in (a `cd` inside a subshell does not last).
    None stands for a folder the guard cannot know (`cd -`, `cd $DIR`)."""
    target = next((a for a in args if a == "-" or not a.startswith("-")), None)
    if target is None:
        new = [str(Path.home())]
    elif target == "-" or "$" in target or "__SUBST__" in target:
        new = [None]
    elif Path(target).expanduser().is_absolute():
        new = [str(Path(target).expanduser())]
    else:
        new = [None if c is None else str(Path(c) / Path(target).expanduser()) for c in cwds]
    return cwds + [d for d in new if d not in cwds]


def check_command(command, cfg, depth=0, cwds=None):
    """Check a shell command line. `cwds` are the folders it could run in,
    which resolve the scripts it names; None for a file being written, whose
    scripts are checked when it runs."""
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
        if name in ("cd", "pushd") and cwds is not None:
            cwds = changed_dirs(stripped[1:], cwds)
        check_simple(tokens, cfg, depth, cwds)
        family = argv_family(name)
        if body is None and family and parse_argv(name, stripped[1:])[0] == "stdin":
            raise Deny("give `%s` its script by path, inline, or in a heredoc; code it reads from a pipe, a "
                       "here-string, or standard input is code the guard cannot check" % name)
        if body is not None and name:
            if family == "shell" or name in ("eval", "source", "."):
                check_command(body, cfg, depth + 1, cwds)
            elif family:
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
    suffix = Path(path).suffix.lower()
    if suffix in SHELL_SUFFIXES and tool_input.get("content") is not None:
        check_shell_text(content, cfg, 1, "File %s" % Path(path).name, None)
    elif suffix in CODE_SUFFIXES:
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
        check_command(command, cfg, cwds=[data.get("cwd") or cfg["package"]])
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
        "at": gc.iso_z(gc.utc_now()), "run_id": cfg.get("run_id"), "event": "pre", "tool": tool,
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
        record = {"at": now, "run_id": cfg.get("run_id"), "url": tool_input.get("url"),
                  "agent_id": data.get("agent_id")}
        if isinstance(response, dict):
            record.update(code=response.get("code"), bytes=response.get("bytes"),
                          redirect=bool(re.search(r"redirect", str(response.get("result", ""))[:300], re.I)))
        append_log(cfg["fetch_log"], record)
    append_log(cfg["tool_log"], {"at": now, "run_id": cfg.get("run_id"), "event": "post", "tool": tool,
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
    append_log(cfg["tool_log"], {"at": gc.iso_z(gc.utc_now()), "run_id": cfg.get("run_id"),
                                 "event": "session-start", "source": data.get("source")})
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
