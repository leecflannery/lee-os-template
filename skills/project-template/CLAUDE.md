# [Project Name]

> [One-sentence objective from SPEC.md]

## Tech Stack

- [Language/framework]
- [Key dependencies]

## Commands

```bash
# Build
[build command]

# Test
[test command]

# Lint
[lint command]

# Run
[run command]
```

## Boundaries

- **Always**: Run tests before committing. Follow PLAN.md task order. Commit after each task.
- **Ask first**: Adding new dependencies. Changing project structure. Modifying the spec.
- **Never**: Skip tests. Implement without a plan. Make changes outside current task scope.

## Development Workflow

This project follows spec-driven development:

1. **SPEC.md** is the source of truth for what we're building
2. **PLAN.md** is the ordered task list — follow it sequentially
3. One task per session. `/clear` between tasks.
4. Write tests first when possible. All tests must pass before committing.
5. If the plan is wrong, update PLAN.md before continuing.

IMPORTANT: Read SPEC.md and PLAN.md before starting any work. Do not freelance beyond the current task.
