---
name: setup
description: Guided onboarding for a fresh personal OS install. Auto-triggered when CLAUDE.md still has [Your name] placeholders. Walks the user through 3 steps in under 5 minutes, teaching the system by using it.
---

# First-Run Setup

This skill runs once — when the OS is a fresh install. After setup, the placeholders are gone and this never triggers again.

## Before You Start

1. **Detect the user's platform** from the environment (darwin = macOS, linux = Linux, win32 = Windows).
2. Set the dictation shortcut:
   - **macOS**: Press 🌐 (Globe key) twice, or Fn twice
   - **Windows**: Press Win + H
   - **Linux**: Varies by desktop environment (GNOME: enable in Settings → Accessibility)

## Opening Message

Keep it short. No explanation of what a "personal OS" is. No feature list. Get moving immediately.

```
Hey — this is a fresh personal OS. I'll set it up with you in about 3 minutes.

This works best as a conversation — you can dictate instead of typing.
[Insert platform-specific dictation shortcut here.]

What's your name, what do you do, and what are you focused on right now?
```

## Step 1: Identity (teaches: CLAUDE.md routing)

**After they answer:**

1. Update the `## About You` section of `CLAUDE.md`:
   - Replace `[Your name]` with their actual name
   - Replace `[What you do]` with their role
   - Replace `[Key context]` with what they shared
   - Write naturally — don't force their words into the template's exact fields. Capture what matters.

2. Update the `## Current Priorities` section:
   - Extract priorities from what they said
   - If they mentioned specific projects, use those
   - If they were vague, use broad domains (e.g., "Work — [role description]", "Side project — [what they mentioned]")
   - Leave a few placeholder slots — they'll fill these naturally over time

3. **Tooltip** (one sentence, no more):

```
Got it — I saved that to your system file. I read this at the start of every session, so I always know who you are and what you're working on.

Tell me about one person you work with regularly — a colleague, collaborator, anyone. What's their name and how do you work together?
```

## Step 2: One Person (teaches: relationship graph)

**After they describe someone:**

1. Create a people file at `llm-context/people/[first-last].md` using the template at `/skills/templates/people-template.md`
2. Fill in what they shared — name, title, company, relationship, context, how they work together
3. Don't ask for fields they didn't mention — fill in what you have, leave the rest for later

4. **Tooltip** (one sentence, then the demo prompt):

```
Created a profile for [Name] at llm-context/people/[name].md. Any time you mention [Name], I'll load their context automatically.

Now try the system — pick one:
- "Prep me for a call with [Name]"
- "Draft a message to [Name] about [something relevant to their priorities]"
- "What should I work on today?"
```

## Step 3: The Aha Moment (teaches: the system working)

**When they pick one:**

Execute the request using the context you just collected. This is the first time they see the system work on their real data.

- **"Prep me for a call"** → Run `/skills/call-prep.md` using their priorities + the person's profile
- **"Draft a message"** → Run `/skills/your-voice.md` (note: no writing samples yet, so use a professional default tone and mention this in the graduation)
- **"What should I work on"** → Run `/skills/task-recommend.md` using their priorities (note: no tasks yet, so recommend based on priorities and suggest creating a task)

After delivering the output, show the graduation card.

## Graduation

```
That's your OS working — I loaded your context and [Name]'s profile to [describe what just happened].

You're set up. From here, just talk about what you're working on:
- Paste any message and I'll triage it
- Mention a new person and I'll create a profile
- Tell me about a meeting and I'll debrief it
- Ask me to write something and I'll match your voice over time

The system gets better the more you use it. What are you working on today?
```

The final question — "What are you working on today?" — transitions directly into the first real work session. No ceremony. No "onboarding complete." They're already inside the system.

## After Setup

- Delete the `jane-doe.md` example people file (they now have a real one)
- Update `tasks/example-setup-os.md`: the first two items ("Clone the repo" and "Fill in CLAUDE.md About You section") are already pre-checked. Check off "Add my current priorities to CLAUDE.md" (done in Step 1) and "Add 2-3 people files for key contacts" → change to partial (1 of 2-3 done). Leave the rest — they'll complete those naturally over time and learn the task system by watching items get checked off.

## Important Guidelines

- **Never lecture.** Every tooltip is one sentence. The system teaches itself by working.
- **Don't explain the architecture.** They don't need to know about routing tables, skill files, or hooks. They'll learn these through progressive unlocks over time.
- **Stay warm but brief.** This is a conversation, not a tutorial.
- **If they give short answers**, that's fine. Work with what you get. Don't push for more detail — they'll add context naturally over time.
- **If they want to skip a step**, let them. The system works with any amount of context. Even just a name and role in CLAUDE.md is enough to start. If they skip Step 2 (no person created), adjust Step 3 options to exclude person-dependent ones — offer "What should I work on today?" as the primary demo instead.
