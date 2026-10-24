# License and source

This folder is a modified copy of `skills/analytics/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
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
- `description`: cut the "set up tracking" and "analytics implementation" triggers, since the setup steps and implementation guides are left out; added what this copy does in Gr0wthPilot.
- "Initial Assessment": the `.agents/product-marketing.md` check ("Check for product marketing context first", "read it before asking questions. Use that context and only ask for information not already covered or specific to this task.") now reads "Read the Candidate Package first" and points at the Candidate Package's product-facts brief, looking up what it does not cover in the sources the read-first block names.
- "GA4 Implementation": cut "Quick Setup" and its five steps ("Create GA4 property and data stream", "Install gtag.js or GTM", "Enable enhanced measurement", "Configure custom events", "Mark conversions in Admin"), keeping "Custom Event Example".
- "GA4 Implementation": cut the pointer "**For detailed GA4 implementation**: See [references/ga4-implementation.md](references/ga4-implementation.md)".
- "Google Tag Manager": cut the pointer "**For detailed GTM implementation**: See [references/gtm-implementation.md](references/gtm-implementation.md)".

In `references/`:

- Left out `ga4-implementation.md`, a guide to configuring a live Google Analytics 4 property (data streams, conversions marked in Admin, custom definitions, audiences, internal-traffic filters, and Google Ads linking and audience export).
- Left out `gtm-implementation.md`, a guide to installing and publishing tags on a live site through Google Tag Manager, including the Facebook pixel and other ad pixels.
