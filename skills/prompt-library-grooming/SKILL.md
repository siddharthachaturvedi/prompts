---
name: prompt-library-grooming
description: Groom a library of prompts kept as files in a git repository - the prompt-library adapter for the grooming-engine skill. Finds prompts that drifted from their name or credit, content that past rewrites dropped, real duplicates and shared boilerplate, then refreshes, merges or retires them through a pull request. Use whenever the user asks to groom, clean up, dedupe, consolidate, audit or rebuild a prompt library, a prompts repo or a collection of system prompts.
---

# Prompt library grooming

This is an adapter. The method lives in the **grooming-engine** skill. Load that skill first and follow its workflow. This file supplies only what is specific to a prompt library in git.

If the engine is not available, tell the user it is needed. The short version meanwhile: judge every prompt separately on what it does (semantic), whether it is still true and what past edits dropped (temporal), and what is lost if it goes (importance). Move durable content first. Retire by moving, never by deleting. Put the whole plan in a pull request.

## Scope unit

One repository or one folder of prompt files per pass.

## Inventory

List every prompt file. For each one record:

- Frontmatter: credit, category, level, tags, source link
- The job, in one line: who uses it, on what input, to get what output
- Its unique content, with any block shared across the library stripped out
- Its history: `git log --follow` on the file, and the text before each large rewrite

Measure shared boilerplate before judging anything. Count the lines that appear word for word in many files. It tells you how much of each prompt is its own.

## Signals for each axis

| Axis | Evidence in a prompt library |
|---|---|
| Semantic | The job each prompt does and the output it produces. Two prompts overlap when they do the same job for the same output, not when they share a framework or a word in the title. A prompt is **mislabeled** when its content no longer matches its name, its credit or its tags |
| Temporal, forward | Named models, tools, products, years, URLs and statistics. Evergreen methods do not expire |
| Temporal, backward | `git show <commit>:<file>` for the version before each rewrite. List what the old version held that the current one lacks: the signature mechanism, named frameworks, exact formats, thresholds, interaction pattern, source link |
| Importance | Usage analytics if the site has any. Otherwise only proxies: whether it is the only prompt for its job, whether a credit to a named person is still accurate, and coverage gaps by level or category. With no usage data, importance between prompts is `unknown` - ask the owner |

A wrong credit outranks a missing detail. A prompt that carries someone's name but no longer contains their method is the first thing to fix.

## Types

| Type | What it is | How it goes stale |
|---|---|---|
| Method prompt | Applies a named framework | When a rewrite flattens the framework into generic steps |
| Credited prompt | Adapted from a named author or community | When its content drifts from the source while the credit stays |
| Interview prompt | Works by asking the user questions in turn | When a rewrite turns it into a one-shot answer |
| Contract block | Text every prompt carries so it stands alone when copied | It does not. It is deliberate repetition |

## Verbs

- **Refresh.** Edit the file in place. Restore what was lost into the library's current structure. Keep improvements the rewrite made, such as replacing a hard-coded scenario with the user's own inputs.
- **Distill.** Merge true duplicates into one survivor. When one file holds two different jobs, split the second into its own file under an honest name.
- **Retire.** Move the file to an `archive/` folder with a frontmatter line naming what replaced it. Git keeps the rest.
- **Undo.** Revert the commit.

File names and numbers are identities, because links point at them. Never renumber. A new prompt takes the next free number.

## Pointers

Links to a prompt use its file name. If a prompt is retired, the site needs a redirect from the old name to the survivor, and the README index needs the row moved or removed.

## Approval surface

A pull request. The branch is the draft and the merge is the yes. Put the Ask list in the pull request description.

## Ledger location

`grooming/LEDGER.md` in the repository, outside the folder the site build reads. One row per prompt, including the ones that were kept.

## Known limits

- **No usage data in a repo.** It cannot tell which prompts people use.
- **Sources are not re-read.** Restoring from git history recovers what the repo once said. It does not confirm the repo matched the original author in the first place. Say so when a credit matters.
- **Shared blocks cut both ways.** A contract block that every prompt carries can contradict one prompt's own rules. Check each prompt against the block it inherits.
