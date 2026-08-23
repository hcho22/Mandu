---
type: source
title: "Running Your Life on Codex: Jason (OpenAI Codex Team) on Automations, Skills & Browser Use"
source-type: video
author: "Jason (OpenAI Codex / Developer Experience team), interviewed"
url: "local"
date-ingested: 2026-08-05
date-created: unknown
tags: [agent-operations, agentic-engineering, codex, openai, skills, plugins, automations, browser-use, computer-use, obsidian, taste, ai-career]
concepts: [heartbeat-automation, personal-voice-skill, skills-vs-plugins, browser-use-vs-computer-use, goal-plan-worklog, reasoning-effort-discipline, self-improving-agent-loop, taste-as-moat, verification-signal-picks-the-mechanism, monorepo-for-agent-context, manager-of-agents]
---

# Running Your Life on Codex

An interview with **Jason**, a member of OpenAI's [[codex]] / Developer Experience team, on how he personally runs large parts of his work and life on Codex and the new **ChatGPT Work** app.
It is the wiki's first primary-source account from inside OpenAI's agent tooling, and the OpenAI-side counterpart to the Anthropic practitioner sources ([[designing-loops-and-workflows]], [[building-at-the-frontier]]).
It covers Work vs Codex, effort-level selection, pinned long-running threads with compaction, an Obsidian markdown vault as the agent's memory, a scheduled "Chief of Staff" automation, personal writing-voice skills, a self-improving skill, the skill-vs-plugin distinction, browser use vs computer use, building an app with a goal/plan/worklog workflow, and a closing argument that **taste** is the skill that remains.

Most of what it contributes is independent OpenAI-side confirmation of patterns the wiki already holds from Anthropic-centric sources - which is exactly its value - plus two genuine points of friction with existing pages (see the flags below).

## Key claims

### ChatGPT Work vs Codex, and effort levels

- **ChatGPT Work is a different view/UX on the same Codex engine,** not a separate product: Codex surfaces git history, PRs, and diffs; Work hides them for non-coding tasks (slides, docs) where seeing Python is not useful. Jason does much of his own work in Work now because he does not review most of the code Codex writes. (Speaker opinion, flagged as personal practice: "a lot of us don't review code anymore.")
- **Effort-level discipline:** medium effort for routine admin/ops (reading Slack, calendar, scheduling); extra-high / ultra for long complex build sessions. Model/effort names in the transcript ("GPT-5.6," "Terra," "Luna," "Sole medium") are flagged uncertain in the raw file; treat the *pattern* (match effort to task) as the claim, not the exact tier names.

### Threads, compaction, and the vault as memory

- The workspace is a small number of **pinned long-running threads**, each a persistent workspace (feedback-signal automations, daily/weekly Chief of Staff, event planning, agents-API work, a personal project, slide-making). He does **not** run hundreds of background threads.
- **Compaction** is automatic, so long threads keep prior context; for overflow he spins up [[sub-agents]], though more cautiously than Ultra mode's automatic spin-up.
- **An Obsidian vault ("Vault") is his central memory and "basically his only project."** It is just markdown files, no database, organized into projects / people / notes / daily notes / preferences. Other repos originate from it; GitHub/cloud pulls from the vault as source of truth. He **rarely opens Obsidian himself** - it exists to give his *agent* context.

### The "Chief of Staff" automation

- A **daily and weekly** automation built on **scheduled tasks**; the daily runs at 9am, 1pm, 5pm and each run reads all Slack, Twitter DMs (via computer use), unanswered email, and his Linear board, updating Linear directly when something needs cleanup, then hands him one consolidated "what needs attention" view.
- Concrete outcomes: surfacing a trip to arrange, a package to pick up, a flight **check-in automation** that texts him the boarding pass when it finds a confirmation + reference number, and screenshotting a mentioned event onto his calendar.
- Explicitly **not free**: built up incrementally over time through iteration and specific feedback.

### Start with a heartbeat, then layer

- The recommended starting point is a simple **heartbeat prompt**: "check my email, Slack, Linear every [interval] - 9am, 1pm, 5pm - and tell me what to prioritize." Then iterate with specific feedback ("make sure everything has a link," "start using Linear"), until it pre-drafts replies rather than just flagging them.
- **Auto-send is not uniform:** he reserves it for well-defined, lower-risk workflows (e.g. "make a PR, check tests, once green, DM Andrew the PR link + preview URL") and stays "surgical" on inbox/Slack triage.

