---
type: concept
tags: [agentic-engineering, planning, review, artifacts, ux]
status: developing
source-count: 3
last-updated: 2026-09-16
---

# Review Plans as Artifacts, Not Markdown

The technical scout in [[agentic-full-stack-build]] returned a **351-line `report.md`**.

Kun's objection has two halves, and the second is the one that matters:
it was a wall of text he didn't want to read, **and, more importantly, one he couldn't easily give targeted feedback on.**

So he had the review re-run as an interactive HTML artifact, where you can annotate any individual element, queue decisions, and view rendered architecture diagrams.

## Why it changes the outcome

- **Feedback becomes per-element instead of per-document.**
Writing "change section 4" against a 351-line file is a worse instrument than clicking the line and saying what's wrong with it.
- **Diagrams expose hidden requirements.**
Reading the architecture diagram is how he caught auditing and encrypted export being baked into the plan: "Otherwise we wouldn't have discovered that there are some hidden requirements being baked into the plan."
Those became scope cuts ([[agent-over-engineering]]).
- **It makes the decisions explicit and enumerable.**
Auth strategy, identity-table design, child sign-in, recovery approach, and the VPS-versus-SaaS cost call were all settled *in* the artifact rather than inferred from prose.
- He used the same mechanism for the front-end: real clickable HTML **wireframes** rather than a markdown file describing prototype scope.
His correction to the agent was explicit - "wireframes, not mocks" - which gets a playable prototype fast without inviting UI polish.

## The connection to actually reading it

This is the practical answer to a failure mode two other sources name.

[[designing-loops-and-workflows]] records that users get lazy, stop reading long AI-generated markdown plans, and just say "just do it," and that this backfires expensively.
[[read-what-the-agent-writes]] states the counter-practice as a discipline: don't exit the loop by skipping the plan.
[[building-products-with-agents]] (the same author) already used HTML artifacts for this.

The insight here is that **discipline is the wrong instrument.**
Telling yourself to read a 351-line report does not work reliably.
Changing the artifact so that reviewing it is faster than skipping it does.
HTML reports are used broadly at Anthropic for exactly this - plans, PRs, status reports, incident reports.

## Workflow reconstruction (2026-09-16)

[[kun-agentic-app-development-workflow]] combines architecture diagrams and explicit decisions with clickable user-flow prototypes before implementation.
The beginner reconstruction makes each component and authority boundary explainable, rather than treating an attractive artifact as an approval by itself.

## Synthesis

The general principle is that **as agents produce more output per unit of human attention, the format of that output becomes a first-class engineering decision.**
Markdown was fine when a human wrote the plan, because writing it was the expensive part and reading was cheap by comparison.
When the agent writes 351 lines in two minutes, reading is the bottleneck and the format has to be optimized for the reviewer.

This is [[defensive-ux]] turned inward - designing for the human being wrong, or tired, rather than the model.
It is also why [[production-watchdog]]'s "link out to the real UI" detail works: same principle, different artifact.

For hcho this maps onto a habit Mandu already has - PRDs, session summaries, recaps - and suggests the upgrade is delivery format rather than more documents.
The `recap.html` front door used for the Rep Today GTM package is already this pattern; the plans that are still long markdown are the ones getting skimmed.
