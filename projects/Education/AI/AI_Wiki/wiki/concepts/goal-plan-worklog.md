---
type: concept
tags: [agentic-engineering, workflows, planning, verification, codex]
status: seed
source-count: 1
last-updated: 2026-08-05
---

# Goal / Plan / Worklog

A three-artifact build workflow for long agent runs, from [[running-life-on-codex]], packaged by [[jason-openai-codex]] as a [[codex]] skill-library entry called **"ultra goal."**
Before building, an extended conversation with the agent about the problem produces three files:

1. **goal.md** - the success criteria. Work continues until it is met.
2. **plan.md** - implementation detail: what to write it in, which tools, which docs to read.
3. **worklog** - a running log the human reviews to see progress and blockers, because long threads [[compaction-over-context-window]] and he will not read every message.

## Two rules that make it work

- **Don't write the goal file yourself - have the agent write it.** Describe the outcome in conversation and let the agent generate its own goal.md; it tends to produce a better-scoped goal than a human writing it cold ([[elicitation-over-prompt-engineering]], [[planning-is-removing-unknowns]]). Keep it an **editable file** so expanded scope is picked up without restarting the run.
- **The goal must specify a verifiable end-state, not a vague feature.** Jason's drum-app goal.md required the agent to use computer use to open the app, upload a specific test video by ID, and confirm the data comes back correctly. The goal names the check, not just the feature ([[define-the-end-to-end-gate]], [[verification-signal-picks-the-mechanism]]).

## Relationship to the wiki's build workflows

This is the OpenAI-side statement of patterns the wiki holds from Anthropic/solo sources, with one addition:

- goal.md is [[define-the-end-to-end-gate]] made a persistent, editable artifact - and, because it demands a verifiable success condition, it is [[eval-driven-development]] at the task level.
- plan.md + worklog is [[plan-code-validate]] and [[review-plans-as-artifacts]]; the worklog specifically answers the [[read-what-the-agent-writes]] problem for long runs (you read the compressed log instead of every message).
- Having the agent author its own goal is the "the model scopes better than you do cold" move, adjacent to [[ramble-then-structure]].
- The whole triad is a [[graph-engineering]] Level-2 (file-based) workflow: each role writes its own markdown file and state persists between steps ([[agents-as-cron-plus-markdown]]).

## Synthesis

The genuinely new emphasis over the existing pages is **the goal as a living, agent-authored, verifiable file** - not a spec you hand down once, but an artifact the agent writes, you edit, and the run is held to until an executable check passes.
That reframes "planning" from a phase into a persistent contract, which is the same direction [[planning-is-removing-unknowns]] pushes from the Anthropic side.

For hcho this maps almost one-to-one onto how he already runs Purvia and Rep Today (implementation PRDs as the goal artifact, story-by-story worklogs, verifiable acceptance criteria) - so its value is confirmation plus one sharpening: the strongest goal files name the check, and the best-scoped ones are drafted with the agent, not dictated to it.
