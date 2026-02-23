---
name: task-complete
description: Marks a task as done and archives it. Use when you say 'mark [task] done' or when work clearly completes an existing task.
---

# Task Complete

Mark a task as done and archive it.

## Trigger Phrases

- "Mark [task] done"
- "Complete [task]"
- "I finished [task]"
- "Done with [task]"
- "[task] is complete"

**Also runs automatically** whenever task management happens -- if any task's status changes to `done` (including batch updates, casual mentions like "I did X", or tasks completed as side effects of other work), archive it immediately.

## Proactive Detection

When working in any domain, cross-reference open tasks against the work being done:

- **Obvious completions** (we just did the thing the task describes): confirm and archive.
- **Likely completions** (the work strongly suggests the task is done): ask first.
- **Domain scanning**: when starting work in a domain, glance at open tasks with that domain tag. Flag any that look stale or completed.

## Steps

1. **Find the task**
   - Search `/tasks/` for matching filename or title
   - If ambiguous, ask to clarify which task

2. **Update front matter**
   - Change `status: todo` or `status: in-progress` to `status: done`
   - Add `completed: YYYY-MM-DD` field (today's date)

3. **Move to archive**
   - Destination: `/tasks/archive/YYYY-MM/` (based on completion date)
   - Create the month folder if it doesn't exist

4. **Confirm completion**
   - Report: "Archived [task] to `/tasks/archive/YYYY-MM/`."

## Edge Cases

- **Task not found:** "I couldn't find a task matching '[query]'. Did you mean one of these? [list open tasks]"
- **Already done:** "That task is already complete (archived [date])."
- **Blocked task:** "This task is marked as blocked. Mark it done anyway? [reason for block]"

## Notes

- Archive preserves the full file -- nothing is deleted
- Time-boxed folders allow easy cleanup after 6+ months
- Use `completed` date for reflection queries ("what did I finish in January?")
