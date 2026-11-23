---
name: grooming-engine
description: The shared core for grooming any body of content - a wiki, a prompt library, a backlog, a drive, a set of repos. Judges every item on three separate axes (semantic, temporal, importance), moves durable knowledge to one home, then retires the rest reversibly with a ledger. Use whenever the user asks to groom, clean up, distill, consolidate, dedupe, prune or archive a collection, and whenever an adapter skill such as confluence-distill-archive or prompt-library-grooming says to load the engine first.
---

# Grooming engine

Grooming is three questions asked of every item in a collection, then one decision. Most cleanups fail because they ask one question - usually "how old is it?" - and treat the answer as the decision.

This is the core. It knows nothing about any particular system. An **adapter** supplies the system: how to list items, what evidence exists, how to retire something reversibly. Read the adapter for the system in front of you, then run this workflow. If no adapter exists, fill in the adapter contract at the end yourself before starting.

## The three axes

Judge each axis on its own evidence. Record all three before deciding anything. Each one can come back `unknown`, and that is a legitimate answer.

### Semantic - what does it say, and does anything else say it?

- **Question.** What job does this item do or what claims does it hold? Is that unique, overlapping, duplicated or contradicted elsewhere?
- **Evidence.** Reading the item itself. Clustering by job, then comparing items inside a cluster side by side.
- **Result.** `unique` / `overlaps <item>` / `duplicate of <item>` / `contradicts <item>` / `mislabeled` (the name or credit no longer matches the content).
- **Trap.** Similar titles are a hint, not a verdict. Two items can share a framework and do different jobs. Two items can share a name and nothing else.

### Temporal - is it still true, and what did time take from it?

Time runs in two directions here. Check both.

- **Forward: is it still true now?** A page goes stale when the thing it describes changes, not when the calendar moves. Ask what would have to change in the world for this to be wrong, then check whether it has.
- **Backward: what did earlier versions hold that this one dropped?** Past rewrites and past cleanups are where durable content most often gets lost. Where the system keeps history, compare the item against its own earlier versions.
- **Result.** `valid` / `expired` / `eroded` (a past edit dropped something durable) / `unknown`.
- **Trap.** Age is not a result. It only tells you where to look first.

### Importance - what is lost if it vanishes?

- **Question.** Who or what depends on this? What does it cost if it is wrong, or gone?
- **Evidence.** Proxies only: usage, inbound references, open work on it, whether it is the only home of a fact, and stakes - a wrong credit, a wrong number or a wrong instruction costs more than a missing nicety.
- **Result.** `load-bearing` / `useful` / `marginal` / `unknown`.
- **Trap.** Importance cannot be read off the page. If no proxy exists, say `unknown` and ask the owner. Do not invent a ranking.

## From three results to one verdict

| Verdict | When | Reason code |
|---|---|---|
| **Keep** | Unique, valid, and at least useful | - |
| **Refresh** | Still needed, but expired, eroded or mislabeled. Fix it in place | Outdated |
| **Distill** | Duplicated or overlapping. Its durable content moves to a survivor or a record, then it retires | Redundant |
| **Archive** | Marginal, with nothing durable to save | Trivial |
| **Ask** | An `unknown` on any axis would change the verdict | - |

The reason codes are the three axes failing: Redundant is semantic, Outdated is temporal, Trivial is importance.

Rules that hold across systems:

- **Important and wrong means Refresh, never Archive.** An expired item people rely on needs repair.
- **Redundant but load-bearing means Keep.** Some repetition is deliberate - a block every item must carry to stand alone. Check why it repeats before removing it.
- **Zero is a valid result.** If nothing deserves to be retired, say so. Do not manufacture merges to look productive.
- **Trivial is the contested call.** Show the evidence and let the owner overrule.

## Principles

