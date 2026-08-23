# Building Products with Coding Agents

*Video Tutorial · Detailed Summary*

A solo AI builder's production workflow — planning, delegating, and validating at scale, demoed live with three home-built tools.

| | |
|---|---|
| **Format** | Host interview / live screen-share walkthrough |
| **Host** | Peter |
| **Guest** | Former L8 engineer (Meta & Microsoft), now a solo AI builder |
| **Core thesis** | Stop being the bottleneck — move yourself out of the agent's loop as much as possible. |
| **Sponsor segment** | Linear (noted, not summarized) |

## Overview

The guest builds software almost entirely through coding agents, shipping **~20–40 pull requests per day** across **at least five parallel sessions** running **20–30 agents on average**. His method keeps the standard *plan → code → validate* loop but redistributes effort: he spends **most of his time planning**, hands **coding entirely to agents**, and **automates validation** so he rarely reviews code line-by-line.

The walkthrough demos three tools he built to remove friction — **Lavish** (visual, interactive planning via HTML artifacts), **Treehouse** (zero-thought git worktree management), and **No Mistakes** (a fresh-context validation pipeline) — alongside practices for sub-agents, `AGENTS.md` testing instructions, and how team workflows must change as PR volume explodes.

**Legend for callout labels used below:**

- 💡 **Tip / Trick** — actionable advice
- 🔧 **Tool / Name** — tools, commands, proper nouns
- 📏 **General Rule** — principle framed as broadly applicable
- 💬 **Speaker Opinion** — personal opinion, preference, or individual experience
- ⚠️ **Caution / Trade-off** — warnings and trade-offs

