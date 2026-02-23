# Personal OS for Claude Code

A personal operating system that turns Claude Code into a persistent, context-aware assistant that knows your work, your people, and your priorities—across every session.

## What This Is

Most people use Claude Code as a chat window. You type, it responds, you close the tab, and everything evaporates.

This template inverts that. Your context lives in **files**, not conversation history. Every session starts by reading what matters. Every session ends by writing back what changed. Knowledge compounds. `/clear` is a feature, not a loss.

The result: Claude that remembers your goals, knows your colleagues, tracks your tasks, writes in your voice, and gets better the more you use it. You're the PM of your own AI product.

### What a morning looks like

You open your terminal and say "What's on for today?" Claude reads your goals, scans your tasks, checks your calendar, and gives you a prioritized briefing — all grounded in context that's been accumulating for weeks. You paste a meeting transcript and say "debrief." Claude updates three people files, archives a task, and flags a connection to your job search. You draft a tricky email and Claude writes it in your voice because it's read your real writing samples. None of this required setup in the moment. The system already knew what to do.

## The Architecture

Five layers, each building on the last:

```
┌─────────────────────────────────────────┐
│  CLAUDE.md — The Router                 │  Claude reads this first.
│  "If asking about X, load Y"            │  Routes every question to
│                                         │  the right context.
├─────────────────────────────────────────┤
│  llm-context/ — The Knowledge Base      │  Domain-specific context
│  work/  personal/  side-project/        │  files loaded on demand.
│  people/  goals.md  decisions.md        │  Small, focused, current.
├─────────────────────────────────────────┤
│  skills/ — The Workflows                │  Reusable markdown
│  today.md  debrief.md  voice.md         │  instructions triggered
│  catchup.md  call-prep.md              │  by natural language.
├─────────────────────────────────────────┤
│  tasks/ — The Work Queue                │  Individual task files
│  task-name.md (YAML front matter)       │  with metadata. Searchable,
│  archive/YYYY-MM/                       │  filterable, archivable.
├─────────────────────────────────────────┤
│  people/ — The Relationship Graph       │  One file per person.
│  (inside llm-context/)                  │  History, context, open
│  jane-doe.md  john-smith.md            │  threads, notes.
└─────────────────────────────────────────┘
```

## Quick Start

### 1. Clone and rename

```bash
git clone https://github.com/leecflannery/lee-os-template.git my-os
cd my-os
```

### 2. Start Claude Code

```bash
claude
```

That's it. Claude detects the fresh install and walks you through setup — about 3 minutes. It'll ask who you are, what you're working on, and who you work with, then show you the system working on your real context. No manual file editing required.

### 3. Use it

After setup, just talk about what you're working on. The system learns new capabilities as you use them:

```
> What's on for today?         → morning briefing
> [paste a Slack message]      → auto-triage + draft response
> Prep me for my 2pm call      → briefing from your context + people files
> I just met with Sarah        → debrief + update everything
```

New features introduce themselves the first time you need them — tasks, voice calibration, meeting debriefs. You don't need to learn the system upfront.

## Directory Map

```
.
├── CLAUDE.md                        # The router — Claude reads this first
├── README.md                        # You're here
│
├── llm-context/                     # All context, organized by domain
│   ├── work/index.md                # Your job / primary work
│   ├── personal/index.md            # Personal life, health, goals
│   ├── side-project/index.md        # Side projects, hobbies
│   ├── people/                      # One file per person
│   │   └── jane-doe.md              # Example person profile
│   ├── your-os/
│   │   └── design-philosophy.md     # Why the system works this way
│   ├── goals.md                     # Goal hierarchy
│   └── decisions.md                 # Decision register
│
├── skills/                          # Reusable workflows as markdown (28 skills)
│   ├── today.md                     # Daily briefing
│   ├── task-recommend.md            # Next task recommendation
│   ├── catchup.md                   # What changed since last session
│   ├── weekly-review.md             # Weekly priority alignment review
│   ├── debrief.md                   # Meeting/event debrief
│   ├── call-prep.md                 # Pre-meeting briefing
│   ├── incoming-comms.md            # Comms triage + auto-route
│   ├── process-meetings.md          # Meeting transcript processing
│   ├── session-end.md               # End-of-session synthesis
│   ├── profile-update.md            # Self-model dreaming pass
│   ├── your-voice.md                # Voice calibration for writing
│   ├── voice-critic.md              # Automated voice consistency check
│   ├── copywriting.md               # Landing page and web copy
│   ├── landing-page-critique.md     # CRO and conversion critique
│   ├── commit.md                    # Git commit workflow
│   ├── new-project.md               # Spec-driven project scaffolding
│   ├── task-create.md               # Create tasks from casual mentions
│   ├── task-complete.md             # Archive completed tasks
│   ├── interview-prep.md            # Interview preparation
│   ├── relationship-building.md     # Strategic outreach
│   ├── pre-flight.md                # Alignment check before complex work
│   ├── friction-log.md              # Operational friction capture
│   ├── paper-summary.md             # Research paper summarization
│   ├── event-checklist.md           # Event lifecycle checklist
│   ├── post-event.md                # Post-event debrief and ops
│   ├── health.md                    # System audit
│   ├── setup.md                     # First-run guided onboarding
│   ├── behaviors.md                 # Detailed behavioral guidelines
│   ├── templates/
│   │   └── people-template.md       # Template for new people files
│   ├── references/
│   │   └── examples.md              # Your real writing samples
│   └── project-template/            # Template for new code projects
│       ├── CLAUDE.md
│       ├── SPEC.md
│       └── PLAN.md
│
├── tasks/                           # Active tasks (YAML front matter)
│   ├── _template.md                 # Task file template
│   └── archive/                     # Completed tasks by month
│
├── ideas/                           # Low-pressure idea parking lot
├── learning/                        # Learning plans and logs
├── research/                        # Paper summaries by topic
├── .claude/
│   ├── settings.json                # Hook configuration
│   └── hooks/
│       ├── bash-guard.sh            # Blocks destructive commands
│       ├── context-sync-nudge.sh    # Nudges ripple-effect checks
│       └── transcript-detector.sh   # Detects meeting transcripts
│
├── setup/
│   └── honcho.md                    # Optional: persistent memory with Honcho
└── .agents/skills/                  # Claude Code native skills (see note below)
```

