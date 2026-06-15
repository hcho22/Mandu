# PRD: Agentic RAG Wiki (Wiki #2 — Full-Mode Template Clone)

## Introduction

Clone the LLM-wiki pattern, already shipped as the evals pilot, into the **Agentic RAG** project as
the second wiki. An LLM Wiki is a persistent, compounding, interlinked collection of markdown files
that Claude builds and maintains from immutable raw sources, read and edited in Obsidian. Unlike RAG
(which re-derives knowledge from raw documents on every query), the wiki is compiled once per source
and then kept current, so cross-references, contradictions, and synthesis accumulate instead of
scattering.

The pilot (`projects/Learning/AI_Engineer/evals/wiki/`, see `.claude/agent/tasks/prd-llm-wiki.md`)
already built the reusable machinery: the `ingest` skill, the `## Wikis` schema and de-dup table in
`CLAUDE.md`, the page shapes, and the conventions. The original PRD explicitly named "Agentic RAG"
as a future wiki and scoped it out of that release. This PRD is that follow-on. Because the template
exists, this is a **thin clone**, not a rebuild: no new skill, no new schema. It stands up the new
wiki's files, seeds project-anchored concept stubs, registers the wiki so the existing `ingest`
skill can resolve it, records the decision, and proves the loop once end to end.

The two wikis differ in two deliberate ways, decided with hcho:

- **Mode is `full`, not `split`.** The evals wiki is a learning wiki, so hcho writes the synthesis.
  Agentic RAG is a built, production-shaped portfolio project where Claude's job is documentation,
  framing, and demo prep; in `full` mode Claude may draft every page including `synthesis.md`, with
  hcho reviewing. This is exactly the `mode: full` branch the pilot schema already defines.
- **Concepts are project-anchored, not curriculum-anchored.** The evals concepts mapped to learning
  Sessions S1-S10. The Agentic RAG concepts map one-to-one to the project's own components and
  deep-dive docs, so the graph view mirrors the system's architecture and the pages feed directly
  into interview talking points.

The wiki accumulates **both** internal knowledge (the project's own design and eval decisions,
sourced from its `docs/` deep-dives) and external research (RAG-eval papers, RAGAS docs, reranker
and judge literature). It directly serves the #1 goal: Agentic RAG is the flagship portfolio piece
for the AI Evals / Quality Engineer target, and a maintained wiki turns its eval apparatus into
durable, interview-ready, interlinked knowledge.

Two further decisions, resolved with hcho, shape this release:

- **Sources are captured verbatim into `raw/`.** Because the deep-dive docs live in the GitHub repo
  (not Mandu), each ingested source is copied verbatim into `raw/` at ingest time and then treated as
  immutable. The wiki stays self-contained and provenance is fixed; when an upstream doc changes, the
  new version is re-ingested as a fresh source rather than editing the saved copy.
- **Interview talking points consolidate to one surface.** Rather than each wiki keeping its own
  talking-points list, all interview talking points land in a single job-search prep surface at
  `projects/job-search/interview-prep.md`. Each wiki's `synthesis.md` points to that surface instead
  of duplicating it, which keeps the de-dup discipline intact.

## Goals

- Stand up a self-contained Agentic RAG wiki under `projects/Agentic_RAG/` with a `raw/` inbox and
  an LLM-maintained `wiki/` directory, structurally identical to the evals pilot.
- Run the wiki in `mode: full` so Claude maintains all pages including synthesis, with hcho
  reviewing rather than authoring.
- Seed 10 project-anchored concept-page stubs mapped one-to-one to the project's components and
  deep-dive docs, so the wiki graph mirrors the system architecture.
- Register the new wiki in the `CLAUDE.md` **Active wikis** list so the existing `ingest` skill
  resolves it by name, reusing the shipped machinery without modifying the skill or the schema.
- Establish a single job-search interview-prep surface (`projects/job-search/interview-prep.md`) that
  all wikis feed, so talking points consolidate in one place.
- Record the wiki-#2 adoption decision in `decisions/log.md` (append-only).
- Prove the loop end to end by ingesting one real source (`docs/evals.md`) with all derived pages
  updated and `raw/` byte-identical.

## User Stories

### US-001: Scaffold the Agentic RAG wiki skeleton (done 2026-06-15)

