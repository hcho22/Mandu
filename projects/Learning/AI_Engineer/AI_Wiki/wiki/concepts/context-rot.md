---
type: concept
tags: [context-engineering, agents, craft]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Context Rot

The degradation in an agent's reliability as its context window fills with accumulated, increasingly noisy history, named in [[building-5-ai-products-solo]] as a driver of hallucination.

## Key points

- A long-running session accumulates stale detail; the model hallucinates more as the signal-to-noise of its context drops.
- Mitigation: start each unit of work with **fresh context** (a new git worktree per phase; a clean session), carrying only a compact progress/decisions file forward.
- This is the operational reason behind [[phased-implementation]]'s fresh-worktree-per-phase rule.
- Two practical tools from [[every-claude-feature-ranked]]: watch a **status line** (model, effort, context %) to know when to `/clear` or `/compact`, and prefer [[checkpoint-rewind]] over piling corrections onto a wrong turn.

## Synthesis

Context rot is the failure mode that [[context-is-king]] guards against from the other side: not just "give good context," but "keep context clean."
It motivates practices across the wiki - [[fresh-context-review]], fresh graders in the [[skill-eval-loop]], [[sub-agents]] that return only conclusions, session-handoff skills in [[building-skills]], and per-phase worktrees - all of which trade accumulated context for reliability.
