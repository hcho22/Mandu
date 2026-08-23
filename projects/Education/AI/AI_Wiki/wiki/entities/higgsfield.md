---
type: entity
tags: [tool, image, video, generative-media, marketing, mcp]
status: seed
source-count: 1
last-updated: 2026-08-21
---

# Higgsfield

A multi-model **image and video generation aggregator**: many third-party models under one subscription, plus a template-driven **Marketing Studio** that turns your assets into ad creatives and sizzle reels.

Appears in [[one-person-marketing-team]] as the generation backend driven by [[claude-code]] over an MCP connector.

## Models named in that source

Video: **Seedance 2.5** (early access exclusive to the platform at the time), **Kling**, **Sora**, **Gemini**.
Image: **Flux**, **GPT Image 2**, **Nano Banana** and **Nano Banana Pro**, **Grok**, and **Soul**, which is Higgsfield's own image model.

Model naming in the raw source comes from auto-generated captions and several entries are flagged uncertain there; see the provenance section of [[one-person-marketing-team]].

## The MCP connector

The integration is the reason it matters to this wiki.
Higgsfield publishes an MCP endpoint under "MCP and CLI"; you add it in Claude as a custom connector and authorize it.
After that the agent does the prompting and the UI navigation, and the source's claim is that **you should never need to open the Higgsfield interface again**.

That is the pattern generalized in [[own-the-context-layer]]: a generation catalog behind an MCP endpoint becomes a tool the agent drives, and the durable asset moves up to the project holding your context and brand rules.

## Cost, from the one run recorded

18 static ad images for $3.43, five Instagram carousels for $9.56, one sizzle reel in two formats for $17.55.
The UGC video batch was the most expensive and its cost was never stated.
See [[make-the-agent-report-its-cost]].

## The honest caveat

From the source's own author: **"It's not the cheapest tool out there for all of these different models."**
The argument for it is aggregation - one account and one bill across a large catalog - plus the Marketing Studio templates, not per-model price.

## Notes

Single-source, and that source is a beginner-facing tutorial with a fictional brand, so treat everything here as descriptive rather than evaluated.
Nothing in the wiki independently corroborates the model list, the pricing, or the connector's reliability.
Related tools named elsewhere for the same job: **Kie AI**, **Google Nano Banana**, **HeyGen**, and **Seedance** in [[building-marketing-agents]].