**Description:** As hcho, I want the `raw/` inbox and `wiki/` directory created under
`projects/Agentic_RAG/` so the project's sources have a home and Claude has a place to write
maintained pages, structurally identical to the evals pilot but in `full` mode.

**Acceptance Criteria:**

- [x] Create `projects/Agentic_RAG/raw/` with a `.gitkeep`.
- [x] Create `projects/Agentic_RAG/wiki/` containing `README.md`, `index.md`, `log.md`,
      `synthesis.md`, and the subdirectories `sources/` and `concepts/` (each with a `.gitkeep`).
- [x] `wiki/README.md` documents: `mode: full` in its YAML frontmatter and prose; the page types;
      the conventions (kebab-case, `[[wikilinks]]`, YAML frontmatter); a pointer to `synthesis.md`
      as the thesis; and a note that in full mode Claude drafts all pages (including synthesis) and
      hcho reviews. It mirrors the evals `wiki/README.md` structure.
- [x] `wiki/index.md` exists with category headers (Sources, Concepts, Synthesis) and no entries
      except the seeded concept stubs (see US-002).
- [x] `wiki/log.md` exists with a one-line header explaining the entry-prefix convention
      `## [YYYY-MM-DD] <op> | <title>`.
- [x] `wiki/synthesis.md` is a stub with the section headers `## Thesis (one paragraph)`,
      `## How the concepts connect`, and `## Open questions`, plus a one-line pointer stating that
      interview talking points live in the single job-search prep surface
      (`projects/job-search/interview-prep.md`), not here. No body text yet (drafted at first ingest,
      per full mode).
- [x] The existing `projects/Agentic_RAG/README.md` is untouched.

**Validation Test:**

- **Setup:** Repo on a feature branch; `projects/Agentic_RAG/` present with its `README.md`.
- **Steps:**
  1. Run `ls -R projects/Agentic_RAG`.
  2. Open `wiki/README.md` and `wiki/synthesis.md`.
- **Expected Result:** `raw/` and `wiki/` (with the five files + two subdirs) exist; README frontmatter
  and prose state `mode: full`; `synthesis.md` has the three headers plus the prep-surface pointer and
  no body text; `projects/Agentic_RAG/README.md` is unchanged.
- **Failure Indicator:** Any directory or file missing, README missing or contradicting `mode: full`,
  `synthesis.md` pre-filled before any ingest, or the project README modified.

### US-002: Seed the 10 project-anchored concept-page stubs (done 2026-06-15)

**Description:** As hcho, I want the 10 core Agentic RAG concepts pre-created as empty skeletons,
mapped one-to-one to the project's components and deep-dive docs, so the wiki mirrors the system's
architecture and gives ingestion a target to attach to.

**Acceptance Criteria:**

- [x] Create 10 files in `wiki/concepts/`, kebab-case, one per concept, each anchored to a project
      component/doc: `permissions-aware-retrieval`, `hybrid-retrieval-rrf`, `retrieval-eval-suite`,
      `ci-eval-gating`, `ragas-metrics`, `security-correctness-eval`, `text-to-sql-semantic-layer`,
      `agentic-tools-and-subagents`, `ingestion-pipeline`, `observability-langsmith`.
