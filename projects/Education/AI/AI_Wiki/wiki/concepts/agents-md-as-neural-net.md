---
type: concept
tags: [agentic-engineering, agents-md, claude-md, context-engineering, self-improvement, method]
status: developing
source-count: 1
last-updated: 2026-08-27
---

# AGENTS.md as a Neural Net

The framing from [[agents-md-is-a-neural-net]] ([[kun]]): a project-level agent memory file (`AGENTS.md` / `CLAUDE.md`) is not a document you edit, it is a set of **weights** you train.
It loads into the system prompt of every session that runs on the project and steers behavior before the agent reads a line of code, "not too differently from a fine-tuned LoRA on top of the model you use."
So the right operation on it is not editing but **gradient descent**: decide a size budget, then train the weights against the loss the sessions actually produced.

## The mapping

| Training concept | Its agent-memory counterpart |
|---|---|
| Weights | The project `AGENTS.md` - what determines behavior before any code is read |
| Model size | The token **budget** - larger holds more knowledge but costs more on every invocation |
| Forward pass | Every agent **session** - the file loads, the agent works, the file is not touched |
| Loss | The gap between what the agent did and what you wanted (rediscovered the schema, ran `npm test` in a pnpm repo, violated a rule that was right there, followed a rule that was wrong) |
| Backward pass | **Reading the transcripts and updating the file** - work out which units caused the loss, which earned their keep, and make small budgeted edits that reduce it |

## Why this is the missing half

Most people only ever run the **forward pass**: they use the memory file in every session and never refine it against loss.
The backward pass is skipped because it is tedious - finding the transcripts, reading megabytes of tool-call noise, keeping quotes honest, counting tokens - which is exactly the part a tool should do ([[backpass]]).
The loss signal already exists: every harness (Claude Code, Codex, pi, opencode, grok, Cursor) writes a transcript of what was asked, what the agent did, which rule it followed, which one tripped it, and what it had to rediscover.
Nobody reads those logs, so the data that would tell you what to change is sitting unused.

## Two details from real training that carry over

- **You do not update on a single example.** One session can be noisy, so you **batch** before you update. This is the constraint that removes most bloat, because most pasted-in rules were reactions to one incident that never recurred.
- **The network has a fixed size.** A bigger file holds more knowledge but is more costly at inference, which is why the budget has to be explicit and every addition is zero-sum against a removal near the limit. See [[skills-as-release-valve]].

Small steps, not one big rewrite: a large step on a memory file is indistinguishable from starting over, and you lose everything that was working. This is the learning rate.

## Why the shape is right

The metaphor also leans into reality: most people will not carefully read their `AGENTS.md` very often, so it is already a black box in practice - which is precisely how you treat a set of weights.
What makes the method more than "ask an agent to clean up this file" is the rigor it imports from training: real transcripts as the only input, verbatim quotes as the only admissible evidence, a fixed budget, a small step size, a minimum batch, and a human gate that writes.

## Synthesis

This is the wiki's sharpest available answer to a question it has been circling: *what do you actually do with your accumulated instructions over time?*
It reframes the standing tension in [[agentic-engineering]] - do instructions compound as an asset ([[building-skills]], [[self-updating-config]]) or accrue as debt ([[ablation-driven-development]])?
The answer here is neither: they are **weights**, and weights are neither kept forever nor deleted wholesale - they are trained continuously within a fixed capacity.
That makes this the operational middle between [[self-updating-config]] (which had the idea but not the discipline) and [[ablation-driven-development]] (which resets the whole file on a model release rather than nudging it weekly from loss).
The two are complementary tools on the same debt: ablation is the periodic full retrain keyed to a new model; the backward pass is the small gradient step keyed to the transcripts of the model you have now.

For hcho this is immediately reflexive.
Mandu's own `CLAUDE.md` and long skill files are exactly the "weights trained transactionally from anecdotes" this page warns about, and the same [[looking-at-your-data|read-your-own-traces]] instinct that runs the eval spine is what the backward pass asks for, pointed at session logs instead of product traffic.
The budget discipline it forces is also the honest version of the [[principles-over-constraints]] advice the wiki already holds: "keep it short" becomes "keep it under an explicit token budget, and pay for every addition."
