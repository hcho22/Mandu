---
type: concept
tags: [testing, evals, agents, e2e, validation]
status: developing
source-count: 4
last-updated: 2026-10-14
---

# Agent Testing Instructions

The practice from [[building-products-with-agents]] of writing explicit end-to-end testing instructions in `AGENTS.md` (or `CLAUDE.md`), because agents default to shallow, code-only unit tests that do not validate behavior.

## Key points

- Write the instructions as "how I would test this myself": drive the real app (e.g. an Electron desktop app via a browser), take screenshots, check for console errors.
- Turn recurring core flows into automated E2E tests (e.g. Playwright) so they run on every change.
- Guiding rule: whenever you do something manually, turn it into something the agent does for you - today's models can usually figure out how.

## Workflow reconstruction (2026-09-16)

[[kun-agentic-app-development-workflow]] turns testing instructions into a user journey with actual dependencies, persistence and retrieval, plus a meaningful permission or failure case.
Build output and verifier doubles remain useful narrower evidence rather than substitutes for the full journey.

## Requirement-linked evidence (2026-09-23)

[[projects/Education/AI/AI_Wiki/wiki/sources/agentic-code-review-guide|Reviewing AI-Generated Code Safely]] adds a useful check on the checks: would this evidence fail if the requirement were broken?
A screenshot demonstrates appearance, while interaction, persistence, and side effects need behavioral evidence.
Generated tests that reproduce implementation assumptions require review rather than automatic trust.
After fixes, rerun relevant validation and replace stale evidence; a confidence score is not proof.
For gated changes, test both states and the preserved control path, linking implementation validation to [[merge-ready-vs-launch-ready]].

## A skill against useless tests (2026-10-14)

[[agentic-code-review-strategies]] puts the same worry in a sentence: agents can write useless tests.
[[john-meta-engineer]]'s fix is a dedicated skill "around not writing useless tests," so the tests stay meaningful when they are offered as proof in the PR ([[proof-in-the-pr]]).
It is the negative counterpart of this page's "how I would test this" instructions: one says what a good test does, the other forbids the tests that would pass with the feature broken.

## Synthesis

This is [[looking-at-your-data]] and the [[evals]] discipline pushed down into the agent's own harness: instead of you running the app, the agent validates end-to-end the way you would.
It is the behavioral (not just code) half of [[fresh-context-review]] and a prerequisite for [[get-out-of-the-loop]] - you can only stop checking manually once the agent checks behavior for you.
Directly hcho-relevant: writing "how I would test this" instructions is validation expertise encoded as agent config.
