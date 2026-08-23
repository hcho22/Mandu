---
type: concept
tags: [production-llm, feedback, data, moat]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Data Flywheel (Collecting User Feedback)

From [[llm-patterns]]: gather user feedback so the product's data compounds - feedback feeds evals, fine-tuning, and guardrails, and data is one of the few real moats for an LLM product.

## Key points

- **Explicit feedback** - the user acts on a request (thumbs up/down, regenerate, select attributes). Direct but sparse.
- **Implicit feedback** - learned from behavior without asking (Copilot: accept a suggestion = strong positive, tweak = positive, ignore = negative; chatbot stickiness and conversation length).
- **Make it easy and low-friction** (all three human-AI guideline sets agree), and prefer designs where feedback is a natural byproduct of use (Midjourney's upscale/vary/regenerate).
- The loop: usage -> data -> better model/evals -> better UX -> more usage. A virtuous cycle that also builds the moat.

## Synthesis

The data flywheel is the offensive, closest-to-the-user pattern of the [[production-llm]] area, and it closes the loop back to [[evals]]: the feedback you collect becomes the labeled data your eval set, judge calibration, and fine-tuning all need.
It reframes UX decisions as data-collection decisions - every interaction is a chance to capture a preference signal - which is the product-side complement to [[looking-at-your-data]].
For hcho's product bets it is the argument for instrumenting feedback from day one, so the eval harness has real labels to grow on rather than synthetic ones.
