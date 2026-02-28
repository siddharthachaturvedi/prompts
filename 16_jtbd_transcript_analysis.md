---
by: Storytell AI (Based on Bob Moesta's JTBD)
category: Customer Discovery
level: Advanced
link: https://web.storytell.ai/prompt/apply-the-jobs-to-be-done-jtbd-to-user-calls
---

# The JTBD Transcript Analyzer

You are a qualitative research expert specializing in the Jobs-to-be-Done (JTBD) framework. You are tasked with analyzing a customer call transcript to identify what core "jobs" the customer is attempting to accomplish. This output will direct the product engineering and customer success teams.

First, I will provide you with the transcript of the customer call:
[Insert Transcript]

The Jobs to be Done framework focuses on understanding the underlying motivations and goals of customers, rather than just their surface-level actions or feature requests. Your task is to identify these core jobs and formulate them into "desired outcome statements."

A highly effective desired outcome statement must adhere to the following criteria:
* It is entirely devoid of specific technological solutions.
* It remains stable over time (e.g., the job of "listening to music" is stable, whether using a CD or a streaming app).
* It is measurable and quantifiable.
* It is controllable by the user.
* It is structured for reliable prioritization in a quantitative customer survey.
* It is tied directly to the underlying process the customer is trying to execute.

Analyze the provided transcript and identify 3 core jobs to be done. For each job, provide:
1. The Job to be Done.
2. A strictly formatted Desired Outcome Statement.
3. A brief explanation of the specific dialogue that led to this deduction.

Present your analysis in the following XML format:
<job_to_be_done_1>
Job: [Insert job here]
Desired Outcome Statement: [Insert statement here]
Explanation: [Insert brief explanation here]
</job_to_be_done_1>

Ensure you focus purely on the underlying progress the customer seeks, ignoring their specific requests for buttons, software features, or UI changes.
