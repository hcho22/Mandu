# Guardrails: what the tools refuse

"Publish nothing" and "spend nothing new" are kept by what the tools refuse, not only by instructions.
`bin/gr0wthpilot <Product>` starts Claude Code with a permission profile written for that run by `scripts/gp_run.py`, and three independent layers enforce it.
Each layer was proven in live sessions; this page says what each one covers and, honestly, what none of them can.

## How the launcher starts a run

- `--setting-sources project`: Claude Code loads none of the Founder's user or local settings, so no allow rule, hook, or plugin from them reaches the run.
  It loads only Mandu's shared `.claude/settings.json`, which is what makes Claude Code load Mandu's skills; `gp_run.py` refuses to start while that file sets permissions, hooks, the sandbox, plugins, environment variables, an API key helper, or MCP servers.
  Every other Mandu session and Mandu's `.claude/settings.json` are unchanged.
- `--settings <guard records>/profile.json`: the run's own profile, kept with the guard's records (below).
  `gp_run.py` refuses to start when the profile carries a key or a permission rule Claude Code's settings schema does not accept, because Claude Code drops an invalid settings file whole (silently, in print mode).
- `--strict-mcp-config` with no MCP config: no MCP server or connector loads; `--no-chrome`: Claude in Chrome stays off.
- `--permission-mode dontAsk`: anything the profile does not allow is refused without a prompt, so a run never waits on the Founder.
- The session starts inside the Candidate Package, which is what the macOS sandbox lets shell commands write.
- The launcher runs only `/gr0wthpilot <Product>`; it takes no other Claude Code arguments, so nothing on its command line can loosen the profile.
- `caffeinate -i -s -w <pid>` holds system sleep off (the display may still sleep) for exactly the life of the session's own process, and releases it when the session ends, however it ends.
- The profile copies only `model` and `effortLevel` from the Founder's own settings, sets `workflowSizeGuideline` to `unrestricted` (Claude Code's default guideline is "medium", under 10 agents per workflow), and turns auto-memory off, since a run writes no memory.

## Layer 1: the guard hook

`scripts/guard.py` runs before every tool call, in the main session and in every subagent and Workflow agent, in every permission mode, and fails closed: if it errors, the call is refused.
It refuses:

- Shell commands that publish, deploy, upload, or reach a remote host: `git push` and every git subcommand that is not a read, `gh`, `hub`, `glab`, wrangler, vercel, netlify, firebase, surge, heroku, fly, railway, aws, gcloud, az, rclone, scp, sftp, ssh, rsync, nc, telnet, sendmail, `npm publish` and its sign-in commands, twine, fastlane, altool, notarytool, and anything a package runner (`npx`, `bunx`, `npm exec`) would run of those.
  It finds them inside chains, pipes, subshells, `$(...)`, backticks, `bash -c` (or a cluster such as `-lc`), `eval`, `find -exec`, `if`/`then`/`do` and the other shell keywords, and behind `env`, `nohup`, `timeout`, and similar wrappers.
- Shell scripts as the commands they run, by the same rules: a script run with `bash`, `sh`, or `zsh`, with `source` or `.`, or by its path (`./serve.sh`), and a shell-suffixed file the run writes whole.
  A script run by its path is checked by its `#!` line (a script with none runs in the shell), and one whose `#!` names a denied program is refused.
  A shell or interpreter that would read its script from a pipe or a redirection is refused, because the guard cannot see that script; give it a path, inline code, or a heredoc.
