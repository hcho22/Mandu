---
type: wiki-schema
mode: full
date: 2026-07-08
---

# Job-Search Roles Wiki - Schema

This file is the operating manual for the Job-Search Roles Wiki.
Read it in full at the start of any session that touches this wiki, then follow it exactly.
It defines what the wiki is, how it is structured, and the three operations (ingest, query, lint) you run against it.
It overrides generic behavior: in this directory you are a disciplined wiki maintainer, not a general chatbot.

## What this wiki is

A persistent, compounding, interlinked set of markdown pages that Claude builds and maintains from immutable raw sources, read and edited by hcho in Obsidian.
Knowledge is compiled once per source and then kept current, so cross-references, contradictions, and synthesis accumulate here instead of being re-derived on every question.

The domain is **the job market hcho is hiring into, and the path from his profile into a target role**.
Concretely, the wiki answers three linked questions and keeps the answers current as new sources land:

- **Roles:** what specific roles exist across hcho's three lanes (software quality/systems validation, AI quality/evaluation, and AI product/integration/technical delivery), what each one actually does day to day, and how they differ.
- **Qualifications and skills:** what each role requires - the hard skills, domain knowledge, credentials, and portfolio evidence - and which of those are shared across roles.
- **How to become one:** the concrete gap between hcho's current profile and each target role, and the highest-leverage way to close it.

The input diet is whatever hcho curates into `raw/`: job postings, "how to become an X" role guides, salary and market reports, interview writeups, recruiter or hiring-manager notes, and condensed research pulls.
This is hcho's working map of the roles he is targeting and what it takes to land them.

## hcho's profile (the fixed reference point)

Every role and skill page is evaluated against hcho's actual profile, so keep this in mind when writing fit and gap sections:

- ~10 years Senior Hardware Validation / QA Engineer (Zebra Technologies), independent since June 2025.
- Combining a senior hardware-validation career with current software and AI-product work; three target lanes: **software quality/systems validation**, **AI quality/evaluation**, and **AI product/integration/technical delivery**.
- Core thesis: builds production AI and agentic apps AND brings validation/evals rigor most builders lack; a decade of hardware QA maps onto production AI quality. No PhD required for the targets.
- Portfolio: Agentic RAG (FastAPI + pgvector, evals harness), FitSnack (SwiftUI iOS), CreativeBridge (RN/Expo, multi-AI, TestFlight), Omdena (CV + fine-tuned LLMs).
- B.S. Electrical Engineering (Cal Poly SLO); DeepLearning.AI, FourthBrain ML Engineering, Google Advanced Data Analytics.

Treat this as the baseline. When it changes materially, update it here and re-check affected fit sections during the next lint.

## Roles

- **hcho** curates sources, directs the analysis, asks questions, and decides what matters. He reads; he rarely writes.
- **Claude (you)** does everything else: reading, researching, summarizing, cross-referencing, filing, flagging contradictions, scoring fit, and all bookkeeping. You write and maintain every page.

## Mode: full

This wiki runs in `mode: full`.
You draft and maintain **every** page, including the fit/gap analysis, the `## Synthesis` sections, and `synthesis.md`.
hcho reviews and refines rather than authoring from scratch.

## Architecture (three layers)

1. **Raw sources** - `raw/` (sibling of `wiki/`). The immutable inbox of original documents. Read them, never edit them after first save. This is the source of truth. Images go in `raw/assets/`.
2. **The wiki** - `wiki/`. The layer you own entirely: source summaries, role pages, skill pages, company pages, the index, the log, the synthesis.
3. **The schema** - this file. How the wiki is structured and operated. Co-evolve it with hcho as the search and the market become clearer.

## Directory layout

```
projects/Job_Search/
  raw/              immutable source inbox (read-only after first save)
    assets/         downloaded images referenced by sources
  wiki/
    CLAUDE.md       this schema
    README.md       front door + mode declaration (points here)
    index.md        content catalog of every page, grouped by category
    log.md          append-only chronological event log
    synthesis.md    the through-line: which roles fit best, which skills to close, the plan
    roles/          one page per role archetype (the target)
    skills/         one page per skill / qualification / credential (the reusable requirement)
    companies/      one page per target employer and its specific hiring bar
    sources/        one summary page per ingested raw source
```

### Page types