- [x] Each file has YAML frontmatter: `type: concept`, `tags`, `date`, `source-count: 0`,
      `status: stub`, and a `component:` field naming the project module/doc it maps to (the
      project-anchored equivalent of the evals wiki's `session:` field).
- [x] Each file body contains a one-line neutral definition placeholder, an empty `## From the
      sources` section (filled on ingest), and an empty `## Synthesis` section (Claude may draft this
      in full mode at ingest time). No synthesis is written at seed time.
- [x] Each concept stub is listed in `wiki/index.md` under Concepts with `(stub)` noted.

**Validation Test:**

- **Setup:** US-001 complete.
- **Steps:**
  1. Run `ls projects/Agentic_RAG/wiki/concepts` and count files.
  2. Open `concepts/retrieval-eval-suite.md` and `concepts/permissions-aware-retrieval.md`.
  3. Open `wiki/index.md`.
- **Expected Result:** 10 concept files plus `.gitkeep`; each has the frontmatter fields (including a
  `component:` mapping) and the `## From the sources` and empty `## Synthesis` sections; index lists
  all 10 marked `(stub)`.
- **Failure Indicator:** Wrong count, missing frontmatter or `component:` field, a concept body
  containing synthesis written at seed time, or concepts absent from the index.

### US-003: Register the wiki in CLAUDE.md Active wikis (done 2026-06-15)

**Description:** As hcho, I want the Agentic RAG wiki added to the Active wikis list so the existing
`ingest` skill can resolve it by name, reusing the shipped machinery with no skill or schema change.

**Acceptance Criteria:**

- [x] In the `## Wikis` section of `CLAUDE.md`, add a second entry to the **Active wikis** list:
      Agentic RAG at `projects/Agentic_RAG/wiki/`, mode full.
- [x] No change to the `ingest` skill, the `## Wikis` schema prose, the de-dup table, or the
      SPLIT/FULL rule. The skill already resolves named wikis from this list and already documents
      the `full` branch; only the list entry is added.
- [x] The addition mirrors the style of the existing evals-pilot entry (one concise line, no new
      tooling claims).

**Validation Test:**

- **Setup:** US-001 complete.
- **Steps:**
  1. Open `CLAUDE.md` and locate the Active wikis list in the `## Wikis` section.
  2. Confirm both wikis are listed with their modes.
  3. Diff `.claude/skills/ingest/SKILL.md` against `main`.
- **Expected Result:** Active wikis lists the evals pilot (split) and the Agentic RAG wiki (full);
  the `ingest` skill file is unchanged.
- **Failure Indicator:** Agentic RAG wiki absent from the list, listed with the wrong mode, the
  `ingest` skill edited, or the de-dup table / schema prose altered.

### US-004: Record the wiki-#2 adoption decision (done 2026-06-15)

**Description:** As hcho, I want the decision to clone the wiki pattern to Agentic RAG (in full mode)
recorded so the rationale is durable.

**Acceptance Criteria:**

- [x] Append exactly one entry to `decisions/log.md` in the existing pipe format
      (`[YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...`), recording: the clone of the
      LLM-wiki template to Agentic RAG as wiki #2; the choice of `mode: full` (built portfolio
      project, Claude maintains all pages, hcho reviews); the project-anchored concept backbone; the
      both-internal-and-external source diet; capturing sources verbatim into `raw/`; and
      consolidating interview talking points into the single `projects/job-search/interview-prep.md`
      surface. Append only; do not edit prior entries.
- [x] No `.gitignore` change is required: `.obsidian/` is already ignored (added during the pilot).
      If for any reason it is absent, add it; otherwise leave `.gitignore` untouched.

**Validation Test:**

- **Setup:** Repo on the feature branch.
- **Steps:**
  1. Run `grep -c "^\[" decisions/log.md` before and after to confirm exactly one new entry.
  2. Run `grep -n "obsidian" .gitignore`.
- **Expected Result:** Exactly one appended decision entry in the correct format, naming Agentic RAG,
  full mode, and the project-anchored backbone; no prior entry altered; `.obsidian/` present in
  `.gitignore` (unchanged).
- **Failure Indicator:** Zero or more than one new entry, malformed entry, a prior entry changed, or
  `.obsidian/` no longer ignored.

### US-005: Establish the single job-search interview-prep surface (done 2026-06-15)

**Description:** As hcho, I want one consolidation surface for interview talking points across all
wikis and projects, so talking points live in a single job-search prep file rather than scattered
per-wiki, and the Agentic RAG wiki feeds it.

**Acceptance Criteria:**

- [x] Create `projects/job-search/interview-prep.md` as the canonical home for interview talking
      points, with a short intro stating it consolidates talking points across projects and wikis,
      and a per-project section structure seeded with an `## Agentic RAG` section (empty, ready to
      receive points).
- [x] The Agentic RAG `wiki/synthesis.md` points to this surface for talking points (no per-wiki
      duplicate list), and `projects/job-search/README.md` references the surface.
- [x] Add a one-line note to the `## Wikis` section of `CLAUDE.md` stating that interview talking
      points consolidate to `projects/job-search/interview-prep.md` (so future ingests route them
      there), consistent with the de-dup discipline.

**Validation Test:**

