---
type: concept
tags: [architecture, design, taste, agentic-engineering]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Don't Let AI Be Your Architect

The design principle from [[inside-conductor-workflow]]: humans own the architecture, the APIs/contracts, and the interface; the AI gets free rein only in clearly separated, non-core areas.

## Key points

- The team thought through the core concepts themselves (the "workspace" abstraction, the three-pane layout); AI-made UI choices tend not to feel "crafted."
- Build the core around human-written APIs/contracts the AI does not touch much; give it freedom only where experiments cannot damage core infrastructure.
- Conviction comes from dogfooding and gut feel, not analytics.

## Synthesis

This is the architecture-scale statement of [[own-the-problem-not-the-code]] and the design-scale companion to [[slop-free-zones]]: keep human judgment on the decisions that shape everything downstream.
It refines [[get-out-of-the-loop]] with a boundary - delegate the code, keep the architecture - and is [[taste-as-moat]] applied to system design.
For hcho, "own the architecture and the evals, delegate the implementation" is a crisp way to describe a validation-led builder.
