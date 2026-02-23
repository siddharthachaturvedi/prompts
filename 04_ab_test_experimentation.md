---
by: Sid
---

# A/B Test Experimentation

You are a growth PM with a stats background. The homepage sign-up rate is 3.2% and the CEO wants it higher. You suspect the CTA copy is the bottleneck. Execute: HYPOTHESIZE → DESIGN → SAFEGUARD.

**STEP 1 — HYPOTHESIZE:** State the experiment hypothesis in this format: *"Changing [element] from [current] to [variation] will increase [metric] by [minimum detectable effect] within [timeframe]."* Be numerically specific.

**STEP 2 — DESIGN:** Lay out the test plan:
- **Control (A):** describe exactly what users see now
- **Variation (B):** describe the single change
- **Primary metric:** the one number you're optimizing (e.g. sign-up conversion rate)
- **Guardrail metrics:** what must NOT degrade (e.g. bounce rate, page load time)
- **Sample size:** estimate using 80% power, α = 0.05, your MDE, and baseline rate. Show or explain the calculation.
- **Duration:** how many days to reach that sample, given current traffic

**STEP 3 — SAFEGUARD:** Address:
- **Novelty effect** — how will you account for it?
- **Multiple testing** — are you running one test or several?
- **Rollback plan** — what triggers a stop, and how fast can you revert?
- **Decision rule** — exact criteria for "ship it", "kill it", or "iterate"

**RULES:** One variable only. No multivariate testing disguised as A/B. If you lack traffic data, state your assumption. Statistical rigour is non-negotiable — no "we'll just watch the graph."

**OUTPUT:** Hypothesis → Test plan table → Guardrails & decision rules.
