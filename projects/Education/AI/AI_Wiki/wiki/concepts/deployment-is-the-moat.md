---
type: concept
tags: [ai-career, strategy, deployment, positioning]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# Deployment Is the Moat

**"The edge is no longer who has the intelligence. It's where, how, and why they use it."**

From [[fde-in-30-days]].
Frontier models release constantly and the same foundational capability is available to any company that can pay for it.
Across ~50 enterprise clients Vas observes the same stack repeatedly: [[claude-code]], Cursor, GitHub Copilot.

Because everyone has access to the same intelligence, **intelligence itself is no longer the moat**.

## What's left to be good at

- Bridging general-purpose AI capability with a **specific company's** unique processes, systems, and context.
- Every business runs differently even for the "same" function - accounts payable can be a 10-step or a 30-step process depending on the company.
- Knowing where AI **doesn't** belong.
Early in the wave teams over-applied AI to everything, producing token maxing and hallucinations.
Cited: **95% of generative AI pilots fail** (an MIT figure as referenced by Vas, reported rather than verified here).

## Synthesis

This is the wiki's cleanest statement of *why the AI-engineer job exists at all*, and it makes several existing pages rhyme.

[[ai-engineer-is-a-builder]] says the role builds on existing models rather than training them, and doesn't need a PhD.
This explains why that's true: if the models are a commodity, the value is entirely in application, and application is not a research skill.
[[taste-as-moat]] says encoded judgment is the durable value as production gets cheap - the same argument one layer up.
[[switchers-edge]] says the bar moved from credential to owned-outcome judgment; commoditized intelligence is the mechanism that moved it.

The strategic reading for hcho cuts two ways and both are worth holding.

**Favorable:** it validates the pivot's core premise.
If the moat is deployment judgment rather than ML depth, then a decade of understanding how real systems fail in real operational contexts is an asset, and the missing piece was only ever the AI-native execution layer - which is what the last year of building has been.

**Unfavorable:** it applies to the product bet too.
The Agentic RAG starter kit is not defensible because of its retrieval quality, since anyone can buy the same models.
It is defensible to the extent it encodes **deployment knowledge** - permissions, RLS, escalation, the eval harness, the things that make a RAG system survive contact with a real org.
That is worth stating explicitly, because it means the validation-first strategy and the productization strategy are the same strategy: the buyer interviews are how you learn the deployment knowledge that *is* the product.
