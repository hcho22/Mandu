---
type: concept
tags: [evals, reproducibility, benchmarks, rigor]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Score Reproducibility

From [[llm-evaluation-guidebook]]: you usually can't reproduce a model's reported benchmark score, because many small, easy-to-miss factors each move results by points.

## What moves a score

- **Code base** - the exact eval implementation (author code, `lm_eval`, `lighteval`); if not provided, precise reproduction is essentially impossible.
- **Metric definition** - "exact match" may secretly be prefix/suffix/quasi match, or log-likelihood vs generative; the name doesn't tell you.
- **Normalization** - stripping punctuation/spacing/case, or math-answer extraction, changes results a lot.
- **Prompt format** - semantically-equivalent formats (`A` vs `A.` vs `(A)`) swing scores up to ~7 points; models increasingly overfit specific benchmark prompt formats.
- **Chat template / system prompt** - not following the model's expected template kills performance; reasoning traces must be stripped.
- **Few-shot** - count, which examples, and their exact order all matter (order alone: ~3 points).
- **Loading** - hardware/GPU, inference library (transformers vs vLLM vs sglang), batch size, and precision/quantization all change numbers.

## Synthesis

This is the sharpest practical lesson in the [[evals]] area and a validation principle in pure form: **an unreproducible measurement is not a measurement.**
It generalizes [[benchmark-sensitivity]] (differences *across* benchmark implementations) into the full checklist for reproducing *any* reported number, and it is why [[eval-driven-development]] and pinned, version-controlled eval pipelines beat trusting a leaderboard figure.
For hcho it is a strong, credible interview stance ("I don't trust a score I can't reproduce end to end, and here are the eight things that break reproduction") - exactly the rigor AI-quality roles are hiring for.
