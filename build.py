import os
import json
import re

CATEGORY_ORDER = [
    "Prompting & Thinking Systems",
    "Customer Discovery & Segmentation",
    "Market & Competitive Intelligence",
    "Product Planning & Experimentation",
    "Positioning, Pricing & GTM",
    "Finance & Fundraising",
    "Org Design & Change",
    "Decision Quality & Executive Synthesis",
]

SKILLS_DIR = "skills"
SKILL_CATEGORY = "Skills"
REPO_URL = "https://github.com/siddharthachaturvedi/prompts"

ACRONYMS = {
    "ab": "A/B",
    "crit": "CRIT",
    "gtm": "GTM",
    "jtbd": "JTBD",
    "mvp": "MVP",
    "prd": "PRD",
    "swot": "SWOT",
    "tam": "TAM",
}

SMALL_WORDS = {"a", "an", "and", "for", "in", "of", "on", "or", "the", "to"}

PHRASE_FIXES = (
    ("Meta Prompt to Auto Prompt", "Meta Prompt to Auto-Prompt"),
    ("Lean MVP Customer Validation", "Lean MVP and Customer Validation"),
    ("Motivation Job Redesign", "Motivation and Job Redesign"),
    ("Strategic Pre Mortem", "Strategic Pre-Mortem"),
    ("Project Pre Mortem", "Project Pre-Mortem"),
    ("Multi Framework", "Multi-Framework"),
    ("Context Aware", "Context-Aware"),
    ("Go to Market", "Go-To-Market"),
    ("Market Sizing TAM Analysis", "Market Sizing & TAM Analysis"),
    ("Customer Persona Segmentation", "Customer Persona & Segmentation"),
    ("SWOT Five Forces", "SWOT + Five Forces"),
    ("Financial Modeling Unit Economics", "Financial Modeling & Unit Economics"),
    ("Risk Assessment Scenario Planning", "Risk Assessment & Scenario Planning"),
    ("Market Entry Expansion Strategy", "Market Entry & Expansion Strategy"),
)

def format_slug_title(slug):
    """Convert a filename slug into a display title without damaging acronyms."""
    words = []
    for i, token in enumerate(re.split(r"[_-]+", slug)):
        lower = token.lower()
        if lower in ACRONYMS:
            words.append(ACRONYMS[lower])
        elif lower in SMALL_WORDS and i != 0:
            words.append(lower)
        else:
            words.append(lower.capitalize())

    title = " ".join(words)
    for old, new in PHRASE_FIXES:
        title = title.replace(old, new)
    return title

def create_title(filename):
    """Convert filename like '00_meta_prompt.md' into '00 - Meta Prompt'."""
    name, _ = os.path.splitext(filename)
    
    match = re.match(r'^(\d+)[_-](.*)', name)
    if match:
        num = match.group(1)
        rest = match.group(2)
        return f"{num} - {format_slug_title(rest)}"
    else:
        return format_slug_title(name)

def word_count(text):
    """Count words in a string."""
    return len(text.split())

def category_rank(category):
    """Stable workstream order for filters and reporting."""
    try:
        return CATEGORY_ORDER.index(category)
    except ValueError:
        return len(CATEGORY_ORDER)

def load_skills(base_dir):
    """Read skills/<name>/SKILL.md files into site records.

    A skill keeps the standard SKILL.md frontmatter (name, description) and
    nothing site-specific. Everything the site needs is derived here.
    """
    skills = []
    skills_dir = os.path.join(base_dir, SKILLS_DIR)
    if not os.path.isdir(skills_dir):
        return skills

    for slug in sorted(os.listdir(skills_dir)):
        filepath = os.path.join(skills_dir, slug, "SKILL.md")
        if not os.path.isfile(filepath):
            continue
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()

        name = slug
        description = ""
        body = source.strip()
        if source.startswith("---"):
            parts = source.split("---", 2)
            if len(parts) >= 3:
                body = parts[2].strip()
                for line in parts[1].strip().splitlines():
                    key_val = line.split(":", 1)
                    if len(key_val) == 2:
                        key = key_val[0].strip().lower()
                        val = key_val[1].strip().strip('"\'')
                        if key == "name":
                            name = val
                        elif key == "description":
                            description = val

        # Prefer the skill's own H1 as its display title.
        heading = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
        title = heading.group(1).strip() if heading else format_slug_title(name)

        skills.append({
            "filename": f"skill-{slug}.md",
            "type": "skill",
            "slug": slug,
            "title": title,
            "category": SKILL_CATEGORY,
            "categoryRank": category_rank(SKILL_CATEGORY),
            "level": "",
            "link": f"{REPO_URL}/tree/main/{SKILLS_DIR}/{slug}",
            "tags": [],
            "words": word_count(body),
            "description": description,
            "content": body,
            "source": source,
        })
    return skills

def build_site():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    prompts = []

    # Sorted so the generated file is identical from one machine to the next.
    for filename in sorted(os.listdir(base_dir)):
        if filename.endswith(".md") and filename != "README.md":
            filepath = os.path.join(base_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            title = create_title(filename)
            
            # Parse optional frontmatter (---\nkey: val\n---)
            category = ""
            level = ""
            link = ""
            tags = []
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    frontmatter = parts[1]
                    content = parts[2].strip()
                    for line in frontmatter.strip().splitlines():
                        key_val = line.split(":", 1)
                        if len(key_val) == 2:
                            key = key_val[0].strip().lower()
                            val = key_val[1].strip()
                            if key == "category":
                                category = val
                            elif key == "level":
                                level = val
                            elif key == "link":
                                link = val
                            elif key == "tags":
                                tags = [tag.strip() for tag in val.split(",") if tag.strip()]
            
            prompts.append({
                "filename": filename,
                "type": "prompt",
                "title": title,
                "category": category,
                "categoryRank": category_rank(category),
                "level": level,
                "link": link,
                "tags": tags,
                "words": word_count(content),
                "content": content
            })
            
    skills = load_skills(base_dir)
    print(f"Found {len(prompts)} prompts and {len(skills)} skill{'' if len(skills) == 1 else 's'}.")

    # Collect unique categories for template
    categories = sorted(set(p["category"] for p in prompts if p["category"]), key=category_rank)

    template_path = os.path.join(base_dir, "template.html")
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Escape "</" so text inside a prompt or skill can never close the data script tag.
    json_data = json.dumps(prompts + skills, indent=2).replace("</", "<\\/")
    html_output = template.replace("{{ PROMPTS_JSON }}", json_data)
    
    output_path = os.path.join(base_dir, "index.html")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_output)
        
    print(f"Successfully generated {output_path}")
    print(f"Categories: {', '.join(categories)}")

if __name__ == "__main__":
    build_site()
