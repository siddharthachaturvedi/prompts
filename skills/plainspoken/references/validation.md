# Initial validation

8 November 2026. This is a small qualitative review, not a controlled comparison or a user study.

## Method

An independent evaluator received the skill and seven response-only requests. It could read the calibration examples. A second evaluator read only the core instructions and answered five additional cases, including a two-turn style switch. The primary author inspected both sets of actual responses. No external actions were performed by the simulated replies.

The first set overlaps substantially with the calibration examples. It mainly checks faithful application. The second set uses different content and checks transfer, but remains unblinded and uses a model evaluator. No baseline comparison, repeated trials, reader-comprehension measurements, or token-savings claim is available.

## Observed results

| Case | What was checked | Observation |
| --- | --- | --- |
| Pilot study rewrite | Uncertainty, 8% figure, two-site limitation, seasonal confounding, causal caution | Retained |
| Personal essay opening | Images and unresolved emotional meaning | Original retained because it already worked |
| Three unfinished drafts | Usable starting point without a large plan | One draft and one rough sentence |
| Forgiveness and responsibility | Requested depth and serious objection | 445-word response, with an objection and qualified position |
| Folder rename status | Completed action versus uninspected app label | Distinguished explicitly |
| Sadness without advice | Respect for requested emotional support | No checklist or task; general examples were framed as possibilities |
| API explanation | Familiar context plus mechanism | Spreadsheet example and request/response relationship |
| Renewal condition | Necessary condition, exact deadline, UTC, subsidiary exception, Q3 | All retained; ambiguous referent not silently resolved |
| Hometown paragraph | Tentative voice and metaphor | Original retained |
| Partial CSV export | 218/240 rows, HTTP 429, no retries, unknown cause | Reported 22 missing rows and uncertainty |
| Floating-point explanation | Actual mechanism for a reader who understands fractions | Binary denominator restriction, finite precision, and separate rounding explained |
| One-off edit then ornate invitation | Local scope and new stylistic instruction | Later request honored |

No substantive loss of meaning was identified in these responses. This does not establish that losses will never occur.

## Selected held-out outputs

### Conditional wording

Input: “We cannot renew unless the audit finishes by 17:00 UTC on 12 November; subsidiaries are exempt only if they had no transactions in Q3.”

Output: “We can renew only if the audit finishes by 17:00 UTC on 12 November. Subsidiaries are exempt only if they had no transactions in Q3.”

The necessary condition remains necessary rather than becoming a sufficient guarantee. The original does not specify the referent of the exemption; the rewrite does not invent one.

### Partial completion

Output: “The export is incomplete: it contains 218 of 240 rows, so 22 are missing. The API returned HTTP 429, a rate-limit response. I haven't retried yet, and I don't know why the limit was reached.”

This reports the observed error without inventing a cause such as an exhausted daily quota.

### Voice preservation

Input and output: “I envy people who call a city home without first checking whether it still wants them. Mine remembers me, I think. I'm less sure it recognises me.”

The evaluator chose not to change already effective prose. That is defensible, though a user may want a short explanation when they expected an edit. The skill permits commentary when a material choice needs explanation.

## Review changes

An additional critique suggested two clarifications, both incorporated: preserve the full coverage requested by the user, and honor an explicitly requested chat-wide style until the user changes it. No further rules were added from hypothetical failures.

## What to test next in actual use

Look for whether the reader asks for missing connections, more depth, less repetition, or recovery of their original voice. Revise the narrow instruction responsible for a demonstrated problem. Avoid growing a blacklist of words or adding compulsory output sections.
