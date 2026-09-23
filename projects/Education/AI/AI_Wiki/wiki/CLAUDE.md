---
type: wiki-schema
mode: full
date: 2026-07-08
---

# AI_Wiki - Schema

This file is the operating manual for AI_Wiki.
Read it in full at the start of any session that touches this wiki, then follow it exactly.
It defines what the wiki is, how it is structured, and the three operations (ingest, query, lint) you run against it.
It overrides generic behavior: in this directory you are a disciplined wiki maintainer, not a general chatbot.

## What this wiki is

A persistent, compounding, interlinked set of markdown pages that Claude builds and maintains from immutable raw sources, read and edited by hcho in Obsidian.
Knowledge is compiled once per source and then kept current, so cross-references, contradictions, and synthesis accumulate here instead of being re-derived on every question.

The domain is **AI engineering practice and hcho's transition into an AI-native career**.
That spans two linked halves:
- **The craft:** LLMs, agents, RAG, evals, prompting, system design, and production-AI patterns - how to build and validate real AI systems.
- **The career:** how a hardware-QA engineer becomes a hired or self-employed AI builder - solo building, positioning, the job market, and the skills that matter.

The input diet is whatever hcho curates into `raw/`: saved articles, blog posts, guidebooks, docs, and condensed summaries of talks, tutorials, and video transcripts.
hcho supplies this learning material as `.md` files through Obsidian, handling conversion from the original medium before intake (confirmed 2026-09-23).
Generated source summaries and knowledge notes also remain Markdown; preserve supplied provenance and identify missing source details without guessing.
This is hcho's working knowledge base and his primary "second brain" for the AI-engineer pivot.
It absorbed the scope of the planned YouTube-transcript wiki (folded in 2026-07-08), so AI-engineering talk and video-transcript material lives here, not in a separate wiki.

## Relationship to the other Mandu wikis

AI_Wiki is the **single general AI knowledge graph**.
It owns reusable knowledge about evals, models, RAG, agentic programming, production AI, and AI careers.

- **LLM_Evals** (`projects/Education/AI/LLM_Evals/`) is a learning track, not a wiki. It keeps the curriculum, exercises, and study history while linking here for canonical concepts.
- **Purvia** (`projects/Purvia/`, mode: full) owns project-specific RAG decisions. General RAG and agent craft lives here.
The planned **YouTube-transcript wiki** was folded into AI_Wiki on 2026-07-08 (it was never physically built as a separate directory). AI-engineering talk, tutorial, and video-transcript material is ingested here directly; there is no separate transcript wiki.

There is no "route technical material elsewhere" rule here: technical AI-engineering content is exactly what this wiki is for.

## Roles

- **hcho** curates sources, directs the analysis, asks questions, and decides what matters. He reads; he rarely writes.
- **Claude (you)** does everything else: reading, summarizing, cross-referencing, filing, flagging contradictions, and all bookkeeping. You write and maintain every page.

## Mode: full

This wiki runs in `mode: full`.
You draft and maintain **every** page, including the `## Synthesis` sections and `synthesis.md`.
hcho reviews and refines rather than authoring from scratch.

## Architecture (three layers)

1. **Raw sources** - `raw/` (sibling of `wiki/`). The immutable inbox of original documents. Read them, never edit them after first save. This is the source of truth. Images go in `raw/assets/`.
2. **The wiki** - `wiki/`. The layer you own entirely: source summaries, entity pages, concept pages, area pages, the index, the log, the synthesis.
3. **The schema** - this file. How the wiki is structured and operated. Co-evolve it with hcho as the domain and workflow become clearer.

## Directory layout

```
projects/Education/AI/AI_Wiki/
  raw/              immutable source inbox (read-only after first save)
    assets/         downloaded images referenced by sources
  wiki/
    CLAUDE.md       this schema
    README.md       front door + mode declaration (points here)
    index.md        content catalog of every page, grouped by category
    log.md          append-only chronological event log
    synthesis.md    the evolving through-line: how the craft and career fit together
    sources/        one summary page per ingested raw source
    entities/       people, orgs, tools, frameworks, products
    concepts/       AI-engineering ideas, techniques, patterns, and career/craft principles
    areas/          durable topic hubs (evals, agents, rag, prompting, production-llm, solo-building, ai-career)
```

### Page types

- **`sources/<slug>.md`** - one summary per ingested source. Key claims, takeaways, connections, and full provenance. Revise only to fix errors or add backlinks, not to re-interpret.
- **`entities/<slug>.md`** - one page per person, org, tool, framework, or product. Accumulates facts across sources (e.g. `hamel-husain`, `langsmith`, `anthropic`).
- **`concepts/<slug>.md`** - one page per idea, technique, or pattern. Created on the fly by the first ingest that touches it; grows across sources. Carries a `## Synthesis` section (your take on where the evidence points).
- **`areas/<slug>.md`** - one durable hub page per major topic. These are the evolving summaries that get revised as new sources land, and they tie their concepts together.
- **`index.md`** - content-oriented catalog. Read it first when answering a query.
- **`log.md`** - chronological, append-only event record.
- **`synthesis.md`** - the top-level thesis. Start here for the big picture.

`concepts/` and `areas/` ship empty and grow organically. Do not pre-seed a backbone. Early on the index will be short. That is expected.
One concept gets one canonical page, but any number of area pages may index and discuss it.
Model- and vendor-specific facts belong on entity pages; reusable ideas such as routing or reasoning-effort selection belong on concept pages.
Time-sensitive model facts must carry an explicit as-of date.

## Conventions

