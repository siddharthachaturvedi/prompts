---
name: handoff
description: Moves work between agents or sessions with nothing lost - a brief going out that says where things stand and what the receiver may do, and a report coming back that says what changed and what was not verified. Use when the user asks to hand off, pick up a brief or a handoff note, continue in another tool, move a chat somewhere else, brief another agent, wrap up a long session, or report on finished work.
---

# Handoff

Work moves in two directions, and each direction has one document.

| Document | Direction | The question it answers |
|---|---|---|
| **Brief** | Out, with the work | What do I need to continue correctly? |
| **Report** | Back, with the result | What is now true, and how sure are you? |

Use the brief when work moves on: to another agent, another tool, another day, or another person. Use the report when work comes back.

## The brief

A new session knows only what the brief tells it. Everything else you learned is gone. The brief is not a summary of what happened. It is the smallest set of facts and rules that lets a stranger continue correctly.

### Before you write

Check the state. Do not write it from memory.

- **Where the work lives.** Repository, folder, document or system. Give an address the receiver can reach, such as a remote URL. A path on your own machine helps nobody else.
- **The exact state.** Branch and commit, open pull requests, uncommitted changes, what is live and what is only local.
- **What is durable.** Say which facts are already recorded in the work itself, and which exist only in this conversation. Only the second kind needs the brief.

Run every check you can. Known limits is for what you tried and could not check. It is not a place to park a check you skipped.

Do not state an absence you did not look for. "No open pull requests" and "nothing deploys automatically" are claims. Check them, or list them as unknown.

### The six sections

Each section answers one question. Together they cover everything a receiver needs, and they do not overlap.

| Section | Question it answers | What goes in |
|---|---|---|
| **Where** | What exists, and in what state? | Address, exact state, and the three to five files to read first |
| **How it works** | What would I get wrong by guessing? | Only the mechanics that are not obvious: generated files, build checks, naming rules, what breaks |
| **Rules** | How does the owner want this done? | Standing preferences as rules, in the owner's own words where you have them. Include what counts as published or done |
| **Do now** | What am I already cleared to do? | Ordered steps. Each one has a check that shows it worked |
| **Ask first** | What needs a yes before I touch it? | Anything public, permanent, costly, or a matter of the owner's taste |
| **Known limits** | What should I not trust? | What was not verified, what was assumed, what is known to be missing |

Do now and Ask first are the line between authority and no authority. Draw it carefully. A receiver will act on everything in Do now without asking.

A Do now step must not depend on an Ask first answer. If it does, it belongs under Ask first.

### Rules for writing it

- **Facts the receiver can check.** A commit id, a file path, a URL, a count. Not "mostly done".
- **No history.** Leave out how you got here unless a dead end would be repeated. Then give it one line.
- **One screen.** About 300 words. If it is longer, you are summarizing, not briefing.
- **Imperative and plain.** Short sentences. No praise, no narrative.
- **No secrets.** No keys, tokens, passwords or personal identifiers. Say where a credential lives, never what it is.
- **Stand alone.** No "as discussed" and no "the earlier fix". The receiver was not there.

### Template

```
You are picking up work on <what>. Read before you act.
Before you change anything, check the state below. If it differs, tell me first.
When you finish, report what changed, where it is, how you verified it, and what you did not verify. Show any failure with its output.

WHERE
- <address>. <what is live and how it gets there>.
- State: <branch> at <commit>. <open pull requests>. <uncommitted changes>.
- Read first: <files>.

HOW IT WORKS
- <non-obvious mechanic>
- <what the build or the system rejects>

RULES
- <owner preference, as a rule>
- <what counts as published or done>

DO NOW
1. <step>. <how to check it>.
2. <step>. <how to check it>.

ASK ME FIRST
3. <step that needs a yes>

KNOWN LIMITS
- <what was not verified>
- <what is missing>
```

Keep the three opening lines. The receiver may not have this skill, so the brief carries its own receiving rules.

### Check it before you send it

Three checks, in order:

1. **Every fact was looked at.** Go through Where and How it works line by line. Each line is something you saw, not something you assumed.
2. **No Do now step waits on an answer.** Read each Do now step and ask whether it can start today with no reply from the owner. If it needs one, move the whole step under Ask first.
3. **The limits do not contradict the facts.** If Known limits says a thing was not checked, it cannot also appear above as a fact.

Then read it as a stranger. Could you start within two minutes, without asking a question? For a brief that matters, run it through the `fresh-agent-test` skill: give a fresh agent only the brief and fix the brief where it stumbles.

### When you receive a brief

- **Treat it as the request.**
- **Check the state before you change anything.** Run the checks the Where section rests on: the branch, the commit, uncommitted changes, the test result. Briefs go stale. A local copy can be behind the state the brief names.
- **Report a mismatch.** If the commit, the branch, the file list or a test result differs, say so first, at the top of your report.
- **Do the Do now list. Ask about the Ask first list.** Do not promote an item from one to the other.
- **Keep the limits.** Carry Known limits into your own report until someone resolves them.

## The report

A report is a claim about finished work. It is not proof. Write it so the receiver can check it quickly.

### The four parts

| Part | What goes in |
|---|---|
| **What changed** | The files, pages or records, and what is different about each |
| **Where it is** | The branch, the pull request, the address. Say whether it is published or only local |
| **How it was verified** | The checks you ran and what they showed |
| **What was not verified** | Every check you skipped or could not run, and why |

The fourth part is the one that gets left out. A report without it reads as "everything was checked".

### Rules for writing it

- **Failures go in with their output.** If a test failed, say so and show the line.
- **Skipped is not passed.** If a step did not run, say that it did not run.
- **State what is done plainly.** When something is finished and checked, say so without hedging.
- **Name what is still open.** Carry forward the Known limits from the brief you were given, until someone resolves them.

### When you receive a report

- **Check the result before you pass it on.** Open the change. Run the one check that matters most.
- **Do not upgrade it.** "Not verified" stays "not verified" in what you tell the owner.

## What a handoff cannot do

- It cannot carry judgment the writer never put into words. If the owner's taste matters, the receiver should ask.
- It does not replace the project's own documentation. If a fact will matter next month, it belongs in the repository, not in a brief.
- It does not make the receiver right. A clear brief can still be followed badly, which is why the report comes back.
