"""
Create the llm-context directory structure and populate with conversation files.
Also creates index.md files with project metadata from projects.json.
"""

import json
import re
import os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
LLM_CONTEXT = BASE_DIR / "llm-context"
CONVERSATIONS_PATH = LLM_CONTEXT / "chats" / "conversations.json"
PROJECTS_PATH = LLM_CONTEXT / "chats" / "projects.json"
CLASSIFICATION_PATH = BASE_DIR / "scripts" / "classification_results.json"


def slugify(text, max_len=60):
    """Convert text to URL-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    text = text.strip("-")
    return text[:max_len]


def conversation_to_markdown(conv):
    """Convert a conversation object to formatted markdown."""
    lines = []
    name = conv.get("name", "(untitled)")
    date = conv.get("created_at", "")[:10]
    lines.append(f"# {name}")
    lines.append(f"\n**Date:** {date}")
    lines.append(f"**Messages:** {len(conv.get('chat_messages', []))}")
    lines.append("")

    for msg in conv.get("chat_messages", []):
        sender = msg.get("sender", "unknown")
        text = msg.get("text", "")
        if sender == "human":
            lines.append(f"## Human\n")
            lines.append(text)
            lines.append("")
        elif sender == "assistant":
            lines.append(f"## Assistant\n")
            lines.append(text)
            lines.append("")

    return "\n".join(lines)


def create_index_md(category, project_metadata=None):
    """Create an index.md for a project directory."""
    # Map category to friendly name
    names = {
        "course-material/math-e142": "Math E-142: Mathematics for Artificial Intelligence",
        "course-material/csci-e20": "CSCI E-20: Discrete Mathematics for Computer Science",
        "job-interviews/blok": "Blok — Job Interview Prep",
        "job-interviews/lyft": "Lyft — Job Interview Prep",
        "job-interviews/google": "Google — Job Interview Prep",
        "job-interviews/intuit": "Intuit — Takehome & Interview Prep",
        "job-interviews/openai-residency": "OpenAI Research Residency — Application",
        "job-interviews/other": "Other Job Interviews & General Prep",
        "personal/relationships": "Relationships",
        "personal/health": "Health — Physical & Mental",
        "personal/spirituality": "Spirituality — Buddhism, Zen, Enneagram",
        "personal/dating": "Dating",
        "personal/gabriel": "Gabriel",
        "personal/self-growth": "Self-Growth & Reflection",
        "personal/learning/ai-ml": "Learning — AI & Machine Learning",
        "personal/learning/coding": "Learning — Coding & Dev Tools",
        "personal/learning/general": "Learning — General Knowledge",
        "personal/miscellaneous": "Miscellaneous",
        "portfolio/semantle": "Semantle — Word Game Project",
        "portfolio/other": "Other Portfolio Projects",
    }

    name = names.get(category, category.split("/")[-1].replace("-", " ").title())
    lines = [f"# {name}", ""]

    if project_metadata:
        if project_metadata.get("description"):
            lines.append(f"## Description\n")
            lines.append(project_metadata["description"])
            lines.append("")
        if project_metadata.get("prompt_template"):
            lines.append(f"## Prompt Template\n")
            lines.append(f"```")
            lines.append(project_metadata["prompt_template"])
            lines.append(f"```")
            lines.append("")
        if project_metadata.get("docs"):
            lines.append(f"## Associated Documents\n")
            for doc in project_metadata["docs"]:
                lines.append(f"- **{doc['filename']}** — uploaded {doc['created_at'][:10]}")
            lines.append("")

    return "\n".join(lines)


def main():
    # Load data
    with open(CONVERSATIONS_PATH) as f:
        conversations = json.load(f)
    with open(PROJECTS_PATH) as f:
        projects = json.load(f)
    with open(CLASSIFICATION_PATH) as f:
        classification_data = json.load(f)

    classifications = classification_data["classifications"]

    # Build conversation lookup by UUID
    conv_by_uuid = {c["uuid"]: c for c in conversations}

    # Map existing projects to categories
    project_meta_map = {
        "Math E-142": "course-material/math-e142",
        "CSCI E-20": "course-material/csci-e20",
        "Intuit Takehome": "job-interviews/intuit",
        "Blok": "job-interviews/blok",
        "Lyft": "job-interviews/lyft",
        "Google ": "job-interviews/google",
        "OpenAI Research Residency": "job-interviews/openai-residency",
        "Gabriel": "personal/gabriel",
        "AI & Consciousness": "personal/learning/ai-ml",
        "Portfolio": "portfolio/other",
        "Personal": "personal/miscellaneous",
        "Research": "personal/learning/ai-ml",
    }

    # Build project metadata by category
    project_metadata = {}
    for proj in projects:
        cat = project_meta_map.get(proj["name"])
        if cat and not proj.get("is_starter_project"):
            project_metadata[cat] = {
                "name": proj["name"],
                "description": proj.get("description", ""),
                "prompt_template": proj.get("prompt_template", ""),
                "docs": proj.get("docs", []),
            }

    # Collect all categories
    all_categories = set()
    for info in classifications.values():
        all_categories.add(info["category"])

    # Always include these even if empty
    for cat in ["portfolio/other", "personal/self-growth"]:
        all_categories.add(cat)

    # Create directories
    print("=== Creating directories ===")
    for category in sorted(all_categories):
        dir_path = LLM_CONTEXT / category
        conv_dir = dir_path / "conversations"
        conv_dir.mkdir(parents=True, exist_ok=True)
        print(f"  Created {category}/conversations/")

        # Create index.md
        meta = project_metadata.get(category)
        index_content = create_index_md(category, meta)
        index_path = dir_path / "index.md"
        if not index_path.exists():
            index_path.write_text(index_content)
            print(f"  Wrote {category}/index.md")

    # Write conversation files
    print("\n=== Writing conversation files ===")
    written = 0
    skipped = 0
    for uuid, info in classifications.items():
        conv = conv_by_uuid.get(uuid)
        if not conv:
            skipped += 1
            continue

        category = info["category"]
        date = info["date"]
        name = info.get("name", "untitled")
        slug = slugify(name)
        if not slug:
            slug = "untitled"

        filename = f"{date}-{slug}.md"
        filepath = LLM_CONTEXT / category / "conversations" / filename

        # Handle duplicate filenames
        if filepath.exists():
            counter = 2
            while filepath.exists():
                filename = f"{date}-{slug}-{counter}.md"
                filepath = LLM_CONTEXT / category / "conversations" / filename
                counter += 1

        md_content = conversation_to_markdown(conv)
        filepath.write_text(md_content)
        written += 1

    print(f"  Written: {written} conversation files")
    print(f"  Skipped: {skipped} (UUID not found)")

    # Write Intuit docs (they have full text content in the JSON)
    print("\n=== Writing Intuit takehome docs ===")
    for proj in projects:
        if proj["name"] == "Intuit Takehome" and proj.get("docs"):
            docs_dir = LLM_CONTEXT / "job-interviews" / "intuit" / "docs"
            docs_dir.mkdir(parents=True, exist_ok=True)
            for doc in proj["docs"]:
                doc_path = docs_dir / doc["filename"]
                doc_path.write_text(doc.get("content", ""))
                print(f"  Wrote {doc['filename']}")

    # Summary
    print("\n=== Summary ===")
    by_cat = {}
    for info in classifications.values():
        cat = info["category"]
        by_cat[cat] = by_cat.get(cat, 0) + 1
    for cat, count in sorted(by_cat.items()):
        print(f"  {cat}: {count} conversations")
    print(f"  Total: {sum(by_cat.values())} conversations written")

    # Surface docs that Emily needs to move manually
    print("\n=== Documents for Emily to move manually ===")
    for proj in projects:
        if proj.get("docs") and proj["name"] != "Intuit Takehome" and not proj.get("is_starter_project"):
            cat = project_meta_map.get(proj["name"], "unknown")
            for doc in proj["docs"]:
                content_len = len(doc.get("content", ""))
                is_pdf = doc["filename"].lower().endswith(".pdf")
                if is_pdf:
                    print(f"  [{proj['name']}] {doc['filename']} → {cat}/ (PDF, {content_len} chars text)")
                else:
                    print(f"  [{proj['name']}] {doc['filename']} → {cat}/ (text, will write)")

    # Write non-PDF, non-Intuit docs
    for proj in projects:
        if proj.get("docs") and proj["name"] != "Intuit Takehome" and not proj.get("is_starter_project"):
            cat = project_meta_map.get(proj["name"])
            if not cat:
                continue
            docs_dir = LLM_CONTEXT / cat / "docs"
            for doc in proj["docs"]:
                is_pdf = doc["filename"].lower().endswith(".pdf")
                if not is_pdf and doc.get("content"):
                    docs_dir.mkdir(parents=True, exist_ok=True)
                    doc_path = docs_dir / doc["filename"]
                    doc_path.write_text(doc.get("content", ""))
                    print(f"  Wrote {cat}/docs/{doc['filename']}")


if __name__ == "__main__":
    main()