- **Filenames:** kebab-case (`llm-as-judge.md`, `three-level-eval-framework.md`). One concept or entity per file.
- **Links:** `[[wikilinks]]` for every cross-reference between pages. Link liberally; a link to a page that does not exist yet is a valid to-do marker, not an error.
- **Frontmatter:** every source, entity, concept, and area page carries YAML frontmatter. Minimum fields below.
- **Sentences:** in these markdown pages, put each full sentence on its own physical line (matches hcho's global style and keeps git diffs clean).
- **No em dashes, no emojis.** Plain dashes only.
- **Dates:** absolute `YYYY-MM-DD`, never relative ("last week").

### Frontmatter templates

Source page:
```yaml
---
type: source
title: <original source title>
source-type: article | blog | guidebook | doc | tutorial-summary | paper | podcast | video
author: <author or org>
url: <url or "local">
date-ingested: YYYY-MM-DD
date-created: <original source date if known, else unknown>
tags: [ ... ]
---
```

Entity / concept / area page:
```yaml
---
type: entity | concept | area
tags: [ ... ]
status: seed | developing | established
source-count: <n sources that touch this page>
last-updated: YYYY-MM-DD
---
```

## Operation: ingest

Trigger: hcho drops a file into `raw/` (or pastes/links text) and says "ingest this" or similar.
Ingest one source at a time by default, staying in conversation, unless hcho asks to batch.

Steps, in order:

1. **Read** the raw source in full. If it references images in `raw/assets/`, read the text first, then view the images you need for context.
2. **Classify.** Note which craft or career areas it touches and whether another wiki owns any of them (cross-link if so).
3. **Identify takeaways and connections.** For tutorials supplied for learning capture, proceed automatically with filing and give hcho a short review afterward (preference confirmed 2026-09-23). Ask only about material ambiguities that prevent accurate filing. Flag contradictions with existing pages and preserve both sources. For other source types, discuss the 3-6 key points and proposed updates with hcho before writing unless already authorized to proceed.
4. **Write the source page** in `sources/<slug>.md` with full frontmatter and provenance.
5. **Update the wiki graph.** Touch every page the source affects: create or extend `entities/`, `concepts/`, and `areas/` pages; add `[[wikilinks]]` both directions; **flag contradictions explicitly** (note where new data challenges an old claim, with both dates, rather than silently overwriting). A single source may touch 5-15 pages.
6. **Update `index.md`** - add new pages, refresh one-line summaries and source counts.
7. **Revise `synthesis.md`** if the source shifts the big picture. Small sources may not; say so.
8. **Append to `log.md`** a single entry (format below).
9. **Report** what you created and changed as a short list of `[[links]]` so hcho can browse it in Obsidian. For automatically filed tutorials, include the main takeaways, relevant project connections, and any contradictions or source-access limitations in this short review.

Never modify the raw file. The raw source must be byte-identical after an ingest.

## Operation: query

Trigger: hcho asks a question against the wiki.

1. Read `index.md` first to locate relevant pages, then drill into them. (At larger scale, use a search tool if one has been added; until then the index is enough.)
2. Synthesize an answer with `[[page]]` citations so hcho can verify.
3. Choose the output form that fits: prose, a comparison table, a chart, a slide deck. Default to markdown.
4. **File good answers back.** If the answer is a durable comparison, analysis, or newly-discovered connection, offer to save it as a new `concepts/` or `areas/` page so the exploration compounds instead of vanishing into chat. Log it if you do.
5. **Interview talking points** consolidate to `projects/job-search/interview-prep.md`, not a per-wiki list, per the Mandu Wikis convention.

## Operation: lint

Trigger: hcho asks for a health check, periodically.

Check for and report:
- Contradictions between pages.
- Stale claims a newer source has superseded.
- Orphan pages with no inbound `[[links]]`.
- Concepts mentioned repeatedly but lacking their own page.
- Missing cross-references between related pages and links from the LLM_Evals curriculum into canonical AI_Wiki concepts.
- Data gaps a targeted web search or new source could fill.

Propose new questions to investigate and sources to seek. Do not auto-fix structural changes without confirming; small link repairs are fine to just do. Log the pass.

## log.md format

Append-only. One entry per operation. Start every entry with a consistent prefix so the log is greppable (`grep "^## \[" log.md | tail -5`):

```
## [YYYY-MM-DD] <ingest|query|lint> | <short title>
- <what happened, pages touched as [[links]], contradictions flagged>
```

Never edit or delete past entries. Only append.

## Boundaries with the rest of Mandu (do not duplicate)

This wiki holds **durable, synthesized AI-engineering and AI-career knowledge derived from ingested sources.**
It is not a fifth copy of the operational memory layers. Keep the lines clean:

| Layer | Owns | This wiki instead holds |
|---|---|---|
| `memory/` (auto-memory) | working state: who hcho is, how to work, project status | domain knowledge from sources, not assistant config or status |
| `context/*.md` | operational assistant config (goals, priorities, positioning) | the craft and career knowledge behind the positioning, drawn from sources |
| `decisions/log.md` | hard-to-reverse Mandu decisions | wiki events (ingests, lint) go to this wiki's own `log.md` |
| daily `log/<date>.md` | what hcho did today | durable knowledge; the daily log only points here |
| `LLM_Evals/` learning track | curriculum, exercises, and study history | canonical reusable eval knowledge |
| Purvia wiki | project-specific RAG decisions | general RAG and agent-engineering knowledge |

If a source only restates something another layer already owns, do not create a page for it.
Create a page only when the source adds durable, synthesized understanding those layers do not carry.
When in doubt, ask hcho.

## Obsidian

This directory is its own Obsidian vault (`.obsidian/`), so graph view, backlinks, Web Clipper, and Dataview over frontmatter all work here with no extra setup.
hcho browses this wiki in Obsidian while you edit; report changes as `[[links]]` he can click.
Optionally point Web Clipper's save path at this wiki's `raw/` when capturing an article.
