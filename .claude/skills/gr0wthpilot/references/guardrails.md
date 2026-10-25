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

`scripts/guard.py` runs before every tool call, in the main session and in every subagent and Workflow agent, in every permission mode, and fails closed on its own errors: if it errors, the call is refused.
Hook input it cannot parse as JSON is read as an empty call, which names no tool and is allowed.
It refuses:

- Shell commands that publish, deploy, upload, or reach a remote host: `git push` and every git subcommand that is not a read, `gh`, `hub`, `glab`, wrangler, vercel, netlify, firebase, surge, heroku, fly, railway, aws, gcloud, az, rclone, scp, sftp, ssh, rsync, nc, telnet, sendmail, `npm publish` and its sign-in commands, twine, fastlane, altool, notarytool, and anything a package runner (`npx`, `bunx`, `bun x`, `npm exec`) would run of those.
  It finds them inside chains, pipes, subshells, `$(...)`, backticks (in double quotes too), an unquoted heredoc's `$(...)` and backticks, `bash -c` (or a cluster such as `-lc`), `eval`, `find -exec`, `if`/`then`/`do` and the other shell keywords, and behind `env`, `nohup`, `timeout`, `xargs`, and similar wrappers.
  A wrapper option it does not know is refused, because its value could be the program the wrapper runs (`env -S`).
