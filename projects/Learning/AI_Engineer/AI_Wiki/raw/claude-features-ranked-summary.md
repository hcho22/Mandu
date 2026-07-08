# Every Claude Feature Ranked (D Tier to Top 12)

*Detailed summary of a YouTube tutorial in which the creator tier-ranks the Claude ecosystem — Claude chat, Claude Cowork, and Claude Code — based on 500+ hours of use.*

---

## Overview

The speaker ranks Claude features from **D tier** up through **A tier**, then counts down a **Top 12** (effectively the S tier). Rankings are explicitly personal: they reflect how much each feature changes his day-to-day work, which is mostly **knowledge work and automation** — not building software or SaaS products — so developers may weigh things differently. His #1 takeaway is **Skills**: reusable markdown "recipes" that make Claude execute repeat tasks consistently. Other top picks center on autonomy and visibility: the status line, scheduled routines, remote control from a phone, looping reminders, sub-agents, checkpoint rewind, agent teams, auto-memory, usage insights, cloud planning, and goal-driven runs.

> **📖 How to read this document**
> - **`[OPINION]`** marks statements presented as the speaker's personal preference or judgment.
> - **`[RULE]`** marks advice the speaker presents as a general rule or best practice.
> - Exact tool names, commands, and numbers are preserved; obvious caption misspellings (e.g., "cloud code," "clawmd") are corrected. See the [appendix](#appendix-caption-corrections--uncertain-terms) for the full correction log.

---

## Table of Contents

1. [Intro & How the Ranking Works](#1-intro--how-the-ranking-works)
2. [D Tier — Essential Groundwork, Nobody's Favorite](#2-d-tier--essential-groundwork-nobodys-favorite)
3. [C Tier — Great Features He Rarely Uses](#3-c-tier--great-features-he-rarely-uses)
4. [B Tier — Super Useful, Just Outside the Top Picks](#4-b-tier--super-useful-just-outside-the-top-picks)
5. [A Tier — Honorable Mentions](#5-a-tier--honorable-mentions)
6. [The Top 12 Countdown (#12–#6)](#6-the-top-12-countdown-126)
   - [#12 — `/goal`: run until a condition is met](#12--goal-run-until-a-condition-is-met)
   - [#11 — Ultraplan: offload planning to the cloud](#11--ultraplan-offload-planning-to-the-cloud)
   - [#10 — `/insights`: a report on how you use Claude Code](#10--insights-a-report-on-how-you-use-claude-code)
   - [#9 — Auto-memory: Claude improves its own memory](#9--auto-memory-claude-improves-its-own-memory)
   - [#8 — Agent teams: panels and debate boards](#8--agent-teams-panels-and-debate-boards)
   - [#7 — `/rewind`: roll back to a checkpoint](#7--rewind-roll-back-to-a-checkpoint)
   - [#6 — Sub-agents: parallel background workers](#6--sub-agents-parallel-background-workers)
7. [The Top 5 (#5–#2)](#7-the-top-5-52)
   - [#5 — `/loop`: repeating prompts on a local cron](#5--loop-repeating-prompts-on-a-local-cron)
   - [#4 — Remote control: drive your local session from your phone](#4--remote-control-drive-your-local-session-from-your-phone)
   - [#3 — Routines: schedule an actual agent](#3--routines-schedule-an-actual-agent)
   - [#2 — Status line: see your model, effort, and context at all times](#2--status-line-see-your-model-effort-and-context-at-all-times)
8. [#1 — Skills: The Single Biggest Leverage](#8-1--skills-the-single-biggest-leverage)
9. [Final Thoughts & Resources](#9-final-thoughts--resources)
- [Appendix: Caption Corrections & Uncertain Terms](#appendix-caption-corrections--uncertain-terms)

---

## 1. Intro & How the Ranking Works

The speaker has spent **over 500 hours** across Claude's ecosystem: chat, Cowork, and Claude Code. He ranks features from D up to his Top 12, by one criterion: **impact on his actual day-to-day work** — not global popularity and not how "cool" a feature is.

**`[OPINION]`** The whole list is framed as subjective: he does mostly knowledge work and automation rather than heavy software engineering, and says viewers who build software or SaaS "might disagree with some of these." He notes his slides were built with Claude Code itself.

> **💡 Tips, tricks & actionable advice**
> - **`[RULE]`** Value features based on *how you* use Claude — take any ranking "with a grain of salt."
> - The video's stated goal: surface features you may not know about or may be using incorrectly.

---

## 2. D Tier — Essential Groundwork, Nobody's Favorite

**`[OPINION]`** D tier is not "bad" — these features are "very real and very useful," just unexciting baseline plumbing ("nobody's favorite feature"). Standouts he calls out:

**CLAUDE.md** — essential project setup; without it a project "doesn't feel very good," but it's the bare-minimum groundwork. **Context lifecycle** — `/clear`, `/compact`, and resuming a conversation. **Web search / web fetch** — Claude Code's native search, which can spin off research immediately. Also in this tier: **file uploads, fast mode, permissions, custom themes,** and the **IDE extension**.

> **💡 Tips, tricks & actionable advice**
> - Try `/theme`: switch auto / dark mode, use a **colorblind-friendly** theme, or define fully custom themes. **`[OPINION]`** Even the speaker only discovered this while making the video.
> - **`[OPINION]`** In VS Code he prefers running Claude Code in the **terminal**, but the IDE extension is where he started when first learning — a fine on-ramp.

---

## 3. C Tier — Great Features He Rarely Uses

**Voice mode** — `/voice` lets you talk and Claude dictates for you. He prefers a third-party dictation tool (captioned "Glido") as "even faster and better."

**Cowork** — **`[OPINION]`** "an amazing product," but he skipped it and went straight to Claude Code, arguing that "pretty much anything you can do in Cowork, you can do in Code," so it's better to learn the more capable tool well. He stresses Claude Code is not just for engineering: he uses it as his **executive assistant** and has turned it into his "AI operating system."

**Interactive connectors** — in chat or Cowork, you log in to a service and instantly get all its tool calls, instead of wrestling with terminal setup. **Local file access** — a major inherent benefit of local terminal coding agents.

> **💡 Tips, tricks & actionable advice**
> - **`[RULE]`** If you are completely non-technical and overwhelmed, **starting with Cowork is absolutely fine**.
> - Connectors are the low-friction path to tools: log in once and the tool calls are just available.

---

## 4. B Tier — Super Useful, Just Outside the Top Picks

**Dynamic workflows** — he's "been loving" this: token-hungry but excellent at processing in parallel. **`[OPINION]`** Rated B mainly because it was very new at recording time and he hadn't yet settled how it fits his daily routine (he has a separate full video on it). **Deep research** — `/deep-research` plus a topic automatically invokes one of those dynamic workflows.

**Git worktrees** — run isolated copies of a codebase so parallel work never collides, then merge back together; **`[RULE]`** especially important when sharing a codebase with others or juggling multiple features. **Ultra review** — a slash command that spins up a code review in the cloud. **`[OPINION]`** His one gripe: typing it doesn't trigger the rainbow-color text effect that "ultrathink" and workflows get.

**Interactive charts** — ask Claude chat for diagrams/interactive elements and it builds them inline. **Recap** — if a Claude Code session has been idle, the terminal shows a recap of what that session was working on (e.g., his showed a slide deck for an upcoming Claude Code hooks video). Also here: **Claude for Microsoft 365, Claude in Chrome, computer use**.

> **💡 Tips, tricks & actionable advice**
> - Lots of terminal tabs open? The **recap** at the bottom tells you instantly what each session was doing.
> - Working with teammates or on several features at once? Adopt **git worktrees** for isolation + clean merges.

---

## 5. A Tier — Honorable Mentions

**Google Workspace CLI** — **`[OPINION]`** his #1 honorable mention, though "not actually a Claude feature." Nearly everything he does lives in ClickUp or Google (Sheets, Docs, Drive, Gmail, Calendar), so letting his agent drive Google via CLI — and building skills around that CLI — makes everything easier to touch and maintain.

**Dispatch** — the "channels" feature (released, he notes, "when OpenClaw was just going nuts") that lets you continue conversations with your Claude from your phone, especially for Cowork runs. **Claude desktop app** — he keeps it open beside VS Code: it manages his **cloud and local routines**, shows multiple projects/sessions visually in a left-hand sidebar, and copies/pastes conversation text cleanly — terminal copies come out with weird wrapping and spacing.

**Claude Design** — his team uses it heavily: shared design systems for different landing-page and offer types, inline comments, and very fast proof-of-concept spin-up. Plus: **auto mode** (his preferred permission level), **Claude Code hooks, effort levels, agent view** (a dashboard of all terminals running inside Claude Code), **`/btw`** (ask side questions without interrupting the main terminal's task — captioned "slash, by the way"), **`/context`**, and **prompt caching** — a big silent token-saver running in the background.

> **💡 Tips, tricks & actionable advice**
> - Use the **desktop app** (or IDE extension) when you need to copy/paste long answers — no terminal wrapping.
> - Live in Google Workspace? Give your agent the **CLI** and wrap your common operations in skills.

---

## 6. The Top 12 Countdown (#12–#6)

*These are the features he "actually uses all the time." (The caption reads "didn't make my top 30" for B tier, but the countdown is a top 12.)*

### #12 — `/goal`: run until a condition is met

Tell Claude an objective and it won't stop until the condition is hit, with verification built in. Demo: "research the best riddles and don't stop until you pull back three riddles you'd consider very hard to solve" — completed in **43 seconds**. Real example: the globe element on his website (AI Automation Society) loaded slowly, so he ran "/goal … don't stop optimizing this page until the user would refresh and the globe appears instantly" — it ran about **an hour and a half** trying different approaches, and the globe now loads essentially instantly.

> **💡 Tips, tricks & actionable advice**
> - **`[RULE]`** Write an objective **"definition of done"** — subjective criteria like "very hard to solve" weaken the loop. If there's a metric to optimize, use it.
> - **`[OPINION]`** Ignore the 24–48-hour marathon demos; he's never needed one. The value is firing off a goal, going to lunch or to bed, and having high confidence it's done when you return.
> - Works for orchestration too: "`/goal` execute these skills for me and don't stop until X, Y, and Z."

### #11 — Ultraplan: offload planning to the cloud

Typing **ultraplan** (it gets the rainbow-color effect) offloads planning to the cloud across multiple planning agents. Demo: "help me figure out how I can make five times the monthly recurring revenue compared to the previous month" — a deliberately ambiguous big task. Claude asks "do you want to run in the cloud?", returns a link, clones the repo, and plans in the cloud; you can pull the plan back into the terminal or start executing it in Claude on the web. His run showed **five background tasks**.

> **💡 Tips, tricks & actionable advice**
> - **`[RULE]`** Reach for ultraplan when a task is big enough that real planning effort up front pays off.
> - Planning runs in the background — **you can keep working in the terminal** while the cloud plans.

### #10 — `/insights`: a report on how you use Claude Code

`/insights` generates an HTML report on your past **30 days** of usage: what you do a lot, what you're doing badly, features to utilize more, and skills you should build. His report covered **over 1,500 messages across 153 sessions** (only ~2–3 weeks of local data because he'd just gotten a new PC). Sections include what's working, what's hindering you, quick wins to try, and ambitious workflows, with a clickable table of contents (e.g., "where things go wrong").

> **💡 Tips, tricks & actionable advice**
> - **`[RULE]`** Re-run it periodically to watch how your Claude Code usage evolves and to harvest the suggested quick wins.

### #9 — Auto-memory: Claude improves its own memory

Originally released under the name "auto-dream": at intervals (every so many sessions, conversations, or amount of time) Claude searches back through what you did together and updates its own memory without being prompted — it "dreams and makes itself smarter."

> **💡 Tips, tricks & actionable advice**
> - Run `/memory` to check whether auto-memory is enabled — **if it's off and you want it, turn it on**. The docs explain how it works in detail.

### #8 — Agent teams: panels and debate boards

**`[OPINION]`** "One of my favorite features ever," though **token intensive**. Agent teams are groups of agents that can **talk to each other**: he creates panels/debate boards with personas (e.g., one complete beginner, one CEO, etc.) that analyze or brainstorm a topic through rounds of debate until they reach agreement — useful for hearing genuinely different perspectives.

> **💡 Tips, tricks & actionable advice**
> - **`[OPINION]`** His budget trick: when ~**30 minutes** remain in the **5-hour** usage window with ~**50%** of the session left, he "spends" the surplus on agent teams.
> - It's experimental: enable **agent teams in your .claude settings** first; after that you can spin up teams with completely natural language.

### #7 — `/rewind`: roll back to a checkpoint

Rolls both your **code and the conversation** back to an earlier checkpoint — you pick the exact prompt in the conversation to return to. **`[RULE]`** Because everything is cached and reloaded, it's better for your context to **rewind** when Claude gets something wrong than to say "no, that was wrong, do it this way instead" and pile corrections on top.

### #6 — Sub-agents: parallel background workers

Sub-agents can be invoked automatically in the background or on request. Key contrast with agent teams: **agent teams talk to each other and debate; sub-agents work in parallel and only report to the main terminal session** that invoked them. In his .claude directory — alongside skills, rules, and workflows — there's an **agents** folder of markdown files: each defines an agent, the tools it may use, and any skills that live inside it, and gets invoked much like a skill.

> **💡 Tips, tricks & actionable advice**
> - **`[RULE]`** Customize agents as markdown files in `.claude/agents` — declare their tools and embed skills.

---

## 7. The Top 5 (#5–#2)

### #5 — `/loop`: repeating prompts on a local cron

Makes a prompt repeat on a schedule. Demo: "`/loop` every minute just remind me to use the restroom" — Claude sets it up via a **cron create tool** as a local cron job. Loops are **bound to their session**: a different terminal can run different crons, and closing the terminal kills its cron. Loops auto-shut-down if the terminal has been open longer than **seven days**.

> **💡 Tips, tricks & actionable advice**
> - No slash command needed — natural language works: "set up a recurring loop to do this every 10 / 20 minutes, every hour."

### #4 — Remote control: drive your local session from your phone

Say "enable remote control" and Claude Code gives you a link; open it on your phone or the web — or open the Claude mobile app > Code and select the session up top — and you're driving the **same local session**, fully synced: messages he sends from his phone appear on his computer and vice versa (his demo even showed the restroom-reminder loop arriving on the phone). **`[OPINION]`** He loves this for taking a walk or hitting the gym while a session keeps building or brainstorming.

### #3 — Routines: schedule an actual agent

Scheduling here means scheduling **a real agent** — your Claude Code terminal, addressed exactly the way you normally talk to it — not a deterministic Python script or bare API calls. Create one with `/schedule`, or (his preference) in the **desktop app**, where routines can be viewed on a calendar or as a list, and set up as either **local or cloud** routines.

### #2 — Status line: see your model, effort, and context at all times

**`[OPINION]`** "Probably one of the most slept-on things ever." His status line shows the model and effort (**Opus 4.8, xhigh**) and context consumption — e.g., **27%, 274,000 of 1,000,000 tokens**. **`[RULE]`** He calls context visibility "one of the most important things you need" in Claude Code: it tells him when to run his session-handoff skill, when to `/clear`, and when to `/compact`. It was the main reason he switched from the VS Code extension to the terminal.

> **💡 Tips, tricks & actionable advice**
> - Easiest fix ever: run `/statusline` and describe exactly what you want shown — you can even paste a screenshot of a status line you like and say "I want this."
> - Pair it with `/context` (visualize what's silently eating tokens in the window) and `/usage` (session/week stats: models used, token counts).

---

## 8. #1 — Skills: The Single Biggest Leverage

**`[OPINION]`** Skills are "the thing that has given me so much more leverage" and his clear #1 day-to-day feature. A skill is "basically a recipe": just as you cook lasagna from the recipe rather than from memory, the agent reads the skill and performs the task **far more consistently** than if you re-typed the same prompt every time — his examples include presentations, making thumbnails, and trimming videos.

Skills are plain **markdown files living in your .claude directory**, so they're easy to share with a team and to refine continuously (he refines his daily). You can also pull in other people's skills, or install **plugins** that bundle skills, hooks, MCP servers, and more. Skills scale in both directions: big ones can have many steps and tools and even **route to other skills** (chaining), while tiny ones work too — his **session handoff** skill is literally a four-sentence prompt he kept retyping, now one quick slash command.

> **💡 Tips, tricks & actionable advice**
> - **`[RULE]`** Turn any prompt you find yourself repeating into a skill — skills "don't have to be complex."
> - Skills aren't Code-only: the same skills work in **Claude Code, Claude chat, and Claude Cowork**.
> - Borrow before you build: grab community skills and plugins (skills + hooks + MCP servers) as starting points.

---

## 9. Final Thoughts & Resources

**`[OPINION]`** He repeats that viewers won't fully agree with the board — the point was to show his reasoning, surface unknown features, and inspire heavier use of the top 12. The full slide deck, resource guides, skills, and GitHub repos are available free in his Skool community (link in the video description): join > Classroom > All YouTube Resources.

---

## Appendix: Caption Corrections & Uncertain Terms

Auto-generated captions garbled several product and command names. Corrections applied in this summary:

| Caption text | Rendered as |
|---|---|
| "cloud code" / "claw" | Claude Code / Claude |
| "clawmd" | CLAUDE.md |
| "co-work" | Cowork |
| "slashgoal" / "SLG goal" / "SLGO" | `/goal` |
| "ultra plan" | ultraplan |
| "slashinsights" | `/insights` |
| "autodream" | auto-dream (original name of auto-memory) |
| "slashre" / "slre" | `/rewind` |
| "/deepress research" | `/deep-research` |
| "cronreate tool" | cron create tool |
| "/ status line" | `/statusline` |
| "slashcontext" / "slash usage" | `/context`, `/usage` |
| "do.claude" / "doclaude" | `.claude` (settings/config directory) |
| "A Automation Society" | AI Automation Society (his website) |
| "it spins up PC's really quick" | POCs (proofs of concept) |
| "school community" | Skool community |
| "Ultra code hooks" | Claude Code hooks (probable) |
| "slash, by the way" | `/btw` (probable; described as asking side questions) |
| "didn't make my top 30" | likely "top 12" (the countdown shown) |

**Left as captioned** (could not be confidently corrected): **"Glido"** (a third-party dictation tool) and **"Excal presentations"** (possibly Excalidraw). **"Ultra review," "ultrathink," "dispatch," "OpenClaw," "agent view,"** and **"dynamic workflows"** are kept as spoken.
