# License and source

This folder is a modified copy of `skills/ab-testing/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
It was copied into Mandu on 2026-10-24 for Gr0wthPilot and is updated only by hand, pinned to that commit.
The upstream `evals/` folder is left out, since no Mandu skill keeps evals.
It has no `## Memory` section or `MEMORY.md`, since Gr0wthPilot's own `MEMORY.md` covers its phase skills.
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
- `description`: added what this copy is for in Gr0wthPilot ("In Gr0wthPilot this copy pre-registers the hook-only A/B pairs of a Candidate Package's Test Kit; it runs no test and reads no results."), before "For tracking implementation, see analytics."
- "Initial Assessment": the `.agents/product-marketing.md` check now points at the Candidate Package's product-facts brief, and "only ask for information not already covered or specific to this task" now reads "look up only what it does not cover or what is specific to this task, in the sources that block names".
- "Documentation": added an "In Gr0wthPilot" note after "Decision and learnings" that the hypothesis and variants go in `05-social-pmf/ab-pairs.md`, and that results, the decision, and learnings come from gr0wthlab's Test Kit after Handoff, never from the run.
- "The Experiment Loop": added an "In Gr0wthPilot" note after the loop that a run does steps 1 and 2 and the design half of step 3 ("Design and run the test"), and that running the tests, steps 4 to 6 ("Generate new hypotheses from learnings" among them), the playbook, and the cadence come after Handoff with gr0wthlab's Test Kit.

In `references/test-templates.md`:

- Test Plan Template, "Pre-Launch Checklist": cut "Stakeholders informed" and "Calendar hold for analysis date" (contacting people and scheduling).
- Results Documentation Template: added an "In Gr0wthPilot" note under the heading that a run never fills in this template, its "Learnings" section included.
- Quick Test Brief Template: added an "In Gr0wthPilot" note after the template to leave "**Result**" at TBD and "**Learnings**" empty.
