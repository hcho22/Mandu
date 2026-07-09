---
type: skill
category: technical
hcho-level: strong
demand: 5
status: established
last-updated: 2026-07-08
source-count: 6
tags: [rag, retrieval, vector-db, ai-builder]
---

# RAG systems

## What it is
Retrieval-Augmented Generation: retrieving relevant context from a vector database (or hybrid store) and feeding it to an LLM at generation time.
Covers embedding, chunking, retrieval architecture (dense, sparse, hybrid/RRF), and permission-aware retrieval.

## Why roles want it
A recurring must-have for [[applied-ai-engineer]] and the broader AI builder bucket.
Carries an explicit comp premium (+10-15% at mid level).
"RAG" postings grew ~340% since 2024.

## Why it matters for landing a role
RAG is the dominant pattern for making LLMs useful on private data, so it is the single most concrete proxy for "can build a real production AI system" rather than just call an API.
A raw LLM reasons well but does not know your business; RAG is the research assistant that hands it the right documents before every answer, which is what almost every enterprise AI product needs.
Three reasons it reads as a differentiator, not a checkbox:
- Demand and comp: required by 5 of the ingested roles, and RAG architecture adds +10-15% at mid level (per [[applied-ai-engineer-role-research]]).
- Market direction: "LLM"/"RAG" postings grew ~340% since 2024 while generic "machine learning" postings declined ~18%.
- It bundles the hard parts: doing RAG well forces retrieval quality, chunking, hybrid search, and [[eval-pipeline-design]] to measure it, so "I have shipped production RAG" implicitly claims the whole production-AI competency.
It appears across role types in different guises: [[cohere]] Applied AI (vector DBs), [[hex]] Search-and-Context (permissions-aware indexing at scale), [[closure]] (unstructured + structured retrieval), and the [[forward-deployed-engineer]] roles (client/server RAG apps).

## How to acquire or demonstrate
Ship a production RAG system with a real vector store, not a notebook demo.
Show retrieval quality work: a retrieval eval suite, hybrid retrieval, reranking.

## hcho's current level: strong
Evidence: the Agentic RAG flagship - FastAPI + pgvector, hybrid retrieval (RRF), raw OpenAI SDK (framework-free), permission-aware retrieval, plus a retrieval eval suite.
This is a production-grade portfolio artifact, not a toy.

## Gap and how to close
Minimal skill gap.
The remaining work is packaging: make the deployment and eval-gate story legible to a hiring manager (see [[applied-ai-engineer]] path). Cross-link: [[eval-pipeline-design]], [[mlops-deployment]].

## Roles that require it
- [[applied-ai-engineer]] (must-have)
- [[forward-deployed-engineer]] (must/strong-plus; client+server RAG apps at Cohere North, Closure)
- [[ai-research-engineer]] (must-have; Hex Search and Context - permissions-aware indexing, a direct hcho match)
- [[ai-content-engineer]] (preferred)
- [[founding-ai-engineer]] (must-have; unstructured + structured retrieval)
