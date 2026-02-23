---
name: weekly-review
description: Weekly review that checks if time allocation matched priorities, surfaces stalls, and sets intention for next week. Use when you say '/review' or 'How did this week go?'
---

# Weekly Review

Zoom out. Check if this week's work matched this week's priorities.

## Trigger Phrases

- "Weekly review"
- "How did this week go?"
- "What did I get done this week?"
- `/review`

## Before You Start

Load:
- `/llm-context/goals.md` -- Current priorities and goals
- Any active domain index files relevant to current priorities

## The Review (3 phases)

Based on GTD's Get Clear > Get Current > Get Creative.

### Phase 1: Get Clear (~5 min)

Gather everything that happened this week.

1. **Scan `/tasks/`** -- List all tasks by status:
   - Completed this week
   - In-progress (carried over)
   - New tasks created
   - Blocked tasks

2. **Check for orphans** -- Are there things you did this week that aren't captured in a task file? If so, either create the task (and mark it done) or note it as untracked work.

3. **Process loose ends** -- Any context shared this session that should be saved to `/llm-context/`? Any people mentioned who need profiles?

Output:

```
THIS WEEK'S WORK

Completed:
- [task] (domain)
- [task] (domain)

In Progress:
- [task] (domain) -- [status note]

Blocked:
- [task] (domain) -- [why]

New Tasks Created:
- [task] (domain)

Untracked Work:
- [anything done that wasn't in a task file]
```

### Phase 2: Get Current (~10 min)

Check whether time allocation matched priorities.

1. **Priority alignment check** -- Load priorities from `goals.md`. For each priority, assess:
   - Did it get meaningful time this week?
   - What moved forward?
   - What didn't move and why?

2. **Metrics snapshot** -- Capture current numbers for anything you track:
   - Subscribers, engagement rates
   - Job search: applications, interviews, responses
   - Project milestones hit
   - Any other key metrics

3. **Side quest audit** -- Flag any work this week that was a side quest (not aligned with top priorities). Not to shame -- just to make it visible.

Output:

```
PRIORITY ALIGNMENT

1. [Priority 1]: [Moved / Stalled / No time]
   - What happened: [summary]
   - Next week: [what needs to happen]

2. [Priority 2]: [Moved / Stalled / No time]
   ...

METRICS SNAPSHOT
- [Metric]: [X] (prev: [Y], delta: [Z])

SIDE QUEST CHECK
- [Any work that wasn't priority-aligned]
- Time spent: [estimate]
- Worth it? [Yes -- because... / No -- reclaim this time]
```

### Phase 3: Get Creative (~5 min)

Look ahead and set intention for next week.

1. **What's the one thing?** -- If you could only accomplish one thing next week, what should it be? This should come from the highest-priority domain that stalled or needs momentum.

2. **Upcoming deadlines** -- Anything due in the next 7-14 days?

3. **Energy check** -- Ask: "How are you feeling about the balance this week? Burned out, energized, bored, scattered?" This is a signal for whether to recommend aggressive or conservative next-week planning.

4. **Recommendations** -- Based on the review, suggest:
   - Tasks to prioritize next week (max 3)
   - Tasks to defer or drop
   - Any context that should be updated in `/llm-context/`

Output:

```
NEXT WEEK

One thing: [The single most important task]

Must-do:
- [ ] [Task 1]
- [ ] [Task 2]
- [ ] [Task 3]

Defer:
- [Task] -- [why it can wait]

Drop:
- [Task] -- [why it's not worth doing]

Open questions:
- [Anything unresolved that needs a decision]
```

## After the Review

1. Create any new task files that emerged
2. Archive completed tasks to `/tasks/archive/YYYY-MM/`
3. Update `/llm-context/goals.md` if priorities shifted
4. Update any domain index files with new metrics or context

## Guidelines

- **Keep it to 20 minutes.** A 70% complete review is better than no review.
- **Don't moralize.** The review surfaces facts, not judgments.
- **Track trends, not just snapshots.** One week means nothing. Three weeks is a signal.
- **Ask, don't assume energy levels.** Capacity varies week to week.
- **Friday or Sunday.** Pick a consistent day. Consistency matters more than timing.

## Sources

Framework informed by:
- [David Allen's GTD Weekly Review](https://super-productivity.com/blog/gtd-weekly-review-guide/) -- three-phase structure (Get Clear, Get Current, Get Creative)
- [Taylor Pearson: Entrepreneur's Weekly Review](https://taylorpearson.me/weeklyreview/) -- resistance-focused questions, one-thing framing
- [Khe Hy: GTD Weekly Review in 25 Minutes](https://www.khehy.com/gtd-weekly-review) -- time-boxed approach, 70% completion principle
