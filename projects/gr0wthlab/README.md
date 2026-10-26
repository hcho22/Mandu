# gr0wthlab

**One-liner:** The "Marketing Engineer": a standalone agent that runs once a week on hcho's Mac and turns a product's go-to-market package (kept here in Mandu) into that week's drafts, evidence, and one Review Queue for hcho to decide.
It never publishes, sends, or spends, and it cannot write to Mandu or to any product repo; it proposes, and each owner applies what hcho approves.
Version 1 serves Rep Today's pre-launch marketing; Immerse joins as listen-only after Rep Today's first 14-day window has run cleanly.

**Repo:** https://github.com/hcho22/gr0wthlab (`main`, created 2026-10-08).
Visibility: private until about 18:50 UTC on 2026-10-12, then public; private on 2026-10-13 by hcho's call, "gr0wthlab records - private repo"; public again on 2026-10-14 while v1 was built; private from 2026-10-16, made so on his "gr0wthlab - go live" before the first real run, as he required (a real run refuses to start while the repo is public); public again as found on 2026-10-26, changed after the 2026-10-23 morning review by an action no record names, with the 2026-10-16 and 2026-10-19 records on `main`; **private again since about 10:41 PT on 2026-10-26, made so by hcho** (GitHub API `updated_at` 17:41:11 UTC).
`main` has no branch protection, which GitHub's free plan does not offer on a private repo.
**Development checkout (code and PRs):** `/Users/hcho/Developer/FM_Private/firstmate-private/projects/gr0wthlab` (verified 2026-10-26 at `6776dd0`, clean, in sync with GitHub); firstmate builds it, and it holds none of hcho's records.
**Production clone (hcho's records):** `~/gr0wthlab`, where the weekly run, the sitting page, and `ledger/` live; cloned 2026-10-16, and the weekly LaunchAgent (Sundays 16:00) installed 2026-10-21.
Its first scheduled start, 2026-10-25 16:00, refused to run because the repo was public, so the clone is still at `df34b86` (2026-10-19) until the next run syncs `main`.

**Strategic role: tracked as of 2026-10-12 at hcho's request, not ranked.**
It is tooling in service of Rep Today's launch (priority #1), not a product bet of its own, so it has no place in the Rep Today, Immerse, Purvia order unless hcho gives it one.
It is still a fourth build stream on the same solo capacity.
Logged in `decisions/log.md`.

---

## Status

_Last verified: 2026-10-26._

- **All 34 PRs so far merged (#1 to #34, 2026-10-08 to 2026-10-23); none open.**
  `main` is at `6776dd0` (#34, 2026-10-23), and all 14 CI runs since 2026-10-16 passed.
  Since 2026-10-15: an approved Weekly Read kill reaches the package as its own proposal (#29), cross-file contradictions in the package review (#30), frozen Hooks exempt from two Hook rules when `brand-rules.json` says so (#31), the live Waitlist view and window 1's dates (#32), the Waitlist line that ends every post caption (#33), and no skill installed on the Mac reaching a weekly session (#34).
- **PRD progress: 73 of 99 acceptance boxes checked across 18 stories (64 on 2026-10-15, 44 on 2026-10-12).**
  Complete: US-ME01, 02, 04, 05, 06, 07, 12, 15, 16.
  Partly done: US-ME08, 09, 11, 14, 17.
  Not started: the scheduling-service spike and loading (US-ME03, US-ME10, parked by hcho's manual-posting choice), listening (US-ME13), and Immerse listening (US-ME18, parked).
- **In operation since 2026-10-16, with nothing published yet.**
  Two on-demand runs (`20261016T181554Z-on-demand-307c`, `20261019T133323Z-on-demand-c2e0`) and one sitting (2026-10-18, 15 decisions).
  The first scheduled run, due Sunday 2026-10-25 at 16:00, fired on time and refused to start because the repo was public; a refused start earns no retry, so the week's run waits for hcho to start one on demand now that the repo is private again (10-26), and there was no sitting on 2026-10-25.
  `config/run.json` on `main` has `waitlist.live_since` 2026-10-21, window 1's first sitting 2026-10-25, and a 10:00 slot, so day 1 is Monday 2026-10-26; the production clone picks these up when a run syncs `main`.
  No post item has been queued yet, so nothing was ready for day 1; a run from 2026-10-26 on prepares days from the next day only, so day 1 can no longer be prepared under these dates.
  No footage exists, and no outreach record shows a message sent.
- **Each production run commits `workspace/` and `ledger/` to `main`, so the repo must be private**: unposted drafts, Review Queue items, hcho's decisions with their reasons, his typed results, counts, and run reports.
  It was public from about 10-23 until hcho made it private on 2026-10-26, and GitHub's traffic shows outside clones on 2026-10-23 and 10-24 that cannot be recalled.
  A pattern scan of the full history for API keys and private keys found none on 2026-10-12, and a scan on 2026-10-26 of the 2026-10-16 and 2026-10-19 records commits found none either; that is a pattern search, not a dedicated secret scanner.
- **CI minutes are metered only while the repo is private, including a macOS job of about 17 minutes per run.**
  A GitHub billing limit blocked CI while the repo was private on 2026-10-12; usage since 2026-10-16 was not checked.
- **Size on `main` (static counts, 2026-10-26):** 108 Python files, about 32,100 lines outside tests, and 1,546 test functions in 54 test files.
- **Immerse is still `listening-only` in the registry, with no package.**
  A Gr0wthPilot Candidate Package for Immerse sits untracked in `projects/Immerse/gtm/` since 2026-10-25; nothing reads it until hcho says "Immerse - hand to gr0wthlab" and firstmate adds it to the registry through a reviewed change.

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
  Both are still unapplied on 2026-10-26, and his 2026-10-21 choice to exempt the frozen Hooks from the Hook rules, over rewriting them, likely makes both moot; he has not said so.
- **Choices hcho gives firstmate outside the sitting page reach the package as direct edits, not through the reader.**
  Since 2026-10-21: window 1 text only with a 10:00 slot (Mandu `3bf4acc`), and the frozen-Hook exemption and the caption's Waitlist line (Mandu `4db78ff`, with gr0wthlab PRs #31 and #33).

## Gates before anything public

1. **The Rep Today Waitlist must be live.** Done: live on reptoday.app since 2026-10-21 (RepToday PRs #203 to #214), and `waitlist.live_since` is 2026-10-21 on `main` (#32).
2. **hcho sets the first sitting and the posting slot.** Done 2026-10-21: first sitting Sunday 2026-10-25, slot 10:00, so day 1 is Monday 2026-10-26 (#32).
3. **The trademark line in the package.** Closed: pre-publication checklist line 9 is checked since the approved `20261016-name-status-update` was applied (Mandu `0de57af`).
4. **A production clone and the Sunday 16:00 schedule.** Done: clone 2026-10-16, LaunchAgent 2026-10-21.
   But a run starts only while the repo is private: the first scheduled start, 2026-10-25, refused because it is public again.
5. **Posting is manual.** hcho chose manual posting on 2026-10-11, so no scheduling-service integration is being built.
6. **Footage.** Open: no window-1 footage exists in `/Users/hcho/Mandu/projects/RepToday/window-1/`; every window-1 shot is now a phone screen recording, and filming is hcho's.

## Decisions waiting on hcho (2026-10-26)

- First (the repo is private again since 10-26): start the week's run on demand (`~/gr0wthlab/src/bin/gr0wthlab run`) and hold the sitting; and whether window 1 keeps its dates, with day 1 skipped, or moves `first_sitting` through a reviewed change.
- On the sitting page: five open Review Queue items (two creator messages carried over from 2026-10-18, a new GMB Fitness message, the proposal to remove GMB Fitness from creator outreach, and the 2026-10-19 notice), and a choice for the approved but choice-less `20261016-p11-kill-read-conflict` and `20261016-prelaunch-paid-spend-conflict`.
- From firstmate's backlog: when to build the path for hcho to supply threads and reviews for listening; until then listening produces nothing (his "later for now", 2026-10-13).
- From firstmate's backlog: whether to schedule three follow-ups nobody asked for: a lock so a boundary check and a weekly run cannot overlap, a hardening of the boundary probe, and not starting a session while the agent's changed Instructions could not be put back.
- From firstmate's backlog (2026-10-24): when to schedule `gr0wthlab-replacement-package`, needed only before a second Handoff of a re-run package.
- Settled since 2026-10-15: going live (2026-10-16), the Waitlist build (approved 2026-10-19, live 2026-10-21), text-only filming and the 10:00 slot, the frozen-Hook exemption (2026-10-21), the caption's Waitlist line ("cta - B", 2026-10-22), the marketingskills companions and #34 ("1a, 2a, 3a", 2026-10-23), and creator disclosure told in person ("a", 2026-10-23).

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