- Anything outside the small part of the shell the guard follows with certainty, rather than guessing how the shell reads it: a program named by a variable, a substitution, a glob, a word with a space, a leading `=`, or a `<` or `>` (`$X pr create`, `$(echo gh)`, `env -S 'gh pr'`, zsh's `=open`); any `{` or `}` outside quotes (a group, a function body, or a brace expansion; only the literal `{}` placeholder passes); a function definition (`function f`, `f()`) and zsh's `repeat` and `foreach`; an escaped space or operator before `#`; a `${...}` holding `#`, `=`, an operator, or a quote; ANSI-C quoting (`$'...'`); a heredoc whose delimiter is not one plain word; unbalanced quotes.
  The refusal says to write the command more simply; separate commands or a subshell do what a group or a function would.
  A redirection before the program is read with its target, attached (`>out.txt`) or not, so the program after it is the one checked.
- Shell builtins that run a command later or under another name: `alias`, `hash`, `enable`, `trap`, `bind`, `complete`, `compgen`, `fc`.
- A variable a command sets must be named by one plain word, whether by an assignment (`NAME=`, `NAME+=`), `export`, `declare`, `typeset`, `local`, `readonly`, `read`, `printf -v`, `mapfile`, `getopts`, or `let`; `export "${x}_ENV=..."` is refused.
- Setting, in any of those forms, a variable that makes a program load code the guard never sees: `BASH_ENV`, `ENV`, `ZDOTDIR`, `PS4`, `PROMPT_COMMAND`, `NODE_OPTIONS`, `PYTHONPATH`, `PYTHONSTARTUP`, `PYTHONHOME`, `PERL5OPT`, `PERL5LIB`, `RUBYOPT`, `RUBYLIB`, `LD_PRELOAD`, every `DYLD_` variable, and the like, or pointing a name at one (`declare -n ref=BASH_ENV`).
  Merely mentioning one (`grep -rn ENV .`) is fine.
- These rules hold the same for shell files the run writes and scripts it runs.
- Shell scripts as the commands they run, by the same rules: a script run with `bash`, `sh`, or `zsh`, with `source` or `.`, or by its path (`./serve.sh`), and a shell-suffixed file the run writes whole.
  A script run by its path is checked by its `#!` line (a script with none runs in the shell), and one whose `#!` names a denied program is refused.
  A shell's or interpreter's own options are read only up to the script, so a flag passed to the script (`build.py -c config.json`) is the script's, and options that take a value (`-o pipefail`, `-X utf8`) are skipped with it.
  An option that loads a code file is checked like a script: Node's `-r`, `--require`, `--import`, and `--loader`, bun's `--preload`, Ruby's `-r`, and a shell's `--rcfile` and `--init-file`; one that names a package rather than a file the guard can read (`--import tsx`) is refused, so run `npx tsx` instead.
  Options that load code the guard cannot read at all are refused: Perl's `-M`, `-m`, and `-I`, Ruby's `-I`, Deno's and bun's `--import-map` and `--config`, and Python's `-W` naming a dotted warning class.
  `python3 -m` runs only the standard library's `http.server` and `json.tool`, and only when no file in the command's folder would be imported in their place.
  A relative script path is found from the command's working folder, as moved by any `cd` earlier in the command; a script the guard cannot find, or one after a `cd` it cannot follow (`cd -`, `cd $DIR`), is refused, so give its path.
  A shell or interpreter that would read code from a pipe, a here-string, or standard input is refused, whatever its flags (`bash -v` and `python3 -v` still run what they read), because the guard cannot see that code; give it a path, inline code, or a heredoc, whose body the guard reads.
  `xargs` handing words to a shell or interpreter is refused for the same reason.
  A `#` that starts a word (at the start, or after an unescaped space, tab, newline, `;`, `|`, or `&`) starts a comment, as in the shell, so a comment's apostrophe does not break the parse; an escaped character never ends a word or starts a comment.
- curl or wget with any flag that sends data or credentials (`-d`, `-F`, `-T`, `-X POST`, `--json`, `-u`, `--post-data`).
- Inline code (`-c`, `-e`, Node's and bun's `-p`, and clusters such as `-Bc` or `-ne`), scripts the run executes (by an interpreter, `tsx`, `ts-node`, `bun`, or `deno`, or by their path), and code files the run writes, when they hold code that sends (smtplib, `requests.post`, a POST `fetch`, `urlopen(..., data=...)`, raw sockets) or runs a denied program: the program a subprocess, `os.exec*`, `child_process`, or `system()` call is given, compared by its basename, so `'/usr/bin/open'` is caught and a page's `classList.toggle('open', ...)` is not.
- Programs that act as the Founder: `open`, osascript, `security` (the keychain), `chrome-devtools-axi` (his signed-in Chrome), `claude`, codex, and other agents.
- Reading a `.env` file, printing the environment, and any command or file content holding a value from a `.env` file.
- Any write outside the Candidate Package and the run's cache folder, which includes the guard's own records, and any write into a protected package (the live package, or an earlier Candidate Package).
- WebFetch of a page the site's robots.txt disallows for automated readers, or of a site whose robots.txt cannot be read; it checks with the RFC 9309 rules, including `*` and `$` patterns, and caches each robots.txt for six hours.
- AskUserQuestion, every MCP and connector tool, Artifact, RemoteTrigger, PushNotification, SendMessage, CronCreate, ScheduleWakeup, EnterWorktree, and worktree isolation in Agent or Workflow calls.
- Skills other than gr0wthpilot, customer-research, and influencer-marketing.
- `xcrun`, `xcodebuild`, and Chrome themselves, which run only through their wrappers, and a wrapper run inside a chain, pipe, redirection, or subshell.

It also logs every call, with secret values redacted, to `tool-log.jsonl`, and every WebFetch's URL and HTTP code to `fetch-log.jsonl`, both in the guard's records, each record stamped with the run's id; the source check and `run-audit.md` read those logs.
The logs are kept per Product, so a re-run's checks count only records with its own run id: a page an earlier run fetched does not count as fetched by this one.

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

- `gp-sim` creates simulators only as `Gr0wthPilot-<Product>-<n>`, records them in a ledger kept per Product in the guard's records (`<Product>.guard/simulators.json`), so it holds the devices of every run of that Product, touches no device the ledger does not hold, keeps at most two and boots one at a time, and writes files only into the package or the cache folder, besides that ledger.
  `gp-sim cleanup` lists the devices again after deleting and marks deleted exactly the ledger's devices that are gone, so the ledger never calls a device deleted that still exists.
  It installs only an app gp-xcodebuild built in the guard's build folder, because the simulator runs an app unsandboxed.
- `gp-chrome` runs headless Chrome on a fresh throwaway profile (so none of the Founder's sign-ins load), opens only local pages, and writes only into the package or the cache folder.
  It never opens a page by a `file://` URL: a page file in the package or the cache folder is served, with the rest of that folder (so a carousel slide's `../carousel.css` loads), by an http server on `127.0.0.1` that `gp-chrome` starts for that one call and stops after, and that refuses any path leaving that folder or entering a protected package, symlinks followed.
  A file the page asked for and did not get is printed as a warning, so a screenshot missing its styles or images does not pass unnoticed.
  An http page can neither frame, embed, nor read a local file, so a page cannot show or read the Founder's files (his `.env` files or the `gh` token among them) in a screenshot, a PDF, the DOM, or a measurement.
  An `http` URL the run gives must be on `localhost` or `127.0.0.1` with no userinfo, backslash, or whitespace, and is rebuilt from its checked parts before Chrome sees it.
- `gp-xcodebuild` builds only from a copy of the Product's committed tree in the guard's build folder, `<Product>.guard/build/`, which no tool of the run can write.
  `gp-xcodebuild source` records every file's SHA-256, and every build checks the copy against that record and exports it again from its commit when anything differs.
  It accepts only the actions and options a simulator build needs (build, test, and clean actions; `-project`, `-workspace`, `-xcconfig`, `-scheme`, `-target`, `-configuration`, `-destination`, `-sdk`, `-testPlan`, `-only-testing`, `-skip-testing`, `-resultBundlePath`, a few display and package-resolution flags, and `SETTING=value`) and refuses every other one, `-resolvePackageDependencies` included, so no option can write elsewhere (`-resultStreamPath`), archive, export, or download a platform.
  The project, workspace, and `.xcconfig` must lie in that copy.
  Every call, `-showBuildSettings` included, gets the build folder's own DerivedData, which holds the Swift packages a build fetches and compiles and the app `gp-sim` installs, so xcodebuild never reads or writes the Founder's DerivedData; only a result bundle may go to the cache folder.
  It refuses `-list`, which xcodebuild cannot run with a DerivedData path; the build recipe in `app-screens.md` does not need it.
  A build setting may name no path outside the build folder and no `$(`, `${`, or `..`.
  Every call except an information one (`-showBuildSettings` and the like, with no action) names an iOS Simulator `-destination` or `-sdk iphonesimulator`, a call with no action included, since xcodebuild then builds, and without one it uses the project's default SDK, a device's.
  A `-destination` must be an iOS Simulator one, and an `-sdk` and an `SDKROOT=` setting must be `iphonesimulator`; an `-xcconfig`, which overrides the command line, and every file it includes must lie in the copy and set `SDKROOT` to nothing else, and the wrapper clears `XCODE_XCCONFIG_FILE`.
  Tests run only on a simulator in the Product's ledger (named by `id=` or `name=`, so xcodebuild never boots one of the Founder's own), and the wrapper refuses archive, export, signing with a team, device registration, and App Store Connect.

## The guard's own records

A run's folders sit under the cache root, `~/Library/Caches/Gr0wthPilot` (or `GR0WTHPILOT_WORK`):

- `<Product>/`, the cache folder, which the run writes.
- `<Product>.guard/`, the guard's records: its config, the permission profile, the robots.txt cache, the tool log, the WebFetch log, the simulator ledger, and `build/`, gp-xcodebuild's verified source copy and DerivedData.
  No tool of the run can write it: it is outside the sandbox's writable folders and in its denied ones, outside the profile's edit allow rules and in its deny rules, and outside what the guard's write check allows.
  Only the guard hook, which runs outside the sandbox, and the unsandboxed wrappers (`gp-sim` keeps the simulator ledger, `gp-xcodebuild` the build folder) write it.
  So a run cannot forge a robots.txt verdict, turn off the guard's secret or script checks through its config, or rewrite which pages it fetched: during a run the source check reads only the guard's live WebFetch log.

These records the run could still alter, because a sandboxed command or the run itself must write them:

- `last30days-log.jsonl` in the cache folder, written by `gp-last30days` inside the sandbox, and the last30days output in the package whose SHA-256 it records; the hash proves a file is the one the wrapper saw only as far as the log itself is trusted.
- The preflight receipt in the cache folder, which the guard writes and the sandboxed preflight deletes.
- The workflow script copies, the scratch folder, and any result bundle in the cache folder.
- Everything in the package itself, including `run-evidence/` and `run-audit.md`, which `audit_run.py` copies and writes from the guard's records at the end of the run.

## What no layer covers

These gaps remain, and are accepted for a run the Founder starts and watches himself:

- A page the run writes and then renders with `gp-chrome` could run its own JavaScript, and Chrome there reaches the network, so a page written to send data would send it.
  What such a page can reach is the network and the files in the Candidate Package or cache folder that holds it, which `gp-chrome` serves; it cannot load or show any other local file, and the throwaway profile carries no account or cookie.
  A page from a server the run started itself on `localhost` shows whatever that server serves.
  The run never writes such a page, and the guard refuses code files that send; but HTML is not scanned for scripts that send.
- The guard reads the script a command runs, not the modules that script imports (a local `helpers.py` or `require('./lib')`).
- A process inside the sandbox can still send a request to an allowed research host (Reddit, YouTube, Hacker News, Polymarket); it holds no credentials for any of them, so it cannot post as the Founder.
- `gp-xcodebuild` runs the Product's own build scripts unsandboxed.
  They are the Founder's own committed code, checked against its commit before every build, and the build runs on a copy, never in the repository.
- In the interactive session, the Founder can change the permission mode himself (Shift+Tab); the guard and the sandbox still apply in every mode.
  `disableAutoMode` is honored only in managed settings, so auto mode stays selectable.
- The guard reads shell commands and the scripts they run by name; a determined script could hide a denied program in a way it cannot parse, and the guard does not read what a build tool runs from its own files (`package.json` scripts, a Makefile).
  The sandbox's write and network limits still hold for whatever runs inside it.
- The last30days log and the copies in `run-evidence/` are writable by the run (see "The guard's own records"), so they are the run's record, not tamper-proof evidence.
  The source check reads the `run-evidence/` copy of the WebFetch log only with no run config present, as when the package is checked after the run.
