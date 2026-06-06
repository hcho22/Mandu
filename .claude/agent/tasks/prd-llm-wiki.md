# PRD: LLM Wiki (Evals Pilot + Replicable Template)

## Introduction

Bring the "LLM Wiki" pattern into Mandu. An LLM Wiki is a persistent, compounding, interlinked
collection of markdown files that the assistant (Claude) builds and maintains from immutable raw
sources, viewed and edited in Obsidian. Unlike RAG (which re-derives knowledge from raw documents
on every query), the wiki is compiled once per source and then kept current, so cross-references,
contradictions, and synthesis accumulate instead of scattering.

Today Mandu already has most of the skeleton (a schema in `CLAUDE.md` + `context/`, topic pages in
project READMEs, a decision log, daily logs, persistent memory). What is missing is the part that
makes knowledge compound: a raw-source inbox, an ingest workflow, interlinking plus an index,
query results filed back as pages, and a lint pass.

This PRD scopes one deliverable shipped as a single PR: a working **pilot wiki** for the evals
learning track, built as a **replicable template** (structure + ingest skill + schema) so the
pattern can later clone to other projects. It directly serves the #1 goal: landing an AI evals /
quality engineering role while building and learning production-quality work. The evals wiki both
builds the core skill and produces the Q3 2026 "demonstrable eval writeup."

This PRD assumes the design decisions resolved in the prior grilling session (see
`/Users/hcho/.claude/plans/llm-wiki-a-curried-koala.md`).

## Goals

- Stand up a self-contained evals wiki under `projects/Learning/AI Engineer/evals/` with a
  `raw/` inbox and an LLM-maintained `wiki/` directory.
- Ship an `ingest` skill that turns one raw source into updated wiki pages in a single pass,
  mirroring the existing `daily-log` skill's structure and safety discipline.
- Encode the wiki conventions and de-duplication rules in `CLAUDE.md` so the pattern is repeatable
  and does not become a fifth redundant memory layer.
- Preserve learning value on this (learning) wiki via SPLIT mode: Claude does bookkeeping and
  neutral skeletons; hcho writes the synthesis and thesis.
- Prove the loop end-to-end by ingesting one real source with all derived pages updated.

## User Stories

### US-001: Scaffold the evals wiki skeleton

**Description:** As hcho, I want the `raw/` inbox and `wiki/` directory created under the evals
track so sources have a home and the assistant has a place to write maintained pages.

**Acceptance Criteria:**

- [x] Create `projects/Learning/AI Engineer/evals/raw/` with a `.gitkeep`.
- [x] Create `projects/Learning/AI Engineer/evals/wiki/` containing `README.md`, `index.md`,
      `log.md`, `synthesis.md`, and the subdirectories `sources/` and `concepts/` (each with a
      `.gitkeep`).
- [x] `wiki/README.md` documents: `mode: split`, the page types, the conventions (kebab-case,
      `[[wikilinks]]`, YAML frontmatter), a pointer to `synthesis.md` as the thesis, and the manual
      Obsidian setup step.
- [x] `wiki/index.md` exists with category headers (Sources, Concepts, Synthesis) and is empty of
      entries except the seeded concept stubs (see US-002).
- [x] `wiki/log.md` exists with a one-line header explaining the entry prefix convention
      `## [YYYY-MM-DD] <op> | <title>`.
- [x] `wiki/synthesis.md` is a stub with section headers only: `## Thesis (one paragraph, my words)`,
      `## How the concepts connect`, `## Open questions`, `## Interview talking points`. No prose
      written by Claude.
- [x] Existing `README.md`, `learning-plan.md`, and `log/` in that folder are untouched.

**Validation Test:**

- **Setup:** Repo on a feature branch, evals folder present.
- **Steps:**
  1. Run `ls -R "projects/Learning/AI Engineer/evals"`.
  2. Open `wiki/README.md` and `wiki/synthesis.md`.
- **Expected Result:** `raw/` and `wiki/` (with the five files + two subdirs) exist; README states
  `mode: split`; `synthesis.md` has the four headers and no body text.
- **Failure Indicator:** Any directory or file missing, README missing the mode, or `synthesis.md`
  pre-filled with Claude-written synthesis.

### US-002: Seed the 10 concept-page stubs (mapped to S1-S10)

**Description:** As hcho, I want the 10 high-leverage evals concepts pre-created as empty skeletons
so the wiki mirrors my learning-plan curriculum and gives ingestion a target to attach to.

**Acceptance Criteria:**

