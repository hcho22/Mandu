---
type: concept
tags: [agentic-engineering, prompting, context-engineering, method, anthropic]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# Ablation-Driven Development

Delete your entire prompt layer, use the product against the new model, and add back **only** what repeatedly fails.

Named from the research term by [[boris-cherny]] in [[building-at-the-frontier]].
The distinction he draws is precise: **an eval measures; an ablation removes things to measure.**
You bring the deleted material back **line by line** to see what each line actually contributes.

## The loop

1. **Delete.** The whole system prompt, the `CLAUDE.md`, the skills, the hooks.
2. **Use it.** Run the real product or your real codebase against the new model.
3. **Observe** where it does well and where it stumbles.
4. **Add back only what repeatedly fails** - the same failure, seen more than once.

## Key points

- **Don't guess what the model needs.** You will predict wrong. The method exists because prediction fails.
- **Don't add too early.** Every instruction is re-read on *every* invocation, so it has to earn its token cost.
- Anthropic runs this internally with an undocumented "simple mode" (`CLAUDE_CODE_SIMPLE=1`) that strips all system prompts including tool prompts.
- **The surprising finding:** with the prompts removed, Claude Code's model is *slightly more intelligent*.
The prompts ship anyway because they make the tool behave like a coherent product for a human - a product decision, not a capability one.
- Asked whether every AI-product builder should ablate on every model release and be brave enough to delete: **"100%."**
- **For users, not just builders:** every six months delete your `CLAUDE.md`, your skills, and your hooks and see what happens.
- The frequency is set by model releases, not by a calendar. Every new model invalidates the last model's corrections.

## Relationship to [[principles-over-constraints]]

These are the finding and the method for it.
[[principles-over-constraints]] records *that* Anthropic cut the Claude Code system prompt by 80% and *that* smarter models need less direction.
This page records *how you find out which 80%*, on your own product, without waiting for Anthropic to tell you.
Before this source the wiki had the conclusion without a procedure, which made it advice rather than practice.

## Synthesis

This is the sharpest available answer to a question the wiki has been circling: what do you actually *do* when a new model ships?
The honest answer is that most accumulated prompt engineering is **debt written against a model that no longer exists**, and the only reliable way to find the debt is to zero the balance and let the failures re-accumulate.

For hcho this cuts two ways.
It argues against over-investing in elaborate `CLAUDE.md` files and skill libraries, including in Mandu itself - a system tuned for one model generation quietly becomes a tax on the next.
But it also plays directly to a validation background: ablation *is* controlled experimentation, one variable at a time, with the discipline to trust the observation over the prior.
That is closer to hardware bring-up than to software engineering, and it is a rare thing to already know how to do.

The tension worth watching is with [[building-skills]] and [[self-updating-config]], which treat accumulated instructions as a compounding asset.
Boris's position is that they compound only until the next model, and that most people never pay the debt down.
See also [[evals-saturate-and-get-replaced]], which makes the same argument about the artifact everyone assumes is durable.

## The complement: the weekly gradient step (2026-08-27)

[[agents-md-is-a-neural-net]] ([[kun]]) is the other half of this method rather than a competitor to it.
Both are anti-bloat, evidence-driven, and budget-respecting; they differ in **cadence and step size**.
Ablation is a periodic full reset keyed to **model releases** - zero the whole prompt layer and let only repeated failures re-accumulate, because a new model invalidates the last one's corrections.
The backward pass ([[backpass]]) is a **weekly small step** keyed to **transcript loss** - nudge a handful of units on the model you have now, using the sessions that actually ran as the gradient.
Read through [[agents-md-as-neural-net]], they are the same picture at two timescales: ablation is the occasional full retrain, backpass is the ongoing gradient descent between retrains.
This partly answers the tension above - instructions are neither pure asset nor pure debt but **weights**, kept within a fixed capacity and retrained on two clocks - though Boris's stronger claim stands, that most accumulated configuration is debt against a model that no longer exists and only a delete-to-zero reliably surfaces it.
