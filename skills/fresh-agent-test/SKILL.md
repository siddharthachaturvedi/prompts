---
name: fresh-agent-test
description: Tests any written instruction - a skill, a prompt, an install guide, a handoff brief - by giving it to a fresh agent that knows nothing else, then fixes the instruction where the agent stumbles. Use when the user asks whether a prompt or skill works, before publishing instructions for other people or agents, or after editing them.
---

# Fresh agent test

You cannot proofread your own instructions. You know what you meant, so you read what you meant. A fresh agent knows only the words. Where it stumbles, the words are wrong.

This is the test. Hand the instruction to an agent with no other context. Watch what it does. Fix the instruction. Run it again.

## Set up the test

1. **A clean room.** A scratch folder. No memory, no project instructions, none of your conversation. Start a new session every run. A resumed session carries its earlier mistakes forward and will keep making them.
2. **A safe room.** Work on a copy, never the real thing. Deny writes outside the scratch folder. Deny installs too. A package manager writes outside it. The agent is following instructions you have not proven yet.
3. **Only what a real user would give.** The instruction, and the one sentence a user would type. Nothing else.
4. **A cheaper model, where you have one.** If a small model can follow the instruction, a larger one will.

## Run it

- **Do not coach.** If you help it past a gap, you have hidden the gap.
- **Answer as a typical user would.** When it asks a question, give a short plain answer. Keep a note of every question it asks.
- **Let it finish.** A stumble early on does not tell you how the later steps hold.
- **Keep the output.** You will compare runs.

## Read the result

Every stumble is one of five kinds. Name the kind before you fix anything.

| Kind | What you see | What it means |
|---|---|---|
| **Asked again** | It asks for something the instruction should have asked for, or asks twice | An input is missing or vague |
| **Invented** | It adds a fact, a name or a rule nobody gave it | A gap was filled by guessing |
| **Skipped** | It leaves out a step or a check it could have done | The step reads as optional |
| **Misread** | It does something other than what you meant | The wording points the wrong way |
| **Blocked** | The environment stopped it | Not the instruction's fault |

Read the runs side by side, not one at a time. Where two fresh agents did different things with the same words, the instruction left that choice open. Count each difference as Invented, even when both outputs look reasonable.

Check the output against the purpose, not only against the steps. An agent can follow every step and still produce the wrong thing.

## Fix the instruction, not the agent

- **One fix per stumble.** Make the smallest change in wording that would have prevented it.
- **Fix where it happened.** Put the change at the step that failed. Do not add a warning at the top.
- **A gap in meaning is the owner's to fill.** If a fix needs a choice only the owner can make, such as what counts as urgent, ask. If you cannot ask, pick the plainest reading and say so in the report.
- **Do not fix a Blocked.** Change the test setup, or record that the step could not be exercised.
- **Do not add a rule for a one-off.** If a stumble does not repeat on the next run, leave the instruction alone.
- **Length is not a fix.** If the instruction keeps growing, a step is doing two jobs. Split it.

## Run it again

- **Start a new session each time.**
- **After a fix, read the whole output again**, not only the part you fixed. A fix can break a step that worked.
- **One clean run is not a pass.** Stop when two runs in a row are clean, or after five runs.
- **Still stumbling after five?** The instruction needs restructuring, not more patches.

## Report

- How many runs, and on which model.
- Each stumble, its kind, and the fix.
- Each choice you made for the owner in a fix, so they can overrule it.
- What the test could not exercise. Write paths, real systems and anything Blocked belong here.
- What still stumbles.

Say plainly what was not tested. "Passed" means it passed these runs, in this room.

## What this test cannot do

- **It does not prove the instruction is right.** It shows that an agent can follow it. Whether following it gives a good result is your judgment.
- **Agents differ.** A pass on one model is evidence for another, not proof.
- **It cannot test what the room forbids.** A safe room blocks the risky steps, and those are the ones that matter most. Test them separately, with the owner watching.
