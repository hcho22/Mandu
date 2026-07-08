---
type: concept
tags: [evals, eval-design, llm-as-judge]
status: developing
source-count: 2
last-updated: 2026-07-08
---

# Pass/Fail Over Score-Based Evals

The eval-design guidance from [[ai-skill-from-scratch]]: prefer binary pass/fail checks over score-based ("rate this 1-5") evals when a model is the grader.

## Key points

- A model cannot reliably distinguish a 3/5 from a 4/5 or 5/5; it will invent the number, so score-based grades are noisy. ([[lets-talk-about-llm-evaluation]] confirms model judges are "bad at consistent score ranges.")
- If you must elicit a score, have the model **reason before scoring** - it measurably improves consistency ([[lets-talk-about-llm-evaluation]]).
- Pass/fail checks are concrete and repeatable, and they compose into a checklist the model can loop against (see [[skill-eval-loop]]).
- Group checks by category (e.g. intro, voice, substance, tone, call-to-action) so failures are actionable.

## Synthesis

This is a practical refinement of [[llm-as-judge]]: it says that when you must use a model to grade, constrain the judgment to binary decisions it can actually make.
It rhymes with Hamel Husain's caution in [[your-ai-product-needs-evals]] about naive agreement metrics - both are about not trusting a judge to do something it cannot reliably do - and the rigorous version of that caution lives in [[precision-recall]].
Expect deeper eval sources (the HuggingFace guidebook, "Evaluate AI Systems") to complicate this with cases where graded rubrics do add value; link them here.
