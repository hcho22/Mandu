---
type: concept
tags: [agentic-rag, evals, ci, regression]
date: 2026-06-15
source-count: 1
status: seeded
component: "docs/evals.md CI and nightly eval workflows"
---

# CI Eval Gating

A CI workflow that compares retrieval-eval results against baselines so retrieval regressions are visible before merge or during scheduled runs.

## From the sources

[[agentic-rag-evals]] provides the worked regression example for the CI loop:

- The PR workflow runs the retrieval suite on PR head and on `main`, then posts a delta table for the headline metrics and per-category recall.
- A throwaway PR changed `DEFAULT_CHUNK_SIZE` from 500 to 100. Smaller chunks split answer spans and caused a sharp retrieval regression.
- CI reported vector and hybrid `recall@5` at 0.350 with a negative 0.510 delta versus `main`; MRR and nDCG@5 also dropped sharply. Keyword moved less in absolute terms because it was already near zero.
- The category breakdown made the cause interpretable: multi-hop and paraphrase questions dropped most because they depend on chunk spans retaining enough answer context.
- The document treats this as an honest demonstration: the regression cause was contrived, but the workflow caught and posted it automatically in a few minutes.
- The RAGAS section extends the gating idea: score thresholds use fixed absolute drops against a rolling 4-week median, operational gates remain fixed, and some red alerts require cross-family corroboration.

## Synthesis

The value of the CI gate is the delta comment, not just the pass/fail. It turns retrieval quality into reviewable evidence: a reviewer can see which mode regressed, which slice regressed, and whether the change affects retrieval mechanics, answer quality, or a harder operational/security property.
