---
name: copywriting
description: Writes landing page and web copy using positioning frameworks (PAS, StoryBrand, AIDA). Runs through voice critic and landing page critique before presenting. Use when you say '/copywriting' or 'Write copy for...'.
---

# Copywriting

Write landing page and web copy that converts. Starts from positioning, applies the right framework, writes in your voice, and runs through the full critique pipeline before presenting.

## Trigger Phrases

- "Write copy for..."
- "Update the site copy"
- "Draft landing page copy"
- "Write the homepage"
- `/copywriting`

## Before You Start

Load in this order:
1. Any positioning or strategy context for the product/project
2. `/skills/your-voice.md` -- voice baseline
3. The target page or component (read the existing copy first)

Know the answers to these before writing:
- **Who is this for?** (specific audience, not "everyone")
- **What would they do without this?** (competitive alternatives)
- **What's the one thing that's different?** (differentiated value)
- **What should they do next?** (the CTA)

## Framework Selection

Pick based on the copy task. Don't mix frameworks within a section -- pick one and commit.

| Framework | When to Use | Structure |
|-----------|------------|-----------|
| **PAS** (Problem-Agitate-Solve) | Landing page hero, short-form, email signup sections | Problem > Agitate > Solve |
| **StoryBrand** | Longer pages, about pages, trust-building contexts | Character > Problem > Guide > Plan > CTA > Avoid Failure > Success |
| **AIDA** | Conversion-focused sections, CTAs, signup flows | Attention > Interest > Desire > Action |

## Positioning to Copy Translation

Copy doesn't come from brainstorming -- it comes from positioning.

### Step 1: Extract from positioning

| Positioning Element | Copy Element |
|--------------------|-------------|
| Competitive alternatives (what they'd do without you) | Problem statement -- name the alternative they're stuck with |
| Differentiated value (what you do that no one else does) | Headline or subhead -- lead with the difference |
| Target market (who gets value fastest) | Voice and specificity -- speak directly to their situation |
| What you're NOT | Anti-positioning -- clarify what this isn't |

### Step 2: Write the headline from the differentiation

**Five headline formulas (pick one):**

1. **Benefit + Time** -- "Become smarter in 5 minutes" (Morning Brew)
2. **Pain validation** -- "GTM is a grind" (Pavilion)
3. **Identity** -- "The Builders' Network" (AI Tinkerers)
4. **Personalization** -- "Events matched to what you're into"
5. **Superlative** -- "The world's leading AI ecosystem" (Cerebral Valley). Don't use without proof.

**Test:** Read the headline aloud. If it could describe anything in your category, it's too generic. If it could only describe your product, it's right.

### Step 3: Write the subhead from the solution

The subhead answers: "How does this actually work?" One sentence. Specific.

## Copy Hierarchy

Standard stack for a landing page. Not every page needs all sections -- but this is the order when they appear.

### 1. Hero (Above the Fold)

| Element | Purpose | Guidelines |
|---------|---------|-----------|
| Headline | Grab attention, state value | One of the 5 formulas above. Max 10 words. |
| Subheading | Clarify the headline | One sentence. How it works or who it's for. |
| CTA | Drive action | One clear action. Visible, not buried. |
| Proof element | Build credibility | One number or social proof. |

**Rule:** A visitor should understand what this is, who it's for, and what to do next within 5 seconds.

### 2. Value Section (Below the Fold)

Answer "Why should I care?" 3-5 bullet benefits. Specific, not generic.

### 3. Social Proof

Community size, notable users, testimonials, or partner logos. Use real numbers.

### 4. How It Works

Clear path to first value. Remove friction.

### 5. CTA Zone

Multiple CTAs at different commitment levels. Each CTA gets reassurance copy: "Free. One email a week." / "No spam, unsubscribe anytime."

## Anti-Patterns

| Generic Copy | What Actually Works |
|-------------|-------------------|
| "Join our vibrant community" | Name what the community does |
| "Connect with like-minded professionals" | Be specific about who |
| "Unlock exclusive access" | Name what they get |
| "Stay ahead of the curve" | Say what they'll learn |
| "Don't miss out" | Name what they'll miss |

## Voice Integration

Write the copy first using the framework. Then pass it through your voice filter:

1. **Check against `/skills/your-voice.md`**
2. **Read the anti-patterns table** -- is Claude defaulting to corporate?
3. **The real test:** Would you actually say this out loud to someone? If not, rewrite.

## Output Format

```
COPY DELIVERABLE: [Page/Section Name]
Date: [Date]
Framework: [PAS / StoryBrand / AIDA]
Target audience: [Who]

HERO
  Headline:     [X]
  Subheading:   [X]
  CTA:          [X]
  Proof:        [X]

[ADDITIONAL SECTIONS as needed]

META/SEO
  Page title:   [X]
  Description:  [X]
  OG title:     [X]

ALTERNATIVES (for A/B consideration)
  Alt headline 1: [X]
  Alt headline 2: [X]
```

## Pipeline

After drafting copy with this skill:

1. **Run voice critic** (`/skills/voice-critic.md`) -- score must be 7+ before presenting
2. **Run landing page critique** (`/skills/landing-page-critique.md`) -- structural evaluation
3. If score < 7 or critique flags issues, revise and re-run
4. Present with copy organized by component/section

## Guidelines

- **Clarity beats cleverness.** 80% of people don't read past the headline.
- **Specificity beats generality.** Real numbers beat "a growing community."
- **One idea per section.** Don't stack multiple value props in one paragraph.
- **The customer is the hero.** Your product is the guide, not the star.
- **Name the alternative.** Naming what they'd do without you is more powerful than describing yourself.

## Sources

- [PAS Framework -- Copyblogger](https://copyblogger.com/problem-agitate-solve/)
- [StoryBrand SB7 -- Donald Miller](https://storybrand.com)
- [April Dunford -- Positioning to Copy](https://www.aprildunford.com/)
- [CXL -- High-Converting Landing Pages](https://cxl.com/blog/how-to-build-a-high-converting-landing-page/)
- [Unbounce -- Headline Formulas](https://unbounce.com/landing-page-examples/formulas-for-landing-page-headlines-with-examples/)
