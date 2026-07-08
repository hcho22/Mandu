---
type: concept
tags: [claude-code, context-engineering, workflow]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Checkpoint Rewind

The practice, from [[every-claude-feature-ranked]], of rolling both code and conversation back to an earlier checkpoint (`/rewind`) when the agent goes wrong, rather than piling corrections on top.

## Key points

- You pick the exact prompt in the conversation to return to; both the code and the context are restored.
- Because everything is cached and reloaded, rewinding keeps the context clean, whereas "no, that was wrong, do it this way" appends noise.

## Synthesis

This is a direct countermeasure to [[context-rot]]: a wrong turn plus corrections bloats and biases the context, while a rewind removes the bad branch entirely.
It complements the save-point role of worktrees in [[phased-implementation]] - both treat state as revertible rather than something you talk your way out of.
