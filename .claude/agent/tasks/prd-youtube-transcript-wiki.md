> SUPERSEDED (2026-07-08): This wiki was never physically built as a separate directory.
> Its scope was folded into AI_Wiki (`projects/Learning/AI_Engineer/AI_Wiki/`), which already realizes exactly this spec (full mode, organic concepts, AI-engineering domain, talk/tutorial/transcript diet).
> See the 2026-07-08 "Fold the planned YouTube-transcript wiki into AI_Wiki" entry in `decisions/log.md`. Retained for history only.

# PRD: YouTube-Transcript Wiki (Wiki #3 - Full-Mode, Organic-Growth Clone)

## Introduction

Clone the LLM-wiki pattern, already shipped as the evals pilot (wiki #1) and the Agentic RAG wiki (wiki #2), into a third wiki fed by **YouTube video transcripts**.
An LLM Wiki is a persistent, compounding, interlinked collection of markdown files that Claude builds and maintains from immutable raw sources, read and edited in Obsidian.
Unlike RAG (which re-derives knowledge from raw documents on every query), the wiki is compiled once per source and then kept current, so cross-references, contradictions, and synthesis accumulate instead of scattering.

This wiki's **domain is AI engineering** (LLMs, agents, RAG, evals, prompting, and adjacent production-AI topics); its **input diet is video transcripts** from talks, conference sessions, and tutorials.
"YouTube_transcript" names the medium, not the domain: the wiki is scoped to AI-engineering knowledge so it compounds coherently, and it cross-links to the evals and Agentic RAG wikis rather than overlapping them.

The pilot (`projects/Learning/AI_Engineer/evals/wiki/`, see `.claude/agent/tasks/prd-llm-wiki.md`) already built the reusable machinery: the `ingest` skill, the `## Wikis` schema and de-dup table in `CLAUDE.md`, the page shapes, and the conventions.
The Agentic RAG clone (`.claude/agent/tasks/prd-agentic-rag-wiki.md`) proved the pattern clones cleanly with no new skill and no schema change.
Because the template exists, this is a **thin clone**, not a rebuild: it stands up the new wiki's files, registers the wiki so the existing `ingest` skill can resolve it, records the decision, and proves the loop once end to end.

This release is deliberately even thinner than the Agentic RAG clone, per decisions resolved with hcho:

- **Mode is `full`.** Claude drafts every page including `synthesis.md`, with hcho reviewing. This is a knowledge-capture wiki (turn hours of video into durable, interlinked, interview-ready notes), not a synthesis-by-hcho learning wiki, so `full` mode fits. It reuses the `mode: full` branch the pilot schema already defines.
- **Concepts grow organically.** Unlike wikis #1 (curriculum-anchored S1-S10) and #2 (project-anchored to components), this wiki seeds **no** concept backbone. The `concepts/` directory ships empty, and each concept page is created by the first ingest that touches it. This fits an open-ended video diet with no fixed curriculum.
- **The standard source template is reused unchanged.** A transcript is treated as plain pasted text. No transcript-specific template, no timestamp-citation machinery, no video-metadata fields beyond what the existing template already captures under `## Source` provenance. This keeps the clone template-faithful and defers any video-specific tooling to a later release if it proves worth it.

The wiki directly serves the #1 goal: it converts the AI-engineering talks hcho watches into a compounding knowledge base that feeds interview prep and sharpens the AI-builder / evals positioning, at near-zero authoring overhead because Claude maintains it.

## Goals

- Stand up a self-contained YouTube-transcript wiki under `projects/Learning/AI_Engineer/Youtube_transcript/` with a `raw/` inbox and an LLM-maintained `wiki/` directory, structurally identical to the two prior wikis.
- Run the wiki in `mode: full` so Claude maintains all pages including synthesis, with hcho reviewing rather than authoring.
- Ship it with **no seeded concept backbone**: concepts are created organically at ingest time, so the wiki grows to match whatever the videos actually cover.
- Register the new wiki in the `CLAUDE.md` **Active wikis** list so the existing `ingest` skill resolves it by name, reusing the shipped machinery without modifying the skill, its source template, or the schema.
- Route interview talking points to the existing single prep surface (`projects/job-search/interview-prep.md`), consistent with the de-dup discipline established in wiki #2.
- Record the wiki-#3 adoption decision in `decisions/log.md` (append-only).
- Prove the loop end to end by ingesting one real AI-engineering video transcript, with the first concept pages **created** from scratch and `raw/` byte-identical.

## User Stories

### US-001: Scaffold the YouTube-transcript wiki skeleton (full mode, no seeded concepts)

**Description:** As hcho, I want the `raw/` inbox and `wiki/` directory created under `projects/Learning/AI_Engineer/Youtube_transcript/` so transcripts have a home and Claude has a place to write maintained pages, structurally identical to the prior wikis but in `full` mode and with an empty concept set.

**Acceptance Criteria:**

- [ ] Create `projects/Learning/AI_Engineer/Youtube_transcript/raw/` with a `.gitkeep`.
- [ ] Create `projects/Learning/AI_Engineer/Youtube_transcript/wiki/` containing `README.md`, `index.md`, `log.md`, `synthesis.md`, and the subdirectories `sources/` and `concepts/` (each with a `.gitkeep`).
- [ ] `wiki/README.md` documents: `mode: full` in its YAML frontmatter and prose; the AI-engineering domain with a video-transcript source diet; the page types; the conventions (kebab-case, `[[wikilinks]]`, YAML frontmatter); a pointer to `synthesis.md` as the thesis; a note that in full mode Claude drafts all pages (including synthesis) and hcho reviews; and an explicit note that **concepts grow organically** (no seeded backbone; each concept page is created by the ingest that first touches it). It otherwise mirrors the Agentic RAG `wiki/README.md` structure.
- [ ] `wiki/index.md` exists with category headers (Sources, Concepts, Synthesis) and **no entries** under any header (the wiki starts empty).
- [ ] `wiki/log.md` exists with a one-line header explaining the entry-prefix convention `## [YYYY-MM-DD] <op> | <title>`.
- [ ] `wiki/synthesis.md` is a stub with the section headers `## Thesis (one paragraph)`, `## How the concepts connect`, and `## Open questions`, plus a one-line pointer stating that interview talking points live in the single job-search prep surface (`projects/job-search/interview-prep.md`), not here. No body text yet (drafted at first ingest, per full mode).
- [ ] `concepts/` contains only a `.gitkeep` (no seeded concept files).

**Validation Test:**

- **Setup:** Repo on a feature branch; the empty `projects/Learning/AI_Engineer/Youtube_transcript/` folder present.
- **Steps:**
  1. Run `ls -R projects/Learning/AI_Engineer/Youtube_transcript`.
  2. Open `wiki/README.md` and `wiki/synthesis.md`.
  3. Run `ls projects/Learning/AI_Engineer/Youtube_transcript/wiki/concepts`.
- **Expected Result:** `raw/` and `wiki/` (with the five files + two subdirs) exist; README frontmatter and prose state `mode: full` and the organic-growth note; `synthesis.md` has the three headers plus the prep-surface pointer and no body text; `concepts/` holds only `.gitkeep`; `index.md` has category headers and no entries.
- **Failure Indicator:** Any directory or file missing, README missing/contradicting `mode: full` or the organic-growth note, `synthesis.md` pre-filled before any ingest, or a seeded concept file present in `concepts/`.

### US-002: Register the wiki in CLAUDE.md Active wikis

**Description:** As hcho, I want the YouTube-transcript wiki added to the Active wikis list so the existing `ingest` skill can resolve it by name, reusing the shipped machinery with no skill or schema change.

**Acceptance Criteria:**

- [ ] In the `## Wikis` section of `CLAUDE.md`, add a third entry to the **Active wikis** list: YouTube-transcript wiki at `projects/Learning/AI_Engineer/Youtube_transcript/wiki/`, mode full, with a short "(AI-engineering topics, video-transcript diet)" note.
- [ ] No change to the `ingest` skill, its source-summary template, the `## Wikis` schema prose, the de-dup table, or the SPLIT/FULL rule. The skill already resolves named wikis from this list and already documents the `full` branch; only the list entry is added.
- [ ] The addition mirrors the style of the existing evals-pilot and Agentic RAG entries (one concise line, no new tooling claims).

**Validation Test:**

- **Setup:** US-001 complete.
- **Steps:**
  1. Open `CLAUDE.md` and locate the Active wikis list in the `## Wikis` section.
  2. Confirm all three wikis are listed with their modes.
  3. Diff `.claude/skills/ingest/SKILL.md` and `.claude/skills/ingest/assets/source-summary-template.md` against `main`.
- **Expected Result:** Active wikis lists the evals pilot (split), the Agentic RAG wiki (full), and the YouTube-transcript wiki (full); the `ingest` skill and its template files are unchanged.
- **Failure Indicator:** The new wiki absent from the list, listed with the wrong mode, the `ingest` skill or its template edited, or the de-dup table / schema prose altered.

### US-003: Wire the wiki to the single interview-prep surface

**Description:** As hcho, I want the new wiki's talking points to route into the one existing prep surface, so points stay consolidated in one place rather than scattered per-wiki.

**Acceptance Criteria:**

- [ ] Add one new section to `projects/job-search/interview-prep.md` for this wiki's domain, headed `## AI Engineering (from talks & tutorials)` (empty, ready to receive points), placed consistently with the existing `## Agentic RAG` section.
- [ ] The new wiki's `wiki/synthesis.md` points to `projects/job-search/interview-prep.md` for talking points (no per-wiki duplicate list), matching how the Agentic RAG wiki's `synthesis.md` does it.
- [ ] No change to the existing `## Agentic RAG` section or to the intro of `interview-prep.md` beyond adding the one new section.

**Validation Test:**

- **Setup:** US-001 complete (so `synthesis.md` exists to point at the surface); `projects/job-search/interview-prep.md` exists from wiki #2.
- **Steps:**
  1. Open `projects/job-search/interview-prep.md` and confirm the new `## AI Engineering (from talks & tutorials)` section.
  2. Open the new wiki's `wiki/synthesis.md` and confirm the pointer.
  3. Run `grep -n "interview-prep" "projects/Learning/AI_Engineer/Youtube_transcript/wiki/synthesis.md"`.
- **Expected Result:** The prep surface has the new empty section; `synthesis.md` points to the surface; the existing `## Agentic RAG` section is untouched.
- **Failure Indicator:** Section missing, talking points duplicated in `synthesis.md`, the existing prep-surface content altered, or no pointer from `synthesis.md`.

### US-004: Record the wiki-#3 adoption decision

**Description:** As hcho, I want the decision to clone the wiki pattern to a video-transcript wiki (full mode, organic concepts) recorded so the rationale is durable.

**Acceptance Criteria:**

- [ ] Append exactly one entry to `decisions/log.md` in the existing pipe format (`[YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...`), recording: the clone of the LLM-wiki template as wiki #3 fed by YouTube transcripts; the AI-engineering domain scope with a video-transcript diet (medium is not the domain); the choice of `mode: full`; the organic-growth concept model (no seeded backbone); reuse of the standard source template unchanged; and routing talking points to the central prep surface. Append only; do not edit prior entries.
- [ ] No `.gitignore` change is required: `.obsidian/` is already ignored (added during the pilot). If for any reason it is absent, add it; otherwise leave `.gitignore` untouched.

**Validation Test:**

- **Setup:** Repo on the feature branch.
- **Steps:**
  1. Run `grep -c "^\[" decisions/log.md` before and after to confirm exactly one new entry.
  2. Run `grep -n "obsidian" .gitignore`.
- **Expected Result:** Exactly one appended decision entry in the correct format, naming the YouTube-transcript wiki, full mode, and the organic-growth model; no prior entry altered; `.obsidian/` present in `.gitignore` (unchanged).
- **Failure Indicator:** Zero or more than one new entry, malformed entry, a prior entry changed, or `.obsidian/` no longer ignored.

### US-005: Prove the loop with one real transcript ingest (definition of done)

**Description:** As hcho, I want to ingest one real AI-engineering video transcript through the full pipeline so I can see the wiki compound from empty, with concept pages created on the fly and Claude drafting the synthesis (full mode) for me to review.

**Acceptance Criteria:**

- [ ] Save one real AI-engineering video transcript (hcho pastes it, or saves it into `raw/` from YouTube's transcript panel or a clip) verbatim into `raw/<slug>.md`, and treat it as immutable thereafter.
- [ ] Run `ingest` against it, naming the YouTube-transcript wiki as the target. It produces `sources/<slug>.md` from the standard source template, with a summary, `## Key claims`, `## Connections` (`[[concept]]` links), and `## Source` provenance that captures the video's title, channel/author, and URL.
- [ ] Because no concepts are seeded, the ingest **creates** at least two new concept pages in `wiki/concepts/` for the topics the transcript covers, each in the full-mode shape (a one-line definition, `## From the sources` filled from this transcript, and a Claude-drafted `## Synthesis`), with `source-count: 1` and `status` not `stub`.
- [ ] Because the wiki is `mode: full`, Claude may also seed `wiki/synthesis.md` (thesis, connections, open questions). Any interview talking points are written to the `## AI Engineering (from talks & tutorials)` section of `projects/job-search/interview-prep.md`, not into `synthesis.md`.
- [ ] It adds the source under `## Sources` and the new concepts under `## Concepts` in `wiki/index.md`, and appends `## [<today>] ingest | <Video Title>` to `wiki/log.md`.
- [ ] `raw/<slug>.md` is byte-identical before and after the rest of the ingest.

**Validation Test:**

- **Setup:** US-001 through US-004 complete; one real AI-engineering video transcript available.
- **Steps:**
  1. After saving the raw file, record a checksum (`shasum "projects/Learning/AI_Engineer/Youtube_transcript/raw/<slug>.md"`).
  2. Run the ingest against the YouTube-transcript wiki.
  3. Inspect `sources/`, the newly created concept pages, `index.md`, `log.md`, and `synthesis.md`.
  4. Re-checksum the raw file.
- **Expected Result:** Source summary created from the standard template; at least two concept pages newly created with `source-count: 1`, `## From the sources` filled, and a drafted `## Synthesis`; index lists the source and the new concepts; log appended; raw checksum unchanged; in full mode, `synthesis.md` may be drafted by Claude.
- **Failure Indicator:** Raw file modified after capture, the source not summarized, fewer than two concept pages created, `source-count` not set to 1, the index/log not updated, or talking points written into `synthesis.md` instead of the prep surface.

## Functional Requirements

- FR-1: The system must provide a `raw/` inbox at `projects/Learning/AI_Engineer/Youtube_transcript/raw/` holding immutable source documents (saved transcripts) that Claude reads but never edits after the initial save.
- FR-2: The system must provide a `wiki/` directory at `projects/Learning/AI_Engineer/Youtube_transcript/wiki/` containing `README.md` (local schema, `mode: full`), `index.md`, `log.md`, `synthesis.md`, `sources/`, and `concepts/`, structurally identical to the prior wikis.
- FR-3: Concept and source pages must use kebab-case filenames, `[[wikilinks]]` for cross-references, and YAML frontmatter including `type`, `tags`, `date`, and `source-count` (concept pages also carry `status`).
- FR-4: The wiki must ship with **no seeded concept pages**; the `concepts/` directory starts empty (`.gitkeep` only), and concept pages are created by the ingest that first covers each topic.
- FR-5: The wiki's `README.md` must declare `mode: full`; under full mode Claude may write all pages including the `## Synthesis` sections and `synthesis.md`. Interview talking points are routed to the central prep surface (FR-10), not duplicated in `synthesis.md`.
- FR-6: The wiki must be added to the **Active wikis** list in the `CLAUDE.md` `## Wikis` section so the existing `ingest` skill resolves it by name. No change is made to the `ingest` skill, its source-summary template, or the schema prose.
- FR-7: The `ingest` skill (unchanged) must, in one pass against this wiki, save the transcript into `raw/`, create/refresh a source summary, create or extend the affected concept pages, update the index, and append a dated entry to `log.md`.
- FR-8: The `ingest` skill must never modify any file under `raw/` after it has been saved; the first ingest's raw source must be byte-identical before and after.
- FR-9: `log.md` entries must begin with the prefix `## [YYYY-MM-DD] <op> | <title>`, with the date resolved via `date +%Y-%m-%d`.
- FR-10: Interview talking points must consolidate into the single job-search prep surface (`projects/job-search/interview-prep.md`) under a section for this wiki's domain; the wiki's `synthesis.md` points to it rather than maintaining a per-wiki duplicate list.
- FR-11: Exactly one append-only entry must be added to `decisions/log.md` recording the wiki-#3 adoption, the full-mode choice, and the organic-growth concept model.
- FR-12: The de-dup boundaries already in the `CLAUDE.md` `## Wikis` table continue to apply: domain knowledge goes to the wiki, not to `memory/`, `decisions/log.md`, or daily `log/` files.

## Non-Goals (Out of Scope)

- No rebuild of the `ingest` skill, its source-summary template, the `## Wikis` schema prose, or the de-dup table. They shipped with the pilot and are reused as-is; only the Active-wikis list gains one line.
- No transcript-specific source template, no timestamp-citation fields, and no video-metadata schema beyond the standard template's `## Source` provenance. Transcripts are treated as plain pasted text this release.
- No seeded concept backbone. Concepts are created organically at ingest time; pre-creating a topic list is out of scope.
- No automated transcript fetching. Capturing a transcript is manual (paste, or save YouTube's transcript panel / a clip into `raw/`); a fetch tool or API is out of scope.
- No change to the `ingest` skill's default target (it still defaults to the evals pilot; this wiki's ingests are invoked by naming the wiki). Repointing the default is out of scope.
- No `query` or `lint` skills. Both remain documented `CLAUDE.md` workflows, as in the prior wikis.
- No new interview-prep surface. This release reuses the existing `projects/job-search/interview-prep.md` from wiki #2 and only adds one section to it.
- No changes to the evals pilot or Agentic RAG wikis, `context/`, `memory/`, or existing project READMEs beyond the additive files and the single `CLAUDE.md`, `interview-prep.md`, and `decisions/log.md` entries specified above.
- No Marp slide decks or Dataview dashboards. Frontmatter is added now so they work later; the views themselves are out of scope.
- No batch ingestion. Sources are ingested one at a time with hcho in the loop.

## Design Considerations

- **Clone the Agentic RAG wiki file-for-file.** `projects/Agentic_RAG/wiki/` is the closest structural template (same five files, same two subdirs, same `mode: full` conventions, same full-mode concept-page shape of `## From the sources` + a Claude-writable `## Synthesis`). The only intentional divergences are the domain (AI-engineering, video-fed), the empty concept set at scaffold time, and reusing the standard source template unchanged.
- **Organic growth is the distinguishing feature.** Wikis #1 and #2 seeded a concept backbone so the graph mirrored a curriculum or an architecture. This wiki has neither, so it starts empty and the graph accretes to match what the videos actually teach. Early on the index will be short; that is expected, and it is why the definition of done (US-005) emphasizes concept pages being **created**, not extended.
- **Domain over medium.** The wiki is named for its medium but scoped to AI engineering so it compounds. When a transcript covers a topic the evals or Agentic RAG wiki already owns, the concept page should `[[link]]` across to that wiki's page rather than duplicating it, keeping the three wikis complementary.
- **Obsidian is the read/edit surface.** `/Users/hcho/Mandu` is already an Obsidian vault from the pilot, so graph view, backlinks, Web Clipper, and Dataview work over the new wiki with no extra setup. Optionally point Web Clipper's save path at this wiki's `raw/` when capturing a transcript.
- **One prep surface, not per-wiki lists.** Talking points consolidate into `projects/job-search/interview-prep.md` under a new `## AI Engineering (from talks & tutorials)` section; `synthesis.md` keeps thesis/connections/open-questions and points there.

## Technical Considerations

- **The ingest must create concept pages, not just extend stubs.** This is the first wiki with no seeded concepts, so the first ingest against any topic **creates** its concept page. This is the existing full-mode Step 5 ("write the concept page fully") applied to a not-yet-existing file, so no skill change is required. If in practice the skill reads as assuming pre-existing stubs, a one-line "create the page if it does not exist" clarification to Step 5 is the minimal fix (flagged in Open Questions); it is not part of this release.
- **Transcript capture is manual.** hcho pastes the transcript or saves it into `raw/` (e.g., copy from YouTube's transcript panel). Because the standard template is reused, no timestamps or speaker turns are required; whatever text is captured is treated as the immutable source. Provenance (title, channel, URL) is recorded in the summary's `## Source` section.
- **Lives under the parked Learning track for topical grouping only.** The `projects/Learning/AI_Engineer/` location groups this with the evals track by subject; it does not reactivate the parked Learning workstream, and because it runs `mode: full` it is a Claude-maintained knowledge-capture wiki rather than an hcho-authored study wiki.
- **The path has no space.** `projects/Learning/AI_Engineer/Youtube_transcript/` needs no quoting for a space (unlike the older evals path); quoting stays harmless.
- **`.obsidian/` is already gitignored** from the pilot, so no `.gitignore` change is expected.
- **Full mode widens what Claude writes, not the de-dup boundary.** Claude may draft synthesis here, but domain knowledge still belongs only in the wiki, not duplicated into `memory/`, `decisions/log.md`, or daily logs (FR-12).

## Success Metrics

- **Primary (definition of done):** one real AI-engineering video transcript ingested end to end (source summary + at least two newly created concept pages + index + log), with the raw transcript byte-identical after the ingest (US-005).
- The YouTube-transcript wiki is resolvable by the existing `ingest` skill via the Active wikis list, with no skill, template, or schema edits.
- A single ingest touches multiple pages (summary + >=2 concepts + index + log) in one pass from an empty start, demonstrating the compounding payoff, and in full mode seeds `synthesis.md` while routing talking points to the central prep surface.
- Zero duplication: no domain knowledge written into `memory/`, `decisions/log.md`, or daily logs during this clone.

## Open Questions

- After a few ingests, is the standard source template genuinely sufficient for video, or does timestamp-aware citation ("at 12:34") earn a transcript-specific template and a one-line ingest tweak? Revisit once ~5 transcripts are in.
- Should Step 5 of the `ingest` skill get an explicit "create the concept page if it does not exist yet" line, now that an organic-growth (no-seed) wiki exists, so the behavior is documented rather than inferred?
- What threshold makes the growing, unseeded index unwieldy enough to want a lightweight topic grouping (or the deferred `lint`/`query` workflows promoted to skills)?
- When a transcript's topic overlaps the evals or Agentic RAG wiki, what is the rule of thumb for cross-linking versus creating a local concept page, so the three wikis stay complementary and non-duplicative?
