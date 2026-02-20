# Debrief

After a conversation, meeting, or event, capture structured notes and update context.

## Trigger Phrases

- "Debrief on..."
- "I just met with..."
- "I just had dinner with..."
- "Just got out of a call with..."
- `/debrief`

## Steps

### Mode A: Transcript already available
If the meeting transcript/notes have already been read or processed in this session, skip straight to analysis. Don't ask for re-explanation.

1. **Present the analysis** — structured by domain:
   - **For work meetings:** What happened, strategic implications, what you did well, what to watch for, next moves.
   - **For personal/community:** Key learnings, relationship developments, operational takeaways.

2. **Then do context routing** (Step 4 below) — if not already done during transcript processing.

### Mode B: No transcript — raw notes from you
1. **Listen** — Let the raw notes come through. Don't interrupt.

2. **Extract and structure:**
   - **Key facts** — Names, companies, numbers, dates, decisions
   - **Action items** — Things you committed to or need to do
   - **Open questions** — Unresolved items or things to think about
   - **Emotional read** — How you're feeling about it (if shared)

3. **Confirm:**
   > "Here's what I captured: [summary]. Anything I missed?"

4. **Auto-Route Context Updates (DO THIS EVERY TIME)**

   After confirmation, immediately update all affected files:

   ### People files
   - Update `/llm-context/people/[name].md` for every person discussed — add new relationship history entry with date, key details, and next steps
   - If a person doesn't have a profile yet, create one using `/skills/templates/people-template.md`

   ### Domain context
   - Update the relevant `/llm-context/` domain files with new facts, decisions, or status changes
   - Use the Context Routing table in CLAUDE.md to identify which files to update

   ### Tasks
   - Create task files for all action items in `/tasks/`
   - If this debrief resolves an existing task, archive it
   - If existing tasks are affected (blocked, unblocked, changed scope), update them

   ### Index files
   - Update any `index.md` files in affected directories

   ### Report
   End with a brief summary:
   ```
   **Context updated:**
   - Updated people/jane-doe.md (added today's meeting notes)
   - Updated work/index.md (new project timeline)
   - Created task: follow-up-with-jane.md (due next Friday)
   - Archived task: schedule-sync.md
   ```

## Guidelines

- Don't ask for re-explanation of things already shared — work with what's given, infer what you can
- If a person is mentioned, check `/llm-context/people/` for existing context
- Bias toward creating tasks — if something sounds actionable, make it a task
- Keep summaries direct, not polished — this is operational, not a blog post
- **Don't ask "should I update context?"** — just do it and report what changed
