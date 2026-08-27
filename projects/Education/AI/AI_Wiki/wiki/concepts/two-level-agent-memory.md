---
type: concept
tags: [agentic-engineering, agents-md, claude-md, context-engineering, method]
status: seed
source-count: 1
last-updated: 2026-08-27
---

# Two-Level Agent Memory

The rule from [[agents-md-is-a-neural-net]] ([[kun]]): agent memory files exist at two levels that deserve **opposite** treatment.

## The two levels

- **The user-level file is yours, and you handwrite it.**
Your global `~/.claude/CLAUDE.md` or `~/AGENTS.md` holds your preferences and opinions - prefer quality over development cost, reproduce a bug end-to-end before fixing it, fix the flaky test you walked past even if it is not yours.
These are preferences you own, they change rarely, and no tool or agent should "optimize" them.
This file is small and written by hand, on purpose.

- **The project-level file is a neural net, and you train it.**
It loads into the system prompt of sessions that run on the project and steers the agent's behavior in that repo.
Instead of editing it like a document, you give it a token budget and train it on the sessions that actually ran ([[agents-md-as-neural-net]]).

## Why the split matters

The two files fail differently, so they need different maintenance.
The user file's risk is that someone or some tool edits your own preferences out from under you; the fix is that only you touch it.
The project file's risk is [[four-bad-memory-states|bloat, staleness, and drift]] from transactional editing; the fix is budgeted, evidence-driven training.
Automated self-improvement ([[self-updating-config]], [[backpass]]) is aimed squarely at the **project** level - it should never rewrite the preferences you hand-authored.

This also explains a failure the wiki records elsewhere as **drift**: when `AGENTS.md` and `CLAUDE.md` disagree, or each harness gets a different set of instructions, it is usually because project-level and user-level content got mixed into the same file with the same (wrong) maintenance habit.

## Synthesis

A small, clean boundary that sharpens the wiki's self-improvement pages.
[[self-updating-config]] and the auto-memory it describes are powerful precisely because they run on the project level, where the correction history is the training signal; pointing the same automation at your hand-written preferences would be a category error.
For hcho the mapping is direct: `~/.claude/CLAUDE.md` (the global instructions that open every Mandu session) is the handwritten user file and should stay short and stable, while each project's `AGENTS.md` - and Firstmate's own - is a trainable net whose budget and loss are worth managing deliberately.
It pairs with [[principles-over-constraints]] (the user file is where principles live) and [[capabilities-not-instructions]] (neither file is where safety should live - remove the key, do not write the rule).
