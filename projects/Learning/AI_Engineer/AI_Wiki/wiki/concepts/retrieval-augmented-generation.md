---
type: concept
tags: [rag, retrieval, embeddings, production-llm]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Retrieval-Augmented Generation (RAG)

From [[zero-to-hireable-ai-engineer]]: give the model a library to look things up in, so it can answer about your specific documents instead of relying only on its training data.

## The pipeline

1. **Chunk** your documents into pieces.
2. **Embed** each chunk into a vector (numbers capturing its meaning); similar meaning -> nearby vectors.
3. **Store** the vectors (with metadata) in a vector database.
4. **Retrieve** at query time: embed the question the same way, find the closest chunks, optionally rerank them.
5. **Ground**: hand the top chunks to the model with the question and instruct it to answer only from that context and to cite sources.

## Key points

- Everything past the basic flow is refinement: metadata filtering, reranking, chunk-size tuning, query rewriting.
- The grounding prompt does heavy lifting - giving the model an approved way to say "I don't have enough information in the provided documents" is the single most effective way to cut hallucinations.
- A minimal build teaches the whole idea: embed 20 sentences and return the 3 most similar to a new one - that is RAG in miniature.

## Synthesis

RAG is the anchor concept of the [[rag]] area and the technical core of hcho's flagship product, so this page will grow as deeper sources land.
Its most important lesson is downstream, in [[retrieval-is-the-bottleneck]]: the generation step is rarely where RAG fails, so the engineering (and the evals) belong in retrieval and grounding.
Connects to [[single-call-workflow-or-agent]] (add retrieval when the model needs your data, before reaching for an agent) and [[system-design]] (the pipeline is an architecture with real trade-offs).
