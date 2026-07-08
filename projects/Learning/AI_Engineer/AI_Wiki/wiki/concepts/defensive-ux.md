---
type: concept
tags: [production-llm, ux, design, trust, human-ai]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Defensive UX

From [[llm-patterns]]: a design strategy that assumes the model will sometimes be wrong (inaccuracies, hallucinations, varying output) and builds the interface to anticipate, guide, and handle that gracefully.

## The patterns (from Microsoft/Google/Apple human-AI guidelines)

- **Set the right expectations** - a disclaimer or landing-page note about what the AI can and cannot do; short-term trust dip, long-term trust gain.
- **Enable efficient dismissal** - make it easy to ignore/dismiss AI suggestions (Copilot: keep typing to skip a suggestion).
- **Provide attribution** - citations and sources (BingChat), social proof, "because you read..." - lets users appraise and calibrate trust.
- **Anchor on familiarity** - introduce AI features through familiar UI; resist exotic "magical" elements. Note: chat is high-effort and raises expectations, so it is often the wrong default UX.

## Synthesis

Defensive UX is the user-facing member of the [[production-llm]] area and the design twin of [[guardrails]]: guardrails keep bad output from leaving the system; defensive UX manages the reality that some imperfect output still reaches the user.
It is a direct application of the [[cost-of-being-wrong]] lens to the interface - the higher the cost of a wrong answer, the more the UI must expose uncertainty, attribution, and easy correction.
The attribution pattern also connects to [[retrieval-is-the-bottleneck]] and grounded [[retrieval-augmented-generation|RAG]]: citations are simultaneously a trust feature and a debugging aid.