### Personal voice skills and self-improvement

- A **"write me" skill** reads a past week of his Slack messages and mimics his voice, refined so tone shifts by audience (external vs team, executive vs coworker). He has tweet-me, email-me, voice-transcript-to-blog, and video-to-video-essay skills, all edited iteratively over time.
- He **periodically cleans up skill bloat**, asking Codex to audit history: "look at the past 400 sessions, which skills were never used, clean things up, interview me." Sessions are stored as JSON he can point Codex at.
- A **"self-improve" skill** (built ~4 months prior) reviews which skills are called most, reads the sessions where they ran, and surfaces recurring feedback patterns; a Slack-reply skill (transcript "Slack honey," flagged uncertain) learned to auto-reply into Slack after a task because he kept asking it to.
- Framing: managing a skill is like managing a new hire - "it's not the fact that I'm going to have a skill that just runs forever perfectly."

### Skills vs plugins

- **A skill is one component of a plugin.** A plugin bundles multiple skills, potentially multiple **MCP servers**, plus other scripts/resources (e.g. a "Better Writing" plugin bundling write/Slack/email skills to share with a team).
- OpenAI opened public submission to the **Codex plugin directory**: skill-only submissions are reviewed quickly; submissions that include MCP servers get a more thorough security audit.

### Browser use vs computer use

- **Browser use** = operating within Codex's in-app browser for website tasks; it supports OAuth/login and uses your **cookies**, so it works while logged into your accounts, and can drive **multiple tabs** at once (e.g. open every candidate product in its own tab for side-by-side review rather than a markdown summary).
- **Computer use** = OS/app-level control, for tasks with no good API path (e.g. an Airtable CSV export: open the export, press download, move the file, continue the pipeline) and general app testing.
- Anecdote: from a bike ride, he remote-controlled his MacBook via his phone, had Codex use computer use to find/fix/re-export a broken-subtitle video and post it to Slack, then poll the thread every 30 minutes to iterate (V2, V3, V4) - approved by the time he got home and used as the "Migrate to Codex" launch video.
- He does not yet let computer use complete purchases/checkouts autonomously (his own risk tolerance, not a platform limit).

### Building an app: goal / plan / worklog

- He built a drum-practice tool (rudiments, adjustable tempo, later YouTube-upload with drum-track extraction) over **~one week of iteration**, and explicitly pushes back on the "I ran one goal for six hours" framing - these tools grow through iteration.
- Before building, an extended conversation with Codex produces three artifacts (a skill-library entry called **"ultra goal"**): a **goal.md** (success criteria; work continues until met), a **plan.md** (implementation detail, tools, docs to read), and a **worklog** (a running log he reviews to see progress/blockers, since long threads compact and he will not read every message).
- **Don't write the goal file yourself** - describe the outcome and have Codex generate its own goal.md, which tends to be better-scoped. Keep it an editable file so scope changes are picked up without a restart.
- **Goals must specify a verifiable end-state:** his drum-app goal.md required Codex to use computer use to open the app, upload a specific test video by ID, and confirm the data comes back correctly - not a vague feature request.
- He no longer generates mockup images before building (needed in "the 5.5 world," unnecessary now) provided he specifies tools like **Tailwind** and **shadcn/ui**.

### Taste as the remaining skill

- Asked what to learn now that "coding is solved," his answer is **taste** - "the ability to articulate what you don't like about something." Analogy: "if you want taste, you have to eat."
- His recommended path for beginners (including non-engineers): have Codex build something, then get specific about dissatisfaction ("add a keyboard shortcut for tempo," "why does it flicker when I switch panels") rather than needing the vocabulary upfront. "The only job left is to understand what you don't like about something and put it into words and tell the AI."
- On the "manager of agents" framing raised by the host: Jason says he does **not** relate to feeling like a manager - he frames his role as caring about outcomes and quality, not hours or hands-on code. (Flagged by both speakers as personal philosophy.)

## Connections

