"""
Classify ChatGPT conversations into the personal OS directory structure.
3-pass approach: heuristic → Haiku API → ambiguity flagging.

Usage: python3 scripts/classify_chatgpt.py
"""

import json
import os
import re
import time
import datetime
from pathlib import Path
import anthropic

# ── Paths ──────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
JSON_DIR = BASE_DIR / "llm-context" / "chats" / "openai" / "online_activity" / "conversations" / "conversations_jsons"
OUTPUT_FILE = BASE_DIR / "scripts" / "chatgpt_classification_results.json"

# ── Categories ─────────────────────────────────────────────────────
CATEGORIES = {
    # grad-school
    "grad-school/math-e142": "Harvard Math E-142 (probability, statistics, stochastic processes course)",
    "grad-school/csci-e20": "Harvard CSCI E-20 (discrete math, computer science course)",
    "grad-school/other": "Other graduate school coursework or academic assignments",

    # job-interviews
    "job-interviews/blok": "Blok company job interview prep and application",
    "job-interviews/google": "Google job interview prep and application",
    "job-interviews/intuit": "Intuit job interview prep and application",
    "job-interviews/lyft": "Lyft job interview prep and application",
    "job-interviews/openai-residency": "OpenAI residency application and prep",
    "job-interviews/other": "Other job interviews, applications, resume writing, cover letters, career prep",

    # personal
    "personal/health": "Physical health, mental health, therapy, medications, fitness, nutrition, medical questions",
    "personal/dating": "Dating, romantic relationships, dating apps, relationship advice",
    "personal/gabriel": "About Gabriel Nordenskiöld specifically",
    "personal/relationships": "Friendships, family, social dynamics, communication with people (non-dating)",
    "personal/self-growth": "Personal development, self-reflection, identity, life decisions",
    "personal/spirituality": "Spirituality, religion, Buddhism, Zen, astrology, enneagram, meditation",
    "personal/learning/ai-ml": "AI, machine learning, LLMs, deep learning, data science theory/concepts",
    "personal/learning/coding": "Programming, software tools, Git, SQL, Python coding, IDE setup, Claude Code",
    "personal/learning/general": "General knowledge, trivia, history, politics, geography, culture, language, random questions",
    "personal/miscellaneous": "One-off conversations that don't fit elsewhere: recipes, pet care, entertainment recs, travel, creative requests",

    # portfolio
    "portfolio/semantle": "Semantle game project or word-embedding games",
    "portfolio/other": "Other portfolio projects, personal websites, side projects, data projects",
}

# ── Heuristic keyword rules ───────────────────────────────────────
HEURISTIC_RULES = [
    # grad-school
    (r"math.?e.?142|stochastic|markov chain|probability (theory|distribution)|poisson|bayes.* theorem|conditional probability|random (variable|walk)|expected value|variance.*formula|combinatorics|math 142", "grad-school/math-e142", 5),
    (r"csci.?e.?20|discrete math|boolean algebra|propositional logic|graph theory|combinatorial", "grad-school/csci-e20", 5),
    (r"pset|problem set|homework assignment.*class|coursework|harvard extension|e-\d{2,3}", "grad-school/other", 4),

    # job-interviews
    (r"\bblok\b", "job-interviews/blok", 5),
    (r"google interview|google (coding|system design|behavioral)|google application", "job-interviews/google", 5),
    (r"\bintuit\b", "job-interviews/intuit", 5),
    (r"\blyft\b", "job-interviews/lyft", 5),
    (r"openai.*(residency|application|interview|apply)", "job-interviews/openai-residency", 5),
    (r"(resume|cover letter|job (application|description|interview)|behavioral interview|star method|salary negotiation|linkedin profile)", "job-interviews/other", 4),

    # personal - gabriel
    (r"\bgabriel\b|\bnordenskiöld\b|\bnordenskiold\b|\bgabe\b", "personal/gabriel", 5),

    # personal - health
    (r"(therapy|therapist|mental health|anxiety|depression|bipolar|adhd|medication|prescription|semaglutide|ozempic|botox|fitness|workout|exercise|stretching|yoga|nutrition|calories|protein|symptom|diagnosis|medical|doctor|strep|headache|vaccine|vomiting|ALS|dementia)", "personal/health", 4),

    # personal - dating
    (r"(dating app|hinge|bumble|tinder|first date|dating profile|romantic|boyfriend|girlfriend)", "personal/dating", 4),

    # personal - spirituality
    (r"(buddhis[mt]|zen|meditation|koan|dharma|tantra|enneagram|astrology|gemini women|spiritual|manifesting|law of attraction|non.?duality)", "personal/spirituality", 4),

    # personal - self-growth
    (r"(self.?reflect|personal growth|identity|hard truths|life decision|self.?improvement)", "personal/self-growth", 4),

    # personal - learning/ai-ml
    (r"(machine learning|deep learning|neural network|transformer|LLM|GPT|claude|anthropic|attention mechanism|backpropagation|gradient descent|fine.?tun|LoRA|gaussian mixture|PCA|training.*model|inference|token.*context|constitutional ai)", "personal/learning/ai-ml", 4),

    # personal - learning/coding
    (r"(python|pandas|sklearn|matplotlib|sql|mysql|postgres|git\b|github|docker|kubernetes|jupyter|regex|venv|pip install|npm|javascript|html|css|latex|pdflatex|cursor|vs.?code|claude code|api.?key|mcp server)", "personal/learning/coding", 4),

    # personal - learning/general - Swedish language
    (r"(svenska|svensk|swedish|pratar du|stockholm|sweden|bättre|övning)", "personal/learning/general", 4),

    # portfolio
    (r"(semantle|word embed|word2vec.*game)", "portfolio/semantle", 5),
    (r"(portfolio|personal website|side project|landing page|github pages|deploy)", "portfolio/other", 4),
]


