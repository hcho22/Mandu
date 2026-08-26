---
type: concept
tags: [evals, metrics, classification]
date: 2026-06-08
source-count: 6
status: seeded
session: "S2 - Classical ML metric foundations"
---

# Classification Metrics

Confusion-matrix-derived measures (accuracy, precision, recall, F1, ROC-AUC, PR-AUC) and when each fails, notably under class imbalance.

## From the sources

Eugene Yan, [[patterns-for-building-llm-based-systems-and-products]], positions classification metrics within a broader metric-selection decision and warns about classical text-generation metrics:

- For **classification-like LLM tasks** (toxicity detection, document categorization, extractive QA without dialogue), use standard classification metrics: **precision, recall, PR-AUC**. Choosing a metric you can compute and interpret as a single comparable number is the point.
- For reference tasks with no single correct answer (translation, extractive summarization), use **reference-based generation metrics**: matching-based **BLEU** (precision-oriented, n-gram) and **ROUGE** (recall-oriented), or embedding-based **BERTScore** (cosine similarity, handles synonyms) and **MoverScore** (soft many-to-one token alignment). See [[rag-evaluation]] for the reference-based vs reference-free split.
- These classical metrics have three pitfalls: **poor correlation with human judgment**, **poor adaptability** across tasks (n-gram overlap is meaningless for dialogue or abstractive summarization, where a zero-overlap answer can still be correct), and **poor reproducibility** (high cross-study variance; a survey of 2,000 studies found ROUGE scores hard to reproduce and often computed with incorrect implementations).
- Takeaway for this concept: classification metrics are the reliable, interpretable floor; for open-ended generation, classical metrics break down and teams fall back to LLM-as-judge (see [[llm-as-judge]]).

The Google Machine Learning Crash Course, [[classification-accuracy-precision-recall]], gives the foundational definitions, all computed at a **single fixed threshold** (they shift as the threshold moves):

- **Accuracy** = (TP + TN) / total. Coarse but useful only on **balanced** data; on imbalanced data it misleads (always-predict-majority scores 99% on a 1%-positive set while being useless).
- **Recall** = **TPR** = "probability of detection" = TP / (TP + FN). Prioritize when **false negatives are costly** (disease detection).
- **False positive rate (FPR)** = "probability of false alarm" = FP / (FP + TN). Volatile when actual negatives are few.
- **Precision** = TP / (TP + FP). Prioritize when **false positives are costly**.
- **Precision-recall tradeoff:** raising the threshold cuts false positives (raises precision) but adds false negatives (lowers recall), so the two usually move inversely.
- **F1** = harmonic mean = 2PR / (P + R) = 2TP / (2TP + FP + FN): balances precision and recall, beats accuracy on imbalanced data, and tracks the worse of the two when they diverge.
- **Metric choice is cost-driven** (recall when FN hurts, precision/FPR when FP hurts); accuracy is only a rough progress check on balanced data. Division by zero yields **NaN** (e.g. precision when the model never predicts positive).
- This is the derivation behind the LLM-eval rule of thumb on [[llm-as-judge]] and from Yan: do not trust raw accuracy on imbalanced data - report precision and recall.

The Google Machine Learning Crash Course, [[classification-roc-and-auc]], extends the same metrics from a single threshold to **all thresholds**:

- **ROC curve** (receiver operating characteristic) plots **TPR (y) against FPR (x)** at every threshold - a visual map of performance across all operating points.
- **AUC** (area under the ROC curve) = the probability the model ranks a **random positive above a random negative**; it is **threshold-independent**. Reference points: **1.0** perfect, **0.5** random (diagonal), **< 0.5** worse than chance (and reversible by flipping predictions).
- **AUC compares whole models** (higher is generally better) when classes are roughly balanced.
- **PR curve / PR-AUC:** on **imbalanced** data, a precision-recall curve (precision on y, recall on x) and its area compare models better than ROC/AUC.
- **Threshold selection:** the ROC points closest to (0, 1) are the best thresholds; pick among them by cost - lower-FPR when false positives hurt, higher-TPR when false negatives hurt, balanced otherwise.

