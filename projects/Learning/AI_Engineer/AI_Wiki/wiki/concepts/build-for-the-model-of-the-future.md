---
type: concept
tags: [ai-career, architecture, strategy, agents]
status: seed
source-count: 2
last-updated: 2026-07-08
---

# Build for the Model of the Future

The principle that you should design agentic applications for the model that will exist *next*, not today's, because each model generation unlocks the previously impossible.

## Two sources

- [[ai-era-50-career-tips]] (via Boris Cherny, [[boris-cherny]]): Claude Code was built assuming future models would catch up to its features; building only for current models is easy to copy and limits your thinking.
- [[production-agent-with-cma]]: Claude Managed Agents let you "skate the exponential" - auto-benefit from each new model family without re-architecting.

## Key points

- Design headroom for capability you cannot yet rely on, so improvements land for free as models improve.
- Choose infrastructure/abstractions that decouple your product from a specific model generation.

## Synthesis

This is a bet on the derivative, not the level: the leverage is building where the trend is going.
It pairs with [[phased-autonomy]] and [[plan-code-validate]] (widen scope as capability arrives) and gives hcho an architecture principle for the Agentic RAG flagship - build the harness and evals so a stronger model upgrades the product without a rewrite.
