# Master profile

The single source of truth for hcho's job applications: every Claim about his experience, with the evidence behind it.
Resumes and application answers are built from it; the `.docx` files in `../Resume/` are older and contain overstated lines, so never copy from them.
Terms (Claim, Evidence, Evidence scale, Skill index, Application packet) are defined in the root `CONTEXT.md`.

## Files

| File | What it is | Edit it? |
|---|---|---|
| `master-profile.yaml` | The profile itself: periods, projects, skills vocabulary, and Claims | Yes, or ask Mandu |
| `master-profile.md` | Readable view of every Claim, grouped by period and project | No, generated |
| `skill-index.md` | Per skill: paid-job time, project time, coursework, and lanes | No, generated |
| `render_profile.py` | Checks the rules and regenerates both pages | Only to change the rules |
| `test_render_profile.py` | Tests for the rules and the year math | Alongside the script |

## Everyday use

- **Something new to claim** (a shipped feature, a new number, a finished course): tell Mandu, for example "add to my profile: Rep Today passed App Review".
  Mandu finds the evidence, writes the Claim, and re-renders.
- **Editing by hand:** change `master-profile.yaml`, then run `python3 render_profile.py` in this folder.
  It refuses to write anything if a Claim breaks a rule and lists what to fix.
- **Checking a job requirement** such as "3+ years of professional Python": look the skill up in `skill-index.md`.
  Only the Employer column counts as professional experience.
- **Before using a number in an application:** run `python3 render_profile.py --stale` to list numbers older than 14 days, then re-read their sources.
- **Verifying nothing drifted:** `python3 render_profile.py --check` fails if the pages are out of date; `python3 -m unittest test_render_profile` runs the tests.

## Open notes

Claims with an `open_question` show it in `master-profile.md`.
As of 2026-10-08 they cover Coursera completion dates, Omdena project months and details, whether the Zebra count of 6 was products or product lines, whether the 10 technicians reported to hcho, and the B.S. graduation year.

## Where it is used

Application packets in `../applications/` are built only from this profile; see the `application-packet` skill.
