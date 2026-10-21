# Immerse

**One-liner:** A nostalgic, intentional film-camera iOS app (working title "Film Camera Experience").
Instead of picking a vintage filter after unlimited capture, you choose a Camera, load a bounded Film, shoot within its capacity, and the result is revealed by that format's own rules.

**Name:** "Immerse" is the repo name.
The final product name is not selected (PRD open decision DEC-01), and the PRD uses the descriptive title "Film Camera Experience".

**Repo:** https://github.com/hcho22/Immerse (`main`). **GitHub reports it as PUBLIC** (re-verified 2026-10-15), although earlier Mandu records called it private.
Its event history shows no visibility change, which is consistent with it having been public since creation on 2026-09-29; whether it should stay public is hcho's call.
**Local checkout:** `/Users/hcho/Developer/fm_private/firstmate-private/projects/Immerse` (branch `main`, verified 2026-10-15 at `4906054`, clean tree, in sync with GitHub). This is firstmate's live home; `FM_Private` and `fm_private` resolve to the same folder.

**Strategic role: ranked #2, immediately after Rep Today (hcho's call, 2026-09-29).**
Added to daily tracking on 2026-09-29 at hcho's request.
Order is Rep Today, Immerse, Purvia, then the job search as the parallel hedge.
The ranking set where attention went next; full v1 native implementation started on 2026-10-02 (PR #7).
Logged in `decisions/log.md`.

---

## Status

_Last verified: 2026-10-15._

- **All four PRD 2.1 implementation slices are merged, and the manual iPhone test candidate is ready (`771d5e2`).**
  hcho approved the last look boards (6x6, 16mm color and black-and-white) on 2026-10-12, and the looks slice merged as [PR #25](https://github.com/hcho22/Immerse/pull/25) on 2026-10-13.
  Ten more PRs followed through #35 (`4906054`, 2026-10-15), each on a decision he gave: four-part CI with a narrow rerun rule (#27), Darkroom limits and export checks (#28), the Instant's contrast and toning range (#29), a low-storage warning (#30), Crop fit on short screens (#31), and a side-by-side landscape Darkroom (#34).
  [PR #36](https://github.com/hcho22/Immerse/pull/36), aimed at three flaky failures, is open.
- **Still nothing validated on a physical iPhone; the pass waits on hcho.**
  firstmate's hold `immerse-v1-hardware-validation` names `771d5e2` and his iPhone 13 Pro, and the plan in `Evidence/NativeApp/manual-validation.md` leaves him a handful of calls before starting.
  An iPhone 11, a second iPhone, and a small iPhone are not available, so those scenarios cannot run.
- **CI: 6 of 11 `main` runs green since `0e69ed2`, the last six green**, the newest only after a permitted dropped-touch rerun.
  Failures were four different tests plus one run that hit the 120-minute cap; runs now take 46 to 62 minutes.
  `main` has no branch protection.
- **Decisions:** DEC-11 is checked; DEC-04 is decided in substance; DEC-05 has its rule but waits on hcho's seven sample shots; DEC-14 is "no analytics, learn from TestFlight interviews and Apple reports"; firstmate recorded the native stack (DEC-03) as answered on 2026-10-13, but the tracker box is unchecked.
  DEC-01 (name) and DEC-02 (price) are open, and no kill criteria or validation plan exists.
- **Task tracker:** 253 items, 10 checked (5 discovery, 5 decisions), 135 v1 and 108 v2 items open; no implementation task is checked until a phone has run it.
  The PRD and tracker headers still describe a planning baseline.
- **The repo is public**; since 10-12 that includes hcho's film-look calibration files and two boards that hotlink reference photos that are not openly licensed.
  On 2026-10-13 hcho did not say the visibility was unintended, which is not an explicit decision.
- **PRD 2.0 and 2.1 (2026-10-07):** five Cameras; the 6x6 and 16mm dropped their decade and gained a color or black-and-white Film Stock; the 16mm runs 2:47; looks are "fresh, not aged" except the Instant and Super 8 (ADR 0016); Darkroom contrast grades apply to every Photo Film.
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

- **No price or final brand** (DEC-01, DEC-02). firstmate recorded hcho's "1. fine" on the native stack (Swift/SwiftUI and eight flow choices) on 2026-10-13, though the storage library was not named to him and the tracker's DEC-03 box is unchecked. Pricing is deferred to before M2 billing work. Render and export sizes (DEC-04) were decided on 2026-10-13 except the Movie capture's native 4:3 size, which stays provisional. The platform and service boundary are settled: iOS 26, iPhone only, with no Immerse backend.
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
- `2026-09-29-film-camera-experience-v1/adr/`: decision records through ADR 0016 on `main` (0013 fresh-not-aged looks, 0014 Film Stock, 0015 Format References, 0016 the Instant and Super 8 exceptions).
- `Evidence/NativeApp/manual-validation.md`: the manual iPhone test plan, pinned to the current candidate.
- `2026-09-29-film-camera-experience-v1/sources/`: domain model and prototype notes.
- `2026-09-29-nostalgic-camera-app-market-research-hipstamatic.md`: market research.

## What a daily review should check

1. New commits, PRs, and issues on `hcho22/Immerse` since the last log.
2. Movement in the task tracker: new `[x]` items, resolved `DEC-*` decisions, and any owner or evidence annotations.
3. CI on `main`, device-validation evidence, and whether any backend has appeared (native app since 2026-10-02; no backend as of 2026-10-15).
   Also check firstmate's local worktrees (`~/.treehouse/Immerse-3833fe/`) for unpushed branches, since GitHub alone can understate progress.
4. Scope changes, since the PRD asks for changes to be versioned rather than overwritten.
5. Whether hcho has made a go/no-go or kill-criteria decision, which belongs in `decisions/log.md` and `context/current-priorities.md`.

Daily entries live in `log/<YYYY-MM-DD>.md`.
