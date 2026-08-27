---
type: concept
tags: [claude-code, config, self-improvement, agentic-engineering, agents-md]
status: developing
source-count: 2
last-updated: 2026-08-27
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

## The rigorous version (2026-08-27, [[agents-md-is-a-neural-net]])

[[kun]]'s "train your `AGENTS.md` like a neural net" is the same loop as Pigford's learnings-skill, made disciplined and given a shipped tool ([[backpass]]).
It supplies exactly what the seed version left implicit - *how* to update without bloating - via the [[agents-md-as-neural-net]] framing: the file is the weights, the budget is the model size, every session is a forward pass, the loss lives in the transcripts, and reading them to make edits is the backward pass.

Four constraints turn "mine the corrections" into a method that does not degrade the file:

- **Verbatim-quote evidence only.** The loss signal is the actual session logs, not recollection; a proposed edit without a quote is discarded in code, not by a prompt.
- **Batch before you update.** One bad session is noise; only a batch (his default: two sessions minimum) reveals a real pattern. This is the single constraint that removes most bloat, because most pasted-in rules were one-incident reactions.
- **Small steps under an explicit budget.** About five edits per pass, and near the budget every addition names the removal or extraction that pays for it, with [[skills-as-release-valve|skills as the release valve]].
- **A human gate writes.** Nothing commits until a person accepts each edit; rejections are remembered.

It also widens the input: Pigford's skill reads the chat you just had, while backpass reads the transcript stores across every harness (Claude Code, Codex, pi, opencode, grok, Cursor) and ties each session to the repo.

## Synthesis

This closes the loop on [[context-is-king]] and [[building-skills]]: the system does not just consume context, it curates its own.
It is a specific, high-value automation for an [[ai-operating-system]] and a natural extension of [[phased-autonomy]] (the config earns trust as its rules prove out).

With the second source the concept also finds its place in the wiki's sharpest tension.
[[ablation-driven-development]] treats accumulated instructions as debt to be zeroed on a model release; this page treats them as an asset to be grown.
[[agents-md-as-neural-net]] reconciles the two: instructions are **weights**, trained continuously within a fixed budget - ablation is the periodic full retrain, the backward pass is the weekly gradient step, and both are anti-bloat and evidence-driven rather than opposed.
Directly reusable for hcho: a learnings skill that mines correction history is a small, portfolio-worthy piece of agentic engineering, and [[backpass]] is a ready pattern to run against Mandu's own long configuration.
