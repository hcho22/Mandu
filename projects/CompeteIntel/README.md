# CompeteIntel

**One-liner:** A competitive-intelligence engine that turns a single competitor name into a cited, confidence-scored **Brief** (Markdown + structured JSON). One name in; the engine resolves the entity, plans the research, fans out source-grounded retrieval tools, synthesizes findings into cited Claims, and returns a Brief that is explicit about what it does and does not know.

**Repo:** https://github.com/hcho22/competeIntel (private)

**Status:** Built. v1 milestones **M1-M3** complete — the full four-agent pipeline (Planner, Research, Pricing, Synthesis), the guardrailed tool library, the FastMCP adapter, and a CI release gate are implemented. v1 is the **engine only** (no self-serve signup, billing, or multi-tenancy). 147 tests; `mypy` strict with the pydantic plugin.

## Why this project / how it fits

This is a **second flagship portfolio piece for the AI Eval / QA Engineer target**, complementary to [Agentic RAG](../Agentic_RAG/README.md). Where Agentic RAG showcases *retrieval* evals, CompeteIntel showcases **evals on a multi-agent generative pipeline with citation grounding** — the harder, more current evals problem:

- **Golden set as ground truth:** a 20-query, version-controlled golden set (`evals/golden.py` + `golden_set.json`).
- **LLM citation judge + calibration:** verifies each Claim is actually supported by its cited source, with a calibration harness that measures the judge against labeled pairs (judging the judge — a core evals-role skill).
- **CI release gate:** `python -m competeintel.evals.gate` runs the engine over the golden set, computes the PRD section 8 metrics (citation / pricing / recency), applies thresholds, and exits `0`/`1` naming the failing metric. Wired into `.github/workflows/eval-gate.yml`, so a sub-threshold build goes red.
- **Uncertainty as a first-class output:** every Claim carries a bucketed **Confidence** (High / Medium / Low) and a **Conflict** flag; the Brief reports its own **Coverage** (complete / partial / unavailable) so gaps are visible, never silent.
- **A quality property under a budget:** a wall-clock budget bounds the research fan-out, not the whole pipeline. On expiry, pending Research is cancelled but Synthesis still runs on the Evidence in hand with every guardrail applied; dropped Sections are marked `unavailable`.

Interview talking points: evaluating non-deterministic multi-agent output, citation-grounding verification, calibrating an LLM judge against human labels, confidence / coverage as honesty mechanisms, and gating releases on eval thresholds rather than asserting quality.

## What a Brief is

A Brief covers **exactly one** competitor in six fixed Sections: **Snapshot** (firmographics), **Features**, **Pricing** (normalized to a fixed schema, the highest-stakes Section), **Recent launches**, **Customer sentiment** (labeled lower-confidence), and **Positioning gap** (an inferred weakness grounded in at least two of the Brief's own Claims). Every fact-bearing Claim carries its Evidence, a per-source Citation, a bucketed Confidence, and a Conflict flag when sources disagree. The fixed domain vocabulary lives in the repo's `CONTEXT.md`; code and Briefs use those exact terms.

## Stack

- **Language:** Python 3.10+ (the `.venv` runs 3.11, required by FastMCP); `mypy` strict + pydantic plugin.
- **Agents / LLM:** Anthropic (Claude) for all four agents plus the citation judge; per-agent model overrides via env (`PLANNER_MODEL`, `SYNTHESIS_MODEL`, `PRICING_MODEL`, `JUDGE_MODEL`, ...).
- **Orchestration:** hand-rolled `asyncio` (plan -> parallel fan-out -> synthesize); one typed `BriefState` threaded through the whole pipeline (no agent framework).
- **Tools / retrieval:** Exa (web search) + Firecrawl (page fetch) behind provider interfaces; a `@guarded_tool` middleware layer adds PII redaction, source-quality scoring, recency, and caching.
- **Interface:** FastMCP server exposing `generate_brief` plus 5 atomic tools.
- **CI / evals:** GitHub Actions release gate (unit tests + typecheck on every push/PR; the gate on `main`).

## Key components / architecture

- **`state.py`** — `BriefState`, the single typed contract threaded through the pipeline.
- **`orchestrator.py`** — `run_pipeline()`: Planner -> parallel Research -> Synthesis, with the budget.
- **`brief.py`** — assemble / render Markdown / render JSON, plus the citation gates.
- **`mcp_adapter.py`** — the FastMCP server: `generate_brief` + 5 atomic tools.
- **`agents/`** — Planner (entity resolution: resolved / ambiguous / unresolvable, plus research planning), Research (a Plan Section -> cited Evidence), Synthesis (Evidence -> grouped Claims + Confidence), Pricing (a captured pricing page -> span-checked PriceTiers).
- **`tools/`** — the shared guardrailed retrieval library (search, fetcher, pricing, features, firmographics, changelog) + `middleware.py`.
- **`evals/`** — golden set, citation judge, metrics, calibration, runner, and the CI `gate.py`.

Every external dependency (search, fetch, each LLM agent) sits behind an abstract interface with a `register_*` hook, so tests inject deterministic fakes and no unit test touches the network.

## Design commitments (ADRs)

Load-bearing decisions live in the repo's `docs/adr/` (ADRs win over the older PRD where they conflict):

- **0001** Engine-first scope — v1 is the pipeline only.
- **0002** Shared tool library + thin MCP adapter.
- **0003** Four-agent decomposition, each independently evaluable.
- **0004** Hand-rolled async orchestrator over a framework.
- **0005** Disciplined partial Brief under a budget.
- **0006** Uncertainty posture — entity resolution halts on ambiguity; represent uncertainty (Confidence / Conflict / Coverage) everywhere else rather than halting.

## Key docs (in the repo)

- `CONTEXT.md` — the fixed domain language (authoritative for naming).
- `Competitive_Intelligence_Agent_PRD.md` — the spec; milestones M1-M3, user stories US-001 through US-022.
- `docs/adr/` — the six architecture decisions.
- `.github/workflows/eval-gate.yml` — the CI eval gate.

## How Claude helps

This is a **built, production-shaped portfolio project** (like Agentic RAG, not HabitLoop's tutor mode). Help here means code review, polishing, eval-design critique, documentation, demo prep, and especially translating the citation-judge and release-gate work into interview talking points and resume / portfolio framing for the AI Evals job search.

## Daily tracking (optional)

Not daily-tracked by default. To log progress, say "log my CompeteIntel progress" and the `daily-log` skill will create `projects/CompeteIntel/log/<date>.md` on first use.
