# Turning Claude into a One-Person Marketing Team

**Claude Code + Higgsfield — full project walkthrough**

---

## Overview

A non-technical walkthrough of building a persistent marketing "team" inside Claude Code, connected to Higgsfield (a multi-model AI image/video platform) via MCP. The speaker (Nate Herk) uses a fictional brand — **PerkForm**, a canned protein coffee energy drink — to demonstrate the full arc: set up a project folder, load business context and brand guidelines, connect Higgsfield as a connector, then generate a website, ad creatives, a sizzle reel, Instagram carousels, UGC video ads, and finally an Excel creative tracker.

The core argument: you *could* use Higgsfield directly, but routing everything through a Claude Code project gives you three things Higgsfield alone can't — **persistent business context**, **reusable skills**, and **enforced brand guidelines** — which is what separates branded output from generic AI slop.

**Real cost data from the session:** 18 ad creatives for $3.43 · one sizzle reel (2 formats) for $17.55 · 5 Instagram carousels for $9.56.

---

## Table of Contents

1. [What We're Building (Roadmap)](#1-what-were-building-roadmap)
2. [The Prerequisite: The Three Ps](#2-the-prerequisite-the-three-ps)
3. [Why Higgsfield, and Why Route It Through Claude](#3-why-higgsfield-and-why-route-it-through-claude)
4. [Step 1 — Get Base Assets (Logo, Product Shots)](#4-step-1--get-base-assets-logo-product-shots)
5. [Step 2 — Install Claude Code and Create the Project Folder](#5-step-2--install-claude-code-and-create-the-project-folder)
6. [Step 3 — Build CLAUDE.md and the Context Files](#6-step-3--build-claudemd-and-the-context-files)
7. [Skills: Reusable Recipes (and the "grill me" Trick)](#7-skills-reusable-recipes-and-the-grill-me-trick)
8. [Step 4 — Load Assets Into the Project](#8-step-4--load-assets-into-the-project)
9. [Step 5 — Connect Higgsfield to Claude (MCP Connector)](#9-step-5--connect-higgsfield-to-claude-mcp-connector)
10. [Step 6 — Build the Website (scroll-world)](#10-step-6--build-the-website-scroll-world)
11. [Step 7 — Generate Marketing Assets (4 Use Cases)](#11-step-7--generate-marketing-assets-4-use-cases)
12. [Reviewing the Deliverables + Real Costs](#12-reviewing-the-deliverables--real-costs)
13. [Step 8 — Build a Creative Tracker Spreadsheet](#13-step-8--build-a-creative-tracker-spreadsheet)
14. [Closing Takeaways](#14-closing-takeaways)
15. [Appendix — Caption Corrections](#appendix--caption-corrections)

---

## 1. What We're Building (Roadmap)

The video is structured as three phases:

1. **The project** — install Claude Code, create the folder/file structure, load business context.
2. **Higgsfield setup** — create an account and connect it to Claude as a custom connector.
3. **Asset generation** — start producing deliverables and evolving the system over time.

> 📏 **General Rule**
> Despite the name, Claude Code is not being used for coding here. It's being used because it works out of **directories and projects** — that's what enables persistent context that compounds over time.

> 🗣️ **Speaker Opinion**
> "You don't have to be technical at all… You just have to know what to ask for." The speaker explicitly assumes zero prior experience with these tools.

---

## 2. The Prerequisite: The Three Ps

Before any tooling, the speaker runs what he calls the **AI Monetization Readiness Assessment** — three things you must be able to state about the business:

| P | Question |
|---|---|
| **Pain** | What pain is your business trying to solve? |
| **Person** | Who specifically feels that pain? |
| **Promise** | How does your brand/product/service promise to solve that pain for that person? |

**PerkForm's Three Ps as used in the video:**

- **Person** — a busy, fitness-minded professional who relies on coffee, cares about protein, and frequently rushes through breakfast.
- **Pain** — mornings require too many separate products: coffee, a protein shake, and something portable.
- **Promise** — PerkForm gives them their coffee ritual and their protein in one grab-and-go can, making it easier to start energized and stay on track.

> 📏 **General Rule**
> This context is what stops marketing assets from reading as "generic AI slop." Assets have to have a purpose and intent behind them — and that intent comes from the Three Ps, not from the model.

> 💡 **Tip**
> The Three Ps are the minimum viable context dump. Everything downstream (website copy, ad angles, carousel hooks, UGC scripts) is derived from them.

---

## 3. Why Higgsfield, and Why Route It Through Claude

**Higgsfield** is an aggregator: many AI models under one subscription, plus a Marketing Studio.

> 🔧 **Tools — models available inside Higgsfield (as named in the video)**
> - **Seedance 2.5** — video model; early access available only on Higgsfield
> - **Kling** — video
> - **Sora** — video
> - **Gemini** — video
> - **Flux** — image
> - **GPT Image 2** — image (used for all the PerkForm logos and product shots)
> - **Nano Banana** / **Nano Banana Pro** — image
> - **Grok** — image
> - **Soul** — Higgsfield's own image model (appears later in the cost tracker)
> - **Marketing Studio** — templates that turn your assets into ad creatives and sizzle reels, powered by the models on the back end

**The case for putting Claude in front of it:**

| Claude Code gives you | What it does |
|---|---|
| **Project context** | Claude understands the business, avatar, positioning, and messaging on every request |
| **Skills** | Reusable recipes/workflows so an Instagram carousel or a UGC ad is always made the same way — skills are how you scale |
| **Brand guidelines** | Color scheme, logo system, typography, brand intent — followed automatically on every deliverable |

> 📏 **General Rule**
> Once Higgsfield is connected, Claude does the prompting and the UI navigation. You should never have to be inside the Higgsfield interface again — you ask Claude for things and it goes and does them.

---

## 4. Step 1 — Get Base Assets (Logo, Product Shots)

If you don't already have a logo or product photography:

1. Go to Higgsfield and create an account.
2. Go to **Image → Create an image**.
3. Choose a model (speaker's pick: **GPT Image 2**).
4. Prompt for a logo in plain language.

The speaker's live demo prompt (paraphrased): *"Hey, I've got a SaaS product called Kalanly [?] and I want a quick logo drafted up — it's an online calendar booking/appointment SaaS."* → hit **Generate**.

**What PerkForm ended up with:** four logo variants (text, light mode, dark mode, and the icon), three flavors (**vanilla latte**, **salted caramel**, **bold mocha**), and **11 product shots** covering both individual and studio setups.

> 🗣️ **Speaker Opinion**
> The generated logo — a coffee bean with a lightning bolt — was unprompted and "pretty clever." He only asked for "a logo."

> 💡 **Tip**
> Don't over-engineer at this stage. Get a few base assets generated so you feel comfortable with the tool, then fill in gaps later as you go.

---

## 5. Step 2 — Install Claude Code and Create the Project Folder

**Install:**

1. Search Google for **Claude Code desktop** and follow the link.
2. Install the version for your operating system.
3. Sign in with your subscription.

The interface looks much like Claude or ChatGPT on the web: a chat box, plus a **folder picker**.

**Create the project:**

1. Create a new, **empty folder** on your desktop (speaker's: `perkform marketing`, inside a parent folder called `Claude Code YouTube`).
2. In Claude Code, start a new chat. The indicator at the bottom reads **local** — meaning Claude is running against your own machine.
3. Click **Open folder** and navigate to the folder you just created.
4. Select it and click **Trust workspace**.

> ⚠️ **Caution**
> Trusting the workspace grants Claude the ability to read inside that folder, add files, edit them, and move them around. Know what you're pointing it at.

> 💡 **Tip — see what Claude is doing to your files**
> Click the **three dots** in the top right → **Files**. This gives you a live file-tree view of the project as Claude creates folders and assets.

---

## 6. Step 3 — Build CLAUDE.md and the Context Files

`CLAUDE.md` is the project's operating doc — instructions that tell any future session what this project is and what to load.

**The setup prompt (paraphrased from the video):**

> "My name is Nate. I run a business called PerkForm — an energy drink company where the drinks are coffee-flavored and also contain protein. I'm going to give you information about the business so you can save it as context for the project. Ultimately you're going to be like my marketing team: you'll help me generate ads, a website, UGC content. Understanding my business, my motivations, and my avatar will help a lot when you're creating this. I'm going to dump in a bunch of information, and I need you to create me a `CLAUDE.md` file as well as any other context files you think are relevant that you can reference later."

Then paste in the business context: the Three Ps, general business info, marketing angles, anything else relevant.

**What Claude generated (the resulting project structure):**

```
perkform marketing/
├── CLAUDE.md            # operating doc — what this project is, what to load
├── context/             # brand positioning (3 Ps), customer avatar,
│                        # product facts, voice & copy, message bank,
│                        # playbooks, landscape
├── assets/              # (empty at first) logos, product shots, guidelines
├── output/              # (empty at first) all deliverables land here
└── open questions
```

**What `CLAUDE.md` actually contained:** a short, plain description — *"This is the marketing project for PerkForm, a canned protein coffee brand. Nate Herk owns this business. Read these files before writing anything."* — followed by pointers to the context files.

> 💡 **Tip — treat CLAUDE.md as a living document**
> Expect to change it daily or weekly. When something matters, just say: *"Hey Claude, by the way, add that to the CLAUDE.md — this is important."*

> 📏 **General Rule**
> Separate the operating doc from the context. `CLAUDE.md` sets the scene and routes to files; the detailed positioning, avatar, and voice live in `context/` as individual Markdown files.

> 💡 **Tip**
> Don't be intimidated by the Claude Code output stream — it's just narrating what it's thinking, what it's doing, and which files it's creating.

---

## 7. Skills: Reusable Recipes (and the "grill me" Trick)

**Skills** are saved, reusable workflows — Markdown files containing a prompt/recipe — so that a given deliverable type is always produced the same way.

**The `grill me` skill:** its stated purpose is *to relentlessly interview the user about every aspect of a topic until you reach shared understanding.* It transfers what's in your head into the agent's context, digging with question after question until it's satisfied.

**How to install and use a skill:**

1. Download the skill (a `.md` file). The speaker hosts his free in a Skool community — **Classroom → All YouTube Resources**; link in the video description.
2. Drag the `.md` file directly into the Claude chat.
3. Say: *"This is a skill called `grill me`. Go ahead and install this inside of this project so I can use it."*
4. Then: *"Run the `grill me` skill on my product and my marketing so you understand how I think about marketing my product."*
5. Claude interviews you one question at a time and **saves the interview** as context for later.

> 💡 **Tip**
> `grill me` is the fix for "I don't know what context to give it." Instead of writing a context dump, let the agent extract it from you.

> 📏 **General Rule**
> Skills aren't only for content generation — they're useful for any repeatable workflow, including intake and discovery.

> 💡 **Tip — build skills *after* you like something**
> When a deliverable comes back the way you want it (a carousel style, an ad format), turn it into a skill: *"I loved carousel 2 — let's make a skill around that one so I can do that style again."* The inverse works too: *"I don't like carousel 3, never make them like that again."*

---

## 8. Step 4 — Load Assets Into the Project

Drag your real assets into the project's `assets/` folder from your file explorer:

- The 4 logo files
- The product shots folder (11 images)
- The **brand guidelines PDF** — containing color scheme, brand intent, logo system, typography

> 💡 **Tip**
> You don't have to move originals — copy them in instead if you'd rather keep your source files where they are.

**Troubleshooting moment from the video:** the `product shots` folder appeared broken in Claude's file panel — it rendered as an unreadable item rather than a folder. Rather than guess, the speaker asked Claude directly:

> *"Inside the assets folder in this project, I dragged in another folder called product shots, but it's appearing weird. Can you actually see all of the product shots inside that folder? There should be 11 of them."*

Claude read the files and confirmed all 11 JPGs, returning a full inventory. The issue was cosmetic — likely a display bug or a refresh delay in the file panel.

> 📏 **General Rule**
> When the UI confuses you, **ask Claude what it sees**. Verification through the agent beats guessing from the interface.

---

## 9. Step 5 — Connect Higgsfield to Claude (MCP Connector)

1. In your Higgsfield account, click **MCP and CLI** at the top.
2. The first entry listed is **Claude** — copy that URL.
3. In Claude, go to **Customize → Connectors → Add custom connector**.
4. Paste the URL, name it **Higgsfield**, and hit **Add**.
5. A prompt appears — click **Connect to Claude**.
6. You'll be taken to Higgsfield to sign in with the account you already created.
7. Grant permission so Higgsfield and Claude can talk to each other.
8. Confirmation shows you're connected.

Once connected, Claude can operate Higgsfield on your behalf: *"Hey Claude, make me an image"* or *"Hey Claude, go to the Marketing Studio"* — and it does it.

> 🔧 **Tool**
> **Higgsfield MCP connector** — the single integration point that turns Higgsfield's whole model catalog into something Claude can drive.

---

## 10. Step 6 — Build the Website (scroll-world)

> 🔧 **Tool**
> **scroll-world [?]** — a public GitHub repo by a creator the captions render as "Oso" [?]. It produces scroll-driven, 3D-interactive websites. Link was in the video description.

**How it's used:** copy the **GitHub repo URL** and paste it straight into the Claude chat. GitHub is just a place to store and share code; because the repo is public, you can use it directly.

**The build prompt (paraphrased):**

> "First I want to set up a website for our business PerkForm. Inside this project you already have our logo, brand guidelines, and product shots. Think carefully from a design perspective: how can we use those logos and assets together with the scroll-world GitHub repo I just linked, to create a super premium and professional but also interactive and fun website? Look at our Three Ps and our personas, and make sure the copy and the structure of the site appeal to our target person and show how we're solving their pain with our business promise."

**What Claude did:** read the brand guidelines PDF, reviewed the scroll-world repo, and checked what Higgsfield could actually host. It reported pulling the design system **straight from the guidelines PDF rather than inventing one**, and deliberately opened on the **pain, not the product**.

**The resulting site, scrolling top to bottom:**

| Section | What happens |
|---|---|
| Hero | *"Your morning shouldn't require two drinks."* — animated background |
| Merge scene | Coffee on the left, protein on the right; they merge as you scroll into a vanilla latte PerkForm |
| Copy shift | Text changes to *"One can and you're out the door."* |
| Time pressure | *"11 minutes before you leave"* — shower, find keys, answer one email, make breakfast, grab coffee, go |
| Nutrition | Placeholder — nutrition facts were never supplied to Claude |
| Flavors | Bold mocha (close-up with condensation and drips), vanilla latte (spinning), salted caramel — all **Seedance 2.5** videos generated by Higgsfield, wired so clips scrub forward as you scroll |

> 🗣️ **Speaker Opinion**
> "This is more unique than a typical AI vibe-coded site on the first pass… for this being one prompt, not too bad." He rates it as on-brand and not obviously AI-generated.

> 📏 **General Rule**
> Assume nothing is perfect on the first prompt. Expect to come back with feedback.

> ⚠️ **Caution — the site is not live**
> The URL shown was `localhost:8931`. Localhost means the app is running only on your own computer — copy that URL to another machine and nobody sees anything. To publish, connect the codebase to **GitHub**, push, then deploy to **Vercel**. The speaker estimates ~5 minutes and points to a separate tutorial of his.

---

## 11. Step 7 — Generate Marketing Assets (4 Use Cases)

All four were fired off into the **same chat** and run in parallel.

### Use case 1 — BOGO ad creatives

Prompt (paraphrased): a big **BOGO** sale is coming (buy one box, get one box free), available in mixed-flavor boxes or single flavors. Generate a large batch of varied ad creatives — different copy, different images — so we can test broadly. Use Higgsfield with our brand context. **Report the cost at the end**, and save everything to a folder in `output/` labeled for the summer BOGO offer.

### Use case 2 — Sizzle reel

Prompt (paraphrased): use **Higgsfield Marketing Studio** specifically, because it produces fast-paced, energetic edits with music. Make a viral-style sizzle reel for the PerkForm product suitable for the website and socials.

### Use case 3 — Instagram carousels

Prompt (paraphrased): we're launching PerkForm's Instagram presence and need a few carousels aimed at our target audience — why we created the product, who it's for, what problems it solves, the flavors. Get creative and tell me which would make good pinned posts. Save to the correct folder and report the cost.

### Use case 4 — UGC video ads

Prompt (paraphrased): create several **vertical** UGC-style video ads for social — organic-feeling videos of people holding the product, reviewing it, saying what they like. They should match our target person and speak to the pain we solve. Vary the treatment — some more edited, some raw takes. **Seedance 2.5** is fine, or try other models.

> 📏 **General Rule — the four-part prompt pattern**
> Every prompt in this section states: (1) the **motivation**, (2) the **end goal**, (3) **where to save the output**, and (4) **report the cost**. Claude infers the rest from project context.

> 💡 **Tip**
> Explicitly asking *"tell me how much this cost"* on every generation is what makes the later analytics tracker possible.

> 🗣️ **Speaker Opinion**
> "I'm basically just talking to this thing like I would a human."

---

## 12. Reviewing the Deliverables + Real Costs

Everything landed in `output/`, subdivided into `ads/`, `social/`, `ugc/`, `video/`, and `web/`.

### Cost summary

| Deliverable | What was produced | Cost |
|---|---|---|
| BOGO ad creatives | **18** static ad images | **$3.43** |
| Sizzle reel | 1 vertical + 1 landscape, with music and edits | **$17.55** |
| Instagram carousels | **5** carousels, ~7–8 slides each | **$9.56** |
| UGC video ads | 4 creator characters, storyboards, QA pass, videos | Most expensive of the four (figure not stated) |

### Ad creatives — `output/ads/summer bogo/`

Contains `images/`, `V1 backup/`, `ad copy`, and `run notes`.

Sample headlines produced: *"Two drinks, one can"* · *"Buy one box, get one free — mixed flavors or all-in-one"* · *"Breakfast optional"* · *"Stock the whole summer"* · *"Can't pick? Don't. Mix box."* · *"Two for one"* · *"Gym bag to desk — the shaker stays clean"* · *"Same habit, more return"* · *"Cold case, handled"* · *"Bold mocha, doubled."*

Consistent brand fonts and color scheme throughout, consistent product renders across all 18, plus some **blank versions with no copy** so you can add your own later.

> 💡 **Tip — separate copy from art**
> Because all 18 are saved, a future promotion doesn't require regenerating images. Swap the CTA or the copy onto the existing graphics — or take one winning line ("Same habit, more return") and apply it across all 18.

> 💡 **Tip — bring your own subject-matter expertise**
> "I literally just said, 'Hey, create me some ads for BOGO.'" If you actually know what makes a good creative and good ad copy, put that into the prompt and the output improves substantially.

### Sizzle reel — `output/video/sizzle reel/`

> 🗣️ **Speaker Opinion**
> "Those are insane… it has all of these different scenes, all of the music, the elements, the copy. This is so good." He notes one flaw: **the logo wasn't exactly correct**. On cost: video is obviously more expensive than images, but $17.55 versus hiring a video editor for the same output is not a close comparison.

> 🗣️ **Speaker Opinion — the honest caveat on Higgsfield**
> "It's not the cheapest tool out there for all of these different models. But it has everything aggregated into one spot," plus extras like the Marketing Studio.

### Instagram carousels — 5 carousels

Sample copy: *"Your morning shouldn't require two drinks"* · *"Coffee happens because coffee always happens. Protein is the maybe."* · *"Two purchases, two things to carry — so we put them in one can."* · *"Same habit, one less stop."* · *"Three flavors of coffee."* · *"Coffee that pulls its weight."* Branding and can renders stayed consistent across all of them.

> 📏 **General Rule**
> "Volume negates luck." More creatives → more chances to hit. Once assets are live you have performance data, and data lets you iterate.

> 💡 **Tip — close the loop**
> Connect Claude to your actual performance data and have it review weekly: what it made, what performed, then make more of what worked. That's a self-reinforcing cycle.

### UGC ads — `output/ugc/ugc ads 08-20/`

Subfolders: `boards/`, `creators/`, `QA/`, `video/`. The pipeline Claude built itself:

1. **Creators** — generated **4 consistent character images** (reusable as a recurring brand avatar).
2. **Boards** — storyboards per ad (selfie-style framing, coffee cup and protein shake, product open, close-up, drinking) so video generation is *controlled by a planned story* rather than improvised.
3. **Video** — generated from characters + boards.
4. **QA** — a quality-assurance pass where Claude screenshotted and reviewed its own videos. One clip was **rejected** with the note "back panel," apparently a text or logo defect, before Claude reported the job finished.

Sample script line from a finished ad: *"Coffee in one hand, protein shake in the other. Both going cold on the counter. That's the morning this replaces. Protein coffee, sealed and cold. No blender. Coffee that pulls its weight."*

> 🗣️ **Speaker Opinion — the honest critique**
> "You can kind of tell it's an AI avatar still. But the thing that I don't like about these is that they are still very ad-like — they're very salesy. You can tell it's not completely organic." His proposed fix: have Claude analyze existing UGC content, or write scripts *you* approve first, then feed the approved scripts plus storyboards into video generation.

> 🗣️ **Speaker Opinion**
> The rapid-cut editing (2-second clip, 1-second clip, 2-second clip) is engaging, but wasn't required — a 15-second raw selfie-style take would also work. Claude chose to cut them up.

> ⚠️ **Caution**
> UGC generations were the slowest and most expensive because each one required images *and* storyboards *and* extra QA passes before the video itself.

---

## 13. Step 8 — Build a Creative Tracker Spreadsheet

**Why:** `output/` gets messy as volume grows, and you want a better surface for reviewing what you've made.

**The prompt (paraphrased):** *"We just went through four rounds of generations — BOGO ad creatives, sizzle reel, carousels, and UGC content. Create me an Excel sheet showing the date, the type of generation, the outputs, and the core angle we were using — because every time we create content we have some angle, and later I want to analyze which angles and which copy worked best. Give me an Excel sheet with analytics we can grow over time and use to make better decisions."*

**Runtime:** roughly **8 minutes**. Output landed in `output/analytics/` as a **creative tracker**.

**Tabs in the workbook:**

| Tab | Contents |
|---|---|
| Overview | Explains what each tab holds |
| Generation log | ID, date, generation type, campaign, channel, primary angle, angles covered, deliverables, gens built, tool and model, credits, dollar cost, status |
| Creative assets | Each image and video with its supporting copy |
| Angle performance | Where analytics data gets added over time |
| Copy bank | Reusable copy lines |
| Cost summary | Spend rollup |

Models logged in the generation log: **Nano Banana Pro**, **Marketing Studio**, **GPT Image 2**, **Soul**, and **Seedance 2.5**.

> 🗣️ **Speaker Opinion**
> "It even made this Excel sheet using our brand guidelines — the color scheme, the bold lime green, the tabs down at the bottom. Normally when I make Excel sheets with Claude it does not do this." He found it funny and unprompted that the design system leaked into the spreadsheet.

> 💡 **Tip — what to automate next**
> Build automations that sweep and update the sheet continuously; drop ideas into the sheet and tell Claude *"check the sheet and process anything that's new"*; run weekly automated research that scrapes competitor creatives and files ideas into the sheet.

---

## 14. Closing Takeaways

Recap of the build: set up the project → set up the brand context → connect Higgsfield → generate assets → track them. The reason for connecting Higgsfield *to Claude* rather than using it standalone remains the throughline: **business context, skills, and brand guidelines**.

> ⚠️ **Caution — realistic expectations**
> "You can't just expect to throw one prompt out there and then go viral and make a million dollars." What was demonstrated is how far you get with a few prompts *before* you actually dig in with research and your own taste.

> 🔧 **Further resource**
> The speaker's free **six-hour Claude Code course for non-coders**, linked from the video.

---

## Appendix — Caption Corrections

Auto-generated captions introduced consistent misspellings. Corrections applied throughout this document:

| Caption text | Corrected to | Notes |
|---|---|---|
| Higsfield, Hicksfield, Higfield | **Higgsfield** | The AI model aggregator platform |
| Cloud Code, cloud code | **Claude Code** | |
| claw.md, cloudmd, closet MD, cloud.MD | **CLAUDE.md** | The project operating doc |
| Cance 2.5, C dance 2.5, Sea Dance 2.5 | **Seedance 2.5** | ByteDance video model |
| GBT image 2, GBT image 2.0 | **GPT Image 2** [?] | Image model; exact product naming uncertain |
| Cling | **Kling** | Video model |
| Grock | **Grok** | |
| Soul GBT image | **Soul, GPT Image** | "Soul" is Higgsfield's own image model — likely two models listed, not one |
| VCEL | **Vercel** | Hosting platform |
| Perkformm, Perk Form | **PerkForm** | The fictional demo brand |
| UDC ad | **UGC ad** | User-generated content |
| Jim Bro brand | **gym bro brand** | |
| free school community | **Skool community** | Course/community platform |
| Jen's build | **gens built** | Number of generations built, a spreadsheet column |
| localhost 8931 | **`localhost:8931`** | |
| costed us $343 | **$3.43** | Confirmed by his later "not as cheap as three bucks" |
| This one was like 1755 | **$17.55** | Sizzle reel cost, stated in credits/dollars |
| on 820 | **August 20** | UGC folder date stamp |
| Scroll World | **scroll-world** [?] | Exact repo name/casing not visible on screen |
| Oso | **[?]** | scroll-world repo author; name uncertain from audio |
| Kalanly | **[?]** | Throwaway demo SaaS name; spelling uncertain |
| Nate Herk | **Nate Herk** | Retained as spoken; the speaker/business owner |

*Items marked **[?]** are unverified — the caption was ambiguous and the correct spelling could not be confirmed from context.*
