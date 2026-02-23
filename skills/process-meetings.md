---
name: process-meetings
description: Processes meeting transcripts or notes and routes extracted context to domain files, people profiles, and tasks. Use when a transcript is dropped or you say '/process-meetings'.
---

# Process Meetings

Process raw meeting notes and route extracted context to the appropriate domain files in `/llm-context/`.

## Trigger

- "Process meetings", "Process my meeting notes", `/process-meetings`
- For a specific meeting: "Process the [meeting name] from today"

---

## Process

### 1. Identify Unprocessed Meetings

If you maintain a meeting notes index, look for entries that lack a brief description (unprocessed). If processing all, start with the most recent first. If there are many (10+), confirm: "There are N unprocessed meetings. Want me to do all of them, or focus on a specific date range?"

### 2. Read and Extract

For each unprocessed meeting, read the raw transcript/notes and extract:

**Always extract:**

| Field | What to capture |
|-------|----------------|
| **Brief description** | 1 sentence -- what was this meeting about? |
| **Key decisions** | Anything decided or agreed upon |
| **Action items** | Things committed to or that need doing |
| **Status changes** | Project status updates, timeline shifts, blockers added/removed |
| **New people** | Anyone mentioned who should get a people file or profile update |
| **Open questions** | Unresolved items or things to follow up on |

### 3. Route Extracted Context

For each piece of extracted context:

1. **Read the target domain context file** to understand current structure and content
2. **Add new information in the appropriate section** -- match the file's existing structure
3. **Date-stamp the addition** using the meeting date:
   ```
   *(from 2026-02-10 Team Sync)*
   ```
4. **Avoid duplication** -- if the context file already captures this information, skip it
5. **If a relevant domain file doesn't exist yet**, note it and suggest creating one -- do not create new context files without asking

### 4. Create Action Items

For action items extracted from meetings:

1. Check if an existing task in `/tasks/` already covers this action
2. If not, **create the task file immediately** -- don't ask
3. Follow the task-create skill format

### 5. Update People Files

For new people mentioned in meetings:

1. Check if `/llm-context/people/[name].md` already exists
2. If it exists, update with new information from the meeting
3. If it doesn't exist, **create the profile immediately** using the people template

### 6. Update Meeting Notes Index

If you maintain a meeting notes index, update the entry with a brief description after processing. The description serves double duty: it summarizes the meeting AND marks it as processed.

### 7. Report Results

After processing, present a structured summary:

```
## Meetings Processed

### [Meeting Title] (YYYY-MM-DD)
**Summary:** [1-sentence description]
**Context routed to:**
- [file] -- [what was added]
**Action items:**
- [ ] [action item]
**People updates:**
- [person] -- [new/updated profile note]

---

## Overall
- **Meetings processed:** N
- **Context files updated:** [list]
- **New action items:** N
- **People needing profiles:** [list]
```

---

## Context Routing

Use the Context Routing table in CLAUDE.md to determine where to route information. When a meeting spans multiple domains, route relevant parts to each domain file.

**Ambiguous meetings:** If content doesn't clearly fit a domain, read the first ~50 lines and categorize by content. If still unclear, ask.

---

## Important Rules

### Personal/Sensitive Meetings
- Extract **themes and insights only**. Never copy raw sensitive content verbatim.
- Synthesize into the language already used in the target context file.
- Date-stamp additions.

### Work Meetings
- Focus on: decisions, blockers, status changes, deliverables, deadlines, ownership changes.
- Skip: meeting logistics, small talk, agenda reviews, "let's schedule a follow-up."
- For 1:1s, capture: feedback given, goals discussed, career development notes, project priorities.

### Cross-Domain Meetings
- Some meetings span domains. Route the relevant parts to each domain file.
- Avoid duplicating the same information -- each domain file should get what's relevant to that domain.

### General
- Always ask before creating new context files.
- Date-stamp all additions so context freshness is visible.
- If a transcript is empty or mostly logistics, mark it as processed: "Logistics only -- no substantive context extracted."
- Process meetings in chronological order within a batch (oldest first) so context builds naturally.
