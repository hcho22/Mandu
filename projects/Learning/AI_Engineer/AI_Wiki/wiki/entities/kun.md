---
type: entity
tags: [person, agentic-engineering, tooling, solo-builder]
status: developing
source-count: 2
last-updated: 2026-08-01
---

# Kun

Principal engineer (L8), ex-Meta, Microsoft, and Atlassian; builder of a small stack of open agent tooling.

**Identification note:** the wiki previously recorded this person only as "solo L8 builder" in [[building-products-with-agents]].
[[agentic-full-stack-build]] names him as **Kun**, and the two sources are the same author.
His GitHub handle and personal domain were not recoverable from that source's auto-captions and are deliberately not guessed here.

## His tools

- **First Mate** - his open-source orchestrator. You (the "captain") talk to exactly one agent, which dispatches work to "crewmates." See [[one-orchestrator-agent]].
- **Lavish** - renders plans as interactive HTML artifacts with per-element annotation and rendered diagrams. See [[review-plans-as-artifacts]].
- **No Mistakes** - a local validation pipeline that runs against every code change. He needs it precisely *because* he does not review code himself.

## What shows up in the wiki

**From [[building-products-with-agents]] (the principles):**
[[get-out-of-the-loop]], [[plan-code-validate]], [[fresh-context-review]], [[phased-implementation]].

**From [[agentic-full-stack-build]] (the principles executed end to end):**
[[one-orchestrator-agent]], [[review-plans-as-artifacts]], [[anchor-cost-in-real-pricing]], [[agent-over-engineering]], [[compaction-over-context-window]], [[define-the-end-to-end-gate]], [[design-system-not-a-design]], [[ramble-then-structure]], [[credential-vaults]].

## Why he's a useful source

The second source is close to a **natural experiment** on what the human still does.
He built an entire full-stack app - market research, technical planning, backend, infrastructure, design system, native iOS app, deployed on a real VPS with real Apple sign-in - **without reading source code**, on a non-frontier model (GPT-5.6 Luna), using Sonnet rather than Opus for design.

Across that whole session he needed exactly **two** interventions: a cost estimate anchored in stale pricing data, and a class of invented scope (dev/prod tiers, audit events, encrypted export).
Neither is a correctness judgment.
Both are judgments about *how much system this situation deserves*, which is a sharper account of the human's remaining role than most sources manage.

## Positions worth knowing

- **"You don't really need the best model for everything."** He deliberately picked a harder, more uncertain model to make the session more honest.
- **Watching tool calls is obsolete.** He runs a "calm mode" hiding all tool calls; useful with weaker models, now just noise.
- **Compaction is an implementation detail.** Four auto-compactions with no visible degradation, which the wiki records as a live tension with [[context-rot]].
- **Give the agent broad permissions, gate production explicitly.** "As we delegate more and more things to agents, this is going to become more and more important."

## Notes

The wiki's best-documented single build session, and the closest thing it has to a controlled test of [[agentic-engineering]] practice.
Complements [[ryan-carson]] (who runs many agents and schedules his own attention) with the opposite ergonomic answer: many agents, **one** human interface.
