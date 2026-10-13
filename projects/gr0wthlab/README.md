# gr0wthlab

**One-liner:** The "Marketing Engineer": a standalone agent that runs once a week on hcho's Mac and turns a product's go-to-market package (kept here in Mandu) into that week's drafts, evidence, and one Review Queue for hcho to decide.
It never publishes, sends, or spends, and it cannot write to Mandu or to any product repo; it proposes, and each owner applies what hcho approves.
Version 1 serves Rep Today's pre-launch marketing; Immerse joins as listen-only after Rep Today's first 14-day window has run cleanly.

**Repo:** https://github.com/hcho22/gr0wthlab (**public** since 2026-10-12, `main`, created 2026-10-08; it was private until about 18:50 UTC that day).
`main` has no branch protection.
**Local checkout:** `/Users/hcho/Developer/FM_Private/firstmate-private/projects/gr0wthlab` (verified 2026-10-12 at `48b9c2d`, clean, in sync with GitHub).
firstmate builds it; no production clone exists yet at `~/gr0wthlab`.

**Strategic role: tracked as of 2026-10-12 at hcho's request, not ranked.**
It is tooling in service of Rep Today's launch (priority #1), not a product bet of its own, so it has no place in the Rep Today, Immerse, Purvia order unless hcho gives it one.
It is still a fourth build stream on the same solo capacity.
Logged in `decisions/log.md`.

---

## Status

_Last verified: 2026-10-12._

