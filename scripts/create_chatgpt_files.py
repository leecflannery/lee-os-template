"""
Create markdown conversation files from classified ChatGPT conversations.
Reads classification results and original JSON, writes YYYY-MM-DD-slug-chatgpt.md files
into the correct /conversations/ directories.

Usage: python3 scripts/create_chatgpt_files.py
"""

import json
import os
import re
import datetime

BASE = "/Users/emilyhk/ehk-os"
JSON_DIR = f"{BASE}/llm-context/chats/openai/online_activity/conversations/conversations_jsons"
CLASSIFICATION_FILE = f"{BASE}/scripts/chatgpt_classification_results.json"


def slugify(title):
    """Convert title to URL-friendly slug."""
    if not title:
        return "untitled"
    slug = title.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug[:80] if slug else "untitled"


def extract_messages(mapping):
    """Extract messages in order from ChatGPT mapping structure."""
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
            if text_parts and author_role in ('user', 'assistant'):
                messages.append({
                    'role': author_role,
                    'text': '\n'.join(text_parts)
                })
        children = node.get('children', [])
        queue.extend(children)

    return messages


def format_conversation(title, date_str, messages):
    """Format conversation as markdown matching existing format."""
    lines = [f"# {title}", ""]
    lines.append(f"**Date:** {date_str}")
    lines.append(f"**Messages:** {len(messages)}")

    for msg in messages:
        lines.append("")
        if msg['role'] == 'user':
            lines.append("## Human")
        else:
            lines.append("## Assistant")
        lines.append("")
        lines.append(msg['text'].rstrip())

    return '\n'.join(lines) + '\n'


def main():
    # Load classification results
    with open(CLASSIFICATION_FILE) as f:
        data = json.load(f)
    classifications = data['classifications']

    # Build lookup: conversation_id -> classification
    print(f"Loaded {len(classifications)} classifications.")

    # Load all conversations from JSON
    all_convos = {}
    for fname in sorted(os.listdir(JSON_DIR)):
        if not fname.endswith('.json'):
            continue
        with open(os.path.join(JSON_DIR, fname)) as f:
            convs = json.load(f)
        for conv in convs:
            cid = conv.get('conversation_id', conv.get('id', ''))
            all_convos[cid] = conv

    print(f"Loaded {len(all_convos)} conversations from JSON files.")

    # Create files
    created = 0
    skipped = 0
    errors = 0
    files_by_category = {}

    for cid, cls in classifications.items():
        conv = all_convos.get(cid)
        if not conv:
            print(f"  WARNING: No conversation found for ID {cid}")
            errors += 1
            continue

        category = cls['category']
        title = cls['name'] or 'Untitled'
        date_str = cls['date']
        slug = slugify(title)

        # Build target path
        target_dir = os.path.join(BASE, category, "conversations")
        os.makedirs(target_dir, exist_ok=True)

        filename = f"{date_str}-{slug}-chatgpt.md"
        filepath = os.path.join(target_dir, filename)

        # Handle duplicate filenames
        if os.path.exists(filepath):
            counter = 2
            while os.path.exists(filepath):
                filename = f"{date_str}-{slug}-{counter}-chatgpt.md"
                filepath = os.path.join(target_dir, filename)
                counter += 1

        # Extract messages
        mapping = conv.get('mapping', {})
        messages = extract_messages(mapping)

        if not messages:
            skipped += 1
            continue

        # Write file
        content = format_conversation(title, date_str, messages)
        with open(filepath, 'w') as f:
            f.write(content)

        created += 1
        files_by_category.setdefault(category, []).append(filename)

    print(f"\nDone!")
    print(f"  Created: {created}")
    print(f"  Skipped (no messages): {skipped}")
    print(f"  Errors: {errors}")

    print(f"\nFiles per category:")
    for cat in sorted(files_by_category.keys()):
        print(f"  {cat}: {len(files_by_category[cat])}")

    # Verify total
    total_files = sum(len(files) for files in files_by_category.values())
    print(f"\nTotal files written: {total_files}")


if __name__ == "__main__":
    main()
