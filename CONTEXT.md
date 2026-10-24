# Mandu

Mandu is hcho's personal agent for keeping track of projects, finding potential employment opportunities, and answering questions from material hcho learns through tutorials.
This context records the shared language as the second-brain design is clarified.

## Language

**Mandu**:
hcho's personal agent spanning project tracking, job search, and questions about learned material.
_Avoid_: Using Mandu to mean only a notes folder or only a tutorial library.

**Project**:
A tracked workstream in hcho's portfolio with its own purpose and current state.

**Learning source**:
A Markdown (`.md`) file that hcho brings into Mandu through Obsidian to support learning and later questions.

**Inbox**:
The shared entry point for new learning sources before Mandu organizes them into the appropriate knowledge area.

**Subject area**:
A reusable field of knowledge that hcho studies, independent of any one project's lifespan.

**Project review**:
An assessment of a project's current state using available project evidence together with hcho's updates.
The same Project review may be read in a chat session or delivered to hcho's phone.
_Avoid_: Calling the phone-delivered version a "brief"; it is the same Project review.

**Job search**:
hcho's ongoing workstream for finding and pursuing employment opportunities that match his experience and preferences.

**Capture**:
A short update hcho sends Mandu from wherever hcho is, which Mandu files into the record it belongs to.
_Avoid_: Treating a Capture as a Learning source; Captures are status and decisions, not study material.

**Dispatch**:
Mandu handing development work on a Project to firstmate, which carries it out and reports the outcome back.

**Account action**:
Something Mandu does in one of hcho's external accounts, such as email, calendar, or a job application, that other people can see or that is hard to undo.

**Gr0wthPilot**:
The Mandu skill that takes one of hcho's existing Products and writes its Candidate Package, which hcho may hand to gr0wthlab.
hcho starts each run himself with `bin/gr0wthpilot <Product>`; a run asks him nothing, spends nothing new, publishes nothing, and states no fact it did not fetch.
_Avoid_: "marketing agent", which names the dry-run creative loop in RepToday's package and is easily confused with gr0wthlab.

**Go-To-Market Package**:
A Product's approved marketing decisions in `projects/<Product>/gtm/`, such as its positioning, approved claims, banned language, and Angles, which gr0wthlab reads.
It changes only when hcho approves a proposed change, or whole at a Handoff.

**Candidate Package**:
What a Gr0wthPilot run writes for a Product: a complete, proposed Go-To-Market Package that nothing reads or acts on yet.
For a Product already handed off, a run writes it beside the live package, in a dated `gtm-candidate-<date>/` folder, and never over it.
_Avoid_: calling it the Go-To-Market Package before Handoff, or a Draft, which is a single post or message.

**Handoff**:
hcho's word that a Candidate Package is approved ("<Product> - hand to gr0wthlab"), which makes it the Product's Go-To-Market Package; firstmate then adds the Product to gr0wthlab's product list through a reviewed gr0wthlab change.
Without his word there is no Handoff, however well the Candidate Package passed its own checks.
For a Product already handed off, a Handoff replaces its package whole, only between 14-day windows, and only once gr0wthlab can take a replacement package.

**Launch Set**:
The one-off, ready-to-post first-week posts and profile assets a Candidate Package carries for Instagram, X, and TikTok, which hcho posts by hand.
gr0wthlab never operates them.

**Test Kit**:
The 14-day set of pre-registered posting experiments in a Candidate Package, each an Angle with its Hook pairs, success signal, and kill criterion, on the platforms gr0wthlab runs, today TikTok and YouTube Shorts.
It is the part of the package gr0wthlab operates after Handoff.
_Avoid_: calling the Launch Set's posts part of the Test Kit.

**Master profile**:
hcho's single source of truth for job applications: a ledger of Claims, each backed by evidence.
Every resume and cover note is assembled from it.
_Avoid_: Calling a resume, even the base resume, the Master profile; a resume is one rendering of it.

**Claim**:
One statement about hcho's experience, carrying its result or number, the evidence that proves it, its Evidence scale, and its dates.
A number in a Claim is true only as of its stated as-of date.

