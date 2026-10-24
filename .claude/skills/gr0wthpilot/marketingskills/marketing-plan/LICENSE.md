# License and source

This folder is a modified copy of `skills/marketing-plan/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
It was copied into Mandu on 2026-10-24 for Gr0wthPilot and is updated only by hand, pinned to that commit.
The upstream `evals/` folder is left out, since no Mandu skill keeps evals.
It has no `## Memory` section or `MEMORY.md` of its own, since Gr0wthPilot's `MEMORY.md` covers its phase skills.
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
- `description`: added what this copy does in Gr0wthPilot.
- "How this skill is invoked": added an "In Gr0wthPilot" note under the heading (the Product is the client; skip the slash command, the resume step, and the path-safety rule that guards `~/marketing-plans/`), cut the example "`/marketing-plan` (will prompt for client name)", and cut the sentence "Finalized plans are never silently overwritten", which ends "the user is asked whether to revise as v{N+1}, start fresh, or re-open a section."
- Phase 1 (INIT): added an "In Gr0wthPilot" note after its paragraph: a tool counts as wired only when its key is already in the Product's `.env`, the intake is answered from sources and never asked, and nothing is saved to `research.md`.
- Phase 2 (REVIEW): replaced the interactive review ("Present each section's draft in chat. For each section you can:" with its Approve, Adjust, Add observations, and Expand options, and "Save each confirmed section to the progress file as you go. The skill is resumable", with its `/marketing-plan client-name` resume) with an "In Gr0wthPilot" note: draft each section once, with no approval round or progress file.
- Phase 3 (FINALIZE): cut "Optionally offer to publish to a shared GitHub repo (e.g., `{client-org}/{client-context}/marketing/plan.md`) if the user wants to share it with the team."
- Cross-references, item 2: "Sets up the foundational `.agents/product-marketing.md` context file (positioning, ICP, voice). Read this first;" now reads "Its outline shapes the Candidate Package's `01-research/product-facts-brief.md` (positioning, ICP, voice). Read that brief first;".
- "Output format": added an "In Gr0wthPilot" note under the heading: the deliverable is the Candidate Package's `06-channels/channel-plan.md`.
- "File layout per plan": added an "In Gr0wthPilot" note under the heading: none of the layout is made.
- Related skills, `product-marketing`: "Captures positioning, ICP, voice in `.agents/product-marketing.md`" now reads "Captures positioning, ICP, voice in the Candidate Package's `01-research/product-facts-brief.md`".

In `references/methodology.md`:

- Added an "In Gr0wthPilot" note under the opening paragraph: skip Steps 1.1, 1.1.1, 1.1.2, 1.6, 2.1, and 3.5, "Resuming a plan", and the path-safety rule that confines work to `~/marketing-plans/`; read the Candidate Package and the Product's repository in place of `materials/` and `research.md`, and write the plan into `06-channels/channel-plan.md` in place of `sections/` and `final_plan.md`.
- Step 1.1.2, case 6: cut "Ask the user:" and its question ("This plan is finalized (v{N}). Want to (a) revise it as v{N+1}, (b) start a fresh plan in a new folder, or (c) re-open a specific section?").
- Step 1.3: added an "In Gr0wthPilot" note under "If MCPs/APIs are wired for this client, pull:": a tool counts as wired only when its key is already in the Product's `.env`.
- Step 1.4: "For every gap in the materials, ask the user." now reads "For every gap in the materials, answer from the sources in "Never ask anything" in "Gr0wthPilot copy: read first" in `SKILL.md`, and decide and log what nothing answers."
- Phase 2 goal: cut "getting user confirmation," from "drafting each, getting user confirmation, saving as you go."
- Step 2.2: replaced "Then in chat:" and its six steps (present the draft, ask "Approve, adjust, or expand?", iterate until the user confirms, save the confirmed text to `sections/`, check the box in `progress.md`, move to the next section) with an "In Gr0wthPilot" note: draft each section once, with no chat review.
- Phase 3 goal: cut "and optionally publish to a shared repo" from "Produce `final_plan.md` and optionally publish to a shared repo."
- Cut Step 3.4, "Publish (optional)": asking whether to publish the plan to a shared GitHub repo, then cloning it, committing, and pushing. Step 3.5 keeps its upstream number.
- "Resuming a plan": cut the line "If the user says *"start over"*", which goes on to ask whether to delete the existing folder or move it to `archive/` first.

In `references/ops-stack-mapping.md`:

- Cross-cutting skills table, `product-marketing` row: "Set up the `.agents/product-marketing.md` context file (positioning, ICP, voice)" now reads "Outline the Candidate Package's `01-research/product-facts-brief.md` (positioning, ICP, voice)".