- [x] Create 10 files in `wiki/concepts/`, kebab-case, one per concept, mapped to Sessions S1-S10
      in `learning-plan.md`: `offline-vs-online-evals`, `classification-metrics`,
      `data-leakage-and-splits`, `llm-benchmarks-contamination`, `llm-as-judge`, `rag-evaluation`,
      `production-eval-tooling`, `hallucination-safety-redteam`, `agent-eval-and-stats`,
      `ci-eval-gates-and-drift`.
- [x] Each file has YAML frontmatter: `type: concept`, `tags`, `date`, `source-count: 0`,
      `status: stub`, and a `session:` field referencing its S1-S10 mapping.
- [x] Each file body contains a one-line neutral definition placeholder and a
      `## In my own words (hcho)` section left empty for hcho. No synthesis written by Claude.
- [x] Each concept stub is listed in `wiki/index.md` under Concepts with `(stub)` noted.

**Validation Test:**

- **Setup:** US-001 complete.
- **Steps:**
  1. Run `ls "projects/Learning/AI Engineer/evals/wiki/concepts"` and count files.
  2. Open `concepts/llm-as-judge.md`.
  3. Open `wiki/index.md`.
- **Expected Result:** 10 concept files plus `.gitkeep`; each has the frontmatter fields and an
  empty `## In my own words (hcho)` section; index lists all 10 marked `(stub)`.
- **Failure Indicator:** Wrong count, missing frontmatter, a concept body containing Claude-authored
  synthesis, or concepts absent from the index.

### US-003: Build the `ingest` skill

**Description:** As hcho, I want an `ingest` skill that reads one raw source and updates the
relevant wiki pages in one pass, so adding knowledge is a single reliable command.

**Acceptance Criteria:**

- [x] Create `.claude/skills/ingest/SKILL.md` with frontmatter `name: ingest` and a `description`
      that triggers on "ingest this", "add this to the wiki", "process this paper/source".
- [x] Create `.claude/skills/ingest/assets/source-summary-template.md` (frontmatter +
      `## Key claims`, `## Connections` with `[[concept]]` links, `## Source` provenance).
- [x] The skill workflow documents these ordered steps: (1) resolve target wiki and read its
      `wiki/README.md` for mode; (2) if the source is a URL or pasted text, save it verbatim into
      `raw/<slug>.md` first and treat it as immutable; (3) read the source fully and discuss
      takeaways briefly; (4) write/refresh `sources/<slug>.md`; (5) update affected `concepts/`
      pages per mode (split: extend skeleton + cross-links, leave `## In my own words (hcho)`;
      full: write fully); (6) update `index.md` and bump `source-count`; (7) append to `wiki/log.md`
      with the dated prefix; (8) if today's daily `log/<DATE>.md` exists, add a thin pointer only;
      (9) confirm by listing every page touched.
- [x] The skill states guardrails: never edit anything under `raw/`; respect the wiki's mode; use
      the real date via `date +%Y-%m-%d`; kebab-case + frontmatter + `[[wikilinks]]`; never
      overwrite an existing source summary without showing it first.
- [x] The skill defaults the target wiki to the evals pilot and resolves others from the active-wiki
      list in `CLAUDE.md`.

**Validation Test:**

- **Setup:** US-001 and US-002 complete.
- **Steps:**
  1. Start a fresh assistant turn and say "ingest this source" with a short pasted paragraph.
  2. Observe the skill triggering and the steps it follows.
- **Expected Result:** The skill is discoverable, triggers on the phrase, saves the pasted text into
  `raw/` first, and then walks the documented steps. It does not modify `raw/` after saving and does
  not write the `## In my own words (hcho)` sections.
- **Failure Indicator:** Skill not discovered, does not save raw first, edits raw after saving, or
  writes synthesis into concept/synthesis pages.

### US-004: Add the wiki schema and de-dup rules to CLAUDE.md

**Description:** As hcho, I want the wiki conventions and boundaries encoded in the root schema so
the assistant maintains the wiki consistently and does not duplicate existing memory layers.

**Acceptance Criteria:**

- [x] Add a `## Wikis` section to `CLAUDE.md` describing the pattern in a few lines, the three
      operations (ingest = skill; query = file good answers back as pages; lint = health check), and
      the SPLIT-vs-FULL mode rule.
- [x] Include the de-duplication table: `memory/` owns who-hcho-is/how-to-work/project-status;
      `decisions/log.md` owns hard-to-reverse decisions (wiki events go to `wiki/log.md`); daily
      `log/` owns what-was-done-today (durable knowledge goes to the wiki; daily log only points);
      `learning-plan.md` owns the curriculum (the wiki is accumulated knowledge; cross-link).
