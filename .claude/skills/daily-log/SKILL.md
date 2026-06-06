---
name: daily-log
description: Create or open today's daily log entry for a tracked project (defaults to HabitLoop). Use when the user says "start today's log", "log today's progress", "new daily log", "log my HabitLoop progress", "open today's log", or wants to record what they did today on a project. Scaffolds the day's file from a template, carries forward yesterday's "Next" items, and never overwrites an existing entry.
---

# Daily Log

Creates or opens the day's daily log file for a tracked project under `projects/<Project>/log/<YYYY-MM-DD>.md`. Default project is **HabitLoop** (the one tracked daily). The skill scaffolds a consistent entry from a template and pulls forward unfinished items from the previous log so each day starts where the last one ended.

## When to use this skill

Trigger when the user wants to:
- Start or open today's daily log ("start today's log", "open today's log")
- Record progress on a project for the day ("log my HabitLoop progress", "log what I did today")
- Create a fresh daily entry from the template

## Inputs needed

1. **Project** — defaults to `HabitLoop`. If the user names another project, use `projects/<that-project>/` (it must already exist under `projects/`). If the named project has no `log/` folder yet, create one.
2. **Content (optional)** — if the user describes what they did, fill it into the entry. If they just want the scaffold, create it empty and tell them it's ready.

## Workflow

### Step 1: Resolve project and date
- Project: default `HabitLoop` unless the user names another. Path root is `projects/<Project>/`.
- Date: run `date +%Y-%m-%d` to get today's date. Do not hardcode or guess the date.
- Target file: `projects/<Project>/log/<DATE>.md`.

### Step 2: Check if today's log already exists
- If `projects/<Project>/log/<DATE>.md` already exists, **do not overwrite it.** Read it, show its current contents, and offer to append/update. Stop here unless the user wants edits.
- Only proceed to create when the file does not exist.

### Step 3: Carry forward from the previous log
- List `projects/<Project>/log/` and find the most recent prior entry (highest date filename before today).
- If one exists, read its `## Next` section. Pre-fill today's `**Today's goal:**` and `## Next` placeholder context from those items so unfinished work carries over. Keep it short; this is a starting point the user will edit.
- If no prior log exists, leave the goal blank.

### Step 4: Create today's entry from the template
- Read `assets/daily-log-template.md`.
- Replace `{{PROJECT}}` with the project name and `{{DATE}}` with the resolved date.
- For HabitLoop specifically, `**Milestone focus:**` maps to a milestone in the repo's `ROADMAP.md` (M0–M10). If you know the current milestone from the carried-forward "Next", suggest it.
- Write the file to `projects/<Project>/log/<DATE>.md`.
- If the user provided content, fill the `## Done`, `## Notes / Learnings`, `## Blockers`, and `## Next` sections accordingly.

### Step 5: Confirm
- Tell the user the file path and what was pre-filled (especially carried-forward items).
- For HabitLoop, respect tutor mode: this skill logs progress, it does not write project code.

## Important guidance

- **Never overwrite an existing daily log.** If today's file exists, append or edit only with the user's confirmation. Losing a day's notes is the worst failure mode here.
- **Always use the real system date** via `date +%Y-%m-%d`. Do not trust ambient context for the date when writing a file path.
- **Keep the template consistent.** Use `assets/daily-log-template.md` as the single source of truth for the entry format; do not freehand a different structure.
- **Carry forward, don't duplicate.** Pull yesterday's open "Next" items into today's goal as a starting point, but don't copy the whole previous entry.
- **HabitLoop is tutor mode.** This skill records progress and learnings; it does not write `.js`, `.sql`, or config files for the project. See `projects/HabitLoop/README.md`.

## Reference files

- `assets/daily-log-template.md` — the canonical daily entry format with `{{PROJECT}}` and `{{DATE}}` placeholders.

## Memory

This skill keeps a free-form `MEMORY.md` in its own folder.

- **Start of every run:** read `MEMORY.md` and apply anything relevant before doing the work.
- **Writing is feedback-gated:** append only when hcho explicitly says to remember something for this skill (a "remember this", a correction, or a stated preference). Do not log routine runs.
- **How to append:** add a dated bullet under `## Notes` in the form `- [YYYY-MM-DD] <note>`, using the real date from `date +%Y-%m-%d`.
- **Cap:** keep `MEMORY.md` under 100 lines. When it nears the cap, tell hcho and ask which entries to prune. Never delete entries silently.
