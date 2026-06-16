---
type: concept
tags: [agentic-rag, evals, retrieval, golden-set]
date: 2026-06-15
source-count: 2
status: seeded
component: "docs/evals.md"
---

# Retrieval Eval Suite

An evaluation harness for retrieval quality over a fixed corpus and golden set using recall, rank, and relevance metrics.

## From the sources

[[agentic-rag-evals]] seeds the retrieval eval suite:

- The suite evaluates the real `search_documents` retrieval modes: vector-only, keyword-only, and [[hybrid-retrieval-rrf]].
- The corpus is 7 committed markdown documents describing Acme Co policies. It is intentionally small and interlocking, with refund, shipping, warranty, loyalty, SOP, returns, and product-catalog documents that support both single-chunk and multi-hop questions.
- The seeding path uses the same chunking and embedding code as production ingestion. Stable chunk IDs use `filename_slug:chunk_index`, so `retrieval_gold.yaml` can point to named gold chunks across CI cold starts.
- The golden set has 50 questions: 20 `single_chunk`, 15 `multi_hop`, 10 `adversarial`, and 5 `paraphrase`. The categories make the eval more diagnostic than a single aggregate score.
- Core metrics are `recall@k` for k in 1, 3, 5, and 10, MRR for first-correct rank, and nDCG@5 for ranked relevance. Multi-hop questions receive partial credit when only some gold chunks appear.
- The runner writes full JSON detail and a markdown summary. The source explicitly limits the suite: retrieval-only metrics do not prove answer correctness, tool routing, latency/cost, or generalization to other corpora.

[[permissions-aware-rag]] extends the suite into permission-aware retrieval:

- The correctness eval adds viewer setups and filter strategies: full access, partial access, and no access across pre-filter and post-filter retrieval.
- It keeps the same retrieval quality vocabulary from [[agentic-rag-evals]] while adding security and permissions-specific slices.
- The small 14-chunk corpus makes recall trade-offs invisible in v0, so the source treats the security table as the load-bearing result and the recall tables as scaffolding.
- The permission-scale benchmark seeds 10k chunks, creates viewers at 50%, 10%, and 1% selectivity, and sweeps `ef_search` values of 40, 80, 200, and 500.
- At 10k chunks every scale cell is 1.000 because Postgres chooses exact nearest-neighbor sorting over the filtered visible set; this is a correct planner choice and means a 100k+ corpus is the natural next benchmark.

## Synthesis

The suite is strongest as a delta detector, not as a universal retrieval benchmark. Its small fixed corpus and hand-authored labels make absolute scores narrow, but the same narrowness is what makes PR-vs-main comparison practical: the biases are shared on both sides, so regressions in chunking, retrieval mode, reranking, or permission filtering become visible. The permission extension also shows where evals must distinguish "security property holds" from "recall curve is informative at this scale."
