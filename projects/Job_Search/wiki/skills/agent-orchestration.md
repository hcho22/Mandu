---
type: skill
category: technical
hcho-level: working
demand: 4
status: established
last-updated: 2026-07-08
source-count: 6
tags: [agents, orchestration, react, tool-use, ai-builder]
---

# Agent orchestration

## What it is
Building agents that plan and execute multi-step tasks and act across tools, APIs, and data.
Covers agentic patterns (ReAct, Plan-and-Execute), tool use, orchestration, and failure handling - "beyond simple API calls."
Delivered via a framework (LangGraph, CrewAI) or deliberate framework-free custom state machines.

## Why roles want it
A near-universal must-have across the ingested builder and FDE roles.
Cohere, Anthropic, LangChain, Cresta, and Closure all name multi-step agents/orchestration explicitly.

## How to acquire or demonstrate
Ship an agent that plans and acts across tools with real failure handling, not a single prompt call.
Be able to speak to orchestration tradeoffs (framework vs custom state machine).

## hcho's current level: working
Evidence: Agentic RAG uses agentic tools and subagents (framework-free, raw OpenAI SDK). Cohere explicitly allows "custom state machines," which validates the framework-free stance.
Solid working level; the gap is depth of multi-agent/failure-handling patterns and being fluent in framework tradeoffs.

## Gap and how to close
1. Extend Agentic RAG's agent layer with explicit planning + failure-handling/guardrails to show the full "beyond simple API calls" bar.
2. Be ready to discuss LangGraph/CrewAI vs custom orchestration in interviews even while staying framework-free in the build.
Cross-link: [[llm-application-development]], [[eval-pipeline-design]].

## Roles that require it
- [[applied-ai-engineer]] (must-have)
- [[forward-deployed-engineer]] (must-have)
- [[ml-engineer-ai-agents]] (reasoning/planning)
- [[founding-ai-engineer]] (agentic experiences)
