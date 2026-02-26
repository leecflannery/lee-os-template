"""
Classify 371 Claude.ai conversations into project categories.

Pass 1: Heuristic keyword matching against known projects.
Pass 2: Claude API classification for unlabeled conversations.
Pass 3: Surface ambiguous ones (confidence <= 3) for manual review.
"""

import json
import re
import os
import sys
import time
from pathlib import Path

# ─── Paths ───────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent
CONVERSATIONS_PATH = BASE_DIR / "llm-context" / "chats" / "conversations.json"
PROJECTS_PATH = BASE_DIR / "llm-context" / "chats" / "projects.json"
OUTPUT_PATH = BASE_DIR / "scripts" / "classification_results.json"

# ─── Categories ──────────────────────────────────────────────────────────────

CATEGORIES = {
    "course-material/math-e142": "Math E-142 (Harvard Extension)",
    "course-material/csci-e20": "CSCI E-20 (Harvard Extension)",
    "job-interviews/intuit": "Intuit takehome / interview",
    "job-interviews/blok": "Blok interview / prep",
    "job-interviews/lyft": "Lyft interview / prep",
    "job-interviews/google": "Google interview / prep",
    "job-interviews/openai-residency": "OpenAI Research Residency",
    "job-interviews/other": "Other job interviews (Cedar, Thread AI, Chime, general DS prep)",
    "personal/relationships": "Relationships, communication, conflict",
    "personal/health": "Physical and mental health",
    "personal/spirituality": "Buddhism, zen, meditation, enneagram",
    "personal/dating": "Dating apps, dating advice",
    "personal/gabriel": "Gabriel-related",
    "personal/learning/ai-ml": "AI/ML concepts and research",
    "personal/learning/coding": "Python, SQL, git, dev tools",
    "personal/learning/general": "History, politics, general knowledge / curiosity",
    "personal/miscellaneous": "One-off questions, daily life, trivia",
    "portfolio/semantle": "Semantle project",
    "portfolio/other": "Other portfolio projects",
}


# ─── Heuristic Rules ────────────────────────────────────────────────────────

def _text_block(conv):
    """Extract title + first 2 human messages as a single text block for matching."""
    title = conv.get("name", "").lower()
    human_msgs = []
    for msg in conv.get("chat_messages", []):
        if msg.get("sender") == "human":
            human_msgs.append(msg.get("text", "").lower())
            if len(human_msgs) >= 2:
                break
    return title + " ||| " + " ||| ".join(human_msgs)


def _match(text, patterns):
    """Check if any pattern appears in text (case-insensitive)."""
    return any(p in text for p in patterns)


