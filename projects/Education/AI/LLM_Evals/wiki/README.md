---
type: wiki-readme
mode: split
date: 2026-06-06
---

# Evals Wiki

A persistent, compounding, interlinked set of markdown pages that Claude builds and maintains from immutable raw sources, read and edited in Obsidian. Knowledge is compiled once per source and then kept current, so cross-references and synthesis accumulate here instead of scattering across one-off notes.

## Mode: split

This is a learning wiki, so it runs in `mode: split`:

- **Claude** does the bookkeeping and neutral skeletons: source summaries, concept definitions, cross-links, the index, and the log.
- **hcho** writes the synthesis: the `## In my own words (hcho)` section on each concept page and all of `synthesis.md`.

Claude never writes the `## In my own words (hcho)` sections or `synthesis.md` on this wiki.

## Page types

- `sources/<slug>.md` — one summary per ingested raw source (key claims, connections, provenance).
- `concepts/<slug>.md` — one page per evals concept; accumulates across sources.
- `index.md` — the catalog of every page, grouped by category.
- `log.md` — the dated event log of ingests and other operations.
- `synthesis.md` — hcho's thesis tying the concepts together. Start here for the through-line; it is the point of the wiki.
- `raw/` (sibling of `wiki/`) — the immutable inbox of original sources. Read but never edited after first save.

## Conventions

- **Filenames:** kebab-case (`llm-as-judge.md`).
- **Links:** `[[wikilinks]]` for every cross-reference between pages.
- **Frontmatter:** every concept and source page carries YAML frontmatter with at least `type`, `tags`, `date`, and `source-count`.

## Obsidian setup (manual, one-time)

Open `/Users/hcho/Mandu` as an Obsidian vault to get the graph view, backlinks, Web Clipper (capture into `raw/`), and Dataview over the frontmatter. The wiki is plain markdown in git, so no other infrastructure is required. Optionally point Web Clipper's save and attachment paths at this wiki's `raw/`.
