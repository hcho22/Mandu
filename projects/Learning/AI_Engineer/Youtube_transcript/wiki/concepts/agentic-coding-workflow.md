---
type: concept
tags: [agents, coding-agents, workflow, plan-code-validate, pull-requests]
date: 2026-07-03
source-count: 6
status: seeded
---

# Agentic Coding Workflow

The production loop for building software with coding agents: plan -> code -> validate, with the human deliberately moved off the critical path and every change landed as a reviewable pull request.

## From the sources

[[building-products-with-coding-agents]] frames the loop as "get out of the loop":

- Keep the standard plan -> code -> validate loop but redistribute effort: most time in planning, coding almost entirely to agents, validation mostly automated.
- If you review every line you become the bottleneck; agents write ~10x more PRs than a human used to (his numbers: 20-40 PRs/day across 20-30 agents).
- The depth of the plan determines how long agents run autonomously: short prompt -> spec -> measurable goal, each buying longer unattended runs.

[[building-5-ai-products-solo]] operationalizes it as a "build skill":

- Distinct research, planning, and implementation phases; implementation is broken so that one phase = one PR = one git branch, never a single massive pass. Some plans run 30+ phases so each step is personally testable.
- A running progress/decisions file lets fresh agent sessions know where they are and avoid repeating mistakes.

[[one-person-company-with-ai-agents]] pushes it to a solo full SDLC:

- "Everything is a PR," running a process "designed for a very large team" though solo, because agents (like humans) need reproducible processes that do not depend on the founder.
- Voice brain-dump -> a clarifying-question PRD skill -> "build it" -> a land-PR playbook used 10-20 times a day; he reads PRs and markdown, rarely code.

[[inside-conductor-agent-orchestration]] enforces the loop in tooling:

- A workspace is a git worktree, and you cannot edit files directly - every workspace must create a PR you then merge, so no change bypasses review.
- PRs are reviewed in-app with GitHub-style inline comments; most workspaces are disposable experiments and only the good ones get promoted.

[[working-with-fable-5-in-claude-code]] pushes the loop to longer autonomous runs with a more capable model:

- "It's not a better Opus": a more capable agentic model pays off only if you restructure work around longer end-to-end runs and sub-agent decomposition, not by reusing old prompts. The run-until-done "goal" cleared a 16-PR backlog and merged ~a month of roadmap in ~5.5 hours.
- Two durability practices make long runs safe: capture the plan as a repo `to-do.md` the agent works and commits against, and align first by *asking the model questions* (it correctly pushed back that a single workflow was the wrong tool for checkpoint-driven, review-gated work).
- Verify more than you produce: he burned more tokens spinning up agents to stress-test the result (diff prod vs main, try old and new features) than producing it, and uses time-to-fix and files-touched as a codebase-health signal (under ~3 min likely simple, an hour+ suggests an architecture problem; a too-fast fix is also suspect).

[[ai-era-50-career-moves]] names the meta-skill and a design mindset:

- "Agentic engineering is the new expertise," with four pillars - context engineering, agentic validations, agentic tooling (building tools for the agent), and compound engineering - as the leverage that grows as models improve.
- To build agentic tools, read the hard code: learn the ReAct loop (reason -> tool use -> act -> repeat until done) from open-source agents. And build for the model of the *future*, not today's, so your design isn't limited to what current models can do.

## Synthesis

Across four independent builders the same shape recurs: the plan -> code -> validate loop is unchanged from pre-AI engineering, but the *effort distribution inverts* - humans concentrate on the plan and the final judgment while agents own the middle. Two invariants make the human safe to remove from the middle. First, **the pull request is the unit of work**: everything is a PR, so every change is atomic, reviewable, and reversible, which is what lets a solo builder run a large-team SDLC. Second, **plan depth buys autonomy**: a one-line prompt bounces back immediately, a spec or a measurable goal lets an agent run for a long time, so investment moves up-front into planning. The validation half of the loop is where the human is replaced most carefully - see [[evals-for-agents]] for the fresh-context and adversarial-review techniques that make automated validation trustworthy. The parallelism that makes this economical is [[parallel-agent-orchestration]], and the plans/config that agents run against are shaped by [[context-engineering]]. As models get capable enough to run for hours ([[working-with-fable-5-in-claude-code]]'s "goal"), two things become load-bearing: a durable in-repo checklist so the long run has state to work against, and [[model-routing-and-cost-control]] so those hours don't cost thousands. This is the video-diet analogue of the internal build discipline in the Agentic RAG wiki, where [[ci-eval-gating]] plays the automated-validation role in a real repo.
