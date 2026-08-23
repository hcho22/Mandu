---
type: source
title: "Classification: ROC and AUC (Google ML Crash Course)"
source-type: doc
author: "Google"
url: "https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc"
date-ingested: 2026-07-08
date-created: 2026-06-08
tags: [ml-metrics, classification, roc, auc, precision-recall, thresholds]
---

# Classification: ROC and AUC (Google ML Crash Course)

A reference page from Google's ([[google]]) Machine Learning Crash Course explaining how to evaluate a binary classifier across all classification thresholds, rather than at a single threshold.
This is the wiki's first classical-ML-metrics source and the founding page of the [[ml-metrics]] area.

## Key claims

- **[[roc-and-auc|ROC curve]]:** plots true positive rate (TPR) against false positive rate (FPR) at every threshold. A perfect model reaches (FPR=0, TPR=1); random guessing is the diagonal from (0,0) to (1,1).
- **[[roc-and-auc|AUC]]** (area under the ROC curve) = the probability that the model ranks a randomly chosen positive example above a randomly chosen negative one, independent of threshold. Perfect = 1.0; random = 0.5; below 0.5 is worse than chance (and can be fixed by flipping the labels).
- **AUC/ROC assume roughly balanced classes.** For imbalanced data, [[precision-recall]] curves (precision vs recall across thresholds) give a better comparison - the same imbalance caveat Hamel Husain raised for judge agreement.
- **[[classification-threshold|Threshold choice]] is a cost decision:** points on the ROC nearest (0,1) are the best thresholds; pick a low-FPR point when false positives are costly, a high-TPR point when false negatives are costly, or a balanced point when costs are similar.

## Connections

- [[ml-metrics]] - founding source for the metrics area.
- [[roc-and-auc]], [[precision-recall]], [[classification-threshold]] - the concepts.
- [[llm-as-judge]] / [[pass-fail-over-score-evals]] - gives a rigorous home to the "precision and recall, not raw agreement" caution those pages reference; imbalanced-data intuition is identical.
- [[cost-of-being-wrong]] - threshold selection is the operational form of "follow the cost of being wrong" (FP vs FN cost).
- [[evals]] - classical classification metrics underpin how LLM/agent evaluations are scored.

## Source

- **Author:** Google (Machine Learning Crash Course)
- **Title:** Classification: ROC and AUC
- **URL:** https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc
- **Raw:** [[Classification ROC and AUC    Machine Learning]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