def heuristic_classify(conv):
    """
    Returns (category, confidence, reason) or None if no match.
    Confidence for heuristics is 4 or 5.
    """
    text = _text_block(conv)
    title = conv.get("name", "").lower()

    # ── Math E-142 ──
    if _match(text, ["math e-142", "math e142", "mml-book", "mml book"]):
        return ("course-material/math-e142", 5, "Direct mention of Math E-142 or MML book")
    if _match(title, ["chapter 4 mml", "chapter 3 mml", "chapter 2 mml", "chapter 1 mml"]):
        return ("course-material/math-e142", 5, "MML chapter reference in title")
    # MML book chapter references in messages
    if _match(text, ["mml", "mathematics for machine learning"]) and _match(text, ["chapter", "exercise", "section"]):
        return ("course-material/math-e142", 5, "MML textbook chapter/exercise reference")
    # Specific math topics that match E-142 course content
    if _match(title, ["gaussian mixture model", "pca", "dimensionality reduction"]) and _match(text, ["course", "e-142", "mml"]):
        return ("course-material/math-e142", 4, "ML math topic in course context")
    if _match(text, ["math e-142", "mathe142"]):
        return ("course-material/math-e142", 5, "Direct course reference")
    # LaTeX assignments for math course
    if _match(text, ["latex"]) and _match(text, ["assignment", "homework", "pset"]) and _match(text, ["math", "mml", "e-142"]):
        return ("course-material/math-e142", 5, "LaTeX assignment for math course")
    # "exercise N.N in the book" pattern (MML exercises)
    if re.search(r"exercise\s+\d+\.\d+\s+in the book", _text_block(conv)):
        return ("course-material/math-e142", 4, "MML textbook exercise reference")
    # Reading chapters pattern for MML
    if _match(text, ["for week"]) and _match(text, ["reading chapter", "chapter 2", "chapter 3", "chapter 4", "chapter 5"]) and _match(text, ["class notes", "homework"]):
        return ("course-material/math-e142", 4, "Weekly MML reading with homework")

    # ── CSCI E-20 ──
    if _match(text, ["csci e-20", "csci e20", "cscie20", "csci-e20"]):
        return ("course-material/csci-e20", 5, "Direct mention of CSCI E-20")
    if _match(text, ["discrete math"]) and _match(text, ["course", "harvard", "homework", "week", "class", "chapter"]):
        return ("course-material/csci-e20", 5, "Discrete math in course context")
    if _match(text, ["discrete_math_lewis_zax", "theoretical_cs_fleck"]):
        return ("course-material/csci-e20", 5, "CSCI E-20 textbook reference")
    # Week notes for discrete math
    if _match(title, ["week "]) and _match(text, ["discrete", "number theory", "proof", "prime"]):
        return ("course-material/csci-e20", 4, "Weekly notes on discrete math topics")
    # Specific discrete math topics
    if _match(title, ["infinitely many primes", "associativity of congruence", "composite numbers with prime",
                       "factoring difference of squares", "finding zeros of quadratic"]):
        return ("course-material/csci-e20", 4, "Discrete math / number theory topic")
    if _match(text, ["week 4 discrete math"]):
        return ("course-material/csci-e20", 5, "CSCI E-20 week reference")

    # ── Intuit ──
    if _match(text, ["intuit"]):
        return ("job-interviews/intuit", 5, "Direct mention of Intuit")
    if _match(text, ["promotion analysis", "2015 half-off", "2015 product discount"]):
        return ("job-interviews/intuit", 4, "Intuit takehome analysis topic")
    if _match(text, ["customer_insights", "ab_test_design"]):
        return ("job-interviews/intuit", 5, "Intuit takehome document reference")
    # Intuit-style takehome analysis patterns
    if _match(title, ["deluxe product promotion", "early 2015 product discount"]):
        return ("job-interviews/intuit", 4, "Intuit takehome promotion analysis")
    if _match(title, ["channel conversion rates", "stacked bar chart of completed users",
                       "free product growth marketing", "customer base overview",
                       "predicting tax filing"]):
        return ("job-interviews/intuit", 4, "Likely Intuit takehome analysis")

    # ── Blok ──
    if _match(text, ["blok", "joinblok", "behavioral ai platform"]):
        return ("job-interviews/blok", 5, "Direct mention of Blok")
    if _match(title, ["blok"]):
        return ("job-interviews/blok", 5, "Blok in title")

    # ── Lyft ──
    if _match(text, ["lyft"]) and _match(text, ["interview", "prep", "phone screen", "data scien"]):
        return ("job-interviews/lyft", 5, "Lyft interview context")
    if _match(title, ["lyft"]):
        return ("job-interviews/lyft", 5, "Lyft in title")

    # ── Google ──
    if _match(text, ["google"]) and _match(text, ["interview", "job", "application", "role"]):
        return ("job-interviews/google", 4, "Google job/interview context")

    # ── OpenAI Research Residency ──
    if _match(text, ["openai"]) and _match(text, ["research residency", "residency application"]):
        return ("job-interviews/openai-residency", 5, "OpenAI research residency")
    if _match(title, ["research residency"]):
        return ("job-interviews/openai-residency", 5, "Research residency in title")

    # ── Other job interviews ──
    if _match(title, ["interview prep", "phone screen prep"]) and not _match(text, ["lyft", "blok", "google", "intuit"]):
        return ("job-interviews/other", 4, "General interview prep")
    if _match(title, ["cedar", "thread ai", "chime"]) and _match(text, ["interview"]):
        return ("job-interviews/other", 4, "Other company interview")
    if _match(title, ["preparing for thread ai and chime"]):
        return ("job-interviews/other", 5, "Thread AI / Chime interview prep")
    if _match(title, ["cedar data science"]):
        return ("job-interviews/other", 5, "Cedar interview prep")
    # General data science interview prep
    if _match(title, ["data science interview preparation"]):
        return ("job-interviews/other", 4, "General DS interview prep")
    # Salary negotiation
    if _match(title, ["salary", "equity negotiation", "contract rate"]) and _match(text, ["interview", "offer", "job", "blok", "lyft", "google"]):
        return ("job-interviews/other", 4, "Job negotiation")
    # Negotiating contract rate
    if _match(title, ["negotiating contract rate"]):
        return ("job-interviews/other", 4, "Contract rate negotiation")
    # Experimentation fundamentals (interview prep topic)
    if _match(title, ["experimentation fundamentals"]):
        return ("job-interviews/other", 3, "Likely interview prep topic")
    # Behavioral clustering / GRE prep (interview-adjacent)
    if _match(title, ["behavioral clustering"]):
        return ("job-interviews/other", 4, "Interview-related behavioral analysis")
    if _match(title, ["gre math", "gre formulas"]) or _match(title, ["last-minute gre"]):
        return ("job-interviews/other", 4, "GRE prep for grad school applications")
    # Reference letters
    if _match(title, ["recommendation letter", "reference letter"]):
        return ("job-interviews/other", 4, "Recommendation/reference letter")
    # DoorDash/marketplace metrics (interview prep topic)
    if _match(title, ["doordash marketplace", "metrics for marketplace"]):
        return ("job-interviews/other", 3, "Marketplace metrics - likely interview prep")
    # RFM metrics, evaluation models
    if _match(title, ["rfm metrics"]):
        return ("job-interviews/other", 3, "Likely interview prep topic")

    # ── Gabriel ──
    if _match(text, ["gabriel nordenskiöld", "gabriel nordenskjöld", "gabriel nordenskiold"]):
        return ("personal/gabriel", 5, "Gabriel Nordenskiöld reference")
    if _match(title, ["gabriel"]) and not _match(text, ["archangel", "bible"]):
        return ("personal/gabriel", 4, "Gabriel in title (likely personal)")

    # ── Portfolio ──
    if _match(text, ["semantle"]):
        return ("portfolio/semantle", 5, "Semantle project reference")
    if _match(title, ["portfolio"]) or _match(text, ["portfolio project"]):
        return ("portfolio/other", 4, "Portfolio reference")

    # No heuristic match
    return None