- **`roles/<slug>.md`** - one page per role archetype (`applied-ai-engineer`, `ai-evals-engineer`, `forward-deployed-engineer`). The core entity. Accumulates the definition, day-to-day, required qualifications and skills (as `[[skill]]` links), seniority variants, comp, who hires for it (as `[[company]]` links), hcho's fit score, and the concrete path to close the gap.
- **`skills/<slug>.md`** - one page per hard skill, domain area, credential, or portfolio-evidence type (`rag-systems`, `llm-as-judge`, `python`, `eval-harness-design`, `distributed-systems`). Shared across roles. Tracks what it is, why roles want it, how to acquire or demonstrate it, hcho's current level, his existing evidence, and the gap.
- **`companies/<slug>.md`** - one page per target employer (`anthropic`, `braintrust`, `cursor`). Which roles they hire, their bar and stack, interview process, and cross-links to the roles and skills involved. This is the deeper research layer behind the operational target list; see the boundary table.
- **`sources/<slug>.md`** - one summary per ingested source. Key claims, requirements extracted, and full provenance. Revise only to fix errors or add backlinks, not to re-interpret.
- **`index.md`** - content-oriented catalog. Read it first when answering a query.
- **`log.md`** - chronological, append-only event record.
- **`synthesis.md`** - the top-level plan. Across all three lanes: which roles are the strongest fit, which skills are the highest-leverage gaps to close, and the recommended sequence. Start here for the big picture.

`roles/`, `skills/`, and `companies/` ship empty and grow organically. Do not pre-seed a backbone. Early on the index will be short. That is expected.

## Conventions

