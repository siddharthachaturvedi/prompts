# Grooming ledger

A record of every grooming pass on this library: what was judged, on what evidence, and what changed. Run with the [grooming-engine](../skills/grooming-engine/SKILL.md) and its [prompt-library adapter](../skills/prompt-library-grooming/SKILL.md).

**To undo a pass:** revert its commit. Nothing is ever deleted outside git.

## Pass 1 - 23 Nov 2026

### What the three axes found

- **Semantic.** No two prompts are true duplicates. The pairs that look alike by title - two Blue Ocean, two pre-mortems, two customer-profile, two go-to-market - do different jobs. Three prompts were **mislabeled**: their content had changed while their name and credit stayed (11, 20, 23).
- **Temporal, forward.** Nothing has expired. The prompts name no years, models, tools or URLs. The site's own description had: it still said "PM, OB, and prompt engineering" after the library grew to eight workstreams.
- **Temporal, backward.** This is where the damage was. The June 2026 rework (`91f6c6b`) moved every prompt into one shared structure and, on the way, dropped what made most of them distinct: named frameworks, exact formats, thresholds, interview patterns and all six source links.
- **Importance.** Unknown. The repository has no usage data, so the prompts cannot be ranked against each other. The one proxy available is stakes: a prompt that carries someone's name but not their method came first.

### Scorecard

| | Before | After |
|---|---|---|
| Prompts | 41 | 42 |
| Retired | - | 0 |
| Merged as duplicates | - | 0 |
| Mislabeled (name or credit no longer matched content) | 3 | 0 |
| Prompts credited to others that still carry the source's method | not checked | 18 of 18 |
| Source links | 0 | 6 |
| Refreshed this pass | - | 19 |
| Split into its own file | - | 1 |
| Words that are shared boilerplate | 52% | unchanged, on purpose |
| Not yet refreshed | - | 22 |

**Claim coverage for this pass.** 64 signature elements from the pre-rework versions were checked back in: 64 present. Of the lines this pass replaced, 16 had content that would have been lost; all 16 were carried into the new wording. 4 were dropped on purpose (below). Lost: 0.

### Dropped on purpose

| Prompt | Dropped | Why |
|---|---|---|
| 12 | "Ask no more than 3 questions at a time" | The source method is one question at a time |
| 20 | "First 90-day GTM plan" | The source forbids granular tactics. The 90-day plan lives in 35 |
| 21 | "Before/after narrative" | The restored from/to formula is the before and after |
| 23 | "Use repo inspection only when the user has asked for implementation" | Replaced by confirming permissions once at the start |

### Shared boilerplate - kept

The intake protocol and quality bar are word for word the same in all 41 files, and make up 52% of the library's words. That is redundant on the semantic axis and load-bearing on the importance axis: each prompt is copied out on its own, so each must carry the contract. Verdict: Keep. One side effect was fixed: the shared "ask up to 3 questions" contradicted the interview prompts, which now say their own pattern replaces it.

### Every prompt

Importance is `unknown` for all rows unless stated. "Eroded" means the June rework dropped durable content.

