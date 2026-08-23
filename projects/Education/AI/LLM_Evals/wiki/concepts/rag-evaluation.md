---
type: concept
tags: [evals, rag, ragas]
date: 2026-06-08
source-count: 3
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

Chip Huyen, [[evaluate-ai-systems]], focuses on the generation-side factuality contract that RAG creates:

- RAG systems retrieve external context, and the generated response should be factually consistent with that retrieved context. This is **local factual consistency**, which is easier to evaluate than open-world factuality because the evidence is explicit.
- A RAG eval should separate component failures. If the final answer is wrong, the failure may come from retrieval, context preparation, generation, or post-processing; each intermediate output should be evaluated independently before relying only on the end-to-end score.
- Factual-consistency checks can be implemented with an LLM judge, textual entailment/NLI scorer, or knowledge-augmented verification pipeline. The evaluation should focus on query slices where hallucination is likely, such as niche knowledge and questions about nonexistent facts.

Clémentine Fourrier, Thibaud Frere, Guilherme Penedo & Thomas Wolf, [[evaluation-guidebook]], add the long-context benchmark lineage that underpins retrieval evaluation:

- **Long-context eval evolved** from **NIAH** (Needle in a Haystack - plant a fact in long text, retrieve it; near-solved by 2025) to **RULER** (multi-hop tracing, variable tracking) and **Michelangelo/MRCR**, up to **HELMET**, which bundles RAG/QA datasets (Natural Questions, TriviaQA, PopQA, HotpotQA, NarrativeQA), recall (RULER/JSONKV), generation-with-citation (ALCE), summarization, and reranking (MS MARCO) into one higher-signal suite. Caution against aggregating overlapping suites (HELMET already includes InfinityBench).
- Retrieval-heavy assistant tasks like **GAIA** turn retrieval into an end-to-end agentic eval (combine tools + reasoning + retrieval to answer real queries - see [[agent-eval-and-stats]]), and knowledge benchmarks are shifting from closed-book to **open-book/retrieval** as models gain web access - making retrieval quality central to what "knowledge" evals now measure (see [[llm-benchmarks-contamination]]).

## In my own words (hcho)
