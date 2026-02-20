# Task Recommend

Suggest the next best task based on current goals and priorities.

## Trigger Phrases

- "What should I work on?"
- "Recommend a task"
- "/next"
- "What's most important right now?"
- "Help me prioritize"
- "What's next?"

## Steps

1. **Load goals**
   - Read `/llm-context/goals.md` for the priority hierarchy
   - The goal hierarchy determines which domain gets priority

2. **Scan tasks**
   - Read all files in `/tasks/` with `status: todo` or `status: in-progress`
   - Sort by: (a) alignment with top goal, (b) due date, (c) tags
   - Skip anything marked done or blocked

3. **Load energy context**
   - Read `/llm-context/personal/index.md` for energy level and constraints
   - If energy is low, suggest lighter tasks over heavy ones

4. **Generate recommendation**

```
## Next up: [Task name]
**Why:** [How it connects to your top goal]
**Due:** [date, if set]

### After that:
- [Next 2 tasks in priority order]

### Overdue:
- [Any overdue tasks, if applicable]

---
Ready to go?
```

## Goal Hierarchy

<!-- CUSTOMIZE: Replace these with your actual priorities. Keep in sync with CLAUDE.md. -->

1. **[Primary focus]** — Gets first claim on time and energy
2. **[Second priority]** — Active but secondary
3. **[Third priority]** — Maintain, don't invest heavily
4. **[Fourth priority]** — Background / opportunistic

## Guidelines

- Be direct. Don't over-explain the scoring. Just say what's next and why.
- If you seem stuck, suggest the smallest possible next step on the current task.
- If something is blocked, say what's blocking it and suggest an unblock action.
- End with a prompt to act, not a question about feelings.
- If all tasks are done or blocked, say so and suggest creating new ones.
