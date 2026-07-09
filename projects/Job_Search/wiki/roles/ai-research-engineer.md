---
type: role
bucket: ai-builder
seniority: senior
fit: 3
status: developing
source-count: 2
last-updated: 2026-07-08
tags: [ai-builder, ai-research-engineer, product-ai, mlops, retrieval]
---

# AI Research Engineer

## What it is
A product-embedded engineer who pushes the capabilities of an AI product through experimentation: running experiments, fine-tuning, deploying AI infra, and building experimentation tooling.
Despite "Research" in the title, this is applied product work, not pure research - both ingested postings (Hex) are explicit that it is production-facing, serving real users.
Sits in the **AI builder** bucket, tilted toward MLOps and experimentation.

## Day-to-day
- Build AI product experiences (e.g. Hex's Notebook Agent: SQL/Python data copilot).
- Run experiments, fine-tune models, deploy AI infrastructure, maintain experimentation tooling.
- Use LLMs to evaluate agent threads; push SQL-generation quality; build agentic search and permissions-aware indexing.
- Partner with product teams; 0-to-1 greenfield features.

## Required qualifications and skills

Must-have:
- Senior engineer from an AI Eng, SWE, or MLE background (not new-grad).
- Getting AI/ML into production serving real users.
- [[mlops-deployment]] - core MLOps and SW architecture; strong on infra aspects (their stack: Postgres, Redis, Kubernetes, Terraform, Helm, AWS).
- [[python]] and [[typescript]] - comfortable in both; strong in one, open to the other.
- Experimentalist mindset; high quality bar for design, correctness, testing.

Role-specific:
- [[rag-systems]] - the Search and Context variant is retrieval-centric: search/recommendation systems, permissions-aware indexing at scale.
- [[eval-pipeline-design]] - "using LLMs to evaluate agent threads."

## Seniority and comp
Senior. [[hex]]: $214K-$285K (base role) and $225K-$285K (Search and Context). SF, NYC, or Remote (USA for the retrieval variant).

## Who hires for it
- [[hex]] - AI Research Engineer, and AI Research Engineer, Search and Context.

## hcho's fit and gap
**Fit: 3/5 - strong on retrieval, gapped on MLOps infra and TS.**

Strong:
- The Search and Context variant maps almost exactly onto Agentic RAG: permissions-aware retrieval, search quality, RAG at scale. This is a standout overlap - see [[rag-systems]] (hcho: strong).
- Evals and experimentation rigor fit hcho's differentiator.

Gaps:
- [[mlops-deployment]] - they want strong infra MLOps (Kubernetes, Terraform, Helm, AWS); this is hcho's named gap.
- [[typescript]] - their stack is TS-heavy front and back; hcho is Python-primary.
- "Senior AI/SWE/MLE" framing wants demonstrated production tenure.

## Path to close the gap
1. Lead the Search and Context variant with hcho's permissions-aware retrieval work - it is a direct, unusual match most applicants cannot show.
2. Close [[mlops-deployment]] infra depth (containerize + cloud deploy Agentic RAG) - same action item as [[applied-ai-engineer]].
3. Build minimal [[typescript]] fluency to clear the "open to both" bar.

## Sources
- [[hex-ai-research-engineer]]
- [[hex-ai-research-engineer-search-and-context]]
