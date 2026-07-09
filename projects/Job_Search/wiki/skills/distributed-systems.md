---
type: skill
category: technical
hcho-level: working
demand: 3
status: developing
last-updated: 2026-07-08
source-count: 4
tags: [distributed-systems, backend, infra, cloud, kubernetes]
---

# Distributed systems

## What it is
Building resilient, secure, scalable backend systems: distributed architecture, cloud infrastructure (AWS/GCP/Azure), containers, Kubernetes, and infrastructure-as-code.
Overlaps [[mlops-deployment]] but is broader (general backend/infra, not just the ML serving path).

## Why roles want it
The backend/infra-weighted roles name it: Closure ("resilient, secure distributed systems"), Cresta ("distributed systems and cloud-based AI infrastructure"), Vercel v0 (IaC: Terraform, CloudFormation, Kubernetes), LangChain (cloud + K8s nice-to-have).

## How to acquire or demonstrate
Show a production backend under real-world constraints: scaling, security, containerization, cloud deploy.

## hcho's current level: working
Evidence for: Agentic RAG has a real FastAPI backend with permission-aware/RLS security (Supabase) - genuine backend and security work.
Evidence against: not large-scale distributed systems; deploys are managed-platform (Supabase) rather than self-managed cloud/K8s infra.

## Gap and how to close
1. Containerize Agentic RAG and add a documented cloud deploy (shared action item with [[mlops-deployment]]).
2. Foreground the security/permissions architecture (RLS, permission-aware retrieval) - it maps to the "secure systems" ask.
3. For roles leading with heavy distributed-systems depth (Closure, Cresta), lead with the AI/RAG strengths and treat infra depth as the growth area.

## Roles that require it
- [[founding-ai-engineer]] (must-have; backend depth)
- [[ml-engineer-ai-agents]] (distributed systems + cloud AI infra)
- [[forward-deployed-engineer]] (nice-to-have; Vercel v0, LangChain)
