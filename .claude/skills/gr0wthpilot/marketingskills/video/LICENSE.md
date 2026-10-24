# License and source

This folder is a modified copy of `skills/video/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
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
- `description`: added what this copy is for in Gr0wthPilot ("In Gr0wthPilot this copy makes a Candidate Package's product walkthrough video from the Product's real app screens with Remotion or ffmpeg; it publishes and schedules nothing."), before "For video content strategy".
- "Before Starting": the `.agents/product-marketing.md` check now points at the Candidate Package's product-facts brief, and "only ask for information not already covered or specific to this task" now reads "look up only what it does not cover or what is specific to this task, in the sources that block names".
- "Before Starting": "Gather this context (ask if not provided)" now reads "Gather this context (answer it from the sources in "Gr0wthPilot copy: read first" if not provided)".
- "Repurposing Workflow": cut the last step, "Distribute: TikTok, Reels, Shorts, LinkedIn", with the arrow above it, and added an "In Gr0wthPilot" note after the diagram to use Descript, Opus Clip, and CapCut only under "No new spending".
- "Product Demo Video": added an "In Gr0wthPilot" note after the steps that steps 4 ("AI B-roll", with Veo or Runway) and 5 ("Voiceover", "record yourself or use AI avatar") use those tools only under "No new spending", and that a voiceover the Founder would record himself is left out.
- "Batch Social Clips": cut step 5, "**Schedule** across platforms", and added an "In Gr0wthPilot" note that step 4 ("via CapCut or Captions.ai") uses those tools only under "No new spending".
- "Common Mistakes": item 3, "**Uncanny valley avatars**", no longer says "if avatar quality matters, invest in HeyGen Creator+ tier".

In `references/product-demo-recording.md`:

- "Before Recording", item 5: "Pull these from product marketing context when it exists" now reads "Pull these from the Candidate Package's `02-brand/` folder".
- "Optional Narration": added an "In Gr0wthPilot" note before the steps that step 1 ("Generate one clip per caption with a TTS provider") runs a paid TTS provider, pointing to "No new spending".
- "Optional Narration", "API keys": "If the key isn't set, tell the user which variable to set in their own shell and fall back to a silent recording in the meantime" now reads "If the key isn't set, fall back to a silent recording".

In `references/ai-video-prompting.md`:

- "Prompting Workflow": added an "In Gr0wthPilot" note after the steps that steps 3 and 4 ("Generate 3-4 variations", "Iterate on the best") run a paid video model, pointing to "No new spending".

In `references/edit-anatomy.md`:

- "Step 4": added an "In Gr0wthPilot" note under the heading that the review ("Show the beat sheet before anyone edits anything") is the agent's own and waits for no one.
