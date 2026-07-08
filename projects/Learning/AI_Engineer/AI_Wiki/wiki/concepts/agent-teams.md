---
type: concept
tags: [agents, multi-agent, deliberation, agentic-engineering]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Agent Teams

Groups of agents that talk to each other and debate, from [[every-claude-feature-ranked]] - distinct from [[sub-agents]] (which work in parallel and only report back to the main session).

## Key points

- Create panels or debate boards with distinct personas (e.g. a complete beginner, a CEO) that analyze or brainstorm a topic through rounds of debate until they reach agreement.
- The value is hearing genuinely different perspectives, not just parallel throughput.
- Token intensive and experimental (enabled in `.claude` settings), then driven with natural language.

## Synthesis

Agent teams are the deliberative branch of multi-agent work, where [[sub-agents]] are the parallel branch.
The debate-to-agreement structure is a generative cousin of [[adversarial-code-review]]: multiple perspectives surface what a single pass misses - here for ideas rather than bugs.
For hcho, persona debate is a lightweight way to pressure-test a plan or a design (a validation move applied to thinking, not just code).