def load_all_conversations():
    """Load and parse all ChatGPT JSON files."""
    all_convos = []

    for fname in sorted(os.listdir(JSON_DIR)):
        if not fname.endswith('.json'):
            continue
        with open(os.path.join(JSON_DIR, fname)) as f:
            data = json.load(f)
        for conv in data:
            title = conv.get('title', '') or ''
            create_time = conv.get('create_time', 0)

            # Extract messages in order
            mapping = conv.get('mapping', {})
            root = None
            for nid, node in mapping.items():
                if node.get('parent') is None:
                    root = nid
                    break

            messages = []
            queue = [root] if root else []
            while queue:
                current_id = queue.pop(0)
                node = mapping[current_id]
                msg = node.get('message')
                if msg and msg.get('content', {}).get('parts'):
                    author_role = msg.get('author', {}).get('role', 'unknown')
                    parts = msg['content']['parts']
                    text_parts = [p for p in parts if isinstance(p, str) and p.strip()]
                    if text_parts:
                        messages.append({
                            'role': author_role,
                            'text': '\n'.join(text_parts)
                        })
                children = node.get('children', [])
                queue.extend(children)

            human_msgs = [m for m in messages if m['role'] == 'user']
            assistant_msgs = [m for m in messages if m['role'] == 'assistant']

            if not human_msgs:
                continue  # skip empty

            dt = datetime.datetime.fromtimestamp(create_time) if create_time else None

            all_convos.append({
                'id': conv.get('conversation_id', conv.get('id', '')),
                'title': title,
                'date': dt.strftime('%Y-%m-%d') if dt else 'unknown',
                'msg_count': len(messages),
                'human_msg_count': len(human_msgs),
                'first_human_msgs': [m['text'][:500] for m in human_msgs[:2]],
                'all_messages': messages,
                'file': fname,
                'gizmo_id': conv.get('gizmo_id'),
            })

    return all_convos


def classify_heuristic(conv):
    """Pass 1: keyword-based classification."""
    text_block = (conv['title'].lower() + ' ' +
                  ' '.join(conv['first_human_msgs']).lower())

    for pattern, category, confidence in HEURISTIC_RULES:
        if re.search(pattern, text_block, re.IGNORECASE):
            return category, confidence, f"Heuristic match: {pattern[:40]}"
    return None, 0, None


