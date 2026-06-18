---
name: job-hunter
description: Scan a curated list of company career pages and surface roles the user is qualified for, ranked by fit against their resume. Use this skill whenever the user asks to "search for jobs", "find roles", "look at careers pages", "see who's hiring", or mentions specific companies they want to apply to. Also trigger when the user provides a list of companies (AI-native, startups, etc.) and wants to know which ones have open positions matching their background. Produces a ranked shortlist with role title, link, fit score, and a one-line rationale.
---

# Job Hunter

A skill for systematically searching a target list of companies for roles the user is qualified for, given their resume and stated preferences.

## When to use this skill

Trigger this skill when the user wants to:
- Search a specific list of company career pages for open roles
- Find roles matching their resume across multiple companies
- Get a ranked shortlist of "apply now" candidates with fit rationale
- Filter a broad company list (e.g., "10 AI startups") down to ones actively hiring for their skillset

## Inputs needed

Before searching, confirm:
1. **Resume** — should be in context already (uploaded file or pasted). If not, ask the user to provide it.
2. **Target companies** — a list. May come as: a typed list, an uploaded image/screenshot, a CSV, or a category ("5 AI-native companies"). If only a category is given, ask the user to specify names OR confirm they want you to propose the list.
3. **Role preferences** — **HARD FILTER**: surface only **builder roles** — the core responsibility is building with LLMs / agents / RAG / prompt engineering, or shipping production AI product features at an AI-native company. Qualifying titles include: "AI Engineer", "AI Builder", "Applied AI Engineer", "Agentic Engineer", "LLM Engineer", "GenAI Engineer", "AI Product Engineer", "Forward Deployed (AI) Engineer", "(AI) Solutions Engineer", "Member of Technical Staff", and "Software / Full-Stack Engineer" roles whose core work is shipping AI product features.
   - **Seniority**: include **Mid-level and Senior individual-contributor** builder roles. Drop the prior mid-level-only cap — 10 years of validation experience makes Senior IC roles a strength, and startups do not ladder cleanly.
   - **Exclude**: Staff / Principal / Lead roles that require team leadership or deep ML research; roles requiring 6+ years of *specialized* AI/ML or a research/PhD background (genuine stretch); and pure non-AI roles. Junior/entry roles only if AI-builder-titled and they clear the pay bar.

   A role qualifies if it is a builder role by the above. Drop everything else before scoring.
4. **Location** — **HARD FILTER**: keep only roles that are **remote (US-eligible)** OR **onsite/hybrid within 25 miles of Burbank, CA** (greater LA — e.g. Burbank, Glendale, Pasadena, Hollywood, Studio City, North Hollywood, Universal City, Sherman Oaks, Downtown LA). Drop every other onsite/relocation role, even strong fits. hcho is not relocating.
5. **Stretch tolerance** — the user may want to include roles that are a stretch (e.g., "apply even if it's a borderline match"). Borderline roles that still score Fit 4 are kept and marked; Fit 3 and below are dropped (see Step 3).

If any of these are missing, ask in a single batched question before starting the search.

## Workflow

### Step 1: Build the target list
Compile the companies into a structured list. For each, identify the canonical careers page URL. Common patterns:
- `{company}.com/careers`
- `{company}.com/jobs`
- `jobs.lever.co/{company}`
- `boards.greenhouse.io/{company}`
- `{company}.com/about/careers`

If a careers URL is unknown, run a web search: `"{company} careers page"` and pick the official domain (not LinkedIn/Indeed aggregators — go to the source).

### Step 2: Fetch and parse each careers page
For each company, fetch the careers page. Look for:
- Role titles
- Location / remote status
- Team / department
- Direct apply link

**Apply the hard filters immediately**: discard any role that is not a **builder role** (see "Role preferences"), AND discard any role that is **not remote (US-eligible) and not within 25 miles of Burbank, CA** (see "Location"). Don't carry non-AI roles, Staff/Principal/Lead, research/PhD-gated roles, or out-of-area onsite roles into scoring — they're noise. Mid-level and Senior IC builder roles both qualify.

If the careers page is a JavaScript-heavy app (common with Greenhouse, Lever, Ashby embeds), the visible HTML may not list roles. In that case:
- Look for the underlying job board URL (often linked from the page)
- Try the ATS directly: `boards.greenhouse.io/{slug}`, `jobs.lever.co/{slug}`, `jobs.ashbyhq.com/{slug}`
- If still blocked, note "careers page requires JS — manual review needed" and move on

### Step 3: Score each role against the resume
**Anchor scoring on demonstrated shipping, not years.** A shipped portfolio (CreativeBridge on TestFlight; Agentic RAG: FastAPI / pgvector / raw OpenAI SDK / RLS / LangSmith) satisfies "builds and ships with LLMs / RAG / agents." Treat the 10-year validation background as **production-engineering rigor** — a plus for roles that emphasize shipping production-grade systems, not a QA pigeonhole. Prefer roles with **take-home or pair-build** interviews over algorithmic-gauntlet screens.

