---
type: source
tags: [evals, metrics, classification, roc, auc, pr-auc, thresholds]
date: 2026-06-08
title: "Classification: ROC and AUC"
author: "Google Machine Learning Crash Course"
url: "https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc"
concepts: [classification-metrics]
---

# Classification: ROC and AUC

A Google Machine Learning Crash Course page that moves from single-threshold metrics to evaluating a binary classifier across **all** thresholds: the ROC curve (TPR vs FPR at every threshold), its summary statistic AUC (interpreted as a ranking probability), the PR curve as the imbalanced-data alternative, and how to read a ROC curve to pick both a model and an operating threshold. It is the direct sequel to the accuracy/precision/recall page.

## Key claims

- Single-threshold metrics (accuracy, precision, recall) only describe one operating point; evaluating quality **across all thresholds** needs different tools.
- **ROC curve** (receiver operating characteristic, a name held over from WWII radar) plots **TPR on the y-axis against FPR on the x-axis** at every threshold - a visual map of performance across all thresholds.
- **AUC** (area under the ROC curve) = the probability that the model ranks a **randomly chosen positive higher than a randomly chosen negative**. It is **threshold-independent**: it measures ranking quality regardless of where the threshold is set.
- AUC reference points: **1.0** = perfect ranking; **0.5** = random guessing (the diagonal line); **below 0.5** = worse than chance - and a worse-than-chance classifier can be made better than chance simply by **reversing its predictions** (no retraining).
- **AUC compares models:** when the dataset is roughly balanced, the model with greater AUC is generally better.
- **PR curve / PR-AUC:** ROC/AUC work well when classes are roughly balanced; on **imbalanced** datasets a **precision-recall curve** (precision on y, recall on x across thresholds) and its area give a better comparative visualization.
- **Threshold selection from the ROC:** the points closest to (0, 1) are the best-performing thresholds. Choose among them by cost - a lower-FPR point when false positives (false alarms) are costly, a higher-TPR point when false negatives are costly, or a balanced point when costs are roughly equal.

## Connections

- [[classification-metrics]] - extends the S2 page from single-threshold metrics to **threshold-independent** evaluation: the ROC curve, AUC as a ranking probability, PR-AUC for imbalanced data, and threshold/model selection. Builds directly on the TPR and FPR definitions from [[classification-accuracy-precision-recall]].

## Source

- **Author:** Google Machine Learning Crash Course
- **Title:** Classification: ROC and AUC
- **URL:** https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc
- **Raw:** `raw/Classification ROC and AUC    Machine Learning.md` (clipped markdown copy, immutable)
- **Ingested:** 2026-06-08