# ─── Load Data ───────────────────────────────────────────────────────────────

def load_data():
    with open(CONVERSATIONS_PATH) as f:
        conversations = json.load(f)
    with open(PROJECTS_PATH) as f:
        projects = json.load(f)
    return conversations, projects


# ─── Pass 1: Heuristic Classification ───────────────────────────────────────

def run_pass1(conversations):
    results = {}
    for conv in conversations:
        uuid = conv["uuid"]
        match = heuristic_classify(conv)
        if match:
            category, confidence, reason = match
            results[uuid] = {
                "name": conv["name"],
                "date": conv["created_at"][:10],
                "msg_count": len(conv.get("chat_messages", [])),
                "category": category,
                "confidence": confidence,
                "reason": reason,
                "method": "heuristic",
            }
    return results


# ─── Pass 2: Claude API Classification ──────────────────────────────────────

def build_api_prompt(conv):
    """Build a classification prompt for a single conversation."""
    title = conv.get("name", "(untitled)")
    human_msgs = []
    for msg in conv.get("chat_messages", []):
        if msg.get("sender") == "human":
            text = msg.get("text", "")[:500]  # truncate long messages
            human_msgs.append(text)
            if len(human_msgs) >= 2:
                break

    messages_text = "\n---\n".join(human_msgs) if human_msgs else "(no messages)"

    return f"""Classify this conversation into exactly one category.

CONVERSATION TITLE: {title}
FIRST HUMAN MESSAGES:
{messages_text}

CATEGORIES (pick exactly one):
- course-material/math-e142: Math for AI course (Harvard Extension), MML textbook topics
- course-material/csci-e20: Discrete Math for CS course (Harvard Extension)
- job-interviews/blok: Blok company interview/prep
- job-interviews/lyft: Lyft interview/prep
- job-interviews/google: Google interview/prep
- job-interviews/intuit: Intuit interview/takehome
- job-interviews/openai-residency: OpenAI Research Residency application
- job-interviews/other: Other job interviews, general DS interview prep, salary negotiation
- personal/relationships: Relationships, communication, conflict, family
- personal/health: Physical health, mental health, medication, exercise
- personal/spirituality: Buddhism, zen, meditation, enneagram, philosophy of consciousness
- personal/dating: Dating apps, dating advice, romantic interests
- personal/gabriel: About a person named Gabriel
- personal/learning/ai-ml: AI/ML concepts, research papers, technical AI topics
- personal/learning/coding: Python, SQL, git, dev tools, programming questions
- personal/learning/general: History, politics, geography, general knowledge, curiosity questions
- personal/miscellaneous: One-off daily life questions, trivia, food, travel, random
- portfolio/semantle: Semantle word game project
- portfolio/other: Other portfolio/side projects

Respond with ONLY a JSON object (no markdown, no explanation):
{{"category": "...", "confidence": N, "reason": "brief reason"}}

confidence is 1-5 where:
1 = very unsure, could be many categories
2 = somewhat unsure
3 = reasonable guess but not certain
4 = fairly confident
5 = very confident
"""


