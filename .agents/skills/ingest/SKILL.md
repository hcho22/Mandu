---
name: ingest
description: Ingest one learning source (a tutorial summary, article, doc, paper, course notes, or pasted text) into the right wiki, updating every page it touches in a single pass. Use when hcho runs "/ingest", says "ingest this", "ingest this source", "add this to the wiki", "process this paper", "process this source", or pastes/links a source to file into a wiki. With no source named, it takes the sole pending Markdown file in the project's root `inbox/`.
---

# Ingest

Turns one learning source into updated wiki pages in a single pass.
It picks the destination wiki, keeps the source byte-identical in that wiki's `raw/` folder, writes a source summary, extends the pages the source touches, updates the index and log, and ends with a short review.

This is the `ingest` operation of the wiki pattern in the `## Wikis` section of the project instructions (in Mandu, `AGENTS.md`, which `CLAUDE.md` imports for Claude Code).
That section also holds the shared inbox rule, hcho's learning-capture preferences, and the **Active wikis** list.
Read it at the start of every run; where this skill and that section disagree, that section wins.

## When to use this skill

Trigger when hcho:
- Runs `/ingest`, with or without a file name, usually after dropping a file into `inbox/`.
- Asks to file a source into a wiki ("ingest this", "add this to the wiki", "process this paper/source").
- Pastes text or gives a URL to capture.

A file landing in `inbox/` does not start anything by itself; hcho's `/ingest` is the trigger.

## Workflow

### Step 1: Resolve the source

Use the first rule that applies:
1. **Explicit source.** A path hcho names (in `inbox/`, in an existing `raw/` folder, or elsewhere), a URL, or pasted text. Use it as given.
2. **One pending inbox file.** List `inbox/` at the project root, ignoring `README.md` (workflow guidance, never a source) and anything that is not `.md`. If exactly one file remains, use it.
3. **Several pending inbox files.** List them and ask hcho which one to process. Do not guess and do not batch.
4. **Nothing pending.** Say the inbox is empty and ask for a source.

Quote every path; some source filenames contain spaces.

### Step 2: Read the source and choose the destination wiki

- Read the source end to end before deciding anything. If it references images, read the text first, then view the images you need.
- If hcho named a wiki, use it.
- Otherwise pick the one wiki whose subject the source mainly serves, from the Active wikis list. General AI material (evals, models, RAG, agentic engineering, AI careers) goes to AI_Wiki. The old evals-pilot path `projects/Learning/AI_Engineer/evals/` is retired; never write there.
- Confirm the wiki's `wiki/` folder exists on disk. If the Active wikis list names a wiki that is missing, say so instead of creating it silently.
- A source has one home. When it also informs another wiki, that wiki gets cross-links on its relevant pages and a log entry that points to the home source summary. It does not get a second raw file or summary.
- Create a new subject wiki only when no existing wiki fits and the material warrants a lasting subject. Copy the layout of an existing full-mode wiki (`<Subject>/README.md`, `raw/`, and `wiki/` with `README.md` carrying `mode:`, `index.md`, `log.md`, `synthesis.md`, `sources/`, `concepts/`, `entities/`). Register it in the Active wikis list in `AGENTS.md`, in `projects/Education/README.md`, and in `Home.md`. If it is unclear whether the source needs a new subject or fits an existing one, ask.
- Read the destination's `wiki/README.md`, plus `wiki/CLAUDE.md` if it has one. Note its `mode:` (`split` or `full`), which governs Step 5, and its page conventions.

### Step 3: Preserve the source in `raw/`

- Derive a kebab-case `<slug>` from the source title. Drop any date prefix such as `092326_` from the inbox filename.
- If `raw/<slug>.md` already exists, compare bytes. Identical means the source was already ingested: tell hcho and stop. Different means pick a distinct slug.
- **Inbox file:** copy it byte-identical to `<wiki-root>/raw/<slug>.md`, confirm both SHA-256 hashes match (`shasum -a 256`), then remove the original from `inbox/`. If a byte-identical second copy is also in the inbox, move it to `archives/inbox-duplicates/<YYYY-MM-DD>/` rather than deleting it.
- **URL or pasted text:** save it verbatim to `raw/<slug>.md` before doing anything else.
- **Already in a `raw/` folder:** use it as-is. Never re-save, rename, or edit it.
- Images go in `raw/assets/`.
- From here on the raw file is immutable.

