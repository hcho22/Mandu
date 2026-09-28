---
name: job-hunter
description: Search employer career pages, job aggregators such as Indeed, and freelance marketplaces such as Upwork for full-time roles and paid contracts that match the user's current skills. Rank verified opportunities against the resume and engagement-quality gates. Use whenever the user asks to search for jobs, contracts, freelance work, gigs, clients, or companies hiring.
---

# Job Hunter

A skill for systematically searching direct employers, broad job sites, and freelance marketplaces for work the user is qualified to perform.

## When to use this skill

Trigger this skill when the user wants to:
- Search a specific list of company career pages for open roles
- Search broad job sites such as Indeed, Wellfound, Built In, or YC Jobs
- Search freelance marketplaces such as Upwork or Contra for paid project work
- Find roles matching their resume across multiple companies
- Get a ranked shortlist of "apply now" roles and "propose now" contracts with fit rationale
- Filter a broad company list (e.g., "10 AI startups") down to ones actively hiring for their skillset

## Inputs needed

Before searching, confirm:
1. **Resume** — should be in context already (uploaded file or pasted). If not, ask the user to provide it.
2. **Search scope** — a company list is optional. When the user does not specify sources, run the combined source mix in `assets/search-sources.yaml`: direct employer/ATS pages, full-time aggregators, startup job boards, and freelance marketplaces. If the user names a company, site, engagement type, or category, add that source without narrowing away the default mix unless they explicitly request a narrow scan.
3. **Role preferences** — **HARD FILTER**: a role must fit at least one of the three lanes below. Judge the responsibilities, not the title.
   - **Software quality and systems validation:** SDET; Software QA Automation Engineer; Systems Validation Engineer; Verification and Validation Engineer; Product Quality Engineer; Test Infrastructure Engineer; API or Backend Test Automation Engineer; Mobile QA Automation Engineer; iOS Test Engineer; Release Quality Engineer. Prefer automation, APIs, mobile, connected devices, developer tools, or AI products. Exclude manual-only QA and pure hardware-only validation with no meaningful software or automation ownership.
   - **AI quality and evaluation:** AI Quality Engineer; AI Test Engineer; AI/ML Validation Engineer; **Machine Learning Engineer, Evals**; **Machine Learning Evaluation Engineer**; **ML Quality Engineer**; **Model Quality Engineer**; **ML Validation Engineer**; **LLM Evaluation Engineer**; Model Evaluation Engineer; AI Reliability Engineer; ML Systems QA Engineer; Evaluation Platform Engineer; Responsible AI Test Engineer; **Data Scientist, Model Evaluation**; **Data Scientist, Trust and Safety**; **Data Scientist, AI Quality**; **Data Scientist, AI Reliability**; and AI red-team roles centered on systematic product evaluation rather than security research. For Data Scientist, Trust and Safety, keep roles centered on ML models, anomaly or abuse detection, model performance, evaluation, or reliability; exclude policy operations, conventional product analytics, and reporting-led roles. Hardware-validation tenure demonstrates rigor, test design, and failure analysis, but does not substitute for a required multi-year record of shipping software test infrastructure or evaluation systems.
   - **AI product, integration, and technical delivery:** AI Engineer; AI Builder; Applied AI Engineer; **Applied Machine Learning Engineer**; **AI/ML Engineer**; Agentic Engineer; LLM Engineer; GenAI Engineer; AI Product Engineer; **Data Scientist, Applied ML**; Integration Engineer; Implementation Engineer; Customer Engineer; hands-on Technical Solutions Engineer; Developer Support Engineer; Technical Support Engineer for APIs, developer tools, or AI platforms; Product Engineer for internal tools or workflow automation; Forward Deployed AI Engineer; and Software / Full-Stack Engineer roles whose core work is shipping AI product features. Applied-ML and data-science titles qualify only when the work centers on model building or evaluation, NLP/CV, LLMs/RAG/agents, or productionizing a supported ML capability.
   - **Seniority:** include **Mid-level and Senior individual-contributor** roles whose stated experience and core competencies are honestly clearable. Ten years of validation experience supports senior quality/validation roles, but does not become ten years of software, AI/ML, SDK, infrastructure, or enterprise-delivery experience.
   - **Exclude:** Staff / Principal / Lead roles requiring leadership or missing specialized depth; research/PhD-gated roles; manual-only QA or annotation; generic customer support; quota-dominated sales engineering; pure hardware-only validation; frontend-specialist, SDK/library, DevOps/SRE, or MLOps-platform roles when that unsupported specialty is the role's spine. For data science and machine learning, exclude roles whose spine is product/growth analytics, business intelligence, causal-inference or Bayesian leadership, recommendations/ranking/pricing/forecasting, core model training or post-training, distributed GPU training, inference optimization, CUDA, feature-store/platform ownership, or another advanced specialty not demonstrated by the resume.

   Preserve qualified AI-builder roles while broadening beyond them. A role qualifies if it fits one lane and clears the location, compensation, seniority, and evidence gates below.
