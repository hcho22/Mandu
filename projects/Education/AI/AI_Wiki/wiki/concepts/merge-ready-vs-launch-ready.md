---
type: concept
tags: [code-review, release, feature-flags, validation]
status: developing
source-count: 4
last-updated: 2026-10-14
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

## The last 20% (2026-10-14)

[[agentic-code-review-strategies]], a named summary of what is most likely the talk behind the first source, gives the split in the speaker's words: "Even if it's merge ready, I don't think it's launch ready."
[[john-meta-engineer]] calls the first phase "broad strokes": everything gated and landed, which leaves the feature about 80% done.
The last 20% is where most of his human effort goes:

- refactoring and cleaning up what the agents wrote;
- running a group of agents to audit the whole feature before launch for performance, bugs, security, and whether it works to spec;
- polish such as animations, which needs human taste.

By his estimate the last 20% takes as long as the first 80%.
Then he opens the gate to a canary or an A/B test even without statistical power, because a trickle of traffic surfaces crashes and alerts before everyone sees the feature.
The audit step is new to this page: review per PR checks each change, while a pre-launch audit checks the assembled feature, which no single PR review sees.

[[agentic-coding-workflow-idea-to-review]] turns the split into two gated phases: review ends with the PR merged and its gate off, and launch has its own exit gate (audit findings fixed or accepted, the canary clean for an agreed window, the gate fully open or the feature removed, and lessons added to `AGENTS.md` or a skill).
"Or the feature has been removed" is a useful addition: a launch phase that can end in deletion is one where merged code is not presumed to ship.

## Synthesis

A gate is a containment mechanism whose behavior needs evidence, not a certificate of safety.
Mandu's qualification: disabling a feature may stop future actions without undoing writes or external effects already performed, so recovery must be evaluated separately from the switch itself.
[[risk-based-agent-governance]] determines the depth of that evaluation, while [[agent-testing-instructions]] supplies observable proof.
For project tracking, record implementation, validation, and exposure as distinct facts rather than allowing “merged” to imply “launched.”

## Source

- [[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] - derived, undated tutorial; no universal rollout thresholds or readiness scoring model supplied.
- [[token-maxing-with-agents]] - Theo's pre-merge and post-merge framing and the 15-second revert heuristic; a rule of thumb, not a measured threshold.
- [[agentic-coding-workflow-idea-to-review]] - review and launch as separately gated phases; compiler-authored.
- [[agentic-code-review-strategies]] - John's "broad strokes" 80%, the agent audit and polish in the last 20%, and the canary; his estimate, not a measurement.
