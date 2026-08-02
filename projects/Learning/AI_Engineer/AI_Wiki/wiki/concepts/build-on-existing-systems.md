---
type: concept
tags: [ai-career, fde, deployment, enterprise, integration]
status: seed
source-count: 1
last-updated: 2026-08-01
---

# Build On Existing Systems, Never Force a Migration

The deployment constraint from [[fde-in-30-days]], and the one Vas states most bluntly.

**The example:** a client spent multiple years and several million dollars migrating to **NetSuite**.
Telling that client they now need to move *off* NetSuite for an AI solution would fail immediately - "they're going to tell you to get lost."

Instead, build on top of and integrate with what they already run: NetSuite, Salesforce, SAP, Concur, Expensify, Gong, Workday.

## Why it's non-negotiable

- The existing system represents **sunk cost, political capital, and somebody's career**. Proposing to replace it is proposing that a past decision was wrong, and you are asking the person who made it to agree.
- Migration risk is the client's, not yours, which makes the pitch asymmetric.
- It stacks with the de-risking problem: bringing in an FDE is *already* perceived as risk, so the engagement has to reduce risk, not add the largest available one.
- The alternative framing offered in the conversation: pitch improvements to the existing stack - efficiency, faster customer reach, revenue growth - rather than disruptive replacement.

## The rollout that follows

Gradual, in stages: **sandbox/controlled testing → shadow mode → increasing autonomy → full production.**
Meeting clients in person makes this journey easier to walk them through than being "a guy behind a computer screen" flipping a switch.

## Synthesis

The strategic point is that **the integration surface is the product**, not an implementation detail of it.
An AI system that requires you to replace the system of record is not a product an enterprise can buy, regardless of how good it is.

This is the enterprise-sales form of a constraint the wiki already holds technically.
[[agent-readable-website]] and [[agent-building-blocks]] argue that agents need existing systems to expose docs, schemas, and endpoints; this argues the same thing from the buyer's side - the agent has to meet the stack where it is.

The staged rollout is also **[[phased-autonomy]] sold to a client** rather than practiced privately.
That is a genuinely useful reframe: shadow mode isn't only an engineering safety practice, it is the mechanism by which a client's trust is earned incrementally, and it is what makes the [[audit-eval-deployment]] eval report worth producing.

For hcho this is a design constraint on the Agentic RAG starter kit, and a sharper one than it first appears.
A permission-aware RAG product's whole value proposition is respecting an org's *existing* identity and access model - Okta, Google Workspace, whatever the customer already has - rather than asking them to re-model permissions in a new system.
"Bring your own auth and your own document store" is not a feature request to defer; per this source it is the difference between a product and a demo.
