---
type: concept
tags: [claude-code, config, self-improvement, agentic-engineering]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Self-Updating Config

The practice from [[building-5-ai-products-solo]] of having an AI improve its own instruction file automatically.
Josh Pigford's "learnings skill," run after a phase ships, reviews the worktree plus the actual chat transcript - including the repeated corrections he had to give - and distills them into additions to `CLAUDE.md`, so the config keeps the model from repeating mistakes.

## Key points

- The signal is the **correction history**: what the human had to fix or re-explain becomes a durable rule.
- Runs after shipping, so lessons are captured while fresh.
- Result is a continuously improving config rather than a static, hand-maintained one.

## Also a native feature

[[every-claude-feature-ranked]] describes Claude Code's **auto-memory** ("auto-dream"): at intervals Claude searches back over your sessions and updates its own memory unprompted - the platform version of the learnings-skill pattern.

## Synthesis

This closes the loop on [[context-is-king]] and [[building-skills]]: the system does not just consume context, it curates its own.
It is a specific, high-value automation for an [[ai-operating-system]] and a natural extension of [[phased-autonomy]] (the config earns trust as its rules prove out).
Directly reusable for hcho: a learnings skill that mines correction history is a small, portfolio-worthy piece of agentic engineering.