**Evidence**:
What makes a Claim true, in one of two kinds.
Linked evidence is something anyone could open, such as a repository, an eval receipt, or a certificate; Attested evidence is hcho vouching for work where no artifact could exist, and being able to defend it in an interview.
_Avoid_: Treating an earlier resume line as evidence; past resumes are only leads to check.

**Application packet**:
Everything Mandu prepares for one job application: a one-page resume assembled only from Master profile Claims in the ad's own wording, answers for that application form's text fields, and a short note on the gaps hcho should own in an interview.
hcho reviews it and submits it himself.
_Avoid_: Calling the packet "the application"; the application is what hcho submits.

**Skill index**:
A table, built from the Master profile and never edited by hand, showing for each skill how long hcho has used it at an employer and in his own projects, and which job-search lanes it supports.
It is how a job requirement such as "3+ years of professional Python" gets checked against hcho's record.

**Evidence scale**:
Where a Claim was earned: at an employer, in hcho's own project, or in coursework.
It limits how far a Claim can stretch against a job requirement; project-scale work never counts as employer tenure.
Volunteer work is project-scale even when done on a team.

## Relationships

- **Mandu** keeps track of multiple **Projects**.
- **Mandu** answers hcho's questions using **Learning sources**.
- A **Learning source** may be relevant to multiple **Projects**.
- **Learning sources** are organized into **Subject areas** as material arrives, with links across subjects and projects where useful.
- A **Project review** combines available project records with hcho's updates about work or decisions not captured there.
- **Job search** is a core Mandu responsibility and a tracked workstream alongside the product projects.
- A tailored resume or cover note may only select and rephrase **Claims** from the **Master profile**; it never introduces a new one.
- A statement with neither Linked nor Attested **Evidence** is not a **Claim** and cannot enter the **Master profile**.
- A **Capture** never records a decision on a gr0wthlab Review Queue item or anything else hcho did for gr0wthlab; he gives those on gr0wthlab's own sitting page, gr0wthlab keeps them, and Mandu only reads them.
- A **Dispatch** from gr0wthlab starts only from a Dispatch request that gr0wthlab's queue closed as approved and whose decision record says approve; Mandu does not hand it to firstmate itself, but gives the request to hcho to pass to firstmate, and writes nothing outside Mandu.
- A **Gr0wthPilot** run writes only its **Candidate Package** in `projects/<Product>/` and reads the Product's own repository without changing it; it never writes into a live **Go-To-Market Package**.
- A **Candidate Package** becomes a **Go-To-Market Package** only at a **Handoff**; its **Test Kit** is what gr0wthlab then runs, and its **Launch Set** stays hcho's to post.
- Mandu prepares an **Application packet** but never submits it; submitting is an **Account action** hcho takes himself.
- Work from June 2025 onward requires Linked **Evidence**; Attested **Evidence** is reserved for earlier work and for coursework awaiting its certificate.
- Independent work is described once as built solo by directing AI coding agents; a **Claim** then says "built" only for work hcho can explain, how and why, without notes in an interview, and a Claim he would need to study first is not used until he has.

## Agreed operating approach

