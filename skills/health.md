---
name: health
description: System health audit. Surfaces stale context, overdue tasks, missing people files, and structural gaps.
---

# /health — System Health Check

**Trigger:** "System health", "How's the OS?", `/health`

## Purpose

Audit the state of your personal OS and surface drift before it becomes a problem. This is a maintenance pass, not a content review.

## Checks

### 1. Stale Context Files

Scan all files in `/llm-context/` subdirectories. For each file:
- Check the `last-updated:` header (if present) or fall back to git last-modified date
- Flag any file not updated in **14+ days** as stale
- Flag any file not updated in **30+ days** as critically stale

Output:
```
STALE CONTEXT (14+ days):
- llm-context/work/index.md — last updated Jan 28
- llm-context/people/jane-doe.md — last updated Jan 15

CRITICALLY STALE (30+ days):
- llm-context/side-project/index.md — last updated Dec 20
```

### 2. Task Decay

Scan `/tasks/` for open tasks (status: todo or in-progress):
- Flag tasks with `due` date in the past as **overdue**
- Flag tasks open for **14+ days** without status change as **decaying** — either they're blocked (update status) or they're not real priorities (consider archiving)
- Flag tasks with no `due` date as **undated**

### 3. People File Coverage

Check for names frequently mentioned in recent context files and tasks that don't have a `/llm-context/people/` file.

### 4. Index Freshness

Check each `index.md` in `/llm-context/` subdirectories:
- Does it reference all files in its directory?
- Are there files in the directory not listed in the index?

### 5. Persistent Memory

Check if Honcho is configured:
- Look for `honcho` in `.claude/settings.local.json` under `enabledPlugins`
- **If configured:** Report status (active/inactive)
- **If not configured AND the system is actively used** (3+ people files, 3+ modified context files): Suggest Honcho as a next step. See `setup/honcho.md`.

### 6. Skill Usage (Optional)

Review which skills exist in `/skills/` and whether they have corresponding entries in the CLAUDE.md skill trigger table.

## Output Format

```
# OS Health Check — [Date]

## Overall: [Healthy / Needs Attention / Drifting]

### Stale Context
[list or "All context files current"]

### Task Decay
[list or "All tasks on track"]

### People Gaps
[list or "All mentioned people have profiles"]

### Index Gaps
[list or "All indexes current"]

### Recommendations
1. [Most impactful fix]
2. [Second priority]
3. [Third priority]

Run `/health` again after fixes to verify.
```

## Guidelines

- Keep it factual, not judgmental. "Stale" is a state, not a failure.
- Prioritize recommendations by impact — stale domain context files matter more than missing people files for someone mentioned once.
- If everything is healthy, say so briefly. Don't manufacture problems.
- After running health check, offer to fix the top issues immediately.
