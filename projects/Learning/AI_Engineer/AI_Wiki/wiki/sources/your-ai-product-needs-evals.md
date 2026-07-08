---
type: source
title: "Your AI Product Needs Evals"
source-type: blog
author: "Hamel Husain"
url: "https://hamel.dev/blog/posts/evals/"
date-ingested: 2026-07-08
date-created: 2024-03-29
tags: [evals, llm, testing, llm-as-judge, fine-tuning]
---

# Your AI Product Needs Evals

A foundational blog post by [[hamel-husain]] arguing that the difference between an AI product that keeps improving and one stuck at the demo stage is a systematic **evaluation system**.
Drawing on five years building LLM products (starting with CodeSearchNet at GitHub) and consulting work on domain-specific AI, Husain lays out a three-level eval framework and shows how a good eval system pays for itself by doubling as debugging and fine-tuning infrastructure.
The running case study is Lucy, Rechat's real-estate AI assistant, whose prompt-only development plateaued into whack-a-mole failures until evals were introduced.

## Key claims

- Iteration speed is the driver of AI-product success, and it depends on three activities: evaluating quality via tests, debugging via logging and data inspection, and modifying behavior via prompts/fine-tuning/code. Most teams do only the third, which caps them at demo quality.
- Evaluation should be structured in three levels (the [[three-level-eval-framework]]): L1 unit tests, L2 human and model eval, L3 A/B testing.
- **L1 - [[llm-unit-tests]]:** cheap, fast assertions run on every code change; scope them per feature and scenario; generate test cases with LLMs; run them in existing CI (GitHub Actions) and track pass rates over time. You do not need production data to start.
- **L2 - human and model eval:** log traces, then remove all friction from [[looking-at-your-data]]; build a domain-specific trace viewer in a day (Gradio/Streamlit/Shiny); start with binary good/bad labels. Automate with [[llm-as-judge]] but keep humans in the loop and track judge-vs-human alignment.
- **L3 - A/B testing:** resembles ordinary product A/B testing; defer it until you have confidence about product-market fit.
- Do not use raw agreement to measure judge-human alignment on imbalanced datasets; use precision and recall separately.
- A solid eval system unlocks fine-tuning (99% of fine-tuning work is assembling high-quality data, which the eval system's synthesis and curation produces) and debugging (traces, assertion flags, root-cause navigation overlap heavily with eval infrastructure).
- Build problem-specific eval systems, not generic frameworks; keep it simple and avoid expensive tooling early.

## Connections

- [[evals]] - this is the founding source for the evals area hub.
- [[three-level-eval-framework]] - the post's central model.
- [[llm-unit-tests]] - Level 1.
- [[llm-as-judge]] - the Level 2 automated-eval technique, plus the agreement/precision-recall caveat.
- [[looking-at-your-data]] - the "remove all friction from data inspection" principle that recurs across the eval literature.
- [[hamel-husain]] - author.
- Cross-wiki: hcho's own eval synthesis lives in the evals pilot wiki (`projects/Learning/AI_Engineer/evals/`, split mode); this page is the broad reference layer.

## Source

- **Author:** Hamel Husain
- **Title:** Your AI Product Needs Evals
- **URL:** https://hamel.dev/blog/posts/evals/
- **Published:** 2024-03-29 (adapted from a Vanishing Gradients podcast; reviewers included Jeremy Howard, Eugene Yan, Shreya Shankar)
- **Raw:** [[your-ai-product-needs-evals]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