- curl or wget with any flag that sends data or credentials (`-d`, `-F`, `-T`, `-X POST`, `--json`, `-u`, `--post-data`).
- Inline code (`-c`, `-e`, Node's `-p`, and clusters such as `-Bc` or `-ne`), scripts the run executes (by an interpreter, `python3 -m` from the package, `tsx`, `ts-node`, `bun`, or `deno`, or by their path), and code files the run writes, when they hold code that sends (smtplib, `requests.post`, a POST `fetch`, `urlopen(..., data=...)`, raw sockets) or runs a denied program: the program a subprocess, `os.exec*`, `child_process`, or `system()` call is given, compared by its basename, so `'/usr/bin/open'` is caught and a page's `classList.toggle('open', ...)` is not.
- Programs that act as the Founder: `open`, osascript, `security` (the keychain), `chrome-devtools-axi` (his signed-in Chrome), `claude`, codex, and other agents.
- Reading a `.env` file, printing the environment, and any command or file content holding a value from a `.env` file.
- Any write outside the Candidate Package and the run's cache folder, which includes the guard's own records, and any write into a protected package (the live package, or an earlier Candidate Package).
- WebFetch of a page the site's robots.txt disallows for automated readers, or of a site whose robots.txt cannot be read; it checks with the RFC 9309 rules, including `*` and `$` patterns, and caches each robots.txt for six hours.
- AskUserQuestion, every MCP and connector tool, Artifact, RemoteTrigger, PushNotification, SendMessage, CronCreate, ScheduleWakeup, EnterWorktree, and worktree isolation in Agent or Workflow calls.
- Skills other than gr0wthpilot, customer-research, and influencer-marketing.
- `xcrun`, `xcodebuild`, and Chrome themselves, which run only through their wrappers, and a wrapper run inside a chain, pipe, redirection, or subshell.

It also logs every call, with secret values redacted, to `tool-log.jsonl`, and every WebFetch's URL and HTTP code to `fetch-log.jsonl`, both in the guard's records; the source check and `run-audit.md` read those logs.

## Layer 2: the permission rules

The profile allows Bash, the file tools, WebFetch, WebSearch, Agent, Workflow, the task tools, and the three skills, and allows edits only under the Candidate Package and the cache folder.
It denies, as a second, independent layer, Artifact, EnterWorktree, every MCP tool, the publishing and remote commands above by name, reading `.env` files, and edits in protected packages and in the guard's records.
A deny rule beats any allow rule.

## Layer 3: the macOS sandbox

Every shell command and every process it starts runs in Claude Code's sandbox (Seatbelt), in strict mode: a command can never ask to run outside it.

- Writes: only the Candidate Package (the session's working folder), the cache folder, and the per-session temp folder; protected packages and the guard's records are denied outright.
- Network: only the hosts last30days reads (Reddit, its archive host, YouTube, Hacker News, Polymarket).
  GitHub is deliberately not on the list, because the `gh` token on this Mac can write.
  The open web is read only through WebFetch, which is GET-only and robots-checked by the guard.

Three wrappers run outside the sandbox, because what they drive cannot run inside it (the simulator service, Chrome, and xcodebuild's system services), and each enforces its own rules:

- `gp-sim` creates simulators only as `Gr0wthPilot-<Product>-<n>`, records them in the run's ledger, touches no other device, keeps at most two and boots one at a time, and writes files only into the package or the cache folder.
  `gp-sim cleanup` lists the devices again after deleting and marks deleted exactly the run's devices that are gone, so the ledger never calls a device deleted that still exists.
- `gp-chrome` runs headless Chrome on a fresh throwaway profile (so none of the Founder's sign-ins load), opens only local pages, and writes only into the package or the cache folder.
- `gp-xcodebuild` builds a copy of the Product's committed tree in the cache folder, for the simulator only, runs tests only on a simulator the run created (named by `id=` or `name=`, so xcodebuild never boots one of the Founder's own), and refuses archive, export, signing with a team, device registration, and App Store Connect.

## The guard's own records

A run's folders sit under the cache root, `~/Library/Caches/Gr0wthPilot` (or `GR0WTHPILOT_WORK`):

- `<Product>/`, the cache folder, which the run writes.
- `<Product>.guard/`, the guard's records: its config, the permission profile, the robots.txt cache, the tool log, the WebFetch log, and the simulator ledger.
  No tool of the run can write it: it is outside the sandbox's writable folders and in its denied ones, outside the profile's edit allow rules and in its deny rules, and outside what the guard's write check allows.
  Only the guard hook, which runs outside the sandbox, and the unsandboxed wrappers (`gp-sim` keeps the simulator ledger) write it.
  So a run cannot forge a robots.txt verdict, turn off the guard's secret or script checks through its config, or rewrite which pages it fetched: during a run the source check reads only the guard's live WebFetch log.

These records the run could still alter, because a sandboxed command or the run itself must write them:

- `last30days-log.jsonl` in the cache folder, written by `gp-last30days` inside the sandbox, and the last30days output in the package whose SHA-256 it records; the hash proves a file is the one the wrapper saw only as far as the log itself is trusted.
- The preflight receipt in the cache folder, which the guard writes and the sandboxed preflight deletes.
- The workflow script copies, the scratch folder, the source copy, and the build output in the cache folder.
- Everything in the package itself, including `run-evidence/` and `run-audit.md`, which `audit_run.py` copies and writes from the guard's records at the end of the run.

## What no layer covers

These gaps remain, and are accepted for a run the Founder starts and watches himself:

- A page the run writes and then renders with `gp-chrome` could run its own JavaScript, and Chrome there reaches the network, so a page written to send data would send it.
  The run never writes such a page, the guard refuses code files that send, and the throwaway profile carries no account; but HTML is not scanned for scripts that send.
- A process inside the sandbox can still send a request to an allowed research host (Reddit, YouTube, Hacker News, Polymarket); it holds no credentials for any of them, so it cannot post as the Founder.
- `gp-xcodebuild` runs the Product's own build scripts unsandboxed.
  They are the Founder's own code, and the build runs on a copy, never in the repository.
- In the interactive session, the Founder can change the permission mode himself (Shift+Tab); the guard and the sandbox still apply in every mode.
  `disableAutoMode` is honored only in managed settings, so auto mode stays selectable.
- The guard reads shell commands and the scripts they run by name; a determined script could hide a denied program in a way it cannot parse, and the guard does not read what a build tool runs from its own files (`package.json` scripts, a Makefile).
  The sandbox's write and network limits still hold for whatever runs inside it.
- The last30days log and the copies in `run-evidence/` are writable by the run (see "The guard's own records"), so they are the run's record, not tamper-proof evidence.
  The source check reads the `run-evidence/` copy of the WebFetch log only with no run config present, as when the package is checked after the run.
