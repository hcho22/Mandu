---
name: ingest
description: Ingest one raw source (a paper, blog post, doc, or pasted text) into a wiki, updating every page it touches in a single pass. Use when hcho says "ingest this", "ingest this source", "add this to the wiki", "process this paper", "process this source", or pastes/links a source to file into a wiki. Defaults to the evals pilot wiki.
---

# Ingest

Turns one raw source into updated wiki pages in a single pass: saves the source verbatim into the wiki's `raw/` inbox, writes a source summary, extends the concept pages it touches with cross-links, updates the index, and logs the event. Built as a sibling of the `daily-log` skill: resolve the target, never overwrite blindly, scaffold from a template, cross-reference, confirm.

This is the `ingest` operation of the wiki pattern (see the `## Wikis` section of `CLAUDE.md`). It is the wiki write-path that adds knowledge.

## When to use this skill

Trigger when hcho wants to:
- File a source into a wiki ("ingest this", "ingest this source", "add this to the wiki")
- Process a paper, blog post, or doc into maintained pages ("process this paper/source")
- Paste text or give a URL and have it captured and summarized into the wiki

## Inputs needed

1. **Source** - a URL, a pasted block of text, or a path to a file already saved under the wiki's `raw/`. If none is given, ask for it.
2. **Target wiki** - defaults to the **evals pilot** at `projects/Learning/AI Engineer/evals/`. If hcho names another wiki, resolve it from the **Active wikis** list in the `## Wikis` section of `CLAUDE.md`.

## Workflow

### Step 1: Resolve the target wiki and read its mode
- Default target: the evals pilot wiki (`projects/Learning/AI Engineer/evals/`). Otherwise resolve from the Active wikis list in `CLAUDE.md`.
- Read the wiki's `wiki/README.md` and note its `mode:` (`split` or `full`). This governs Step 5.
- Quote all paths: the evals wiki path contains a space.

### Step 2: Save the source into `raw/` first (immutability)
- Derive a kebab-case `<slug>` from the source title.
- If the source is a URL or pasted text, save it verbatim into `raw/<slug>.md` before doing anything else, and treat it as immutable from that point on.
- If the source is already a file under `raw/`, use it as-is. Never re-save or edit it.

### Step 3: Read the source fully and discuss takeaways
- Read the saved `raw/<slug>.md` end to end.
- Give hcho a brief, neutral summary of the main takeaways (a few sentences). This is bookkeeping, not synthesis.

### Step 4: Write or refresh the source summary
- From `assets/source-summary-template.md`, create `wiki/sources/<slug>.md`.
- Fill the neutral summary, `## Key claims`, `## Connections` (with `[[concept]]` links to the concept pages this source informs), and `## Source` provenance (author, title, URL, link to the raw file, ingest date).
- If `wiki/sources/<slug>.md` already exists, show it to hcho first and confirm before overwriting.

### Step 5: Update the concept pages this source touches (mode-aware)
- For each concept the source informs, open `wiki/concepts/<concept>.md`.
- **split mode:** extend the neutral skeleton (sharpen the definition, add the key points this source contributes) and add a `[[source]]` cross-link to the summary. Do NOT write the `## In my own words (hcho)` section. Do NOT touch `synthesis.md`.
- **full mode:** write the concept page fully, including synthesis.

### Step 6: Update the index and bump counts
- Add the new source under `## Sources` in `wiki/index.md` as a `[[<slug>]]` link.
- For each concept updated, increment `source-count` in its frontmatter, and once it has at least one source drop the `(stub)` marker in the index and update `status:` from `stub`.

### Step 7: Append to the wiki log
- Get the real date via `date +%Y-%m-%d`.
- Append an entry to `wiki/log.md` beginning with `## [YYYY-MM-DD] ingest | <Source Title>`, listing the pages touched.

### Step 8: Thin pointer in today's daily log (only if it exists)
- If a daily `log/<DATE>.md` exists for the wiki's project today, add a one-line pointer to the ingest (for example: "Ingested <title> into the evals wiki: [[<slug>]]").
- Keep it a pointer only. Do not duplicate the wiki's knowledge into the daily log.

### Step 9: Confirm
- List every page created or modified (raw, source summary, each concept, index, log, and the daily-log pointer if added) so hcho can review what changed.

## Important guidance (guardrails)

- **Never edit anything under `raw/`** after the initial save. The raw inbox is immutable; it is the source of truth and must stay byte-identical.
- **Respect the wiki's mode.** On a `split` wiki, never write the `## In my own words (hcho)` sections or `synthesis.md` - those are hcho's. On a `full` wiki, you may write them.
- **Use the real system date** via `date +%Y-%m-%d`. Do not trust ambient context for dates.
- **Follow the conventions:** kebab-case filenames, YAML frontmatter (`type`, `tags`, `date`, plus `source-count` on concept pages), and `[[wikilinks]]` for every cross-reference.
- **Never overwrite an existing source summary without showing it first.** Read it, show it, and confirm before replacing.
- **One source at a time.** No batch ingestion; hcho stays in the loop.

## Reference files

- `assets/source-summary-template.md` - the canonical source-summary format (frontmatter + `## Key claims`, `## Connections`, `## Source`).

## Memory

This skill keeps a free-form `MEMORY.md` in its own folder.

- **Start of every run:** read `MEMORY.md` and apply anything relevant before doing the work.
- **Writing is feedback-gated:** append only when hcho explicitly says to remember something for this skill (a "remember this", a correction, or a stated preference). Do not log routine runs.
- **How to append:** add a dated bullet under `## Notes` in the form `- [YYYY-MM-DD] <note>`, using the real date from `date +%Y-%m-%d`.
- **Cap:** keep `MEMORY.md` under 100 lines. When it nears the cap, tell hcho and ask which entries to prune. Never delete entries silently.
