---
type: concept
tags: [evals, pipeline, methodology, ci, production]
status: established
source-count: 4
last-updated: 2026-09-15
---

# Designing an Evaluation Pipeline

From [[evaluate-ai-systems]] ([[chip-huyen]]) and [[llm-evaluation-guidebook]]: how to assemble the eval methods into a reliable pipeline that guides application development - the answer to "how do eval harnesses work in practice?"

## The three steps

1. **Evaluate all components** - measure the end-to-end output *and* each intermediate step, and evaluate both per-turn (each output) and per-task (did it accomplish the goal, in how many turns?). Isolating components tells you where the system actually fails.
2. **Create an evaluation guideline** - the most important step. Define what good *and* bad look like (a *correct* answer isn't always *good* - LinkedIn's "you're a terrible fit" example), build scoring rubrics with examples validated by humans, and **tie eval metrics to business metrics** with a usefulness threshold (e.g. 80% factual consistency -> automate 30% of support).
3. **Define methods and data** - pick a method per criterion (specialized classifier, semantic similarity, AI judge); mix cheap-broad with expensive-narrow; use logprobs for confidence; **slice** the data (guard against Simpson's paradox); size the eval set (OpenAI: ~100 examples for a 10% difference, ~1000 for 3%; bootstrap to check reliability); and **evaluate the evaluation pipeline** itself (temperature 0, reproducibility, metric correlation, added cost/latency). Then iterate with experiment tracking.

## Creating your own eval and reporting it ([[llm-evaluation-guidebook]])

- **Build the dataset** three ways: reuse/aggregate existing data (watch redundancy and balance), human annotation (guideline design dominates the effort - GAIA), or synthetic (rule-based procedural generation to resist [[data-contamination]]; or model-generated with cross-family verification). Always look at your data yourself.
- **Sampling metrics** for robustness: pass@k, maj@n (majority vote), cot@n, avg@n - avoid in cheap ablations, use for post-training/inference; report all sampling params (they multiply cost by k).
- **Statistical validity** (the "forgotten children"): report confidence intervals (bootstrapping), and report cost/time/environmental footprint alongside scores so a 100x-pricier judge is justified against its signal.
- Prefer [[functional-scorers|functional]] scoring over judges wherever a constraint is programmatically checkable.

## Production tooling and error discovery ([[ai-evals-error-analysis]])

Production eval tooling should make the human review loop fast: render traces in a task-specific interface, select a diverse sample, collect open-ended annotations, cluster recurring failures, and distill them into binary rubric criteria.
Dedicated tools such as Braintrust, Arize, and LangSmith mainly win on integration; general coding agents can recover similar obvious errors.
Neither class reliably discovers non-obvious, product-specific failures without human judgment, and automated findings still need review because false positives can distort the product.
Track eval data, prompts, model versions, sampling settings, cost, latency, and criterion-level precision and recall so a score change is attributable.

## Synthesis

This is the capstone of the [[evals]] area: it turns the individual methods ([[three-eval-methods]], [[llm-as-judge]], [[factual-consistency]]) into a system, and it is the missing "CI-gating in practice" piece the area flagged as an open thread.
Nearly every step is textbook validation engineering rebadged for LLMs: test each component in isolation, write an unambiguous rubric, slice by subgroup, size your sample for statistical confidence, keep the test rig itself under test, and log every variable. That correspondence is hcho's edge stated as a build.
It is the blueprint for the Agentic RAG eval harness (component-level + task-level, business-tied thresholds, sliced sets, reproducible judges) and a strong portfolio/interview artifact.
