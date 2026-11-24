# Plainspoken: research and design decisions

Researched 8 November 2026. This is a new synthesis, not a recovery of the user's missing earlier skill. The reviewed sources are mutable online versions; conclusions describe the material inspected on this date. This is a focused review of relevant approaches, not an exhaustive inventory of every writing skill.

## The design decision

Optimize for the effort required to understand and use an answer. Word count is only one contributor. A missing causal connection, ambiguous fragment, unexplained term, or absent qualification can make a shorter response harder to use.

The resulting skill combines action support, disciplined scope, natural prose, and protection of meaning. It adapts to the request: practical work, explanation, reflective discussion, and editing need different shapes. It has no mandatory response template, fixed word ceiling, or clinical claims.

## The three requested skills

### i-have-adhd

The [canonical instructions](https://github.com/ayghri/i-have-adhd/blob/main/skills/i-have-adhd/SKILL.md) emphasize actionable openings, small steps, visible progress, and accessible working state. The current version includes exceptions for explanation, user requests, and completeness; it is more flexible than summaries of it sometimes suggest.

**Adapt:** give an overwhelmed reader an attainable starting point, put prerequisites beside the action, and recover relevant state after interruptions. **Limit:** a philosophical question or emotional disclosure may need understanding rather than an instruction. Estimates should be grounded. Avoid assuming all readers share one memory profile or making biochemical claims about the user. Its README credits loose inspiration from an ADHD workbook; that is not clinical validation of the skill. [Project](https://github.com/ayghri/i-have-adhd)

Its [published internal evaluation](https://github.com/ayghri/i-have-adhd/blob/main/evals/RESULTS.md) used 14 cases and three trials with a same-model blind judge. Aggregate scores improved, but its release gate failed. One reported regression involved a definite causal explanation unsupported by the available facts. This is especially relevant to Plainspoken: decisiveness must not manufacture certainty. The evaluation is small and does not measure clinical or real-reader outcomes.

### Ponytail

The [current skill](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail/SKILL.md) is primarily about coding: understand the task, choose the smallest complete change, and retain the checks that correctness requires. It does not justify skipping affected callers or necessary validation.

**Adapt:** resolve the whole request while removing unnecessary work for both assistant and reader. **Limit:** a minimum code change is not a model for every essay. Importing recurring closing lines about omitted work and risks would create a new conversational ritual. Its [author-run benchmark](https://github.com/DietrichGebert/ponytail) concerns coding tasks, not prose comprehension. Those advertised outcomes were not independently reproduced here.

### Caveman

The [current core instructions](https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md) explicitly preserve meaning, negations, technical strings, and clarity in consequential instructions. Its emphasis on grammar and intelligibility is more nuanced than the name suggests.

**Adapt:** cut ceremonial language and repetition while protecting exact content. **Limit:** optional article dropping, fixed sentence ceilings, blanket restrictions on hedging, and an enduring persona can conflict with the reader's purpose. Inferences still need qualifying language. Reflective writing needs rhythm and room for ambiguity. Plainspoken therefore uses ordinary grammar and does not force terse speech into artifacts.

The repository now contains a larger runtime ecosystem. Reading the skill as a design source does not require installing its scripts, hooks, proxies, or telemetry. Only the newly written Plainspoken package is part of this deliverable.

## Related approaches

| Skill inspected | Useful mechanism | Boundary in Plainspoken |
| --- | --- | --- |
| [Humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md) | Detects structural habits such as staged openings, inflated significance, invented contrasts, and repetitive endings. Checks whether an edit changed the facts. | Return the finished piece without a compulsory draft-and-diagnosis display. Preserve the writer's punctuation and voice; do not invent experiences or feelings to sound human. |
| [Writing Clearly and Concisely](https://github.com/obra/the-elements-of-style/blob/main/skills/writing-clearly-and-concisely/SKILL.md) | Concrete expression, coherent paragraphs, close placement of related words, and deliberate emphasis. | Historical usage preferences do not override dialect, genre, or a requested voice. The full source reference need not load for routine replies. |
| [Feynman Technique](https://github.com/guicortei/feynman-technique/blob/main/skills/feynman-technique/SKILL.md) | Explain mechanisms, use observable examples, adapt to familiarity, and show where analogies stop working. | Do not force every answer through five levels or explain words the reader already knows. |
| [DeepRead](https://github.com/alirezarezvani/claude-skills/blob/main/research/deepread/SKILL.md) | Distinguish propositions, evidence, examples, assumptions, and objections; preserve unresolved questions. | Its detailed analytical format is useful for requested close reading, not every chat response. An illustration must not masquerade as proof. |
| [AI Socratic Tutor](https://github.com/bstellato/ai-teaching-skills/blob/main/ai-socratic-tutor/SKILL.md) | Locate the first missing connection and use a focused question when the user wants coaching. | Do not withhold an answer the user requested or turn ordinary explanations into quizzes. |

These are precedents for prompt design. Their popularity and installation counts do not establish effectiveness. The comparison informed an original instruction set rather than a concatenation of their rules.

## What the evidence supports

### Accessible organization

[W3C's succinct-text guidance](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p05-succinct-text/) recommends meaningful chunks, early purpose, and navigable structure. It explicitly acknowledges that a longer sentence can sometimes be clearer. Its [clear-words guidance](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p01-clear-words/) supports familiar vocabulary and explanations of unfamiliar terms. These are supplemental accessibility design patterns, not additional WCAG conformance requirements or experiments establishing an ideal chat length.

**Application:** use coherent paragraphs and task-appropriate lists. Simplify vocabulary when meaning survives. Retain a precise term when it earns its place and explain it as needed. These choices should respond to the actual reader, not a stereotype.

[Digital.gov's organization guidance](https://digital.gov/guides/plain-language/principles/organize) begins with audience needs, knowledge, and likely questions, then orders information accordingly. **Application:** lead with what the reader came for. For one request that is a recommendation; for another it is a distinction or a usable draft. Applying public-content guidance to assistant replies is a design inference.

### Memory and getting started

[W3C's memory guidance](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o6-memory/) argues for processes that do not depend on retaining information across steps. **Application:** bring necessary context forward at meaningful transitions and put needed information beside the task. Repeating the whole conversation each turn would add a different burden.

In four experiments totaling 1,196 participants, Gilbert studied external reminders for delayed intentions. Reminder use responded to memory demands and interruptions; reminders improved performance on the experimental task. Generalization to a naturalistic task was limited. [Gilbert, 2015](https://journals.sagepub.com/doi/10.1080/17470218.2014.972963)

**Application:** visible, actionable cues are plausible supports for practical work. This does not establish that every response should end with a two-minute task, or that a writing prompt treats ADHD. Plainspoken makes this behavior conditional on the user's goal.

### Coherence and the reader's knowledge

McNamara and Kintsch's experiments examined prior knowledge and text coherence. More coherent text helped some measures; knowledgeable readers sometimes benefited from supplying inferences themselves, and one result did not replicate across experiments. [McNamara & Kintsch, 1996](https://www.tandfonline.com/doi/abs/10.1080/01638539609544975)

**Application:** preserve causal connections and definitions that this reader needs. Adjust explanation to demonstrated familiarity. The experiments compare coherence, not simply short versus long text; they do not justify making prose obscure for experts.

Oppenheimer manipulated unnecessary language complexity and found lower judgments of author intelligence, with processing fluency mediating the effect. [Oppenheimer, 2006](https://onlinelibrary.wiley.com/doi/10.1002/acp.1178)

**Application:** choose a familiar word when it says the same thing. The outcome measured was perceived intelligence, not a universal proof about comprehension or all specialist vocabulary. This supports a preference, not a prohibited-word list.

### Compression and model performance

[JetBrains' paired Caveman benchmark](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/) reported about 8.5% fewer output tokens in its large paired run. Task-score differences were not statistically distinguishable in that setup. This was one model, harness, and task collection; lack of a significant difference does not establish equivalence or a universal savings rate. Code and tool calls also contribute to an agent's output, limiting what prose trimming can save.

The [CAVEWOMAN preprint](https://arxiv.org/abs/2606.24083) reports experiments on eight models and five datasets. Output compression often lowered realized cost, while input compression could increase cost and impair accuracy. Answers scored correct could still diverge semantically from the uncompressed reference. This review used the abstract's reported findings and did not reproduce the study or audit its full experimental record.

**Application:** measure preservation of useful meaning, not merely response length or whether a task passes. Neither study directly validates Plainspoken, and neither establishes a benefit for readers with ADHD.

## Conflicts resolved in the synthesis

| Tension | Decision |
| --- | --- |
| Action first versus thoughtful conversation | Start with the reader's purpose; use an action when action is wanted. |
| Brevity versus complete research | Preserve requested coverage, evidence, and counterarguments; improve organization. |
| Plain words versus precision | Keep useful specialist terms, define them, and use them consistently. |
| Confidence versus honest uncertainty | Separate observation, inference, and what would resolve the unknown. |
| Natural voice versus editing every distinctive feature | Preserve images, ambiguity, humor, and rhythm; an already effective sentence can stay unchanged. |
| Memory support versus repetitive recaps | Restore only the state needed at a transition or restart. |
| Warmth versus canned empathy | Attend to what was actually said without inventing feelings or personal knowledge. |
| Helpful defaults versus taking over | Use informed defaults, honor explicit preferences, and ask only consequential questions. |

## Attribution and limits

The wording and examples in this package are newly authored. Source skills were studied for mechanisms and tradeoffs, not installed or copied wholesale. Ponytail, i-have-adhd, Humanizer, Feynman Technique, and AI Socratic Tutor declare MIT; DeepRead's repository displays MIT. Caveman's current [licensing statement](https://github.com/JuliusBrussee/caveman/blob/main/LICENSING.md) reports Apache-2.0 from v3, while earlier versions used MIT. The Elements of Style repository describes the 1918 source as public domain; this review did not establish a separate license for every modern wrapper file. Anyone later copying source text should check the applicable version and notices.

This is an evidence-informed editorial synthesis. It is not a clinically validated intervention, a guarantee of token savings, or proof that one communication style suits everyone. The practical question is whether its answers preserve meaning, fit the request, and feel easier for this user to read. Independent response simulations and their limitations are recorded in the [validation report](validation.md).
