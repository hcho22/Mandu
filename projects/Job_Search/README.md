# Job Search

**One-liner:** hcho's active search across software quality/systems validation, AI quality/evaluation, and AI product/integration/technical delivery, run as the parallel income hedge alongside the product bets.

**Status:** Active

**Key dates:**
- Target: income by end of 2026 (a role here, or app revenue via Agentic RAG).

## Strategy (updated 2026-09-22)

**Primary strategy: three complementary lanes, broad enough to improve opportunity volume while remaining evidence-backed.**

1. **Software quality and systems validation:** SDET; Software QA Automation; Systems Validation; Verification and Validation; Product Quality; Test Infrastructure; API/backend automation; Mobile/iOS Test; and Release Quality. Favor automation, APIs, mobile, connected devices, developer tools, and AI products. Exclude manual-only QA and pure hardware-only validation with no meaningful software or automation ownership.
2. **AI quality and evaluation:** AI Quality; AI Test; AI/ML Validation; Machine Learning Engineer, Evals; Machine Learning Evaluation; ML or Model Quality; ML Validation; LLM or Model Evaluation; AI Reliability; ML Systems QA; Evaluation Platform; Responsible AI Test; Data Scientist roles centered on Model Evaluation, Trust and Safety, AI Quality, or AI Reliability; and product-evaluation-focused AI red teaming. Trust-and-safety data-science roles qualify only when ML models, anomaly or abuse detection, model performance, evaluation, or reliability are central. Validation tenure supplies rigor, but does not substitute for a required multi-year record of shipping software test infrastructure or evaluation systems.
3. **AI product, integration, and technical delivery:** AI/Applied AI/Agentic/LLM/GenAI/Product Engineer; Applied Machine Learning Engineer; AI/ML Engineer; Data Scientist, Applied ML; Integration or Implementation Engineer; Customer Engineer; hands-on Technical Solutions Engineer; Developer or Technical Support for APIs, developer tools, or AI platforms; Product Engineer for internal tools/workflow automation; Forward Deployed AI Engineer; and software/full-stack roles centered on shipping AI features. Applied-ML and data-science titles qualify when the work centers on model building or evaluation, NLP/CV, LLMs/RAG/agents, or productionizing a supported ML capability.

Preserve qualified AI-builder roles; the broader lanes add credible opportunities rather than replacing them. Apply at the Mid-level and Senior IC levels when the stated experience and core competencies are honestly clearable. Exclude manual QA, annotation, generic support, quota-dominated sales, leadership-heavy Staff/Principal/Lead, research/PhD-gated work, and roles whose spine is an unsupported frontend, SDK/library, DevOps/SRE, MLOps platform, conventional product/growth analytics, causal-inference or Bayesian leadership, recommendation/ranking/pricing/forecasting, core model training/post-training, distributed GPU training, inference optimization, CUDA, or advanced ML specialty.

Use an approximate **40/35/25 application mix** across the three lanes as a starting portfolio, never as a quota that justifies weak matches. The job-hunter skill remains responsible for the exact location, compensation, seniority, evidence, and fit gates.

## Search sources and engagement types (updated 2026-09-28)

Broad and weekly searches now cover three source classes by default:

1. **Direct employer and ATS pages** from the curated company list. These remain authoritative for whether a role is live and for its requirements, location, compensation, and application link.
2. **Full-time discovery sites**, led by Indeed and supplemented by Wellfound, YC Jobs, and Built In. Aggregator results expand coverage; Mandu de-duplicates them and verifies the employer or ATS version when available.
3. **Freelance marketplaces**, led by Upwork and supplemented by Contra and Braintrust when exact listings are accessible.

Full-time roles retain the existing remote-US/Burbank-area, Fit 4–5, seniority, and approximate $150K compensation-top gates. A strong role with undisclosed compensation is separated as conditional rather than counted as qualified.

Freelance work uses the same three skill lanes and Fit 4–5 bar, with contract-specific checks for freshness, scope, rate or fixed-price economics, client history, proposal competition, and platform integrity. Prioritize AI/RAG/agent integrations, FastAPI/React applications, React Native/Expo work, MCP/API integrations, and software or AI validation projects. Exclude manual QA, annotation, unpaid trials, off-platform payment requests, agency-only engagements, vague full-product builds with token budgets, and projects whose core specialty is unsupported. Track these as `To propose` / `Proposed` / `Interviewing` / `Hired` / `Declined` / `Closed` / `Passed`, separately from full-time application statuses.

The existing company tiers remain a starting source list, not a restriction on role lane:

- YC-backed agentic / applied-AI startups (FDE / Applied AI shaped).
- **Tier A/B/C:**
  - **Tier A, Frontier labs:** Anthropic, OpenAI, Google DeepMind, xAI, Meta / FAIR.
  - **Tier B, Evals / observability vendors:** Braintrust, LangChain (LangSmith), Galileo, Patronus, Arize.
  - **Tier C, AI-first product:** Cursor / Anysphere, Perplexity, Harvey, Sierra.

  Each company entry carries `target_role`, `why_fit`, and `watch_outs`.

## Assets and tooling

- **Skill:** `job-hunter` at `.agents/skills/job-hunter/` searches direct employers, broad job sites, and freelance marketplaces, then ranks opportunities by fit and work quality.
- **Target list:** `.agents/skills/job-hunter/assets/companies.yaml` (the company list with tiers).
- **Search-source registry:** `.agents/skills/job-hunter/assets/search-sources.yaml` (direct, aggregator, startup-board, and freelance sources plus query families).
- **Company-list reference:** `.agents/skills/job-hunter/references/company-list.md`.
- **Master profile:** `profile/` (since 2026-10-08) is the single source of truth for career facts: evidence-backed Claims plus a generated Skill index. See `profile/README.md`.
- **Resumes:** `Resume/*.docx` are older renderings and contain overstated lines; build new materials from the Master profile instead.
- **Application packets:** `applications/<date>-<company>-<role>/` (since 2026-10-08), one per role, built by the `application-packet` skill and checked by `applications/build_packet.py`. Each holds the posting snapshot, `packet.yaml`, the generated resume (.pdf, .docx), and `packet.md` for review. hcho submits; Mandu never does.
- **Interview prep:** `interview-prep.md` consolidates talking points across projects and wikis.
- **Roles wiki:** `wiki/` (mode full) maps target roles, their qualifications/skills, and hcho's path into each; sibling `raw/` inbox. Schema in `wiki/CLAUDE.md`. Drop a posting or role guide into `raw/` and say "ingest this."
- **Archive:** `archive/` holds the legacy daily notes (2026-05-12, 05-29, 05-30) and the old long-term `MEMORY.md`, kept read-only for history.
