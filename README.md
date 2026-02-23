# 🧠 Prompt Engineering Repository

A curated collection of advanced system prompts, prompt architectures, and meta-prompts — designed for power users of LLMs.

**🌐 [View the live site →](https://siddharthachaturvedi.github.io/prompts/)**

---

## What's Inside

Each prompt is a standalone Markdown file you can read, copy, and paste into any LLM interface. The collection spans meta-prompting strategies, role architectures, and structured output techniques.

| # | Prompt | Purpose |
|---|--------|---------|
| 00 | [Meta Prompt to Auto-Prompt](00_meta_prompt_to_auto_prompt.md) | Refines any draft prompt into a high-precision system prompt |

> More prompts added regularly. Star & watch the repo to stay updated.

---

## Using the Website

The HTML site is a single self-contained `index.html` — no server required.

- **Browse** prompts from the sidebar
- **Search** to filter by name
- **Toggle** between rendered view and raw editable source
- **Edit** the raw source to tweak it before copying
- **Copy** with one click

---

## Contributing a Prompt

1. Create a Markdown file: `XX_short_name.md` (e.g. `01_code_reviewer.md`)
2. Start the file with a `# Title` header
3. Run the build:
   ```bash
   python3 build.py
   ```
4. Open `index.html` to verify, then submit a PR.

---

## Building Locally

```bash
# Generate the site
python3 build.py

# Open in browser (macOS)
open index.html
```

No dependencies beyond Python 3. The template pulls `Inter` font and `marked.js` from CDN at runtime.

---

## License

MIT — use, remix, and share freely.
