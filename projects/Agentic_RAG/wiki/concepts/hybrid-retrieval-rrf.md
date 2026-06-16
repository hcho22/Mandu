---
type: concept
tags: [agentic-rag, retrieval, hybrid-search, rrf]
date: 2026-06-15
source-count: 2
status: seeded
component: "retrieval stack (pgvector HNSW + Postgres full-text + Reciprocal Rank Fusion)"
---

# Hybrid Retrieval RRF

A retrieval stack that exposes vector-only, keyword-only, and hybrid search, then fuses vector and keyword candidate ranks with Reciprocal Rank Fusion for the hybrid mode.

## From the sources

[[agentic-rag-evals]] grounds hybrid retrieval as one of the three retrieval modes evaluated by the suite:

- `search_documents` exposes vector-only retrieval through pgvector HNSW, keyword-only retrieval through the Postgres full-text `keyword_search` RPC, and hybrid retrieval that runs both paths and fuses the results with Reciprocal Rank Fusion.
- The eval's purpose is to make claims such as "hybrid is better than vector-only" falsifiable. Without shared metrics, hybrid retrieval is only an architectural preference.
- The golden categories are designed to stress different retrieval behaviors: multi-hop questions test aggregate recall, adversarial questions separate lexical and semantic matches, and paraphrase questions test embedding behavior when query terms diverge from corpus wording.
- In the chunk-size regression demo, vector and hybrid lost the most absolute recall while keyword was already near zero. That result shows hybrid's quality depends on upstream chunking and semantic retrieval behavior, not only on the fusion formula.
- Future swaps such as rerankers or vector-store changes need this same mode-by-mode delta, because "better retrieval" is only meaningful relative to a measured baseline.

[[permissions-aware-rag]] adds the permission-filtering dimension:

- Vector, keyword, and hybrid retrieval are all tested under full-access, partial-access, and no-access viewer setups.
- The HNSW gotcha belongs primarily to vector search: selective ACL predicates can cause HNSW walks to exhaust the `ef_search` candidate budget before enough visible chunks pass the filter.
- Hybrid retrieval inherits that behavior when its vector half is affected, even though keyword retrieval has a different execution path.
- At 10k chunks, Postgres avoids the HNSW path for selective viewers and sorts the filtered visible set exactly, so the benchmark shows 1.000 across selectivities rather than a recall curve.

## Synthesis

Hybrid retrieval is useful here because the project can measure when it helps. The important design point is not simply "vector plus keyword"; it is that [[retrieval-eval-suite]] gives the project a way to compare each mode on the same corpus, [[ci-eval-gating]] can catch when a change breaks the mode that looked strongest, and [[permissions-aware-retrieval]] can reveal whether the retrieval plan still behaves when visibility is selective.
