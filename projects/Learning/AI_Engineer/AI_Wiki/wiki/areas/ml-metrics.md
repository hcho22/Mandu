---
type: area
tags: [ml-metrics, classification, evaluation, ml-fundamentals]
status: developing
source-count: 1
last-updated: 2026-07-08
---

# ML Metrics

The durable hub for classical machine-learning evaluation metrics: how you measure whether a model's predictions are any good, and how you choose an operating point.
These are the foundations underneath the newer [[evals]] discipline - LLM and agent evaluations still rest on precision, recall, thresholds, and ranking quality.

## Why it matters here

hcho's edge is validation, and validation runs on metrics.
This area gives the wiki the rigorous vocabulary (TPR/FPR, precision/recall, AUC, thresholds) that the LLM-eval sources gesture at but rarely define, so claims like "use precision and recall, not raw agreement" have a precise home.

## Concepts in this area

- [[roc-and-auc]] - performance across all thresholds; AUC as ranking probability.
- [[precision-recall]] - precision, recall, and PR curves for imbalanced data.
- [[classification-threshold]] - choosing an operating point by the cost of false positives vs false negatives.

## Sources

- [[classification-roc-and-auc]] - Google ML Crash Course on ROC and AUC.

## Synthesis

One source in, the throughline is that a single-threshold metric (accuracy) hides a model's real behavior, so you evaluate across thresholds (ROC/AUC) and pick an operating point by cost.
This connects straight to the wiki's spine: [[classification-threshold]] is the quantitative form of [[cost-of-being-wrong]], and [[precision-recall]] is the rigor behind the eval caveats in [[llm-as-judge]] and [[pass-fail-over-score-evals]].
Expect the deeper evals sources (Evaluate AI Systems, the HuggingFace guidebook) and the LLM-contamination source to extend this area toward model-quality and leakage metrics.
