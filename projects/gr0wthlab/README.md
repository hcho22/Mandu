# gr0wthlab

**One-liner:** The "Marketing Engineer": a standalone agent that runs once a week on hcho's Mac and turns a product's go-to-market package (kept here in Mandu) into that week's drafts, evidence, and one Review Queue for hcho to decide.
It never publishes, sends, or spends, and it cannot write to Mandu or to any product repo; it proposes, and each owner applies what hcho approves.
Version 1 serves Rep Today's pre-launch marketing; Immerse joins as listen-only after Rep Today's first 14-day window has run cleanly.

**Repo:** https://github.com/hcho22/gr0wthlab (`main`, created 2026-10-08).
Visibility: private until about 18:50 UTC on 2026-10-12, then public; private on 2026-10-13 by hcho's call, "gr0wthlab records - private repo"; **public again since 2026-10-14 while v1 is built**, and to be made private before the first real run, which gr0wthlab is to refuse while the repo is public.
`main` has no branch protection.
**Development checkout (code and PRs):** `/Users/hcho/Developer/FM_Private/firstmate-private/projects/gr0wthlab` (verified 2026-10-15 at `b757595`, clean, in sync with GitHub); firstmate builds it, and it holds none of hcho's records.
**Production clone (hcho's records):** `~/gr0wthlab`, where the weekly run, the sitting page, and `ledger/` live; it does not exist yet (checked 2026-10-15).

**Strategic role: tracked as of 2026-10-12 at hcho's request, not ranked.**
It is tooling in service of Rep Today's launch (priority #1), not a product bet of its own, so it has no place in the Rep Today, Immerse, Purvia order unless hcho gives it one.
It is still a fourth build stream on the same solo capacity.
Logged in `decisions/log.md`.

---

## Status

_Last verified: 2026-10-15._

- **All 26 PRs so far merged in eight days (#1 to #26, 2026-10-08 to 2026-10-15), and #27 is open.**
  `main` is at `b757595` (#26, 2026-10-15), and the last eight runs on `main` all passed.
  Since 2026-10-12: the sitting page with hcho's records in `ledger/founder/` (#18), a refusal to run while the repo is public (#21), Instructions changed only through each workflow's example set (#23), the Weekly Read from numbers hcho types (#25, exchange version 8), and a Hook the code does not support sent to hcho as a package-change proposal (#26).
- **PRD progress: 64 of 99 acceptance boxes checked across 18 stories (44 on 2026-10-12).**
  Complete: US-ME01, 02, 04, 06, 07, 12, 15, 16.
  Partly done: US-ME08, 09, 11, 14, 17.
  Not started: the scheduling-service spike and loading (US-ME03, US-ME10, parked by hcho's manual-posting choice), the Waitlist itself (US-ME05), listening (US-ME13), and Immerse listening (US-ME18, parked).
- **Nothing has been published, sent, or scheduled, and no real weekly run has happened.**
  No production clone or schedule is installed, and `config/run.json` has no Waitlist date, first sitting, or posting slot.
  Runs so far were tests in throwaway copies.
- **The repo is public while v1 is built, and a real run refuses to start until it is private** ([PR #21](https://github.com/hcho22/gr0wthlab/pull/21)).
  Each production run commits `workspace/` and `ledger/` to `main`: unposted drafts, Review Queue items, hcho's decisions with their reasons, his typed results, counts, and run reports, so the repo must be private before the first one.
  firstmate holds `gr0wthlab-private-before-first-run` for that moment.
  A pattern scan of the full history for API keys and private keys found none on 2026-10-12; that is a pattern search, not a dedicated secret scanner.
- **CI was blocked by a GitHub billing limit while the repo was private on 2026-10-12; public repos use free runners, so it runs again.**
  Going private before the first run brings the metered minutes back, including one macOS job.
- **Size on `main` (static counts, 2026-10-15):** 106 Python files, about 30,400 lines outside tests, and 1,480 test functions in 53 test files.

## How it connects to Mandu

- **Mandu owns each product's go-to-market package.** For Rep Today that is `projects/RepToday/gtm/` plus `projects/RepToday/02-marketing-launch-checklist_260807.md`; gr0wthlab reads them and never copies or edits them.
- **hcho decides in gr0wthlab, and Mandu only reads (since 2026-10-14; exchange version 8 since 2026-10-15).**
  gr0wthlab's `docs/mandu-exchange.md` (version 8) and ADR 0002 are the contract.
  hcho decides every Review Queue item on the local page `~/gr0wthlab/src/bin/gr0wthlab sitting` serves, and the page writes his decisions, sittings, Beta Build record, Beta Cohort counts, and outreach records into gr0wthlab's `ledger/founder/`.
  In a read week (day 7 and day 14 of a window) he also types each post's numbers from TikTok Studio or YouTube Studio, its comments, and the day it went out on that page, which keeps them as results records in `ledger/founder/results/`; by his decisions of 2026-10-14 gr0wthlab uses no YouTube connection and takes no export file or screenshot (its ADRs 0005 and 0006), and the 200-impression floor counts each platform's views.
  The confirmation that starts Immerse Listening (US-ME18) is given on that page too, by hcho's answer of 2026-10-12; Mandu receives neither these numbers nor that confirmation.
  Mandu has no `exchange/` folder and never will under this design.
- **What Mandu does, through the `gr0wthlab-reader` skill:**
  it reads the Review Queue, items, run reports, Weekly Read memos, and hcho's records, his results records included, from `~/gr0wthlab/ledger/` to show him status, including which Weekly Read numbers are still to give, and writes nothing in gr0wthlab;
  it applies a package change to the package only when `queue.json` lists the item closed as approved and `founder/decisions/<id>.json` says approve, and records it in the Product's daily log;
  it gives hcho an approved Dispatch request, on the same two records, as a message to pass to firstmate, and records it in this project's log as given to hcho to pass to firstmate.
  It never records or corrects a decision, a result, or anything else hcho did for gr0wthlab, and a decision or a number told to Mandu in chat is not one.
  It acts on nothing in a record of an exchange version newer than 8.
- **Package changes hcho approved on 2026-10-10 are not applied here yet:** raise `hook_max_words` from 12 to 18 in `projects/RepToday/gtm/09-extras/marketing-agent/brand-rules.json`, and replace "no streaks" with "no resets" in the day 6 hook (eight places).
  He also answered that the trademark line stays open.
  The exact edits are in firstmate's `data/gr0wthlab/gr0wthlab-mandu-package-fixes/report.md`.
  He gave these answers to firstmate before the sitting page existed, so they are not gr0wthlab records and the reader does not apply them; applying them is a direct edit he can ask for.

## Gates before anything public

1. **The Rep Today Waitlist must be live.** It is the last open Gate 0 item, and `waitlist.live_since` is unset; every post item says nothing can be published until it is.
2. **hcho sets the first sitting and the posting slot** for the first 14-day window; both are unset.
3. **The trademark line in the package is still open** by hcho's answer on 2026-10-10, which blocks post drafts for all seven days of the first batch.
4. **A production clone and the Sunday 16:00 schedule** have to be installed (`docs/operations.md`).
5. **Posting is manual.** hcho chose manual posting on 2026-10-11, so no scheduling-service integration is being built.

## Decisions waiting on hcho (from firstmate's backlog, 2026-10-15)

- When to build the path for hcho to supply threads and reviews for listening; until then listening produces nothing (his "later for now", 2026-10-13).
- Whether to schedule three follow-ups nobody asked for: a lock so a boundary check and a weekly run cannot overlap, a hardening of the boundary probe, and not starting a session while the agent's changed Instructions could not be put back.
- Settled since 2026-10-12: the rule against keeping a stranger's words (middle choice, built in #19), the A/B pair video (decided 2026-10-13), and how an approved Weekly Read kill reaches the package ("angle kill - two approvals", 2026-10-15).

## Key files (in the repo)

- `README.md`: what it is, who does what, the eight guardrails, and the layout.
- `CONTEXT.md`: the glossary (Founder, Draft, Evidence, Review Queue, Weekly Read, Guardrail, and so on).
- `docs/prd/prd-marketing-engineer-v1_261008.md`: the v1 PRD, with acceptance boxes that record what has landed.
- `docs/prd/design-decisions-2026-10-08.md`: the decisions the PRD rests on.
- `docs/adr/0001-evidence-and-drafts-only.md`: why the repo holds evidence and drafts but no strategy.
- `docs/mandu-exchange.md`: what Mandu may read from gr0wthlab and the two approvals it acts on (version 8).
- `docs/adr/0002-the-founder-decides-in-gr0wthlab.md`: why hcho decides on gr0wthlab's sitting page and Mandu only reads.
- `docs/operations.md`: setting up and removing the production clone and schedule, and the weekly sitting.
- `config/run.json` and `config/products.json`: schedule, window, Waitlist date, and where each product's package lives.

## What a review should check

1. New commits, PRs, and CI on `hcho22/gr0wthlab`.
2. PRD acceptance boxes: which stories moved.
3. Whether a production clone and schedule exist, and whether any real weekly run has produced a Review Queue.
4. Whether anything has been sent or published, which only hcho can do: his outreach records show what he sent, but no gr0wthlab record shows that a post was published, so ask him.
   Whether the repo is public, and while it is, what production runs have committed to it, said plainly: a real run is to happen only once the repo is private.
5. `config/run.json`: the Waitlist date, the first sitting, and the posting slot.
6. firstmate's `data/backlog.md` for gr0wthlab holds waiting on hcho.
7. The Review Queue and hcho's records, read with the `gr0wthlab-reader` skill: open items by kind, carried-over items, whether the week's run is overdue, in a read week how many of the asked posts' numbers he has given, the approvals Mandu has applied or given to hcho to pass to firstmate since the previous review, and the approved package-change proposals and Dispatch requests still waiting for hcho's word.
8. Whether `docs/mandu-exchange.md` moved past version 8; a newer version may need a change to the reader.

Review entries live in `log/<YYYY-MM-DD>.md`.