def classify_with_api(convos, api_key):
    """Pass 2: classify unmatched conversations with Haiku."""
    client = anthropic.Anthropic(api_key=api_key)

    category_list = "\n".join(
        f"- {cat}: {desc}" for cat, desc in CATEGORIES.items()
    )

    results = {}
    total = len(convos)
    for i, conv in enumerate(convos):
        cid = conv['id']
        title = conv['title']
        first_msgs = '\n---\n'.join(conv['first_human_msgs'])

        prompt = f"""Classify this ChatGPT conversation into exactly one category.

CONVERSATION TITLE: {title}
FIRST HUMAN MESSAGES:
{first_msgs}

CATEGORIES (pick exactly one):
{category_list}

Respond with ONLY a JSON object:
{{"category": "...", "confidence": N, "reason": "brief reason"}}

confidence: 1=very unsure, 2=somewhat unsure, 3=reasonable guess, 4=fairly confident, 5=very confident"""

        try:
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=200,
                messages=[{"role": "user", "content": prompt}]
            )
            text = response.content[0].text.strip()
            # Strip markdown code blocks if present
            text = re.sub(r'^```json\s*', '', text)
            text = re.sub(r'\s*```$', '', text)
            result = json.loads(text)
            results[cid] = {
                'category': result['category'],
                'confidence': result.get('confidence', 3),
                'reason': result.get('reason', ''),
                'method': 'api'
            }
        except Exception as e:
            print(f"  ERROR on '{title}': {e}")
            results[cid] = {
                'category': 'personal/miscellaneous',
                'confidence': 1,
                'reason': f'API error: {str(e)[:80]}',
                'method': 'api_error'
            }

        if (i + 1) % 25 == 0:
            print(f"  Classified {i+1}/{total}...")
            # Save progress
            with open(OUTPUT_FILE + '.progress', 'w') as f:
                json.dump(results, f, indent=2)

    return results


def main():
    print("Loading ChatGPT conversations...")
    convos = load_all_conversations()
    print(f"Found {len(convos)} non-empty conversations.\n")

    # Pass 1: Heuristics
    print("Pass 1: Heuristic classification...")
    classifications = {}
    unmatched = []

    for conv in convos:
        cat, conf, reason = classify_heuristic(conv)
        if cat:
            classifications[conv['id']] = {
                'name': conv['title'],
                'date': conv['date'],
                'msg_count': conv['msg_count'],
                'category': cat,
                'confidence': conf,
                'reason': reason,
                'method': 'heuristic'
            }
        else:
            unmatched.append(conv)

    print(f"  Heuristics matched {len(classifications)} of {len(convos)} conversations.")
    print(f"  Remaining for API: {len(unmatched)}\n")

    # Pass 2: API classification
    API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
    if not API_KEY:
        print("ERROR: ANTHROPIC_API_KEY not set. Set it and re-run.")
        # Save heuristic results anyway
        save_results(classifications, convos)
        return

    print("Pass 2: API classification with Haiku...")
    api_results = classify_with_api(unmatched, API_KEY)

    for conv in unmatched:
        cid = conv['id']
        if cid in api_results:
            classifications[cid] = {
                'name': conv['title'],
                'date': conv['date'],
                'msg_count': conv['msg_count'],
                **api_results[cid]
            }

    save_results(classifications, convos)


def save_results(classifications, convos):
    """Save classification results to disk."""
    # Count by method
    heuristic_count = sum(1 for c in classifications.values() if c.get('method') == 'heuristic')
    api_count = sum(1 for c in classifications.values() if c.get('method') in ('api', 'api_error'))
    ambiguous = sum(1 for c in classifications.values() if c.get('confidence', 0) <= 3)

    output = {
        'metadata': {
            'total_conversations': len(convos),
            'classified': len(classifications),
            'heuristic_matches': heuristic_count,
            'api_matches': api_count,
            'ambiguous_count': ambiguous,
            'generated_at': datetime.datetime.now().isoformat()
        },
        'classifications': classifications
    }

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to {OUTPUT_FILE}")
    print(f"  Total: {len(convos)}")
    print(f"  Classified: {len(classifications)}")
    print(f"  Heuristic: {heuristic_count}")
    print(f"  API: {api_count}")
    print(f"  Ambiguous (confidence ≤ 3): {ambiguous}")

    # Category breakdown
    cat_counts = {}
    for c in classifications.values():
        cat = c['category']
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    print("\nCategory breakdown:")
    for cat in sorted(cat_counts.keys()):
        print(f"  {cat}: {cat_counts[cat]}")


if __name__ == "__main__":
    main()