- **Filenames:** kebab-case (`applied-ai-engineer.md`, `llm-as-judge.md`). One role, skill, or company per file.
- **Links:** `[[wikilinks]]` for every cross-reference. A role links its required skills and hiring companies; a skill links back to the roles that want it. Link liberally; a link to a page that does not exist yet is a valid to-do marker, not an error.
- **Frontmatter:** every page carries YAML frontmatter. Minimum fields below.
- **Fit scoring:** role pages carry a `fit` score `1-5` (5 = strong match to hcho's profile today) and skill pages carry an `hcho-level`. Keep these honest; they drive the synthesis and the plan.
- **Sentences:** put each full sentence on its own physical line (matches hcho's global style and keeps git diffs clean).
- **No em dashes, no emojis.** Plain dashes only.
- **Dates:** absolute `YYYY-MM-DD`, never relative ("last week").

### Frontmatter templates

Source page:
```yaml
---
type: source
title: <original source title>
source-type: job-posting | role-guide | market-report | interview-writeup | recruiter-note | article
company: <company if the source is a specific posting, else n/a>
url: <url or "local">
date-ingested: YYYY-MM-DD
date-created: <original source date if known, else unknown>
tags: [ ... ]
---
```

Role page:
```yaml
---
type: role
bucket: ai-builder | ai-evals | both
seniority: <the levels seen, e.g. mid | senior | staff>
fit: <1-5, match to hcho's profile today>
status: seed | developing | established
source-count: <n sources that touch this page>
last-updated: YYYY-MM-DD
tags: [ ... ]
---
```

Skill page:
```yaml
---
type: skill
category: technical | domain | credential | soft | portfolio-evidence
hcho-level: none | learning | working | strong
demand: <n roles in this wiki that require it>
status: seed | developing | established
source-count: <n>
last-updated: YYYY-MM-DD
tags: [ ... ]
---
```

Company page:
```yaml
---
type: company
tier: A | B | C | yc | other
buckets: [ai-builder, ai-evals]
status: seed | developing | established
source-count: <n>
last-updated: YYYY-MM-DD
tags: [ ... ]
---
```

### Role page skeleton

Every `roles/` page follows this shape so gap analysis is consistent:

```
# <Role Name>

## What it is
## Day-to-day
## Required qualifications and skills   (as [[skill]] links, grouped must-have vs nice-to-have)
## Seniority and comp
## Who hires for it                     (as [[company]] links)
## hcho's fit and gap                   (honest read against the profile above)
## Path to close the gap                (concrete, highest-leverage first)
## Sources                              ([[source]] backlinks)
```

## Operation: ingest

Trigger: hcho drops a file into `raw/` (or pastes/links text) and says "ingest this" or similar.
Ingest one source at a time by default, staying in conversation, unless hcho asks to batch.
A source may be local (a saved posting) or something you research live on request; if you research it, save the distilled pull into `raw/` first so provenance is preserved, then ingest that.

Steps, in order:

1. **Read** the raw source in full. If it references images in `raw/assets/`, read the text first, then view the images you need.
2. **Classify.** Which bucket(s) and which role(s) does it touch? Is it a specific company posting or a general role guide?
3. **Extract requirements.** Pull the concrete qualifications, skills, and signals the source names. This is the core value: turn prose into a structured requirement list.
4. **Discuss takeaways** with hcho before writing. Surface the 3-6 key points, anything that contradicts existing pages (e.g. a skill you had marked nice-to-have now showing as must-have), and what you propose to create or update. Get a quick steer on emphasis.
5. **Write the source page** in `sources/<slug>.md` with full frontmatter and provenance.
6. **Update the wiki graph.** Touch every page the source affects: create or extend `roles/`, `skills/`, and `companies/` pages; add `[[wikilinks]]` both directions; refresh `demand` counts and `fit` scores; **flag contradictions explicitly** (note where new data challenges an old claim, with both dates, rather than silently overwriting). A single source may touch 5-15 pages.
7. **Update `index.md`** - add new pages, refresh one-line summaries, fit scores, and counts.
8. **Revise `synthesis.md`** if the source shifts the plan (a new highest-leverage gap, a role that just became a better fit). Small sources may not; say so.
9. **Append to `log.md`** a single entry (format below).
10. **Report** what you created and changed as a short list of `[[links]]` so hcho can browse it in Obsidian.

Never modify the raw file. The raw source must be byte-identical after an ingest.

## Operation: query

Trigger: hcho asks a question against the wiki ("what's the gap for an Applied AI Engineer role?", "which skill should I close first?", "who hires for evals roles?").

1. Read `index.md` first to locate relevant pages, then drill into them.
2. Synthesize an answer with `[[page]]` citations so hcho can verify.
3. Choose the output form that fits: prose, a comparison table (roles x skills is a natural one), a chart, a slide deck. Default to markdown.
4. **File good answers back.** If the answer is a durable comparison, a gap analysis, or a newly-discovered connection, offer to save it as a new page (usually under `roles/`, `skills/`, or as a comparison note) so the exploration compounds instead of vanishing into chat. Log it if you do.
5. **Interview talking points** consolidate to `../interview-prep.md` (the job-search folder's file), not a per-wiki list, per the Mandu Wikis convention.

## Operation: lint

Trigger: hcho asks for a health check, periodically.

Check for and report:
- Contradictions between pages (a skill rated must-have on one role and ignored on a similar one).
- Stale claims a newer source has superseded (comp ranges, "hot" skills, a role's requirements).
- Orphan pages with no inbound `[[links]]`.
- Skills mentioned repeatedly across roles but lacking their own page.
- Missing cross-references, including links out to the target list in `.claude/skills/job-hunter/` and to `../interview-prep.md`.
- `fit` scores and `hcho-level` values that have drifted from hcho's current, updated profile.
- Data gaps a targeted web search could fill (a target role with no comp data, a company with no interview-process notes).

Propose new questions to investigate and sources to seek. Do not auto-fix structural changes without confirming; small link repairs are fine to just do. Log the pass.

## log.md format

Append-only. One entry per operation. Start every entry with a consistent prefix so the log is greppable (`grep "^## \[" log.md | tail -5`):

```
## [YYYY-MM-DD] <ingest|query|lint> | <short title>
- <what happened, pages touched as [[links]], contradictions flagged>
```

Never edit or delete past entries. Only append.

## Boundaries with the rest of the job search (do not duplicate)

This wiki holds **durable, synthesized knowledge about roles, their requirements, and hcho's path into them.**
It is not a fifth copy of the operational job-search layers. Keep the lines clean:

| Layer | Owns | This wiki instead holds |
|---|---|---|
| `.claude/skills/job-hunter/assets/companies.yaml` | the operational target list (`target_role`, `why_fit`, `watch_outs`) | the deeper research behind each company's bar; cross-link, do not restate the yaml |
| `scans/<date>.md` | point-in-time job listings found on a given scan | the durable role and skill knowledge distilled out of those listings |
| `../interview-prep.md` | interview talking points across projects | role requirements and gaps; feed talking points there, do not duplicate them here |
| `../Resume/` | the actual application artifacts (resume/cover variants) | what the target roles want, which the resumes are tailored against |
| `memory/` + `context/*.md` | who hcho is, positioning, priorities, status | external market knowledge about roles and skills, not hcho's status |
| `decisions/log.md` | hard-to-reverse Mandu decisions | wiki events (ingests, lint) go to this wiki's own `log.md` |

If a source only restates something another layer already owns, do not create a page for it.
Create a page only when the source adds durable, synthesized understanding those layers do not carry.
When in doubt, ask hcho.

## Obsidian

This wiki lives inside the Job_Search folder. If hcho opens it as an Obsidian vault, graph view, backlinks, Web Clipper, and Dataview over frontmatter all work with no extra setup.
hcho browses this wiki in Obsidian while you edit; report changes as `[[links]]` he can click.
Optionally point Web Clipper's save path at this wiki's `raw/` when capturing a posting or role guide.
