---
type: concept
tags: [evals, criteria, quality, methodology]
status: seed
source-count: 1
last-updated: 2026-07-08
---

# Evaluation Criteria (the four buckets)

From [[evaluate-ai-systems]] ([[chip-huyen]]): an AI application should start from a list of application-specific evaluation criteria, which fall into four buckets.

## The four buckets

- **Domain-specific capability** - can the model do the task at all (code, a language, math)? Constrained by architecture and training data. Evaluated with domain benchmarks, functional correctness (code), and multiple-choice questions.
- **Generation capability** - is the output good? Older NLG metrics (fluency, coherence, faithfulness, relevance) matter less as models improve; the pressing ones now are [[factual-consistency]] and safety (toxicity, bias).
- **Instruction-following capability** - does it do what you asked (format, length, constraints)? Measured by IFEval (auto-verifiable format instructions) and INFOBench (broader, yes/no criteria per instruction); roleplaying is a common instruction type.
- **Cost and latency** - can you afford it and is it fast enough? A Pareto/multi-objective problem; be explicit about what you can't compromise on (e.g. filter by a latency ceiling first).

## Synthesis

This is the "what to measure" backbone of the [[evals]] area, and its key discipline is up front: enumerate the criteria *specific to your application* before building ([[eval-driven-development]]), because a model that aces generic benchmarks can still fail your criteria.
It distinguishes failure modes that are easy to conflate - a bad output can be a capability gap, an instruction-following gap, or a bad prompt - which is exactly the kind of root-cause separation a validation engineer does.
Instruction-following and cost/latency are the criteria practitioners most often forget to test, and they map onto hcho's product bets (structured outputs, latency budgets) directly.