- **Setup:** US-001 complete (so the wiki `synthesis.md` exists to point at the surface).
- **Steps:**
  1. Open `projects/job-search/interview-prep.md`.
  2. Open the Agentic RAG `wiki/synthesis.md` and confirm the pointer.
  3. Run `grep -n "interview-prep" CLAUDE.md projects/job-search/README.md`.
- **Expected Result:** The prep surface exists with an intro and an `## Agentic RAG` section;
  `synthesis.md` points to it; both `CLAUDE.md` and the job-search README reference it.
- **Failure Indicator:** Surface missing, talking points duplicated in `synthesis.md`, or no
  reference from `CLAUDE.md` / the job-search README.

### US-006: Prove the loop with one real end-to-end ingest (definition of done) (done 2026-06-15)

**Description:** As hcho, I want to ingest the project's own `docs/evals.md` through the full pipeline
so I can see the Agentic RAG wiki compound, with Claude drafting the synthesis (full mode) for me to
review and routing any interview talking points to the central prep surface.

**Acceptance Criteria:**

- [x] Save the Agentic RAG `docs/evals.md` content (fetched from the GitHub repo's raw URL or pasted)
      verbatim into `raw/agentic-rag-evals.md`. The deep-dive docs live in the GitHub repo, not in
      Mandu, so the source is captured into `raw/` at ingest time and treated as immutable thereafter.
- [x] Run `ingest` against it, naming the Agentic RAG wiki as the target. It produces
      `sources/agentic-rag-evals.md` with a summary, key claims, and `[[concept]]` cross-links.
- [x] It updates the bodies of at least `concepts/retrieval-eval-suite.md` and
      `concepts/ci-eval-gating.md` (and ideally `ragas-metrics` and `security-correctness-eval`),
      filling `## From the sources`, and bumps each touched concept's `source-count` to 1 and
      `status` from `stub`.
- [x] Because the wiki is `mode: full`, Claude may also draft the `## Synthesis` sections on the
      touched concepts and seed `wiki/synthesis.md` (thesis, connections, open questions). This is
      permitted and expected here (the key behavioral difference from the split-mode pilot). Any
      interview talking points are written to the `## Agentic RAG` section of
      `projects/job-search/interview-prep.md`, not into `synthesis.md`.
- [x] It adds the source to `wiki/index.md` (dropping the `(stub)` marker on now-sourced concepts)
      and appends `## [<today>] ingest | Agentic RAG Evals` to `wiki/log.md`.
- [x] `raw/agentic-rag-evals.md` is byte-identical before and after the rest of the ingest.

**Validation Test:**

- **Setup:** US-001 through US-005 complete; the `docs/evals.md` content available.
- **Steps:**
  1. After saving the raw file, record a checksum (`shasum raw/agentic-rag-evals.md`).
  2. Run the ingest against the Agentic RAG wiki.
  3. Inspect `sources/`, the touched concept pages, `index.md`, `log.md`, and `synthesis.md`.
  4. Re-checksum the raw file.
- **Expected Result:** Source summary created; at least the two named concept skeletons extended with
  `source-count: 1` and `## From the sources` filled; index and log updated; raw checksum unchanged;
  in full mode, `## Synthesis` and `synthesis.md` may be drafted by Claude.
- **Failure Indicator:** Raw file modified after capture, the source not summarized, fewer than two
  concept pages updated, `source-count` not bumped, or the index/log not updated.

## Functional Requirements

- FR-1: The system must provide a `raw/` inbox at `projects/Agentic_RAG/raw/` holding immutable
  source documents that Claude reads but never edits after the initial save.
- FR-2: The system must provide a `wiki/` directory at `projects/Agentic_RAG/wiki/` containing
  `README.md` (local schema, `mode: full`), `index.md`, `log.md`, `synthesis.md`, `sources/`, and
  `concepts/`, structurally identical to the evals pilot.
- FR-3: Concept and source pages must use kebab-case filenames, `[[wikilinks]]` for cross-references,
  and YAML frontmatter including `type`, `tags`, `date`, and `source-count` (concept pages also carry
  `status` and a `component:` mapping).
- FR-4: The 10 concept pages must be seeded as stubs anchored one-to-one to the project's components
  and deep-dive docs, listed in the index, with `status: stub` and `source-count: 0` frontmatter.
- FR-5: The wiki's `README.md` must declare `mode: full`; under full mode Claude may write all pages
  including the `## Synthesis` sections and `synthesis.md`. Interview talking points are routed to the
  central prep surface (FR-12), not duplicated in `synthesis.md`.
- FR-6: The wiki must be added to the **Active wikis** list in the `CLAUDE.md` `## Wikis` section so
  the existing `ingest` skill resolves it by name. No change is made to the `ingest` skill or the
  schema prose.
- FR-7: The `ingest` skill (unchanged) must, in one pass against this wiki, create/refresh a source
  summary, update affected concept pages, update the index, and append a dated entry to `log.md`.
- FR-8: The `ingest` skill must never modify any file under `raw/` after it has been saved; the first
  ingest's raw source must be byte-identical before and after.
- FR-9: `log.md` entries must begin with the prefix `## [YYYY-MM-DD] <op> | <title>`, with the date
  resolved via `date +%Y-%m-%d`.
- FR-10: Exactly one append-only entry must be added to `decisions/log.md` recording the wiki-#2
  adoption, the full-mode choice, and the project-anchored backbone.
- FR-11: The de-dup boundaries already in the `CLAUDE.md` `## Wikis` table continue to apply: domain
  knowledge goes to the wiki, not to `memory/`, `decisions/log.md`, or daily `log/` files.
- FR-12: Interview talking points must consolidate into a single job-search prep surface
  (`projects/job-search/interview-prep.md`); each wiki's `synthesis.md` points to it rather than
  maintaining a per-wiki duplicate list. Sources ingested into any wiki are first captured verbatim
  into that wiki's `raw/` inbox and treated as immutable.

## Non-Goals (Out of Scope)

- No rebuild of the `ingest` skill, the `## Wikis` schema prose, or the de-dup table. They shipped
  with the pilot and are reused as-is; only the Active-wikis list gains one line.
- No change to the `ingest` skill's default target (it still defaults to the evals pilot; Agentic RAG
  ingests are invoked by naming the wiki). Repointing the default is out of scope.
