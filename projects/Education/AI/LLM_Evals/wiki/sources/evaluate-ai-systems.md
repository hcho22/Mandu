---
type: source
tags: [evals, ai-engineering, benchmarks, hallucination, safety, instruction-following, model-selection, production-monitoring]
date: 2026-06-09
title: "Evaluate AI Systems"
author: "Chip Huyen"
url: "n/a"
concepts: [offline-vs-online-evals, classification-metrics, data-leakage-and-splits, llm-benchmarks-contamination, llm-as-judge, rag-evaluation, production-eval-tooling, hallucination-safety-redteam, agent-eval-and-stats, ci-eval-gates-and-drift, error-analysis]
---

# Evaluate AI Systems

Chip Huyen's "Evaluate AI Systems" chapter argues that AI applications should define application-specific evaluation criteria before development, use public benchmarks only as a first-pass model-selection filter, and build private evaluation pipelines that can guide iteration and production monitoring. The chapter covers evaluation criteria for domain capability, generation quality, factual consistency, safety, instruction following, cost, and latency; model-selection tradeoffs between APIs and self-hosting; benchmark selection, aggregation, saturation, and contamination; and practical pipeline design with rubrics, annotated data, slices, statistical checks, and experiment tracking.

## Key claims

- Evaluation-driven development means defining evaluation criteria before building; reliable evaluation pipelines are a bottleneck to AI adoption because they make value, regression, and failure visible.
- Application criteria should be task-specific and can include domain capability, generation capability, instruction-following capability, cost, latency, scale, safety, factual consistency, and business impact.
- Close-ended and exact evaluations are easier to automate than open-ended generation; MCQs and classification metrics are useful but can fail to measure generation ability and can be sensitive to prompt formatting.
- Factual consistency can be evaluated locally against provided context or globally against open knowledge; local factuality is easier and central to summarization, support bots, business analysis, and RAG.
- Factuality methods include AI judges, self-verification, search-augmented verification, textual entailment/NLI, specialized scorers, and benchmarks such as TruthfulQA.
- Safety evaluation can use general-purpose AI judges, provider moderation tools, smaller specialized toxicity or hate-speech classifiers, and benchmarks such as RealToxicityPrompts and BOLD.
- Instruction-following needs its own evaluation because a model can understand a domain while failing output constraints; IFEval uses automatically verifiable instructions, while INFOBench expands into content, style, and linguistic constraints judged by humans or AI.
- Model selection should filter hard attributes first, use public benchmarks and leaderboards to narrow candidates, run private evals to select models, and monitor production after launch.
- The build-versus-buy choice for models depends on data privacy, data lineage, performance, functionality, cost, control, access, transparency, and on-device constraints.
- Public leaderboards are useful but incomplete: benchmark choice, benchmark correlation, score aggregation, implementation details, and benchmark saturation all affect rankings.
- Public benchmarks are often contaminated because benchmark examples can appear in model training data; contamination can be direct, indirect, intentional, or accidental.
- Contamination detection can use n-gram overlap or perplexity, and better reporting would separate clean-sample scores from overall benchmark scores.
- Evaluation pipelines should test end-to-end outputs and intermediate components independently, and should distinguish task-level from turn-level evaluation when the application is multi-step.
- Clear guidelines and scoring rubrics with examples are the backbone of reliable evaluation; if humans cannot apply the rubric consistently, the metric is not trustworthy.
- Evaluation data should be annotated, sliced, bootstrapped, and tracked; detecting smaller score differences requires much larger sample sizes.
- Evaluation pipelines themselves need evaluation: check signal quality, reproducibility, metric correlation, cost, latency, and experiment-tracking discipline.

## Connections

- [[offline-vs-online-evals]] - evaluation-driven development, the workflow from public/offline filters to private evals to production monitoring, and tying metrics back to business outcomes.
- [[classification-metrics]] - MCQs, classification as fixed-choice prediction, accuracy/precision/recall/F1 for close-ended tasks, and logprobs as classification confidence.
- [[data-leakage-and-splits]] - benchmark contamination as training-on-test-set leakage, decontamination methods, clean-sample reporting, data slicing, and bootstrap checks.
- [[llm-benchmarks-contamination]] - benchmark selection, leaderboards, aggregation, correlation, saturation, implementation sensitivity, and why public benchmarks only narrow the candidate set.
- [[llm-as-judge]] - AI judges for factuality, safety, instruction following, roleplaying, INFOBench, RoleLLM, and the need to evaluate judge reliability.
- [[rag-evaluation]] - factual consistency against retrieved context and component-level evaluation of retrieval and generation.
- [[production-eval-tooling]] - the evaluation pipeline recipe: component tests, guidelines, rubrics, methods, annotated data, slices, significance checks, production feedback, and experiment tracking.
- [[hallucination-safety-redteam]] - local/global factuality, hallucination-prone query slices, self-verification, SAFE, entailment scorers, safety categories, moderation classifiers, and toxicity benchmarks.
- [[agent-eval-and-stats]] - task-level versus turn-level evaluation, multi-step task completion, bootstrap reliability, sample-size rules, metric correlation, and Simpson's paradox.
- [[ci-eval-gates-and-drift]] - evals as regression gates, production monitoring, daily/manual sampling, user feedback, usefulness thresholds, and iteration discipline.
- [[error-analysis]] - human-validated rubrics with examples, annotating and slicing data to localize failures, and sampled manual review (LinkedIn's up-to-500 daily conversations) as production error analysis.

## Source

- **Author:** Chip Huyen
- **Title:** Evaluate AI Systems
- **URL:** n/a
- **Raw:** `raw/Evaluate AI Systems.md` (already saved in `raw/`, immutable)
- **Ingested:** 2026-06-09
