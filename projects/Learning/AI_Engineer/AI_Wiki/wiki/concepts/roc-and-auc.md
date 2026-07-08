---
type: concept
tags: [ml-metrics, classification, roc, auc]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# ROC and AUC

Two tools for evaluating a binary classifier across all thresholds, from [[classification-roc-and-auc]].

## ROC curve

- Plots **true positive rate (TPR)** on the y-axis against **false positive rate (FPR)** on the x-axis, computed at every threshold.
- A perfect model passes through (FPR=0, TPR=1); pure random guessing is the diagonal from (0,0) to (1,1).

## AUC (area under the ROC curve)

- Equals the **probability that the model ranks a randomly chosen positive example above a randomly chosen negative one** - a threshold-independent measure of ranking quality.
- 1.0 = perfect ranking; 0.5 = random; below 0.5 = worse than chance (flip the labels to fix it).
- Higher AUC generally means the better model, **as long as classes are roughly balanced**; for imbalanced data prefer [[precision-recall]] curves.

## Synthesis

AUC answers "how well does the model separate the classes, regardless of where I set the cutoff," which is why it is a comparison metric; the cutoff itself is a separate decision (see [[classification-threshold]]).
It is a precise ancestor of LLM-eval intuitions: ranking quality and threshold-independence are exactly what you want when comparing models or judges in [[evals]].
