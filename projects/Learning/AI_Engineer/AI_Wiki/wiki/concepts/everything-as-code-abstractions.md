---
type: concept
tags: [system-design, infrastructure, agentic-engineering, abstraction]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Everything-as-Code Abstraction Layers

From [[building-robust-apps-with-ai]]: the modern stack is a rising stack of abstraction layers that hide hard infrastructure, and the newest layer has a second property that matters for AI - it is "everything-as-code," so agents already know how to operate it.

## The history (layers of abstraction)

- **Own metal** - physical server racks in-office; expensive, hard to predict/scale, risky either way. Not recommended today.
- **Cloud providers** - AWS, GCP, Azure, Cloudflare rented out the metal; the web exploded, but developer (and agent) experience is poor.
- **The higher abstraction layer** - Convex, Vercel, Supabase, Neon, PlanetScale wrap the cloud with excellent developer/agent experience and easy scaling.

## Why it matters for agents

- Because these platforms are configured entirely in code, an agent can build features end-to-end against them - the abstraction is the reason [[agentic-engineering]] on production infra is even possible.
- Convex components are the extreme case: find the component you need (Workflow, Workpool, R2, Autumn), copy its link, hand it to the agent, and it integrates - a non-technical builder can ask in plain English.

## Synthesis

This concept explains *why* the agentic-build workflows elsewhere in the wiki work at all: agents are fluent on everything-as-code platforms and helpless on click-through consoles.
It is the infrastructure counterpart to [[code-as-sawdust]] - if code is regenerable, the durable choices are which platforms you build on and how you wire them, which is [[engineering-trade-offs]] and [[system-design]].
The caution ([[dont-let-ai-be-your-architect]]) still holds: the agent can operate the layer, but choosing the layer and its trade-offs stays human.
