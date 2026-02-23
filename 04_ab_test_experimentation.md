---
by: Sid
---

# A/B Test Experimentation

**Level:** Intermediate | **Domain:** Product Management | **Skill:** Experiment design & data interpretation

## Prompt

A PM wants to increase sign-ups by changing the homepage. Design an A/B test: define the hypothesis, the variation, key metrics, sample size / power considerations, and how you will decide if the change "worked". Include guardrails (e.g. avoiding feature creep) and error risks.

## Frameworks

- **A/B Testing** best practices (Kohavi et al.)
- Lean metrics (Build-Measure-Learn)
- Online controlled experiment literature

## Expected Deliverables

- Hypothesis (e.g. "greater clarity increases sign-up by X%")
- Test plan: variation vs control
- Metric definition (primary / secondary)
- Sample / power outline
- Decision criteria and guardrails

## Scoring Rubric (10 points)

| Criterion | Weight | 5 (Excellent) | 3 (Good) | 1 (Insufficient) |
|---|---:|---|---|---|
| Hypothesis clarity | 3 | Specific effect stated with context | General effect ("improve") | No clear hypothesis |
| Metrics and design | 3 | Correct metrics (primary / guardrail) and sample | Metrics identified, sample vague | Missing metrics or sample details |
| Decision rules (stats) | 2 | Proper use of significance / power (explained) | Acknowledged p-value or CI only | No statistical criteria |
| Consideration of risks | 2 | Addresses real risks (guardrails, novelty bias) | Mentions basic risk (traffic) | Ignores risk factors |

## LLM Tips

- Use **stepwise decomposition** ("First state hypothesis, then design…")
- Provide one sample A/B plan as few-shot reference
- Encourage CoT to justify sample size
- Set a low temperature for numeric precision
