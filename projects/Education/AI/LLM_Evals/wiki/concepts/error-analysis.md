---
type: concept
tags: [evals, error-analysis, rubric, annotation, workflow]
date: 2026-08-26
source-count: 4
status: seeded
session: "S11 - Error analysis: reading data and building the rubric"
---

# Error Analysis

The practice of reading real model outputs to discover and categorize failure modes, then externalizing them into a rubric of pass/fail criteria.
It is the human-driven front end of the eval workflow: the step that produces *what to measure* before any judge, metric, or CI gate can measure it.

## From the sources

Peter Yang, Hamel Husain & Shreya Shankar, [[ai-evals-error-analysis]], make error analysis the explicit centerpiece and give it a working structure:

- **Top-down vs bottom-up evals.** *Top-down* criteria are what a domain expert would derive from the task description alone; *bottom-up* criteria are the failure modes you only find by reading lots of real outputs. AI can generate top-down criteria but is "very bad" at bottom-up ones - that taste has to come from the human. Keep the two explicitly separated so bottom-up coverage stays honest.
- **Error analysis is the hardest and most valuable part of evals** (producing the rubric); its goal is *confidence* - knowing exactly what behavior the model is exhibiting. It is iterative and never "done": seeing more examples surfaces more failure modes that feed back into the rubric.
- **Prefer yes/no, pass/fail criteria** over invented numeric scores, so each criterion reduces to a binary judgment that can later become an LLM judge (see [[llm-as-judge]]) and be scored with precision/recall (see [[classification-metrics]]).
- **Agents scale the tedious parts but not the taste.** Shreya's free **Error Discovery Skill** builds a custom review interface (Python backend + HTML/JS front end using Gestalt visual encoding), clusters traces to pick a diverse initial sample, watches you annotate in situ, and distills your open-ended notes into a taxonomy after ~10 notes. The human reads and reacts; the agent only groups and distills, never invents feedback. Review until *saturated*, not just a handful.
- **The annotation pass yields a labeled dataset for free**, so the resulting rubric can itself be benchmarked. **Mine the back catalog:** run the skill over past inputs and compare its output against your human-edited finals (the real labels) to surface bottom-up patterns from the differences.
- **The payoff feeds the rest of the pipeline:** discovered failure modes become a rubric → a skill → per-criterion LLM judges → a dashboard or real-time trace monitor (see [[production-eval-tooling]] and [[offline-vs-online-evals]]).

Hamel Husain, [[your-ai-product-needs-evals]], supplies the earlier, product-grounded version of the same discipline as Level 2 of his framework:

- **Log and review traces with all friction removed** - build domain-specific viewers so looking at data is fast - and **start with binary good/bad labels**. This trace review is where failure modes are discovered before any automated judge is written.
- Iteration speed rests on three activities - measuring quality, **debugging via logging and data inspection**, and changing behavior - and teams that skip the inspection never get past a demo.
- The labels produced by review then align the LLM judge to human judgment (a spreadsheet of responses, model critiques, and human labels), tying error analysis directly to judge construction (see [[llm-as-judge]]).

Chip Huyen, [[evaluate-ai-systems]], frames the annotation-and-rubric side as a pipeline requirement:

- **Clear guidelines and scoring rubrics with examples are the backbone of reliable evaluation;** if humans cannot apply the rubric consistently, the metric is not trustworthy - so the rubric must be built and validated by human review before automation.
- **Annotate, slice, and debug by subgroup** rather than reading only an aggregate score, so failures can be localized instead of hidden. Curate the annotated data from production examples where possible.
- **Production error analysis can be a sampled manual review** - the chapter cites LinkedIn manually evaluating up to 500 daily conversations - serving as a North Star when automated metrics are weak (see [[ci-eval-gates-and-drift]]).

Eugene Yan, [[patterns-for-building-llm-based-systems-and-products]], gives the lightweight-but-load-bearing version:

- **The best eval is sometimes a human "vibe check"** - the MosaicML anecdote of watching a fixed prompt's answer change over training was more informative than metrics - which is error analysis in its most basic form: a human reading outputs and forming a judgment.
- **"Eval-Driven Development":** build a set of task-specific evals (prompt, context, expected output) derived from looking at your own outputs, and run them on every change (see [[offline-vs-online-evals]] and [[ci-eval-gates-and-drift]]). The eval set originates in the same read-your-data step.

## In my own words (hcho)
