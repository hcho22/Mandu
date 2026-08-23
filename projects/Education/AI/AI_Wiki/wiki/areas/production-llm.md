---
type: area
tags: [production-llm, patterns, fine-tuning, guardrails, caching, ux]
status: developing
source-count: 1
last-updated: 2026-07-08
---

# Production LLM Patterns

The durable hub for the patterns that turn an LLM demo into a product, drawn from [[llm-patterns]] (Eugene Yan).
Karpathy's framing sets the stakes: demos are easy, products are hard.
Yan organizes seven patterns on two axes - improving performance vs reducing cost/risk, and closer to the data vs closer to the user.

## The seven patterns and where they live

- **Evals** -> [[evals]] area (the starting point for everything).
- **RAG** -> [[rag]] area (add knowledge, cut hallucination).
- **[[fine-tuning]]** - get better at a specific task; reach for it last.
- **[[semantic-caching]]** - cut latency and cost by reusing prior generations, safely.
- **[[guardrails]]** - validate input and output for structure, safety, and factuality.
- **[[defensive-ux]]** - anticipate and handle model errors gracefully in the interface.
- **[[data-flywheel]]** - collect user feedback so the system compounds (data as moat).

## The spectrum

From data to user, and defensive to offensive: evals and RAG sit closest to the data and improve performance; caching and guardrails reduce cost/risk; defensive UX and feedback sit closest to the user.
Also-relevant ML patterns Yan flags: cascade (decompose into subtasks the LLM excels at - RAG is an instance), and monitoring (one prod LLM support bot lost 12x more than the human team in an A/B test - so measure value, don't assume it).

## Where this connects

- [[system-design]] - these patterns are the LLM-specific layer on top of general architecture; guardrails, caching, and durability are shared concerns.
- [[single-call-workflow-or-agent]] - the "start with prompting, add retrieval, fine-tune last" ladder is the same restraint principle.
- [[evals]] - underlies all of it: you cannot safely add any pattern without a way to measure whether it helped.

## Sources

- [[llm-patterns]] - Eugene Yan's seven-pattern synthesis (2023).

## Synthesis

One source in, the area's throughline is that **productionizing an LLM is mostly non-LLM engineering**: validating outputs, controlling cost, handling failure, designing for the model being wrong, and closing a feedback loop.
Every pattern except the core generation step is a reliability, cost, or trust concern - which is exactly the surface a validation/QA background owns.
For hcho this is a checklist for the Agentic RAG product and a portfolio-legible skill set: not "I called an API," but "I put guardrails, caching, evals, and a feedback flywheel around it."
