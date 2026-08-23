---
type: concept
tags: [production-llm, caching, cost, latency]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Semantic Caching

From [[llm-patterns]]: store previously computed LLM responses so future similar requests are served fast and cheap - the popularized form keys the cache on the embedding of the input request (e.g. GPTCache).

## Key points

- **Why:** cut latency (seconds -> milliseconds) and cost (avoid recomputing the same generation), and serve use cases that can't tolerate second-scale latency.
- **The danger:** caching purely on semantic similarity is "a disaster waiting to happen" - a request for "Mission Impossible 2" is similar enough to "3" that you can serve the wrong answer.
- **Cache safely instead:** key on item IDs, pairs of IDs, or constrained inputs (genre, director); precompute offline/async for anticipated queries; set a deliberate similarity threshold.
- **Check it fits the usage pattern:** caching pays off under a power-law request distribution (a few requests dominate), not uniformly-random traffic (measure the cache hit rate).

## Synthesis

Semantic caching is the cost/latency lever of the [[production-llm]] area, and its real lesson is a validation one: a cache is a correctness surface, so design it around when a stale-or-similar answer is actually safe, not around what is easy.
It connects to [[reasoning-effort-discipline]] and [[model-routing]] as the third big cost lever, and to [[engineering-trade-offs]] (caching trades consistency for speed/cost, acceptable only where the trade is safe).
