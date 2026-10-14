---
type: concept
tags: [feature-flags, code-review, release, risk, planning]
status: developing
source-count: 4
last-updated: 2026-10-14
---

# Feature Gating from Day One

Put every new feature behind a switch while planning it, not at review time, because the ability to turn a change off is what makes lighter review of it safe.
From [[agentic-code-review-strategies]], where [[john-meta-engineer]] calls rollback the question that decides how much code he reads.

## Key points

- **Feature gating** (also called feature toggling or feature flagging) is branching logic that turns a feature on or off without a new deploy.
- **Start with a plain Boolean flag.** Proper flag infrastructure (LaunchDarkly is his example) can come later; waiting for it is not a reason to ship ungated.
- **Gate everything in broad strokes, and gate the seams specifically.** Separate leaf work that does not touch existing code from integration work, and give each integration layer its own gate, because that is where a change reaches production behavior.
- **Gating comes before coding.** He starts implementation only once the plan, roadmap, and gates exist, then has agents make atomic changes.
- **The payoff is at review and launch.** A confident "yes, I can roll it back" is what licenses a skim of a leaf change ([[risk-based-agent-governance]]), and the same gate later carries a canary or A/B rollout ([[merge-ready-vs-launch-ready]]).

## Earlier, unattributed account (2026-09-23)

[[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]], most likely derived from the same talk, adds two checks: gates should cover background effects as well as integration points, and both states of the gate need testing, including that switching it off restores the control experience.

## A fast undo is the precondition (2026-10-02)

[[token-maxing-with-agents]] states the same dependency as a rule of thumb: if undoing a bad change takes more than 15 seconds, fix the systems before working this way.
A gate is one way to get that 15-second undo without a redeploy.

## The gate as a lifecycle (2026-10-14)

[[agentic-coding-workflow-idea-to-review]] gives the gate a place in every phase: a flag mechanism in the first setup ("a Boolean flag in config is enough"), a gating plan in the contract that names the flag for each feature and gives each integration seam its own, a gate field on every task card, merge **with the gate off**, and opening it to a canary only after a pre-launch audit.
Its review checklist asks the question that makes a gate real: does it exist, default to off, and restore the control experience when switched off?
The phase placement is the compiler's; the rules come from John.

## Synthesis

The idea moves a review decision into planning.
Deciding where the gates go is deciding, in advance, which future changes can be skimmed.
That makes gating a validation design activity, the same move as defining the pass criterion before the test.

Mandu's qualification, carried over from [[merge-ready-vs-launch-ready]]: a gate stops future behavior but does not undo writes, migrations, or messages already sent.
"Can I roll it back?" therefore has two halves, switching the code path off and recovering the state it changed, and only the first comes free with a flag.
A change whose effects outlive the switch is still a one-way door and still earns the deep read.

For a compiled mobile app the gate's reach is narrower than on the web.
Only server-side switches (remote configuration, a proxied endpoint) act without a new App Store review, so a client-only Boolean is a gate for development and testing, not for a fast undo in production.

## Source

- [[agentic-code-review-strategies]] - John's "gate everything" rule, the Boolean starting point, and integration-layer gates.
- [[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] - probable derivation of the same talk; adds both-states testing and background effects.
- [[agentic-coding-workflow-idea-to-review]] - the gate placed in every phase of a merged playbook; compiler-authored structure.
- [[token-maxing-with-agents]] - Theo's 15-second revert rule; a heuristic, not a measured threshold.
