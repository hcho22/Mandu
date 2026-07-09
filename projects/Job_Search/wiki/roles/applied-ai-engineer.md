---
type: role
bucket: ai-builder
seniority: mid | senior
fit: 4
status: established
source-count: 3
last-updated: 2026-07-08
tags: [ai-builder, applied-ai-engineer, llm, rag, agents]
---

# Applied AI Engineer

## What it is
The 2026 product-facing AI engineer.
Integrates LLMs and ML models into real products, where 70%+ of the work is prompts, RAG, agents, and eval.
Also titled AI Engineer (product), AI Application Engineer.
Sits in hcho's **AI builder** bucket and is the closest single match to his Agentic RAG flagship.

## Day-to-day
- Build and maintain pipelines that ship AI features to production.
- Design LLM/agent features tied to a concrete business problem.
- Implement RAG over a vector database; wire in a model provider and orchestration.
- Stand up and own evaluation pipelines; gate shipping on them.
- Work cross-functionally with product, data, and stakeholders.

## Required qualifications and skills

Must-have:
- [[python]] - baseline, non-negotiable (Cohere and Anthropic both name it; TS a plus).
- [[llm-application-development]] - prompting, context engineering, RAG, agents.
- [[rag-systems]] - vector DB + retrieval architecture.
- [[eval-pipeline-design]] - the ship gate (see below); confirmed table stakes - both real postings demand "rigorous evaluation frameworks" measuring accuracy, safety, latency.
- [[agent-orchestration]] - hands-on agentic architectures (ReAct, Plan-and-Execute); a framework (LangGraph, CrewAI) or deliberate framework-free / custom state machines.
- [[customer-facing-delivery]] - both real postings are customer-embedded: translate ambiguous enterprise problems into framed agentic problems, mentor, present, travel ~25%.

Nice-to-have:
- [[mlops-deployment]] - API integration, cloud deployment, production pipelines.
- [[typescript]] - named alongside Python at Cohere.
- SQL and data preprocessing; LLM fine-tuning; MCP servers / Agent Skills (Anthropic).

Education: Bachelor's sufficient; Master's or AI/ML certs a plus, not a gate.

### The ship gate (the eval bar this role is judged on)
A versioned eval set, a numerical score, and a regression alarm.
Offline eval set (~200 curated examples) plus online LLM-as-judge on production traces.
Track at least task-success, latency, and cost-per-task; alert on regression, not absolute thresholds.

## Seniority and comp
Agentic / applied AI engineer band: ~$185K-$320K base + $40K-$120K equity at growth-stage.
Real postings: [[anthropic]] Beneficial Deployments $280K-$300K; [[cohere]] Agentic Workflows (band not posted).
Premiums: RAG architecture +10-15% (mid), fine-tuning +10-15%, MLOps/deployment +$15K-$30K vs notebook-only.
Market: "LLM"/"RAG" postings up ~340% since 2024; generic "ML" postings down ~18%.

## Who hires for it
- [[anthropic]] - Applied AI Engineer, Beneficial Deployments (Tier A; evals + agent advisory for mission-driven partners).
- [[cohere]] - Applied AI Engineer, Agentic Workflows (enterprise agentic workflows, RAG + orchestration).
Also YC-backed agentic/applied-AI startups (see [[founding-ai-engineer]]) and Tier C AI-first product.
Operational target list: `.claude/skills/job-hunter/assets/companies.yaml`.

## hcho's fit and gap
**Fit: 4/5 - one of the strongest matches on the board.**

Strong:
- RAG: the Agentic RAG flagship (FastAPI + pgvector, hybrid retrieval, raw OpenAI SDK) is a direct, production-grade match. The deliberate framework-free choice aligns with shops that avoid LangChain.
- Evals: this role's ship gate is hcho's differentiator. A decade of hardware QA plus the Agentic RAG eval harness (leak suite, golden set, CI gate) is exactly the "eval literacy" signal that now commands a premium.
- Python + product instinct: multiple shipped solo apps (Agentic RAG, FitSnack, CreativeBridge).

Gaps (refined after the 2026-07-08 real-posting batch):
- **Customer-facing enterprise delivery** is a bigger factor than the generic role guide implied. Both real postings are customer-embedded (translate ambiguous enterprise problems, mentor, present, ~25% travel). hcho's QA background is cross-functional but not enterprise-customer-facing; this is now a named gap. See [[customer-facing-delivery]].
- Production MLOps/deployment at scale and formal cloud (AWS/GCP) footprint are lighter than the postings ask; hcho's deploys are Supabase/Apple-native.
- No paid role tenure in the title yet; the evidence is portfolio, not employer-backed.

Note (contradiction with the first ingest, 2026-07-08): the initial role-research pull framed MLOps/cloud as the single biggest gap. The real postings weight **customer-facing delivery and agentic architectures** at least as heavily. Both are now tracked; the plan is reordered accordingly.

## Path to close the gap
1. Lead every application with the eval ship gate as the headline (versioned set, regression alarm, offline+online, three metrics). Confirmed table stakes across the batch, and the requirement most builders cannot demonstrate.
2. Reframe existing cross-functional and stakeholder experience (QA sign-off, vendor/partner work) as customer-facing delivery evidence; lean on the solo-founder shipping story for "high agency / ambiguity."
3. Make Agentic RAG's deployment story explicit: containerize, document the CI eval gate, add a one-page architecture/deploy diagram, and a thin AWS/GCP deploy.
4. Keep the framework-free stance (Cohere explicitly allows "custom state machines") but be ready to speak to LangGraph/CrewAI tradeoffs.

## Sources
- [[applied-ai-engineer-role-research]] (general role guide)
- [[anthropic-applied-ai-engineer-beneficial-deployments]]
- [[cohere-applied-ai-engineer]]
