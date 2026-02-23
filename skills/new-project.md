---
name: new-project
description: Scaffolds a new development project with spec, plan, and structure using the Specify > Plan > Implement > Verify workflow. Use when you say '/new-project' or 'Let's build X'.
---

# Skill: New Project

**Trigger:** "New project", "Start a project", "Let's build X", `/new-project`

## Overview

Codifies the **Specify > Plan > Implement > Verify** workflow for starting a new development project. The human decides what and why. The agent surfaces edge cases, proposes plans, and implements. Tests and git commits are the safety nets.

## Workflow

### Step 1: Brief

Describe what you want to build in 2-3 sentences. Capture:
- What it does
- Who it's for
- Why it matters right now

Don't start coding. Don't start planning. Just listen.

### Step 2: Interview

Ask clarifying questions to fill gaps. Cover:
- **Requirements**: What does "done" look like? What's the MVP?
- **Edge cases**: What happens when things go wrong?
- **Constraints**: Tech stack preferences, hosting, budget, timeline
- **Scope**: What's explicitly out of scope?
- **Dependencies**: External APIs, accounts, services needed

Keep it to 3-5 questions max -- don't interrogate.

### Step 3: Scaffold

Copy the project template and initialize:

```bash
cp -r skills/project-template/ /path/to/[project-name]/
cd /path/to/[project-name]
git init
```

Confirm the project name and location before creating.

### Step 4: Spec

Write `SPEC.md` in the project root using the template. Fill in every section based on the brief and interview. This is the source of truth for the entire project.

**Rules:**
- Use Plan Mode for this step (read-only, no code)
- You approve the spec before moving on
- If something is unclear, ask -- don't assume

### Step 5: Plan

Write `PLAN.md` -- an ordered list of atomic tasks decomposed from the spec.

**Each task must have:**
- Clear description (one sentence)
- Files to create or modify
- Tests to write
- Dependencies (which tasks must finish first)
- Verification criteria

**Rules:**
- Tasks should be completable in one session
- Tasks should be independently testable
- You approve the plan before implementation starts
- Use Plan Mode for this step

### Step 6: Execute

Implement one task at a time, in order.

**Per task:**
1. Mark the task `in-progress` in PLAN.md
2. Write tests first when possible (TDD)
3. Implement the code
4. Run tests -- all must pass
5. Commit with a descriptive message
6. Mark the task `done` in PLAN.md
7. `/clear` before starting the next task

**Rules:**
- Follow the plan. Don't freelance.
- One task per session. `/clear` between tasks.
- If a task reveals the plan is wrong, stop and revise PLAN.md first.
- If Claude has been corrected 2+ times on the same issue, start a fresh session.
- Commit after every completed task -- git is your safety net.

### Step 7: Verify

After all tasks are complete:
1. Run the full test suite
2. Self-audit: compare output against SPEC.md, flag any gaps
3. Manual review: check the code and behavior
4. If gaps exist, create new tasks and return to Step 6

## Quick Reference

| Phase | Who leads | Key artifact | Tool |
|-------|-----------|-------------|------|
| Brief | You | -- | Conversation |
| Interview | Claude | -- | Questions |
| Scaffold | Claude | Project directory | Bash |
| Spec | You + Claude | `SPEC.md` | Plan Mode |
| Plan | Claude > You approve | `PLAN.md` | Plan Mode |
| Execute | Claude > You review | Code + tests | Implementation |
| Verify | You + Claude | Passing tests + spec audit | Review |

## Principles

- **Never skip straight to code.** Spec first, always.
- **Tests are the most precise prompts.** A failing test eliminates ambiguity.
- **Git is the safety net.** Commit after every task. Roll back freely.
- **Context is finite.** `/clear` between tasks. Use subagents for exploration.
- **The plan can change.** But change it explicitly, not by drift.
