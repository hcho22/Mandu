---
type: concept
tags: [agentic-engineering, scope, failure-mode, architecture]
status: developing
source-count: 1
last-updated: 2026-08-01
---

# Agent Over-Engineering

Agents invent requirements you never asked for, and cutting them is where the human still adds value.

From [[agentic-full-stack-build]], where this was one of only three interventions needed across an entire full-stack build.

## The recurring inventions

- **Environment tiers.** The implementation plan proposed deploying a *development* backend alongside production.
Kun cut it: one production MVP environment, no dev/prod split.
For a new app on a VPS nobody knows about, there is no reason for environment tiers.
- **Audit events.** Baked into the architecture plan unasked; deleted as over-engineering for the initial scope.
- **Encrypted export.** Same - deleted.
- **Point-in-time recovery.** Replaced with daily backups plus a nightly export.

His note on the pattern: **GPT models, especially 5.6, have a tendency to over-engineer.**

## Why it's hard to catch

These are all *defensible* features.
Audit trails, environment tiers, and encrypted export are things a competent engineer would build for a real production system, which is precisely why they slip past review - nothing about them looks wrong in isolation.

They are only wrong **relative to the scope**, and scope is the thing the agent infers rather than knows.
Kun caught them by **reading the architecture diagram**, not the prose: "Otherwise we wouldn't have discovered that there are some hidden requirements being baked into the plan."
See [[review-plans-as-artifacts]].

## Synthesis

Pair this with [[anchor-cost-in-real-pricing]] and a clear picture emerges of what the human still does when they have stopped reading code entirely.
Across a whole session - market research, technical planning, backend, infra, design system, iOS app - the interventions were **one cost error and one scope class**.
Neither is a correctness problem.
Both are judgment about *how much system this situation deserves*, which is the thing the agent cannot infer because it depends on facts outside the repo: three users, no revenue, nobody knows the VPS exists.

That is the sharpest available answer to "what is the human for," and it is more specific than [[own-the-problem-not-the-code]] or [[dont-let-ai-be-your-architect]] manage.
Those pages say humans own architecture; this says the ownership is exercised almost entirely as **subtraction**.

It also complicates [[get-out-of-the-loop]] usefully.
Getting out of the loop on implementation is well-evidenced.
Getting out of the loop on *scope* is not, and the same author who most aggressively delegates code review is the one manually deleting invented requirements.

There is a tension with [[engineering-trade-offs]] worth flagging: dev/prod tiers and audit trails are legitimate reliability investments, and cutting them is right at three users and wrong at three thousand.
The judgment is not "agents over-engineer, so cut" but "agents cannot see your stage, so you have to."