> Caption corrections are marked inline where they occur and listed in full in the [Appendix](#appendix--caption-corrections--notes). Uncertain corrections are flagged with **[?]**.

---

## Table of Contents

1. [The Core Philosophy: Get Out of the Loop](#1-the-core-philosophy-get-out-of-the-loop)
2. [The Workflow: Plan → Code → Validate](#2-the-workflow-plan--code--validate)
3. [Running Sessions in Parallel](#3-running-sessions-in-parallel)
4. [The Setup & AI Stack](#4-the-setup--ai-stack)
5. [Planning with a Visual Editor (Lavish)](#5-planning-with-a-visual-editor-lavish)
6. [Planning from Scratch & Writing Specs](#6-planning-from-scratch--writing-specs)
7. [Visual Design](#7-visual-design)
8. [Managing Worktrees (Treehouse)](#8-managing-worktrees-treehouse)
9. [Sub-agents & Context Management](#9-sub-agents--context-management)
10. [Testing & AGENTS.md Instructions](#10-testing--agentsmd-instructions)
11. [Validation Pipeline (No Mistakes)](#11-validation-pipeline-no-mistakes)
12. [How Team Workflows Are Changing](#12-how-team-workflows-are-changing)
13. [Advice for New Builders](#13-advice-for-new-builders)
- [Appendix · Caption Corrections & Notes](#appendix--caption-corrections--notes)

---

## 1. The Core Philosophy: Get Out of the Loop

*The opening framing that everything else serves.*

The central problem: a human who inspects every line an agent produces becomes the rate limiter for the whole system. The guest stopped reviewing the agent's first-pass code entirely, and over time reached a point where his own review no longer caught anything the agents had missed.

> 📏 **General Rule**
> If you review every single line of code, you become the bottleneck. As agents write ~10× more PRs than a human used to, the old human-in-the-loop processes don't scale — so remove yourself from the loop wherever possible.

> 💬 **Speaker Opinion**
> He says he no longer reads the agent's first-pass code at all, and reports having reached a point where he "never catches anything the agents don't catch." (His personal experience, not presented as universally true.)

> 💡 **Scale Reference (his numbers)**
> - **≥ 5** active sessions running at once
> - **20–30** agents running on average (incl. sub-agents)
> - **20–40** PRs shipped per day (sometimes more)
> - Old baseline he contrasts against: an average engineer ships **10–15 PRs per month**

---

## 2. The Workflow: Plan → Code → Validate

*The high-level loop — standard shape, unusual effort distribution.*

He uses the same three phases most builders do. What differs is *how much time he spends in each*:

- **Plan** — mostly the human, with agent assistance. He invests the most time here.
- **Code** — almost entirely the agents. Once requirements are clear, he trusts them to do the work.
- **Validate** — agents do most of it; he applies judgment only when things are ambiguous.

> 📏 **General Rule**
> The depth of the plan determines how long agents can run autonomously. A detailed plan lets agents run for a long time; a one-line prompt means they finish quickly and bounce back to you for the next instruction.

> 💡 **Tip — escalate your planning artifact**
> Move along this spectrum to buy longer autonomous runs:
> - **Short prompt** ("what's the next action?") → frequent re-prompting
> - **Spec** → a comprehensive written set of requirements
> - **Measurable goal** → lets agents do lots of *experimentation* on their own

> 💬 **Host's confession (Peter)**
> Peter admits he's "gone super lazy," giving one-line prompts that never keep agents busy for hours — used to illustrate the cost of under-planning.

Conceptually, code + validation form a loop the agent can run by itself, which is what lets a single delegation run for a long time without the human.

---

## 3. Running Sessions in Parallel

*Only the start and end of a task need the human.*

Because the human is needed only at the beginning (planning) and end (judgment) of each task, he parallelizes many sessions so he's always doing productive work while agents run. He parallelizes both **across different projects** and **within the same project** (multiple sessions doing different things).

> 💡 **Tip — parallelism as productivity**
> Increasing the number of concurrent sessions is itself a core lever for getting more done. Treat your day like overseeing a large scope: jump into whichever thread needs you most.

> 💬 **Speaker Opinion**
> He frames context-switching between agent threads as *faster* than the meeting-driven context-switching of big-tech jobs — more like supervising many escalating workstreams at once.

---

## 4. The Setup & AI Stack

*Where the work actually happens.*

He works almost entirely in the **terminal**, switching to a GUI or browser only occasionally. The demo project is **Hybits** **[?]** — an AI tutor / agentic harness he's building for his son (a kids-oriented agent app). He had just revamped its main screen and wasn't happy with the result.

> 🔧 **Tools / Names**
> - **OpenCode** *(caption: "open code")* — his main agent harness
> - **tmux** *(caption: "t-mox")* — for parallel terminal windows/tabs
> - Project: **Hybits** **[?]** — an Electron-based AI tutor app for kids

> 💬 **Speaker Opinion — why OpenCode**
> He prefers OpenCode because it lets him **quickly try different models** as new ones ship — his stated big benefit of open-source agent tools.

---

## 5. Planning with a Visual Editor (Lavish)

*Replacing the "wall of text" plan with an interactive HTML artifact.*

His typical UI-iteration loop: take a **screenshot** of the messy screen, paste it into the agent, describe the specific problems, and ask the agent to propose options. In the demo he flagged two concrete problems with the kids' screen: *too many technical details that aren't kid-friendly*, and *a large area of unused white space*.

The agent's first plan came back as a long wall of text ("best direction / option 1 / option 2") — slow to read and hard to give targeted feedback on. His fix is to have the agent render the plan through a visual editor instead.

> 🔧 **Tool — Lavish**
> A visual editor he built that (1) generates a rich **HTML artifact** of the plan and (2) supports interactive back-and-forth between human and agent on that artifact. Open source, in his GitHub repo (`lavish` **[?]**).
> - Invoke by telling your agent: `npx lavish` **[?]** to write the technical plan.
> - It runs *within your existing agent session* — it does **not** spin up another agent and needs **no separate API key**.

> 💡 **Tip — annotate instead of retype**
> Because the plan is visual, you can click directly on a part of the artifact and leave feedback (e.g. "I don't care about this"), rather than copy-pasting chunks of a text spec back to the agent to say which part you dislike. The agent presented four layout directions (Options A–D), each with a **button** that sends "I like Option C" back to the agent on click.

> 💬 **Speaker Opinion — HTML over Markdown**
> He built Lavish after reading an article arguing for HTML over Markdown for agent artifacts. He was initially skeptical (HTML felt token-inefficient vs. Markdown), but found in practice the richer, interactive HTML artifact was "super useful" for human–agent collaboration.

> 📏 **General Rule**
> A plain generated HTML file you open in a browser is hard to iterate on — you can see what's wrong but can't easily tell the agent *which part* to change. Coupling the artifact to an interactive feedback channel is what makes visual planning workable.

---

## 6. Planning from Scratch & Writing Specs

*For brand-new ideas he spends a bit more up-front time.*

He uses the same Lavish editor: tells the agent he wants to brainstorm, talks through what he thinks the core parts of the idea are, then asks the agent to **criticize it**, surface **risks and weaknesses** he hasn't considered, and give its opinion. They iterate via the HTML artifact until the idea becomes a spec.

> 💡 **Tip — write preferences, invite pushback**
> When he already has opinions on tools or approach, he writes them down as explicit *preferences* in the spec — but always tells the agent it's okay to push back if something looks wrong, to preserve flexibility and surface more options.

> 🔧 **Tip — bake practices into the tool**
> Rather than maintaining "push back on me" guidance in a user-level `AGENTS.md`, he built those best-practice instructions **into Lavish itself**, so any agent using Lavish already follows them.

---

## 7. Visual Design

*A short aside on UI/visual design.*

> 💬 **Speaker Opinion — Claude Design**
> For visual design he likes **Claude Design** *(caption: "cloud design")* a lot and has used it heavily since launch — to the point of nearly exhausting his quota. On his quota tracker, his weekly Claude quota was mostly used up and Claude Design ~two-thirds used.

> 💡 **Tip — design system first**
> For new projects he uses it to build a **design system** once, then applies that system across many components easily.

---

## 8. Managing Worktrees (Treehouse)

*Avoiding agents stepping on each other in one directory.*

When he spins up a second agent in the same directory, the two sessions step on each other's work. The common answer is **git worktrees** — a worktree is essentially a clone of your current git repo in a separate, parallel directory that doesn't interfere with the main repo. But he finds manual worktrees costly.

> ⚠️ **Caution — the cost of manual worktrees**
> - **Cognitive load:** naming each worktree, then later remembering what each one is doing and which are safe to clean up.
> - **Dependencies:** a fresh worktree doesn't have `node_modules` / installed dependencies — you must reinstall and rebuild every time.

> 🔧 **Tool — Treehouse**
> A "dead simple," no-brainer worktree manager he built. Typing `treehouse` sets up a worktree and drops you into it — no decisions about whether to reuse or create one, and no five minutes spent inventing a name.
> - It draws from a **pool of managed worktrees**, so dependencies are already installed (no reinstall/rebuild each time) — saving both mental load and efficiency.

---

## 9. Sub-agents & Context Management

*When and why to delegate to sub-agents.*

> 📏 **General Rule — models rarely self-delegate**
> Today's models/harnesses aren't great at proactively spawning sub-agents. The main exception is built-in agents like **explore** — e.g. Claude Code will run an explore sub-agent to investigate a codebase on a complex question. In most other cases you have to *prompt* for sub-agents explicitly.

> 💡 **Tip — the real reason to use sub-agents**
> Use a sub-agent to keep the **main session's context window from blowing up**. When you're about to do heavy, exploratory investigation that won't be meaningful to the main session, carve it out to a sub-agent that returns *only its conclusion*. Also good for many isolated tasks — e.g. "spin up 10 sub-agents" for 10 independent experiments.

> 🔧 **Example — the ProgramBench experiment**
> A concrete sub-agent use case he was running:
> - **ProgramBench** *(caption: "program bench")* — a benchmark published ~2 weeks prior by the same team behind **SWE-bench**. It asks agents to build programs (e.g. `ffmpeg`) from scratch and checks whether they meet all requirements and pass all test cases.
> - His twist: run ProgramBench on **Codex**, forcing it to use **TypeScript, JavaScript, and Python** in turn, to see which language yields more requirements completed, more tests passed, and fewer tokens used.
> - Scale: roughly **200 × 8** runs — far too many for one main agent, which would constantly compact and run inefficiently.

---

## 10. Testing & AGENTS.md Instructions

*Making agents validate the way you would — by hand-off, not by hand.*

Each project has an `AGENTS.md` *(caption: "agents MD")* containing high-level project structure context plus explicit **testing instructions**. For Hybits (an Electron desktop app) the instructions tell the agent how to drive the app via a browser and test it end-to-end, including taking screenshots and checking for browser errors.

> 📏 **General Rule — agents default to shallow tests**
> By default, agents like to write *pure code-based unit tests* that often don't validate behavior end-to-end. Codex, for instance, defaults to its built-in in-app browser — which doesn't fit an Electron desktop app that needs different facilities. Without explicit instructions, agents do the minimum and aren't comprehensive.

> 💡 **Tip — turn manual checks into instructions / E2E tests**
> - Write the testing instructions as "how I would test this myself," so the agent validates end-to-end and you skip manually running the app.
> - For recurring core flows (e.g. create a workout, track workouts), have the agent turn them into **automated end-to-end tests** (using tools like **Playwright** *(caption: "playright")*) so they run on every change.

> 📏 **General Rule (his guiding principle, restated for non-technical builders)**
> If you find yourself doing something manually, try to turn it into something the agent does for you. With today's models you can often just ask the agent to automate the manual step, and it will figure out how.

---

## 11. Validation Pipeline (No Mistakes)

*Where most people over-spend time — and how he automates it.*

The default validation move is opening an IDE and reviewing the diff line by line. Since AI writes so much code, that makes the human the bottleneck again. His answer is a tool that reviews in a **fresh context window**.

> 🔧 **Tool — No Mistakes (alias `nm`)**
> A validation pipeline he built, triggered on a code change. Its phases:
> - **Branch:** creates a branch (and commit message) so he never thinks about naming.
> - **Intent:** analyzes the work session to understand his intent + surrounding context (it does *not* copy the whole session into the new window).
> - **Rebase:** rebases the change onto the latest remote `main` to avoid later merge conflicts.
> - **Review:** heavily prompt-engineered to scrutinize the change hard — high recall for edge cases, bugs, logical errors.
> - **Test:** more like CI than local unit tests — checks for regressions and presents **evidence** (screenshots, sometimes video) that the change works.
> - **Documentation:** finds all docs affected by the change (it caught that a design-system example copy wasn't updated).
> - **Lint → Push → create PR.**

> 📏 **General Rule — review in a FRESH context window**
> Reviewing in the same session biases the agent toward believing the existing work is correct (it saw every step), so it misses things. A fresh context window catches far more edge cases. The Intent phase exists to hand that fresh reviewer just enough context — like a principal engineer reviewing with fresh eyes after a brief explanation.

> 💡 **Tip — bug triage & risk-based attention**
> - No Mistakes splits findings into **obvious bugs** (auto-fixed silently) vs. errors whose fix has **product implications** (escalated to him to judge).
> - The PR includes intent summary, what changed, a **risk assessment** (low/medium/high) and test evidence — so he spends more time on high-risk PRs and less on low-risk ones.
> - For low-risk changes he merges without opening the diff; for medium/high risk he opens the diff and reviews himself.

> ⚠️ **Caution / Trade-offs**
> - Running all stages makes shipping a single feature take **longer** — accepted because more confidence means fewer things break later.
> - He doesn't run No Mistakes on *every* change (e.g. trivial doc updates) — heavy validation burns tokens, so he judges whether a change justifies it, like a team where not every PR goes to QA.
> - He never stares at the pipeline; the terminal shows the current phase, so he switches sessions and only jumps back when it needs his judgment.

> 💬 **Speaker Opinion**
> He still always at least *skims* the PR (risk assessment, what the agent did, the fix) before merging — and gently flags that merging blindly is a mistake. Peter admits he sometimes just tells it to merge without looking; the guest's stance is that some review of *what changed and what risks exist* remains useful even without a line-by-line read.

---

## 12. How Team Workflows Are Changing

*Reflections on solo building vs. big-tech teams.*

> 💬 **Speaker Opinion — "liberated," with one regret**
> Asked whether solo building feels lonely, he says he largely feels **liberated**. What he misses: teammates for *brainstorming* — a diverse, smart team that ideates together, which he doesn't think AI can fully replace yet. What he doesn't miss: nobody had time to review his PRs once he was writing ~20 a day, even before he left his last company.

> 📏 **General Rule — processes built for a slower era**
> Team processes and human composition were designed when an average engineer wrote ~10–15 PRs/month, so peer code review was affordable. At 10× the PR volume those assumptions break, and teams are starting to change practices to cope.

> ⚠️ **Caution — what some teams are doing**
> Some smaller startup teams have effectively **stopped doing peer PR reviews** — they still raise a PR as a formality/record but merge without waiting for review and fix problems later. The guest and host note this trends toward *less stable products*; the guest jokes the fix is to use No Mistakes (i.e. automated review).

---

## 13. Advice for New Builders

*Three pieces of advice for ramping up.*

> 💡 **Advice 1 — Build a lot, including throwaways**
> Play a lot and build many things, even throwaway toys. The build process surfaces what you (and the agents) can do better. Build *every* idea you have — send the prompt and see what happens — rather than over-deliberating, building one thing, and quitting when it fails.

> 💡 **Advice 2 — Use more tokens, run more agents in parallel**
> Treat "more tokens / more parallel agents" as a **forcing function** to upgrade your workflow. Working with one agent at a time keeps you in the loop as the bottleneck; pushing for parallelism forces you to move yourself out of it.

> 💡 **Advice 3 — Apply AI to the whole workflow, not just coding**
> Delegate validation, documentation, raising PRs — not only code writing. Whenever you find a manual step, ask whether the agent can take it over.

> 🔧 **Tool — Claude Code `/insights`**
> A slash command that analyzes your Claude Code sessions and generates a report on what could be done better — skills to add, tweaks to memory files — to make Claude Code work more efficiently for you. (He recommends trying it but notes it uses a lot of tokens.)

> 💬 **Speaker Opinion — on "token maxing"**
> He cautions that "token maxing" is partly a meme: don't burn tokens for their own sake — the goal is getting real work done. Advice 2 is about pushing yourself to scale up, not about wastefulness. Since most individuals are on a subscription, the practical move is to make the most of the quota you've already paid for. (Peter relates a personal "scarcity mindset" that makes burning tokens feel uncomfortable.)

> 🔧 **Where to find the guest & tools**
> He's active on **X** and **YouTube** (sharing workflows, tools, setups) and on **GitHub** for projects, using the same handle across X, YouTube, GitHub, and LinkedIn. The exact handle is garbled in the captions **[?]** (see Appendix). Links to **Lavish** and **No Mistakes** were promised in the episode description.

---

## Appendix · Caption Corrections & Notes

The source was an auto-generated transcript. Below is every correction applied for clarity, with confident fixes and uncertain ones marked. Items flagged **[?]** are best guesses where the caption was too garbled to be certain; these were *not* silently changed in meaning, only normalized.

| Caption as transcribed | Corrected to | Confidence / note |
|---|---|---|
| "open code" | `OpenCode` | Confident — named agent harness. |
| "cloud code" | `Claude Code` | Confident — context (slash commands, sub-agents). |
| "codeex" / "codex" | `Codex` | Confident. |
| "cloud design" | `Claude Design` | Confident — design tool, quota tracker context. |
| "t-mox" | `tmux` | Confident — terminal multiplexer. |
| "playright" | `Playwright` | Confident — E2E browser testing tool. |
| "program bench" | `ProgramBench` | Confident — benchmark name (SWE-bench authors). |
| "Swebench" | `SWE-bench` | Confident. |
| "agents MD" / "agent.mmd" | `AGENTS.md` | Confident — per-project agent instructions file. |
| "get work tree" | `git worktree` | Confident. |
| "linear.app/aents" | `linear.app/agents` | Confident — sponsor URL, dropped "g". |
| "L8 engineer" / "LA engineer" | L8 (level-8) engineer | Confident — "LA" later is a mistranscription of "L8". |
| "Lavage editor" / "lavishi" | `Lavish` (editor & repo) | Likely — tool name appears several ways. |
| "hybits" / "high bits" / "hybrids" / "hybrid 2" | `Hybits` **[?]** | **Uncertain** — project name inconsistent across captions; "Hybits" chosen as most frequent rendering. |
| "npx lavish axi" | `npx lavish` **[?]** | **Uncertain** — trailing token ("axi") unclear; exact subcommand not verifiable. |
| "it basically killed a piece of feedback" | "…queued/sent a piece of feedback" **[?]** | **Uncertain** — "killed" appears to be a mishearing; meaning is that clicking a button sends feedback to the agent. |
| "slashkun" / "Kungchan GUID" / "UID" | Handle not reliably recoverable **[?]** | **Uncertain** — the guest's shared handle (X/YouTube/GitHub/LinkedIn) is garbled; left unstated rather than guessed. Check the episode description for accurate links. |
| "LIR" / "linear" | `Linear` | Confident — sponsor (issue-tracking tool). |

**On opinion vs. rule:** Throughout this summary, 💬 marks statements the speaker (or host) gives as personal opinion, preference, or individual experience, while 📏 marks claims framed as general principles. Where a number or proper noun came directly from the transcript it has been preserved exactly; only obvious caption misspellings were corrected as listed above.
