# Mandu

Your personal agent for projects, job search, and anything you study.
Work with Mandu in chat; use this page to browse the records and sources behind its answers.

## Projects and priorities

- [[context/current-priorities|Priorities]]
- [[context/goals|Goals]]
- [[projects/RepToday/README|Rep Today]]
- [[projects/Purvia/README|Purvia]]
- [[projects/Immerse/README|Immerse]]
- [[projects/gr0wthlab/README|gr0wthlab]]
- [[projects/CreativeBridge/README|CreativeBridge]]
- [[projects/CompeteIntel/README|CompeteIntel]]
- [[decisions/log|Decision history]]

Ask Mandu: “Review my projects against the available evidence. What changed, what is blocked, and what should I do next?”
Project pages are recorded snapshots; a fresh review should verify their claims and identify anything it cannot check.

## Job search

- [[projects/Job_Search/README|Search strategy and preferences]]
- [[projects/Job_Search/interview-prep|Interview preparation]]
- [[projects/Job_Search/wiki/index|Roles knowledge library]]

Dated search results and application statuses live in `projects/Job_Search/scans/`.
Ask Mandu: “Find current roles that fit my experience and preferences.”

## Learning

- [[inbox/README|Inbox instructions]]
- [[projects/Education/README|Learning library]]
- [[projects/Education/AI/AI_Wiki/wiki/index|AI knowledge]]
- [[projects/Education/Marketing/wiki/index|Marketing knowledge]]
- [[projects/Education/Business/wiki/index|Business knowledge]]
- [[projects/Education/AI/LLM_Evals/README|Evals study track]]

Drop a `.md` file into `inbox/`, then run `/ingest`.
Mandu preserves the source, organizes useful knowledge by subject, connects relevant projects, and gives a short review.
Other subjects are added as material arrives.

Ask Mandu: “What have I learned about this topic, and how could I use it in my projects?”
Answers start with saved material, link to sources, and distinguish outside evidence and interpretation.

## How Mandu works

- [[CONTEXT|Agreed definitions and workflow]]

Recurring project checks are configured for weekdays at 9 a.m. Pacific, using available project evidence and existing job-search records.
Mandu reports meaningful changes, blockers, completions, failures, or decisions needing attention and stays quiet when nothing actionable changes.
New job searches and `/ingest` remain separately invoked.
