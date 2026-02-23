---
name: commit
description: Generate a meaningful commit message and execute the commit. Use when you say '/commit', 'commit this', or 'commit my changes' in any project.
---

# /commit

Generate a meaningful commit message and execute the commit.

## Trigger Phrases

- `/commit`
- "Commit this"
- "Commit my changes"

## Process

### 1. Assess the working tree

Run these in parallel:
- `git status -s` -- see what's changed (modified, added, deleted, untracked)
- `git diff --stat` -- summary of staged + unstaged changes
- `git diff` or `git diff --cached` -- actual content changes (scan for what matters, skip noise)
- `git log --oneline -5` -- recent commit style for consistency

### 2. Decide what to stage

- If changes are already staged, use what's staged
- If nothing is staged, assess whether ALL changes should go in one commit or should be split
- **Split criteria:** If changes span unrelated concerns (e.g., a bug fix AND a new feature AND a refactor), recommend splitting into separate commits. Present the groupings and ask which to commit first.
- **Never stage:** `.env`, `*.private.md`, `secrets/`, credentials, large binaries, `.DS_Store`
- When in doubt about untracked files, ask once: "Include [files]?"

### 3. Write the commit message

**Format:**
```
[Short imperative title -- what changed, max 72 chars]

[Body -- 2-5 lines explaining WHY, not restating WHAT. What motivated
this change? What does it enable? What was the previous state?]

Co-Authored-By: Claude <co-author model> <noreply@anthropic.com>
```

**Title rules:**
- Imperative mood ("Add feature" not "Added feature")
- Specific -- name the thing that changed ("Slim CLAUDE.md from 284 to 122 lines" not "Update config")
- Include numbers when they tell a story (file counts, line reductions, version bumps)
- No period at the end

**Body rules:**
- Explain the motivation, not the mechanics (the diff shows the mechanics)
- If multiple things changed, use a brief list
- For large changes (20+ files), group by category
- Keep it scannable -- bullets over paragraphs

**Style calibration:**
- Match the voice and detail level of recent commits in the repo
- Small changes get short messages (title only is fine for a typo fix)
- Large changes get structured bodies

### 4. Present and confirm

Show the proposed commit message and file list. Wait for approval before executing.

```
## Proposed commit

**Files (N):**
- [grouped summary of what's being committed]

**Message:**
> [the commit message]

Stage and commit? (Or edit the message first)
```

### 5. Execute

After approval:
1. Stage the files (`git add [specific files]` -- never `git add .` unless all files were reviewed)
2. Commit with the approved message using HEREDOC format
3. Show the resulting commit hash

### 6. Push (only if asked)

**Never auto-push.** If you say "commit and push" or "push it", then push. Otherwise just commit locally. When pushing, confirm the remote and branch first if it's not obvious.

## Multi-commit workflow

When splitting changes across commits:
1. Present all proposed groupings upfront
2. Commit them one at a time, each with its own message
3. After each commit, show remaining uncommitted changes
4. Continue until clean or you say stop

## Guidelines

- **Smart, not verbose.** A one-line fix gets a one-line message. A 150-file reorg gets a structured body.
- **Why > What.** The diff already shows what changed. The message explains why it matters.
- **Consistency.** Match the repo's existing commit style.
- **No secrets.** Scan staged files for anything that looks like credentials, API keys, or private data. Flag before committing.
- **Co-author tag.** Always include the Claude co-author line with the model being used.
