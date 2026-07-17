# PRD: Mandu Agent - give the second brain a body (Phase 1 core loop)

## Introduction

Today **Mandu is inert.** It is a markdown + config repo (an Obsidian vault): a `CLAUDE.md` persona, `context/*.md` state, `decisions/log.md`, five skills, project trackers, and four LLM wikis.
It only "runs" when hcho opens Claude Code and types. Nothing happens on its own.

This feature forks [`raroque/boop-agent`](https://github.com/raroque/boop-agent) - a TypeScript agent runtime (Claude Agent SDK dispatcher + spawned sub-agents, Convex memory, Composio integrations, tiered memory, scheduled automations) - into a standalone **Mandu agent** that reaches into the Mandu vault and runs hcho's operating loop autonomously (wiki ingest/lint, daily brief, job scans, project status), reporting back over an existing channel.
It gives the existing second brain a body.

This PRD scopes only the **buildable core: fork + scaffold (Phase 0) and a headless, vault-only Mandu agent (Phase 1).**
Cross-project reach, gated product-repo writes, and the iMessage surface are explicit non-goals here and belong to later PRDs.

**Governing frame:** a personal operational multiplier + Claude Agent SDK learning + byproduct portfolio piece.
It is **not** a product/income bet - no pricing, no productization. It must not compete with the three income bets (Agentic RAG / Purvia, Rep Today, job search); it exists to raise throughput on them.

## Goals

- Stand up a running, standalone agent (own repo) built on the forked boop runtime, on the Claude Agent SDK path.
- Give the agent hcho's executive-assistant **identity** (persona + comm style + context), loaded rich into the top agent.
- Let the agent **operate the Mandu vault** - run the existing five skills headless and report back - reading/writing the vault safely via git branch/PR, never editing live files under hcho.
- Enforce the memory boundary: **Convex = scratch only; vault/wikis = durable truth** (no fifth redundant memory layer).
- Enforce wiki **split vs full mode** as a hard boundary (skeleton-only + hand-back for split wikis).
- Prove the loop end-to-end with three real autonomous jobs: **daily brief, wiki ingest, weekly lint.**

## User Stories

### US-001: Fork boop-agent and get the stock runtime green

**Description:** As hcho, I want a standalone forked repo running boop's stock behavior first, so I customize a known-good baseline instead of debugging a fork and my changes at once.

**Acceptance Criteria:**

- [ ] Fork `raroque/boop-agent` into a new repo `mandu-agent` at `/Users/hcho/Developer/mandu-agent`, upstream remote retained (for `/upgrade-boop`)
- [ ] `npm install` completes; `npm run setup` run choosing the **Claude Agent SDK** runtime (not Codex)
- [ ] Convex (free tier) provisioned and connected
- [ ] `npm run dev` starts the server + Convex + dashboard without errors
- [ ] Typecheck/lint passes

**Validation Test:**

- **Setup:** Fresh clone of the fork, Node installed, a Claude Code subscription authenticated locally
- **Steps:**
  1. Run `npm install`, then `npm run setup` and pick the Claude Agent SDK runtime
  2. Run `npm run dev`
  3. Send a stock test message through boop's default path
- **Expected Result:** Server boots, Convex connects, the stock agent round-trips a reply. No errors in the console.
- **Failure Indicator:** Setup wizard fails, Convex won't connect, or the stock message does not get a reply.

### US-002: Write CONTEXT.md glossary and seed the ADRs

**Description:** As a future reader (hcho or an AI agent), I want the domain language and the load-bearing decisions written down, so the brain/body split and memory boundary are not re-litigated later.

**Acceptance Criteria:**

- [ ] `CONTEXT.md` at the agent repo root defines: Vault/Mandu (brain), Mandu agent (body), Top agent, Sub-agent, Scratch memory, Durable knowledge
- [ ] `docs/adr/0001-two-repo-brain-body-split.md` records the two-repo decision and rejected alternatives (absorb/monorepo)
- [ ] `docs/adr/0002-rich-top-agent-slim-later.md` records the top-agent shape decision and its trigger to revisit
- [ ] `docs/adr/0003-convex-scratch-vault-truth.md` records the memory boundary
- [ ] Typecheck/lint passes (docs-only, trivially)

**Validation Test:**

- **Setup:** Agent repo scaffolded (US-001 done)
- **Steps:**
  1. Open `CONTEXT.md` and each ADR
  2. Check each ADR states context, decision, rejected alternatives, and consequences
- **Expected Result:** Glossary terms match this PRD; three ADRs exist and are non-empty with real trade-offs.
- **Failure Indicator:** Missing glossary terms, or an ADR that only restates the decision without alternatives/consequences.

### US-003: Load the rich Mandu identity into the top agent

**Description:** As hcho, I want the always-loaded top agent to sound and reason like my Mandu executive assistant, so it is my assistant with a body, not generic boop.

**Acceptance Criteria:**

- [ ] Top agent's system prompt loads a condensed `CLAUDE.md` persona + `context/me.md`, `context/work.md`, `context/current-priorities.md`, `.claude/rules/communication-style.md` from the vault
- [ ] Comm-style rules are enforced: no em dashes, no emojis, direct/no-fluff, structured
- [ ] The top agent can state hcho's #1 priority and the three income bets when asked
- [ ] Typecheck/lint passes

**Validation Test:**

- **Setup:** `VAULT_PATH` configured (US-004), agent running
- **Steps:**
  1. Ask the agent "who are you and what is my top priority?"
  2. Ask it to draft a two-line status note
- **Expected Result:** It identifies as hcho's executive assistant, names income-by-2026 via the three bets, and the drafted note contains no em dashes and no emojis.
- **Failure Indicator:** Generic boop persona, wrong/missing priorities, or output with em dashes/emojis.

### US-004: Configure vault-only reach via VAULT_PATH + allowlist

**Description:** As hcho, I want the agent scoped to only the Mandu vault in Phase 1, so its blast radius is contained and it cannot touch product repos yet.

**Acceptance Criteria:**

- [ ] `VAULT_PATH=/Users/hcho/Mandu` set as the working directory
- [ ] Directory allowlist contains the vault only; all other paths are out of scope by policy
- [ ] Attempting to read a path outside the allowlist is refused
- [ ] The canonical vault path is confirmed (capital-M `/Users/hcho/Mandu` git repo, not the lowercase mirror) and documented
- [ ] Typecheck/lint passes

**Validation Test:**

- **Setup:** Agent running with the allowlist configured
- **Steps:**
  1. Ask the agent to read `context/current-priorities.md` (in scope)
  2. Ask it to read a file under `/Users/hcho/Developer/Purvia` (out of scope)
- **Expected Result:** Step 1 succeeds; step 2 is refused with a clear "out of scope" message.
- **Failure Indicator:** Step 2 succeeds, or step 1 fails.

### US-005: Enforce the vault write-safety rule (branch/PR, never live files)

**Description:** As hcho, I want the agent to never edit live vault files under me, so it cannot clobber my work while I edit in Obsidian; all writes arrive as reviewable PRs.

**Acceptance Criteria:**

- [ ] Any vault write happens on a new git branch, never on `main` and never as an in-place edit of a tracked file hcho may have open
- [ ] The agent opens a PR (or a clearly-labeled branch) for hcho to review/merge
- [ ] Raw-source drops are written to the relevant `raw/` inbox, not into curated pages directly
- [ ] Typecheck/lint passes

**Validation Test:**

- **Setup:** Agent running, vault clean on `main`
- **Steps:**
  1. Ask the agent to record a one-line note in a wiki
  2. Inspect git state in the vault
- **Expected Result:** A new branch + PR exists with the change; `main` is untouched; no unstaged edits to files hcho did not ask about.
- **Failure Indicator:** A direct commit to `main`, or an in-place edit of a live file with no branch/PR.

### US-006: Constrain Convex to scratch memory only

**Description:** As hcho, I want boop's Convex memory used strictly for conversational/operational scratch, so my curated wiki/context stays the single source of durable truth (no fifth redundant memory layer).

**Acceptance Criteria:**

- [ ] boop's automatic memory extraction/consolidation is scoped to operational state (pending reminders, "hcho asked X at T"), not domain knowledge
- [ ] Durable knowledge is written to the vault (wiki/context) via US-005, not into Convex
- [ ] The de-dup boundary (from CLAUDE.md) is encoded as a rule in the top-agent prompt
- [ ] Typecheck/lint passes

**Validation Test:**

- **Setup:** Agent running; complete one ingest conversation and one reminder request
- **Steps:**
  1. After the ingest, inspect the Convex memory store
  2. Inspect the vault PR from the ingest
- **Expected Result:** Convex holds only operational scratch (e.g., "ingested source X at T"); the actual knowledge landed in the vault PR, not Convex.
- **Failure Indicator:** Domain/wiki knowledge duplicated into Convex, or knowledge only in Convex and never written to the vault.

### US-007: Adapt the five skills to load headless

**Description:** As hcho, I want my existing five skills to run in the agent runtime, so I reuse the playbooks I already have instead of rewriting them.

**Acceptance Criteria:**

- [ ] The agent discovers and can invoke the vault's `.claude/skills/{daily-loop,daily-log,ingest,job-hunter,prd}`
- [ ] Each skill's `MEMORY.md` is read at the start of its run, per skill convention
- [ ] Skills that assumed interactive back-and-forth are identified and flagged for headless adaptation (US-008/US-009 cover the first two)
- [ ] Typecheck/lint passes

**Validation Test:**

- **Setup:** Agent running, vault in scope
- **Steps:**
  1. Ask the agent to list the skills it can run
  2. Invoke `prd` (least interactive) on a trivial toy feature
- **Expected Result:** All five skills are listed; `prd` runs and produces a PRD file via the vault write-safety path.
- **Failure Indicator:** Skills not discovered, or a skill errors because it blocks on interactive input.

### US-008: Headless daily-loop morning brief delivered to a report channel

**Description:** As hcho, I want a morning brief generated and delivered without me sitting in a chat, so the agent runs my daily loop autonomously and reports back.

**Acceptance Criteria:**

- [ ] `daily-loop`'s morning brief runs headless (no interactive prompts) and produces a brief from `context/current-priorities.md` + project state
- [ ] The brief is delivered to a configured report channel (email or Slack - hcho picks at build time)
- [ ] The brief follows comm-style rules (no em dashes/emojis, structured, concise)
- [ ] Typecheck/lint passes

**Validation Test:**

- **Setup:** Report channel configured; `current-priorities.md` present
- **Steps:**
  1. Trigger the daily-brief job manually
  2. Check the report channel
- **Expected Result:** A structured brief arrives naming the current top priorities and next actions, in hcho's voice, with no em dashes/emojis.
- **Failure Indicator:** The job blocks waiting for input, nothing is delivered, or the brief violates comm-style rules.

### US-009: Headless wiki ingest that outputs a vault PR

**Description:** As hcho, I want to hand the agent a raw source and have it run the ingest skill unattended, so my wikis compound without me driving Claude Code.

**Acceptance Criteria:**

- [ ] Given a raw source (pasted text, URL, or file), the agent runs the `ingest` skill headless against the target wiki
- [ ] Output is a vault PR touching the correct source/concept pages, the index, and the wiki `log.md`, plus the raw file saved to that wiki's `raw/`
- [ ] The agent reports the result over the report channel (which pages it touched)
- [ ] Typecheck/lint passes

**Validation Test:**

- **Setup:** Report channel configured; AI_Wiki (full mode) in scope
- **Steps:**
  1. Give the agent a short real source and target AI_Wiki
  2. Inspect the resulting vault PR and the report message
- **Expected Result:** A PR updates the right pages + index + log and adds the raw file; the report lists the touched pages. `main` untouched.
- **Failure Indicator:** Direct edit to `main`, wrong pages, missing index/log update, or no report.

### US-010: Enforce wiki split vs full mode

**Description:** As hcho, I want the agent to respect each wiki's mode, so it never writes synthesis into a split-mode wiki that I reserve for myself.

**Acceptance Criteria:**

- [ ] The agent reads the `mode` from each `wiki/README.md` before writing
- [ ] For **full**-mode wikis it may write all pages including synthesis
- [ ] For **split**-mode wikis it writes bookkeeping + neutral skeleton only, then **stops and hands back** (draft-and-confirm), leaving `## In my own words (hcho)` empty
- [ ] Typecheck/lint passes

**Validation Test:**

- **Setup:** The split-mode evals wiki (`projects/Learning/AI_Engineer/evals/wiki/`) in scope
- **Steps:**
  1. Ask the agent to ingest a source into the evals (split) wiki
  2. Inspect the resulting PR
- **Expected Result:** The PR contains a neutral skeleton with the synthesis section left empty and a hand-back note to hcho; no synthesis prose was written.
- **Failure Indicator:** The agent writes synthesis / fills the "In my own words (hcho)" section for a split-mode wiki.

### US-011: Schedule the three core automations

**Description:** As hcho, I want the agent to act on a schedule, not only on demand, so it is genuinely alive - a daily brief and a weekly wiki lint arrive without me starting them.

**Acceptance Criteria:**

- [ ] A **daily** automation runs the morning brief (US-008)
- [ ] A **weekly** automation runs a wiki **lint** across the four wikis (orphans, broken `[[links]]`, stale frontmatter) and reports findings
- [ ] An **on-demand** ingest trigger exists (US-009)
- [ ] Automations run against the local always-awake Mac (no cloud, no iMessage)
- [ ] Typecheck/lint passes

**Validation Test:**

- **Setup:** Agent running locally with automations registered
- **Steps:**
  1. Temporarily set the daily brief and weekly lint to fire in ~1 minute
  2. Wait for both to fire
- **Expected Result:** Both jobs run unattended; the brief and a lint report arrive on the report channel; lint names real orphan/broken-link findings (or a clean bill).
- **Failure Indicator:** A job does not fire, blocks on input, or the lint report is empty/malformed when issues exist.

## Functional Requirements

- FR-1: The system must run as a standalone forked repo (`mandu-agent`) on the Claude Agent SDK runtime with Convex connected.
- FR-2: The top agent must load hcho's rich Mandu identity (persona + comm style + core context) from the vault on every run.
- FR-3: The agent must be scoped by an allowlist to the Mandu vault only in Phase 1; out-of-scope paths must be refused.
- FR-4: All vault writes must occur on a git branch and surface as a PR; the agent must never edit live tracked files in place or commit to `main`.
- FR-5: Convex memory must hold operational scratch only; durable knowledge must be written to the vault.
- FR-6: The agent must discover and run the vault's five skills, reading each skill's `MEMORY.md` at start.
- FR-7: `daily-loop` (brief) and `ingest` must run headless and deliver output to a configured report channel + vault PR.
- FR-8: The agent must read and enforce each wiki's `mode` (full = full write; split = skeleton-only + hand-back).
- FR-9: The system must schedule a daily brief and a weekly wiki lint, running locally, plus expose an on-demand ingest trigger.

## Non-Goals (Out of Scope for this PRD)

- **No iMessage / Sendblue / ngrok surface.** Reporting is via an existing channel (email/Slack/local dashboard). iMessage is a later PRD.
- **No cross-project reach.** The agent touches only the Mandu vault; `Purvia` and `RepToday` repos are out of scope (later PRD, read-only first).
- **No writes to product repos** of any kind.
- **No cloud hosting.** Local always-awake Mac only.
- **No Composio integrations** wired in Phase 1; add per concrete need later.
- **No slim-dispatcher refactor.** Rich top agent now; slim router deferred until token cost/dilution is a measured problem.
- **No productization** - no pricing, landing page, licensing, or open-core split. This is not a product bet.

## Technical Considerations

- **Two repos, linked by path, not git.** Vault stays standalone; agent reaches in via `VAULT_PATH` + allowlist (per ADR-0001). Not a monorepo.
- **Reuse boop's architecture:** `server/interaction-agent.ts` (top agent), `server/execution-agent.ts` (sub-agents), `server/memory/` (constrain to scratch), `server/automations.ts` (daily brief + weekly lint), `scripts/setup.ts`.
- **Reuse the existing skills** in the vault's `.claude/skills/` (already mirrored to `.agents/skills/`) rather than rewriting.
- **Sub-agents for heavy/isolated jobs** (ingest, lint, future repo tests); the top agent stays rich but delegates the heavy lifting.
- **Confirm canonical vault path** (`/Users/hcho/Mandu` vs lowercase mirror) before wiring `VAULT_PATH`.
- **Security:** boop's README states it is "not optimized for cost or security." Even vault-only, keep secret-ignore hygiene; product-repo secret rules come with the later cross-project PRD.

## Success Metrics

- The agent runs the daily brief and weekly lint unattended for one full week with zero manual starts.
- At least one real wiki ingest lands as a correct vault PR without hcho opening Claude Code.
- Zero direct commits to vault `main` by the agent; 100% of writes arrive as branches/PRs.
- Zero durable knowledge written into Convex (spot-checked).
- Split-mode wiki synthesis sections remain hcho-authored (agent never fills them).

## Open Questions

- Report channel for Phase 1: email, Slack, or the inherited boop debug dashboard?
- Which wiki does the ingest loop target first - AI_Wiki only, or all four full-mode wikis from the start?
- Vault PR granularity: one PR per job, or a rolling "agent" branch hcho merges periodically?
- Does the daily brief pull only from `current-priorities.md`, or also scan project `log/` and README status?