- **Nine PRs merged in five days (#1 to #8 and #11, 2026-10-08 to 2026-10-12); three are open (#9, #10, #12).**
  Merged: repository foundation, a Codex launcher that enforces the write boundary, the weekly run with package snapshot and Review Queue, the Waitlist request and an address-free Waitlist read, weekly post drafts, Beta Cohort recruiting, an agent time limit, listening and outreach drafts, and filming plans with finished 9:16 video cut from hcho's footage.
- **PRD progress: 44 of 99 acceptance boxes checked across 18 stories.**
  Complete: US-ME01, US-ME02, US-ME06.
  Mostly done: US-ME04, US-ME07, US-ME08, US-ME09, US-ME17.
  Not started: the scheduling-service spike and loading (US-ME03, US-ME10), the Waitlist itself (US-ME05), results collection and the Weekly Read memo (US-ME11, US-ME12), listening (US-ME13), learning from decisions (US-ME16), and Immerse listening (US-ME18).
- **Nothing has been published, sent, or scheduled, and no real weekly run has happened.**
  `workspace/` and `ledger/` on `main` hold only READMEs and instructions, no production clone or schedule is installed, and the config has no Waitlist date and no first sitting.
  Runs so far were tests in throwaway copies.
- **CI on `main` was blocked by billing while the repo was private, and is running again now that it is public.**
  The run on `48b9c2d` (2026-10-12) first failed all three jobs in two seconds with zero steps; GitHub's message was "The job was not started because recent account payments have failed or your spending limit needs to be increased."
  After the repo went public the same run was re-run: Lint and the Linux tests pass, and the macOS job was still running when last checked.
  Public repos use free runners, so this no longer blocks gr0wthlab; whether the account limit still applies to other private repos was not checked.
- **Being public changes what a real run exposes.**
  Each production run commits `workspace/` and `ledger/` to `main`: unposted post drafts, outreach message drafts, Review Queue items, hcho's decisions with their reasons, Waitlist and Beta Cohort counts, listening quotes with their links, and run reports.
  By design none of that contains an email address, and finished videos are never committed.
  No production run has happened, so nothing of that kind is public yet.
  A pattern scan of the full history for API keys and private keys found none; that is a pattern search, not a dedicated secret scanner.
- **Size on `main` (static counts):** 80 Python files, about 19,400 lines outside tests, 39 test files with 845 test functions.

## How it connects to Mandu

- **Mandu owns each product's go-to-market package.** For Rep Today that is `projects/RepToday/gtm/` plus `projects/RepToday/02-marketing-launch-checklist_260807.md`; gr0wthlab reads them and never copies or edits them.
- **The exchange is changing.** As specified today (`docs/mandu-exchange.md`, version 6), gr0wthlab writes its Review Queue in its own repo and Mandu writes hcho's decisions under `projects/gr0wthlab/exchange/`.
  That folder does not exist, and it has deliberately not been created.
  On 2026-10-12 hcho asked for his decisions and "what I did" records to move into gr0wthlab, decided on a small local page, with the package staying in Mandu and Mandu becoming a reader.
  That change (`gr0wthlab-decisions-in-gr0wthlab` in firstmate's backlog) is not built yet, so what Mandu must read is not defined yet.
- **Package changes hcho approved on 2026-10-10 are not applied here yet:** raise `hook_max_words` from 12 to 18 in `projects/RepToday/gtm/09-extras/marketing-agent/brand-rules.json`, and replace "no streaks" with "no resets" in the day 6 hook (eight places).
  He also answered that the trademark line stays open.
  The exact edits are in firstmate's `data/gr0wthlab/gr0wthlab-mandu-package-fixes/report.md`.

## Gates before anything public

1. **The Rep Today Waitlist must be live.** It is the last open Gate 0 item, and `waitlist.live_since` is unset; every post item says nothing can be published until it is.
2. **hcho sets the first sitting and the posting slot** for the first 14-day window; both are unset.
3. **The trademark line in the package is still open** by hcho's answer on 2026-10-10, which blocks post drafts for all seven days of the first batch.
4. **A production clone and the Sunday 16:00 schedule** have to be installed (`docs/operations.md`).
5. **Posting is manual.** hcho chose manual posting on 2026-10-11, so no scheduling-service integration is being built.

## Decisions waiting on hcho (from firstmate's backlog)

- Confirm how he wants to give decisions: firstmate read his "small local package as a conversation" as a small local page on which the sitting runs as a conversation, and has not confirmed that reading with him.
- Who builds Mandu's read-only side once the decisions change defines what Mandu reads.
- How far the rule against saving a stranger's words reaches into what the agent writes; this should be settled before listening reads real text.
- When to build the path for hcho to supply threads and reviews for listening; until then listening produces nothing.
- Whether the later video of an A/B pair is simply cut from the earlier one.
- Whether to schedule two follow-ups nobody asked for: a lock so a boundary check and a weekly run cannot overlap, and a hardening of the boundary probe.

## Key files (in the repo)

- `README.md`: what it is, who does what, the eight guardrails, and the layout.
- `CONTEXT.md`: the glossary (Founder, Draft, Evidence, Review Queue, Weekly Read, Guardrail, and so on).
- `docs/prd/prd-marketing-engineer-v1_261008.md`: the v1 PRD, with acceptance boxes that record what has landed.
- `docs/prd/design-decisions-2026-10-08.md`: the decisions the PRD rests on.
- `docs/adr/0001-evidence-and-drafts-only.md`: why the repo holds evidence and drafts but no strategy.
- `docs/mandu-exchange.md`: the exchange format between gr0wthlab and Mandu (version 6).
- `docs/operations.md`: setting up and removing the production clone and schedule.
- `config/run.json` and `config/products.json`: schedule, window, Waitlist date, and where each product's package lives.

## What a review should check

1. New commits, PRs, and CI on `hcho22/gr0wthlab`.
2. PRD acceptance boxes: which stories moved.
3. Whether a production clone and schedule exist, and whether any real weekly run has produced a Review Queue.
4. Whether anything has been published or sent, which only hcho can do, and what production runs have committed to the public repo.
5. `config/run.json`: the Waitlist date, the first sitting, and the posting slot.
6. firstmate's `data/backlog.md` for gr0wthlab holds waiting on hcho.
7. Whether the exchange with Mandu has been redefined, and what Mandu is then expected to read or write.

Review entries live in `log/<YYYY-MM-DD>.md`.
