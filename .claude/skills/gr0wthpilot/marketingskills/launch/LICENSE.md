# License and source

This folder is a modified copy of `skills/launch/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
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
- `description`: cut the site-launch triggers ('site launch,' 'go live,' 'pre-launch QA,'), since `references/site-launch-qa.md` is left out, and added what this copy does in Gr0wthPilot.
- "Before Starting": the `.agents/product-marketing.md` check ("Check for product marketing context first", "read it before asking questions. Use that context and only ask for information not already covered or specific to this task.") now reads "Read the Candidate Package first" and points at the Candidate Package's product-facts brief, looking up what it does not cover in the sources the read-first block names.
- Borrowed Channels: added an "In Gr0wthPilot" note after the "Be proactive, not passive" steps: step 3 ("Use tools like SparkToro or Listen Notes") runs only with a key already in the Product's `.env`, and steps 2 ("Pitch win-win collaborations") and 4 ("Set up affiliate/referral incentives") go into the plan as the Founder's.
- Added an "In Gr0wthPilot" note under the "Five-Phase Launch Approach" intro, pointing to the read-first rule that each phase's actions are the Founder's steps after Handoff.
- Product Hunt Launch Strategy: added an "In Gr0wthPilot" note under "How to Launch Successfully": only steps 2 ("Optimize your listing") and 3 ("Study successful launches") of "Before launch day" happen in the run, with the listing as a local draft.
- Added an "In Gr0wthPilot" note under the "Post-Launch Product Marketing" intro and under the "Ongoing Launch Strategy" intro, pointing to the read-first rule that those actions are the Founder's.
- Launch Checklist: added an "In Gr0wthPilot" note under the heading (the Founder's checklist; the run finishes only the items that are local files), and cut the Pre-Launch item "Site QA done if the launch includes a new site, redesign, or migration (see references/site-launch-qa.md)".

In `references/`:

- Left out `site-launch-qa.md` (the checks for taking a website live: deploying, test form submissions, installing tracking, submitting the sitemap in Search Console and Bing Webmaster Tools, rollback, and post-launch monitoring).
