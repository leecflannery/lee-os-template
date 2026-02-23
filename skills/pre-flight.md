---
name: pre-flight
description: Alignment check before complex work. Prevents jumping to output when the approach is ambiguous. Auto-triggers on strategy sessions, multi-step deliverables, and open-ended requests.
---

# Pre-Flight Protocol

## When This Fires

**Automatically trigger on:**
- Strategy sessions (career positioning, project direction, stakeholder navigation)
- Multi-step deliverables (LinkedIn profiles, exec memos, event copy, outreach)
- Content creation where voice/positioning matters
- Any request where multiple valid approaches exist
- Requests that span multiple domains or context files
- Requests like "help me think through," "let's figure out," or open-ended strategic questions

**Do NOT trigger on:**
- Simple file updates (update this people file, add this to context)
- Task management (create task, archive task, what's next)
- Quick lookups (what's on my calendar, what did we discuss with X)
- Incoming comms triage (has its own workflow)
- Meeting processing (has its own workflow)
- Single-file edits with clear instructions
- Specific, unambiguous instructions ("change the heading to X")

**The test:** If you could reasonably start executing two different ways and both seem valid, run pre-flight. If there's only one obvious way to do the work, just do it.

## The Protocol

### Step 1: Restate (1-2 sentences)
State back what you think is being asked for. Be specific -- not "you want help with the project" but "you want to draft the sponsor outreach email for the next event, targeting AI tool companies."

### Step 2: Identify Stage
Which workflow phase does this belong to?
- **Exploration** -- Figuring out what to think. Don't produce deliverables.
- **Spec/Planning** -- Knows what's wanted. Produce a plan or framework for approval.
- **Execution** -- Plan is approved. Build the thing.
- **Review/Refinement** -- Draft exists. Iterate on it.

Say which stage you think this is. If exploration mode and you jump to execution, that's exactly the friction this skill exists to prevent.

### Step 3: Context Scan (show your work)
List the files you'll load before starting:
```
Loading:
- /llm-context/[relevant domain]/index.md
- /llm-context/people/[contact].md (if exists)
- /skills/your-voice.md (outbound communication)
```

If unsure which files are relevant, say so and ask.

### Step 4: Proposed Approach (3-5 bullets)
How you plan to tackle this. Be concrete enough that a wrong direction can be spotted before going down it.

### Step 5: Flag Assumptions
State anything you're assuming that might be wrong:
```
Assumptions:
- This is a cold outreach, not a warm intro
- Target budget is $X
- Want to send this week
```

### Step 6: STOP

Say: **"Ready to proceed with this approach?"**

Do not write a single line of the deliverable until approved, feedback given, or redirected.

## If Redirected

When the approach is corrected or direction changes:
1. Acknowledge the correction specifically ("Got it -- this is exploration, not execution")
2. Re-run the relevant steps with the updated understanding
3. Do NOT try to salvage work from the wrong direction
4. Do NOT say "I was just about to suggest that" -- own the miss cleanly

## If Told "Just Do It"

Sometimes speed matters and pre-flight should be skipped. That's fine. But if the request is genuinely ambiguous and you're guessing, say so: "I can skip pre-flight but I want to flag that I'm making an assumption about X -- is that right?"

## Time Budget

Pre-flight should take 30 seconds to read, not 3 minutes. Keep each step to 1-3 lines. This is an alignment check, not a planning document.
