---
type: concept
tags: [system-design, architecture, agentic-engineering, context]
status: developing
source-count: 2
last-updated: 2026-08-05
---

# Monorepo for Agent Context

From [[building-robust-apps-with-ai]]: start a new app as a single monorepo (Ross uses Turborepo) holding every client, the unified backend, all services, and a shared component library - primarily so the AI agent gets the entire codebase as context at once.

## Key points

- Fragmented, separate repos create separated contexts that are hard for both the human and the agent to hold; one repo removes that friction.
- One unified backend and one shared UI library can serve all client surfaces (Pluto: web, mobile, desktop, admin).
- Ross "almost always starts a new app with a monorepo" for this reason.
- [[running-life-on-codex]] shows the non-code version of the same instinct: [[jason-openai-codex]] keeps almost all his context in a single [[obsidian]] markdown vault ("basically his only project"), organized into projects / people / notes / daily notes / preferences, with other repos originating from it. Same principle - **one place the agent can see all the context at once** - applied to a life/work knowledge base rather than a codebase. He rarely opens it himself; it exists to feed the agent.

## Synthesis

This is [[context-is-king]] applied to repository layout: the agent's output quality is bounded by the context it can see, so structure the codebase to maximize what one agent can hold at once.
It connects the [[system-design]] area to the context-engineering thread that runs through the workflow sources - full-codebase context is why an agent can make coherent cross-cutting changes rather than locally-correct, globally-wrong ones.
A trade-off ([[engineering-trade-offs]]) like any other: monorepos cost build-tooling complexity, bought here for agent legibility.
