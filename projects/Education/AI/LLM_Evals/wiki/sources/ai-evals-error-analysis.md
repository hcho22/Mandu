---
type: source
tags: [evals, error-analysis, llm-as-judge, tooling, workflow]
date: 2026-08-26
title: "Automating AI Evals the Right Way - with Error Analysis"
author: "Peter Yang (host), with Hamel Husain and Shreya Shankar"
url: ""
concepts: [error-analysis, llm-as-judge, production-eval-tooling, classification-metrics, offline-vs-online-evals]
---

# Automating AI Evals the Right Way - with Error Analysis

A YouTube podcast conversation and live demo in which Peter Yang interviews Hamel Husain and Shreya Shankar, the instructors of a popular AI-evals course.
The through-line is that evals still start with a human reading their own outputs and externalizing their taste through **error analysis**, but agents can now do the tedious parts - building a review interface, clustering samples, and distilling open-ended notes into a reusable rubric.
The centerpiece is a demo of Shreya's free **Error Discovery Skill**, and the episode closes with Hamel's benchmark of "do-it-for-you" automated eval vendors, which recover obvious errors but miss the taste-dependent ones that differentiate a product.

## Key claims

- **Top-down vs bottom-up evals** are the organizing frame: top-down evals are what a domain expert would derive from the task alone, and bottom-up evals are failure modes you only find by reading real outputs. AI is good at generating top-down evals and "very bad" at bottom-up ones - that taste has to come from the human.
- **Error analysis is the hardest and most valuable part of evals** (producing the rubric); the goal is confidence - knowing exactly what behavior the model is exhibiting. Evals are iterative and never "done."
- Prefer **yes/no, pass/fail** criteria over invented numeric scores, and explicitly separate a skill's evals into top-down and bottom-up sections to keep bottom-up coverage honest.
- **LLM judges have gotten good at narrow, well-defined criteria** (length, structure adherence); Hamel is now much more bullish on them than before. Each discovered failure mode can become its own LLM judge.
- **Fan out one sub-agent per criterion** (or per small group). Handing a model one giant list of criteria causes it to get "washed out" and lazily skip some; focused per-criterion evaluation keeps it honest.
- **You get a labeled dataset for free** from the annotation pass, so you can benchmark the rubric itself - measure the judges' precision/recall rather than assuming the rubric is good.
- **Mine the back catalog for bottom-up signal:** run the skill on past 10-20 inputs, compare its output to your human-edited finals (the real labels), and have the AI find the patterns in the differences.
- The **Error Discovery Skill** (free, on GitHub) runs five steps: read the dataset and infer its semantic type; design a visual encoding using Gestalt principles; build a review app (Python backend + HTML/JS front end); cluster and pick a diverse initial sample; run an interactive loop where the agent watches annotations and distills them into rubric criteria. The human supplies feedback in situ; the agent only groups and distills, never invents feedback. It proposes a taxonomy after ~10 notes; Shreya advises reviewing until saturated.
- **"Do automated evals work?"** (Hamel's benchmark): Braintrust "Loop", Arize "Alex", and LangSmith - plus coding agents (Claude, Codex) - all recover many errors humans would, but **all miss the same class**: non-obvious errors requiring product judgment (e.g. failing to handle a sales objection, or putting markdown in text messages where it does not render). Coding agents performed about the same as dedicated eval tools; the harness is thin.
- **Watch precision, not just recall:** best-case precision from automated tools is ~80-90%, so 10-20% of flagged "errors" are red herrings that can distort a product if accepted blindly. Still worth using, but review the errors the tool found to confirm you agree.
- Because you can build a bespoke review interface with a coding agent, generic eval SaaS's main advantage is integration, not superior judgment - though doing this well requires a very clear idea of your own workflow.
- The course's five modules span error-analysis philosophy, productionizing and scaling across a team (aligning people on criteria, CI/CD integration, drift monitoring over months), safety and adversarial evaluation (e.g. not leaking tenant data), and joint cost/accuracy improvement (a claimed up-to-100x cost reduction while holding accuracy).
- **Writing is the "final boss":** getting a model to write like you is very hard, so integrate AI feedback as a compare-and-review workflow rather than letting it silently edit prose and add slop. Named slop tells: negative contrast ("not X, it's Y"), triadic parallel enumeration (lists of threes), and staccato fragments (<4-word sentences).

## Connections

- [[error-analysis]] - the source's central subject: reading real outputs to discover failure modes, the top-down vs bottom-up split, and turning annotations into a rubric.
- [[llm-as-judge]] - narrow well-defined criteria are the sweet spot for judges; each discovered failure mode becomes a judge; fan out one sub-agent per criterion to avoid wash-out; measure the judges' precision/recall against the free labeled set.
- [[production-eval-tooling]] - the "do automated evals work?" benchmark of Braintrust, Arize, and LangSmith; bespoke agent-built review interfaces vs off-the-shelf eval SaaS; coding agents as a thin eval harness.
- [[classification-metrics]] - precision vs recall of automated eval tools (~80-90% precision, 10-20% red herrings); benchmarking a rubric with an annotated dataset to check whether the evals themselves are any good.
- [[offline-vs-online-evals]] - error analysis over real logged/production traces as the starting point; the review-and-monitor loop; evals as iterative and never "done."

## Source

- **Author:** Peter Yang (host), with Hamel Husain and Shreya Shankar
- **Title:** Automating AI Evals the Right Way - with Error Analysis
- **URL:** (YouTube podcast; episode-description link not captured in the raw source)
- **Raw:** [[ai-evals-error-analysis]] (saved verbatim in `raw/`, immutable)
- **Ingested:** 2026-08-26
