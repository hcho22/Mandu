---
type: concept
tags: [rag, embeddings, retrieval, vectors]
status: developing
source-count: 2
last-updated: 2026-07-08
---

# Embeddings

Text (or other data) turned into a fixed-size vector of numbers that captures meaning, so that similar items land close together and dissimilar items far apart.
Introduced in the [[rag]] primer of [[zero-to-hireable-ai-engineer]] and deepened by [[llm-patterns]].

## Key points

- The useful property: search-by-meaning - similar text -> nearby vectors - which is the engine under [[retrieval-augmented-generation|RAG]].
- **Model choice matters:** the HuggingFace MTEB leaderboard scores models on diverse tasks; instructor-style models (E5, Instructor, GTE) that prepend a task description often beat the convenient API default for retrieval.
- Embeddings are multimodal (CLIP embeds images and text in one space) and can encode behavior or graph relationships, not just text.
- **ANN indices** retrieve fast at scale by trading a little recall for big speedups: LSH, FAISS, HNSW, ScaNN. Evaluate on recall, latency/throughput, memory, and ease of adding items.

## Synthesis

Embeddings are the substrate of the [[rag]] area: retrieval quality is bounded by embedding quality, so choosing and evaluating the embedding model is upstream of everything in [[retrieval-is-the-bottleneck]].
The recurring lesson is that the popular default is rarely the best retriever - which is a measurement point ([[eval-driven-development]]): benchmark embedding models on *your* retrieval task, don't assume.
Pairs with [[hybrid-retrieval]] (embeddings alone miss exact-match needs) and grounds hcho's flagship, where embedding + index choices are core product decisions.
