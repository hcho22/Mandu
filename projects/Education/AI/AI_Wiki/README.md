# AI_Wiki

Status: active (schema retuned + first ingest 2026-07-08).
Type: personal knowledge base (LLM Wiki pattern), not a product bet.

hcho's broad AI-engineering knowledge base and primary "second brain" for the AI-native career pivot.
Domain: the craft (LLMs, agents, RAG, evals, prompting, production-AI patterns) and the career (solo building, positioning, the job market, the skills that matter).
Claude builds and maintains every page from immutable raw sources; hcho curates sources and reads the results in Obsidian (this directory is its own vault).

Reference layer that cross-links to the specialized wikis (evals pilot, Agentic RAG, YouTube-transcript) rather than duplicating them.

## Layout

- `wiki/CLAUDE.md` - the schema (full operating rules). Read first every session.
- `wiki/README.md` - front door and mode declaration (`mode: full`).
- `wiki/index.md` - catalog of every page.
- `wiki/log.md` - append-only event log.
- `wiki/synthesis.md` - the top-level through-line.
- `wiki/{sources,entities,concepts,areas}/` - the pages.
- `raw/` - immutable source inbox (with `raw/assets/` for images). 22 sources curated, ingesting one at a time.

## Operations

- **ingest**: drop a source into `raw/`, say "ingest this". Claude reads it, discusses takeaways, writes a source page, updates entity/concept/area pages and the index, and logs the pass.
- **query**: ask a question; Claude answers from the wiki with citations and can file good answers back as pages.
- **lint**: periodic health check for contradictions, stale claims, orphans, and gaps.

## Key dates

- 2026-07-08: schema retuned from the generic Second Brain scaffold to an AI-engineering + AI-career KB; consolidated onto this directory (the empty `projects/SecondBrain/` dup retired). First source ingested (Hamel Husain, "Your AI Product Needs Evals").
