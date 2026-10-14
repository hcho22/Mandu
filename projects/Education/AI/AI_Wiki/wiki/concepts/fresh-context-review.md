---
type: concept
tags: [validation, code-review, context-engineering, evals]
status: developing
source-count: 6
last-updated: 2026-10-14
---

# Fresh-Context Review

The principle from [[building-products-with-agents]] that AI-generated work should be reviewed in a **fresh context window**, because a reviewer that saw every step of the work is biased toward believing it is correct and misses edge cases.

## Key points

- The No Mistakes pipeline reviews each change in a clean context, with an "Intent" phase that hands the fresh reviewer just enough context - like a principal engineer reviewing with fresh eyes after a brief explanation.
- Same-session self-review underperforms because the model already "believes" its work.
- The reviewer is heavily prompt-engineered for high recall on bugs, logical errors, and edge cases, and presents test evidence (screenshots/video).

## Fresh context is half the fix ([[designing-loops-and-workflows]])

An Anthropic [[claude-code]] team member names the same effect as [[self-referential-bias]] and prescribes varying **two** things, not one: the verifying agent should have different context *and* a different model from the producing agent.

That distinction matters for this page.
Clearing the context window removes the reviewer's *belief* that the work is correct, which is what this page's original source identified.
It does not remove the model's *preference* for its own style of output, which the eval literature measures directly ([[llm-as-judge]]: GPT-4 about +10%, Claude-v1 about +25% self-win rate).
Fresh context is therefore necessary but not sufficient, and the fuller prescription is three roles with different context and different models: one coordinating, one doing, one verifying.

## Workflow reconstruction (2026-09-16)

[[kun-agentic-app-development-workflow]] separates the first implementation from review against original intent, real integration evidence, documentation, and a risk decision.
The reconstruction reinforces the method but is overlapping secondary material, not another independent experiment.

## Review handoff (2026-09-23)

[[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] specifies a practical handoff: original requirements, current diff, necessary project context, and evidence for the current revision.
A new reviewer supplied the entire implementation conversation may inherit the same assumptions despite being a separate agent.
This guide adds a usable procedure, not an independent measurement of bias reduction.

## "The agents will cheat" (2026-10-14)

[[agentic-code-review-strategies]] gives the practitioner's version of the bias in four words.
[[john-meta-engineer]] calls a reviewer without the producing context an **adversarial review agent**, a new sub-agent or separate agent, because one that helped write the code leans on the earlier conversation and grades it accordingly.
He pairs it with the default review tools ([[claude-code]]'s `/code-review`, [[codex]]'s reviewer) rather than a custom one, plus a PR template so the reviewer sees the same structure every time ([[proof-in-the-pr]]).
This is most likely the same talk as the 2026-09-23 guide, so it names the speaker rather than adding an independent measurement.

## Layered, so the builder never grades itself (2026-10-14)

[[agentic-coding-workflow-idea-to-review]] stacks three independent reviews: a fresh-context agent before the PR opens (Kun's No Mistakes pipeline, or a reviewer subagent), an AI reviewer on GitHub (John's Codex bot), and a human at the depth the risk tier sets.
Its reviewer prompt opens "You did not write this change" and hands over the task's requirement and the architecture doc rather than the conversation, which is the handoff this page's 2026-09-23 section describes.
The layering is the compiler's design; the sources it merges each supply one or two of the layers.

## Synthesis

This is the unifying principle beneath several earlier pages: it is why the [[skill-eval-loop]] runs its grader in a separate agent, why [[context-rot]] motivates fresh sessions, and what makes [[adversarial-code-review]] work (a different model, or a fresh context, does not share the original's blind spots).
It is the strongest single import for hcho: "review in fresh context" is a concrete, teachable validation technique, and productizing it (as No Mistakes does) is exactly the automated-reviewer artifact that [[get-out-of-the-loop]] requires.
With the second source, the technique's mechanism is now named and generalized in [[self-referential-bias]]: this page is the context-variable case of that broader constraint, and the practical upgrade is to vary the model too wherever the check actually matters.
