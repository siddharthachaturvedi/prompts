# 🧠 Prompt Engineering Repository

A curated collection of advanced system prompts, prompt architectures, and meta-prompts — designed for power users of LLMs.

**🌐 [View the live site →](https://sidprompts.netlify.app/)**

---

## What's Inside

Each prompt is a standalone Markdown file you can read, copy, and paste into any LLM interface. The collection spans meta-prompting strategies, role architectures, and structured output techniques.

| # | Prompt | Domain | Level |
|---|--------|--------|-------|
| 00 | [Meta Prompt to Auto-Prompt](00_meta_prompt_to_auto_prompt.md) | Meta | — |
| 01 | [Blue Ocean Value Innovation](01_blue_ocean_value_innovation.md) | PM | Advanced |
| 02 | [Lean MVP & Customer Validation](02_lean_mvp_customer_validation.md) | PM | Intermediate |
| 03 | [Feature Prioritization](03_feature_prioritization.md) | PM | Intermediate |
| 04 | [A/B Test Experimentation](04_ab_test_experimentation.md) | PM | Intermediate |
| 05 | [Stakeholder Influence Strategy](05_stakeholder_influence_strategy.md) | PM | Advanced |
| 06 | [Team Diagnostics](06_team_diagnostics.md) | OB | Intermediate |
| 07 | [Change Management Plan](07_change_management_plan.md) | OB | Advanced |
| 08 | [Conflict Resolution](08_conflict_resolution.md) | OB | Intermediate |
| 09 | [Motivation & Job Redesign](09_motivation_job_redesign.md) | OB | Intermediate |
| 10 | [Culture Intervention](10_culture_intervention.md) | OB | Advanced |

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
