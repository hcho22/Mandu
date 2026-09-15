---
type: entity
tags: [tool, markdown, notes, memory, second-brain]
status: seed
source-count: 1
last-updated: 2026-08-05
---

# Obsidian

A local-first markdown notes app (folders of plain `.md` files with wikilink-style cross-references, backlinks, and a graph view).
In the wiki it appears less as a notes UI and more as **a structured markdown store an agent reads for context**.

## What shows up in the wiki

- [[running-life-on-codex]] - [[jason-openai-codex]] keeps almost all his context in an Obsidian vault ("Vault"), his "basically only project": plain markdown, no database, organized into projects / people / notes / daily notes / preferences, with other repos originating from it as the source of truth. He **rarely opens Obsidian himself** - it exists to give his agent context ([[monorepo-for-agent-context]], [[context-is-king]], [[ai-operating-system]]).

## Notes

Obsidian is also hcho's own tool of record: AI_Wiki and the project-specific Mandu wikis are read in Obsidian while Claude maintains the pages.
So Jason's setup is a near-exact mirror of hcho's - a markdown vault as the agent's single source of truth, browsed by a human in Obsidian, written by an agent - which makes [[running-life-on-codex]] an unusually direct outside validation of the [[ai-operating-system]] pattern hcho already runs.
The durable point is that the value is the **plain-markdown-as-agent-memory** discipline, not the app; Obsidian just makes the same files pleasant for a human to browse (rendered images, backlinks, graph view).