- **Knowledge moves first, items retire second.** Nothing is retired until what it uniquely held is safe somewhere else and checked.
- **Evidence before verdict.** Every verdict carries what was read and what was checked. No evidence, no verdict.
- **Retire reversibly. Never delete.** Use the system's archive, not its delete. If asked to "just delete the junk", offer the reversible action and say it can be undone.
- **Do not upgrade status.** A draft stays a draft, with its date. A guess stays a guess.
- **Dormant is not dead.** Parked work keeps its home and its key documents, marked as parked with a date.
- **One plan, one approval, then act.** Reads are free. Before the first write, show the whole plan and wait for a clear yes. After the yes, do the work rather than describing it.

## Workflow

### 0. Resume
Find the ledger from earlier passes and read it. Skip items already decided unless they changed since.

### 1. Scope
One unit per pass - one space, one folder, one project. A small finished pass beats a sprawling one.

### 2. Inventory
List every item with its signals for all three axes. Include history where the system keeps it. No verdict from a title. Record a **scorecard** of counts now, so the same counts after the pass show the result.

### 3. Judge
For each item: its type (the adapter defines types), then the three axis results with evidence, then the verdict and reason code.

### 4. Distill
Durable content is what will still matter in six months: decisions and their reasons, definitions and numbers that are still true with their sources, signature methods, open questions, and credits. It goes to one of two homes:

- **A survivor** - the kept item that owns the topic. Preferred.
- **A standing record** - one page or file per scope that grows by a dated section each pass.

Every moved item keeps a pointer back to where it came from. Draft everything. Write nothing to the live system yet.

### 5. Verify
Distilling is lossy on purpose, so measure the loss.

- **Claim coverage.** For each source, list its durable claims. Each one is either carried into the survivor or record, or on a short dropped-on-purpose list with a reason. Anything in neither place is **lost**, and lost must be zero before going on.
- **Red-team once.** Weakest claim, any status rounded up, any number or credit without a source.
- **References.** List what points at each item being retired. Those pointers need fixing.

### 6. Approve
Show one view and stop: the scorecard, every item with its three axis results and verdict, the drafts, the edits to kept items, and the Ask list as direct questions. A partial yes is normal - run exactly that subset. If nobody is there to answer, stop here and leave the plan as the output.

### 7. Execute
In an order where a failure halfway loses nothing:

1. Write refreshes, merges and the record. Confirm each landed.
2. Fix pointers so old links lead to the survivor.
3. Mark each retiring item with what replaced it.
4. Retire in small batches. Confirm each batch before the next.

Retry a failure once with corrected input, then record it and move on.

### 8. Ledger
One row per item touched: date, item, type, the three axis results, verdict, reason code, evidence, where its content went, and how to undo. The ledger is what turns a cleanup into an auditable decision, and it is the memory for the next pass.

### 9. Keep it clean
Offer, do not impose: an owner and a review date on what was kept, and a scheduled re-run that resumes from the ledger.

## Report back

- Scorecard, before and after, including claims carried, dropped on purpose and lost
- Links to the record and the ledger
- What failed or needs someone else
- The Ask list, still open

Do not recap the steps.

## What this engine cannot do

Say these plainly when they apply. They are limits of the method, not of effort.

- **Semantic.** It only understands what it has actually read. Overlap across a large collection is found by clustering first, so a pair that lands in different clusters can be missed. A contradiction spread across many items is harder to see than one between two.
- **Temporal.** It cannot know the world changed unless the evidence is reachable from here. `unknown` will be common, and it is the honest result.
- **Importance.** It never sees importance directly, only proxies. With no usage data and no owner to ask, it cannot rank.
- **Distilling.** Claim coverage is a careful second read, not a proof. On anything high-stakes, have someone who did not write the distilled version check it against the sources.

## Adapter contract

An adapter is a short document that answers these for one system:

1. **Scope unit** - what one pass covers
2. **Inventory** - how to list every item and its place in the structure
3. **Signals** - what evidence exists for each axis, and where history lives
4. **Types** - the kinds of item in this system and how each goes stale
5. **Verbs** - how to refresh in place, where the survivor or record lives, the reversible retire action and its undo
6. **Pointers** - how old links keep working: a banner, a redirect, an alias
7. **Approval surface** - a plan in chat, a pull request, a review page
8. **Ledger location**
9. **Known limits** - what the tools here cannot do
