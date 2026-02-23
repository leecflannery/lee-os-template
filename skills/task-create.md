---
name: task-create
description: Creates a properly formatted task file when something actionable is mentioned in conversation. Triggers on 'I need to...', 'Remind me to...', or any clear action item.
---

# Task Create

When something actionable is mentioned casually, create a properly formatted task file.

## Trigger Phrases

- "I need to..."
- "Remind me to..."
- "Add a task for..."
- "Don't let me forget..."
- Or any clear action item mentioned in conversation

## How to Parse

From casual input, extract:
- **Action**: What needs to be done
- **Domain**: Infer from content (work, personal, side-project, etc.)
- **Due date**: If mentioned; otherwise ask or leave blank
- **Tags**: Infer from content using the taxonomy in CLAUDE.md

## Examples

**Input**: "I need to send a thank you email to the recruiter"
**Output file**: `/tasks/job-search-send-thank-you-recruiter.md`

```yaml
---
type: task
due: [tomorrow's date]
tags: [job-search, follow-up]
status: todo
---

Send thank you email to recruiter after interview.

## Notes
- Keep it concise, reference specific conversation points
- Reiterate interest in the role
```

---

**Input**: "Research what that company's product actually does before I apply"
**Output file**: `/tasks/job-search-research-company-product.md`

```yaml
---
type: task
due:
tags: [job-search, research]
status: todo
---

Research the company's product before applying.

## To Cover
- Core product functionality
- Target customer
- Recent funding/news
- How it relates to my experience
```

## File Naming

- Lowercase, hyphenated
- Domain-first: `[domain]-[action].md`
- Examples: `work-send-brief.md`, `personal-schedule-dentist.md`
- Keep it short but identifiable

## After Creating

Confirm:
> "Created task: [filename]. Due: [date or 'no date set']. Anything to add?"
