# Level up: persistent memory with Honcho

Your personal OS already has memory — CLAUDE.md persists across sessions, and context files accumulate knowledge over time. But there's a gap: Claude doesn't remember *patterns* about how you work, what you care about, or what it's learned about you across conversations. Every new session, it starts from the files alone.

[Honcho](https://honcho.dev) fills that gap. It's a Claude Code plugin that gives your agent persistent, cross-session memory — not just what's in your files, but learned insights about you as a person.

## What Honcho adds

| Without Honcho | With Honcho |
|---|---|
| Claude reads your files each session | Claude reads your files AND remembers patterns from past sessions |
| You have to re-explain preferences | Claude learns your preferences over time |
| Context is explicit (what you wrote) | Context is also implicit (what Claude observed) |
| Memory = your files | Memory = your files + accumulated insights about you |

Think of it this way: CLAUDE.md is what you *tell* the agent about yourself. Honcho is what the agent *learns* about you from working together.

## How to set it up

### 1. Install the Honcho plugin

In any Claude Code session, run:

```
/plugin install honcho@honcho
```

Follow the prompts to authenticate. Honcho will set up a session linked to your project.

### 2. Verify it's active

Start a new Claude Code session. You should see a Honcho banner at startup confirming the memory system is loaded.

You can also check the status:

```
/honcho:status
```

### 3. Start using it

Honcho works in the background. As you have conversations, it builds a profile of your preferences, patterns, and working style. You can also explicitly teach it:

- **Search past conversations:** Ask Claude to search for something you discussed before — Honcho enables semantic search across your session history.
- **Query what it knows:** Ask "What do you know about my preferences for X?" and Honcho will surface learned insights.
- **Save key insights:** When something important comes up, Claude can save it to Honcho's memory for future sessions.

### 4. Optional: configure for this project

Honcho automatically scopes memory to your project directory. If you use your personal OS across different folders, Honcho tracks context per project.

## When to use Honcho vs. file-based context

| Use file-based context (`llm-context/`) when... | Use Honcho when... |
|---|---|
| Information is structured and you want to read/edit it | Patterns emerge from usage over time |
| You need precise, curated context | You want Claude to adapt to your style |
| Multiple people might use the same system | Memory is personal to one user |
| You want full control over what Claude knows | You want Claude to learn autonomously |

The two systems complement each other. Files are your explicit knowledge base. Honcho is the implicit learning layer on top.

## Is Honcho required?

No. The personal OS works fully without Honcho. Your files are the primary memory system. Honcho is an enhancement — it makes the experience better over time but isn't a dependency.

If you're just getting started, set up the file-based system first (CLAUDE.md, context files, skills). Add Honcho once you're comfortable and want the agent to start learning from your patterns.

## Learn more

- [Honcho documentation](https://honcho.dev)
- [Claude Code plugins](https://docs.anthropic.com/en/docs/claude-code/plugins)