- No `query` or `lint` skills. Both remain documented `CLAUDE.md` workflows, as in the pilot.
- No wikis #3-#6 (job-search, interview-prep, CreativeBridge, etc.). This release builds only wiki #2.
- No modification of the Agentic RAG GitHub repo or its `docs/` files. The wiki captures a verbatim
  copy of a source into `raw/` and links/synthesizes from it; it does not edit the upstream docs.
- No changes to the evals pilot wiki, `context/`, `memory/`, or existing `projects/Agentic_RAG/README.md`
  content beyond the additive files and the single CLAUDE.md and decision-log entries specified above.
- No retrofit of the evals pilot (or any future wiki) onto the central prep surface, and no automated
  sync between wiki synthesis and the prep surface. This release only establishes the surface and
  wires the Agentic RAG wiki to it; migrating the evals pilot's talking points is a follow-on.
- No Marp slide decks or Dataview dashboards. Frontmatter is added now so they work later; the views
  themselves are out of scope.
- No automated batch ingestion. Sources are ingested one at a time with hcho involved.

## Design Considerations

- **Clone the evals pilot file-for-file.** `projects/Learning/AI_Engineer/evals/wiki/` is the
  structural template: same five files, same two subdirs, same conventions. The only intentional
  divergences are `mode: full` (vs split), the concept backbone (project-anchored vs S1-S10), and the
  full-mode concept-page body (`## From the sources` + a Claude-writable `## Synthesis`, replacing the
  split-mode hcho-only `## In my own words (hcho)` section).
