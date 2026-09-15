---
type: area
tags: [rag, retrieval, embeddings, agents, production-llm]
status: developing
source-count: 3
last-updated: 2026-08-05
---

# RAG (Retrieval-Augmented Generation)

The durable hub for giving a model a library to look things up in, so it can answer from your documents instead of only its training data.
This area is directly load-bearing for hcho: Purvia is a permission-aware RAG starter kit, so the general craft lives here and product-specific decisions live in the Purvia wiki (`projects/Purvia/wiki/`).

## The core idea (plain English)

From [[zero-to-hireable-ai-engineer]]: take your documents, break them into chunks, convert each chunk into a vector (numbers capturing its meaning), and store them.
At query time, embed the question the same way, find the closest chunks, and hand those to the model with the question.
The model answers from what you gave it. Everything else is refinement. See [[retrieval-augmented-generation]].

## Concepts in this area

- [[retrieval-augmented-generation]] - the chunk -> embed -> store -> retrieve -> ground pipeline, and why it exists.
- [[retrieval-is-the-bottleneck]] - most RAG failures are retrieval failures, not model failures; debug what got retrieved first.
- [[embeddings]] - text as vectors; model choice and ANN indices are upstream of everything.
- [[hybrid-retrieval]] - combine keyword (BM25) and semantic search; each covers the other's blind spots.
- [[knowledge-graph]] - store entities and relationships explicitly (GraphRAG) so multi-hop answers become traversable; fixes the "connect scattered facts" blind spot chunk-similarity cannot. **Seed; needs a technical source to deepen.**

## Building blocks (folded here for now, promote as sources deepen them)

- **Chunking** - split documents before embedding; the trade-off is too-big loses precision, too-small loses context (a ~500-char chunk with ~50 overlap is a sane default).
- **Vector database** - store and search embeddings fast (Chroma locally to learn; pgvector when you already run Postgres).
- **Metadata filtering** - tag chunks (source, date, section) and filter at query time.
- **Reranking** - retrieve a broad set fast, then re-score the top few for true relevance.
- **Grounding + citations** - answer only from provided context, cite the source, and give the model an approved way to say "I don't have enough information" (the single most effective anti-hallucination move).
- **Retrieval architectures** ([[llm-patterns]]): DPR (dense retrieval beats BM25 baselines; higher retrieval precision -> higher answer accuracy), FiD, RETRO, HyDE (generate a hypothetical answer, then embed it to retrieve).

## Where this connects

- [[evals]] - a RAG system needs a small eval set (Ragas is RAG-specific) run on every prompt/model/retrieval change.
- [[single-call-workflow-or-agent]] - RAG is often the "add retrieval when the model needs your specific data" step before reaching for an agent.
- [[system-design]] / [[everything-as-code-abstractions]] - vector DBs and pipelines are architecture choices with trade-offs.

## Sources

- [[zero-to-hireable-ai-engineer]] - a clean RAG primer inside the four-month curriculum.
- [[llm-patterns]] - Eugene Yan's RAG pattern: history (DPR/FiD/RETRO/HyDE), embeddings + ANN, and hybrid retrieval.
- [[graph-engineering-isenberg]] - Greg Isenberg: a founder-level introduction of knowledge graphs (GraphRAG) as the complement to ordinary chunk-similarity retrieval.

## Synthesis

One source in, the throughline is that **RAG is a retrieval problem wearing an LLM costume**: the model is rarely the failure point, the retrieval is, so the craft is in chunking, metadata, reranking, and grounding, not in the generation step.
That is a validation-shaped discipline - build a labeled question/chunk set, measure what retrieval actually returns, and fix the pipeline - which is exactly hcho's edge and the spine of his flagship.
Expect the LLM-patterns source (Eugene Yan) and the evals sources to deepen this hub substantially; promote the building blocks above into their own pages as they earn a second source.
