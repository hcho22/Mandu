---
type: concept
tags: [rag, retrieval, knowledge-graph, graphrag, agentic-engineering]
status: seed
source-count: 1
last-updated: 2026-08-05
---

# Knowledge Graph

A structured representation of **how information connects** - entities (people, companies, products, teams, events) joined by typed relationships - that a model can reason over.
Introduced in [[graph-engineering-isenberg]] as one of the two things "graph" means in AI, and deliberately separated there from the agent graph of [[graph-engineering]]: a knowledge graph is about how information connects, an agent graph is about how work moves.

## Why it exists: the limit of ordinary RAG

[[retrieval-augmented-generation]] retrieves text chunks that look *similar* to the query.
That works when the answer sits in one place, and fails when the answer requires **connecting scattered facts**: this customer works at this company, which uses this product, which connects to this tool, whose support issue relates to this feature, owned by this team.
No single chunk contains that chain; similarity search cannot assemble it.
A knowledge graph stores the entities and relationships explicitly, so the connection is traversable rather than something the retriever has to reconstruct from adjacent text.

- Tool named in the source: **Microsoft GraphRAG**.
- This is the relationship-reasoning complement to the wiki's existing retrieval stack ([[retrieval-is-the-bottleneck]], [[hybrid-retrieval]], [[embeddings]]): where hybrid retrieval fixes *lexical vs semantic* blind spots, a knowledge graph fixes the *multi-hop connection* blind spot.

## Key points

- **Complements, does not replace, chunk retrieval.** The source's framing is that the best systems use both a knowledge graph (how information connects) and an agent graph (how work moves).
- The concept is introduced at a shallow depth here - one source, one operator-level explanation. It is a marker for a real technique (GraphRAG, multi-hop retrieval) that a future technical source can deepen.

## Synthesis

This page is intentionally a **seed**: the source is a founder-audience explainer, not a retrieval-engineering account, so it names the idea and its motivating failure without the mechanics (extraction, community detection, graph traversal, cost).
It earns a page because the "connect scattered facts" failure of similarity search is a real and recurring limit of the retrieval stack the wiki documents for hcho's flagship, and because it disambiguates "graph" - the single most confused word in the [[graph-engineering]] discourse.

For hcho's [[rag]] work the actionable read is narrow but real: if a Purvia buyer's questions are multi-hop ("which documents can this role see, given the team they are on and the project it owns"), similarity retrieval will underperform a graph or a SQL join over the permission model - which is, in fact, why Purvia enforces access in a SQL predicate rather than by post-filtering retrieved chunks. Worth revisiting when a proper GraphRAG source lands.
