---
type: source
tags: [evals, unit-tests, llm-as-judge, traces, fine-tuning]
date: 2026-06-06
title: "Your AI Product Needs Evals"
author: "Hamel Husain"
url: "https://hamel.dev/blog/posts/evals/"
concepts: [offline-vs-online-evals, llm-as-judge]
---

# Your AI Product Needs Evals

Hamel Husain argues that what separates an LLM product that keeps improving from one stuck at demo quality is a systematic evaluation system that lets the team iterate quickly. He lays out a three-level eval framework (unit-test assertions; human plus model-graded eval over logged traces; A/B testing) drawn from building Rechat's real-estate assistant "Lucy," and shows the same eval infrastructure also powers fine-tuning data curation and debugging.

## Key claims

- Iteration speed drives AI-product success; it rests on three activities: evaluating quality via tests, debugging via logging/data inspection, and changing behavior (prompts, fine-tuning, code). Teams that only do the third never get past a demo.
- **Level 1 (unit tests):** fast, cheap assertions on scoped features and scenarios, run in CI on every change; generate test cases with an LLM; track pass rates over time. You do not need production data to start.
- **Level 2 (human & model eval):** log and review traces with all friction removed (build domain-specific viewers); start with binary good/bad labels; add an LLM judge but keep humans in the loop and align the judge to human labels.
- **Level 3 (A/B testing):** validate on live traffic; defer until product-market fit is clearer.
- For the judge: use the most capable affordable model, keep a mini-eval for the judge itself, and monitor model-human agreement.
- Do not use raw agreement on imbalanced data; report precision and recall separately.
- A good eval system unlocks fine-tuning (synthetic data generation and curation) and debugging (searchable, assertion-flagged trace logs) almost for free.

## Connections

- [[offline-vs-online-evals]] - the three-level framework is the offline-to-online progression: Level 1 (offline CI assertions) and Level 2 (offline and sampled human + model eval) come before Level 3 (online A/B testing).
- [[llm-as-judge]] - Level 2's "automated evaluation w/ LLMs": align the judge to human labels, pick a capable affordable judge model, run a mini-eval on the judge, and avoid raw-agreement metrics on imbalanced data.

## Source

- **Author:** Hamel Husain
- **Title:** Your AI Product Needs Evals
- **URL:** https://hamel.dev/blog/posts/evals/
- **Published:** 2024-03-29
- **Raw:** `raw/your-ai-product-needs-evals.md` (clipped markdown copy, immutable)
- **Ingested:** 2026-06-06
