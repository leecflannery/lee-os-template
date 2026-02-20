---
name: catchup
description: Quick briefing on what changed since last session. Diffs git history, surfaces context changes, and flags overdue items.
---

# /catchup — What Happened Since Last Session

**Trigger:** "What did I miss?", "Catch me up", "What changed?", `/catchup`, or at session start when returning after 24+ hours

## Purpose

Give a fast, scannable overview of what changed in the OS since the last session so you can orient before diving into work.

## Process

### 1. Git Diff Since Last Session

Run `git log --oneline --since="[last session date]"` and `git diff --stat HEAD~[n commits]` to identify:
- Files created
- Files modified
- Files deleted

Group by type:
- Context files changed
- Tasks created/completed/archived
- Skills modified
- Other

### 2. Context Delta

For each modified context file, summarize what changed in one line:
- "work/index.md — added new project timeline"
- "people/jane-doe.md — updated with meeting follow-up"

### 3. Task Status

Quick snapshot:
- Tasks completed since last session
- Tasks now overdue
- New tasks created
- Blocked tasks

### 4. Pending Follow-Ups

Check for items that were "waiting on" something with a date that has now passed:
- Messages sent but not replied to
- Meetings that should have happened
- Deadlines that hit

### 5. Calendar Preview (if available)

If Google Calendar MCP is connected, show today's agenda.

## Output Format

```
# Catchup — [Date]
Last session: [date/time estimate]

## What Changed
- [file]: [one-line summary of change]
- [file]: [one-line summary of change]

## Tasks
- Completed: [count] ([list])
- New: [count] ([list])
- Overdue: [count] ([list])

## Waiting On
- [person/thing] — [what you're waiting for] — expected by [date]

## Today's Agenda
[Calendar events if available, otherwise skip]

## Suggested Focus
Based on overdue items, deadlines, and priorities:
1. [Top priority for today]
2. [Second priority]
```

## Guidelines

- Speed over completeness. This should take 30 seconds to read.
- Don't rehash known context — focus on what's NEW or CHANGED.
- If nothing meaningful changed, say "Clean slate — nothing changed since last session."
- Naturally flows into `/today` if you want a full daily briefing.