4. **Location** — **HARD FILTER**: keep only roles that are **remote (US-eligible)** OR **onsite/hybrid within 25 miles of Burbank, CA** (greater LA — e.g. Burbank, Glendale, Pasadena, Hollywood, Studio City, North Hollywood, Universal City, Sherman Oaks, Downtown LA). Drop every other onsite/relocation role, even strong fits. hcho is not relocating.
5. **Stretch tolerance** — the user may want to include roles that are a stretch (e.g., "apply even if it's a borderline match"). Borderline roles that still score Fit 4 are kept and marked; Fit 3 and below are dropped (see Step 3).
6. **Opportunity-specific economics:**
   - **Full-time roles:** keep the standing compensation gate: a disclosed band should top at approximately **$150K or more**. If compensation is undisclosed, a substantive Fit 4–5 may be shown only in a clearly separated `Compensation unverified` section and does not count as qualified.
   - **Freelance contracts:** do not apply the annual-salary gate. Evaluate the stated hourly rate or fixed-price scope instead. Exclude obviously uneconomic scopes, such as a multi-week production application for a token fixed price, unless the listing clearly describes a small bounded deliverable. Keep rate-undisclosed contracts only when the scope and client signals are credible, and mark `Verify rate`.

If any of these are missing, ask in a single batched question before starting the search.

## Workflow

### Step 1: Build the source plan

Start from `assets/search-sources.yaml` and the curated companies in `assets/companies.yaml`. A normal weekly scan covers three source classes:

1. **Direct employers and ATS boards** — the curated company list and newly discovered companies.
2. **Full-time discovery sites** — Indeed first, then the enabled startup and technology job boards.
3. **Freelance marketplaces** — Upwork first, then other enabled marketplaces when accessible.

For each discovered employer, identify the canonical careers page URL. Common patterns:
- `{company}.com/careers`
- `{company}.com/jobs`
- `jobs.lever.co/{company}`
- `boards.greenhouse.io/{company}`
- `{company}.com/about/careers`

Use Indeed and other aggregators for discovery. When an employer or ATS version exists, verify the role there and use the direct apply link. If only an exact aggregator listing is readable and current, keep it with `Source-only — verify before applying`; never silently convert a search snippet into a verified opening.

### Step 2: Fetch and parse each source

For employer pages and full-time aggregators, look for:
- Role titles
- Location / remote status
- Team / department
- Direct apply link
- Posted or updated date
- Compensation when disclosed

**Apply the hard filters immediately**: discard any role that fits none of the three lanes (see "Role preferences"), AND discard any role that is **not remote (US-eligible) and not within 25 miles of Burbank, CA** (see "Location"). Don't carry manual-only QA, annotation, generic support, quota-dominated sales, Staff/Principal/Lead, research/PhD-gated, unsupported-specialty, or out-of-area onsite roles into scoring. Mid-level and Senior IC roles may qualify in every lane when their actual requirements are honestly clearable.

If the careers page is a JavaScript-heavy app (common with Greenhouse, Lever, Ashby embeds), the visible HTML may not list roles. In that case:
- Look for the underlying job board URL (often linked from the page)
- Try the ATS directly: `boards.greenhouse.io/{slug}`, `jobs.lever.co/{slug}`, `jobs.ashbyhq.com/{slug}`
- If still blocked, note "careers page requires JS — manual review needed" and move on

For Indeed and other aggregators:

- search each lane using responsibility and stack terms, not just titles;
- de-duplicate the same role across sources by employer, title, location, and requisition ID;
- prefer the employer/ATS description and apply link when available;
- record the aggregator as the discovery source; and
- treat stale snippets, missing exact pages, or contradictory location data as unverified rather than live.

For Upwork and other freelance marketplaces, capture:

