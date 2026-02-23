---
name: relationship-building
description: Strategic skill for building, warming, and maintaining professional relationships. Grounded in Greene, Cialdini, Voss, Grant, and Carnegie frameworks. Use when you say '/outreach' or 'Reach out to [person]'.
---

# Relationship Building

A strategic skill for building, warming, and maintaining professional relationships. Grounded in five frameworks:

- **Greene (48 Laws of Power)** -- Strategic positioning and power dynamics
- **Cialdini (Influence)** -- Persuasion mechanics and ethical application
- **Voss (Never Split the Difference)** -- Tactical communication and reading people
- **Grant (Give and Take)** -- Giving philosophy, boundaries, and long-term generosity
- **Carnegie (How to Win Friends)** -- Warmth, genuine interest, and making people feel valued

## Trigger Phrases

- "Reach out to [person]"
- "Draft a message to [person]"
- "How should I approach [person]?"
- `/outreach`

## Workflow

### Step 1: Load Context

1. Read the person's profile from `/llm-context/people/[name].md`
2. If no profile exists, ask for context and create one
3. Load the relevant domain context
4. Check `/tasks/` for any open tasks related to this person

### Step 2: Assess Relationship Stage

| Stage | Signals | Strategic Focus |
|-------|---------|----------------|
| **New contact** | Met once or never | Be memorable, lead with value, say less |
| **Warming** | 1-3 interactions, no asks yet | Give before asking, build familiarity |
| **Active** | Regular contact, mutual value flowing | Deepen mutual dependency, co-create |
| **Ask-ready** | Trust established, clear mutual benefit | Frame asks around their win, be specific |
| **Dormant** | Haven't spoken in 2+ months | Re-engage with fresh context |
| **Maintaining** | Ongoing, no immediate need | Low-touch warmth, stay visible |

### Step 3: Run the Strategic Lens

Before drafting anything, answer these questions:

**Power & Positioning (Greene)**
1. Position relative to this person -- peer, student, collaborator, leader?
2. Saying too much or too little? (Law 4: Say less than necessary)
3. Projecting confidence appropriate to what's been built? (Law 34)

**Persuasion Mechanics (Cialdini)**
4. Natural reciprocity in play -- have you given something recently?
5. Can you invoke a warm intro or social proof?
6. Shared identity to activate? (Unity: "people like us")
7. Credibility established briefly and honestly? (Authority)

**Reading the Person (Voss)**
8. What does this person actually want? (Not what they say)
9. Emotional temperature -- busy, stressed, excited, open?

**Giving Philosophy (Grant)**
10. Giving or extracting in this interaction? (Give first)
11. Is the ask a "5-minute favor" or a real commitment?
12. Could asking for advice be more powerful than asking for a favor?

**Warmth & Genuine Interest (Carnegie)**
13. Shown genuine interest in this person's work?
14. Is there a specific, honest compliment to lead with?

### Step 4: Identify the Right Move

**Give Moves** (no ask attached)
- Share something relevant to their work
- Congratulate or acknowledge something specific
- Offer help with something they're working on
- Make an introduction

**Warm Moves** (build familiarity)
- Comment on or engage with their content
- Reference a past conversation
- Invite them to something low-stakes

**Ask Moves** (request something specific)
- Ask for advice (most powerful -- activates Ben Franklin effect)
- Ask for an introduction
- Propose collaboration

**Maintain Moves** (keep the relationship warm)
- Forward something relevant with a short note
- Re-engage with fresh context after a gap
- Share an update on something they helped with (closing the loop)

### Step 5: Draft the Message

Apply `/skills/your-voice.md` for tone. Then layer in:

**Structural Principles:**
- Open with connection, not preamble
- One clear purpose per message -- don't stack asks
- Frame the ask around their benefit, not your need
- Include an easy off-ramp ("No pressure either way")
- Close with a specific, low-friction next step
- Keep it short (Law 4)

**Tactical Techniques (Voss):**
- Mirror their communication style
- Use calibrated questions: "How are you thinking about X?"
- The "No"-oriented question for bigger asks: "Would it be crazy if I suggested..."

### Step 6: Update the Person's Profile

After any interaction, update the person's profile with:

```markdown
## Relationship Status
- **Stage:** [new / warming / active / ask-ready / dormant / maintaining]
- **Last contact:** [date and what happened]
- **Next move:** [specific action with timing]
- **You have given:** [intros, content, invites, etc.]
- **They have given:** [advice, intros, opportunities, etc.]
- **Open threads:** [anything unresolved]
```

## Anti-Patterns

1. **Over-explaining in first outreach** -- Keep it short.
2. **Asking before giving** -- Always give first in new/warming relationships.
3. **Stacking asks** -- One ask per message. Period.
4. **Manufacturing scarcity or urgency** -- Only cite real constraints.
5. **Generic flattery** -- Be specific or don't.
6. **Following up too aggressively** -- One strong follow-up, then let your work speak.
7. **Underselling yourself** -- No "just a small thing I'm working on." Frame with quiet confidence.
8. **Apologizing for the ask** -- "Sorry to bother you" undermines everything.
9. **Ignoring their communication style** -- If they write two sentences, don't send four paragraphs.
10. **Treating relationships as transactions** -- Give because it's right, not because you're tracking ROI.

## The Ethical Test (Cialdini)

Before sending anything, ask:

1. **Is this true?** -- Is the scarcity real? Do I genuinely admire this?
2. **Does this benefit them too?** -- Would they be glad they responded?
3. **Would I feel comfortable if they knew my strategy?** -- If yes, it's communication. If no, it's manipulation.

If all three are yes, send it. If any is no, revise.