| # | Prompt | Semantic | Temporal | Verdict | Evidence and change |
|---|---|---|---|---|---|
| 00 | Meta Prompt to Auto-Prompt | Unique. Own rule said 2 questions, shared block said 3 | Valid | Refresh - done | The limit now states it replaces the shared one |
| 01 | Blue Ocean Value Innovation | Unique. Adjacent to 19, boundary held | Eroded: 5-7 competing factors, breaks the value-cost trade-off | Refresh - pending | |
| 02 | Lean MVP and Customer Validation | Unique. Shares assumption ranking with 14 | Eroded: hypothesis sentence format, one person one week limit | Refresh - pending | |
| 03 | Feature Prioritization | Unique | Eroded: explicit formula, show the arithmetic, tie-break rule | Refresh - pending | |
| 04 | A/B Test Experimentation | Unique | Eroded: hypothesis format, 80% power and alpha 0.05, one variable only, rollback plan | Refresh - pending | |
| 05 | Stakeholder Influence Strategy | Unique | Eroded: memo structure, objections with rebuttals | Refresh - pending | |
| 06 | Team Diagnostics | Unique | Eroded: Hackman's five conditions, symptom-cause-theory, fixes that fit one sprint | Refresh - pending | |
| 07 | Change Management Plan | Unique | Eroded: Kotter's eight steps, three phases with who-what-when, resistance behaviours | Refresh - pending | |
| 08 | Conflict Resolution | Unique | Eroded: Thomas-Kilmann modes, position versus interest, what each side gives up and gains | Refresh - pending | |
| 09 | Motivation and Job Redesign | Unique | Eroded: need ratings, change-to-need table, leading and lagging indicators | Refresh - pending | |
| 10 | Culture Intervention | Unique | Eroded: OCAI, one intervention per Schein level, re-measure at six months | Refresh - pending | |
| 11 | CRIT Framework Interrogator | **Mislabeled.** CRIT had been redefined as Claim-Reasons-Implications-Tests | Eroded | Refresh - done. Importance: credit at stake | Restored Context-Role-Interview-Task. The June content moved to 41 |
| 12 | Recursive Diagnostic Interviewer | Unique. Had become a generic questioner | Eroded | Refresh - done. Credit at stake | One question at a time, five areas in order, three-part synthesis |
| 13 | Market Reality Evaluator | Unique. An umbrella over 29, 30 and 37 by design | Eroded | Refresh - done. Credit at stake | Maturity, saturation, top five players, CAC by channel, breakeven conversion, difficulty score |
| 14 | Key Assumptions Finder | Unique. Shares assumption ranking with 02 | Eroded, lightly | Refresh - done. Credit at stake | Behaviour assumptions first, assumption-critical-test table |
| 15 | Strategic Pre-Mortem Analyzer | Unique. Strategy, where 28 is delivery | Eroded | Refresh - done. Credit at stake | Two-years-later frame, and the success retrospective that had vanished |
| 16 | JTBD Transcript Analysis | Unique | Eroded | Refresh - done. Credit at stake | Three core jobs, the six criteria for an outcome statement. Link restored |
| 17 | Multi-Framework Ideal Customer | Unique. Adjacent to 31. Title promised frameworks the body no longer had | Eroded | Refresh - done. Credit at stake | Framework choice by business type, psychographic profile |
| 18 | Unbiased Interview Architect | Unique | Eroded | Refresh - done. Credit at stake | The Mom Test by name, intro, warm-up, core and referral structure |
| 19 | Blue Ocean Strategy Catalyst | Unique. Adjacent to 01, boundary held | Eroded | Refresh - done. Credit at stake | Six paths, three named tiers, category tagline |
| 20 | GTM Mode Selector | **Mislabeled.** The four modes had been replaced by a motion comparison | Eroded | Refresh - done. Credit at stake | Steal, Expand, Defend, Stimulate restored. Motion comparison kept as step two. Link restored |
| 21 | Context-Aware Value Proposition | Unique | Eroded | Refresh - done. Credit at stake | Three propositions under 20 words, the from-to formula, emphasis by business type |
| 22 | User Story Mapper | Unique | Eroded | Refresh - done. Credit at stake | Five to seven steps, five fields per step |
| 23 | Autonomous PRD Execution Agent | **Mislabeled.** An agent that executes a PRD had become a PRD writer | Eroded | Refresh - done. Credit at stake | Executes story by story and stops for review. Drafts the PRD only if none exists |
| 24 | Investor Pitch Architect | Unique | Eroded | Refresh - done. Credit at stake | 10 to 12 slide arc, four fields per slide, the skeptical-partner pass. Link restored |
| 25 | Investor Readiness Scorecard | Unique | Eroded | Refresh - done. Credit at stake | Four diligence areas, documents investors ask for, five actions this week |
| 26 | Obviously Awesome Positioning | Unique | Eroded | Refresh - done. Credit at stake | Five components in order, interview option, positioning canvas. Link restored |
| 27 | Strategic Narrative Architect | Unique | Eroded | Refresh - done. Credit at stake | Five elements including the Promised Land. Link restored |
| 28 | Project Pre-Mortem Coach | Unique. Delivery, where 15 is strategy | Eroded | Refresh - done. Credit at stake | Coaching turn-taking, Mitchell and Klein's prospective hindsight. Link restored |
| 29 | Market Sizing & TAM Analysis | Unique | Not yet compared with its earlier version | Keep - check pending | |
| 30 | Competitive Landscape Deep Dive | Unique | Not yet compared | Keep - check pending | |
| 31 | Customer Persona & Segmentation | Unique. Adjacent to 17 | Not yet compared | Keep - check pending | Needs one scope line: stop at ranked segments |
| 32 | Industry Trend Analysis | Unique | Not yet compared | Keep - check pending | |
| 33 | SWOT + Five Forces | Unique | Not yet compared | Keep - check pending | |
| 34 | Pricing Strategy Analysis | Unique | Not yet compared | Keep - check pending | |
| 35 | Go-To-Market Strategy | Unique. Adjacent to 20 | Not yet compared | Keep - check pending | Needs one scope line: take the mode and motion as given |
| 36 | Customer Journey Mapping | Unique | Not yet compared | Keep - check pending | |
| 37 | Financial Modeling & Unit Economics | Unique | Not yet compared | Keep - check pending | |
| 38 | Risk Assessment & Scenario Planning | Unique | Not yet compared | Keep - check pending | |
| 39 | Market Entry & Expansion Strategy | Unique | Not yet compared | Keep - check pending | |
| 40 | Executive Strategy Synthesis | Unique | Not yet compared | Keep - check pending | |
| 41 | Argument Stress Test | Unique. New file | Valid | New | The claim, reasons, implications, tests audit that had been filed under the CRIT name |

### Ask - open questions for the owner

1. **Sources.** Twelve credited prompts have no source link and never had one in this repository: 11, 12, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25. No links were invented. Do the sources exist somewhere?
2. **Credits on the site.** The site has hidden the `by` line since February. Six prompts now show a Source button again. Is that the intent?
3. **Prompt 20's credit** now reads "r/startups community (u/nzdog), motion comparison added by Sid". Correct?
4. **Prompt 23** originally told the agent to run safe commands without asking. This pass kept the June stance: confirm permissions once, and always ask before anything destructive. Agreed?
5. **Pass 2.** Twenty-two of your own prompts are untouched: 01 to 10 have known erosion listed above, 29 to 40 have not been compared with their earlier versions. Run the same restore on them?
6. **Importance.** Which prompts get used? Without that, the ranking stays unknown.
7. **Shared block.** Keep the contract text in every file, or hold it once and let the build add it?

### Limits of this pass

- Restoring from git history recovers what this repository once said. The original sources were not re-read, so a credit is now consistent with the repository's earlier text, not verified against the author.
- Claim coverage was a second read by the same hand that did the rewrite. Before merging, read a few before-and-after pairs yourself: 11, 20 and 23 changed the most.