- exact job URL, posting date, location eligibility, hourly/fixed-price terms, expected duration, and weekly hours;
- deliverables and the actual technical spine;
- proposal count, client spend, hire rate, payment verification, rating, and last activity when publicly available; and
- whether the client wants an individual freelancer or an agency/team.

Do not bypass site protections. Use public indexed pages or an available signed-in browser session. If native search is blocked, say which evidence is indexed versus directly verified.

### Step 3: Score each role against the resume
Anchor scoring on the evidence relevant to the lane. The validation career supports test strategy, automation, defect isolation, systems thinking, and senior quality ownership. The Omdena and independent portfolio work supports current Python, SQL, PyTorch/TensorFlow/scikit-learn, model training and evaluation, LLM fine-tuning, CV/NLP, RAG/agents, Docker, APIs, observability, and application-level deployment. Do not convert hardware-validation tenure into unearned software, AI/ML, test-infrastructure, SDK, SRE, or enterprise-delivery tenure, and do not describe project-scale deployment as employer-scale MLOps or distributed-ML tenure. Prefer roles with take-home, debugging, system-design, experiment-design, or pair-build interviews over algorithmic-gauntlet screens.

For the targeted ML/data-science expansion, a title alone never earns Fit 4. Keep only roles whose central work is supported by the resume: ML/LLM evaluation, model quality or reliability, applied NLP/CV, RAG/agent systems, failure analysis, validation, or end-to-end applied ML at modest production scale. A role drops to Fit 3 or below when its central bar is conventional product analytics, causal inference, recommendation systems, large-scale data engineering, multi-year employer-scale MLOps, distributed training/serving, GPU optimization, or advanced model research.

For every open role found, score on a 1-5 scale:

- **5 — Strong fit**: One lane matches directly, the core requirements are demonstrated, and no central competency requires a stretch argument. They should apply.
- **4 — Good fit**: One lane matches and the core requirements are supported, with only minor or clearly bridgeable gaps.
- **3 — Stretch fit**: Adjacent experience; would need to make a case. Below the keep-threshold — score it but do not list or save.
- **2 — Weak fit**: Requires deep ML research, 6+ yrs specialized AI, or a PhD; or missing the core stack.
- **1 — Not a fit**: Different discipline, manual-only work, or no credible match to any search lane. Skip.

Include the rationale in one line per role.

**Keep only roles scoring 4 or 5.** Drop Fit 3 (stretch) and below entirely — they are not shown in the shortlist or saved to the tracking note.

### Step 3B: Apply freelance work-quality gates

A freelance listing must score Fit 4–5 and also clear these gates:

- **Freshness:** prioritize listings posted within 7 days. Keep listings 8–14 days old when still active. Keep 15–30 day listings only when recent client activity or an explicit ongoing need is visible. Drop older listings without current activity.
- **Scope:** prefer bounded deliverables, clear acceptance criteria, or a credible ongoing role. Exclude vague "build my whole AI app" requests with no usable scope.
- **Economics:** label hourly or fixed-price terms as `Strong`, `Viable`, `Borderline`, or `Unverified` based on the work requested. Do not invent an hourly equivalent when required hours are absent. Drop budgets that are plainly incompatible with the requested production scope.
- **Client quality:** prefer verified payment, prior spend or hires, a coherent history, and recent activity. Missing client history is a risk flag, not an automatic rejection when the scope is excellent.
- **Competition:** record proposal volume when available. High competition changes priority, not fit.
- **Engagement integrity:** exclude unpaid trials, requests to move payment off-platform, agency-only work when hcho is applying individually, manual annotation/review disguised as AI engineering, and listings that primarily seek an unsupported specialty.

### Step 4: Present the shortlist
Present full-time roles and freelance contracts in separate tables, each grouped by lane and sorted by fit. Include:

| Type | Lane | Company / client | Role or project | Location | Compensation / budget | Fit | Why it fits | Apply / propose |
|------|------|------------------|-----------------|----------|-----------------------|-----|--------------|-----------------|

After the tables, report separate counts for full-time roles and contracts, then name the top three overall actions.

Optionally offer follow-ups:
- "Want me to draft a cover letter for any of these?"
- "Want to expand the search to similar companies?"
- "Any of these you want me to dig deeper on?"

