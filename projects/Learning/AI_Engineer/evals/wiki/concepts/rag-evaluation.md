---
type: concept
tags: [evals, rag, ragas]
date: 2026-06-08
source-count: 1
status: seeded
session: "S6 - RAG evaluation"
---

# RAG Evaluation

Measuring retrieval-augmented generation via the triad of faithfulness, answer relevance, and context precision/recall.

## From the sources

Eugene Yan, [[patterns-for-building-llm-based-systems-and-products]], grounds RAG evaluation in the retrieval half of the pipeline and in metric framing:

- **Retrieval quality drives end-to-end quality.** Dense Passage Retrieval (DPR) beat BM25 on top-5 accuracy (65.2% vs 42.9%), and the DPR paper showed higher retrieval precision translates into higher end-to-end QA accuracy - upstream retrieval is the lever.
- **Evaluate the embedding model** on a benchmark before trusting it: the **MTEB leaderboard** scores embedding models across retrieval, classification, clustering, and summarization tasks.
- **Evaluate the ANN index** (approximate nearest neighbors) on four axes: **recall** against exact nearest neighbors, **latency/throughput**, **memory footprint**, and **ease of adding new items** (some indices must be fully rebuilt). No framework wins on all axes, so define requirements first.
- **Reference-based vs reference-free** is the key metric split. Reference-based metrics compare output to a gold answer (BLEU, ROUGE, BERTScore - see [[classification-metrics]]); reference-free metrics (a strong LLM judge - see [[llm-as-judge]]) need no gold reference, which suits open-ended RAG answers.
- Hybrid retrieval (keyword/BM25 + semantic embeddings) outperformed either alone in Yan's own Obsidian-Copilot work, which has direct implications for what a RAG eval should isolate.

## In my own words (hcho)
