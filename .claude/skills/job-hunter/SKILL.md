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
3. **Role preferences** — **HARD FILTER**: only surface roles that meet at least one of:
   - **Mid-level seniority** (typically 2–5 years experience; titles like "Mid-level Engineer", "Engineer II", "Software Engineer" without Senior/Staff/Principal prefix, or explicitly tagged mid-level). Exclude Junior/Entry-level and Senior/Staff/Principal/Lead roles.
   - **AI Builder–related** (titles or descriptions containing: "AI Builder", "AI Engineer", "Agentic Engineer", "Applied AI", "AI Solutions Engineer", "Forward Deployed AI Engineer", "LLM Engineer", "GenAI Engineer", or roles whose core responsibility is building with LLMs/agents/RAG/prompt engineering).
   
   A role qualifies if it matches **either** criterion. Drop everything else before scoring.
4. **Location / remote preferences** — remote or 25miles radius of Burbank, CA.
5. **Stretch tolerance** — the user may want to include roles that are a stretch (e.g., "apply even if it's a borderline match"). Default: include stretch roles but mark them clearly.

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

**Apply the hard filter immediately**: discard any role that is NOT mid-level AND NOT AI-builder-related (see "Role preferences" in Inputs). Don't carry junior, senior, or non-AI roles into scoring — they're noise.

If the careers page is a JavaScript-heavy app (common with Greenhouse, Lever, Ashby embeds), the visible HTML may not list roles. In that case:
- Look for the underlying job board URL (often linked from the page)
- Try the ATS directly: `boards.greenhouse.io/{slug}`, `jobs.lever.co/{slug}`, `jobs.ashbyhq.com/{slug}`
- If still blocked, note "careers page requires JS — manual review needed" and move on

### Step 3: Score each role against the resume
For every open role found, score on a 1-5 scale:

- **5 — Strong fit**: Role title and requirements clearly map to user's experience. They should apply.
- **4 — Good fit**: Most requirements met; minor gaps that are easily explained in a cover letter.
- **3 — Stretch fit**: User has adjacent experience; would need to make a case. Worth applying if user is open to stretches.
- **2 — Weak fit**: Missing major requirements (e.g., specific years of experience, missing core stack).
- **1 — Not a fit**: Role is in a different discipline. Skip.

Include the rationale in one line per role.

By default, show roles scoring 3 and above. Show 4+ if the user wants a tighter list.

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

- One row per role that scored 3+, with a **Status** column hcho edits over time. Status legend: `To apply` (default) / `Applied` / `Interviewing` / `Offer` / `Rejected` / `Passed` (declined).
- Columns: `Status | Company | Role | Location | Fit | Apply | Notes`. Group remote-eligible vs onsite/relocation, sorted by fit within each group (mirrors the shortlist).
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
- **Enforce the seniority/AI-builder filter.** Senior/Staff/Principal roles and Junior/Entry-level roles should be excluded unless they explicitly fall under the AI Builder umbrella. When in doubt about seniority, check years-of-experience requirements: 2–5 yrs = mid-level (keep), 0–1 yrs = junior (drop), 6+ yrs = senior (drop unless AI-builder-titled).
- **Note when a company has no relevant openings.** It's useful for the user to know "Company X had nothing mid-level or AI-builder" rather than silently omitting them.

## Memory

This skill keeps a free-form `MEMORY.md` in its own folder.

- **Start of every run:** read `MEMORY.md` and apply anything relevant before doing the work.
- **Writing is feedback-gated:** append only when hcho explicitly says to remember something for this skill (a "remember this", a correction, or a stated preference). Do not log routine runs.
- **How to append:** add a dated bullet under `## Notes` in the form `- [YYYY-MM-DD] <note>`, using the real date from `date +%Y-%m-%d`.
- **Cap:** keep `MEMORY.md` under 100 lines. When it nears the cap, tell hcho and ask which entries to prune. Never delete entries silently.