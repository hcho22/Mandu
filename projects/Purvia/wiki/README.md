---
type: wiki-readme
mode: full
date: 2026-06-15
---

# Agentic RAG Wiki

A persistent, compounding, interlinked set of markdown pages that Claude builds and maintains from immutable raw sources, read and edited in Obsidian. Knowledge is compiled once per source and then kept current, so cross-references and synthesis accumulate here instead of scattering across one-off notes.

This is the knowledge base for the **Agentic RAG** project, the flagship portfolio piece for the AI Evals / Quality Engineer target. It accumulates both the project's own design and eval decisions (from its `docs/` deep-dives) and the external research that informs them (RAG-eval papers, RAGAS docs, reranker and judge literature).

## Mode: full

This is a built portfolio project, not a learning track, so it runs in `mode: full`:

- **Claude** drafts and maintains every page, including the concept `## Synthesis` sections and `synthesis.md`.
- **hcho** reviews and refines rather than authoring from scratch.

One exception: interview talking points do not live here. They consolidate into the single job-search prep surface at `projects/job-search/interview-prep.md`, which `synthesis.md` points to, so talking points are not duplicated across wikis.

## Page types

- `sources/<slug>.md` — one summary per ingested raw source (key claims, connections, provenance).
- `concepts/<slug>.md` — one page per Agentic RAG concept, anchored to a project component or deep-dive doc; accumulates across sources.
- `index.md` — the catalog of every page, grouped by category.
- `log.md` — the dated event log of ingests and other operations.
- `synthesis.md` — the thesis tying the concepts together. Start here for the through-line.
- `raw/` (sibling of `wiki/`) — the immutable inbox of original sources. Read but never edited after first save.

## Conventions

- **Filenames:** kebab-case (`permissions-aware-retrieval.md`).
- **Links:** `[[wikilinks]]` for every cross-reference between pages.
- **Frontmatter:** every concept and source page carries YAML frontmatter with at least `type`, `tags`, `date`, and `source-count`; concept pages also carry `status` and a `component:` field mapping the page to its project module or deep-dive doc.

## Obsidian setup (manual, one-time)

`/Users/hcho/Mandu` is already an Obsidian vault (opened for the evals pilot), so the graph view, backlinks, Web Clipper, and Dataview over the frontmatter all work here with no extra infrastructure. Optionally point Web Clipper's save and attachment paths at this wiki's `raw/` when capturing external sources.
