---
type: concept
tags: [evals, tooling, ci, observability]
date: 2026-06-06
source-count: 2
status: seeded
session: "S7 - Production tooling: Promptfoo, DeepEval, Phoenix"
---

# Production Eval Tooling

Running eval suites in CI and observability tools such as Promptfoo, DeepEval, and Arize Phoenix.

## From the sources

Chip Huyen, [[evaluate-ai-systems]], gives the generic evaluation-pipeline scaffold that production tooling should support:

- Evaluate the **end-to-end output** and each component's **intermediate output** independently. For multi-step systems, evaluate per component, per turn, and per task so failures can be localized instead of hidden in an aggregate score.
- Start with an evaluation guideline that defines what the application should and should not do. Ambiguous guidelines produce ambiguous scores.
- For each criterion, choose a scoring system and write a rubric with examples. Validate the rubric with humans before automating it; if humans cannot apply it consistently, the evaluation is not ready.
- Select methods by criterion: specialized toxicity classifiers for toxicity, semantic similarity for relevance, AI judges for factual consistency or subjective criteria, human evaluation where automation is not trustworthy, and cheap broad scorers plus expensive sampled judges when cost matters.
- Curate annotated data for every component and criterion. Use production data where possible, add out-of-scope examples, and slice the data so the system can be debugged by subgroup rather than only by aggregate performance.
- Measure whether the evaluation pipeline itself is reliable: do better responses get better scores, are runs reproducible, do metrics correlate with each other and with business outcomes, and how much cost or latency does evaluation add?
- Track all variables that can affect evaluation results, including evaluation data, rubrics, judge prompts, sampling settings, model versions, and pipeline changes.
- Production evaluation can include manual expert review on a daily sample of outputs. The chapter cites LinkedIn manually evaluating up to 500 daily conversations with AI systems.

Jonathan Chavez, [[what-is-a-contaminated-llm-detection-famous-cases-2026-guide]], adds requirements for tooling that manages benchmark and holdout trust:

- Evaluation tooling should track whether a test set is public, private, gated, post-cutoff, or rotating. That provenance affects how much the score should be trusted.
- For benchmark-style suites, tools should preserve private holdouts, version public releases, and avoid accidentally leaking answer keys or test examples into prompts, logs, fine-tuning data, or vendor training channels.
- Contamination checks can become pipeline checks: time-split reporting where timestamps exist, duplicate or near-duplicate search where corpora are available, membership-inference/perplexity-style checks where logprobs are available, and rephrased/reference-sample comparisons where matched data exists.
- The article reinforces that application evals are part of production tooling, not just research benchmarking: teams should measure on their own codebase, tone, edge cases, and user data because benchmark contamination cannot answer those product-specific questions.

## In my own words (hcho)
