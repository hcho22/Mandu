# License and source

This folder is a modified copy of `skills/customer-research/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
It was copied into Mandu on 2026-10-23 and is updated only by hand, pinned to that commit.
The upstream `evals/` folder is left out, since no Mandu skill keeps evals.
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

- Added the "Mandu copy: read first" block under the title, and the `## Memory` section at the end.
- `description`: added what this copy is for in Mandu.
- "Before Starting": the `.agents/product-marketing.md` check now points at the product's Go-To-Market Package.
- "Questions to Ask Before Proceeding": "the product marketing context file" now reads "the Go-To-Market Package".
- Mode 3: removed "incentives" from the playbook list and "and **incentives** — $50/call, $5/survey" from the summary bullet.
- Persona Generation: cut "When there are no reviews yet" (provisional personas from proxy sources in place of evidence).

In `references/interviews-and-surveys.md`:

- Cut the "Incentives" heading and its $50-per-call, $5-per-survey, and gift-card bullets, keeping "Aim for 10 calls, be happy with 5".
- Outreach template: subject "Quick favor — 30 min, on us" now reads "Quick favor — 30 min", and the gift-card line is cut.
- Survey guardrails: cut the "$5/response incentive" bullet.

In `references/source-guides.md`:

- Reddit tools: cut the Pullpush.io bullet (an archive of Reddit posts, a route around Reddit's `robots.txt`).
