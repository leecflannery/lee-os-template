# Build AI product sense with Claude Code

*Adapted from [How to Build AI Product Sense](https://www.lennysnewsletter.com/p/how-to-build-ai-product-sense) by Tal Raviv and Aman Khan, published in [Lenny's Newsletter](https://www.lennysnewsletter.com). Extended for Claude Code with a working personal OS template by [Lee Flannery](https://github.com/leecflannery).*

---

You're in a product meeting and someone mentions "context engineering" or "RAG" or "agent memory." You nod along. You've watched the explainers, bookmarked the diagrams, maybe even shipped an AI feature. So why does it still feel like you're faking it?

The problem isn't you. Most AI content is designed to induce FOMO, not to teach. The single most transformative habit to actually internalize these concepts is to stop using consumer AI (ChatGPT, Granola, Lovable) and start using coding agents for your real, daily, non-technical work. Strategy, prioritization, decision-making, productivity.

This guide walks you through that shift using Claude Code — Anthropic's CLI agent — and a personal operating system you can use every day. By the end, you'll have hands-on experience with the concepts behind every AI product: tool calling, RAG, agent memory, context engineering. And you'll have a working personal OS to show for it.

**Speed run (3 minutes to value):** If you cloned this template, just run `claude`. It detects the fresh install and walks you through setup conversationally — your identity, one person you work with, and a live demo. You'll be up and running in about 3 minutes. Come back and read the rest when you want to understand *why* it works.

**What we'll build together:**

| Section | What you'll learn |
|---|---|
| 1. Install + open a project | Get Claude Code running |
| 2. What you're looking at | The three components you already know |
| 3. Your first CLAUDE.md | Agent memory — how AI remembers across sessions |
| 4. Watch the tool calls | How agents take action in the world |
| 5. Build the directory structure | Your personal AI product |
| 6. Add context files | RAG — retrieval augmented generation |
| 7. Add your first skill | Progressive disclosure and tool design |
| 8. Context engineering | The constraint behind every AI product |
| 9. Model routing | Choosing the right model for the job |
| 10. MCP and external tools | Connecting agents to external services |

---

## 1. Install and open a project

If you haven't installed Claude Code yet, follow [Anthropic's official setup guide](https://docs.anthropic.com/en/docs/claude-code/overview).

**Two paths through this guide:**

- **If you cloned this template repo:** You already have the full OS structure. The guide explains what each piece does and why. Follow along as a walkthrough — when it says "create X," check whether it already exists first.
- **If you're starting from scratch:** Build each piece as you go. The guide will walk you through creating everything step by step.

Either way, open your project folder and start Claude Code:

```bash
cd ~/my-os    # or wherever you cloned/created your project
claude
```

That's it. You're inside a coding agent. No app to download, no onboarding flow. Just a terminal and an AI that can touch any file on your computer.

> **Tip:** Open this folder in [Cursor](https://cursor.com) or VS Code alongside your terminal. You'll get a visual file explorer and text editor while Claude Code handles the agent work. This is how many practitioners work — the visual editor for reading, the terminal agent for doing.

---

## 2. What you're looking at

Claude Code looks geeky. But it's just three things you've used before, combined:

1. **ChatGPT** — a conversational AI
2. **A text editor** — that reads and writes files
3. **A file explorer** — that navigates your file system

As Tal Raviv puts it: it's "AI that can touch any file on my computer."

In Cursor, these three components are visual panels on screen. In Claude Code, they're invisible — they happen through **tool calls**. When Claude Code needs to read a file, it calls the `Read` tool. When it needs to create one, it calls `Write`. When it needs to search, it uses `Glob` or `Grep`.

Here's the key difference from ChatGPT: **every action is transparent.** You see each tool call. You approve each one. You're watching an agent work, step by step.

This is why coding agents build product sense faster than chat interfaces. In ChatGPT, the magic happens behind a curtain. In Claude Code, you're watching the gears turn.

### Ask mode vs. agent mode

Cursor has a toggle: "Ask" (just chat) vs. "Agent" (take actions). Claude Code doesn't have this toggle — it's always an agent. It can always take actions. But it asks your permission first. Every tool call requires your approval unless you've configured auto-approve rules.

This turns out to be a better mental model for AI products: agents should always be *capable*, but humans should control when they *act*.

---

## 3. Your first CLAUDE.md — agent memory

Let's build something. Ask Claude Code:

```
Create a CLAUDE.md file for my personal operating system.
It should have sections for: who I am, my current priorities,
and behavior guidelines for how you should work with me.
Ask me a few questions first so you can fill it in.
```

Watch what happens. Claude Code will:
1. Ask you questions (the chat part)
2. Use the `Write` tool to create CLAUDE.md (the file part)
3. Show you exactly what it's writing (the transparency part)

You just created **agent memory**.

### What is agent memory?

LLMs are stateless. Every new conversation is a blank slate — like talking to a genius with the short-term memory of a hamster. If you want continuity, you have to engineer it.

CLAUDE.md is Claude Code's memory system. It's a markdown file at the root of your project that Claude reads automatically at the start of every conversation. Whatever you put in CLAUDE.md persists across every session.

**Let that sink in: memory is just a text file that gets loaded into every conversation.** There's no magic. No neural network remembering you. Just a file that gets prepended to the context window.

> **Pro tip:** You can also create a global CLAUDE.md at `~/.claude/CLAUDE.md`. Anything there applies across ALL your projects — portable preferences like communication style, hard rules, and behaviors you always want. Put project-specific routing in the project-level CLAUDE.md, and universal preferences in the global one.

But that also means memory has a cost. Whatever you put in CLAUDE.md takes up space in the context window for every single conversation. Too much memory, and you have less room for everything else. This is why you want to be intentional about what goes in memory (persistent, always relevant) vs. what gets loaded on demand (task-specific). We'll come back to this in section 8.

### What to put in CLAUDE.md

Things that should be in every conversation:

- **Who you are** — role, company, what you're working toward
- **Current priorities** — what matters most right now
- **How you want to work** — communication style, hard rules, behavior guidelines
- **Where to find things** — a routing table pointing to context files

Things that should NOT go in CLAUDE.md:

- Long documents or reference materials (load these on demand)
- Detailed project specs (put in context files)
- Conversation-specific instructions (just say them in the chat)

> **Try it now:** Open the CLAUDE.md that Claude just created. Read it. Edit it by hand if anything feels off. This file is yours — Claude proposes, you decide.

---

## 4. Watch the tool calls

Now let's pay attention to how Claude Code actually works. Ask it:

```
What files and folders are in this project?
Can you walk me through each tool call you used to answer that?
```

You'll see something like:
1. Claude used `Glob` or `Bash` with `ls` to list the directory contents
2. It reported back what it found

These tool calls are the same thing happening inside every AI product. When Perplexity searches the web, it's calling a search tool. When Granola summarizes your meetings, it's calling a transcription tool. When any AI agent takes action, it's calling tools.

### The agent loop

Here's the pattern behind every AI agent:

1. **The LLM decides** what action to take (read a file, search the web, edit text)
2. **The harness executes** the tool call (Claude Code runs the command on your machine)
3. **The result comes back** to the LLM (file contents, search results, success/error)
4. **The LLM decides** what to do next

The LLM can't actually run commands on your computer — it can only produce text. Claude Code is the "harness" (or "MCP client" or "agent framework") that hears what the LLM wants, uses the tool, and returns the result. Think of hiring a handyman: the LLM describes what it wants done, but it can't hold the hammer.

### Tool calling is its own skill

This is a subtle but important insight: **tool calling is a distinct skill, separate from reasoning or writing quality.** A model might be brilliant at writing but clumsy at choosing the right tool. This matters when you're evaluating models for your AI product — "smartest" doesn't always mean "best at taking action."

Try asking Claude Code:

```
List every tool available to you.
```

You'll see tools like `Read`, `Write`, `Edit`, `Glob`, `Grep`, `Bash`, `WebFetch`, and more. Most have familiar names — you've definitely read files and searched directories before. The LLM is just doing what you'd do, through tool calls instead of mouse clicks.

---

## 5. Build the directory structure

Now let's build your personal OS. Ask Claude Code:

```
Create this directory structure for my personal OS:

├── llm-context/        # Domain-specific knowledge
│   ├── work/index.md
│   ├── personal/index.md
│   └── people/
├── skills/             # Reusable workflows
├── tasks/              # Action items
│   └── archive/
└── ideas/              # Low-pressure parking lot
```

Watch Claude create each folder and file. Each `Write` tool call is the equivalent of you creating a file in Finder or File Explorer — except the agent does it in seconds.

### Why this structure?

Every personal OS needs to answer four questions:

| Question | Where it lives |
|---|---|
| What does the AI need to know? | `llm-context/` |
| What needs to get done? | `tasks/` |
| How should recurring things work? | `skills/` |
| What am I thinking about? | `ideas/` |

This is also the architecture of most AI products. Swap the names and it maps directly:

| Personal OS | AI product equivalent |
|---|---|
| `llm-context/` | Knowledge base / RAG index |
| `CLAUDE.md` | System prompt / agent memory |
| `skills/` | Tool definitions / prompt templates |
| `tasks/` | User state / action queue |

You're now the PM of your own AI product.

> **If you cloned the [Lee-OS template](https://github.com/leecflannery/lee-os-template):** This structure is already built out with example files, skills, and a fully-commented CLAUDE.md. Skip ahead to section 6 and start populating it with your own context.

---

## 6. Add context files — retrieval augmented generation (RAG)

Your directories are empty. Let's fix that. Ask Claude Code:

```
Ask me about my current work situation — role, company, what
I'm focused on — and create a context file at
llm-context/work/index.md with what I tell you.
```

Now ask:

```
What's in this project? Explain it to me as a product manager.
```

Watch what happens. Claude Code will **search your project files** before answering. It reads your CLAUDE.md, looks at the directory structure, opens the context files you just created, and synthesizes an answer grounded in your actual content.

**This is RAG — retrieval augmented generation.** Despite the technical name, you've been doing it your whole life. Before answering a hard question, you look things up. Agents do the same thing.

RAG is a fancy term for "before I start talking, I go look everything up and read it first." Whether it's Perplexity searching the web, Google AI Mode pulling sources, or Claude Code searching your project files — it's all the same pattern: pull in relevant documents, then generate a response grounded in those documents.

### RAG vs. memory

Here's a key distinction for AI product sense:

| | Memory (CLAUDE.md) | RAG (context files) |
|---|---|---|
| **When it loads** | Every conversation, automatically | On demand, when relevant |
| **Cost** | Always uses context window space | Only uses space when retrieved |
| **Best for** | Identity, priorities, rules, routing | Domain knowledge, project details, people |
| **Analogy** | Your name and address — always in your head | A textbook — you look it up when you need it |

In your personal OS: CLAUDE.md is memory. Everything in `llm-context/` is RAG.

### Try it

Add a few more context files:

```
Create a context file about my personal goals at
llm-context/personal/index.md. Ask me what I'm working
toward outside of work.
```

The more context you add, the more useful Claude becomes. But there's a limit — which brings us to section 8.

---

## 7. Add your first skill — progressive disclosure

Skills are reusable workflows. Instead of giving Claude the same instructions every time, you write them once as a markdown file and trigger them with a phrase.

Ask Claude Code:

```
Create a skill file at skills/today.md.
It should be a daily briefing workflow that:
1. Reads my goals from llm-context/goals.md (or CLAUDE.md)
2. Checks tasks/ for anything due today or overdue
3. Gives me a short summary of what to focus on
4. Suggests my top 3 priorities for the day
```

Now try it:

```
What's on for today?
```

If your CLAUDE.md has a skill trigger table pointing `/today` to `skills/today.md`, Claude will read the skill file and follow its instructions. If not, add one:

```
Add a skills table to CLAUDE.md that maps "What's on for today?"
and "/today" to skills/today.md
```

### Why this matters for product sense

Skills are an example of **progressive disclosure** — a pattern where you load tools, frameworks, or instructions only when they're needed, not all at once.

This is how production AI products manage complexity. You don't load every possible tool into every conversation. You let the agent (or the user) activate what's needed. Claude Code Skills (the built-in feature) and custom skill files (like we just built) both work this way.

The tradeoff: more skills means more capability, but each loaded skill takes up context window space. Sound familiar? It's the same constraint we saw with memory. Everything competes for the same limited resource.

---

## 8. Context engineering

Every concept we've covered — memory, RAG, tools, skills — they all compete for the same finite resource: the **context window**.

The context window is the total amount of text an LLM can handle in a single conversation. It includes everything: your CLAUDE.md (memory), retrieved context files (RAG), tool definitions, conversation history, and the LLM's own responses.

When you set up AI to do its best work within its limited context window, you're doing **context engineering.**

As Andrej Karpathy put it: "The hottest new programming language is English," and context engineering is how you allocate that English across competing demands.

### What fills the window

In a coding agent like Claude Code, the context window contains:

- **System prompt / memory** — CLAUDE.md, global instructions
- **Tool definitions** — descriptions of every tool the agent can call
- **Retrieved context** — files pulled in via RAG
- **Conversation history** — everything you and the agent have said
- **The agent's reasoning** — its thinking and planning

### Feel the constraint

Try having a long conversation with Claude Code. After 20-30 exchanges, you might notice responses getting less precise, or Claude "forgetting" something you discussed earlier. This is **context rot** — performance degradation as the context window fills up.

Context rot is fuzzy. How badly you feel it depends on the task and the model. You'll notice it less in creative brainstorming and more in precision work like data analysis or complex planning.

The best way to develop intuition for context rot is to use an AI agent for tasks you genuinely care about. Notice when quality starts to drop. Try starting a fresh conversation (`/clear` in Claude Code) and see if the quality jumps back. Over time, you build a feel for how much context is "too much" — the kind of intuition that goes further than any benchmark.

### Practical context engineering

For your personal OS, context engineering means:

1. **Keep CLAUDE.md lean** — Only put what's needed in *every* conversation
2. **Use routing tables** — Point to context files instead of inlining content
3. **Start fresh conversations often** — `/clear` is a feature, not a loss. Your knowledge lives in files, not conversation history
4. **Load context selectively** — Tell Claude which files are relevant instead of loading everything

### Creative solutions (from the post)

AI engineers constantly devise solutions to context limits:

- **Progressive disclosure** — Pull in tools or instructions only when needed (like our skills system)
- **Subagents** — Spawn a new conversation for a subtask, return only the summary to the main thread. The main context stays clean.
- **Summarization** — When you near the context limit, summarize the conversation so far and start fresh. (You've probably done this yourself in long ChatGPT threads.)
- **Tool condensation** — Combine multiple tools into fewer, smarter ones so tool definitions take up less space

These strategies let agents break out of the zero-sum game of context limits. This is where AI engineering gets creative — and no one has fully figured it out yet.

---

## 9. Model routing

Not all models are equal, and "smartest" doesn't mean "best for every task."

Claude Code defaults to a specific model, but production AI products choose models strategically. Here's a practical framework:

| Task type | Best model for it | Why |
|---|---|---|
| Quick file edits, formatting, simple lookups | Faster/cheaper model (Haiku, Sonnet) | Speed matters more than depth |
| Complex writing, nuanced analysis, strategic thinking | Frontier model (Opus) | Quality of reasoning matters |
| Long context, lots of files | Large context window model (Sonnet 1M) | Needs to hold more information |

In a personal OS, you can encode this as a routing principle in CLAUDE.md:

```markdown
## Model routing

- Assembly work (file ops, formatting, simple drafts): work directly
- Judgment work (strategy, analysis, ambiguous decisions): use the strongest model available
```

The deeper lesson: there are only a few frontier LLMs, and they're available to all product teams. Innovation isn't which model you use — it's how you apply it. Make a habit of trying different models for tasks you care about. Over time, you'll develop genuine opinions about model tradeoffs — the kind of intuition that's hard to get from benchmarks alone.

---

## 10. MCP and external tools

So far, our agent only works with local files. But the most valuable data often lives in external services — your calendar, email, project management tools, analytics platforms.

**MCP (Model Context Protocol)** is a standard that lets LLMs interact with external services. Think of it like USB or Bluetooth — instead of each service building a separate integration for each AI tool, they build one MCP connector that works everywhere.

For your personal OS, MCP can connect Claude Code to:
- **Google Calendar** — check your schedule, create events
- **Gmail** — search and read emails
- **Google Drive** — access documents
- **Linear, Notion, Jira** — pull in project data
- **Amplitude, Mixpanel** — query analytics

Most agent tools aren't MCP — just like most electrical wires aren't USB plugs. MCP is just another tool the agent can use, with a standardized interface.

Setting up MCP servers is beyond the scope of this quick start, but the concept matters for product sense: **the value of an agent scales with what it can access.** A personal OS that can see your files, your calendar, your email, and your tasks is dramatically more useful than one that only sees a folder.

One concrete next step: [Honcho](https://honcho.dev) is a Claude Code plugin that gives your agent persistent memory across sessions — not just what's in your files, but patterns it learns about how you work. See [setup/honcho.md](setup/honcho.md) to set it up. It's a good first taste of what external tool integration adds to an agent.

---

## What you've built

If you've followed along, you now have:

- A personal OS with context files, skills, and tasks
- CLAUDE.md as persistent agent memory
- Hands-on experience with RAG, tool calling, context engineering, and model selection

More importantly, you can now decompose any AI product into familiar building blocks. A meeting assistant that writes personalized summaries. A support bot that searches your docs before answering. A coding tool that navigates your entire codebase. You can ask yourself: *how would I build that with what I now know?*

The magic is still delightful — just without the mystique.

---

## Next steps

1. **Use it daily.** The system gets better the more you use it. Start with "What's on for today?" each morning.
2. **Add context as you go.** After meetings, paste your notes. After decisions, update the relevant file. Knowledge compounds.
3. **Build skills from repetition.** If you give Claude the same instructions twice, make it a skill file.
4. **Add persistent memory with Honcho** (optional). Your file-based system is the foundation, but [Honcho](https://honcho.dev) adds a learning layer — Claude remembers patterns about how you work across sessions. See [setup/honcho.md](setup/honcho.md) for instructions.
5. **Share what you learn.** If you build something cool with this, share it. The best personal OS ideas come from seeing how others use theirs.

---

## Credits

This guide is adapted from [How to Build AI Product Sense](https://www.lennysnewsletter.com/p/how-to-build-ai-product-sense) by **Tal Raviv** and **Aman Khan**, published in **[Lenny's Newsletter](https://www.lennysnewsletter.com)**. The original post teaches these concepts through Cursor; this version translates them for Claude Code.

The personal OS template is based on a system built and battle-tested over months of daily use. Inspired by the "How I AI" podcast and the plain-text productivity tradition.

Also shared with the [BSOTA collective](https://github.com/bsota/collective) — Building the State of the Art.
