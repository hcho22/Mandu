---
type: entity
tags: [person, agentic-engineering, tooling, solo-builder]
status: developing
source-count: 5
last-updated: 2026-10-14
---

# Kun

**Kun Chen.** Principal engineer (L8), ex-Meta, Microsoft, and Atlassian; builder of a small stack of open agent tooling.
GitHub handle and personal domain: **kunchenguid** (`github.com/kunchenguid`, `blog.kunchenguid.com`).

**Identification note:** the wiki previously recorded this person only as "solo L8 builder" in [[building-products-with-agents]].
[[agentic-full-stack-build]] named him as **Kun**, and [[agents-md-is-a-neural-net]] - a first-party blog post rather than an auto-captioned transcript - supplies the full name **Kun Chen** and the previously-missing identifiers (`blog.kunchenguid.com`, and the `kunchenguid/backpass` repo).
The earlier caution about not guessing them is now resolved by a byline, not an inference.

## His tools

- **First Mate** - his open-source orchestrator. You (the "captain") talk to exactly one agent, which dispatches work to "crewmates." See [[one-orchestrator-agent]].
- **Lavish** - renders plans as interactive HTML artifacts with per-element annotation and rendered diagrams. See [[review-plans-as-artifacts]]. Reused as the human-review surface in backpass.
- **No Mistakes** - a local validation pipeline that runs against every code change. He needs it precisely *because* he does not review code himself.
- **backpass** - an MIT CLI that trains a project's `AGENTS.md` from agent session transcripts, one gradient step per run. See [[backpass]].

## What shows up in the wiki

**From [[building-products-with-agents]] (the principles):**
[[get-out-of-the-loop]], [[plan-code-validate]], [[fresh-context-review]], [[phased-implementation]].

**From [[agentic-full-stack-build]] (the principles executed end to end):**
[[one-orchestrator-agent]], [[review-plans-as-artifacts]], [[anchor-cost-in-real-pricing]], [[agent-over-engineering]], [[compaction-over-context-window]], [[define-the-end-to-end-gate]], [[design-system-not-a-design]], [[ramble-then-structure]], [[credential-vaults]].

**From [[agents-md-is-a-neural-net]] (configuring the agent, not building with it):**
[[agents-md-as-neural-net]], [[two-level-agent-memory]], [[four-bad-memory-states]], [[skills-as-release-valve]], and the tool [[backpass]].
This is his first source that is purely about **maintaining the agent's memory** rather than shipping a product with it, and it is the one that most directly reaches hcho's own Mandu configuration.

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

## Local workflow reconstruction (2026-09-16)

[[kun-agentic-app-development-workflow]] is an uncredited local reconstruction of four talks attributed to Kun, with beginner prompts and checklists supplied by the compiler.
It connects his build practice to reproducible workstation configuration, project-scoped Second Mates, and proportional review.
This is a fourth cataloged source associated with Kun, not a fourth independent primary source; exact overlap and talk dates are unavailable.
See [[reproducible-agent-environment]] and [[risk-based-agent-governance]].

## Merged with John's practice (2026-10-14)

[[agentic-coding-workflow-idea-to-review]] is a third-order playbook that combines the reconstruction above with [[john-meta-engineer]]'s two talks.
It casts Kun as working "from the front" (intent, research, visual architecture review, contracts, orchestration) and John "from the back" (gates, proof, independent review, review depth by risk).
On reading code the two disagree: Kun's position, as reported, is that reading every diff makes you the bottleneck, while John reads more code than before.
Its compiler verified that **No Mistakes** is public at `github.com/kunchenguid/no-mistakes` (`no-mistakes init`, then `git push no-mistakes` runs review, tests, docs, and lint in a disposable worktree before opening a PR) and marked his other tools unverified.
Mandu's observation: those other tools are in hcho's own environment (First Mate as his firstmate home, Lavish, Treehouse worktrees, and the No Mistakes skill), so their existence is not in doubt for him; their behavior was not tested here.
This adds a cataloged source about Kun, not a new primary one.
