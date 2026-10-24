# License and source

This folder is a modified copy of `skills/image/` from https://github.com/coreyhaines31/marketingskills at commit `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (2026-10-19).
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
- `description`: added what this copy is for in Gr0wthPilot ("In Gr0wthPilot this copy builds a Candidate Package's Launch Set profile assets and carousels from HTML, SVG, and the Product's real screens."), before "For paid ad image creative".
- "Before Starting": the `.agents/product-marketing.md` check now points at the Candidate Package's product-facts brief, and "only ask for information not already covered or specific to this task" now reads "look up only what it does not cover or what is specific to this task, in the sources that block names".
- "Before Starting": "Gather this context (ask if not provided)" now reads "Gather this context (answer it from the sources in "Gr0wthPilot copy: read first" if not provided)".
- "Blog & Article Hero Images": added an "In Gr0wthPilot" note after the workflow that step 2 ("Generate with AI", with Flux, Gemini, or Ideogram) runs a paid image model, pointing to "No new spending".
- "Profile & Listing Banners": added an "In Gr0wthPilot" note after the workflow that step 4 ("Generate with Canva/Figma templates or Ideogram") uses Ideogram only under "No new spending" and Canva or Figma not at all.
- "Optimization Checklist": cut "**Use a CDN** with auto-optimization (Cloudflare, Vercel, Imgix, Cloudinary)" (signing up for and deploying to a hosting service).

In `references/ai-image-prompting.md`:

- "Batch Generation Workflow": added an "In Gr0wthPilot" note after the steps that steps 1, 4, and 5 ("Generate 3-4 test images", "Use Flux multi-reference", "Batch generate") run a paid image model, pointing to "No new spending".
