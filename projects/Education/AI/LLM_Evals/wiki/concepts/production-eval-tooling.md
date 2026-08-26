---
type: concept
tags: [evals, tooling, ci, observability]
date: 2026-06-06
source-count: 4
status: seeded
session: "S7 - Production tooling: Promptfoo, DeepEval, Phoenix"
---

# Production Eval Tooling

Running eval suites in CI and observability tools such as Promptfoo, DeepEval, and Arize Phoenix.

## From the sources

Chip Huyen, [[evaluate-ai-systems]], gives the generic evaluation-pipeline scaffold that production tooling should support:

- Evaluate the **end-to-end output** and each component's **intermediate output** independently. For multi-step systems, evaluate per component, per turn, and per task so failures can be localized instead of hidden in an aggregate score.
- Start with an evaluation guideline that defines what the application should and should not do. Ambiguous guidelines produce ambiguous scores.
- For each criterion, choose a scoring system and write a rubric with examples. Validate the rubric with humans before automating it; if humans cannot apply it consistently, the evaluation is not ready.
- Select methods by criterion: specialized toxicity classifiers for toxicity, semantic similarity for relevance, AI judges for factual consistency or subjective criteria, human evaluation where automation is not trustworthy, and cheap broad scorers plus expensive sampled judges when cost matters.
- Curate annotated data for every component and criterion. Use production data where possible, add out-of-scope examples, and slice the data so the system can be debugged by subgroup rather than only by aggregate performance.
- Measure whether the evaluation pipeline itself is reliable: do better responses get better scores, are runs reproducible, do metrics correlate with each other and with business outcomes, and how much cost or latency does evaluation add?
- Track all variables that can affect evaluation results, including evaluation data, rubrics, judge prompts, sampling settings, model versions, and pipeline changes.
- Production evaluation can include manual expert review on a daily sample of outputs. The chapter cites LinkedIn manually evaluating up to 500 daily conversations with AI systems.

Jonathan Chavez, [[what-is-a-contaminated-llm-detection-famous-cases-2026-guide]], adds requirements for tooling that manages benchmark and holdout trust:

- Evaluation tooling should track whether a test set is public, private, gated, post-cutoff, or rotating. That provenance affects how much the score should be trusted.
- For benchmark-style suites, tools should preserve private holdouts, version public releases, and avoid accidentally leaking answer keys or test examples into prompts, logs, fine-tuning data, or vendor training channels.
- Contamination checks can become pipeline checks: time-split reporting where timestamps exist, duplicate or near-duplicate search where corpora are available, membership-inference/perplexity-style checks where logprobs are available, and rephrased/reference-sample comparisons where matched data exists.
- The article reinforces that application evals are part of production tooling, not just research benchmarking: teams should measure on their own codebase, tone, edge cases, and user data because benchmark contamination cannot answer those product-specific questions.

Clémentine Fourrier, Thibaud Frere, Guilherme Penedo & Thomas Wolf, [[evaluation-guidebook]], add the tooling and reproducibility concerns of running evals at scale:

- **Use a standard harness** to reproduce scores: EleutherAI **lm_eval** or Hugging Face **lighteval** (or HELM). The same MMLU gets different scores across implementations, so reproduction requires the *exact* code, prompt, and tokenization. Beyond code, results move with **hardware, inference library (transformers/vLLM/sglang), batch size, loading precision/quantization, and random seed** - fix all of these for reproducibility.
- **Structured/constrained generation** (the `outlines` library, finite-state machines over a grammar/regex) reduces prompt variance and makes rankings more stable - though some research shows it can lower reasoning performance by moving the output distribution off the model's prior.
- **Annotation tooling:** Argilla for building high-quality annotated datasets; distilabel for synthetic-data generation and judge pipelines.
- **Report cost and efficiency** as first-class eval outputs: total **output tokens**, **monetary cost**, **wall-clock/inference time** (including rate-limit overhead), and increasingly the **environmental footprint**. Cost is decisive when choosing methods - an LLM judge may give better signal than automatic metrics but at ~100x cost, and pass@k/maj@n multiply cost by k (see [[classification-metrics]]).

Peter Yang, Hamel Husain & Shreya Shankar, [[ai-evals-error-analysis]], survey the current "do-it-for-you" eval vendors and argue for bespoke, agent-built tooling:

- **The "do automated evals work?" benchmark.** Hamel took a human-annotated dataset and measured how well each tool recovers the same errors: **Braintrust "Loop"** (trace viewer + chat), **Arize "Alex"**, **LangSmith**'s equivalent, and general **coding agents** (Claude, Codex). All recover many of the errors a human would, but **all miss the same class** - the non-obvious, taste-dependent errors (e.g. failing to handle a sales objection, or emitting markdown into a channel where it does not render).
- **Coding agents performed about the same as dedicated eval tools.** The harness is thin - you are mostly invoking a model behind someone else's prompt - so to improve any tool you must steer the agent with a prior idea of what is good and bad, which requires doing error analysis first. If your traces already live in a tool like LangSmith, using its built-in eval feature is a no-brainer; the tools' real advantage is **integration, not superior judgment**.
- **Bespoke interfaces beat spreadsheets and generic SaaS.** A purpose-built review app (Shreya's Error Discovery Skill builds a Python backend + HTML/JS front end, using Gestalt visual encoding) is far easier on human eyes than reviewing traces in Google Sheets, and fits your workflow in ways off-the-shelf products cannot. The counterpoint: this only works if you have a very clear idea of your own workflow. Each discovered failure mode becomes an LLM judge you can then use to **monitor traces/outputs in real time** (see [[llm-as-judge]] and [[offline-vs-online-evals]]).
- **The course frames tooling around the team and time dimensions** the earlier sources gesture at: aligning multiple people on shared criteria, integrating evals into **CI/CD**, and monitoring **drift** over months of deployment (see [[ci-eval-gates-and-drift]]), plus a safety/adversarial track (e.g. not leaking tenant data; see [[hallucination-safety-redteam]]).

## In my own words (hcho)
