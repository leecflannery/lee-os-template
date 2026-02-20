---
name: incoming-comms
description: Triage incoming communications AND auto-route context updates. Triggered when you paste raw text from an email, Slack message, DM, LinkedIn message, or any communication without a specific question attached.
---

# Incoming Comms Triage + Auto-Route

When raw communication text is dropped into the conversation, run this workflow:

## 1. Identify

- **Who** is this from? Check `/llm-context/people/` for an existing profile.
- **What channel** — email, Slack, LinkedIn, text, etc.
- **What's the ask** — What does the sender want? Summarize in one line.

## 2. Gather Context

Load everything relevant before advising:

- **People file** — `/llm-context/people/[name].md` if it exists
- **Domain context** — Use the Context Routing table to pull in the right `/llm-context/` files based on the topic
- **Active tasks** — Check `/tasks/` for anything related to this person or topic
- **Recent debriefs** — Check if there's a recent debrief involving this person or topic

## 3. Assess

Present a brief summary:

- **From:** [Name, role, relationship]
- **They want:** [One-line summary of the ask or intent]
- **Relevant context:** [Key facts to keep in mind — prior conversations, commitments, strategic considerations]
- **Tone read:** [Urgent? Casual? Needs careful handling? Straightforward?]

## 4. Recommend Next Steps

Advise on what to do:

- Reply now vs. later
- What to say yes/no to
- Any follow-up tasks to create
- Whether this connects to an active priority
- Anything to watch out for (politics, timing, dependencies)

## 5. Draft Response

Using `/skills/your-voice.md`, draft a response ready to copy-paste with minimal edits.

## 6. Auto-Route Context Updates (DO THIS EVERY TIME)

After presenting the triage and draft, AUTOMATICALLY update all affected files. Do not ask — just do it and report what changed.

### People files
- **Existing person:** Update their profile with new information from this communication.
- **New person:** Create a new profile using the template at `/skills/templates/people-template.md`.

### Domain context
- Identify which `/llm-context/` domain files are affected.
- Update them with any new facts, decisions, or status changes.

### Tasks
- **Completed tasks:** If this communication resolves an open task, mark it done and archive it.
- **New tasks:** If the communication creates new action items, create task files.
- **Status changes:** If this changes the status of an existing task, update it.

### Index files
- Update any `index.md` files in affected directories.

### Report
End with a brief summary of what was updated:

```
**Context updated:**
- Updated people/jane-doe.md (added meeting details)
- Updated work/index.md (project timeline shifted)
- Created task: review-proposal.md
- Archived task: send-brief.md
```
