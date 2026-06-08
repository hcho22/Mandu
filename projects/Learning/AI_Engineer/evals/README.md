# Evals (AI Eval / QA)

**One-liner:** Learning track for AI evaluation and quality engineering, the core skill for the target role. Working through a 20-hour, 10-session plan.

**Status:** Active, current learning focus. Started 2026-06-03.

**Plan:** `learning-plan.md` (full 20-hour plan: 10 sessions, one-page cheat sheet, 10-question quiz, 5-level ladder, top-5 resources, Feynman walkthrough).

## Why evals specifically

Highest-leverage topic for the AI Evals / Quality role target. The plan's thesis: master ~10 high-leverage concepts (the offline/online split, golden datasets, classification metrics under class imbalance, LLM-as-judge and its biases, RAG metrics, regression testing, drift, agent trajectory eval, statistical noise, red-teaming) and practice each in a real tool (Promptfoo, DeepEval, RAGAS, Phoenix/LangSmith).

## Portfolio synergy

Agentic RAG already implements much of this in production form, so the study and the portfolio reinforce each other. Use this track to fill the theory gaps behind that work and turn it into crisp interview talking points.

| Concept (this track) | Where it already exists in the portfolio |
| --- | --- |
| Golden set + recall@k / MRR / nDCG | Agentic RAG: 50-question golden set, retrieval eval suite |
| CI eval gating + regression catch | Agentic RAG: PR workflow that caught a Δ -0.510 recall@5 drop |
| RAGAS metrics (faithfulness, answer relevancy, context precision/recall) | Agentic RAG: computed weekly |
| Security property proven by an eval | Agentic RAG: ACL no-access eval (fraction returning zero gold chunks = 1.000) |

## Session progress (10 x 2-hour sessions)

Check off as completed. Current: **S1 (in progress)**.

- [ ] S1 — What evals are and why they matter (offline/online/human-in-loop; eval flywheel; Hamel's L1/L2/L3) — **in progress**
- [ ] S2 — Classical ML metrics (confusion matrix; precision/recall/F1; ROC-AUC vs PR-AUC; class imbalance)
- [ ] S3 — Data splits, leakage, baselines, cross-validation; LLM benchmark contamination
- [ ] S4 — LLM benchmarks: what they measure and their saturation/contamination status
- [ ] S5 — LLM-as-judge: setup, biases (position/verbosity/self-enhancement), human alignment (Cohen's kappa)
- [ ] S6 — RAG evaluation: the RAG triad, RAGAS, reference-based vs reference-free
- [ ] S7 — Production tooling: Promptfoo, DeepEval, Phoenix
- [ ] S8 — Hallucination, safety, red-teaming, guardrails (OWASP LLM Top 10)
- [ ] S9 — Agent eval + statistical rigor (tau-bench, Inspect, confidence intervals)
- [ ] S10 — CI/CD eval gates, drift monitoring, putting it all together

## Learning ladder (current level)

The plan defines 5 levels (Section 4). Track current level here.

- **Current level:** Level 1 (Beginner, 0–4 hrs in) — in progress (working S1, started 2026-06-03).
- L1 Beginner → L2 Practitioner → L3 Intermediate → L4 Advanced → L5 Expert. Promotion criteria for each level are in `learning-plan.md`.

## Top resources (full list in plan Section 5)

1. Hamel Husain — blog ("Your AI Product Needs Evals") + "AI Evals for Engineers & PMs" Maven course (with Shreya Shankar).
2. Chip Huyen — *AI Engineering* (O'Reilly, 2025), Ch. 3–4.
3. Hugging Face Evaluation Guidebook — Clémentine Fourrier.
4. EleutherAI lm-evaluation-harness + Inspect AI (UK AISI).
5. Production tooling triad: Promptfoo + DeepEval + RAGAS, plus Phoenix or LangSmith for observability.

## Tracking

Study-session logs go in `log/` (one file per session or per date). Record: session focus, objectives, hands-on result, learnings, blockers, and next step. Created on first use.
