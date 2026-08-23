---
type: concept
tags: [ml-metrics, classification, thresholds, tradeoffs]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Classification Threshold

The cutoff that converts a model's continuous score into a class label, and the cost-driven decision of where to set it, from [[classification-roc-and-auc]].

## Key points

- Every threshold produces a confusion matrix (TP, FP, TN, FN) and thus a (TPR, FPR) point on the [[roc-and-auc|ROC]] curve; points nearest (0,1) are the best-performing thresholds.
- **The choice is about error costs:**
  - False positives costly to false negatives cheap: pick a low-FPR threshold (lower TPR is acceptable).
  - False negatives costly to false positives cheap: pick a high-TPR threshold.
  - Costs similar: pick the balanced point.
- Threshold selection is separate from model quality: AUC compares models; the threshold sets the operating point of the chosen model.

## Synthesis

This is the quantitative form of [[cost-of-being-wrong]]: "follow the cost of being wrong" becomes "set the threshold by the relative cost of FP vs FN."
For LLM and agent systems the same logic governs where to gate an [[llm-as-judge]] or an escalation rule, tying classical [[ml-metrics]] directly to the [[evals]] hub and to agent design.
