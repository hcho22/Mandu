---
type: concept
tags: [agentic-engineering, skills, plugins, mcp, codex, packaging]
status: seed
source-count: 1
last-updated: 2026-08-05
---

# Skills vs Plugins

The packaging distinction in [[codex]], from [[running-life-on-codex]]:

- A **skill** is one reusable capability or instruction set - a single component.
- A **plugin** is a shareable bundle: multiple skills, potentially multiple **MCP servers**, plus other scripts and resources.

Example from the source: individual write-me / Slack / email skills ([[personal-voice-skill]]) bundled into one **"Better Writing"** plugin to share with a team.

## Key points

- **The bundle is the unit of distribution.** A skill is what you build and iterate on personally; a plugin is how you package several of them (plus their MCP connections and scripts) to hand to other people.
- **Codex plugin directory, public submission open.** Skill-only submissions are reviewed quickly; submissions that include **MCP servers** go through a more thorough security audit - the review bar scales with what the bundle can reach, since an MCP server is executable access to outside systems.

## The same idea, different vocabularies

Every agent stack has a "one capability" unit and a "packaged bundle" unit; only the names differ:

| Stack | One capability | Packaged bundle |
|---|---|---|
| Codex (this source) | skill | **plugin** (skills + MCP servers + scripts) |
| Claude Code | skill | plugin / marketplace bundle |
| Generic | tool / instruction file | MCP server + skill set |

## The atom also has a budget role ([[agents-md-is-a-neural-net]], 2026-08-27)

[[kun]] adds a use for the skill-as-atom this page did not have: it is the unit you **extract to** when trimming an always-loaded memory file to its budget ([[skills-as-release-valve]]).
Narrow-but-triggerable instructions move out of `AGENTS.md` and into a skill, which is why the atom/molecule distinction matters operationally and not just for distribution - the atom is the release valve, the molecule (plugin) is how you share a set of them.

## Synthesis

A small but clarifying distinction: the wiki's [[building-skills]] and [[self-updating-config]] pages treat the *skill* as the atom, and this source names the molecule above it and, usefully, ties the review/trust bar to it - MCP-bearing bundles are audited harder because they carry executable reach, which is the [[credential-vaults]] / [[capabilities-not-instructions]] security instinct applied to distribution.

For hcho the practical read is about **sharing**, not building: his own skills (the Mandu `ingest`, `daily-log`, `prd`, `job-hunter` skills) are personal atoms today; the day any of them is worth handing to someone else, the plugin is the bundle - and the moment it includes an MCP server, it inherits a real security-review obligation. Worth remembering if a Purvia or Rep Today skill ever ships publicly.
