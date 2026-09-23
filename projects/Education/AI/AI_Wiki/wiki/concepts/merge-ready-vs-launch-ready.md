---
type: concept
tags: [code-review, release, feature-flags, validation]
status: seed
source-count: 1
last-updated: 2026-09-23
---

# Merge Ready vs Launch Ready

Merge readiness is sufficient evidence to integrate a change under the project's rules; launch readiness is sufficient evidence and operational preparation to expose it to users.
[[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] separates these milestones using feature gates, broader quality review, and gradual rollout.

## Key points

- A gated change may be ready to integrate while remaining unready for user exposure.
- Test the control path with the gate off and the new path with it on, including background effects and integration points.
- Launch evidence includes the relevant specification, security, performance, user experience, monitoring, and recovery checks.
- Evidence must match the current revision; a review fix can invalidate an earlier test result or recording.
- A limited release can expose operational failures even when it cannot support a reliable A/B-test conclusion.

## Synthesis

A gate is a containment mechanism whose behavior needs evidence, not a certificate of safety.
Mandu's qualification: disabling a feature may stop future actions without undoing writes or external effects already performed, so recovery must be evaluated separately from the switch itself.
[[risk-based-agent-governance]] determines the depth of that evaluation, while [[agent-testing-instructions]] supplies observable proof.
For project tracking, record implementation, validation, and exposure as distinct facts rather than allowing “merged” to imply “launched.”

## Source

- [[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] - derived, undated tutorial; no universal rollout thresholds or readiness scoring model supplied.
