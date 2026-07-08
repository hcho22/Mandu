---
type: concept
tags: [evals, methodology, workflow]
status: developing
source-count: 2
last-updated: 2026-07-08
---

# Eval-Driven Development (EDD)

From [[llm-patterns]] and [[evaluate-ai-systems]]: building solid evals should be the *starting point* of any LLM system, not an afterthought - collect a set of task-specific evals (prompt, context, expected output) first, then let them guide prompt engineering, model selection, and fine-tuning.

## Key points

- Off-the-shelf benchmarks (MMLU) and classical metrics (BLEU/ROUGE) usually don't fit a real product task; start with your own task-specific eval set instead.
- Once you have it, run it on every change - prompt tweak, model swap, retrieval adjustment - to catch improvements and regressions at scale, without eyeballing outputs each time.
- Named by analogy to test-driven development: the eval set is the executable spec of "working."
- **Chip Huyen ([[evaluate-ai-systems]]):** "evaluation is the biggest bottleneck to AI adoption"; define evaluation criteria before building. Caveat she flags: only building applications whose outcomes are easy to measure is "looking for the key under the lamppost" - reliable evaluation *unlocks* harder applications, so invest in it rather than avoiding the hard-to-measure.

## Synthesis

EDD is the methodological spine of the [[evals]] area and the natural companion to Hamel Husain's [[three-level-eval-framework]] (it says *sequence* the levels; EDD says *start* with them).
It is the single most portable idea for hcho: "write the eval before you tune the prompt" is test-first engineering rebadged, and it is the discipline his Agentic RAG eval harness is meant to embody.
Every other production pattern ([[fine-tuning]], [[guardrails]], [[semantic-caching]], [[retrieval-augmented-generation|RAG]]) depends on it - you cannot know a change helped without an eval to measure it.