For every open role found, score on a 1-5 scale:

- **5 — Strong fit**: Builder role; the portfolio directly demonstrates the core requirement. They should apply.
- **4 — Good fit**: Asks for ~2-4 yrs building with LLMs / RAG / agents; the projects cover it with minor gaps explained in a cover letter.
- **3 — Stretch fit**: Adjacent experience; would need to make a case. Below the keep-threshold — score it but do not list or save.
- **2 — Weak fit**: Requires deep ML research, 6+ yrs specialized AI, or a PhD; or missing the core stack.
- **1 — Not a fit**: Different discipline (including standalone QA/SDET, under the builder-only strategy). Skip.

Include the rationale in one line per role.

**Keep only roles scoring 4 or 5.** Drop Fit 3 (stretch) and below entirely — they are not shown in the shortlist or saved to the tracking note.

### Step 4: Present the shortlist
Output as a table grouped by company, sorted by fit score within each company. Include:

| Company | Role | Location | Fit | Why it fits | Apply link |
|---------|------|----------|-----|-------------|------------|

After the table, give a brief summary: "Found N roles across M companies. Top picks: [3 highest-fit roles]."

Optionally offer follow-ups:
- "Want me to draft a cover letter for any of these?"
- "Want to expand the search to similar companies?"
- "Any of these you want me to dig deeper on?"

### Step 5: Save the scan as a dated tracking note (always)
After presenting, persist the scan to `projects/job-search/scans/<YYYY-MM-DD>.md` (create the `scans/` folder if it does not exist; get the real date from `date +%Y-%m-%d`). This is the durable record hcho uses to track applications, so it always gets written, not just on request.

- One row per role that scored **4+**, with a **Status** column hcho edits over time. Status legend: `To apply` (default) / `Applied` / `Interviewing` / `Offer` / `Rejected` / `Passed` (declined).
- Columns: `Status | Company | Role | Location | Fit | Apply | Notes`. Group **remote-eligible vs Burbank-local (within 25 mi)**, sorted by fit within each group (mirrors the shortlist).
- Also record the "no openings / unreachable" companies and the list of companies skipped this run, so the note is a complete record of what was and was not covered.
- **Never overwrite an existing same-day file** — it may already hold hcho's Status edits. If `<YYYY-MM-DD>.md` exists, write `<YYYY-MM-DD>-2.md` (incrementing) instead, and tell hcho.

## Reference files

- `references/scoring-rubric.md` — Detailed scoring criteria with examples, for borderline cases.
- `references/company-list-template.md` — Template for organizing target companies by category.
- `references/ats-patterns.md` — Common ATS URL patterns and how to find them.

Read these only when you need to resolve ambiguity (e.g., a borderline fit score, or a company whose careers page you can't find).

## Output location

- **Target list (input):** `.claude/skills/job-hunter/assets/companies.yaml`.
- **Scan tracking notes (output):** `projects/job-search/scans/<YYYY-MM-DD>.md` — one dated note per scan (see Step 5), with a Status column hcho updates to track applied/passed. This is the canonical record of every scan; do not overwrite prior days.

## Important guidance

- **Be honest about fit.** Don't inflate scores to make the list look productive. A short list of real matches is more valuable than a long list of stretches.
- **Don't fabricate roles.** If a company's careers page is unreachable, say so — never invent a role or URL.
- **Verify links.** Every apply link in the output should be a real URL you actually fetched, not a guess.
- **Respect the resume.** If the resume emphasizes specific domains (e.g., AI engineering, edtech), weight those heavily. Don't surface unrelated roles just because the company is on the list.
- **Enforce the builder filter.** Keep Mid-level and Senior IC builder roles. Drop Staff/Principal/Lead (team-leadership or deep-ML-research) and roles gated on 6+ yrs specialized AI/ML or a PhD. Non-AI roles (including standalone QA/SDET) are out under the builder-only strategy. When in doubt, check whether the core responsibility is *building with LLMs/agents/RAG* — if yes, keep regardless of the Senior label.
- **Enforce the location + fit gates.** Keep only roles that are remote (US-eligible) or within 25 miles of Burbank, CA, and only Fit 4-5. Drop onsite-elsewhere roles and anything Fit 3 or below before it reaches the shortlist or the tracking note. hcho is not relocating.
- **Note when a company has no relevant openings.** It's useful for the user to know "Company X had no builder roles in range" rather than silently omitting them.

## Memory

This skill keeps a free-form `MEMORY.md` in its own folder.

- **Start of every run:** read `MEMORY.md` and apply anything relevant before doing the work.
- **Writing is feedback-gated:** append only when hcho explicitly says to remember something for this skill (a "remember this", a correction, or a stated preference). Do not log routine runs.
- **How to append:** add a dated bullet under `## Notes` in the form `- [YYYY-MM-DD] <note>`, using the real date from `date +%Y-%m-%d`.
- **Cap:** keep `MEMORY.md` under 100 lines. When it nears the cap, tell hcho and ask which entries to prune. Never delete entries silently.
