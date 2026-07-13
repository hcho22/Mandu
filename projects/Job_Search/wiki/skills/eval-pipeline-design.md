---
type: skill
category: technical
hcho-level: strong
demand: 5
status: established
last-updated: 2026-07-13
source-count: 8
tags: [evals, quality, ship-gate, differentiator, ai-evals]
---

# Eval pipeline design

## What it is
Designing and running the evaluation pipelines that gate whether an AI system ships.
The 2026 "ship gate": a versioned eval set, a numerical score, and a regression alarm.
Offline eval set (~200 curated examples) plus online LLM-as-judge on production traces.
Track at least task-success, latency, and cost-per-task; alert on regression, not absolute thresholds.

## Why roles want it
Now table stakes for [[applied-ai-engineer]], not a niche, and the core of the entire AI evals / quality bucket.
It is the requirement most builders cannot actually demonstrate.

## How to acquire or demonstrate
Own a real eval harness on a shipped system: curated golden set, CI gate, regression alarms, offline + online.
Be able to speak to metric choice and to LLM-as-judge reliability.

## hcho's current level: strong (this is the differentiator)
Evidence: a decade of hardware QA / validation maps directly onto production AI quality, plus the Agentic RAG eval harness (leak suite, escalation golden set, CI eval gate).
This is hcho's single strongest positioning asset across both buckets.

## Gap and how to close
Skill is present; the gap is visibility.
Lead applications and interviews with the ship gate as the headline.
Add online LLM-as-judge on production traces to Agentic RAG if not already there, to match the full offline+online bar.
Cross-link: [[rag-systems]], [[mlops-deployment]].

## Confirmed at scale (2026-07-08 posting batch)
Evaluation appeared as a named requirement in nearly every posting across companies: "rigorous evaluation frameworks" (Cohere), "evaluation frameworks and deployment at scale" (Anthropic), "LLM evaluation, observability, guardrails" (LangChain), "evaluation and reliability" (Cresta), benchmark-building (LlamaIndex).
This validates evals as hcho's headline differentiator: it is not a niche, it is a broad baseline that most builders cannot actually demonstrate.

The 2026-07-13 Cohere North FDE (West Coast) posting states the bar almost verbatim to hcho's positioning: "proven ability to build robust evaluation frameworks, moving well beyond trial and error, to measure agent accuracy, safety, and latency." Use this phrasing as a template for how to frame the Agentic RAG eval harness in applications. [[cohere-fde-agentic-platform]]

## Roles that require it
- [[applied-ai-engineer]] (must-have)
- [[forward-deployed-engineer]] (must/strong-plus; "guiding evaluations," observability/guardrails)
- [[ai-research-engineer]] (using LLMs to evaluate agent threads)
- [[ai-content-engineer]] (core deliverable: benchmarks + evaluation frameworks)
- [[ml-engineer-ai-agents]] (evaluation + reliability a named focus)
