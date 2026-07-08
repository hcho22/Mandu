# YouTube-Transcript Wiki Log

Event log for this wiki. Each entry begins with `## [YYYY-MM-DD] <op> | <title>` (op is `ingest`, `query`, `lint`, etc.) so entries are greppable and sort by date.

> Batch note (2026-07-03): first ingest into an empty wiki. Eleven AI-engineering video-transcript summaries were ingested in one sequential pass, creating 11 source pages and organically creating 14 concept pages, then seeding `synthesis.md` (full mode) and routing talking points to `projects/job-search/interview-prep.md`. All 11 raw files were verified byte-identical (checksum before/after). Concepts are marked "created" on the source that first touched them and "extended" thereafter.

## [2026-07-03] ingest | Agents Are the New SaaS

- Created `sources/agents-are-the-new-saas.md` (Startup Ideas Podcast).
- Created concepts `[[agents-as-labor]]`, `[[evals-for-agents]]`, `[[agent-permissions-and-safety]]` (each source-count -> 1).

## [2026-07-03] ingest | Building Your Own AI Operating System

- Created `sources/building-your-own-ai-operating-system.md`.
- Created `[[context-engineering]]`, `[[agent-skills]]`, `[[scheduled-agent-autonomy]]`, `[[agent-memory]]`, `[[human-taste-and-ai-slop]]`; extended `[[agent-permissions-and-safety]]`.

## [2026-07-03] ingest | Building an AI Skill from Scratch

- Created `sources/building-an-ai-skill-from-scratch.md`.
- Extended `[[agent-skills]]`, `[[evals-for-agents]]`, `[[agent-memory]]`, `[[human-taste-and-ai-slop]]`.

## [2026-07-03] ingest | Building 5 AI Products Solo, with Agents

- Created `sources/building-5-ai-products-solo.md` (Josh Pigford).
- Created `[[agentic-coding-workflow]]`, `[[parallel-agent-orchestration]]`; extended `[[agent-skills]]`, `[[evals-for-agents]]`, `[[context-engineering]]`, `[[agents-as-labor]]`, `[[human-taste-and-ai-slop]]`.

## [2026-07-03] ingest | Running a One-Person Company with AI Agents

- Created `sources/one-person-company-with-ai-agents.md` (Ryan Carson).
- Created `[[production-agent-infrastructure]]`; extended `[[agentic-coding-workflow]]`, `[[agent-skills]]`, `[[scheduled-agent-autonomy]]`, `[[agent-permissions-and-safety]]`, `[[agents-as-labor]]`.

## [2026-07-03] ingest | Building Products with Coding Agents

- Created `sources/building-products-with-coding-agents.md`.
- Created `[[sub-agents-and-multi-agent]]`; extended `[[agentic-coding-workflow]]`, `[[parallel-agent-orchestration]]`, `[[evals-for-agents]]`, `[[context-engineering]]`.

## [2026-07-03] ingest | Build a Production-Ready Agent with Claude Managed Agents

- Created `sources/claude-managed-agents.md` (Code with Claude workshop).
- Extended `[[production-agent-infrastructure]]`, `[[agent-skills]]`, `[[agent-permissions-and-safety]]`, `[[agent-memory]]`, `[[sub-agents-and-multi-agent]]`, `[[evals-for-agents]]`.

## [2026-07-03] ingest | Every Claude Feature Ranked

- Created `sources/every-claude-feature-ranked.md`.
- Extended `[[agent-skills]]`, `[[context-engineering]]`, `[[agent-memory]]`, `[[sub-agents-and-multi-agent]]`, `[[parallel-agent-orchestration]]`, `[[scheduled-agent-autonomy]]`.

## [2026-07-03] ingest | Inside Conductor: Voice-First Agent Orchestration

- Created `sources/inside-conductor-agent-orchestration.md` (Charlie, Conductor).
- Extended `[[agentic-coding-workflow]]`, `[[parallel-agent-orchestration]]`, `[[context-engineering]]`, `[[agent-permissions-and-safety]]`, `[[sub-agents-and-multi-agent]]`, `[[human-taste-and-ai-slop]]`.

## [2026-07-03] ingest | Building Robust Applications with AI (Pluto)

- Created `sources/building-robust-applications-with-ai.md` (Ross, Hey Fabrica).
- Created `[[agentic-system-design]]`; extended `[[production-agent-infrastructure]]`.

## [2026-07-03] ingest | Startups for Agents: Building for the Agentic Web

- Created `sources/startups-for-agents-agentic-web.md` (Startup Ideas Podcast).
- Created `[[agentic-web-and-aeo]]`; extended `[[agent-memory]]`, `[[agent-permissions-and-safety]]`.
- Seeded `synthesis.md`; updated `index.md`; added talking points to `projects/job-search/interview-prep.md`.
- No daily-log pointer added because `projects/Learning/AI_Engineer/Youtube_transcript/log/2026-07-03.md` does not exist.

## [2026-07-07] ingest | Working With Fable 5 in Claude Code

- Created `sources/working-with-fable-5-in-claude-code.md` (Theo / T3).
- Created `[[model-routing-and-cost-control]]`; extended `[[agentic-coding-workflow]]`, `[[sub-agents-and-multi-agent]]`, `[[parallel-agent-orchestration]]`, `[[evals-for-agents]]`, `[[agent-skills]]`, `[[agent-permissions-and-safety]]`, `[[scheduled-agent-autonomy]]`.
- Updated `index.md` (source + new concept) and `synthesis.md` (13-source thesis; added the model-routing concept to the map).
- Raw `raw/Fable5_ClaudeCode_Workflow_Summary.md` left byte-identical (immutable inbox).
- No daily-log pointer added because `projects/Learning/AI_Engineer/Youtube_transcript/log/2026-07-07.md` does not exist.

## [2026-07-07] ingest | 50 Career Moves in the AI Era

- Created `sources/ai-era-50-career-moves.md` (unattributed tech creator; PM -> Staff SWE at Meta).
- Extended `[[human-taste-and-ai-slop]]`, `[[agentic-coding-workflow]]`, `[[evals-for-agents]]`, `[[context-engineering]]` (AI-engineering tips only).
- Scope note: primarily a career talk; the career/money/interview bulk is out of this wiki's domain and routes to `projects/job-search/interview-prep.md` (not edited this pass - flagged for hcho).
- Updated `index.md`. Raw `raw/AI_Era_50_Career_Tips_Summary.md` left byte-identical.