### A note on `.agents/skills/`

This template includes Claude Code native skills in `.agents/skills/` — product management frameworks (JTBD, OKRs, positioning, growth loops, etc.) that Claude Code can invoke when doing strategic work. These are separate from the custom workflow skills in `/skills/`. You don't need to configure them — they're available automatically when Claude Code detects a relevant task. Think of `/skills/` as your personal workflows and `.agents/skills/` as professional frameworks. Delete any that aren't relevant to your work, or add your own.

## How to Make It Yours

### Start small
You don't need to fill everything in on day one. Start with CLAUDE.md and one domain. The system grows organically as you use it.

### Let context accumulate naturally
After meetings, paste your notes and say "debrief." After emails, paste them in for triage. After decisions, update the relevant context file. Over time, the system becomes a rich, searchable record of your work.

### Train your voice
Save examples of your real writing in `skills/references/examples.md`. The gap between Claude's drafts and your edits is where your voice lives. After 3-5 examples, Claude starts writing like you.

### Add domains as you need them
New project? Create `llm-context/new-project/index.md` and add a routing entry in CLAUDE.md. The system scales by adding folders, not by reconfiguring anything.

### Build skills from repetition
If you find yourself giving Claude the same instructions more than twice, write a skill file. Skills are just markdown instructions—no code required.

## Design Principles

1. **Files over memory** — Context lives in files, not conversation history. `/clear` is a feature.
2. **Route, don't dump** — Load only what's relevant. Small, focused context files beat monolithic brain dumps.
3. **Minimal structure, maximum flexibility** — It's just markdown and folders. No database, no dependencies, no lock-in.
4. **The system updates itself** — After every substantive exchange, context files get updated. You talk, the system routes.
5. **Skills over instructions** — Repeatable workflows live as readable, editable markdown. No configuration files.

### Hooks: safety rails enforced by shell

Hooks are shell scripts that run automatically before or after Claude uses a tool. They enforce rules deterministically — no amount of prompting can override a hook that blocks a command.

This template ships with three hooks:

- **`bash-guard.sh`** (PreToolUse) — Blocks destructive commands like `rm -rf`, `git push --force`, `git reset --hard`. Fires before every Bash call.
- **`context-sync-nudge.sh`** (PostToolUse) — When a file in `/llm-context/` is edited, reminds Claude to check for ripple effects in other context files.
- **`transcript-detector.sh`** (PostToolUse) — When a meeting transcript lands in the meeting-notes directory, prompts Claude to run the process-meetings skill automatically.

Configuration lives in `.claude/settings.json`. To add your own hooks, create a script in `.claude/hooks/` and register it in the settings file.

**Optional: send-guard (if you add MCP tools)**

If you connect MCP tools for Gmail, Slack, or other messaging services, add a send-guard to prevent Claude from ever sending messages on your behalf. You always want to send your own messages. Create `.claude/hooks/send-guard.sh`:

```bash
#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty')

BLOCKED_PATTERNS=('send_gmail' 'send_message' 'send_email' 'send_chat' 'create_message')

for pattern in "${BLOCKED_PATTERNS[@]}"; do
  if echo "$TOOL_NAME" | grep -qi "$pattern"; then
    echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"deny\",\"permissionDecisionReason\":\"BLOCKED: Draft messages in-conversation only. You send your own messages.\"}}"
    exit 0
  fi
done
exit 0
```

Then register it in `.claude/settings.json` under `PreToolUse` with an empty matcher (matches all tools).

### Add persistent memory with Honcho

Your file-based system handles explicit context — what you write down. [Honcho](https://honcho.dev) adds implicit context — what Claude learns about you from working together. It's a plugin that gives Claude persistent, cross-session memory beyond what's in your files. See [setup/honcho.md](setup/honcho.md) for instructions. This is optional — the OS works fully without it.

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI installed
- A text editor (VS Code, Cursor, etc.)
- [Honcho](https://honcho.dev) plugin (optional — for persistent cross-session memory)
- That's it. The template itself has no dependencies — it's just markdown files and folders.

## Credits

Inspired by the "How I AI" podcast and the plain-text productivity tradition (todo.txt, Markdown-based PKM).

The [quick start guide](quick-start-guide.md) is adapted from [How to Build AI Product Sense](https://www.lennysnewsletter.com/p/how-to-build-ai-product-sense) by Tal Raviv and Aman Khan, published in [Lenny's Newsletter](https://www.lennysnewsletter.com).

Also shared with the [BSOTA collective](https://github.com/bsota/collective) — Building the State of the Art.

## License

MIT — take it, make it yours, share what you learn.
