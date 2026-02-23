---
name: landing-page-critique
description: Structured evaluation of a landing page using CRO and conversion best practices. Scores each section and provides a prioritized action list. Use when you say '/critique' or 'Review the landing page'.
---

# Landing Page Critique

Structured critique framework for evaluating landing pages. Combines CRO best practices, newsletter-specific conversion patterns, and design craft standards.

## When to Use

- "Critique this page", "Review the landing page", "What's wrong with this page"
- After building or updating a landing page
- Before launch to catch conversion killers
- Triggered by `/critique`

## How to Run

1. Read the landing page code (all relevant files: page, layout, styles, components)
2. If a dev server is running, note the URL so you can view alongside
3. Run through all sections below in order
4. Score each section (Pass / Needs Work / Fail)
5. End with a prioritized action list

---

## Section 1: The 5-Second Test

If someone lands on this page and skims for 5 seconds, can they answer:

- [ ] **What is this?** (product/service category is immediately clear)
- [ ] **What do I get?** (value proposition is in the headline or subhead)
- [ ] **What do I do?** (CTA is visible without scrolling)

If any of these fail, nothing else matters. Fix these first.

## Section 2: Above the Fold

| Element | Check | Notes |
|---------|-------|-------|
| **Headline** | Benefit-driven, not clever-for-clever's-sake? | Best formula: benefit + specificity |
| **Subhead** | Expands on headline, sets expectations? | Should answer: what, how often, for whom |
| **CTA** | Visible, single action, high contrast? | One form field (email). One button. Nothing else competing. |
| **Microcopy** | Reduces friction under CTA? | "Free. No spam. Unsubscribe anytime." |
| **Social proof** | Subscriber count, logos, or testimonial? | Even a small number outperforms zero |
| **Visual noise** | Anything competing with the CTA? | Navigation links, multiple buttons, animations -- all conversion killers |

## Section 3: Value Proposition Clarity

- [ ] **Can you explain what this is in one sentence?**
- [ ] **Is the benefit to the reader obvious, or is it about the brand?**
- [ ] **Does the page answer "why should I trust you?"**
- [ ] **Is there a content preview or sample?**

## Section 4: CTA & Form Design

| Check | Pass Criteria |
|-------|---------------|
| **Single field** | Email only. Name field reduces conversions 10-25%. |
| **Button contrast** | CTA button is the highest-contrast element on the page |
| **Button text** | Action verb ("Subscribe", "Get the newsletter", "Join free") |
| **Loading state** | Button shows feedback during submission |
| **Success state** | Clear confirmation after signup |
| **Error state** | Inline validation, helpful message |
| **Mobile tap target** | Button is at least 44px tall |

## Section 5: Below the Fold

- [ ] **Does it reinforce, not repeat?**
- [ ] **Value props are scannable?** Short headlines + one-sentence descriptions.
- [ ] **Second CTA present?** Don't make people scroll back up.
- [ ] **No navigation leaks?** Every link that isn't the CTA is an exit.

## Section 6: Design Craft

| Check | Pass Criteria |
|-------|---------------|
| **Typography hierarchy** | Clear distinction between H1, subhead, body, microcopy |
| **Color discipline** | One accent color max. Used only on CTA and interactive elements. |
| **Whitespace** | Generous spacing around hero content |
| **Line length** | Body text 65-75 characters per line |
| **Responsive** | Test at 375px, 768px, 1024px, 1440px |
| **Consistent spacing** | Follows an 8px grid |

## Section 7: Trust & Credibility

- [ ] **Social proof present?**
- [ ] **Specificity over abstraction?**
- [ ] **No broken promises?**
- [ ] **Professional finish?**

## Section 8: Technical Performance

- [ ] **Page load < 3 seconds** on mobile
- [ ] **No layout shift** (CLS)
- [ ] **Images optimized** -- WebP, proper sizing, lazy loading
- [ ] **Meta tags complete** -- title, description, OG tags
- [ ] **Favicon set**

## Section 9: Conversion Killers (Red Flags)

1. **No social proof** -- even a small number outperforms zero
2. **Clever headline over clear headline**
3. **Multiple CTAs competing** -- decision paralysis
4. **No content preview** -- highest-leverage trust builder
5. **Generic stock imagery** -- worse than no imagery
6. **Missing mobile optimization**
7. **No success state**
8. **Asking for too much** -- every extra field = drop-off
9. **Navigation bar with links** -- every link is an exit

---

## Output Format

```
## Landing Page Critique: [Page Name]

### Score Summary
| Section | Score |
|---------|-------|
| 5-Second Test | Pass / Needs Work / Fail |
| Above the Fold | ... |
| Value Proposition | ... |
| CTA & Form | ... |
| Below the Fold | ... |
| Design Craft | ... |
| Trust & Credibility | ... |
| Technical Performance | ... |

### Top 3 Issues (Fix First)
1. [Highest impact issue]
2. [Second highest]
3. [Third]

### What's Working
- [Things to keep]

### Detailed Notes
[Section-by-section findings]
```

## Sources

- Fogg Behavior Model (motivation x ability x prompt)
- Morning Brew, James Clear, The Hustle landing page patterns
- Unbounce 49-point landing page checklist
- CXL landing page optimization research
