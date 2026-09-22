---
type: synthesis
last-updated: 2026-07-13
status: developing
---

# Synthesis: which role, and how to get there

The top-level plan.
This page answers: across hcho's target lanes, which roles are the strongest fit, which skills are the highest-leverage gaps to close, and in what order.
It is rewritten as ingests shift the picture.

> **Strategy note (2026-09-22):** the operational search broadened after the narrow strategy produced too few useful results. The September 22 expansion adds evaluation-centered MLE and Data Scientist titles plus applied-ML roles, while retaining responsibility-based fit gates. The role ranking below predates this expansion and should be refreshed as new sources are ingested.

## The three search lanes

- **Software quality and systems validation** - automation-heavy SDET, systems/product validation, test infrastructure, API/backend automation, mobile/iOS test, and release quality.
- **AI quality and evaluation** - roles centered on evaluating and assuring production AI systems, including Machine Learning Engineer, Evals; Machine Learning Evaluation Engineer; ML or Model Quality Engineer; ML Validation Engineer; LLM Evaluation Engineer; and Data Scientist roles centered on model evaluation, Trust and Safety modeling, AI quality, or AI reliability.
- **AI product, integration, and technical delivery** - AI product engineering plus Applied Machine Learning Engineer, AI/ML Engineer, Data Scientist roles centered on applied ML, and hands-on integration, implementation, customer engineering, developer support, and forward-deployed delivery.

The cross-cutting differentiator is **validation / evals rigor** from a decade of hardware QA, paired with current software automation and shipped AI/product work.
The 2026-07-08 posting batch confirmed this is the right bet: evaluation is a named requirement in nearly every posting, across companies and role types.

## Best-fit roles (ranked)

Updated after the 2026-07-08 real-posting batch (16 sources, 6 role archetypes):

1. [[applied-ai-engineer]] - fit 4/5. The closest single match to Agentic RAG; RAG + evals are direct strengths. Real targets: [[anthropic]], [[cohere]].
2. [[ai-content-engineer]] - fit 4/5. Fuses hcho's evals differentiator with his active build-in-public motion. Target: [[llamaindex]]. Gap is writing-portfolio volume, which doubles as product marketing.
3. [[forward-deployed-engineer]] - fit 3/5 but the **highest-volume** archetype (9 postings). Technically in reach; the blocker is [[customer-facing-delivery]]. Accessible entry points: [[cohere]] **Agentic Platform West Coast** (remote, LA-local-eligible, eval-forward - added 2026-07-13, [[cohere-fde-agentic-platform]]) and Prompt Specialist (0-5 yrs, eval-centric), [[langchain]] (eval/observability nice-to-have). The West Coast Cohere FDE is notable: it clears the location gate for hcho AND leads with his eval differentiator.
4. [[ai-research-engineer]] - fit 3/5. [[hex]] Search-and-Context is a standout RAG/permissions match and Remote-USA eligible; gaps are MLOps infra + TS.
5. [[ml-engineer-ai-agents]] - fit 3/5. [[cresta]] (resume already tailored); ML-depth gap, eval/reliability is the way in.
6. [[founding-ai-engineer]] - fit 3/5. [[closure]] is clearance-gated; the shape recurs across the YC list.

## Highest-leverage skill gaps

Two kinds of gap: real skill gaps, and visibility gaps on existing strengths.

Real gaps (close these to convert more roles):
- [[customer-facing-delivery]] - hcho: learning. Now the **single biggest blocker**, because the highest-volume archetype (FDE) is built around it. Close by reframing QA/vendor + solo-founder discovery experience (the Agentic RAG buyer interviews are literal customer discovery) and targeting eval-centric FDE variants first.
- [[mlops-deployment]] / [[distributed-systems]] - hcho: working. Containerize + cloud-deploy Agentic RAG to clear the infra bar (Hex, Cresta, Vercel v0).
- [[typescript]] - hcho: learning. Clears "open to both" roles already; only blocks TS-primary employers (Vercel).

Visibility gaps (hcho is strong; make it legible):
- [[eval-pipeline-design]] - confirmed table stakes across nearly every posting. hcho's headline. Lead with it everywhere.
- [[rag-systems]], [[llm-application-development]], [[prompt-engineering]] - all strong; package as public, legible artifacts.

## Recommended sequence

1. **Lead with the eval ship gate on every application.** The batch confirmed evaluation is a near-universal requirement most builders cannot demonstrate; it is hcho's headline differentiator.
2. **Attack the customer-facing gap by reframing, not just building.** Put the Agentic RAG buyer interviews and QA/vendor stakeholder work on the resume as customer-discovery evidence. This unlocks the largest role pool (FDE).
3. **Target the accessible, differentiator-aligned openings first:** Cohere Agentic Platform **West Coast** FDE (LA-local + eval-forward - apply now), Cohere Applied AI + Prompt Specialist FDE, LangChain Deployed Engineer, Hex Search-and-Context, LlamaIndex AI Content Engineer, Cresta ML Eng (resume ready).
4. **Close the deployment/cloud gap** (containerize + thin AWS/GCP deploy of Agentic RAG) to lift fit across Applied AI, AI Research, and ML Eng roles at once.
5. **Housekeeping:** [[cohere]] is now on the operational target list (`companies.yaml`); add [[hex]] if not yet there; decide the 20-40% FDE travel appetite (now a live question given the LA-eligible Cohere West Coast FDE); skip clearance-gated roles (Cohere Sovereign AI, Closure).
