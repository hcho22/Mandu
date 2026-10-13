---
type: concept
tags: [evals, methodology, workflow]
status: established
source-count: 5
last-updated: 2026-09-29
---

# Eval-Driven Development (EDD)

From [[llm-patterns]] and [[evaluate-ai-systems]]: building solid evals should be the *starting point* of any LLM system, not an afterthought - collect a set of task-specific evals (prompt, context, expected output) first, then let them guide prompt engineering, model selection, and fine-tuning.

## Key points

- Off-the-shelf benchmarks (MMLU) and classical metrics (BLEU/ROUGE) usually don't fit a real product task; start with your own task-specific eval set instead.
- Once you have it, run it on every change - prompt tweak, model swap, retrieval adjustment - to catch improvements and regressions at scale, without eyeballing outputs each time.
- Named by analogy to test-driven development: the eval set is the executable spec of "working."
- **Chip Huyen ([[evaluate-ai-systems]]):** "evaluation is the biggest bottleneck to AI adoption"; define evaluation criteria before building. Caveat she flags: only building applications whose outcomes are easy to measure is "looking for the key under the lamppost" - reliable evaluation *unlocks* harder applications, so invest in it rather than avoiding the hard-to-measure.

## The eval as a control mechanism, not just a measurement (2026-08-01)

Two sources in this batch use an eval set for something this page had not recorded: **driving a loop rather than reporting on a change.**

- **As a stop condition** ([[loops-to-run-your-business]]).
Inbox Zero targets **evals ≥ 90%** on email categorization.
At 88% the agent adjusts the prompt or swaps the model and retries **until it clears 90%**.
The eval is not a gate the human reads; it is the exit condition the agent runs against, which is [[verification-signal-picks-the-mechanism]] made concrete.
- **As the sellable artifact** ([[fde-in-30-days]]).
[[audit-eval-deployment]] makes eval the load-bearing middle phase of a paid client engagement: build a **golden dataset** from historical data (5,000 past presentations, 10,000 past emails), run it, and produce a formal report with pass/fail rates and **categorized failure reasons** - 50 cases, 41 pass, 9 fail, of which 5 had missing data and 4 pulled the wrong record.
That report is what earns the client's permission to grant autonomy.

Both are the same move: the eval set stops being a report card and becomes the thing that **decides what happens next**.
[[self-improving-agent-loop]] is the most developed form - a rubric graded against real production traffic, where sub-threshold results open their own fix PRs.

**The caveat that arrived with them:** [[evals-saturate-and-get-replaced]].
[[boris-cherny]] argues an eval survives one to three model generations before saturating, so budget for replacing eval suites rather than maintaining them.
That does not weaken EDD - it argues for investing in the **generator** (the path from observed failure to new test case) over the test cases themselves.

## Accepted work as an operating regression suite (2026-09-29)

[[projects/Education/Business/wiki/sources/ai-rollup-solo-founder-guide|The $5 Trillion AI Rollup Opportunity]] carries EDD into service operations.
It proposes preserving human-approved input/output pairs and rerunning them after rules, prompts, models, or workflows change.
Repeated corrections become reviewed rules and new test cases, so production failures improve both the operating instructions and the regression suite.

Passing that suite informs the human reviewer; it does not grant authority to send consequential work.
The source supplies no implementation or measured outcomes, so this is a compatible operating pattern rather than new proof of effectiveness.

## Synthesis

EDD is the methodological spine of the [[evals]] area and the natural companion to Hamel Husain's [[three-level-eval-framework]] (it says *sequence* the levels; EDD says *start* with them).
It is the single most portable idea for hcho: "write the eval before you tune the prompt" is test-first engineering rebadged, and it is the discipline his Agentic RAG eval harness is meant to embody.
Every other production pattern ([[fine-tuning]], [[guardrails]], [[semantic-caching]], [[retrieval-augmented-generation|RAG]]) depends on it - you cannot know a change helped without an eval to measure it.

## Source added 2026-09-29

- [[projects/Education/Business/wiki/sources/ai-rollup-solo-founder-guide|The $5 Trillion AI Rollup Opportunity]] - accepted human work as regression cases in an AI-assisted service operation.
