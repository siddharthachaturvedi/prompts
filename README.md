# 🧠 Prompt Engineering Repository

A curated collection of advanced system prompts, prompt architectures, and meta-prompts — designed for power users of LLMs.

**🌐 [View the live site →](https://prompts.sidc.ai/)**

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
| 11 | [Crit Framework Interrogator](11_crit_framework_interrogator.md) | Meta | Advanced |
| 12 | [Recursive Diagnostic Interviewer](12_recursive_diagnostic_interviewer.md) | Meta | Advanced |
| 13 | [Market Reality Evaluator](13_market_reality_evaluator.md) | PM | Advanced |
| 14 | [Key Assumptions Finder](14_key_assumptions_finder.md) | Meta | Intermediate |
| 15 | [Strategic Pre-Mortem Analyzer](15_strategic_pre_mortem_analyzer.md) | PM | Advanced |
| 16 | [JTBD Transcript Analysis](16_jtbd_transcript_analysis.md) | PM | Advanced |
| 17 | [Multi-Framework Ideal Customer](17_multi_framework_ideal_customer.md) | PM | Advanced |
| 18 | [Unbiased Interview Architect](18_unbiased_interview_architect.md) | PM | Intermediate |
| 19 | [Blue Ocean Strategy Catalyst](19_blue_ocean_strategy_catalyst.md) | PM | Advanced |
| 20 | [GTM Mode Selector](20_gtm_mode_selector.md) | PM | Intermediate |
| 21 | [Context-Aware Value Proposition](21_context_aware_value_proposition.md) | PM | Intermediate |
| 22 | [User Story Mapper](22_user_story_mapper.md) | PM | Intermediate |
| 23 | [Autonomous PRD Execution Agent](23_autonomous_prd_execution_agent.md) | PM | Advanced |
| 24 | [Investor Pitch Architect](24_investor_pitch_architect.md) | PM | Advanced |
| 25 | [Investor Readiness Scorecard](25_investor_readiness_scorecard.md) | PM | Intermediate |
| 26 | [Obviously Awesome Positioning](26_obviously_awesome_positioning.md) | PM | Advanced |
| 27 | [Strategic Narrative Architect](27_strategic_narrative_architect.md) | PM | Advanced |
| 28 | [Project Pre-Mortem Coach](28_project_pre_mortem_coach.md) | PM | Intermediate |
| 29 | [Market Sizing & TAM Analysis](29_market_sizing_tam_analysis.md) | Consulting | Advanced |
| 30 | [Competitive Landscape Deep Dive](30_competitive_landscape_deep_dive.md) | Consulting | Advanced |
| 31 | [Customer Persona & Segmentation](31_customer_persona_segmentation.md) | Consulting | Advanced |
| 32 | [Industry Trend Analysis](32_industry_trend_analysis.md) | Consulting | Advanced |
| 33 | [SWOT + Five Forces](33_swot_five_forces.md) | Consulting | Advanced |
| 34 | [Pricing Strategy Analysis](34_pricing_strategy_analysis.md) | Consulting | Advanced |
| 35 | [Go-To-Market Strategy](35_go_to_market_strategy.md) | Consulting | Advanced |
| 36 | [Customer Journey Mapping](36_customer_journey_mapping.md) | Consulting | Advanced |
| 37 | [Financial Modeling & Unit Economics](37_financial_modeling_unit_economics.md) | Consulting | Advanced |
| 38 | [Risk Assessment & Scenario Planning](38_risk_assessment_scenario_planning.md) | Consulting | Advanced |
| 39 | [Market Entry & Expansion Strategy](39_market_entry_expansion_strategy.md) | Consulting | Advanced |
| 40 | [Executive Strategy Synthesis](40_executive_strategy_synthesis.md) | Consulting | Advanced |

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
