---
name: profile-update
description: End-of-session synthesis that updates your self-model with explicit conclusions, deductive observations, and identity shifts. Use when you say '/profile' or at the end of a substantive session.
---

# Skill: Profile Update (Dreaming)

**Trigger:** End of any substantive session, or "Update my profile", `/profile`

**Inspired by:** Honcho/Plastic Labs' approach to AI memory -- theory of mind over fact storage, explicit + deductive conclusions, periodic "dreaming" over accumulated context.

## Purpose

Keep your profile as a living, compounding model -- not just facts, but patterns, evolving identity, and deductive insights that improve how Claude works with you over time.

## Instructions

### 1. Review the Session

Scan the full conversation for:
- **Explicit signals** -- things directly stated about preferences, feelings, goals
- **Deductive signals** -- things reasonably inferred from behavior, reactions, choices, or patterns (e.g., evaluated three options and only got excited about the one with creative ownership -- deduction: ownership and creative control matter more than title)
- **Identity shifts** -- any movement in self-perception, goals, or values
- **New information** -- facts, relationships, projects, events not already captured
- **Contradictions** -- anything that conflicts with the existing profile (important -- the profile should evolve, not calcify)

### 2. Categorize Conclusions

For each conclusion, classify as:

- **Explicit** -- Stated directly. Quote or paraphrase.
- **Deductive** -- Inferred from behavior/patterns. State the evidence.

### 3. Propose Updates

Present proposed changes before making them. Format:

```
## Profile Update Proposal

### Explicit (stated directly)
- [conclusion] > Update to: [section]

### Deductive (inferred from this session)
- [conclusion] -- Evidence: [what happened] > Update to: [section]

### Identity Shifts
- [what changed and why it matters]

### Contradictions / Corrections
- [existing profile item] conflicts with [new evidence] > Proposed resolution

### No Change Needed
- [sections that remain accurate]
```

### 4. Apply Updates

After approval (or edits), update the profile file. Key principles:

- **Deductive observations go in a dedicated section** with enough context that future sessions can validate or revise them.
- **Don't just add -- revise.** If a new insight supersedes an old one, update the old one rather than creating a growing list. The profile should be a snapshot of current understanding, not a changelog.
- **Date significant shifts.** When something meaningful changes, add a date marker so the trajectory is visible.
- **Preserve tension.** If you hold two contradictory beliefs, capture both. Don't prematurely resolve ambiguity.

### 5. Cross-Reference

Check if any session insights should also update:
- **`CLAUDE.md`** -- Current priorities, about section, context routing
- Domain context files in `/llm-context/`
- Any relevant `/llm-context/people/` files

Propose these updates alongside the profile update.

## What Makes a Good Profile

The profile is effective when it enables Claude to:
1. **Calibrate tone** -- know when to push, when to back off, when to reflect
2. **Anticipate patterns** -- recognize recurring behaviors before you have to name them
3. **Hold context across sessions** -- remember not just what was said but what it meant
4. **Evolve with you** -- the profile should reflect who you are now, not who you were months ago
5. **Support, not diagnose** -- capture patterns that help Claude work with you effectively

## Anti-Patterns

- Don't add something just because it came up once. Look for patterns across sessions.
- Don't flatten complexity. Nuanced observations are more useful than simple labels.
- Don't remove things that are uncomfortable. If a pattern is real, keep it.
- Don't update the profile without proposing changes first. You own your profile.
