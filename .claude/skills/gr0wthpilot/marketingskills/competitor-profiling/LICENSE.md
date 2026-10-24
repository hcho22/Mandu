# License and source

This folder is a modified copy of `skills/competitor-profiling/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
It was copied into Mandu on 2026-10-24 for Gr0wthPilot and is updated only by hand, pinned to that commit.
The upstream `evals/` folder is left out, since no Mandu skill keeps evals.
There is no `MEMORY.md` or `## Memory` section, since Gr0wthPilot's own `MEMORY.md` covers its phase skills.
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
- "Initial Assessment": the "Check for product marketing context first" check, which read `.agents/product-marketing.md` (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md`), is now "Check the Candidate Package first" and reads the Candidate Package's `01-research/product-facts-brief.md`.
- "Initial Assessment", item 2: "(if not in product marketing context)" now reads "(if not in the product-facts brief)".
- Added an "In Gr0wthPilot" note after the "Tool Stack Selection" fallback paragraph, after Phase 1's "If Firecrawl is unavailable" paragraph, and after Phase 2's opening paragraph, pointing to the read-first rule "No new spending": a tool whose key is not already in the Product's `.env` counts as unavailable.
- "Facts Over Opinions": "confirm it in their docs or a trial" now reads "confirm it in their docs" (a trial means signing up).

In `references/tool-reference.md`:

- Added an "In Gr0wthPilot" note under the opening line, pointing to the read-first rule "No new spending": every tool except WebFetch is used only when its key is already in the Product's `.env`.
