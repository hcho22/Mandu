# License and source

This folder is a modified copy of `skills/ad-creative/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
It was copied into Mandu on 2026-10-24 for Gr0wthPilot and is updated only by hand, pinned to that commit.
The upstream `evals/` folder is left out, since no Mandu skill keeps evals.
It has no `## Memory` section and no `MEMORY.md`, since Gr0wthPilot's own `MEMORY.md` covers its phase skills.
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
- `description`: removed the 'creative retro' trigger, since a Product has no results for a retro before its Test Kit runs, and added what this copy does in Gr0wthPilot.
- "Before Starting": the `.agents/product-marketing.md` check ("Check for product marketing context first") now points at the Candidate Package's `01-research/product-facts-brief.md`.
- "Before Starting": cut "Check its **Learnings** section before drafting: angles, offers, and formats already tested there shouldn't be re-proposed as new ideas, and active lessons apply unless the user says otherwise."
- Grounding rules: "stop and ask the user to populate it before generating" now reads "ground every concept in the Candidate Package's sourced research instead (its `01-research/` files, each source listed in `sources.md`); never ask the user to populate it".
- Added an "In Gr0wthPilot" note after the "Recommended workflow for scaled production" list, pointing step 1 ("Generate hero creative with AI tools") to the read-first "No new spending" rule.
- Cut "Tool Integrations": the "For pulling performance data and managing campaigns, see the tools registry" line, the ad-platform CLI table for pulling performance data and managing campaigns, the "Workflow: Pull Data, Analyze, Generate" block ending "5. Upload to platform", and the "Skip the plumbing" note with its Magister, `tools/SETUP.md`, Supermetrics, and Coupler pointers, since each needs an ad account, a new key, or a new sign-up.

In `references/creative-review-page.md`:

- "Producing and delivering it", step 4: "hand off the folder (html + `images/`), or host it." and the sentence after it ("For a client link, `vercel deploy` or any static host works", through "with local assets.") now read "leave the folder (html + `images/`) in the Candidate Package; the Founder hands it off or hosts it himself after Handoff."

In `references/creative-roadmap.md`:

- Added an "In Gr0wthPilot" note under the Step 1 signals table: the account-performance signal is empty, and the `google-ads` / `meta-ads` / `linkedin-ads` / `tiktok-ads` CLIs are never connected or run.
- Added an "In Gr0wthPilot" note at the head of "Step 5: The Monthly Creative Retro" to skip the step, so no retro, results table, or `## Learnings` section is written.

In `references/generative-tools.md`:

- Added an "In Gr0wthPilot" note after the "Workflow: Voice + Video" block, pointing steps 2 and 3 (ElevenLabs/OpenAI TTS, Runway, Veo, Seedance) to the read-first "No new spending" rule.
- "Remotion Workflow for Ad Creative": cut step "5. Upload to ad platform".
- Added an "In Gr0wthPilot" note after "Recommended Workflow for Scaled Ad Production", pointing step 1 ("Generate hero creative with AI (Nano Banana, Flux, Veo)") to the read-first "No new spending" rule.

In `references/motion-video-ads.md`:

- The brand slots contract: "(or `.agents/product-marketing.md`)" now reads "(the Candidate Package's `02-brand/` files)".
- Added an "In Gr0wthPilot" note at the head of "Pipeline (provider-agnostic)", pointing stages 2 to 4 (paid image, video, and voice models) to the read-first "No new spending" rule.

In `references/platform-specs.md`:

- "Character Counting Tips": cut "Always verify in the platform's ad preview before launching", since the ad preview needs an ad account.