- **Concept stubs mirror the architecture.** The 10 concepts map one-to-one to the project's
  components and deep-dive docs:
  - `permissions-aware-retrieval` -> `docs/permissions-aware-rag.md` (ACL-in-SQL-predicate; the
    post-filter recall collapse on selective ACLs).
  - `hybrid-retrieval-rrf` -> the retrieval stack (pgvector HNSW + Postgres full-text fused by
    Reciprocal Rank Fusion; optional reranker).
  - `retrieval-eval-suite` -> `docs/evals.md` (50-question golden set; recall@k, MRR, nDCG@5).
  - `ci-eval-gating` -> `docs/evals.md` (PR delta-vs-`main` comment, nightly snapshots, recall-floor
    regression alarms; the worked Δ -0.510 catch).
  - `ragas-metrics` -> the weekly RAGAS run (Faithfulness, Answer Relevancy, Context Precision,
    Context Recall).
  - `security-correctness-eval` -> proving the ACL property with an eval (no_access fraction = 1.000).
  - `text-to-sql-semantic-layer` -> `docs/structured-rag.md` (semantic-layer-aware text-to-SQL over an
    allowlisted read-only schema).
  - `agentic-tools-and-subagents` -> the chat loop's tools (`query_database`, `web_search`,
    `spawn_document_agent`).
  - `ingestion-pipeline` -> multi-format ingest (txt/md/pdf/docx/html via docling), chunk + embed +
    index, Realtime status, structured-output metadata extraction.
  - `observability-langsmith` -> LangSmith tracing.
  This makes orphan stubs meaningful: each is a component awaiting its first source.
- **Obsidian is the read/edit surface.** `/Users/hcho/Mandu` is already an Obsidian vault from the
  pilot, so graph view, backlinks, Web Clipper, and Dataview work over the new wiki with no extra
  setup. Optionally point Web Clipper's save path at `projects/Agentic_RAG/raw/` when ingesting
  external sources.
- **One prep surface, not per-wiki lists.** Interview talking points consolidate into
  `projects/job-search/interview-prep.md`, organized by source project (an `## Agentic RAG` section
  to start). Each wiki's `synthesis.md` keeps thesis/connections/open-questions and points to that
  surface, so talking points are not duplicated across wikis. This is a deliberate divergence from the
  evals pilot's `synthesis.md`, whose `## Interview talking points` section predates the consolidation
  decision; retrofitting it is a follow-on (see Non-Goals and Open Questions).

## Technical Considerations

- **Deep-dive docs live in the GitHub repo, not Mandu.** `projects/Agentic_RAG/` holds only
  `README.md` locally; `docs/evals.md`, `docs/permissions-aware-rag.md`, and `docs/structured-rag.md`
  are at https://github.com/hcho22/Agentic_RAG. The first ingest captures `docs/evals.md` into `raw/`
  from its GitHub raw URL or a pasted copy, then treats that copy as the immutable source of truth.
- **Re-ingest, don't edit, on upstream change.** Because `raw/` is immutable, when an upstream doc
  changes the wiki stays current by ingesting the new version as a fresh source, not by editing the
  saved copy.
- **The `ingest` skill resolves the wiki by name.** No skill change is needed; ingests against this
  wiki must name "the Agentic RAG wiki" (the skill still defaults to the evals pilot). The full-mode
  branch is already documented in the skill's Step 5.
- **Full mode widens what Claude writes, not the de-dup boundary.** Claude may draft synthesis here,
  but domain knowledge still belongs only in the wiki, not duplicated into `memory/`,
  `decisions/log.md`, or daily logs (FR-11).
- **`.obsidian/` is already gitignored** from the pilot, so no `.gitignore` change is expected.

## Success Metrics

- **Primary (definition of done):** `docs/evals.md` ingested end to end (source summary + at least two
  concept updates + index + log), with `raw/agentic-rag-evals.md` byte-identical after the ingest
  (US-005).
- The Agentic RAG wiki is resolvable by the existing `ingest` skill via the Active wikis list, with
  no skill or schema edits.
- A single ingest touches multiple pages (summary + >=2 concepts + index + log) in one pass,
  demonstrating the compounding payoff, and in full mode seeds `synthesis.md` (thesis/connections)
  while routing interview talking points to `projects/job-search/interview-prep.md`.
- Zero duplication: no domain knowledge written into `memory/`, `decisions/log.md`, or daily logs
  during this clone.

## Open Questions

- When and how should the evals pilot's existing `## Interview talking points` be migrated into the
  central `projects/job-search/interview-prep.md` surface, and should that surface eventually graduate
  into its own interview-prep wiki?
- What threshold triggers cloning wiki #3 (e.g., job-search company-intel): a fixed number of sources
  ingested across the first two wikis, or a calendar point in the job search?
- Should the `ingest` skill eventually take a default-wiki argument or infer the target from the
  working directory, so naming the wiki each time is unnecessary once there are several?