- Chat is hcho's primary interface to Mandu for project reviews, job searches, and learning questions; an Obsidian home page provides navigation to the underlying Markdown records and sources.
- Start with evidence-based project reviews: inspect available repositories and project records, combine findings with hcho's updates, and ask about missing context.
- Run recurring evidence-based project checks every weekday at 9 a.m. Pacific (America/Los_Angeles), using available canonical repository evidence, project records, and hcho's updates; notify only for meaningful changes, blockers, completions, failures, or decisions needing attention.
- The active automation is `mandu-weekday-project-review`; include existing job-search records in reviews, while new job searches and learning ingestion remain separately invoked.
- Build on the existing job-search workflow and its established role preferences, fit criteria, and dated scan records.
- Before a Claim's number enters a tailored draft, re-read its source if the as-of date is more than 14 days old; use the current number or drop the Claim, and tell hcho which in the approval request. Attested numbers describe finished work and are exempt. The Master profile has no scheduled refresh.
- Answer learning questions from saved material first, citing the relevant notes and sources; supplement with outside knowledge when needed and distinguish sourced claims from Mandu's interpretation.
- Verify current technical details against official documentation, and identify gaps or contradictions rather than treating a tutorial as current by default.
- When hcho supplies a tutorial for learning capture, preserve the source, automatically summarize and file useful knowledge, connect relevant existing notes and projects, and provide a short review afterward.
- Ask about material ambiguities that prevent accurate filing; routine ingestion does not require a pre-filing discussion.
- Learning inputs include videos, articles, documentation, courses, and personal notes, supplied as `.md` files; hcho handles conversion, including YouTube-to-Markdown conversion, before adding them through Obsidian.
- Keep the saved learning sources and generated knowledge notes in Markdown; preserve supplied source links and timestamps, and identify missing provenance without inventing it.
- Use the root `inbox/` folder as the shared drop location for incoming learning files; Mandu determines their destination and project connections, while existing source folders remain intact.
- hcho runs the existing `/ingest` skill after adding a learning file through Obsidian; this is the processing trigger, followed by automatic filing and a short review.
- Support anything hcho studies, organized by subject as material arrives; retain the existing AI wiki for general AI knowledge and create other subject areas only when needed.
- Give reusable knowledge one authoritative home and link it to relevant projects rather than duplicating it for each use.

## Example dialogue

> **hcho:** "Keep track of my projects, help me find employment opportunities, and answer questions from my tutorials."
> **Mandu:** "I will start project reviews from available evidence and your updates, and use the existing job-search and learning records for those responsibilities."

## Flagged ambiguities

- "Second brain" resolved on 2026-09-23: Mandu is a personal agent serving project tracking, job search, and learning questions.
- Project-update approach resolved on 2026-09-23: evidence-based reviews first, with recurring checks to be added.
- Recurring review resolved and configured: weekdays at 9 a.m. Pacific, with notifications only for meaningful changes or required attention.
- Learning-answer approach resolved on 2026-09-23: saved material first, supplemented when needed, with clear attribution and verification of current technical details.
- Tutorial-capture approach resolved on 2026-09-23: automatic organization followed by a short review, with questions only for material ambiguities.
- Learning-input format resolved on 2026-09-23: all learning material arrives as `.md` files, regardless of its original medium.
- Learning intake location resolved: one root `inbox/` folder in Mandu.
- Learning processing trigger resolved: hcho invokes the existing `/ingest` skill after adding a file.
- Learning scope resolved: anything hcho studies, organized by subject as material arrives.
- Interaction model resolved: chat first, with an Obsidian home page for browsing and reviewing the shared records.
- Application-pipeline focus resolved on 2026-10-08: the bottleneck is time per application and low confidence in matches, not finding roles; work starts with the Master profile.
- Master profile form resolved on 2026-10-08: an evidence-tagged Claim ledger, not a fuller resume.
- Employment gap resolved on 2026-10-08: 2018 to 2023 is a career break with ML retraining, shown as one honest line; coursework is dated by year range until exact certificate dates are filled in later.
- Master profile scope resolved on 2026-10-08: full Claims for Rep Today, Purvia, Immerse, CreativeBridge, Omdena, and Zebra, plus one grouped Claim for the 2018 to 2023 retraining that backs the career-break line; smaller builds stay out for now.
- Omdena engagement resolved on 2026-10-08: volunteer collaborative projects, so every Omdena Claim is project-scale and the "AI/ML Consultant" framing is retired.
- AI-agent authorship resolved on 2026-10-08: stated once for all independent work, with plain verbs in each Claim, gated by whether hcho can explain the work in an interview.
- Application output resolved on 2026-10-08: one Application packet per role, shaped to that form's actual fields rather than a fixed cover note, with a target of about ten minutes of hcho's time per application.
- Private-repository evidence resolved on 2026-10-08: hcho made CreativeBridge public so its Claims meet the "anyone could open" bar; Story_Quest stays private and its Claim is marked private.
