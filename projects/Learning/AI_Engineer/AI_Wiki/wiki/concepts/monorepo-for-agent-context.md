---
type: concept
tags: [system-design, architecture, agentic-engineering, context]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Monorepo for Agent Context

From [[building-robust-apps-with-ai]]: start a new app as a single monorepo (Ross uses Turborepo) holding every client, the unified backend, all services, and a shared component library - primarily so the AI agent gets the entire codebase as context at once.

## Key points

- Fragmented, separate repos create separated contexts that are hard for both the human and the agent to hold; one repo removes that friction.
- One unified backend and one shared UI library can serve all client surfaces (Pluto: web, mobile, desktop, admin).
- Ross "almost always starts a new app with a monorepo" for this reason.

## Synthesis

This is [[context-is-king]] applied to repository layout: the agent's output quality is bounded by the context it can see, so structure the codebase to maximize what one agent can hold at once.
It connects the [[system-design]] area to the context-engineering thread that runs through the workflow sources - full-codebase context is why an agent can make coherent cross-cutting changes rather than locally-correct, globally-wrong ones.
A trade-off ([[engineering-trade-offs]]) like any other: monorepos cost build-tooling complexity, bought here for agent legibility.
