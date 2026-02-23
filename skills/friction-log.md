---
name: friction-log
description: Captures operational friction as it happens. Every entry is a future product feature or process improvement. Use when you say '/friction' or 'That was annoying'.
---

# Friction Log

Capture friction as it happens. Every entry is a future improvement.

## Trigger Phrases

- "Friction log"
- "That was annoying"
- "Spent too long on..."
- "I had to check three places for..."
- "This should be easier"
- `/friction`

## How It Works

When friction is mentioned, capture it immediately. Don't wait for a formal session -- the best friction logs are captured in the moment, when the frustration is fresh.

### Entry Format

Append each entry to a friction log file (create one if it doesn't exist):

```
### [Date] -- [Short description]

**Severity:** RED | YELLOW | GREEN
**Category:** [see categories below]
**Context:** [What you were trying to do]
**What happened:** [The friction -- what went wrong, what took too long, what was confusing]
**Time wasted:** [Estimate -- 5 min, 30 min, 2 hours]
**Current workaround:** [How you handled it]
**Product implication:** [What software or process could fix this]
```

### Severity (Google's Stoplight System)

- **RED** -- Would have quit if this wasn't important. Blocking or seriously painful.
- **YELLOW** -- Frustrating but manageable. Took extra time or required a workaround.
- **GREEN** -- Minor annoyance or "this could be better." Log it but don't prioritize.

### Categories

Tag each entry with one or more. Customize these to your domain:

| Category | Examples |
|----------|----------|
| `tooling` | Software issues, missing integrations, manual workarounds |
| `communication` | Coordination overhead, unclear handoffs, missed context |
| `process` | Steps that should be automated, repeated manual work |
| `information` | Hard to find data, scattered context, version confusion |
| `onboarding` | Setup friction, unclear documentation, first-time confusion |

## Capture Principles (from Stripe + Google)

1. **Arrive at the task the way a user would.** Don't skip to the ideal path -- document the real path.
2. **Nothing is too small.** "Had to copy-paste the same thing into three tools" is a valid entry.
3. **Include what works too.** Mark good experiences as GREEN. This prevents rebuilding things that already work.
4. **Be specific, not emotional.** "Spent 20 minutes finding the email because it's in Slack, not the CRM" > "Communication is a mess."
5. **Estimate time wasted.** This is how you prioritize fixes.
6. **Log in real time when possible.** The best friction logs are written in the moment.

## Roadmap Generation

After 5+ entries, you can ask: "What should I fix first?"

Sort entries by:
1. **Frequency x Time wasted** -- A 15-min friction that happens weekly beats a 2-hour friction that happened once
2. **Severity** -- RED entries get weighted higher
3. **Category clustering** -- If most entries are in one category, that's the area to fix first

## Sources

Methodology informed by:
- [Stripe: How We Use Friction Logs](https://github.com/mikeb-stripe/friction-logging-toolkit/blob/main/how-we-use-friction-logs-at-stripe.md)
- [Google's Friction Log Template](https://sites.research.google/datacardsplaybook/activities/friction-log-template.pdf) -- stoplight severity system
- [Chameleon: Friction Logs for Product Managers](https://www.chameleon.io/blog/friction-logs)
- [Resend: How We Use Friction Logs](https://resend.com/blog/how-we-use-friction-logs-to-improve-the-product) -- fresh-eyes methodology
