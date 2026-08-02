---
type: concept
tags: [agents, agent-ops, cron, skills]
status: established
source-count: 4
last-updated: 2026-08-01
---

# Agents Are Cron Jobs + Markdown Files

The core mental model from [[one-person-company-with-agents]]: an agent = a good **cron** (a deterministic, repeatable schedule for when it runs) + a good **skill** (a markdown instruction file for how it works).

## Key points

- **Crons over heartbeats:** a heartbeat fires "whenever the agent thinks about it" and is not reliably timed; a cron runs on a guaranteed schedule. Build your own heartbeat as a minimal cron pointing at one skill.
- **DRY:** keep the cron message minimal ("use this skill"); all detail lives once, in the skill file.
- This demystifies agents: reliable automation is scheduling + instructions, not magic.
- [[every-claude-feature-ranked]]'s "Routines" are the first-class version: you schedule a *real agent* (your Claude Code terminal), not a deterministic script; `/loop` sets a session-bound local cron.

## How the pattern matured (2026-08-01)

Three sources in one batch show the same primitive at three very different scales, and the scaling is instructive.

| Scale | Source | Form |
|---|---|---|
| Solo founder, pre-PMF | [[one-person-company-with-agents]] | A cron + a markdown skill file |
| Solo founder, post-PMF | [[running-teams-of-ai-agents]] | Cloud **playbooks** that trigger **child triage sessions** on failure |
| Frontier lab | [[building-at-the-frontier]] | 20-30 daily **routines** across four codebases, each ending in a PR |

The mechanism did not change. Two things did:

- **The prompts got shorter, not longer.** Anthropic's dead-code and abstraction-police routines are **one-sentence prompts**, with the sophistication supplied by the model ([[self-maintaining-codebase]], [[principles-over-constraints]]). At scale, the markdown half of "cron plus markdown" shrinks.
- **Failure handling became the real design.** Ryan Carson's playbooks spawn a child session on failure and his rubric-graded loop opens PRs ([[self-improving-agent-loop]]). His own verdict: **"observability is the hard part, not the automation."** The cron is trivial; knowing it ran, what it did, and what happened to the PR is the engineering.

The local/cloud distinction also got named: [[dynamic-workflows-as-test-time-compute]] separates a **loop** (a local cron for Claude) from a **routine** (the same thing in the cloud so you can close your laptop).

**The one challenge to the model:** [[marketing-agent]] argues a cron plus a skill file is *not sufficient* for an agent whose decision requires cross-channel context - without a [[unified-data-warehouse-for-agents]] the cron has nothing to reason over.
That is a fair boundary rather than a refutation: this model holds when the decision is local to the task.

## Synthesis

This is the operational floor under the whole [[ai-operating-system]] and [[building-skills]] story: cadence (the fourth of the [[four-cs-framework]]) is literally crons, and capability is markdown skills.
It reframes "agent" from an autonomous mystery into two boring, controllable pieces, which is exactly the constrain-and-verify posture the wiki keeps returning to.

Four sources in, the pattern has held up unusually well, which is itself notable in a wiki full of one-generation advice.
What the later sources add is that the hard parts are **not** the two pieces named here - they are the observability path and the failure branch, both of which sit outside the model entirely.
See [[agent-operations]] for the area this anchors.
