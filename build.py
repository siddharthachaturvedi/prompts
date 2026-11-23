import datetime
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
SITE_URL = "https://prompts.sidc.ai"
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

def roman(number):
    """Year in Roman numerals, for the page kicker (as on sidc.ai)."""
    out = ""
    for value, numeral in ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                           (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")):
        while number >= value:
            out += numeral
            number -= value
    return out

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

        needs = re.search(r"adapter for the ([a-z0-9-]+) skill", description)
        requires = needs.group(1) if needs else ""
        category = "Adapters" if requires else "Engine"

        skills.append({
            "filename": f"skill-{slug}.md",
            "type": "skill",
            "slug": slug,
            "title": title,
            "category": category,
            "categoryRank": category_rank(category),
            "requires": requires,
            "level": "",
            "link": f"{REPO_URL}/tree/main/{SKILLS_DIR}/{slug}",
            "tags": [],
            "words": word_count(body),
            "description": description,
            "content": body,
            "source": source,
        })
    return skills

def check_mece(prompts):
    """Stop the build if the library stops being MECE.

    Mutually exclusive: each prompt sits in exactly one known workstream and
    answers one question that no other prompt answers. Steps order the prompts
    inside a workstream, 1..n with no repeats.
    Collectively exhaustive, as far as a build can tell: no workstream is empty.
    Whether a workstream is missing a question is a judgment call, kept in
    grooming/LEDGER.md.
    """
    problems = []
    questions = {}
    steps = {}
    for p in prompts:
        name = p["filename"]
        if p["category"] not in CATEGORY_ORDER:
            problems.append(f"{name}: category '{p['category']}' is not one of the workstreams")
        if not p["question"]:
            problems.append(f"{name}: no question")
        elif p["question"].lower() in questions:
            problems.append(f"{name}: same question as {questions[p['question'].lower()]}")
        else:
            questions[p["question"].lower()] = name
        steps.setdefault(p["category"], []).append(p["step"])
    for category in CATEGORY_ORDER:
        found = sorted(steps.get(category, []))
        if not found:
            problems.append(f"{category}: no prompts")
        elif found != list(range(1, len(found) + 1)):
            problems.append(f"{category}: steps are {found}, expected 1 to {len(found)} with no repeats")
    if problems:
        raise SystemExit("MECE check failed:\n  " + "\n  ".join(problems))

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
            mode = ""
            question = ""
            step = 0
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
                            elif key == "mode":
                                mode = val
                            elif key == "question":
                                question = val
                            elif key == "step":
                                step = int(val) if val.isdigit() else 0
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
                "mode": mode,
                "question": question,
                "step": step,
                "tags": tags,
                "words": word_count(content),
                "content": content
            })
            
    check_mece(prompts)
    skills = load_skills(base_dir)
    print(f"Found {len(prompts)} prompts and {len(skills)} skill{'' if len(skills) == 1 else 's'}.")

    # Collect unique categories for reporting
    categories = sorted(set(p["category"] for p in prompts if p["category"]), key=category_rank)

    template_path = os.path.join(base_dir, "template.html")
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    engines = [s for s in skills if not s["requires"]]
    adapters = [s for s in skills if s["requires"]]

    def summary(description):
        first = re.match(r"^.*?[.!?](?=\s|$)", description)
        return first.group(0) if first else description

    def count(n, word):
        return f"{n} {word}" if n == 1 else f"{n} {word}s"

    # Each page shows its sibling: a one-line door in the hero, and on the
    # prompts page the skills in full below the grid, engine first.
    skills_shelf = {
        "door_label": "Skills",
        "door": f"{count(len(engines), 'engine')} and {count(len(adapters), 'adapter')}",
        "kicker": "Skills // beyond a prompt",
        "title": "Skills",
        "lede": "When a prompt is not enough, hand the whole job to an agent. "
                "One engine holds the method. Adapters plug it into a system.",
        "href": f"{SKILLS_DIR}/",
        "link": "All skills",
        "items": [
            {
                "slug": s["slug"],
                "title": s["title"],
                "summary": summary(s["description"]),
                "category": s["category"],
                "requires": s["requires"],
                "words": s["words"],
                "href": f"{SKILLS_DIR}/#skill-{s['slug']}",
            }
            for s in engines + adapters
        ],
    }
    prompts_shelf = {
        "door_label": "Prompts",
        "door": f"{len(prompts)} prompts in {len(categories)} moves",
        "href": "../",
        "items": [],
    }

    year = datetime.date.today().year
    kicker_year = roman(year)

    # Prompts and skills are separate pages. Links between them are relative,
    # so the pair still works if it is ever served under another path.
    pages = [
        {
            "output": "index.html",
            "items": prompts,
            "kind": "prompts",
            "name": "Prompts",
            "title": "Prompts - Siddhartha Chaturvedi",
            "url": f"{SITE_URL}/",
            "kicker": f"Prompts // {kicker_year}",
            "lede": "Decision-grade prompts for MBA students, executives, and startup operators. "
                    "Eight moves, in the order a venture meets them. Copy one, edit it, or launch it in your LLM.",
            "description": "Decision-grade prompts for strategy, product, go-to-market, finance, and org design. "
                           "Copy, edit, or launch directly in your LLM.",
            "search": "Search titles, moves, tags, or prompt text… (⌘K)",
            "prompts_href": "./",
            "skills_href": "skills/",
            "shelf": skills_shelf,
        },
        {
            "output": os.path.join(SKILLS_DIR, "index.html"),
            "items": skills,
            "kind": "skills",
            "name": "Skills",
            "title": "Skills - Siddhartha Chaturvedi",
            "url": f"{SITE_URL}/{SKILLS_DIR}/",
            "kicker": f"Skills // {kicker_year}",
            "lede": "Longer, tool-using workflows for agents. One engine holds the method. "
                    "Adapters plug it into a system.",
            "description": "Agent skills by Siddhartha Chaturvedi: a grooming engine that judges content on three axes, "
                           "and adapters that plug it into real systems.",
            "search": "Search skills… (⌘K)",
            "prompts_href": "../",
            "skills_href": "./",
            "shelf": prompts_shelf,
        },
    ]

    for page in pages:
        # Escape "</" so text inside a prompt or skill can never close the data script tag.
        json_data = json.dumps(page["items"], indent=2).replace("</", "<\\/")
        values = {
            "PROMPTS_JSON": json_data,
            "PAGE_CONFIG": json.dumps({"kind": page["kind"]}),
            "SHELF_JSON": json.dumps(page["shelf"]).replace("</", "<\\/"),
            "PAGE_TITLE": page["title"],
            "PAGE_DESCRIPTION": page["description"],
            "PAGE_URL": page["url"],
            "PAGE_NAME": page["name"],
            "PAGE_KICKER": page["kicker"],
            "PAGE_LEDE": page["lede"],
            "SEARCH_PLACEHOLDER": page["search"],
            "PROMPTS_HREF": page["prompts_href"],
            "SKILLS_HREF": page["skills_href"],
            "PROMPTS_CURRENT": " current" if page["kind"] == "prompts" else "",
            "SKILLS_CURRENT": " current" if page["kind"] == "skills" else "",
            "YEAR": str(year),
        }
        html_output = template
        for key, value in values.items():
            html_output = html_output.replace("{{ " + key + " }}", value)
        leftover = re.findall(r"\{\{ [A-Z_]+ \}\}", html_output.split('<script id="prompts-data"')[0])
        assert not leftover, f"unfilled placeholders: {leftover}"

        output_path = os.path.join(base_dir, page["output"])
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"Successfully generated {output_path}")

    print(f"Categories: {', '.join(categories)}")

if __name__ == "__main__":
    build_site()
