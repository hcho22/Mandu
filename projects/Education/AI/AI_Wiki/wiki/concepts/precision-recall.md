---
type: concept
tags: [ml-metrics, classification, precision, recall, evaluation]
status: established
source-count: 3
last-updated: 2026-09-15
---

# Precision and Recall

The two error-aware classification metrics, introduced in the wiki via [[classification-roc-and-auc]] and referenced by several eval sources.

## Definitions

- **Accuracy** = (TP + TN) / total and is only a useful coarse measure when the classes are balanced.
- **Precision** = of the examples the model flagged positive, how many really are positive (TP / (TP + FP)). Penalizes false positives.
- **Recall** (TPR) = of the actually positive examples, how many the model caught (TP / (TP + FN)). Penalizes false negatives.
- **F1** = 2PR / (P + R), the harmonic mean that tracks the weaker of precision and recall and is more informative than accuracy on imbalanced data.
- A **precision-recall (PR) curve** plots precision vs recall across thresholds and is a better comparison than [[roc-and-auc|ROC/AUC]] when classes are imbalanced.

## Why it recurs in evals

- [[llm-as-judge]]: use precision and recall separately, not raw agreement, when validating a model judge on imbalanced data - the exact reason PR curves beat AUC on imbalance.
- [[pass-fail-over-score-evals]]: the same "don't trust a single aggregate number" instinct.
- [[ai-evals-error-analysis]]: automated eval tools with high recall can still damage a product when 10-20% of their flagged errors are false positives, so a human-labeled set must measure the rubric itself.

## Synthesis

Precision vs recall is the metric-level statement of a value judgment: which error hurts more.
That makes it the quantitative twin of [[classification-threshold]] and [[cost-of-being-wrong]], and the rigorous vocabulary hcho should reach for when talking evals in interviews - it is exactly the validation precision his background implies.