- [x] Include an **Active wikis** list: evals pilot at `projects/Learning/AI Engineer/evals/wiki/`,
      mode split.
- [x] The addition mirrors the style of the existing `## Projects` and `## Skills` sections (concise,
      no new tooling claims).

**Validation Test:**

- **Setup:** US-001 complete.
- **Steps:**
  1. Open `CLAUDE.md` and locate the `## Wikis` section.
  2. Read the de-dup table and the active-wiki list.
- **Expected Result:** Section present, de-dup table covers all four existing layers, evals wiki
  listed with mode split.
- **Failure Indicator:** Section missing, any of the four layers absent from the table, or the wiki
  presented as overriding/duplicating memory or the decision log.

### US-005: Repo housekeeping (gitignore + decision log)

**Description:** As hcho, I want the Obsidian config kept out of git and the adoption decision
recorded, so the repo stays clean and the rationale is durable.

**Acceptance Criteria:**

- [x] Add `.obsidian/` to `.gitignore`.
- [x] Append one entry to `decisions/log.md` in the existing pipe format
      (`[YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...`) recording adoption of the
      LLM-wiki pattern, the Mandu-as-Obsidian-vault choice, and the split-mode rule for learning
      wikis. Append only; do not edit prior entries.

**Validation Test:**

- **Setup:** Repo on the feature branch.
- **Steps:**
  1. Run `grep -n "obsidian" .gitignore`.
  2. Run `grep -c "^\[" decisions/log.md` before and after to confirm exactly one new entry.
- **Expected Result:** `.obsidian/` present in `.gitignore`; exactly one appended decision entry in
  the correct format; no prior entries altered.
- **Failure Indicator:** `.obsidian/` not ignored, missing or malformed decision entry, or a prior
  entry changed.

### US-006: Prove the loop with one real end-to-end ingest (definition of done)

**Description:** As hcho, I want to ingest one real source through the full pipeline so I can see the
wiki compound, with my synthesis left for me to write.

**Acceptance Criteria:**

- [x] Save Hamel Husain's "Your AI Product Needs Evals" (learning-plan Section 1, S1) into
      `raw/your-ai-product-needs-evals.md` (verbatim text or a clipped markdown copy).
- [x] Run `ingest` against it. It produces `sources/your-ai-product-needs-evals.md` with a summary,
      key claims, and `[[concept]]` cross-links.
- [x] It updates the skeleton bodies of at least `concepts/offline-vs-online-evals.md` and
      `concepts/llm-as-judge.md` and bumps their `source-count` to 1, while leaving their
      `## In my own words (hcho)` sections empty.
- [x] It adds the source to `wiki/index.md` and appends
      `## [<today>] ingest | Your AI Product Needs Evals` to `wiki/log.md`.
- [x] `raw/your-ai-product-needs-evals.md` is byte-identical before and after the ingest.
- [x] `wiki/synthesis.md` is unchanged.

**Validation Test:**

- **Setup:** US-001 through US-004 complete; the Hamel source text available.
- **Steps:**
  1. Record a checksum of the raw file (`shasum raw/your-ai-product-needs-evals.md`).
  2. Run the ingest.
  3. Inspect `sources/`, the two concept pages, `index.md`, `log.md`, and `synthesis.md`.
  4. Re-checksum the raw file.
- **Expected Result:** Source summary created; both concept skeletons extended with `source-count: 1`
  and empty `## In my own words (hcho)`; index and log updated; raw checksum unchanged; synthesis
  unchanged.
- **Failure Indicator:** Raw file modified, any `## In my own words (hcho)` or `synthesis.md`
  written by Claude, or any of the derived pages not updated.

## Functional Requirements

- FR-1: The system must provide a `raw/` inbox per wiki holding immutable source documents that the
  assistant reads but never edits after initial save.
- FR-2: The system must provide a `wiki/` directory per wiki containing `README.md` (local schema),
  `index.md` (catalog), `log.md` (event log), `synthesis.md` (hcho-authored thesis), `sources/`,
  and `concepts/`.
- FR-3: Concept and source pages must use kebab-case filenames, `[[wikilinks]]` for cross-references,
  and YAML frontmatter including `type`, `tags`, `date`, and `source-count`.
- FR-4: The `ingest` skill must, in one pass, create/refresh a source summary, update affected
  concept pages, update the index, and append a dated entry to `log.md`.
