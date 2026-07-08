# Working With Fable 5 in Claude Code

**Theo (T3)'s workflow, prompts, model-routing setup, and cost-control tips for a new era of agentic engineering**

> **Source:** YouTube tutorial (auto-caption transcript) · **Speaker:** Theo (T3 / soydev) · **Domain:** Claude Code, sub-agents, workflows, model routing · **Format:** Scannable reference document

---

## Overview

The speaker walks through how he adapted his entire agentic-coding workflow to get the most out of **Fable 5**, Anthropic's newest model, during a limited window of subscription access. His core thesis: **Fable is not "a better Opus"** — reusing old Opus-era prompts wastes it. The real gain is *how far it can go* on end-to-end work: implementing, testing, verifying, and breaking tasks into sub-agents and workflows.

The video is split into two halves. The **first half** is cost min-maxing (reasoning-effort discipline and routing token-heavy work to cheaper models like GPT-5.5 via the Codex CLI). The **second half** is the live workflow: triaging a backlog of 16 stale pull requests on his project **Lakebed**, then setting a long-running "goal" that shipped roughly a month of planned work in ~5.5 hours for about **$150** total across all models. He closes with parallelization tricks (T3 Code + Tailscale + work trees) and a note on reading a codebase's health by how long an agent takes to fix things.

---

## Table of Contents

