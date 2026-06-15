---
type: source
tags: [evals, benchmarks, llm-as-judge, metrics, contamination, statistics, fundamentals]
date: 2026-06-15
title: "The LLM Evaluation Guidebook"
author: "Clémentine Fourrier, Thibaud Frere, Guilherme Penedo, Thomas Wolf (Hugging Face / OpenEvals)"
url: "https://huggingface.co/spaces/OpenEvals/evaluation-guidebook"
concepts: [offline-vs-online-evals, classification-metrics, data-leakage-and-splits, llm-benchmarks-contamination, llm-as-judge, rag-evaluation, production-eval-tooling, hallucination-safety-redteam, agent-eval-and-stats, ci-eval-gates-and-drift]
---

# The LLM Evaluation Guidebook

A comprehensive, practitioner-facing guide to LLM evaluation distilled from the Hugging Face OpenEvals team's experience scoring ~15,000 models over three years (Open LLM Leaderboard 1 and 2, GAIA). Published December 2025. It walks the full arc: why people evaluate (model-builder vs model-user perspectives), the LLM mechanics that affect scores (tokenization, inference, log-likelihood vs generative evaluation), how to use existing benchmarks (the 2025 landscape by capability, plus saturation and contamination), how to select benchmarks that give reliable training signal, how to build your own evaluation (datasets, prompts, contamination management), and the hard problem of scoring free-form text (automatic metrics, human evaluation, LLM-as-judge, reward models), closing with the "forgotten children" of evaluation: statistical validity and cost. The guidebook is opinionated toward interpretable, functional, contamination-resistant evaluation over model judges.

## Key claims

- Evaluation is a proxy: a high benchmark score measures "best on these samples for this task that we hope proxy a capability," not the capability itself. Every method (automatic metrics, human judges, model judges) carries its own biases and tradeoffs.
- **Saturation** (models cluster near the ceiling, losing discriminative power) and **contamination** (eval data leaks into training, inflating scores) are distinct failure modes; a contaminated benchmark can still give useful training signal even when it is useless for final comparison.
- Two inference methods structure benchmark evaluation: **log-likelihood** (score candidate-answer probabilities; fast, good for multiple-choice and small-model signal) and **generative** (let the model produce text; the only option for closed APIs, and what most 2025 evals use). Three task formulations trade signal for difficulty: MCF, CF, FG.
- The 2025 benchmark landscape spans reasoning/commonsense, knowledge (MMLU-Pro, GPQA, HLE), math (AIME, MATH-500, FrontierMath), code (LiveCodeBench, SWE-Bench), long context (RULER, HELMET), instruction following (IFEval/IFBench), tool-calling (TauBench, BFCL, MCP-Universe), integrated assistant tasks (GAIA2, DABStep), games, and forecasters. The field is moving from isolated skills toward capability orchestration.
- Reproducing reported scores to the decimal is extremely hard: prompt format (semantically-equivalent variants swing scores up to ~7 points), chat templates, few-shot count/order, normalization, code base, hardware, inference library, batch size, precision, and random seed all move results.
- The FineWeb team's four criteria for a benchmark that gives signal during pre-training: monotonicity (Spearman ≥ 0.5), low noise (SNR > 20), non-random performance (≥ 3 std above baseline), and model-ordering consistency (Kendall's tau).
- Scoring free-form text is the central challenge. Automatic match-based metrics (exact match, BLEU, ROUGE, TER, BLEURT) are cheap and reproducible but break on open-ended tasks; accuracy needs length/PMI normalization; sampling metrics (pass@k, maj@n, cot@n, avg@n) trade cost for robustness; **functional scorers** (verifiable constraints, IFEval-style) are the authors' preferred approach.
- LLM-as-judge is powerful but tricky: seven catalogued biases (no internal consistency, inconsistent score ranges, self-preference, blindness to input perturbation, position, verbosity, format). Pairwise comparison beats absolute scoring; emit reasoning before the score; use a jury; and always evaluate your evaluator against a small high-quality baseline before trusting it. Judges are weak hallucination detectors.
- Reward models (Bradley-Terry pairwise) are a fast, deterministic, position-bias-resistant alternative judge; use win rates / win probabilities (not raw averages) for relative-score models, and track win-rate over training to detect degradation and select checkpoints.
- Always report confidence intervals (standard deviations or bootstrapping) and cost/efficiency (output tokens, monetary cost, time, environmental footprint). An LLM judge can cost ~100x an automatic metric for better signal that is not always justified.

## Connections

- [[offline-vs-online-evals]] - model-builder vs model-user perspectives; log-likelihood vs generative methods; MCF/CF/FG formulations.
- [[llm-benchmarks-contamination]] - the 2025 benchmark tour by capability; saturation vs contamination; the move to integrated assistant tasks.
- [[classification-metrics]] - automatic scoring metrics (exact match, BLEU/ROUGE/TER/BLEURT), aggregation (P/R/F1/MCC), accuracy normalization, sampling metrics, functional scorers.
- [[llm-as-judge]] - judge definition and uses, getting a judge, the seven biases and mitigations, evaluating your evaluator, reward models.
- [[data-leakage-and-splits]] - managing contamination when building an eval: canary strings, gating, procedural generation, overfitting vs generalization.
- [[agent-eval-and-stats]] - tool-calling/agent benchmarks (TauBench, BFCL, MCP-Universe) and statistical validity (confidence intervals, bootstrapping).
- [[ci-eval-gates-and-drift]] - ablations and checkpoint evals; the FineWeb benchmark-selection criteria; reward-model checkpoint selection.
- [[production-eval-tooling]] - standard harnesses (lm_eval, lighteval), reproducibility factors, structured generation (outlines), annotation tooling (Argilla, distilabel), cost reporting.
- [[rag-evaluation]] - long-context benchmark lineage (NIAH, RULER, HELMET and its RAG/QA datasets); closed-book to open-book shift.
- [[hallucination-safety-redteam]] - non-compliance (CoCoNot), judges as weak hallucination detectors, calibration, games as safety probes, human-eval biases.
- Same author's earlier blog [[lets-talk-about-llm-evaluation]] is the short precursor to this full guidebook; cross-references Eugene Yan's LLM-evaluators writing referenced in [[patterns-for-building-llm-based-systems-and-products]].

## Source

- **Author:** Clémentine Fourrier, Thibaud Frere, Guilherme Penedo, Thomas Wolf (Hugging Face / OpenEvals)
- **Title:** The LLM Evaluation Guidebook
- **URL:** https://huggingface.co/spaces/OpenEvals/evaluation-guidebook
- **Raw:** [[Evaluation Guidebook - a Hugging Face Space by OpenEvals]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-06-15