- FR-5: On a wiki whose `README.md` declares `mode: split`, the assistant must not write the
  `## In my own words (hcho)` sections or `synthesis.md`; those are authored by hcho.
- FR-6: On a wiki whose `README.md` declares `mode: full`, the assistant may write all pages
  including synthesis.
- FR-7: The `ingest` skill must never modify any file under `raw/` after it has been saved.
- FR-8: The `ingest` skill must resolve the current date via `date +%Y-%m-%d`, not ambient context.
- FR-9: `log.md` entries must begin with the prefix `## [YYYY-MM-DD] <op> | <title>` so they are
  greppable.
- FR-10: `CLAUDE.md` must carry a `## Wikis` section with the pattern, the three operations, the
  SPLIT/FULL rule, the de-dup table, and an active-wiki list.
- FR-11: The 10 evals concept pages must be seeded as stubs mapped to learning-plan Sessions S1-S10,
  listed in the index, with `status: stub` frontmatter.
- FR-12: When a daily `log/<DATE>.md` exists, an ingest may add a thin pointer to it but must not
  duplicate the wiki's knowledge there.

## Non-Goals (Out of Scope)

- No `qmd` or any search engine. `index.md` plus Obsidian search is the search layer until a wiki
  passes roughly 100 sources.
- No `query` or `lint` skills in this release. Both are documented as `CLAUDE.md` workflows only and
  promoted to skills later if needed.
- No wikis #2-#6 (job-search, Agentic RAG, interview-prep, CreativeBridge, HabitLoop). This release
  builds only the pilot plus the replicable template.
- No Marp slide decks or Dataview dashboards. Frontmatter is added now so they work later; the
  views themselves are out of scope.
- Claude does not author synthesis, takeaways, or thesis on learning wikis.
- No automated batch ingestion. Sources are ingested one at a time with hcho involved.
- No changes to existing `README.md`, `learning-plan.md`, `log/`, `context/`, or `memory/` content
  beyond the additive schema and decision-log entries specified above.

## Design Considerations

- **Reuse the `daily-log` skill as the structural model** (`.claude/skills/daily-log/SKILL.md` and
  `assets/daily-log-template.md`): resolve target, never overwrite, scaffold from a template,
  carry/cross-reference, confirm. The `ingest` skill should feel like a sibling.
- **Concept stubs mirror the curriculum** so the graph view maps directly to Sessions S1-S10 in
  `learning-plan.md`. This makes orphan stubs meaningful (each is a topic awaiting its first source).
- **Obsidian is the read/edit surface.** The wiki is plain markdown in git, so Obsidian's graph view,
  backlinks, Web Clipper (capture into `raw/`), Dataview (frontmatter), and Marp all work without
  extra infrastructure.

## Technical Considerations

- **Folder path contains a space** (`projects/Learning/AI Engineer/evals/`). All scripts and skill
  steps must quote paths.
- **Manual step for hcho (not done by the implementation):** open `/Users/hcho/Mandu` as an Obsidian
  vault; optionally point Web Clipper's save + attachment paths at the target wiki's `raw/`.
- **De-dup discipline is the main risk.** Without the FR-10 boundaries, the wiki will duplicate
  `memory/`, `decisions/log.md`, and daily logs. The schema section is the control.
- **Immutability of `raw/`** is enforced by skill guardrails and verified by checksum in US-006.

## Success Metrics

- **Primary (definition of done):** one real source ingested end-to-end (summary + at least two
  concept updates + index + log), with `raw/` byte-identical and `synthesis.md` untouched (US-006).
- The `ingest` skill is discoverable and triggers on natural phrasing ("ingest this source").
- A single ingest touches multiple pages (summary + >=2 concepts + index + log) in one pass,
  demonstrating the compounding/bookkeeping payoff.
- Zero duplication: no domain knowledge written into `memory/`, `decisions/log.md`, or daily logs
  during the pilot.

## Open Questions

- Where should the glossary of wiki domain terms ultimately live: inline in the `CLAUDE.md`
  `## Wikis` section, or as a dedicated `context/wiki.md` (auto-loaded every session)?
- What concrete thresholds promote `query` and `lint` from workflows to skills (e.g., after N
  ingests, or once a second wiki exists)?
- When is the trigger to clone the template to wiki #2 (job-search company-intel): a fixed number of
  evals sources ingested, or a calendar point in the job search?
- Should `ingest` auto-add the thin daily-log pointer (FR-12) by default, or only when hcho asks?
