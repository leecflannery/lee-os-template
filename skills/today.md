---
name: today
description: Daily briefing that surfaces priorities, due tasks, overdue items, and stale context. Use when you say '/today' or 'What's on for today?'
---

# /today

Generate your daily briefing.

## Steps

1. **Load goals**
   - Read `/llm-context/goals.md` for current priorities
   - Note the goal hierarchy for framing the day

2. **Scan tasks**
   - Search `/tasks/` for files where `due` is today or past due
   - Search for any files with `status: blocked` that mention waiting on something with a date
   - Note any `high-priority` tags
   - Flag which goals each task advances
   - **Task decay check:** Flag any task open 14+ days without progress — either it's blocked (update status) or it's not a real priority (suggest archiving)

3. **Context freshness check**
   - Scan `/llm-context/` domain index files for `last-updated:` headers or git dates
   - Flag any domain context not updated in 14+ days
   - Don't list every file — just the domains that are drifting

4. **Domain check-in** (one item each, only if relevant today)
   <!-- CUSTOMIZE: Replace these with your actual domains -->
   - **Work**: Only if something is due this week
   - **Side project**: Current blocker or next step
   - **Personal**: Only if there's a time-sensitive item

## Output Format

```
# Today: [Day, Month Date]

## Focus
[Reference the #1 goal from goals.md]

## Top Priority
[The single most important task today, tied to goals]

## Tasks Due
- [ ] [task name] — [context]
- [ ] [task name] — [context]

## Overdue
- [ ] [task name] — [days overdue]

## Decaying (14+ days, no progress)
- [ ] [task name] — opened [date]. Still relevant? Archive or update.

## Context Drift
[Domains with stale context, or "All context current"]

## Notes
[Any blocked items, upcoming deadlines within 3 days, or calendar conflicts]
```

## Guidelines

- Keep it scannable — no paragraphs
- If a section is empty, omit it
- Time estimates only if you've added them to task files
- End with: "What would you like to tackle first?"
