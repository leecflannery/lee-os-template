# Personal OS

This is your personal operating system for managing tasks, context, and automation with Claude Code.

<!-- FIRST-RUN DETECTION:
     If the About You section still contains "[Your name]", this is a fresh install.
     Run /skills/setup.md immediately to guide the user through interactive setup.
     Do NOT show a help wall or feature list. Just start the setup conversation. -->

<!-- ============================================================
     HOW THIS FILE WORKS

     Claude Code automatically reads CLAUDE.md at project root.
     This file is your "router" — it tells Claude:
       1. Who you are (so it has context)
       2. Where to find information (routing table)
       3. How to behave (guidelines)
       4. What workflows exist (skills)

     You can also have a global CLAUDE.md at ~/.claude/CLAUDE.md
     for instructions that apply across ALL projects. Put portable
     preferences there (communication style, hard rules) and
     project-specific routing here.
     ============================================================ -->

## About You

<!-- CUSTOMIZE: Replace this section with your own context.
     The more specific you are, the better Claude can help. -->

- **Name:** [Your name]
- **Role:** [What you do — e.g., "Product Manager at Acme Corp"]
- **Location:** [City]
- **Key context:** [2-3 sentences about what makes your situation unique — current projects, career stage, what you're building toward]

## Current Priorities

<!-- CUSTOMIZE: List your top priorities in order.
     These drive task recommendations and daily briefings.
     Update these whenever your focus shifts. -->

1. **[Primary focus]** — [Brief description of what this is and why it matters]
2. **[Second priority]** — [Brief description]
3. **[Third priority]** — [Brief description]
4. **[Fourth priority]** — [Brief description]

## Directory Structure

```
/tasks/          — Individual task files (YAML front matter)
/tasks/archive/  — Completed tasks organized by YYYY-MM
/ideas/          — Ideas and projects you're thinking about (no pressure to act)
/llm-context/    — Context files by domain (work, personal, side-project, people, etc.)
/skills/         — Reusable workflows and prompts
/research/       — Paper summaries by topic
/learning/       — Learning plans, logs, and skill development tracking
```

## Context Routing

<!-- CUSTOMIZE: Map your domains to context files.
     Add rows as you create new context areas.
     Claude uses this table to know what to load for each topic. -->

Load relevant context based on what you ask:

| If asking about... | Load... |
|-------------------|---------|
| Work, job, day-to-day role | `/llm-context/work/index.md` |
| Personal life, health, goals | `/llm-context/personal/index.md` |
| Side project | `/llm-context/side-project/index.md` |
| A specific person | `/llm-context/people/[name].md` |
| Goals, priorities | `/llm-context/goals.md` |
| Past decisions | `/llm-context/decisions.md` |
| How this OS works | `/llm-context/your-os/design-philosophy.md` |
| Writing/drafting a message | `/skills/your-voice.md` + `/skills/references/examples.md` + `/llm-context/people/[recipient].md` |
| Task prioritization, what to work on | `/llm-context/goals.md` then `/tasks/*.md` |

<!-- ADD YOUR OWN DOMAINS:
| Job search, applications, interviews | `/llm-context/job-search/index.md` |
| [Company name], role context | `/llm-context/[company]/index.md` |
| Community events, meetups | `/llm-context/community/index.md` |
-->

## Skills

Reusable workflows live in `/skills/`. When you ask for something that matches a skill, Claude reads the skill file first and follows its instructions.

<!-- CUSTOMIZE: Add your own skills as you build them.
     Skills are just markdown files with instructions. -->

| Skill | Trigger |
|-------|---------|
| `/skills/today.md` | "What's on for today?", `/today` |
| `/skills/task-recommend.md` | "What should I work on?", `/next`, "What's next?" |
| `/skills/catchup.md` | "What did I miss?", "Catch me up", `/catchup` |
| `/skills/weekly-review.md` | "How did this week go?", `/review` |
| `/skills/debrief.md` | "I just met with...", "Debrief on...", `/debrief` |
| `/skills/call-prep.md` | "Prep me for [meeting]", "Brief me on [person]", `/call-prep` |
| `/skills/incoming-comms.md` | Pasted text from an email, Slack, DM, or any communication without a specific question |
| `/skills/process-meetings.md` | Meeting transcript dropped, `/process-meetings` |
| `/skills/session-end.md` | "What did we learn today?", `/session-end` — only for sessions with significant strategic or personal content |
| `/skills/profile-update.md` | `/profile`, end of substantive session |
| `/skills/your-voice.md` | Writing any communication — emails, Slack, LinkedIn, professional messages |
| `/skills/voice-critic.md` | Automatically before outward-facing drafts. Also `/voice-critic` |
| `/skills/copywriting.md` | "Write copy for...", "Draft landing page copy", `/copywriting` |
| `/skills/landing-page-critique.md` | "Critique this page", `/critique` |
| `/skills/commit.md` | `/commit`, "Commit this", "Commit my changes" |
| `/skills/new-project.md` | `/new-project`, "Let's build X" |
| `/skills/task-create.md` | Casual mention of a task, "I need to..." |
| `/skills/task-complete.md` | "Mark [task] done", "I finished [task]" |
| `/skills/interview-prep.md` | "Prep me for [company] interview" |
| `/skills/relationship-building.md` | `/outreach`, "Reach out to [person]" |
| `/skills/pre-flight.md` | Auto on strategy sessions and multi-step deliverables |
| `/skills/friction-log.md` | "That was annoying", `/friction` |
| `/skills/paper-summary.md` | "Summarize this paper" |
| `/skills/event-checklist.md` | `/event-checklist`, "Set up a checklist for [event]" |
| `/skills/post-event.md` | `/post-event`, "How did the event go?" |
| `/skills/health.md` | "System health", "How's the OS?", `/health` |
| `/skills/setup.md` | Auto-triggered on first run when `[Your name]` placeholder detected |

## People File Template

When creating new people files, use the template at `/skills/templates/people-template.md`. All people files should have consistent structure: Basic Info table, How We Met, Context, Relationship History, Open Threads, and Notes.

## Task Format

Files in `/tasks/` use this structure:

```yaml
---
type: task | idea | bug
due: YYYY-MM-DD
tags: [domain, action-type]
status: todo | in-progress | done | blocked
---

[Description and notes]
```

## Tag Taxonomy

<!-- CUSTOMIZE: Replace these with your own domains and action types. -->

### Domains
- work
- personal
- side-project

### Action Types
- research
- write
- outreach
- build
- review
- follow-up

## Auto-Processing Triggers

These triggers fire automatically — you should never have to say "process this" or "update context."

| When you... | Automatically... |
|-------------|-----------------|
| Paste raw text from a message/email/DM without a question | Run `/skills/incoming-comms.md` — triage, draft response, update all affected files |
| Say "prep me for [call/meeting with person]" | Run `/skills/call-prep.md` — load person file, domain context, open tasks, active decisions → output briefing |
| Mention a new person by name with context | Create people file immediately from template |
| Complete work that overlaps with an open task | Archive the task and report |
| Have a substantive exchange on any topic | Update all affected context files in `/llm-context/` immediately |

## Behavioral Rules

**Full behavioral guidelines live in `/skills/behaviors.md`.** Load when context management, proactive nudges, or auto-routing questions arise.

**Key behaviors (always active):**
- Update context files in real-time after substantive exchanges — don't ask, just update and report
- Search existing context before asking for information
- Auto-create people files when new contacts are mentioned
- Auto-close tasks when work clearly completes them

## Hooks (Enforced by Shell)

<!-- Hooks are shell scripts that run automatically before or after Claude uses a tool.
     They enforce safety rules and keep the system in sync without relying on prompts alone.

     Configuration lives in .claude/settings.json. Three included hooks ship with this template:

     bash-guard.sh         — blocks destructive commands (rm -rf, force push, etc.)
     context-sync-nudge.sh — reminds Claude to check for ripple effects after context edits
     transcript-detector.sh — detects meeting transcripts and prompts processing

     OPTIONAL: If you add MCP tools for email/Slack/calendar, consider adding a send-guard
     hook that blocks outbound communication tools. You always want to send your own messages.
     See the README for an example send-guard.sh. -->

| Hook | Event | What it does |
|------|-------|-------------|
| `bash-guard.sh` | PreToolUse (Bash) | Blocks `rm -rf`, `git push --force`, etc. |
| `context-sync-nudge.sh` | PostToolUse (Write/Edit) | Nudges ripple-effect check on `/llm-context/` edits |
| `transcript-detector.sh` | PostToolUse (Bash/Write) | Detects meeting transcripts and prompts processing |

## Writing Voice

**Trigger:** Any time Claude is writing words that will come from you to another person — emails, Slack, DMs, LinkedIn, everything.

**Before every draft:**
1. Read `/skills/your-voice.md` and `/skills/references/examples.md`
2. Load the recipient's people file if one exists
3. Match register to channel (Slack DM ≠ exec email ≠ LinkedIn post)

**For high-stakes content** (LinkedIn, exec memos, outreach): run `/skills/voice-critic.md` on the draft.

## Hard Rules

<!-- CUSTOMIZE: Add your own non-negotiable rules here. -->

1. **NEVER send emails, messages, or any external communication without explicit approval.** Draft first, confirm, then you send manually.
2. **NEVER offer to send things.** You send your own messages. Claude only drafts.
3. **NEVER take actions visible to others without confirmation.** Calendar events with attendees, shared documents, external posts — always ask first.
