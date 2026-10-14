---
type: entity
tags: [tool, agent-platform, open-source]
status: seed
source-count: 3
last-updated: 2026-10-14
---

# Open Claw

An open-source agent platform, configured throughout [[one-person-company-with-agents]] (Ryan Carson names his instance "R2").
(Name as transcribed in the sources; exact product spelling flagged uncertain there.)

## What shows up in the wiki

- Run as a personal chief-of-staff via the open-sourced "Claw Chief" layer (markdown files + crons), embodying [[agents-as-cron-plus-markdown]].
- Managed remotely (SSH over Tailscale) and configured by talking to Codex; a clone of Open Claw's own source is kept in the workspace so the agent can read and fix itself.
- Slack is its control surface; it is given [[agent-as-employee|its own identity and scoped permissions]].

- [[building-robust-apps-with-ai]] - OpenClaw is the agent that Ross's ([[ross-hey-fabrica]]) product Pluto actually deploys, running on Daytona sandboxes with a self-healing browser per agent.

- [[stop-prompting-design-loops-and-goals]] (2026-10-14) names its creator as **Peter Steinberger**, described by the speaker as now at OpenAI, who posted a "monthly reminder" to stop prompting coding agents and design loops that prompt them. Spelling and employer are as captioned, not verified.

## Notes

Carson deliberately uses out-of-the-box Open Claw + custom skills/crons rather than building a custom harness ("don't build a custom machine").
Now seen across two independent builders (Carson's chief-of-staff, Ross's Pluto), suggesting it is a real load-bearing agent platform, not a one-off.
