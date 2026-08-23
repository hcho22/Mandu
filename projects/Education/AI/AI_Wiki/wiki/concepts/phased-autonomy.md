---
type: concept
tags: [agent-safety, agents, deployment, trust]
status: established
source-count: 3
last-updated: 2026-08-01
---

# Phased Autonomy (The Bike Method)

The principle from [[ai-operating-system-tutorial]] that you grant an agent or skill autonomy in stages, only after it earns trust - like teaching a kid to ride a bike (hold the seat, keep a hand ready, let go gradually, keep watching).

## Key points

- Low barriers to entry (a skill built and shipped same-day) must not create a false sense of security; too much trust in something not ready is dangerous.
- Grant autonomy incrementally, and only after a skill has demonstrated reliability.
- Every run improves the skill, so early supervised runs are not wasted time.

## The commercial version, with named stages (2026-08-01)

[[fde-in-30-days]] gives the enterprise-deployment form of the same principle, and it is the most concrete staging in the wiki:

**sandbox / controlled testing → shadow mode → increasing autonomy → full production.**

Two additions that matter:

- **A human approval step *inside* the workflow, not just around it.**
Vas "strongly recommends" all his FDEs push for this shape: intake → validation → agent drafting → **human approval** → remaining steps execute.
The approval is placed before the agent proceeds to the back half of the workflow, so the autonomy is granted per-segment rather than per-agent.
- **The staging is a trust-building mechanism, not only a safety one.**
Bringing in an agent is perceived by the client as risk, and the graduated rollout is how that risk gets retired visibly.
The [[audit-eval-deployment]] eval report is the evidence that justifies each promotion, which makes [[evals]] the thing that literally purchases autonomy.

**A harder-edged variant** from [[agentic-full-stack-build]] and [[running-teams-of-ai-agents]]: rather than a smooth ramp, both practitioners draw **one hard line at the production boundary** - broad permissions everywhere else, explicit per-access authorization for anything touching prod ([[credential-vaults]]).
That is a step function, not a gradient, and it suggests the right shape depends on whether the blast radius is recoverable.

## Synthesis

This is the deployment-time sibling of two design-time ideas: [[start-as-a-workflow]] (begin predictable, earn autonomy) and the [[minimal-useful-agent]] ladder (draft to act).
Together they form the wiki's consistent stance on agent autonomy: constrain first, widen only on evidence.
It is enforced in practice by [[capabilities-not-instructions]] (widening trust means adding keys deliberately) and measured by [[evals]] (evidence that a rung was earned).

Three sources in, this is one of the most consistently corroborated ideas in the wiki - a personal-productivity source, an Anthropic-adjacent product source, and an enterprise-consulting source all independently prescribe the same ramp.
What the third adds is that **the ramp is legible to a buyer**, which turns a safety practice into a sales structure.
