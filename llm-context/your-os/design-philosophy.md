# Design Philosophy

Why the system works this way, and the principles that should guide how you extend it.

---

## Core Insight

Traditional AI chat relies on conversation history. This system inverts that:

- Context lives in **files**, not memory
- `/clear` is a **feature**, not a loss
- Claude reads what it needs, when it needs it
- Knowledge **compounds** in the right places

The conversation is ephemeral. The knowledge persists in files.

---

## Foundational Principles

### 1. Claude as Operating System, Not Chat History

You're not having a conversation with Claude. You're running an operating system where Claude is the execution engine. CLAUDE.md is the boot sequence. Context files are the filesystem. Skills are the programs.

### 2. Knowledge Lives Where It's Relevant

No central brain dump. No session logs. Information goes into the domain where it belongs:
- Work learnings go to `/llm-context/work/`
- Project decisions go to `/llm-context/[project]/`
- People context goes to `/llm-context/people/`

This means you find things by **topic**, not by "when did we talk about this?"

### 3. Minimal Structure, Maximum Flexibility

No database. No dependencies. No app. Just markdown files with conventions:
- YAML front matter for metadata
- Folder structure for organization
- Trigger phrases for workflows

Works with any text editor. Portable. Version-controllable.

### 4. The System Updates Itself

After every substantive exchange, Claude updates the relevant context files. You talk, the system routes. You shouldn't have to manage the system — the system manages itself through the behavior guidelines in CLAUDE.md.

---

## Key Design Decisions

### CLAUDE.md as the Router

A single file at project root that Claude reads first. Contains: who you are, current priorities, routing table ("if asking about X, load Y"), skill triggers, and behavior guidelines.

**Why:** Claude Code automatically reads `CLAUDE.md`. By putting routing logic there, Claude knows where to look without loading everything into context.

### Context Routing Over Monolithic Context

Small, focused context files loaded on-demand — not one giant file with everything.

**Why:**
- Only load what's relevant to the current ask
- Each file stays readable and maintainable
- Claude doesn't get overwhelmed with irrelevant information
- Easy to update one domain without touching others

### Skills as Markdown Workflows

Reusable workflows live in `/skills/` as markdown files. Trigger phrases activate them.

**Why not real slash commands?**
- Markdown skills are human-readable, editable, and version-controlled
- Trigger-phrase matching is flexible enough
- No setup or configuration required
- You can read and edit skills in any text editor

### No Session Logs

Session logs are an anti-pattern for this system:
- They create another place to search
- Chronological organization forces digging through dates
- The whole point of focused context files is knowledge lives where it's relevant

**Instead:** At session end, Claude proposes updates to domain context files. The session disappears; the insights persist in the right place.

### Tasks as Individual Files

Each task is a standalone markdown file with YAML front matter.

**Why:**
- Easy to search, filter, manipulate
- YAML enables structured queries (by status, tag, due date)
- Files can contain notes, context, subtasks
- No app lock-in

### External Tools Stay External

GitHub issues stay in GitHub. Calendar stays in Calendar. Don't duplicate.

**Why:**
- Avoids sync problems
- Specialized tools are better at their job
- Context files can summarize current state without duplicating
- `/tasks/` is for cross-domain or non-tool tasks

---

## How to Extend the System

### Adding a New Domain

1. Create `llm-context/[domain]/index.md`
2. Add a routing entry in CLAUDE.md
3. Start populating with context

### Adding a New Skill

1. Create `skills/[skill-name].md` with instructions
2. Add trigger phrases to the skill trigger table in CLAUDE.md
3. Use it naturally in conversation

### Adding People

Just mention someone new with context. Claude creates the file from the template. Or create one manually in `llm-context/people/`.

### Growing a Domain

When a domain gets complex, split into sub-files:
```
llm-context/work/
  index.md           # Overview and routing
  ai-strategy.md     # Specific sub-topic
  clients/           # Sub-folder for related context
    client-a.md
    client-b.md
```

Update the routing table in CLAUDE.md to point to the new locations.

---

## References

- Inspired by plain-text productivity traditions (todo.txt, Markdown-based PKM)
- Claude Code documentation: CLAUDE.md conventions
- The "How I AI" podcast (origin of the "files over memory" insight)
