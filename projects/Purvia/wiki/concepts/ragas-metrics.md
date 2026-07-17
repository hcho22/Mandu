---
type: concept
tags: [agentic-rag, evals, ragas, generation]
date: 2026-06-15
source-count: 1
status: seeded
component: "weekly RAGAS eval workflow"
---

# RAGAS Metrics

RAGAS metrics that evaluate generated answers and retrieved contexts for faithfulness, answer relevancy, context precision, and context recall.

## From the sources

[[agentic-rag-evals]] describes RAGAS as a standardized supplement to the custom judge path:

- The runner can add RAGAS Faithfulness, Answer Relevancy, Context Precision, and Context Recall for selected hybrid-mode cells.
- RAGAS is not the primary independent judge. It uses `gpt-4o-mini`, the same family as the answer generator, so the project keeps the custom Claude judge as the cross-family signal.
- RAGAS is scoped to hybrid retrieval and only to `full_access x pre_filter` and `partial_access x pre_filter`; vector/keyword comparisons remain in the retrieval metrics, and `no_access` cells belong to the security table.
- Score gates use fixed absolute deltas in each metric's native units, not percentage or sigma thresholds. The document argues that sigma is unstable on a 4-week window and percentages mislead near 0 or 1.
- Score baselines use a rolling 4-week median so genuine sustained quality improvements can rebaseline, while operational gates such as effective coverage and API errors stay fixed.
- Faithfulness or Answer Relevancy drops become red only when the independent Claude judge corroborates the same drop in the same cell; Context Precision and Context Recall have no Claude equivalent and are tagged as single-judge red.
- The source explicitly warns that embeddings, generation, and RAGAS judge calls are not bit-deterministic, so thresholds need enough margin to ignore ordinary jitter.

## Synthesis

RAGAS is useful here because it gives the project familiar RAG-eval vocabulary, but the source refuses to overclaim it. The stronger design is the combination: RAGAS for standardized labels, Claude for independent corroboration, and [[ci-eval-gating]] rules that treat single-judge drift differently from corroborated failure.
