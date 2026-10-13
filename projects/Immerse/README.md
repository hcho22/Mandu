# Immerse

**One-liner:** A nostalgic, intentional film-camera iOS app (working title "Film Camera Experience").
Instead of picking a vintage filter after unlimited capture, you choose a Camera, load a bounded Film, shoot within its capacity, and the result is revealed by that format's own rules.

**Name:** "Immerse" is the repo name.
The final product name is not selected (PRD open decision DEC-01), and the PRD uses the descriptive title "Film Camera Experience".

**Repo:** https://github.com/hcho22/Immerse (`main`). **GitHub reports it as PUBLIC** (re-verified 2026-10-12), although earlier Mandu records called it private.
Its event history shows no visibility change, which is consistent with it having been public since creation on 2026-09-29; whether it should stay public is hcho's call.
**Local checkout:** `/Users/hcho/Developer/fm_private/firstmate-private/projects/Immerse` (branch `main`, verified 2026-10-12 at `0e69ed2`, clean tree, in sync with GitHub). This is firstmate's live home; `FM_Private` and `fm_private` resolve to the same folder.

**Strategic role: ranked #2, immediately after Rep Today (hcho's call, 2026-09-29).**
Added to daily tracking on 2026-09-29 at hcho's request.
Order is Rep Today, Immerse, Purvia, then the job search as the parallel hedge.
The ranking set where attention went next; full v1 native implementation started on 2026-10-02 (PR #7).
Logged in `decisions/log.md`.

---

## Status

_Last verified: 2026-10-12._

- **PRD 2.0 and 2.1 landed, and three of four implementation slices are merged (PRs #14-#24, 2026-10-05 to 2026-10-09).**
  `main` is at `0e69ed2`.
  The lineup is still five Cameras; the 6x6 and 16mm dropped their decade and gained a color or black-and-white Film Stock, the 16mm runs 2:47, looks are "fresh, not aged" and judged against one internal Format Reference per Camera, and Darkroom contrast grades apply to every Photo Film.
  Merged slices: capture behavior (#19), names and the Instant card (#22), and Film Stock (#24).
- **The fourth slice, per-Camera looks, is unmerged and waits on hcho.**
  It lives on a local branch only (`fm/immerse-prd2-looks`, 18 commits, not pushed).
  hcho approved the Instant, Disposable, and Super 8 looks on 2026-10-10; the 6x6 and 16mm boards are at round 7 awaiting his verdict.
- **Still nothing validated on a physical iPhone.**
  On 2026-10-06 hcho chose the manual-test candidate to be the build that includes PRD 2.0 after all slices, so device validation waits on the looks slice.
  PR #7's "High" risk note and its capture, export, and Trial fixes remain software-only.
- **CI: 9 of 11 `main` runs green since #14, the last four green.**
  The two failures were different flaky UI tests on commits with no app-code change, and a run now takes up to 108 minutes against a 120-minute cap.
  `main` has no branch protection.
- **Size on `main` (static counts):** 159 Swift files; app sources 15 files and 2,787 lines; package sources 41 files and 5,928 lines; test methods 44 app unit, 77 app UI, 194 package, 84 probe.
  The media catalog is still empty and no live StoreKit product or price exists.
- **Task tracker:** 252 items (PRD 2.0 added 14); the same 9 are checked (5 discovery, 4 decisions), 135 v1 and 108 v2 items are open, and no implementation task is checked.
  The PRD and tracker headers still describe a planning baseline.
- **Earlier baseline (2026-09-29 to 2026-10-01):** Design A, "Film Journal", selected; Group Films deferred to v2 (PR #3); personal-only on-phone system approved (PR #4); architecture revision 3 approved (PR #5); users, journeys, and the clickable design reference approved (PR #6).

## V1 scope (from PRD 2.1, 2026-10-07)

| Area | Included in v1 | Excluded or deferred |
| --- | --- | --- |
| Platform | Native iOS, new in-app captures, rear and front lenses | Android, web capture, App Clips, existing-media import |
| Photo Cameras | 1990s Disposable (27 exposures), 1970s Instant (10), 6x6 Medium Format (12, color or black-and-white Film Stock) | CCD digicams, MiniDV, Half Frame, VHS, Hi8 |
| Movie Cameras | 1960s Super 8 (3:20), 16mm Cinema (2:47, color or black-and-white Film Stock) | Movie timeline editing, a Movie Darkroom |
| Films | Personal Photo and Movie Films | Photo Group Films, Group Movies, Instant Groups, same-device Give Camera mode |
| Editing and sharing | Reversible per-photo analog Darkroom (contrast grades on every Photo Film, toning on black-and-white only, no Instant crop); optional Photos export | AI retouching, Movie editing, Group sharing and Private Prints |
| Business model | One all-inclusive monthly or yearly subscription, plus one Photo OR Movie Trial Film | Per-Film fees, exposure wallet, tiers |
| Privacy and management | Archive, personal whole-Film deletion, account deletion | Group contribution withdrawal, participant removal, Guest deletion, co-hosts, Host transfer |

Product principles to remember: camera authenticity wins over convenience, a Film is bounded and immutable once loaded, sealed captures cannot be reviewed, and expiration of a subscription never locks existing Films.

## Open questions

- **No price, final brand, or formally approved native stack** (DEC-01 to DEC-03). The code uses SwiftUI and raw SQLite as reversible defaults. Pricing is deferred to before M2 billing work, and render/export sizes (DEC-04) are open. The platform and service boundary are settled: iOS 26, iPhone only, with no Immerse backend.
- **Group Films are deferred.**
  Accountless participation, serialized Group Movie recording, Host Release, and shared privacy exits remain documented for v2 and should not shape the minimum v1 architecture.
- **How it earns income is undecided.**
  There is no market-validation plan, kill criteria, or distribution plan in the repo yet, only a market-research file (`2026-09-29-nostalgic-camera-app-market-research-hipstamatic.md`).
  The income-by-end-of-2026 goal and Rep Today's PMF test both compete for the same solo capacity.
  The build started on 2026-10-02 without them, so defining kill criteria and a validation plan is now overdue rather than a precondition.

## Key files (in the repo)

- `2026-09-29-film-camera-experience-v1/2026-10-06-film-camera-experience-v1-prd-version-2.0.md`: the current PRD (version 2.1; the filename kept "2.0").
- `2026-09-29-film-camera-experience-v1/2026-09-29-film-camera-experience-v1-prd.md`: PRD 1.5, superseded and kept unchanged.
- `2026-09-29-film-camera-experience-v1/2026-09-29-film-camera-experience-v1-task-tracker.md`: the canonical checkbox list and source of truth for status.
- `2026-09-29-film-camera-experience-v1/2026-09-29-film-camera-experience-v1-architecture.md`: the approved v1 architecture baseline and early checks.
- `2026-09-29-film-camera-experience-v1/adr/`: decision records through ADR 0015 on `main` (0013 fresh-not-aged looks, 0014 Film Stock, 0015 Format References); ADR 0016 exists only on the unmerged looks branch.
- `2026-09-29-film-camera-experience-v1/sources/`: domain model and prototype notes.
- `2026-09-29-nostalgic-camera-app-market-research-hipstamatic.md`: market research.

## What a daily review should check

1. New commits, PRs, and issues on `hcho22/Immerse` since the last log.
2. Movement in the task tracker: new `[x]` items, resolved `DEC-*` decisions, and any owner or evidence annotations.
3. CI on `main`, device-validation evidence, and whether any backend has appeared (native app since 2026-10-02; no backend as of 2026-10-12).
   Also check firstmate's local worktrees for unpushed branches, since the looks slice is not on GitHub.
4. Scope changes, since the PRD asks for changes to be versioned rather than overwritten.
5. Whether hcho has made a go/no-go or kill-criteria decision, which belongs in `decisions/log.md` and `context/current-priorities.md`.

Daily entries live in `log/<YYYY-MM-DD>.md`.
