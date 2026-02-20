---
name: call-prep
description: Auto-aggregates all relevant context for an upcoming meeting or call. Loads people profiles, domain context, open tasks, and decision status into a single briefing.
---

# Call Prep

Generate a pre-call briefing that consolidates everything you need before a meeting.

## Trigger Phrases

- "Prep me for [meeting/call]"
- "Brief me on [person/group]"
- "What do I need to know before talking to [person]?"
- `/call-prep`

## Inputs (ask if not provided)

1. **Who** — Name(s) of the people in the meeting
2. **What** — Topic or purpose of the call (if known)

## Process

### Step 1: Load People Context

For each person in the meeting:
- Check `/llm-context/people/[name].md` — load if exists
- If no profile exists, note it and offer to create one after the call

### Step 2: Load Domain Context

Based on the people and topic, load the relevant domain index. Skim for what's relevant to this call — don't dump the whole file.

### Step 3: Load Active Decisions

Check `/llm-context/decisions.md` for pending decisions that involve these people or this topic.

### Step 4: Load Related Tasks

Search `/tasks/` for tasks referencing the people or topic. Note status and due dates.

## Output Format

```
CALL PREP: [Meeting Name / Topic]
With: [Names]

─── PEOPLE ───

[Person 1]
- Role: [what they do]
- Relationship: [how you know them]
- Key context: [2-3 bullets relevant to THIS call]
- Last interaction: [date, topic]

─── CONTEXT ───

[2-4 bullets of domain context relevant to the call. Not a full index dump.]

─── OPEN DECISIONS ───

[Pending decisions from decisions.md relevant to this call]
- [Decision]: [current lean] — decide by [date]

─── OPEN TASKS ───

[Tasks related to this meeting or these people]
- [Task]: [status] — due [date]

─── YOUR OBJECTIVES ───

Based on all the above:
1. [Specific, actionable objective]
2. [Objective]
3. [Objective]

─── WATCH OUT FOR ───

[1-2 relationship dynamics, framing risks, or things to be careful about.
Pulled from people profiles and past debriefs.]
```

## After the Call

Remind: "Say `/debrief` and I'll capture what happened and update the relevant files."

## Guidelines

- **2 minutes to read.** If deeper context is needed on any section, ask.
- **Objectives are the core value.** Everything else is context for the objectives.
- **"Watch out for" is strategic.** Relationship dynamics, power dynamics, framing risks.
