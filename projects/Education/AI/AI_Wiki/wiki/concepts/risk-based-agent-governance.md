---
type: concept
tags: [agentic-engineering, risk, governance, review, production]
status: seed
source-count: 1
last-updated: 2026-09-16
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

## Synthesis

Proportionality directs scarce review attention toward incorrect or irreversible results that matter most.
This complements [[phased-autonomy]] and [[capabilities-not-instructions]] rather than replacing structural permission boundaries.
[[fresh-context-review]] and [[define-the-end-to-end-gate]] provide evidence; governance determines who may act on it.
The source's automatic-merge examples are context-specific, and its beginner recommendation favors human review of important applications.

## Source

- [[kun-agentic-app-development-workflow]] - secondary account of project policies plus compiler-authored beginner recommendations.