def run_pass2_api(conversations, existing_results):
    """Classify unlabeled conversations using Claude API."""
    try:
        import anthropic
    except ImportError:
        print("Installing anthropic package...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "anthropic"])
        import anthropic

    client = anthropic.Anthropic()
    unlabeled = [c for c in conversations if c["uuid"] not in existing_results]
    print(f"\nPass 2: Classifying {len(unlabeled)} conversations via Claude API...")

    api_results = {}
    for i, conv in enumerate(unlabeled):
        uuid = conv["uuid"]
        prompt = build_api_prompt(conv)

        try:
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=200,
                messages=[{"role": "user", "content": prompt}],
            )
            text = response.content[0].text.strip()
            # Strip markdown code block wrapping if present
            if text.startswith("```"):
                text = re.sub(r"^```(?:json)?\s*", "", text)
                text = re.sub(r"\s*```$", "", text)
            parsed = json.loads(text)
            api_results[uuid] = {
                "name": conv["name"],
                "date": conv["created_at"][:10],
                "msg_count": len(conv.get("chat_messages", [])),
                "category": parsed["category"],
                "confidence": parsed["confidence"],
                "reason": parsed["reason"],
                "method": "api",
            }
        except (json.JSONDecodeError, KeyError, IndexError) as e:
            print(f"  [{i+1}/{len(unlabeled)}] PARSE ERROR for '{conv['name'][:50]}': {e}")
            api_results[uuid] = {
                "name": conv["name"],
                "date": conv["created_at"][:10],
                "msg_count": len(conv.get("chat_messages", [])),
                "category": "personal/miscellaneous",
                "confidence": 1,
                "reason": f"API parse error: {e}",
                "method": "api-error",
            }
        except Exception as e:
            print(f"  [{i+1}/{len(unlabeled)}] API ERROR for '{conv['name'][:50]}': {e}")
            api_results[uuid] = {
                "name": conv["name"],
                "date": conv["created_at"][:10],
                "msg_count": len(conv.get("chat_messages", [])),
                "category": "personal/miscellaneous",
                "confidence": 1,
                "reason": f"API error: {e}",
                "method": "api-error",
            }

        if (i + 1) % 25 == 0:
            print(f"  [{i+1}/{len(unlabeled)}] classified...")

    return api_results


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    print("Loading data...")
    conversations, projects = load_data()
    print(f"Loaded {len(conversations)} conversations, {len(projects)} projects")

    # Pass 1
    print("\n=== Pass 1: Heuristic Classification ===")
    results = run_pass1(conversations)
    print(f"Heuristic matches: {len(results)} / {len(conversations)}")

    # Summary
    by_cat = {}
    for r in results.values():
        cat = r["category"]
        by_cat[cat] = by_cat.get(cat, 0) + 1
    for cat, count in sorted(by_cat.items()):
        print(f"  {cat}: {count}")

    # Pass 2
    print("\n=== Pass 2: Claude API Classification ===")
    api_results = run_pass2_api(conversations, results)
    results.update(api_results)
    print(f"\nTotal classified: {len(results)} / {len(conversations)}")

    # Summary after both passes
    by_cat = {}
    for r in results.values():
        cat = r["category"]
        by_cat[cat] = by_cat.get(cat, 0) + 1
    print("\n=== Final Category Counts ===")
    for cat, count in sorted(by_cat.items()):
        print(f"  {cat}: {count}")

    # Ambiguous conversations
    ambiguous = {k: v for k, v in results.items() if v["confidence"] <= 3}
    print(f"\n=== Ambiguous (confidence <= 3): {len(ambiguous)} ===")
    if len(ambiguous) > 50:
        print(f"  (>50 ambiguous, tightening to confidence < 3)")
        ambiguous = {k: v for k, v in results.items() if v["confidence"] < 3}
        print(f"  Ambiguous (confidence < 3): {len(ambiguous)}")

    for r in sorted(ambiguous.values(), key=lambda x: x["confidence"]):
        print(f"  [{r['confidence']}] {r['name'][:60]} → {r['category']} ({r['reason']})")

    # Save results
    output = {
        "metadata": {
            "total_conversations": len(conversations),
            "heuristic_matches": len([r for r in results.values() if r["method"] == "heuristic"]),
            "api_matches": len([r for r in results.values() if r["method"] == "api"]),
            "ambiguous_count": len(ambiguous),
        },
        "classifications": results,
        "ambiguous": ambiguous,
    }
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
