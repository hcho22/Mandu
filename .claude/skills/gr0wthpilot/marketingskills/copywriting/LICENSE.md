# License and source

This folder is a modified copy of `skills/copywriting/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
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
- "Before Writing": the `.agents/product-marketing.md` check ("Check for product marketing context first", "read it before asking questions. Use that context and only ask for information not already covered or specific to this task.") now reads "Read the Candidate Package first" and points at the Candidate Package's product-facts brief, looking up what it does not cover in the sources the read-first block names.
- "Before Writing": cut the Learnings line ("Check its **Learnings** section before drafting: angles and claims already tested there shouldn't be re-proposed as new ideas, and active lessons apply unless the user says otherwise.").
- "Gather this context (ask if not provided):" now reads "Gather this context (answer it from the sources in "Gr0wthPilot copy: read first" if not provided):".

In `references/ai-tells.md`:

- Rewrite Rules, rule 5 ("Don't invent to de-slop"): "Mark it `[NEED: proof]` and ask." now reads "Mark it `[NEED: proof]`.".
