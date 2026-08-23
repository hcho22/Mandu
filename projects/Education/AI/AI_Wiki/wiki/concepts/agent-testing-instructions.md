---
type: concept
tags: [testing, evals, agents, e2e, validation]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Agent Testing Instructions

The practice from [[building-products-with-agents]] of writing explicit end-to-end testing instructions in `AGENTS.md` (or `CLAUDE.md`), because agents default to shallow, code-only unit tests that do not validate behavior.

## Key points

- Write the instructions as "how I would test this myself": drive the real app (e.g. an Electron desktop app via a browser), take screenshots, check for console errors.
- Turn recurring core flows into automated E2E tests (e.g. Playwright) so they run on every change.
- Guiding rule: whenever you do something manually, turn it into something the agent does for you - today's models can usually figure out how.

## Synthesis

This is [[looking-at-your-data]] and the [[evals]] discipline pushed down into the agent's own harness: instead of you running the app, the agent validates end-to-end the way you would.
It is the behavioral (not just code) half of [[fresh-context-review]] and a prerequisite for [[get-out-of-the-loop]] - you can only stop checking manually once the agent checks behavior for you.
Directly hcho-relevant: writing "how I would test this" instructions is validation expertise encoded as agent config.
