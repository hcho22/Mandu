---
type: concept
tags: [business-operations, knowledge-management, agents, quality]
status: seed
source-count: 1
last-updated: 2026-09-29
---

# Service Business Operating System

A service business operating system is the maintained set of workflows, rules, permissions, runbooks, examples, tests, and measures that lets people and tools deliver work consistently without erasing local judgment.

## Structure

- Separate global rules from company- and client-specific knowledge.
- Give each automated role an explicit job description: allowed actions, forbidden actions, required inputs, stop conditions, and escalation paths.
- Separate intake, preparation, review, and human approval. Preparation and review systems should not send consequential work.
- Preserve accepted human work as test cases that can be rerun after a rule, prompt, model, or workflow changes.
- Turn repeated corrections into reviewed rules and tests; keep one-off preferences local.
- Track profit, labor savings, correction burden, client retention, employee retention, and incidents together.
- Maintain runbooks for common failures, escalation, rollback, and recovery.

## Synthesis

The operating system improves through a controlled loop: real work produces corrections; reviewed corrections update rules; accepted examples become regression tests; test and production evidence informs the next change. This is the business-level expression of [[projects/Education/AI/AI_Wiki/wiki/concepts/eval-driven-development|Eval-driven development]].

Permissions and human authority must scale with consequence, following [[projects/Education/AI/AI_Wiki/wiki/concepts/risk-based-agent-governance|Risk-based agent governance]]. The source describes this structure conceptually but supplies no implementation, security design, or measured outcome.

## Source

- [[../sources/ai-rollup-solo-founder-guide|The $5 Trillion AI Rollup Opportunity]]
