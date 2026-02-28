import os
import json
import re

def create_title(filename):
    """Convert filename like '00_meta_prompt.md' into '00 - Meta Prompt'"""
    name, _ = os.path.splitext(filename)
    
    match = re.match(r'^(\d+)[_-](.*)', name)
    if match:
        num = match.group(1)
        rest = match.group(2)
        rest = rest.replace('_', ' ').replace('-', ' ').title()
        return f"{num} - {rest}"
    else:
        return name.replace('_', ' ').replace('-', ' ').title()

def word_count(text):
    """Count words in a string."""
    return len(text.split())

def build_site():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    prompts = []
    
    for filename in os.listdir(base_dir):
        if filename.endswith(".md") and filename != "README.md":
            filepath = os.path.join(base_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            title = create_title(filename)
            
            # Parse optional frontmatter (---\nkey: val\n---)
            by = ""
            category = ""
            level = ""
            link = ""
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
                            if key == "by":
                                by = val
                            elif key == "category":
                                category = val
                            elif key == "level":
                                level = val
                            elif key == "link":
                                link = val
            
            prompts.append({
                "filename": filename,
                "title": title,
                "by": by,
                "category": category,
                "level": level,
                "link": link,
                "words": word_count(content),
                "content": content
            })
            
    print(f"Found {len(prompts)} prompts.")
    
    # Collect unique categories for template
    categories = sorted(set(p["category"] for p in prompts if p["category"]))
    
    template_path = os.path.join(base_dir, "template.html")
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
        
    json_data = json.dumps(prompts, indent=2)
    html_output = template.replace("{{ PROMPTS_JSON }}", json_data)
    
    output_path = os.path.join(base_dir, "index.html")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_output)
        
    print(f"Successfully generated {output_path}")
    print(f"Categories: {', '.join(categories)}")

if __name__ == "__main__":
    build_site()
