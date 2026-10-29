# Immerse

**One-liner:** A nostalgic, intentional film-camera iOS app (working title "Film Camera Experience").
Instead of picking a vintage filter after unlimited capture, you choose a Camera, load a bounded Film, shoot within its capacity, and the result is revealed by that format's own rules.

**Name:** "Immerse" is the repo name.
On 2026-10-28 hcho chose Rewound as the name the app shows (PRD decision DEC-01), but App Store Connect then refused "Rewound" as already in use, so Rewound is out.
A name-only rerun is pending, and until a name clears the app keeps showing Immerse; the PRD uses the descriptive title "Film Camera Experience".

**Repo:** https://github.com/hcho22/Immerse (`main`). **GitHub reports it as PUBLIC** (re-verified 2026-10-26), although earlier Mandu records called it private.
Its event history shows no visibility change, which is consistent with it having been public since creation on 2026-09-29; whether it should stay public is hcho's call.
**Local checkout:** `/Users/hcho/Developer/fm_private/firstmate-private/projects/Immerse` (branch `main`, verified 2026-10-26 at `8eb6f50`, clean tree, in sync with GitHub). This is firstmate's live home; `FM_Private` and `fm_private` resolve to the same folder.

**Strategic role: ranked #2, immediately after Rep Today (hcho's call, 2026-09-29).**
Added to daily tracking on 2026-09-29 at hcho's request.
Order is Rep Today, Immerse, Purvia, then the job search as the parallel hedge.
The ranking set where attention went next; full v1 native implementation started on 2026-10-02 (PR #7).
Logged in `decisions/log.md`.

---

## Status

_Last verified: 2026-10-26._

- **v1 is built (all four PRD 2.1 slices merged by 2026-10-13), and hcho now tries Debug builds on his own iPhone and turns what he sees into changes.**
  Sixteen PRs merged from #36 to #61 (`8eb6f50`, 2026-10-21); three change the app on his words: the Instant's camera comes back by itself after each print (#37), the shooting screen never turns, the 6x6 viewfinder is not reversed and it gets the iPhone's zoom steps (#38, ADR 0017), and a Debug-only "Develop at once" switch for immediate look feedback (#61).
  The other thirteen are CI flake fixes (eight) and test-plan re-pins (five); no PR is open and `main` has not moved since 2026-10-21 (re-verified 2026-10-26).
- **The formal iPhone pass has not started; it waits on hcho.**
  firstmate's hold `immerse-v1-hardware-validation` covers his iPhone 13 Pro, and `Evidence/NativeApp/manual-validation.md` is pinned to `8a104e1` with 42 lettered scenarios; P01-P05 (Develop at once) need a re-pin to `8eb6f50` to count.
  The plan still says "Nothing in this plan has been run on a phone", and no result has come back through firstmate's browser page of it.
  An iPhone 11, a second iPhone, and a small iPhone are not available, so those scenarios cannot run.
- **Go-to-market Candidate Package: `gtm/` in this folder, written by Gr0wthPilot run `immerse-20261025-043407` on 2026-10-25, untracked, unfinished, and not handed to gr0wthlab.**
  Front door `gtm/recap.html`; the Founder's ordered path is `gtm/launch-checklist.md`, and its first item is whether Immerse runs now or stays listening-only.
  It proposes the name Rewound (clearance UNVERIFIED), $4.99 a month or $29.99 a year, kill criteria K1 to K8 with a hard park at Day 90, and a 14-day Test Kit plus a Beta Cohort; hcho chose Rewound on 2026-10-28 and App Store Connect then refused it, and none of the rest is adopted.
  Gates are recorded through `critic-1` only; the site re-shoot failed because the run called `gp-chrome` by absolute path, which the sandbox does not exempt, not because Chrome broke (`log/2026-10-26.md`).
  gr0wthlab still lists Immerse as `listening-only`; Mandu never edits the run's output.
- **CI: 11 of 16 `main` runs green since `4906054`, the last two clean, and no run since 2026-10-21**; only 8 were green at the first try (two passed through a permitted rerun, one on a second attempt).
  The five failures were four flaky tests, each followed by a fix PR, and one run that never got a Mac runner; clean runs take 49 to 74 minutes.
  `main` has no branch protection or rulesets.
- **Decisions:** DEC-11 is checked; DEC-04 is decided in substance; DEC-05 has its rule but waits on hcho's seven sample shots; DEC-14 is "no analytics, learn from TestFlight interviews and Apple reports"; firstmate recorded the native stack (DEC-03) as answered on 2026-10-13, but the tracker box is unchecked.
  DEC-01 (name) is open again after App Store Connect refused Rewound on 2026-10-28, with a name-only rerun pending; DEC-02 (price) is open, and hcho has adopted no kill criteria or validation plan; the Candidate Package above proposes all four.
- **Task tracker:** 253 items, 10 checked (5 discovery, 5 decisions), 135 v1 and 108 v2 items open; no implementation task is checked until a phone has run it.
  The PRD and tracker headers still describe a planning baseline.
- **The repo is public**; since 10-12 that includes hcho's film-look calibration files and two boards that hotlink reference photos that are not openly licensed.
  On 2026-10-13 hcho did not say the visibility was unintended, which is not an explicit decision, and nothing has been recorded since.
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

- **No price or final brand** (DEC-01, DEC-02); Rewound was chosen on 2026-10-28 and then refused by App Store Connect, so the app shows Immerse until a rerun name clears; the Candidate Package's $4.99 a month or $29.99 a year is unadopted. firstmate recorded hcho's "1. fine" on the native stack (Swift/SwiftUI and eight flow choices) on 2026-10-13, though the storage library was not named to him and the tracker's DEC-03 box is unchecked. Pricing is deferred to before M2 billing work. Render and export sizes (DEC-04) were decided on 2026-10-13 except the Movie capture's native 4:3 size, which stays provisional. The platform and service boundary are settled: iOS 26, iPhone only, with no Immerse backend.
- **Group Films are deferred.**
  Accountless participation, serialized Group Movie recording, Host Release, and shared privacy exits remain documented for v2 and should not shape the minimum v1 architecture.
- **How it earns income is undecided.**
  The repo has no market-validation plan, kill criteria, or distribution plan, only a market-research file (`2026-09-29-nostalgic-camera-app-market-research-hipstamatic.md`).
  The Candidate Package in `gtm/` (2026-10-25) proposes all three, and hcho has adopted none.
  The income-by-end-of-2026 goal and Rep Today's PMF test both compete for the same solo capacity.
  The build started on 2026-10-02 without them, so defining kill criteria and a validation plan is now overdue rather than a precondition.

## Key files (in the repo)

- `2026-09-29-film-camera-experience-v1/2026-10-06-film-camera-experience-v1-prd-version-2.0.md`: the current PRD (version 2.1; the filename kept "2.0").
- `2026-09-29-film-camera-experience-v1/2026-09-29-film-camera-experience-v1-prd.md`: PRD 1.5, superseded and kept unchanged.
- `2026-09-29-film-camera-experience-v1/2026-09-29-film-camera-experience-v1-task-tracker.md`: the canonical checkbox list and source of truth for status.
- `2026-09-29-film-camera-experience-v1/2026-09-29-film-camera-experience-v1-architecture.md`: the approved v1 architecture baseline and early checks.
- `2026-09-29-film-camera-experience-v1/adr/`: decision records through ADR 0017 on `main` (0013 fresh-not-aged looks, 0014 Film Stock, 0015 Format References, 0016 the Instant and Super 8 exceptions, 0017 the shooting screen that never turns and the 6x6's normal viewfinder and zoom).
- `Evidence/NativeApp/manual-validation.md`: the manual iPhone test plan, pinned to the current candidate (`8a104e1` as of 2026-10-23).
- `2026-09-29-film-camera-experience-v1/sources/`: domain model and prototype notes.
- `2026-09-29-nostalgic-camera-app-market-research-hipstamatic.md`: market research.

## What a daily review should check

1. New commits, PRs, and issues on `hcho22/Immerse` since the last log.
2. Movement in the task tracker: new `[x]` items, resolved `DEC-*` decisions, and any owner or evidence annotations.
3. CI on `main`, device-validation evidence, and whether any backend has appeared (native app since 2026-10-02; no backend as of 2026-10-26).
   Also check firstmate's local worktrees (`~/.treehouse/Immerse-3833fe/`) for unpushed branches, since GitHub alone can understate progress.
4. Scope changes, since the PRD asks for changes to be versioned rather than overwritten.
5. Whether hcho has made a go/no-go or kill-criteria decision, which belongs in `decisions/log.md` and `context/current-priorities.md`.
6. The Candidate Package in `gtm/`: its gates in `gtm/run-journal.json`, and whether hcho has said its Handoff line, "Immerse - hand to gr0wthlab".

Daily entries live in `log/<YYYY-MM-DD>.md`.
