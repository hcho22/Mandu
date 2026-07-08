---
type: area
tags: [evals, testing, llm, quality]
status: established
source-count: 9
last-updated: 2026-07-08
---

# Evals

The durable hub for AI-system evaluation: how you measure whether an LLM product actually works, and how you keep improving it past the demo stage.
This is a core area for hcho, both as craft and as career edge (a decade of hardware QA maps directly onto production-AI quality).

## Why it matters

The recurring thesis across the eval literature is that iteration speed decides AI-product success, and iteration speed depends on having a real evaluation system rather than endless prompt-tweaking.
Evals turn "the model feels better now" into a measurable, repeatable signal, and the same infrastructure doubles as your debugging and fine-tuning data engine.

## Concepts in this area

- [[three-level-eval-framework]] - the L1 unit tests / L2 human and model eval / L3 A/B testing model.
- [[llm-unit-tests]] - Level 1: cheap assertions in CI.
- [[llm-as-judge]] - Level 2 automated evaluation with a model, aligned to human labels.
- [[looking-at-your-data]] - the principle that you must remove all friction from inspecting traces.
- [[pass-fail-over-score-evals]] - prefer binary checks over 1-5 scores when a model grades.
- [[skill-eval-loop]] - a self-checking loop: a separate grader runs pass/fail checks until output passes.
- [[eval-driven-development]] - build task-specific evals first, then let them guide every change.
- [[reference-based-metrics]] - BLEU/ROUGE/BERTScore and their three pitfalls (weak human correlation, poor adaptability, poor reproducibility).
- [[benchmark-sensitivity]] - the same model scores differently across benchmark implementations; leaderboard scores aren't comparable unless identical.
- [[three-eval-methods]] - the three ways to evaluate (automated benchmarks, human as judge, model as judge) and how each fails.
- [[purposes-of-evaluation]] - the three reasons to evaluate (non-regression, ranking, capability), usually conflated.
- [[data-contamination]] - eval data leaking into training inflates scores that don't generalize; the deepest benchmark-validity threat.
- [[evaluation-criteria]] - the four buckets: domain-specific capability, generation, instruction-following, cost/latency.
- [[factual-consistency]] - hallucination detection (local vs global; NLI, SelfCheckGPT, SAFE); the central RAG metric.
- [[model-build-vs-buy]] - self-host open-weight vs commercial API, along seven axes.
- [[evaluation-pipeline]] - how to assemble methods into a reliable, sliced, business-tied, reproducible pipeline (CI-gating in practice).
- [[benchmark-saturation]] - a benchmark near the ceiling loses discriminative power; the decay partner of contamination.
- [[functional-scorers]] - rule-based verifiers (IFEval-style); the interpretable, cheap, contamination-resistant default over judges.
- [[score-reproducibility]] - the full checklist of why a reported benchmark score won't reproduce.
- [[contamination-detection]] - the three flavors and five methods for catching benchmark contamination without corpus access.

## Sources

- [[your-ai-product-needs-evals]] - Hamel Husain's foundational three-level framework.
- [[agents-are-the-new-saas]] - reframes an eval set (50 real examples of the job) as the agent's "gym" and a sales asset; ties evals to the [[agent-saas]] business model.
- [[ai-era-50-career-tips]] - restates the eval discipline as a career edge: "learn where the AI fails, keep a log," and lists "agentic validations" as a core skill of [[agentic-engineering]].
- [[ai-skill-from-scratch]] - evals applied inside a skill: a self-grading loop with pass/fail checks run by a separate agent until the output passes.
- [[llm-patterns]] - Eugene Yan's evals pattern: Eval-Driven Development, the limits of reference-based metrics and benchmarks, and validated LLM-as-judge with its biases.
- [[lets-talk-about-llm-evaluation]] - Clémentine Fourrier (HF): the three methods, the three purposes, and contamination - the area's organizing taxonomy.
- [[evaluate-ai-systems]] - Chip Huyen (AI Engineering Ch. 4): the end-to-end reference - criteria, model selection/build-vs-buy, contamination detection, and how to design an evaluation pipeline.
- [[llm-evaluation-guidebook]] - Fourrier et al. (OpenEvals/HF): the exhaustive benchmarking-side reference - saturation, reproducibility, functional scorers, the judge-bias catalog, and creating your own eval.
- [[what-is-a-contaminated-llm]] - Jonathan Chavez (llm-stats): the dedicated contamination deep-dive - the Codeforces cliff, five detection methods, famous cases, and the contamination-resistant 2026 stack.

## Synthesis

As of the first source, the area's throughline is Husain's: build problem-specific eval systems, not generic frameworks; start with cheap assertions and human trace review, add model-based judging only once it is aligned to human judgment, and defer A/B testing until product-market fit is close.
The single most transferable idea is [[looking-at-your-data]] - the discipline of actually reading model outputs, which is where hcho's validation background is a direct advantage.
Eugene Yan's [[llm-patterns]] hardens this into method: **Eval-Driven Development** ([[eval-driven-development]]) makes the eval set the starting point, and it supplies the "why generic measures fail" backbone - [[reference-based-metrics]] (BLEU/ROUGE mislead on open-ended tasks) and [[benchmark-sensitivity]] (leaderboard scores aren't reproducible across implementations). The latter is the bridge to data contamination, coming in a later source.
Open threads to fill as more sources land: how judge alignment is measured rigorously (precision/recall over raw agreement, now sharpened by the known judge biases), how RAG evaluation differs (Ragas; [[retrieval-is-the-bottleneck]]), and how eval harnesses gate CI in practice.

The classical foundations under all of this live in [[ml-metrics]] ([[precision-recall]], [[roc-and-auc]], [[classification-threshold]]); the eval caveats here are LLM-era restatements of those.

Cross-wiki: hcho's own hand-written eval synthesis lives in the evals pilot wiki (`projects/Learning/AI_Engineer/evals/`, split mode); this hub is the broad reference layer that cross-links to it.