1. [The Big Picture: Fable Is a New Era, Not a Better Opus](#1-the-big-picture-fable-is-a-new-era-not-a-better-opus)
2. [Cost Min-Maxing, Part 1 — Reasoning Effort Discipline](#2-cost-min-maxing-part-1--reasoning-effort-discipline)
3. [Cost Min-Maxing, Part 2 — Routing Work to GPT-5.5 via Codex CLI](#3-cost-min-maxing-part-2--routing-work-to-gpt-55-via-codex-cli)
4. [Configuring `CLAUDE.md`: The Model-Selection Glossary](#4-configuring-claudemd-the-model-selection-glossary)
5. [The Skills: Codex Review, Implementation & Computer Use](#5-the-skills-codex-review-implementation--computer-use)
6. [The Live Workflow — Triaging & Shipping the Lakebed Backlog](#6-the-live-workflow--triaging--shipping-the-lakebed-backlog)
7. [Parallelizing Everything: T3 Code, Tailscale & Work Trees](#7-parallelizing-everything-t3-code-tailscale--work-trees)
8. [Judging Output: Time-Taken as a Codebase Health Signal](#8-judging-output-time-taken-as-a-codebase-health-signal)
9. [Final Pro Tip & Closing Thoughts](#9-final-pro-tip--closing-thoughts)
10. [Appendix A — Caption Corrections Log](#appendix-a--caption-corrections-log)

**Callout legend:** 💡 TIP · 🛠️ TOOLS · 📏 RULE · 💬 OPINION · ⚠️ CAUTION

---

## 1. The Big Picture: Fable Is a New Era, Not a Better Opus

*Framing · Mindset shift*

- The speaker lost access to Fable for a stretch, fell back to **Opus 4.8** and **GPT-5.5**, and found the work quality dropped enough that a project (Lakebed) stalled with 20–30 half-finished PRs piling up.
- When Fable returned, he reports getting **more work done in one day than in the entire prior month** — clearing planned-but-unfinished work end to end.
- The stated key insight: the improvement isn't only raw intelligence or code quality — it's **how much further Fable can go** on full implementations (writing, testing, verifying) and especially at **decomposing tasks and handing them to sub-agents**.
- He references a companion video addressing "misconceptions" (claims the model is nerfed, terrible, or too expensive) and recommends watching it first, though he calls it optional.

> 💬 **OPINION**
> "This model isn't a better Opus." Taking prompts that worked for Opus and handing them to Fable will *not* yield much improvement — the mindset and prompting have to change to exploit longer, end-to-end autonomous runs. He frames Fable as "a fundamental change in what these models are capable of."

> 📏 **RULE**
> To benefit from a more capable agentic model, restructure work around **longer autonomous runs and sub-agent decomposition** rather than treating it as a drop-in replacement for a previous model with the same prompts.

---

## 2. Cost Min-Maxing, Part 1 — Reasoning Effort Discipline

*Cost control · Configuration*

He deliberately covers cost reduction *before* the exciting workflow, because adopting the workflow blindly is expensive — his first 3 days with Fable would have cost thousands of dollars if paid in cash.

- The single biggest lever: **do not run Fable above "high" reasoning effort.** The options to the right of high — **x-high**, **max**, and **Ultra Code** — are described as "dangerous."
- Why: x-high and max **second-guess themselves and run in loops**, reasoning longer and longer, producing over-engineered code with far too many changes for a simple request — at drastically higher cost.
- Reasoning effort applies **per tool call / per change**, not to how long the agent can run overall. A 500-step task doesn't get more steps from max — it just **overthinks each step**. Higher effort ≠ "can solve harder problems or work longer."
- He notes **Ultra Code uses "high" under the hood** — it just spins up many more of them — which he reads as Anthropic itself agreeing high is the best value.
- Every person he spoke to who was blowing through their usage was on x-high, max, or Ultra Code.

> 📏 **RULE**
> Keep reasoning effort in the **low → high** range; **high is the best bang for your buck** and is the default for a reason. Low/medium/high can still run for very long times and are capable of things GPT-5.5 can't do.

> 💡 **TIP**
> Just leave it on **high** and stop thinking about it. The speaker estimates this one change alone cuts many people's bills by half or more.

> ⚠️ **CAUTION**
> The x-high / max / Ultra Code options are visually tempting ("a fancy gradient… like a slot machine"). Resist. They tend to over-reason, over-change, and over-charge.

> 💬 **OPINION**
> He is "a little scared" the whole Anthropic 5-family may have an over-reasoning problem at the top two effort settings, and observes GPT-5.5 and (to a lesser degree) Opus 4.8 also tend to over-reason. Presented as his personal read, not established fact.

---

## 3. Cost Min-Maxing, Part 2 — Routing Work to GPT-5.5 via Codex CLI

*Cost control · Model routing*

- Core move: teach Claude Code to **shell out to GPT-5.5 via the Codex CLI** for token-heavy or specialized tasks, so Fable orchestrates but doesn't pay for the expensive grunt work.
- The trigger phrase in his `CLAUDE.md` is literally **"shell out"** — signalling the model can call GPT-5.5 through `bash` (which Claude Code already has).
- Tasks worth routing to GPT-5.5 / Codex: **computer use** (where OpenAI currently far outperforms Anthropic — Xcode setup, navigating complex apps, hundreds of screenshots), plus **digging through logs**, **reading giant PDFs / implementation specs**, and other high-token investigation.
- Result on the big Lakebed run: total spend across *all* models ≈ **$150**, fitting inside two subscriptions. Neither broke 40% usage; his Codex sub sat around **15%** for the whole week.
- He clarifies a caption artifact: the model's `CLAUDE.md` says OpenAI is "near free… due to a deal," but he has **no special OpenAI deal** — Claude just phrased his note that way. The real point is Codex usage limits are extremely generous (he estimates ~$14k/month of inference), so anyone gets effectively the same headroom.

> 💡 **TIP**
> Setting up model routing took him about **one hour** and massively cut costs. Route the expensive, high-token, or computer-use tasks to GPT-5.5/Codex; let Fable steer.

> 🛠️ **TOOLS & COMMANDS**
> - **Codex CLI** — OpenAI's CLI; the only way to reach GPT-5.5. Called from Claude Code via `bash`.
> - **Codex desktop app** — strong **computer use**: full Mac control (Xcode setup, app navigation, screenshots, sending a video when done).
> - For investigation / data analysis he runs `codex exec --read-only` directly with a self-contained prompt.
> - Skill hooks referenced: `codex implementation`, `codex review`, `codex computer use`.

> 💬 **OPINION**
> On code quality: GPT-5.5 "writes TypeScript like a Python dev and Rust like a super-paranoid C++ dev." It solves any problem and matches shown patterns well, but its style isn't what he wants for public-facing SDKs/APIs — hence letting Fable steer and review.

---

## 4. Configuring `CLAUDE.md`: The Model-Selection Glossary

*Configuration · Prompt engineering*

- Most of his work went into his **global `CLAUDE.md`**: preferred tech for new apps, code style, general preferences — plus a section for **picking the right model for workflows and sub-agents**.
- He explains the two mechanisms the config steers:
  - **Sub-agents** — the agent spawns other agents to do things (e.g., five sub-agents to analyze five files).
  - **Workflows** — a JavaScript file the model writes that **programmatically** defines multi-stage work, feeding one stage's results into the next (fan-out and verify).
- Fable is now smart enough to **invent sub-agent archetypes** (reviewer, adversarial reviewer, exploratory, etc.) per task — so hand-defining fixed archetypes is no longer worth it.
- Because Fable was trained before GPT-5.5 / Opus 4.8 existed, **it doesn't know those models' current strengths** — so he encodes his own "gut feel" ratings in the config.
- He rates each model on three axes he cares about — **intelligence** (hardest problem it can handle unsupervised), **taste** (UI/UX, code quality, API design, copy), and **cost**:

| Model | Intelligence | Taste | Cost (to him) |
|-------|--------------|-------|---------------|
| **Fable 5** | Best in class | Best in class | High (worst) |
| **GPT-5.5** | Very high | Low | Very low (rated "9/10" cheap for him) |
| **Opus 4.8** | High (below GPT-5.5) | High | Often cheaper than Sonnet 5 |
| **Sonnet 5** | Lower | Slightly higher than GPT-5.5 | Token-hungry (not much cheaper) |
| **Haiku** | ⚠️ "Never use Haiku" — not useful for anything real with GPT-5.5 effectively free | | |

> 💡 **TIP**
> The most valuable thing in a `CLAUDE.md` / `AGENTS.md` is effectively a **glossary**: define the terms you use (e.g. what *intelligence* and *taste* mean to you). This aligns your task descriptions with the model and tells it how to apply those terms when choosing which model to call.

> 📏 **RULE** *(written by the model, endorsed by him)*
> - Ratings are **defaults, not limits** — the model has standing permission to override them. If a cheaper model's output doesn't meet the bar, re-run or redo with a smarter model **without asking**. "Judge the output, not the price tag."
> - Bulk mechanical work (clear-spec implementations, data analysis, migrations) → GPT-5.5 (effectively free).
> - Anything user-facing (UI copy, API design) needs **taste > 7**.
> - Reviews of plans/implementations → Fable 5 or Opus 4.8, optionally GPT-5.5 as an extra independent perspective.

> ⚠️ **CAUTION** *(nuance he flags)*
> The model auto-wrote a line making **cost** a hard priority axis ("Intelligence > Taste > Cost… cost is a tiebreaker only"). He read it live and **disagreed**: don't let cost *prevent* using the right model — instead use cheap models to gather info and try things first, then move the real work to a more expensive model. This is a good illustration of reviewing model-generated config rather than trusting it.

> 🛠️ **TOOLS** *(workflow / GPT-5.5 quirk)*
> You can't select GPT-5.5 directly as a model when defining a Claude Code workflow — workflows must call a Claude model. Workaround he encoded: have **Sonnet on low** spawn Codex/GPT-5.5, collect the result, and report it back (cheap orchestration). He also asked for a **prefix on sub-agents** using GPT-5.5 so he could spot them in workflow logs.

---

## 5. The Skills: Codex Review, Implementation & Computer Use

*Configuration · Skills*

- He is "normally not a big skills user" and plans to delete these once models (or Anthropic's computer use) improve — but for now they're very helpful. He keeps only a few.
- **Codex Review skill** — asks the Codex CLI (GPT-5.5) for an independent review of uncommitted changes, a branch diff, a commit, or a specific implementation. Meant to be called by a sub-agent that triggers Codex and passes feedback back up.
  Defined workflow: identify the review target → create a temp artifact directory for the Codex report → run `codex review` with a focused prompt → read the report and **verify important claims against the code** before presenting them.
- **Codex Implementation sub-agent** — similar shape, for bounded work (usually on a work tree). "A little more guarded than I'd like," but works well enough.
- **Computer Use skill (his favorite)** — lets Claude borrow Codex's computer-use powers without building it into Claude or burning huge usage. Invokes Codex/GPT-5.5 to run local app verification: browser automation, simulators, screenshots, app launching, runtime inspection.
- Key mechanic: **the model only sees a skill's *description* until it calls the skill** — so the description must carry enough info for the model to decide whether to invoke it, then the rest of the context loads on use.

> 💡 **TIP** *(learned by iterating)*
> - The **commands** inside a skill matter most — not because the model usually gets them wrong, but because the rare miss is very annoying. When it errors, ask the model "what did you get wrong / what's the right structure?" then paste the corrected command into the skill.
> - Prompt Codex **simply**. Claude tends to prompt Codex as if it were Claude — it isn't. Codex won't do things you didn't ask, so heavy guardrails like "do not edit files" are often unnecessary.
> - Handle the empty-result case explicitly: tell the skill that **if Codex finds nothing, say so clearly** and name the review target it inspected. This stopped the parent model from getting confused and re-running.
> - Consider broadening trigger descriptions to a sensible default — he edited "when the user asks Claude to have Codex test a flow" down to just "when the user asks Claude to test a flow."

> 📏 **RULE** *(delivered emphatically)*
> **Don't blindly copy-paste someone else's skills/config.** He deliberately doesn't post his files as links. Screenshot them, hand them to a model, and have it guide you to build your own. If you're scared of editing these files, get over it — you need to be unafraid to make small changes and break things. Adapt as you go; it's cheap and it compounds.

---

## 6. The Live Workflow — Triaging & Shipping the Lakebed Backlog

*Live demo · Prompting patterns*

The centerpiece: clearing **16 open, stale, partially-finished PRs** on his (solo, unreleased) project **Lakebed** and then shipping ~a month of planned work.

### Step 1 — Triage prompt

He opened with a deliberately structured request he calls "a good example of a prompt for this era":

> 🛠️ **TOOLS** *(prompt pattern, paraphrased structure)*
> *"Investigate and review the open PRs for Lakebed right now."* Return a list indicating which are: **ready to merge**; **mostly good but need a rebase / small touch-ups**; **trumped** (by better PRs or already-merged work); and **good ideas better off scrapped and rewritten**. **"Use a workflow to break up the work into multiple reviewers to help solidify your decisions."**

- The model spawned a workflow, ran, and returned a triage: **48 agents finished — 16 investigators (one per PR)**, each verdict stress-tested by a Fable + Opus judge panel; **14 of 16 were unanimous**, and it resolved the 2 contested ones. It also gave a suggested order of operations (e.g., merge #69, fix the allow-list for #68, rebase #61, then #48…).
- He **read all of it** to understand the plan, then leveraged a safe **staging environment** (merging to main only deploys to staging; prod stays human-gated) to move fast — "let's YOLO a little."

### Step 2 — Clean up + spec the remaining work

Next prompt: close the trumped/dead PRs, then for the keepers write up new **HTML plans** (via his HTML planning skill) for the best path forward, honoring Lakebed's goal of **simplicity**. Break the planning into sub-agents, review the plans with sub-agents too, link each plan back to the PRs that inspired it, and share the links for review.

### Step 3 — Align via questions, then set a "goal"

- He asked clarifying questions (e.g., whether to do it as one workflow or hand-made work trees). The model pushed back thoughtfully: a single workflow is the **wrong tool** for a checkpoint-driven program (each PR needs CI + human review + merge before the next rebase). It recommended orchestrating from the current session, spawning work trees itself, and using workflows only for **multi-agent review passes**.
- He then had it write the plan as a `to-do.md` to crank through.

> 🛠️ **TOOLS** *(the "goal" — long-running loop)*
> A **goal** tells the model to keep going until conditions pass. His conditions: complete all discussed work, with explicit permission to **create work trees, rebase, branch, merge PRs, close PRs**. Instructions included: work step-by-step, mark each item in `to-do.md` done as completed, commit/merge the to-do changes as you go, review thoroughly, and — crucially — **do not merge code until the automated reviewers approve** (his setup: **Bugbot, Macroscope, Code Rabbit**).

- It then **ran for ~5 hours**; every time he checked GitHub on his phone, more code had landed. A month-long roadmap he'd been circling got merged into Lakebed.
- He stress-tested the result himself and spun up **other agents** to try new features, old features, and porting old-style apps to the new way, plus agents to diff prod vs main and flag risks. Almost nothing needed fixing — he burned **more tokens verifying** than producing the work.

> 📏 **RULE** *(safety architecture)*
> Aggressive auto-merge is only sane because **production stays human-in-the-loop.** Merging to main deploys to **staging only**; the agent cannot ship or touch prod. Set up this guardrail before letting an agent "merge with confidence."

> 💡 **TIP**
> - **Ask your models questions** when unsure — it aligns you and the model on the plan. "It's almost like that's what they were originally built for."
> - Have the agent capture the plan as a **to-do file in the repo** so long runs have a durable checklist to work and commit against.
> - Iterate your config from real failures: when he hit a problem mid-run he'd return to the original thread, ask how to prevent it, tell the model to **cut its suggestions in half**, then add them to the config.

> 💬 **OPINION**
> He admits merging straight to main "might sound insane" and that he's "still not pushing it hard enough" since so little needed fixing. Lakebed went from ~a month behind to ~a month ahead of schedule. These are his personal takes on his own risk tolerance and project state.

---

## 7. Parallelizing Everything: T3 Code, Tailscale & Work Trees

*Tooling · Multi-machine workflow*

- Motivation: he got frustrated running Claude over **SSH** (broken image pasting, poor select behavior, bad scroll), so he went back to **T3 Code**.
- **T3 Code** doesn't have to run on the same machine as your agents. Pair it with something like **Tailscale** to connect to another computer from the T3 Code website or app. The **T3 Code mobile app** (open source, in the repo, buildable yourself) let him do serious work from his phone while at a conference.
- This made parallelizing trivial: any time an idea or bug appeared, he'd **spin up a new work tree or workflow** for it — including from his phone.
- Concrete phone workflow for a flaky test: screenshot the failure → open T3 Code → pick which machine + which repo directory (he has one repo on 4 machines, one of them in 3 places) → pick a model (Fable) → paste the image → prompt: *"figure out why this test fails randomly… it's on a work tree so this won't affect other work,"* plus the PR number (**#3683**) and a link to the bad run. Then re-run the job with less worry.
- **Merging parallel work trees:** instead of handing a teammate five separate PRs, he asked Fable to pull the changes from all the work trees into **one branch with conflicts handled** — done in ~5 minutes — so he could test everything at once and file a single documented PR.
- He notes T3 Code is fully open source, currently un-monetized, and he's spent (his figure) **over $250k** on tokens and salaries building it — plus a forthcoming **T3 Connect** service to remove the manual Tailscale setup.

> 🛠️ **TOOLS**
> - **T3 Code** (web + desktop + open-source mobile app) — remote-control agents across machines.
> - **Tailscale** — mesh VPN to reach your other computers.
> - **T3 Connect** — upcoming service to skip manual Tailscale setup.
> - **Work trees** (git worktrees) — isolate parallel experiments so they don't affect other work.
> - Machines in play: main laptop, **Mac Mini**, Linux boxes (he references his Linux setup video).

> 💬 **OPINION** *(aside)*
> He's frustrated with **GitHub**'s slowness — says the slowest part of the whole workflow is waiting for GitHub load times, and he'd "gladly pay $100/month" for a faster equivalent. Purely his personal gripe.

---

## 8. Judging Output: Time-Taken as a Codebase Health Signal

*Mental model · Reviewing agent work*

- He doesn't expect most phone-spawned code to be merged — part of the point is **gauging how hard a problem actually is** by how long the agent takes.
- His rough heuristic (personal, but broadly useful):
  - **Under ~3 minutes** → probably a simple fix; comfortable filing the PR.
  - **~15 minutes** → "a little scary," worth closer attention.
  - **An hour or more** → something may be wrong with the architecture; go deeper.
- Examples: a mobile thread-scroll-jumping fix took **over 1.5 hours** → he won't blindly merge it. A "sliding back" bug fixed in **2 min 20 sec** was *too* simple — it referenced a "drawer" behavior he wasn't sure still existed, so he questioned it and found the model was partly wrong. Both extremes warranted scrutiny.

> 📏 **RULE**
> Use **time-to-fix and number of files touched** as a diagnostic for where a codebase is healthy vs. fragile. Then reason about the **architecture and the request** — not just whether the diff reads correctly. When unsure, **ask the model questions** rather than guessing.

---

## 9. Final Pro Tip & Closing Thoughts

*Tooling · Wrap-up*

- **Vibe Proxy** — if you're worried about hitting usage limits, it **auto-splits traffic across multiple accounts**. Easier to set up than he expected.
- Trade-off he flags: Vibe Proxy uses the **API-key version of Claude Code**, so you lose some built-in features (e.g. the `/remote` control), which he says he hasn't really missed.
- Closing sentiment: the volume and ambition of his work has ramped up massively; he's "having more fun than ever" and invites viewers to try the workflow themselves.

> 💡 **TIP**
> If usage caps are the constraint, look into **Vibe Proxy** to distribute load across accounts — accepting the loss of a few built-in Claude Code conveniences.

> 💬 **OPINION** *(the throughline)*
> His overarching claim is emotional and personal: Fable "one-shot" him, he loves the model, and the biggest unlock wasn't any single trick but **changing how his brain works when collaborating with the model** — being more ambitious, delegating aggressively to sub-agents/work trees, and verifying heavily. Treat the specific numbers and setups as his experience, not universal benchmarks.

---

## Appendix A — Caption Corrections Log

*Transcript fidelity*

Auto-caption misspellings corrected in this summary. Proper nouns, commands, and numbers were preserved verbatim where the transcript was clear. **(?)** marks corrections where some uncertainty remains.

| As transcribed | Corrected to | Note |
|----------------|--------------|------|
| "codecs" / "codeex" / "Codeex" | `Codex CLI` | OpenAI's Codex command-line tool |
| "GPD55" / "GBD55" / "GBD 5.5" / "GPT55" / "GBT55" / "55" | `GPT-5.5` | Bare "55" also = GPT-5.5 |
| "Opus 48" | `Opus 4.8` | Anthropic model |
| "Sonet 5" / "set 5" | `Sonnet 5` | Anthropic model |
| "cloud code" / "quad code" | `Claude Code` | — |
| "claude.md" / "claw MD" / "claimd" / "cloudmd" | `CLAUDE.md` | Config file |
| "agents MD" | `AGENTS.md` | Config file |
| "Lake Bed" | `Lakebed` | His project name |
| "tail scale" | `Tailscale` | Mesh VPN |
| "Cotlin" | `Kotlin` | Language |
| "aents" / "sub aents" | `agents / sub-agents` | — |
| "poll requests" | `pull requests` | — |
| "implicitations" | `implementations` | — |
| "glossery" | `glossary` | — |
| "readon" / "read on" | `--read-only` | In `codex exec --read-only` |
| "Xcode" | `Xcode` | Preserved (already correct) |
| "soy.link / soyv.link/infinite red" | `soydev.link/infinite-red` **(?)** | Best-guess of speaker's link shortener; verify exact URL |
| "T3 code electron desktop app" | `T3 Code Electron desktop app` | Capitalization normalized |
| "Bugbot, Macroscope, Code Rabbit" | Preserved as-is **(?)** | Automated code reviewers; "Bugbot"/"Macroscope" spelling assumed from audio |
