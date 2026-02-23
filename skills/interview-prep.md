---
name: interview-prep
description: Assembles company research, question prep, and positioning for an upcoming interview. Use when you say 'Prep me for [company] interview'.
---

# Skill: Interview Prep

**Trigger:** "Prep me for [company] interview"

## Instructions

1. Check if a company file exists in your job search context
   - If yes, load it
   - If no, create a stub and research the company
2. Load your professional context and background
3. Load your job search context

## Research Company (if needed)

- Company mission and product
- Recent news/funding
- Key leadership
- Product/technical challenges they likely face
- Why you're a fit

## Prep Output

### Company Overview
[Brief summary]

### Likely Interview Focus Areas
- [Based on role and company stage]

### Your Relevant Experience
- [Mapped from professional context]

### Questions They May Ask
1. [Question] -- [Suggested angle]
2. ...

### Questions You Should Ask
1. [Question] -- [Why it's good]
2. ...

### Potential Red Flags to Address
- [If any gaps or concerns, how to handle]

## Auto-Route Context Updates (after prep)

After generating the prep, immediately:

### Company file
- Create or update the company file with all research findings, interview date, role details, and prep notes

### People files
- Create profiles for any interviewers or contacts mentioned -- name, title, and any context that helps prepare

### Tasks
- Create a task for interview follow-up (thank you note, next steps)
- Check if existing job-search tasks are affected

### Report
```
**Context updated:**
- Updated [company].md (added interview prep, date)
- Created people/[interviewer].md
- Created task: [company]-interview-followup.md
```
