---
type: concept
tags: [ai-career, architecture, strategy, agents]
status: established
source-count: 3
last-updated: 2026-08-01
---

# Build for the Model of the Future

The principle that you should design agentic applications for the model that will exist *next*, not today's, because each model generation unlocks the previously impossible.

## Two sources

- [[ai-era-50-career-tips]] (via Boris Cherny, [[boris-cherny]]): Claude Code was built assuming future models would catch up to its features; building only for current models is easy to copy and limits your thinking.
- [[production-agent-with-cma]]: Claude Managed Agents let you "skate the exponential" - auto-benefit from each new model family without re-architecting.

## Key points

- Design headroom for capability you cannot yet rely on, so improvements land for free as models improve.
- Choose infrastructure/abstractions that decouple your product from a specific model generation.

## From its author, with a procedure attached (2026-08-01)

[[building-at-the-frontier]] is [[boris-cherny]] stating his own principle directly, and it converts an aspiration into three concrete practices:

- **Keep re-throwing your standing hard problem at each new model.** The previous one failing says nothing about the next one. This is how the Bun Zig-to-Rust rewrite happened - a test re-run every generation until one passed ([[long-horizon-agent-runs]]).
- **Delete what you built for the last model.** [[ablation-driven-development]] is the maintenance cost of this principle: designing for the future model also means removing the corrections you wrote for the past one, or they hobble the new one ([[product-overhang]]).
- **Give the model tasks slightly harder than you think it can handle**, and play with no commercial goal.

The claim underneath is that headroom is not speculative: **dozens to hundreds of undiscovered elicitations exist in today's models already.**
So "build for the model of the future" is partly a misnomer - a lot of the future capability is present now and unclaimed.

The caution attached is [[evals-saturate-and-get-replaced]]: if you build for the next model, expect the evals proving today's version works to have a one-to-three-generation half-life.

## Synthesis

This is a bet on the derivative, not the level: the leverage is building where the trend is going.
It pairs with [[phased-autonomy]] and [[plan-code-validate]] (widen scope as capability arrives) and gives hcho an architecture principle for the Agentic RAG flagship - build the harness and evals so a stronger model upgrades the product without a rewrite.

The third source makes it operational rather than aspirational.
The practice is **keeping a list of things the model recently could not do and re-testing it every release**, which costs almost nothing and is the only way to notice when a limitation stops being one.
Most people file failed attempts as settled facts; that is the specific mistake this principle guards against.
