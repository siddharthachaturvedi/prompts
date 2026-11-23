# Prompt Engineering Repository

A curated library of decision-grade prompts for MBA students, executives, startup operators, and strategy teams.

Live site: [prompts.sidc.ai](https://prompts.sidc.ai/)

## Organization

The library is MECE at two levels, and the build fails if it stops being so.

- **Every prompt sits in exactly one workstream.** On the site each workstream shows as a verb, in path order: Think, Discover, Size up, Build, Sell, Fund, Run, Decide.
- **Every prompt answers exactly one question, and no two prompts answer the same one.** The `step` orders the questions inside a workstream.

Prompts that neighbour each other carry one rule saying where they stop. Known gaps - questions a workstream does not answer yet - are listed in the [ledger](grooming/LEDGER.md). Cross-cutting methods such as JTBD, TAM, SWOT, PRD, A/B testing, and Blue Ocean live in `tags`, not as overlapping categories.

### Prompting & Thinking Systems

| Step | Answers | Prompt | Level | Tags |
|---|---|---|---|---|
| 1 | How do I make this prompt better? | [Meta Prompt to Auto-Prompt](00_meta_prompt_to_auto_prompt.md) | Advanced | prompt design, prompt critique, output quality, meta-prompting |
| 2 | What do you need to know before advising me? | [CRIT Framework Interrogator](11_crit_framework_interrogator.md) | Intermediate | prompt design, CRIT, interview, context gathering |
| 3 | What is the real problem here? | [Recursive Diagnostic Interviewer](12_recursive_diagnostic_interviewer.md) | Advanced | diagnosis, questioning, root cause, coaching |

### Customer Discovery & Segmentation

| Step | Answers | Prompt | Level | Tags |
|---|---|---|---|---|
| 1 | What should I ask customers? | [Unbiased Interview Architect](18_unbiased_interview_architect.md) | Beginner | customer interviews, research script, bias reduction, discovery |
| 2 | What did customers actually tell me? | [JTBD Transcript Analysis](16_jtbd_transcript_analysis.md) | Advanced | JTBD, interview analysis, customer motivation, outcome statements |
| 3 | Which groups of customers are there? | [Customer Persona & Segmentation](31_customer_persona_segmentation.md) | Advanced | segmentation, personas, ICP, customer strategy |
| 4 | Who is the best-fit customer? | [Multi-Framework Ideal Customer](17_multi_framework_ideal_customer.md) | Advanced | ICP, segmentation, customer strategy, personas |
| 5 | Where does their experience break? | [Customer Journey Mapping](36_customer_journey_mapping.md) | Advanced | customer journey, experience design, touchpoints, service blueprint |
| 6 | How do I test this idea cheaply? | [Lean MVP and Customer Validation](02_lean_mvp_customer_validation.md) | Intermediate | lean startup, MVP, customer discovery, experiments, validation |

### Market & Competitive Intelligence

| Step | Answers | Prompt | Level | Tags |
|---|---|---|---|---|
| 1 | How big is the market? | [Market Sizing & TAM Analysis](29_market_sizing_tam_analysis.md) | Advanced | TAM, SAM, SOM, market sizing, source triangulation |
| 2 | Who else is in it? | [Competitive Landscape Deep Dive](30_competitive_landscape_deep_dive.md) | Advanced | competitive analysis, alternatives, market map, strategy |
| 3 | What is changing? | [Industry Trend Analysis](32_industry_trend_analysis.md) | Advanced | industry trends, market timing, PESTLE, scenarios |
| 4 | Is the market structurally attractive? | [SWOT + Five Forces](33_swot_five_forces.md) | Advanced | SWOT, Porter Five Forces, industry structure, strategy |
| 5 | Where is the uncontested space? | [Blue Ocean Strategy Catalyst](19_blue_ocean_strategy_catalyst.md) | Advanced | category creation, noncustomers, blue ocean, strategic moves |
| 6 | How do I redesign the offer to stand apart? | [Blue Ocean Value Innovation](01_blue_ocean_value_innovation.md) | Advanced | blue ocean, ERRC, value curve, market creation, strategy |
| 7 | Is this worth pursuing at all? | [Market Reality Evaluator](13_market_reality_evaluator.md) | Advanced | startup evaluation, market attractiveness, competition, unit economics |

### Product Planning & Experimentation

| Step | Answers | Prompt | Level | Tags |
|---|---|---|---|---|
| 1 | What should we build first? | [Feature Prioritization](03_feature_prioritization.md) | Intermediate | prioritization, roadmap, RICE, Kano, tradeoffs |
| 2 | What goes in the first release? | [User Story Mapper](22_user_story_mapper.md) | Intermediate | user stories, product discovery, roadmap, agile |
| 3 | Can an agent build it, story by story? | [Autonomous PRD Execution Agent](23_autonomous_prd_execution_agent.md) | Advanced | PRD, execution agent, product specification, delivery |
| 4 | How do I test this change properly? | [A/B Test Experimentation](04_ab_test_experimentation.md) | Intermediate | A/B testing, experimentation, metrics, statistical design |

### Positioning, Pricing & GTM

| Step | Answers | Prompt | Level | Tags |
|---|---|---|---|---|
| 1 | What are we, and for whom? | [Obviously Awesome Positioning](26_obviously_awesome_positioning.md) | Advanced | positioning, April Dunford, category, competitive alternatives |
| 2 | How do I say it in one line? | [Context-Aware Value Proposition](21_context_aware_value_proposition.md) | Intermediate | value proposition, messaging, customer context, positioning |
| 3 | What story makes change feel necessary? | [Strategic Narrative Architect](27_strategic_narrative_architect.md) | Advanced | strategic narrative, category design, executive storytelling, sales narrative |
| 4 | What should it cost? | [Pricing Strategy Analysis](34_pricing_strategy_analysis.md) | Advanced | pricing, monetization, willingness to pay, packaging |
| 5 | Which way of selling fits? | [GTM Mode Selector](20_gtm_mode_selector.md) | Advanced | GTM, distribution strategy, sales motion, growth model |
| 6 | How do we launch? | [Go-To-Market Strategy](35_go_to_market_strategy.md) | Advanced | GTM strategy, launch, channels, sales, growth |
| 7 | How do we enter a new market? | [Market Entry & Expansion Strategy](39_market_entry_expansion_strategy.md) | Advanced | market entry, expansion, international strategy, beachhead |

### Finance & Fundraising

| Step | Answers | Prompt | Level | Tags |
|---|---|---|---|---|
| 1 | Do the numbers work? | [Financial Modeling & Unit Economics](37_financial_modeling_unit_economics.md) | Advanced | unit economics, financial model, CAC, LTV, contribution margin |
| 2 | Are we ready to raise? | [Investor Readiness Scorecard](25_investor_readiness_scorecard.md) | Intermediate | fundraising readiness, investor diligence, startup metrics, scorecard |
| 3 | How do I pitch it? | [Investor Pitch Architect](24_investor_pitch_architect.md) | Advanced | fundraising, pitch deck, investor narrative, venture capital |

### Org Design & Change

| Step | Answers | Prompt | Level | Tags |
|---|---|---|---|---|
| 1 | Why is the team underperforming? | [Team Diagnostics](06_team_diagnostics.md) | Intermediate | team effectiveness, operating model, org behavior, leadership |
| 2 | How do I make the work motivating? | [Motivation and Job Redesign](09_motivation_job_redesign.md) | Intermediate | motivation, job design, incentives, leadership, org behavior |
| 3 | How do I resolve this conflict? | [Conflict Resolution](08_conflict_resolution.md) | Intermediate | conflict, negotiation, leadership, communication |
| 4 | How do I win support for this? | [Stakeholder Influence Strategy](05_stakeholder_influence_strategy.md) | Advanced | stakeholder management, influence, executive communication, politics |
| 5 | How do I get people to adopt a change? | [Change Management Plan](07_change_management_plan.md) | Advanced | change management, ADKAR, operating change, adoption |
| 6 | How do I shift the culture? | [Culture Intervention](10_culture_intervention.md) | Advanced | culture, Schein, competing values, org change |

### Decision Quality & Executive Synthesis

| Step | Answers | Prompt | Level | Tags |
|---|---|---|---|---|
| 1 | What am I assuming? | [Key Assumptions Finder](14_key_assumptions_finder.md) | Beginner | assumptions, uncertainty, decision quality, validation |
| 2 | Does this argument hold? | [Argument Stress Test](41_argument_stress_test.md) | Intermediate | critical thinking, assumptions, reasoning, challenge |
| 3 | How could this strategy fail? | [Strategic Pre-Mortem Analyzer](15_strategic_pre_mortem_analyzer.md) | Intermediate | pre-mortem, strategy risk, decision quality, failure modes |
| 4 | How could this project fail? | [Project Pre-Mortem Coach](28_project_pre_mortem_coach.md) | Intermediate | project risk, execution, pre-mortem, delivery planning |
| 5 | What if the future goes differently? | [Risk Assessment & Scenario Planning](38_risk_assessment_scenario_planning.md) | Advanced | scenario planning, risk assessment, uncertainty, strategy |
| 6 | What is the recommendation? | [Executive Strategy Synthesis](40_executive_strategy_synthesis.md) | Advanced | executive synthesis, board memo, strategy recommendation, decision memo |

## Prompt Quality Contract

Each prompt should be useful in three contexts: a demanding MBA classroom, an executive decision meeting, and a startup operating review. New prompts should include:

- A clear use case and expert role
- An intake protocol that asks up to 3 high-value questions when context is missing
- Required inputs
- A structured method
- A decision-ready output format
- Rules for assumptions, evidence quality, tradeoffs, and confidence
- MECE frontmatter: `by`, `category`, `question`, `step`, `level`, and `tags`, plus `link` to the source when the prompt is adapted from someone else's work
- When a prompt is adapted, its content must still carry the source's method. A credit on a prompt that no longer contains the credited idea is worse than no credit

## Using the Website

The build writes two self-contained pages: `index.html` for prompts and `skills/index.html` for skills. No server is required after build. The look follows [sidc.ai](https://sidc.ai): its palette, type and breadcrumb bar. The tokens sit at the top of `template.html`.

- Browse prompts along the path: eight moves, in the order a venture meets them - Think, Discover, Size up, Build, Sell, Fund, Run, Decide
- Skills have their own page at [prompts.sidc.ai/skills](https://prompts.sidc.ai/skills/)
- Search across titles, workstreams, tags, and prompt text
- Filter by level
- Sort by number, title, or length
- Toggle between rendered view and raw editable source
- Edit the raw source before copying or launching in an LLM

## Contributing a Prompt

1. Create a Markdown file named `XX_short_name.md`, for example `42_board_memo.md`. Numbers are identities, so never reuse or renumber one.
2. Use frontmatter with `by`, one MECE `category`, the one `question` it answers, its `step` inside that workstream, `level`, comma-separated `tags`, and `link` if there is a source. If the new prompt belongs between two existing ones, renumber the `step` values after it. Add `mode: interview` if the prompt asks the user questions in turn, or `mode: agent` if it acts inside a repository.
3. Start the body with a `# Title` heading.
4. Follow the prompt quality contract above.
5. Run the build and review the generated site.

```bash
python3 build.py
open index.html
```

## Building Locally

```bash
python3 build.py
python3 -m http.server 8123
```

Then open [http://localhost:8123/index.html](http://localhost:8123/index.html).

No build dependencies beyond Python 3. The site loads Inter, Playfair Display, JetBrains Mono, and marked.js from CDNs at runtime.

## Skills

Longer, tool-using workflows live in [`skills/`](skills/). They have their own page at [prompts.sidc.ai/skills](https://prompts.sidc.ai/skills/): one engine and its adapters, each with a download button. They are also on the landing page itself: a door under the title, and a full Skills section below the prompts. Searching there finds skills too.

| Skill | What it does |
|---|---|
| [grooming-engine](skills/grooming-engine/SKILL.md) | The shared core. Judges every item on three axes - semantic, temporal, importance - then keeps, refreshes, distills or retires it, with a ledger |
| [confluence-distill-archive](skills/confluence-distill-archive/SKILL.md) | Adapter: grooms a Confluence space through the Atlassian Rovo MCP |
| [prompt-library-grooming](skills/prompt-library-grooming/SKILL.md) | Adapter: grooms a prompt library kept in git. This library is groomed with it - see the [ledger](grooming/LEDGER.md) |

### Contributing a Skill

1. Create a folder `skills/<skill-name>/` with a `SKILL.md` inside.
2. Use the standard skill frontmatter only: `name` and a one-line `description`. Keep the description free of `: ` so it stays valid YAML.
3. Start the body with a `# Title` heading. The site uses it as the card title.
4. Run the build and review the generated site.

## License

MIT. Use, remix, and share freely.
