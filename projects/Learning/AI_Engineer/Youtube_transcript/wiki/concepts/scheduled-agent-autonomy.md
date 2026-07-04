---
type: concept
tags: [cron, scheduling, cadence, routines, autonomy, playbooks]
date: 2026-07-03
source-count: 3
status: seeded
---

# Scheduled Agent Autonomy

Making agents act on their own on a deterministic schedule - crons, routines, and run-until-done goals - so work happens automatically (the "cadence" layer) rather than only when you prompt.

## From the sources

[[one-person-company-with-ai-agents]] makes scheduling half of what an agent is:

- An agent = a good cron (when it runs) + a good skill (how it works). Crons are deterministic and repeatable; heartbeats are not reliably time-triggered ("whenever I think about it"), so he builds a custom heartbeat as a 15-minute cron pointing at one skill.
- Follow DRY: the cron message is minimal ("use this skill") and all detail lives once in the skill. Devin "schedules" run playbooks (skill-like docs), e.g., a weekly full user-journey run and nightly content pipeline; the value is improving the playbooks over time.

[[building-your-own-ai-operating-system]] names cadence as the final layer:

- Cadence is the fourth C (after Context, Connections, Capabilities): turning everything into work that happens automatically while your laptop is closed, without being asked. It depends on the layers before it - no reliable cadence without capabilities.

[[every-claude-feature-ranked]] catalogs the scheduling primitives:

- Routines schedule a real agent addressed the way you normally talk to it (local or cloud), not a deterministic script. /loop repeats a prompt on a local, session-bound cron (dies when the terminal closes; auto-shuts after 7 days). /goal runs until a verifiable condition is met - write an objective "definition of done."

## Synthesis

Cadence is where an agent stops being a tool you invoke and becomes a system that runs itself, and the sources agree on how to make that reliable. **Determinism comes from crons, not heartbeats**: a cron is a guaranteed schedule while a heartbeat is best-effort, so anything that must happen on time is a cron. **The schedule is thin, the skill is thick** (DRY): the cron or routine just says "run this skill/playbook," and all behavior lives once in the referenced file - which makes cadence a scheduled invocation of [[agent-skills]]. **Autonomy needs a verifiable stop condition**: /goal-style run-until-done only works with an objective definition of done (a metric, not "make it good"), the same discipline that makes [[evals-for-agents]] trustworthy. There is a clean layering here from [[building-your-own-ai-operating-system]]: cadence sits on top of capabilities (skills) which sit on connections and context, so scheduling autonomy is the last thing you add, not the first. And it is inseparable from [[agent-permissions-and-safety]] - an agent that acts unprompted on a schedule is exactly the case where an over-broad capability does damage nobody asked for (the 150k-email incident happened because an agent proactively picked up a task), so cadence raises the stakes on least-privilege.
