---
type: wiki-readme
mode: full
date: 2026-07-03
---

# YouTube-Transcript Wiki

A persistent, compounding, interlinked set of markdown pages that Claude builds and maintains from immutable raw sources, read and edited in Obsidian.
Knowledge is compiled once per source and then kept current, so cross-references and synthesis accumulate here instead of scattering across one-off notes.

This wiki's **domain is AI engineering** (LLMs, agents, RAG, evals, prompting, and adjacent production-AI topics).
Its **input diet is video transcripts** from talks, conference sessions, and tutorials.
"YouTube_transcript" names the medium, not the domain: the wiki is scoped to AI-engineering knowledge so it compounds coherently, and it cross-links to the evals and Agentic RAG wikis rather than overlapping them.

## Mode: full

This is a knowledge-capture wiki (turn hours of video into durable, interlinked, interview-ready notes), not an hcho-authored learning wiki, so it runs in `mode: full`:

- **Claude** drafts and maintains every page, including the concept `## Synthesis` sections and `synthesis.md`.
- **hcho** reviews and refines rather than authoring from scratch.

One exception: interview talking points do not live here.
They consolidate into the single job-search prep surface at `projects/job-search/interview-prep.md` (the `## AI Engineering (from talks & tutorials)` section), which `synthesis.md` points to, so talking points are not duplicated across wikis.

## Concepts grow organically

Unlike the evals pilot (curriculum-anchored) and the Agentic RAG wiki (project-anchored), this wiki seeds **no** concept backbone.
The `concepts/` directory ships empty, and each concept page is **created by the first ingest that touches it**.
This fits an open-ended video diet with no fixed curriculum: the graph accretes to match whatever the videos actually teach, so early on the index will be short, and that is expected.

When a transcript covers a topic the evals or Agentic RAG wiki already owns, the concept page should `[[link]]` across to that wiki's page rather than duplicating it, keeping the three wikis complementary.

## Page types

- `sources/<slug>.md` - one summary per ingested transcript (key claims, connections, provenance including the video title, channel, and URL).
- `concepts/<slug>.md` - one page per AI-engineering concept, created on the fly by the ingest that first covers it; accumulates across sources.
- `index.md` - the catalog of every page, grouped by category.
- `log.md` - the dated event log of ingests and other operations.
- `synthesis.md` - the thesis tying the concepts together. Start here for the through-line.
- `raw/` (sibling of `wiki/`) - the immutable inbox of original transcripts. Read but never edited after first save.

## Conventions

- **Filenames:** kebab-case (`prompt-caching.md`).
- **Links:** `[[wikilinks]]` for every cross-reference between pages.
- **Frontmatter:** every concept and source page carries YAML frontmatter with at least `type`, `tags`, `date`, and `source-count`; concept pages also carry `status`.

## Obsidian setup (manual, one-time)

`/Users/hcho/Mandu` is already an Obsidian vault (opened for the evals pilot), so the graph view, backlinks, Web Clipper, and Dataview over the frontmatter all work here with no extra infrastructure.
Optionally point Web Clipper's save path at this wiki's `raw/` when capturing a transcript from YouTube's transcript panel.
