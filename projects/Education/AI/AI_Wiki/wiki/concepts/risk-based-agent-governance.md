---
type: concept
tags: [agentic-engineering, risk, governance, review, production]
status: developing
source-count: 2
last-updated: 2026-09-23
---

# Risk-Based Agent Governance

Choose independent verification and human authority from a change's consequences and reversibility.
[[kun-agentic-app-development-workflow]] describes different project policies and offers a beginner adaptation that favors stronger review for important applications.
Its categories are a decision aid, not an industry standard or proof that automated approval is safe.

## Key points

- Reversible experiments can use a smaller validation process while retaining an observable result.
- Customer-facing behavior needs real user-journey evidence and relevant failure cases.
- Authentication, payments, permissions, secrets, destructive migrations, and customer data need explicit architecture, security, and recovery scrutiny.
- Worktree isolation limits collisions; it does not establish deployment or merge authority.
- Agent tests and fresh-context review inform a decision rather than granting production access.
- Explain risk and remaining uncertainty in the PR so reviewers can assess the actual change.

## Trunk, leaves, and release risk (2026-09-23)

[[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] makes the triage concrete: trace dependencies and side effects before treating a change as an isolated leaf.
Shared state, networking, permissions, and existing production behavior deserve closer review even when the diff is short.
Feature gates reduce exposure only when they cover relevant integration points and the disabled path has been tested.
[[merge-ready-vs-launch-ready]] separates integration evidence from the decision to expose users.
This is additional secondary guidance, not a validated risk score or proof that a gate makes a change safe.

## Synthesis

Proportionality directs scarce review attention toward incorrect or irreversible results that matter most.
This complements [[phased-autonomy]] and [[capabilities-not-instructions]] rather than replacing structural permission boundaries.
[[fresh-context-review]] and [[define-the-end-to-end-gate]] provide evidence; governance determines who may act on it.
The source's automatic-merge examples are context-specific, and its beginner recommendation favors human review of important applications.

## Source

- [[kun-agentic-app-development-workflow]] - secondary account of project policies plus compiler-authored beginner recommendations.
- [[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] - unidentified speaker's review workflow, reconstructed as a beginner guide.
