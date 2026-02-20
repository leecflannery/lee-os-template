---
name: voice-critic
description: Automatic voice consistency check for outward-facing content. Run before presenting any draft of LinkedIn posts, emails, event copy, outreach messages, or professional positioning content.
---

# Voice Critic

Self-check workflow that catches generic, corporate, or misaligned drafts before you see them.

## When to Run

Automatically before presenting any outward-facing content:
- LinkedIn profiles, headlines, posts
- Emails to external contacts
- Event copy, promotional text
- Outreach messages
- Professional positioning content (bios, about sections)

Does NOT apply to internal notes, task files, context updates, or casual messages to close peers.

## Process

### 1. Write the draft

Using `/skills/your-voice.md` principles and context from relevant domain files.

### 2. Run the critic

Evaluate the draft against these criteria:

| Check | What to flag |
|-------|-------------|
| Corporate defaults | "Synergy," "leverage," "I'm passionate about," "excited to announce," filler phrases |
| Aspirational inflation | Claiming scope you don't have, inflating titles, describing future state as current |
| Generic LinkedIn voice | Humble-brag structures, thesis statements, "Here's what I learned" framing |
| Over-hedging | "I was just wondering if maybe," excessive qualifiers |
| Performative enthusiasm | Too many exclamation points, "really great," "amazing opportunity" |
| Wrong register | Too formal for Slack, too casual for exec email, mismatch with channel |
| Credential leading | Opening with titles/degrees instead of concrete work |
| Narrating shared context | Explaining things the recipient already knows |
| Em-dash style | Spaced em-dashes (word — word) instead of unspaced (word—word) |
| Length bloat | Three paragraphs where one would do, unnecessary preamble |

<!-- CUSTOMIZE: Add your own anti-patterns as you discover them.
     The patterns above are common Claude defaults that rarely match
     anyone's actual voice. Your specific catches will be more valuable. -->

**Scoring:**
- Score: 1-10 on voice match
- Flagged lines: specific phrases that don't match, with rewrites
- Overall note: one sentence on what's off (or "clean" if nothing)

### 3. Revise or present

- **Score 7+:** Present the draft with a brief note on what was caught (if anything)
- **Score 4-6:** Revise based on critic feedback, re-check, then present both versions
- **Score 1-3:** Start over. The framing is wrong, not just the words

### 4. After edits

If significant rewriting happens, ask: "Want me to add this to the voice examples?" Follow the feedback loop in `/skills/your-voice.md`.
