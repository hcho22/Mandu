---
type: skill
category: technical
hcho-level: strong
demand: 2
status: developing
last-updated: 2026-07-08
source-count: 3
tags: [prompt-engineering, context-engineering, evals, ai-builder]
---

# Prompt engineering

## What it is
Designing, refining, and systematically iterating on prompts (and context) to improve LLM/agent performance, measured against metrics rather than by trial and error.
Tightly coupled to [[eval-pipeline-design]]: serious prompt work is metric-driven.

## Why roles want it
Named directly by Anthropic ("advanced prompt engineering") and Cohere (the FDE Prompt Specialist role is centered on prompt optimization + evaluation for the Command model).
Part of the broader [[llm-application-development]] competency.

## How to acquire or demonstrate
Show metric-driven prompt iteration on a real system: a prompt/version tied to eval scores, not vibes.
The Cohere Prompt Specialist role explicitly pairs prompt optimization with metric tracking (quality, efficiency, accuracy).

## hcho's current level: strong
Evidence: Agentic RAG and CreativeBridge both required production prompt/context engineering; hcho's evals rigor means he can tie prompts to measured outcomes, which is exactly the metric-driven framing these roles want.

## Gap and how to close
Minimal. Package a prompt-iteration-with-evals example (prompt change -> eval delta) as a portfolio artifact - it doubles as [[eval-pipeline-design]] evidence and is a strong fit for the Cohere Prompt Specialist FDE (0-5 years, accessible).

## Roles that require it
- [[forward-deployed-engineer]] (Anthropic; Cohere Prompt Specialist centers on it)
- [[applied-ai-engineer]] (part of LLM app dev)
