# License and source

This folder is a modified copy of `skills/sales-enablement/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
It was copied into Mandu on 2026-10-24 for Gr0wthPilot and is updated only by hand, pinned to that commit.
The upstream `evals/` folder is left out, since no Mandu skill keeps evals.
It has no `MEMORY.md` and no `## Memory` section, since Gr0wthPilot's own `MEMORY.md` covers its phase skills.
The changes from upstream are listed under "Changes from upstream" below.

## Upstream license

```
MIT License

Copyright (c) 2025 Corey Haines

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Changes from upstream

In `SKILL.md`:

- Added the "Gr0wthPilot copy: read first" block under the title.
- `description`: cut the 'cold call script' and 'voicemail script' triggers, so the trigger list now ends at "'what should I give my sales reps.'"; and added what this copy does in Gr0wthPilot.
- "Before Starting": the `.agents/product-marketing.md` check ("Check for product marketing context first") now reads "Check the Candidate Package first" and points at the Candidate Package's `01-research/product-facts-brief.md`.
- "Sales Uses What Sales Trusts": cut "Involve reps in creation." and "Test drafts with your top performers first."
- Battle Cards: "**Ask which competitor.**" now reads "**Decide which competitor.**", and "ask in one short question. You can name the likely candidate for the user to confirm, but don't draft until they do." now says to pick the likely candidate from the Candidate Package's `01-research/competitor-<slug>.md` files and log the pick `[DECIDED BY AGENT]` with the rejected alternative in `decisions-log.md` before drafting.
- Win-Loss Analysis, step 6: "send product gaps to the product team" now reads "list product gaps for the product team".
- Demo Scripts & Talk Tracks: cut the "**For cold call openers, voicemails, and first-minute pushback**" pointer to `references/cold-call-scripts.md`.

In `references/win-loss-analysis.md`:

- Interview Questions: cut "Ask within 2-4 weeks of the decision. Have someone other than the deal's rep do it if possible.", keeping the questions.

Left out of `references/`:

- `cold-call-scripts.md` (cold-call openers, pushback, voicemail, and gatekeeper scripts and call recording: calls that reach people).
