---
type: concept
tags: [code-review, release, feature-flags, validation]
status: seed
source-count: 2
last-updated: 2026-10-02
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

## Both sides of the merge button (2026-10-02)

[[token-maxing-with-agents]] describes the same split from a speed-first practitioner: before merge, make it likely the PR is safe by the time a human sees it; after merge, make bad changes easy to revert and catch problems before users do.
Its heuristic: if undoing a bad change takes more than 15 seconds, fix your systems before vibe coding.
The rule assumes a deploy target where reverting is near-instant, such as a web app.
For an App Store binary the post-merge half is weak, because a fix waits on review, so more of the evidence has to move before release and only server-side surfaces (flags, remote configuration, a proxied endpoint) keep a fast undo.

## Synthesis

A gate is a containment mechanism whose behavior needs evidence, not a certificate of safety.
Mandu's qualification: disabling a feature may stop future actions without undoing writes or external effects already performed, so recovery must be evaluated separately from the switch itself.
[[risk-based-agent-governance]] determines the depth of that evaluation, while [[agent-testing-instructions]] supplies observable proof.
For project tracking, record implementation, validation, and exposure as distinct facts rather than allowing “merged” to imply “launched.”

## Source

- [[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] - derived, undated tutorial; no universal rollout thresholds or readiness scoring model supplied.
- [[token-maxing-with-agents]] - Theo's pre-merge and post-merge framing and the 15-second revert heuristic; a rule of thumb, not a measured threshold.
