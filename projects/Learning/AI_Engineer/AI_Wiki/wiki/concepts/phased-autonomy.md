---
type: concept
tags: [agent-safety, agents, deployment, trust]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Phased Autonomy (The Bike Method)

The principle from [[ai-operating-system-tutorial]] that you grant an agent or skill autonomy in stages, only after it earns trust - like teaching a kid to ride a bike (hold the seat, keep a hand ready, let go gradually, keep watching).

## Key points

- Low barriers to entry (a skill built and shipped same-day) must not create a false sense of security; too much trust in something not ready is dangerous.
- Grant autonomy incrementally, and only after a skill has demonstrated reliability.
- Every run improves the skill, so early supervised runs are not wasted time.

## Synthesis

This is the deployment-time sibling of two design-time ideas: [[start-as-a-workflow]] (begin predictable, earn autonomy) and the [[minimal-useful-agent]] ladder (draft to act).
Together they form the wiki's consistent stance on agent autonomy: constrain first, widen only on evidence.
It is enforced in practice by [[capabilities-not-instructions]] (widening trust means adding keys deliberately) and measured by [[evals]] (evidence that a rung was earned).
