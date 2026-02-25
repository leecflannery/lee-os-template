---
name: import-chats
description: Imports and organizes LLM chat history (Claude.ai, ChatGPT, etc.) into the OS directory structure. Classifies conversations by topic using heuristics + API, creates project directories, and writes conversation files.
---

# Import Chats

Import the user's LLM chat history into organized, searchable project directories.

## Trigger Phrases

- "Import my chats"
- "Organize my chat history"
- `/import-chats`

## Prerequisites

Before starting, confirm with the user:

1. **Exported chat data** exists in `llm-context/chats/` (unzipped)
2. **Python 3 venv** is set up with `anthropic` installed
3. **`ANTHROPIC_API_KEY`** is set as an environment variable

If any are missing, tell the user what's needed and point them to the README Quick Start step 3 for instructions.

## Steps

### 1. Load and inspect the export

- Read `llm-context/chats/conversations.json` — this is the main file
- If `projects.json` exists, read it too — extract project names, descriptions, prompt templates, and attached docs
- Count total conversations, filter out empty ones (no messages or no human messages)
- Report: "Found N conversations (M empty, skipping those)."

**Claude.ai format:** Array of objects with `uuid`, `name`, `chat_messages[].text`, `chat_messages[].sender`

**ChatGPT format:** Array of objects with `conversation_id`, `title`, `mapping` (nested dict of message nodes). Adapt the loader — classification logic is the same.

### 2. Define categories with the user

- Ask the user what domains/projects they expect to find in their history
- Propose a category structure based on their answer. Categories should be **purpose-driven** (why they had the conversation, not just the topic)
- Common top-level categories: `course-material/`, `job-interviews/`, `personal/`, `portfolio/`
- Sub-categories emerge from the data — don't over-specify upfront
- Get user approval on the category list before proceeding

### 3. Classify — Pass 1: Heuristic matching

Write keyword rules that map conversations to known categories. For each conversation, build a text block from the title (lowercased) + first 2 human messages, then match against keyword patterns.

- Assign confidence 4-5 for heuristic matches
- Good for: named entities (companies, courses, people), document references, explicit topic mentions
- Report match count: "Heuristics matched N of M conversations."

### 4. Classify — Pass 2: LLM classification

For every unmatched conversation, call the Anthropic API (Haiku model) with this prompt structure:

```
Classify this conversation into exactly one category.

CONVERSATION TITLE: {title}
FIRST HUMAN MESSAGES:
{first 1-2 human messages, truncated to ~500 chars each}

CATEGORIES (pick exactly one):
- category/subcategory: Description of what belongs here
- ...

Respond with ONLY a JSON object:
{"category": "...", "confidence": N, "reason": "brief reason"}

confidence: 1=very unsure, 2=somewhat unsure, 3=reasonable guess, 4=fairly confident, 5=very confident
```

- Strip markdown code block wrappers before parsing JSON responses
- Save results progressively — don't lose work if the script crashes partway through

### 5. Classify — Pass 3: Surface ambiguous conversations

Flag conversations where confidence <= 3. If that yields > 50, tighten to confidence < 3.

Present flagged conversations in a table for the user to confirm or reassign:

```
| # | Title | Auto-category | Confidence | Reason |
```

Apply the user's manual corrections.

### 6. Save classification results

Write the full classification to a JSON file (e.g., `scripts/classification_results.json`):

```json
{
  "metadata": {
    "total_conversations": 371,
    "heuristic_matches": 54,
    "api_matches": 316,
    "ambiguous_count": 33
  },
  "classifications": {
    "conversation-uuid": {
      "name": "Conversation title",
      "date": "2026-01-15",
      "msg_count": 12,
      "category": "category/subcategory",
      "confidence": 5,
      "reason": "Reason for classification",
      "method": "heuristic | api | manual"
    }
  }
}
```

### 7. Create directories and write files

For each category, create:

```
category-name/
├── index.md
├── conversations/
│   └── YYYY-MM-DD-slug.md
└── docs/
```

**`index.md`** — Pull from `projects.json` if available: project name, description, prompt template, list of attached docs.

**Conversation files** — Named `YYYY-MM-DD-slug.md`:

```markdown
# Conversation Title

**Date:** YYYY-MM-DD
**Messages:** N

## Human

First human message...

## Assistant

First assistant response...
```

**Attached docs** — Write text/markdown docs directly to `docs/`. For PDFs, surface filenames and paths so the user can move them manually.

### 8. Create people files

If conversations reference specific people (partners, colleagues, mentors), create people files using the template at `skills/templates/people-template.md`. Extract what you can from the conversations: name, relationship type, key dates, context, communication style.

### 9. Clean up and verify

1. Move project directories to the correct level in the OS hierarchy (root level, alongside `ideas/`, `learning/`, etc.)
2. Remove demo/placeholder directories if no longer needed
3. Update `CLAUDE.md` context routing table with new top-level directories
4. Verify all conversations are accounted for — compare total written vs. total in export
5. Report final summary to the user

## Scripts

Two Python scripts support this workflow and live in `scripts/`:

| Script | Purpose |
|--------|---------|
| `classify_conversations.py` | 3-pass classification (heuristic → API → ambiguity flagging) |
| `create_directories.py` | Directory creation, conversation file writing, metadata migration |

These are specific to the Claude.ai export format. For other platforms, reuse the classification logic and adapt the data loader.

## Guidelines

- Skip empty or unnamed conversations — they add noise with no value
- Don't pre-define every sub-category — let clusters emerge from classification results
- Use Haiku for classification — it's a simple task, no need for a frontier model
- Always get user approval on the category structure before classifying
- Save classification results to disk so work isn't lost
- After writing files, report what was created so the user can verify
