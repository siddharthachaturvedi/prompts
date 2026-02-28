---
by: Kevin Leneway (Pioneer Square Labs)
category: Engineering & Execution
level: Advanced
---

# The Autonomous PRD Execution Agent

(Note: This prompt is designed to be fed directly into an AI-powered IDE like Cursor, referencing a pre-written markdown file named cursor-tasks.md containing the project's PRD and task checklist).

@cursor-tasks.md

Go through each story and task in the attached @cursor-tasks.md file. Find the next sequential story to work on.

Review each unfinished task within that story. Correct any immediate logical issues or ask for clarifications—but do so ONLY if absolutely needed to prevent a build failure.

Then, proceed to autonomously create or edit the necessary repository files to complete each task. After you complete all the tasks within a specific story, update the @cursor-tasks.md file to physically check off the completed tasks.

Run builds and commits after each story is finalized. Run all safe terminal commands without asking for my approval to maintain velocity. Continue executing each task sequentially until you have finished the entire story. Once the story is complete, stop execution and wait for me to review the code before proceeding to the next story block.
