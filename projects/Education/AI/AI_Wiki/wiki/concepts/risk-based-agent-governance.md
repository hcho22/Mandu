---
type: concept
tags: [agentic-engineering, risk, governance, review, production]
status: developing
source-count: 6
last-updated: 2026-10-14
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

## Operational separation in service work (2026-09-29)

[[projects/Education/Business/wiki/sources/ai-rollup-solo-founder-guide|The $5 Trillion AI Rollup Opportunity]] applies the same governance principle to recurring service work.
It separates intake, preparation, review, and human approval, and says preparation and review agents should not send client-facing work.
Each automated role should declare permitted actions, forbidden actions, required inputs, stop conditions, and escalation paths.
That separation is a structural control: a useful draft cannot silently become an authorized external action.

The guide's business results and market claims are unverified, but its permission boundaries are consistent with this page's consequence-based approach.

## Merge authority written into the prompt (2026-10-02)

[[token-maxing-with-agents]] grants merge authority per task: the prompt states the conditions under which the agent may merge, and trusted threads merge without a human reading them.
That is governance by instruction rather than by structural boundary, which [[capabilities-not-instructions]] warns against for anything consequential.
The earlier [[working-with-fable-5]] run was safer in exactly this respect, because merges deployed only to staging.
Prompt-stated merge conditions fit reversible, low-blast-radius changes; consequential ones still need a boundary the agent cannot talk its way past.

## The named speaker's procedure (2026-10-14)

[[agentic-code-review-strategies]] is a named summary of what is most likely the same talk as the 2026-09-23 guide, by [[john-meta-engineer]], so it sharpens that section rather than corroborating it independently.
It supplies the procedure in his own order:

1. **Tag the change twice:** trunk or leaf, and reversible or one-way door.
2. **Ask three safety questions:** what control experience must not change, how bad it would be if this went wrong, and can it be rolled back.
3. **Turn the review-depth knob:** up for trunk code, infrastructure, many dependents, and one-way doors; down for gated leaf work that carries proof ([[proof-in-the-pr]]).

Rollback is the hinge, which is why gating is decided while planning ([[feature-gating-from-day-one]]).
His last tip is that knowing your own codebase's architecture is what makes this fast: you can see at a glance what touches the dangerous zones.
He reports reading more code than before under this regime, which is a reminder that proportional review is a reallocation of attention, not a reduction of it.

## Tiers assigned before the code exists (2026-10-14)

[[agentic-coding-workflow-idea-to-review]] merges John's blast radius with Kun's per-project policies into an editor-authored three-tier table, assigned while planning rather than at review:

| Tier | Typical areas | Rollback | Human review |
|---|---|---|---|
| Low | Leaf UI, gated experiments, internal tools, docs | Flag off or revert | AI review and a skim |
| Medium | Customer-facing features, important data flows, auth-adjacent UI | Flag off | AI review; a human reads every file touching a contract or shared code |
| High | Auth, payments, permissions, migrations, secrets, infrastructure, shared state, one-way doors | May be impossible | Security review, every line read, a rollback plan |

Two rules make the table hold up in practice.
The tier is **confirmed or raised at review**: a task planned as a leaf that ends up editing a shared reducer is trunk, whatever the task card said.
And the one-way-door question is made concrete: a data migration, a deletion, a public API change, or an external send.
The table is a compiler's teaching aid built on secondary sources, not a validated standard; its value is that it forces the tier decision before the diff exists.

## Synthesis

Proportionality directs scarce review attention toward incorrect or irreversible results that matter most.
This complements [[phased-autonomy]] and [[capabilities-not-instructions]] rather than replacing structural permission boundaries.
[[fresh-context-review]] and [[define-the-end-to-end-gate]] provide evidence; governance determines who may act on it.
The source's automatic-merge examples are context-specific, and its beginner recommendation favors human review of important applications.

## Source

- [[kun-agentic-app-development-workflow]] - secondary account of project policies plus compiler-authored beginner recommendations.
- [[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] - unidentified speaker's review workflow, reconstructed as a beginner guide.
- [[projects/Education/Business/wiki/sources/ai-rollup-solo-founder-guide|The $5 Trillion AI Rollup Opportunity]] - unidentified source's service-business workflow and human-approval guidance.
- [[token-maxing-with-agents]] - Theo's prompt-stated merge conditions; one practitioner's practice.
- [[agentic-coding-workflow-idea-to-review]] - compiler's three-tier table and re-triage rule; third-order material.
- [[agentic-code-review-strategies]] - John's named account of the trunk/leaf procedure; probably the same talk as the 2026-09-23 guide, so one voice rather than two.