Chip Huyen, [[evaluate-ai-systems]], places these metrics inside AI-system evaluation:

- Multiple-choice questions are common in LLM benchmarks because they are easy to create, verify, reproduce, and compare against a random baseline. Classification is the special case where every example shares the same choice set.
- MCQ and classification metrics are useful for knowledge, reasoning, intent classification, sentiment analysis, next-action prediction, and other close-ended tasks, but they do not directly test the model's ability to generate good open-ended responses.
- MCQ scores can shift under small prompt-format changes, such as option wording, extra spaces, or an added "Choices:" prefix, so benchmark scores should not be treated as exact measures of model capability.
- When logprobs are available, they can expose classification confidence: a model whose class probabilities are evenly spread is less reliable than one assigning high probability to a single class.

Clémentine Fourrier, Thibaud Frere, Guilherme Penedo & Thomas Wolf, [[evaluation-guidebook]], catalog the automatic metrics for scoring free-form text and how to aggregate them:

- **Match-based string metrics** sit on a flexibility ladder: **exact match** (and its fuzzy variants - prefix/suffix/quasi-exact, often hidden behind the same name), n-gram overlap **BLEU** (precision, length-biased, weak human correlation) and **ROUGE** (recall), edit-distance **TER**, and embedding-based **BLEURT** (BERT trained on human judgments). The metric *name* alone is unreliable - you must read the code to know what it computes.
- **Aggregating per-sample scores:** for **binary** scores use precision (FP-costly), recall (FN-costly), **F1**, or **MCC** (robust to imbalance); for **continuous** scores use MSE/MAE; for calibration studies use R^2 / Pearson / Spearman. For high-stakes domains (medical, toxicity) report **worst-case**, not average, performance.
- **Accuracy needs length normalization** in multiple-choice log-likelihood eval, or the model just prefers shorter answers: `acc_char`, `acc_token`, and `acc_pmi` (normalizes by the answer's unconditional probability - best for hard reasoning/knowledge tasks, ~2x costlier). Recommended default is max(acc_char, acc_token); F1 for generative tasks unless exact match is required.
- **Sampling-based metrics** trade cost for robustness: **pass@k over n** (unbiased estimator), **maj@n** (majority vote, good for math/reasoning), **cot@n**, and **avg@n** (stable average). Always report temperature/top-p/k; avoid sampling in cheap ablations (use greedy + fixed seed), reserve it for post-training and inference-time-compute studies.
- **Functional scorers** are the authors' favorite: instead of fuzzy-matching a reference, check whether output satisfies verifiable constraints (IFEval-style: "exactly 3 bullets", valid JSON), as unit tests do for code. They are unambiguous, fast, cheap, and contamination-resistant - preferred over model judges (see [[llm-as-judge]]) when feasible.

Peter Yang, Hamel Husain & Shreya Shankar, [[ai-evals-error-analysis]], put the precision/recall lens on the *eval tools themselves*, not just the product model:

- **Watch precision, not just recall, when trusting an automated eval tool.** In Hamel's benchmark, best-case precision from the "do-it-for-you" vendors is only ~**80-90%**, meaning **10-20% of flagged "errors" are red herrings** that can distort a product if accepted blindly. High recall alone is not enough - a tool that surfaces many real errors but also many false ones still needs a human to confirm the flagged set (see [[production-eval-tooling]]).
- **Benchmark the rubric with a labeled set.** Error analysis produces annotated samples for free, so the rubric's judges can be scored with ordinary precision/recall against those labels - evals are not just a rubric, you have to measure whether the rubric is any good (the same "evaluate your evaluator" point on [[llm-as-judge]]).
- **Prefer yes/no pass/fail criteria over invented numeric scores**, which reduces each criterion to a binary classification whose precision and recall are directly computable, rather than an uncalibrated 1-5 scale.

## In my own words (hcho)
