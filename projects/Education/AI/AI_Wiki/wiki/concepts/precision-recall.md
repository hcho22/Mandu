---
type: concept
tags: [ml-metrics, classification, precision, recall, evaluation]
status: developing
source-count: 1
last-updated: 2026-07-08
---

# Precision and Recall

The two error-aware classification metrics, introduced in the wiki via [[classification-roc-and-auc]] and referenced by several eval sources.

## Definitions

- **Precision** = of the examples the model flagged positive, how many really are positive (TP / (TP + FP)). Penalizes false positives.
- **Recall** (TPR) = of the actually positive examples, how many the model caught (TP / (TP + FN)). Penalizes false negatives.
- A **precision-recall (PR) curve** plots precision vs recall across thresholds and is a better comparison than [[roc-and-auc|ROC/AUC]] when classes are imbalanced.

## Why it recurs in evals

- [[llm-as-judge]]: use precision and recall separately, not raw agreement, when validating a model judge on imbalanced data - the exact reason PR curves beat AUC on imbalance.
- [[pass-fail-over-score-evals]]: the same "don't trust a single aggregate number" instinct.

## Synthesis

Precision vs recall is the metric-level statement of a value judgment: which error hurts more.
That makes it the quantitative twin of [[classification-threshold]] and [[cost-of-being-wrong]], and the rigorous vocabulary hcho should reach for when talking evals in interviews - it is exactly the validation precision his background implies.
