---
type: concept
tags: [evals, testing, framework]
status: developing
source-count: 1
last-updated: 2026-07-08
---

# Three-Level Eval Framework

A model for structuring LLM evaluation into three ascending levels, introduced by [[hamel-husain]] in [[your-ai-product-needs-evals]].
Each level trades cost against fidelity, and you add higher levels only as the product matures.

## The three levels

| Level | What it is | Cost | When |
|---|---|---|---|
| L1 | [[llm-unit-tests]] - assertions run on every code change | Cheap, fast | From day one |
| L2 | Human and model eval - read traces, then [[llm-as-judge]] aligned to human labels | Moderate | As failures get subtle |
| L3 | A/B testing in production | Expensive, slow signal | Only near product-market fit |

## Key points

- L1 assertions are scoped per feature and scenario (e.g. "only one listing matches" implies `len(listing_array) == 1`), and test cases can be LLM-generated so you do not need production data to start.
- L2 begins with [[looking-at-your-data]] and binary good/bad labels, then automates with a model judge once the judge is aligned to human judgment.
- L3 mirrors ordinary product A/B testing and should be deferred until you are confident about PMF.

## Synthesis

The framework's value is that it sequences eval effort by product maturity, so a solo builder does not over-invest in A/B infrastructure before the basics exist.
For hcho, L1 and L2 are the immediately actionable layers, and they map cleanly onto a hardware-QA instinct: assert the cheap invariants first, then look hard at the actual outputs.
Expect later sources to extend this with RAG-specific evaluation and CI-gating patterns; link them here as they arrive.