- [[heartbeat-automation]] - the Chief-of-Staff scheduled briefing this source is the fullest account of; the OpenAI-side sibling of [[agents-as-cron-plus-markdown]] and [[production-watchdog]].
- [[personal-voice-skill]] - the write-me/tweet-me/email-me pattern (build a voice skill from your own message history, refine by audience).
- [[skills-vs-plugins]] - the source's clean definition: skill = one capability, plugin = a shareable bundle of skills + MCP servers + scripts.
- [[browser-use-vs-computer-use]] - the two automation surfaces and when each applies.
- [[goal-plan-worklog]] - the "ultra goal" three-artifact build workflow, with verifiable goals and agent-authored goal files.
- [[reasoning-effort-discipline]] - independent OpenAI-side statement of the effort lever (medium for admin, ultra for builds).
- [[compaction-over-context-window]] - automatic compaction is what keeps his pinned threads alive; a second source for the pattern.
- [[self-improving-agent-loop]] and [[self-updating-config]] - the self-improve skill and skill-bloat audit are this pattern applied to a personal skill library.
- [[monorepo-for-agent-context]] and [[context-is-king]] and [[ai-operating-system]] - the markdown vault as the agent's single source of truth; near-identical to hcho's own Mandu setup.
- [[verification-signal-picks-the-mechanism]] and [[define-the-end-to-end-gate]] - "goals must specify a verifiable end-state" is the same principle from OpenAI's side.
- [[taste-as-moat]] and [[two-kinds-of-judgment]] and [[own-the-problem-not-the-code]] - taste as the durable remaining skill.
- [[building-skills]] and [[elicitation-over-prompt-engineering]] - iterative skill-building and having the agent author its own goal.
- [[manager-of-agents]] - **tension:** Jason explicitly rejects the "manager" self-image (see the flag below).
- [[read-what-the-agent-writes]] - **tension:** "a lot of us don't review code anymore" (see the flag below).
- [[codex]], [[openai]], [[jason-openai-codex]], [[obsidian]] - entities.

## Two frictions with the existing wiki (flagged, not resolved)

1. **"A lot of us don't review code anymore"** (this source) sits against [[read-what-the-agent-writes]] and [[adversarial-code-review]] (2026-07-28 sources), which argue that not reading the agent's work is how you lose judgment. These are less opposed than they look: Jason has *moved verification to a different layer* - verifiable goal.md end-states, computer-use self-checks, and separate checker steps - rather than abandoning it. The disagreement is about *where* the check lives (reading diffs vs an executable oracle), not whether to check. Recorded on both pages.
2. **Jason rejects the "manager of agents" self-image**, which is the exact frame [[manager-of-agents]] builds on. His counter is that he cares about outcomes and quality, not about supervising labor. This is a real perspective split worth watching: [[manager-of-agents]] treats decision-throughput-as-bottleneck as the reframe; Jason treats "articulating taste" as the job and finds "manager" limiting. Both may be describing the same activity with different metaphors (the [[agent-as-employee]] page already notes the coworker metaphor is "helpful but limiting").

## Source

- **Author:** Jason (OpenAI Codex / Developer Experience team), in a recorded interview
- **Title:** Running Your Life on Codex: Jason (OpenAI Codex Team) on Automations, Skills & Browser Use
- **Format:** YouTube interview/tutorial, ingested as a detailed summary with a transcription-notes appendix
- **URL:** local (no URL captured with the raw file)
- **Raw:** `raw/codex-chatgpt-work-summary.md` (saved verbatim, immutable)
- **Ingested:** 2026-08-05

### Provenance caveats

The raw file is a summary of an auto-captioned transcript and carries a corrections appendix.
Items explicitly flagged uncertain there and preserved as uncertain here: the model/effort names ("GPT-5.6," "Terra," "Luna," "Sole medium"); the "Slack honey" skill name; Jason's X handle ("@JXNLCO," transcribed phonetically); and the team lead "Tibo."
"Codex" and "ChatGPT / ChatGPT Work" were normalized from several mis-transcriptions.
A mid-transcript Google AI Studio sponsor segment was excluded from the summary as unrelated advertising.
Speaker opinions are marked as such in the raw file and preserved as opinion above; several claims (no-code-review, no-mockups-needed, the manager framing) are explicitly Jason's personal practice, not product guarantees.
