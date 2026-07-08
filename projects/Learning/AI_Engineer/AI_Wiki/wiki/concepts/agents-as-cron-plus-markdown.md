---
type: concept
tags: [agents, agent-ops, cron, skills]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Agents Are Cron Jobs + Markdown Files

The core mental model from [[one-person-company-with-agents]]: an agent = a good **cron** (a deterministic, repeatable schedule for when it runs) + a good **skill** (a markdown instruction file for how it works).

## Key points

- **Crons over heartbeats:** a heartbeat fires "whenever the agent thinks about it" and is not reliably timed; a cron runs on a guaranteed schedule. Build your own heartbeat as a minimal cron pointing at one skill.
- **DRY:** keep the cron message minimal ("use this skill"); all detail lives once, in the skill file.
- This demystifies agents: reliable automation is scheduling + instructions, not magic.
- [[every-claude-feature-ranked]]'s "Routines" are the first-class version: you schedule a *real agent* (your Claude Code terminal), not a deterministic script; `/loop` sets a session-bound local cron.

## Synthesis

This is the operational floor under the whole [[ai-operating-system]] and [[building-skills]] story: cadence (the fourth of the [[four-cs-framework]]) is literally crons, and capability is markdown skills.
It reframes "agent" from an autonomous mystery into two boring, controllable pieces, which is exactly the constrain-and-verify posture the wiki keeps returning to.