### Step 4: Write the source summary

- Create `wiki/sources/<slug>.md`, following the destination's own source-page conventions and its existing pages in `wiki/sources/`. Fall back to `assets/source-summary-template.md` only when the wiki has no convention of its own.
- Record provenance: title, author, URL, timestamps, a link to the raw file, and the ingest date. Keep whatever hcho supplied. When a detail is missing, write `unknown` and flag it; never invent one.
- If `wiki/sources/<slug>.md` already exists, show it to hcho and confirm before overwriting.

### Step 5: Update the pages the source touches (mode-aware)

- Extend existing concept, entity, and area pages before creating new ones. Create a page only when the source warrants it. Add `[[wikilinks]]` in both directions.
- Where the knowledge applies to a tracked project, link that project from the relevant page or from `synthesis.md`.
- Preserve what is already there, especially hcho's own writing. When the source contradicts an existing claim, record both claims with their dates and flag the contradiction. Add it to the wiki's tensions table if it has one. Never overwrite the older claim silently.
- **split mode:** extend the neutral skeleton and add the cross-link to the source summary. Do NOT write the `## In my own words (hcho)` sections or `synthesis.md`.
- **full mode:** write pages fully, and revise `synthesis.md` when the source changes the big picture. If it does not, say so in the review.

### Step 6: Update the index and counts

- Add the source summary and any new pages to `wiki/index.md`, and refresh the one-line summaries the source changed.
- Bump `source-count` and `last-updated` in the frontmatter of every page you extended, and move `status:` forward once a stub gains its first source.

### Step 7: Append to the wiki log

- Get the real date with `date +%Y-%m-%d`.
- Append one entry to `wiki/log.md` that starts with `## [YYYY-MM-DD] ingest | <Source Title>`.
- List where the source came from (for example, "cleared from the shared inbox"), the pages created and extended, contradictions flagged, evidence limits (no URL, undated, caption-derived, sponsor segments, interested-party claims), and the new page counts.
- A wiki that only received cross-links gets its own short log entry pointing to the home source.

### Step 8: Thin pointer in today's daily log (only if it exists)

- If a daily `log/<DATE>.md` exists for a related project today, add a one-line pointer such as "Ingested <title> into AI_Wiki: [[<slug>]]".
- Keep it a pointer only. The knowledge itself stays in the wiki.

### Step 9: Short review

File first, then report. Routine ingestion needs no discussion before filing.
Give hcho a short review with:
- Where the source went and why, and the inbox file it cleared.
- The main takeaways in a few sentences, plus any project connections.
- Every page created or modified, as `[[links]]` he can open in Obsidian.
- Contradictions, provenance gaps, and evidence limits.
- Questions only about material ambiguities that block accurate filing.

## Important guidance (guardrails)

- **Never edit anything under `raw/`** after the first save. It must stay byte-identical.
- **`inbox/README.md` is never a source.**
- **Respect the wiki's mode.** On a `split` wiki, the `## In my own words (hcho)` sections and `synthesis.md` are hcho's. On a `full` wiki, you may write them.
- **Use the real system date** from `date +%Y-%m-%d`. Do not trust ambient context for dates.
- **Follow the wiki's conventions:** kebab-case filenames, YAML frontmatter, `[[wikilinks]]`, full vault-relative links between wikis, one sentence per line, and no em dashes.
- **Never overwrite an existing source summary without showing it first.**
- **One source per run.** Process several only when hcho explicitly asks for a batch, and record that direction in the wiki log.
- **Ingestion records knowledge, not beliefs.** A persuasive source does not establish hcho's views or approve anything for publication. Keep source claims, compiler additions, and synthesis apart.

## Reference files

- `assets/source-summary-template.md` - fallback source-summary format for a wiki without its own source-page convention.

## Memory

This skill keeps a free-form `MEMORY.md` in its own folder.

- **Start of every run:** read `MEMORY.md` and apply anything relevant before doing the work.
- **Writing is feedback-gated:** append only when hcho explicitly says to remember something for this skill (a "remember this", a correction, or a stated preference). Do not log routine runs.
- **How to append:** add a dated bullet under `## Notes` in the form `- [YYYY-MM-DD] <note>`, using the real date from `date +%Y-%m-%d`.
- **Cap:** keep `MEMORY.md` under 100 lines. When it nears the cap, tell hcho and ask which entries to prune. Never delete entries silently.
