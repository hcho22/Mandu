---
type: source
title: "Building Products with Coding Agents"
source-type: tutorial-summary
author: "Former L8 engineer (Meta/Microsoft), solo AI builder"
url: "local"
date-ingested: 2026-07-08
date-created: unknown
tags: [agentic-engineering, code-review, validation, sub-agents, testing, workflow]
---

# Building Products with Coding Agents

A summarized live walkthrough by a former L8 engineer (Meta and Microsoft), now a solo AI builder shipping ~20-40 PRs/day across 5+ parallel sessions running 20-30 agents.
Core thesis: [[get-out-of-the-loop|stop being the bottleneck]] - move yourself out of the agent's loop as much as possible.
Demoed with three home-built, open-source tools: Lavish (visual planning), Treehouse (worktree management), and No Mistakes (a fresh-context validation pipeline).

Meta note for hcho: Lavish and No Mistakes are the same tools exposed in this Claude Code session (`lavish-axi`, the `no-mistakes` skill).

## Key claims

- **Get out of the loop:** reviewing every line makes the human the rate limiter as agents write ~10x more PRs; he stopped reading first-pass code and reached a point where his review "never catches anything the agents don't." See [[get-out-of-the-loop]].
- **[[plan-code-validate]] with an unusual effort split:** most time in planning (human + agent), coding almost entirely to agents, validation mostly automated. **Plan depth buys autonomy:** short prompt to written spec to measurable goal - the more comprehensive the plan, the longer agents run unattended.
- **Visual planning:** render the plan as an interactive HTML artifact (Lavish) so you click and annotate options instead of copy-pasting text; HTML over Markdown for agent artifacts when collaboration matters. Bake best-practice guidance ("push back on me") into the tool, not a user-level `AGENTS.md`.
- **[[sub-agents]]:** models rarely self-delegate (except built-ins like Claude Code's explore); the real reason to use sub-agents is to keep the main session's context from blowing up - carve out heavy exploration and return only the conclusion; also good for many isolated experiments.
- **[[agent-testing-instructions]]:** agents default to shallow code-only unit tests; write `AGENTS.md` testing instructions as "how I would test this myself" for end-to-end validation (drive the app, screenshot, check console errors), and turn recurring flows into automated E2E tests (Playwright).
- **[[fresh-context-review]]:** the No Mistakes pipeline reviews each change in a fresh context window (same-session review is biased toward believing the work is correct); an Intent phase hands the fresh reviewer just enough context, like a principal engineer reviewing with fresh eyes.
- **Risk-based attention:** No Mistakes auto-fixes obvious bugs, escalates product-implication fixes, and tags each PR low/medium/high risk with test evidence - so the human spends time on high-risk PRs and merges low-risk ones without opening the diff. Do not run heavy validation on trivial changes (it burns tokens).
- **Team workflows are breaking:** peer review was affordable at 10-15 PRs/month; at 10x volume some teams have stopped reviewing (trending toward less stable products) - the fix is automated review.
- **Advice:** build a lot including throwaways; use parallelism as a forcing function to move yourself out of the loop; apply AI to the whole workflow (validation, docs, PRs), not just coding; but "token maxing" is partly a meme - the goal is real work.

## Connections

- [[get-out-of-the-loop]], [[plan-code-validate]], [[fresh-context-review]], [[agent-testing-instructions]], [[sub-agents]] - the workflow concepts.
- [[fresh-context-review]] unifies the isolated-grader idea from [[skill-eval-loop]] with [[context-rot]] and generalizes [[adversarial-code-review]] (No Mistakes is a productized adversarial reviewer).
- [[everything-is-a-pr]] - No Mistakes ends in a risk-assessed PR; the same code-factory SDLC.
- [[phased-implementation]] - Treehouse is a worktree manager (pooled, pre-installed deps); worktrees again.
- [[looking-at-your-data]] / [[evals]] - "test evidence" (screenshots/video) is looking at your data, automated.
- [[opencode]], [[anthropic]] (Claude Design, Claude Code /insights), [[openai]] (Codex, ProgramBench) - tools cited.

## Source

- **Author:** Former L8 engineer (Meta and Microsoft), now solo AI builder (handle garbled in captions); interviewed by Peter
- **Title:** Building Products with Coding Agents
- **Tools cited:** OpenCode (harness), tmux, Lavish, Treehouse, No Mistakes, Claude Design, Claude Code /insights, Codex, Playwright; benchmarks ProgramBench / SWE-bench.
- **Raw:** [[Building-Products-with-Agents-Summary]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-07-08