### Step 5: Save the scan as a dated tracking note (always)
After presenting, persist the scan to `projects/Job_Search/scans/<YYYY-MM-DD>.md` (create the `scans/` folder if it does not exist; get the real date from `date +%Y-%m-%d`). This is the durable record hcho uses to track applications and proposals, so it always gets written, not just on request.

- One row per opportunity that scored **4+**, with a **Status** column hcho edits over time. Full-time status legend: `To apply` / `Applied` / `Interviewing` / `Offer` / `Rejected` / `Passed`. Freelance status legend: `To propose` / `Proposed` / `Interviewing` / `Hired` / `Declined` / `Closed` / `Passed`.
- Columns: `Status | Type | Source | Lane | Company/client | Role/project | Location | Compensation/budget | Fit | Apply/propose | Notes`. Keep full-time and freelance sections separate, then group by lane and fit.
- Also record the "no openings / unreachable" companies and the list of companies skipped this run, so the note is a complete record of what was and was not covered.
- **Never overwrite an existing same-day file** — it may already hold hcho's Status edits. If `<YYYY-MM-DD>.md` exists, write `<YYYY-MM-DD>-2.md` (incrementing) instead, and tell hcho.

## Reference files

- `references/scoring-rubic.md` — Detailed scoring criteria with examples, for borderline cases.
- `references/company-list.md` — Current organized company list and targeting notes.
- `references/ats-patterns.md` — Common ATS URL patterns and how to find them.

Read these only when you need to resolve ambiguity (e.g., a borderline fit score, or a company whose careers page you can't find).

## Output location

- **Target list (input):** `.agents/skills/job-hunter/assets/companies.yaml`.
- **Source registry (input):** `.agents/skills/job-hunter/assets/search-sources.yaml`.
- **Scan tracking notes (output):** `projects/Job_Search/scans/<YYYY-MM-DD>.md` — one dated note per scan (see Step 5), with a Status column hcho updates to track applications and proposals. This is the canonical record of every scan; do not overwrite prior days.

## Important guidance

- **Be honest about fit.** Don't inflate scores to make the list look productive. A short list of real matches is more valuable than a long list of stretches.
- **Don't fabricate roles.** If a company's careers page is unreachable, say so — never invent a role or URL.
- **Verify links.** Every apply link in the output should be a real URL you actually fetched, not a guess.
- **Respect the resume.** If the resume emphasizes specific domains (e.g., AI engineering, edtech), weight those heavily. Don't surface unrelated roles just because the company is on the list.
- **Enforce the three-lane filter.** Keep honestly qualified Mid-level and Senior IC roles in software quality/systems validation, AI quality/evaluation, or AI product/integration/technical delivery. Keep current AI-builder matches; the broader lanes add credible opportunities rather than replacing them. Read the full JD and drop roles whose spine is manual QA, generic support, quota sales, unsupported specialization, leadership, or research.
- **Use the lanes as a portfolio, not quotas.** For application planning, start with an approximate 40/35/25 mix across software quality/validation, AI quality/evaluation, and AI product/integration/technical delivery. Never pad a lane to hit the mix; report the verified market instead.
- **Enforce the location + fit gates.** Keep only roles that are remote (US-eligible) or within 25 miles of Burbank, CA, and only Fit 4-5. Drop onsite-elsewhere roles and anything Fit 3 or below before it reaches the shortlist or the tracking note. hcho is not relocating.
- **Treat aggregators as discovery sources.** Indeed and similar sites expand coverage; the employer or ATS remains authoritative when available. Preserve an exact aggregator link only when the listing itself is current and readable.
- **Keep employment and freelance evidence separate.** Annual compensation gates do not apply to contracts, and a freelance project does not become employer software tenure. Track applications and proposals with their own statuses.
- **Note when a company has no relevant openings.** It's useful for the user to know a company had no qualifying role in any lane rather than silently omitting it.

## Memory

This skill keeps a free-form `MEMORY.md` in its own folder.

- **Start of every run:** read `MEMORY.md` and apply anything relevant before doing the work.
- **Writing is feedback-gated:** append only when hcho explicitly says to remember something for this skill (a "remember this", a correction, or a stated preference). Do not log routine runs.
- **How to append:** add a dated bullet under `## Notes` in the form `- [YYYY-MM-DD] <note>`, using the real date from `date +%Y-%m-%d`.
- **Cap:** keep `MEMORY.md` under 100 lines. When it nears the cap, tell hcho and ask which entries to prune. Never delete entries silently.
