---
type: source
tags: [evals, metrics, classification, precision, recall, f1, class-imbalance]
date: 2026-06-08
title: "Classification: Accuracy, recall, precision, and related metrics"
author: "Google Machine Learning Crash Course"
url: "https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall"
concepts: [classification-metrics]
---

# Classification: Accuracy, recall, precision, and related metrics

A Google Machine Learning Crash Course page that defines the core single-threshold classification metrics derived from the confusion matrix (accuracy, recall/TPR, false positive rate, precision, F1) and gives guidance on which to optimize based on class balance and the relative cost of false positives versus false negatives. The recurring theme is that accuracy is misleading on imbalanced data, so metric choice should follow the cost of each error type.

## Key claims

- All metrics here are computed at a **single fixed classification threshold** and change as the threshold changes; tuning the threshold trades these metrics off against each other.
- **Accuracy** = (TP + TN) / (TP + TN + FP + FN): the fraction of all classifications that are correct. A coarse, useful measure only on **balanced** datasets. On imbalanced data it is misleading - a model that always predicts the majority class scores 99% accuracy on a 1%-positive dataset while being useless.
- **Recall** (= **true positive rate**, = "probability of detection") = TP / (TP + FN): the fraction of actual positives correctly caught. The metric to prioritize when **false negatives are costly** (e.g. disease detection).
- **False positive rate (FPR)** (= "probability of false alarm") = FP / (FP + TN): the fraction of actual negatives wrongly flagged. Can be **volatile** when actual negatives are few (one flip swings it widely).
- **Precision** = TP / (TP + FP): the fraction of positive predictions that are actually positive. The metric to prioritize when **false positives are costly**. Less meaningful when actual positives are extremely rare.
- **Precision-recall tradeoff:** raising the threshold reduces false positives (raises precision) but increases false negatives (lowers recall), so precision and recall usually move inversely.
- **F1 score** = harmonic mean of precision and recall = 2 * (P * R) / (P + R) = 2TP / (2TP + FP + FN): balances the two and is preferable to accuracy on imbalanced data. When precision and recall diverge, F1 tracks the worse of the two.
- **Metric choice is cost-driven:** recall when false negatives hurt most, precision or FPR when false positives hurt most, accuracy only as a rough progress indicator on balanced data.
- **NaN** arises from division by zero (e.g. precision when TP = FP = 0, as when a model never predicts positive); it can signal either a degenerate or a trivially-perfect case and must be read in context.

## Connections

- [[classification-metrics]] - this is the foundational definition source for the S2 page: the confusion-matrix metrics (accuracy, recall/TPR, FPR, precision, F1), the precision-recall tradeoff, and the class-imbalance failure of accuracy. Grounds the LLM-specific guidance (use precision/recall, not raw accuracy, on imbalanced data) that [[llm-as-judge]] and [[patterns-for-building-llm-based-systems-and-products]] state without deriving.

## Source

- **Author:** Google Machine Learning Crash Course
- **Title:** Classification: Accuracy, recall, precision, and related metrics
- **URL:** https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall
- **Raw:** `raw/Classification Accuracy, recall, precision, and related metrics    Machine Learning.md` (clipped markdown copy, immutable)
- **Ingested:** 2026-06-08
