---
type: skill
category: technical
hcho-level: working
demand: 3
status: developing
last-updated: 2026-07-08
source-count: 4
tags: [mlops, deployment, cloud, infra, ai-builder]
---

# MLOps and deployment

## What it is
Getting AI systems into production and keeping them running: API integration, containerization, cloud deployment (AWS / GCP), and production pipelines.
The signal that separates a shipping engineer from a notebook-only candidate.

## Why roles want it
A must-have for [[applied-ai-engineer]].
Carries a comp premium of +$15K-$30K versus notebook-only candidates.

## How to acquire or demonstrate
Deploy a real service to a major cloud with a documented pipeline and CI.
Show the deploy story, not just the app: architecture diagram, container, CI gate.

## hcho's current level: working
Evidence: shipped and deployed apps (Agentic RAG backend, FitSnack iOS, CreativeBridge on TestFlight), so hcho does ship to production.
But deploys lean Supabase / Apple-native, not big-cloud (AWS/GCP) infra, which the postings name explicitly.

## Gap and how to close
This is the largest single gap for [[applied-ai-engineer]].
1. Containerize Agentic RAG and document its CI eval gate.
2. Stand up a thin AWS or GCP deployment of it to check the named cloud-platform box.
3. Produce a one-page architecture/deploy diagram so the story is legible in an interview.
Cross-link: [[rag-systems]], [[eval-pipeline-design]].

## Roles that require it
- [[applied-ai-engineer]] (nice-to-have)
- [[ai-research-engineer]] (must-have; Hex wants strong infra MLOps - Kubernetes, Terraform, Helm, AWS)
- [[ml-engineer-ai-agents]] (distributed systems + cloud AI infra)

Note: the Hex AI Research Engineer role raises the bar here from "nice" to "must" with explicit infra MLOps. This reinforces the deploy/cloud action item across roles.
