---
name: confluence-distill-archive
description: Clean up a Confluence space through the Atlassian Rovo v2 MCP - inventory every page, judge each on whether it is still true (not just old), move durable knowledge into a standing decision record with source links, then archive the leftovers reversibly with a ledger and a before/after scorecard. Use whenever the user says clean up, tidy, declutter, prune, distill, consolidate, retire or archive Confluence, a space or a wiki, asks what is stale, duplicated or dead in Confluence, or wants cleaner knowledge for Rovo or other AI assistants - even if they never say the word archive.
---

# Confluence distill and archive

Most cleanup tools sort pages by age and archive the old ones. That loses knowledge and keeps wrong pages that happen to be recent. This skill does the part those tools skip: it reads each page, asks whether it is still true, moves what is worth keeping into one clean home, and only then archives - reversibly, with a record of what went where.

The order is the point. Knowledge moves first, pages archive second.

## Principles

- **Truth beats age.** A page goes stale when the thing it describes changes, not when time passes. An old decision record can be fully valid. A two-week-old how-to can already be wrong. Age is a hint about where to look, never the verdict.
- **Confluence is ground truth. Jira status drifts.** Read Jira as evidence. Never change Jira as part of a Confluence cleanup.
- **Evidence before verdict.** Cleanups go wrong when work gets marked done that was not. Every verdict carries its evidence. No evidence, no verdict - the page goes to Ask.
- **Archive, never delete.** Archive is reversible with `unarchiveConfluenceContent`. Do not call `executeDestructive` here, even if asked to "just delete the junk" - offer archive and say it can be undone.
- **Dormant is not dead.** A parked project keeps its home page and key specs. State it as parked, with the date.
- **Do not upgrade status.** "In Design" becomes "In Design as of 12 March". Never round a draft up to a decision.
- **One plan, one approval, then act.** Reads are free. Before the first write, show the whole plan and wait for a clear yes. After the yes, run the writes - do not describe what you would do.

## Tools

Use the Atlassian Rovo v2 MCP. Call `getAccessibleAtlassianResources` once and pass the cloudId as a top-level argument beside `name` and `inputs`. A Confluence URL's hostname also works as cloudId.

- Direct: `searchConfluence` (CQL), `getConfluenceContent`, `createConfluenceContent`, `updateConfluenceContent`, `getJiraIssue`.
- `executeRead`: `listConfluenceSpaces`, `getConfluenceSpace`, `listConfluenceContent`, `getConfluenceContentDescendants`, `getConfluenceContentAnalytics`, `listConfluenceContentVersions`, `listConfluenceTasks`, `listConfluenceComments`, `listConfluenceAttachments`, `getConfluenceContentStatus`, `getContentFormatGuide`.
- `executeWrite`: `addLabelsToConfluenceContent`, `moveConfluenceContent`, `setConfluenceContentStatus`, `archiveConfluenceContent`, `unarchiveConfluenceContent`.

These names were confirmed with `discover`. The catalog changes. If a call fails as unknown, run `discover` with a plain verb-plus-object query and use what it returns. Never guess an operation name.

Known limits - plan around them:

- **No backlinks operation.** Find references with a CQL text search on the page title, and by reading the hub pages (space home, the parent) for links. A text search can miss link macros, so say the check is partial.
- **Labels can be added, but no remove-label operation was found.** Treat labels as permanent. Label only pages that are being archived. Never label Keep pages - it also counts as activity and can confuse Confluence's own inactivity rules.
- **Archive takes one content id, with no option for children.** Do not rely on what happens to children. Go leaves first.
- **Account mismatch.** The connector can sign in as a different account than the content owner. `currentUser()` filters then return nothing, silently. Scope by space, not by person.
- **Permissions.** Ordinary users can usually archive only their own pages. On a permission error, do not retry - collect those pages for a space admin.
- **Call budget.** The MCP has hourly limits by plan. Use `detail: summary` for inventory and `detail: full` only for pages that might be distilled.
- **Authoring.** Before writing any body, call `getContentFormatGuide` and `getConfluenceSpace` (space instructions). Updates need the `snapshotToken` from the latest read.

## Workflow

### 0. Resume

Look for a `Cleanup ledger` page in the space. If it exists, read it first. Skip pages already decided unless they changed since. The ledger is the memory between passes.

### 1. Scope and thresholds

One space or one page tree per pass. If the user did not say which, list spaces with page counts and ask once.

Defaults, which the user can change: a page is a **stale candidate** after 180 days without an edit and no recorded viewers. A page edited in the last 30 days is **fresh** and cannot be archived without asking.

### 2. Inventory

One table, every item, real signals. No verdict from a title.

- Pages and blog posts: `searchConfluence` with `space = "KEY" AND type in (page, blogpost) ORDER BY lastmodified ASC`, paged to the end. Live docs come back as pages.
- Tree: `getConfluenceContentDescendants` from the space `homepageId`, depth 10. Gives parent ids and catches whiteboards, databases and folders.
- Unfinished business: one `listConfluenceTasks` call with `spaceId` and `status: incomplete` covers the whole space. Open tasks mean live work.
- Per candidate page: `getConfluenceContentAnalytics` (an empty viewers list means nobody opened it in the window), `listConfluenceComments` with `resolution-status: open`, `listConfluenceAttachments`, `getConfluenceContentStatus`.

Record a **scorecard** now: pages in tree, stale candidates, scaffold pages, duplicate clusters, open tasks, pages with no viewers. The same counts after the pass are the result.

### 3. Classify

First name the **type**, because type decides how to judge it:

| Type | Examples | How it goes stale |
|---|---|---|
| Hub | Space home, index pages | Rewrite it, never archive it |
| Record | Decisions, post-incident reviews, lessons learned, submitted documents, notices held on file | It does not. Age is irrelevant |
| Reference | Specs, how-tos, configuration, boilerplate | When the thing it describes changes |
| Working | Drafts, meeting notes, plans, status pages | When the work ends |
| Scaffold | Empty or untitled docs, untouched templates, test artifacts | It was never alive |

Then give exactly one **verdict**, and for anything not kept, one **reason code**:

| Verdict | Means |
|---|---|
| **Keep** | Still true, or the only home of a live fact |
| **Distill** | Holds durable knowledge, but the page is superseded, duplicated or finished |
| **Archive** | Nothing durable to save |
| **Ask** | The evidence cannot settle it |

Reason codes: **Redundant** (said elsewhere), **Outdated** (no longer true), **Trivial** (never mattered). Trivial is the one people disagree on, so show the evidence and let the user overrule.

**Truth test for Reference pages.** Before calling a spec Outdated or Keep, check what is cheap to check: the status of any Jira issue it cites, whether the pages and links it points to still exist, whether a newer page covers the same topic. Record what was checked. If it cannot be tested from here, the verdict is Ask, phrased as a real question: "Is the payments API design still the plan?"

**Duplicates.** Cluster by similar titles and by searching a distinctive phrase. The survivor is the one with more references, the later edit and the better place in the tree. The others are Distill - Redundant, merged into it.

Overrides:

- A page with open tasks or open comments is live work. Keep or Ask, never a silent Archive.
- A page that declares its own status - a "sample data" banner, a "source of record" note - is deliberate. Keep.
- Someone else's page, or a fresh page: Ask.
- A parent with live children cannot be archived as is. Move the keepers out first, or keep the parent.

### 4. Distill

Knowledge goes to one of two homes:

- **Merge** into the Keep page that owns the topic. Preferred.
- **Decision record** - one standing page per space, titled `Decision record`, under the space home. Each pass appends a dated section. One page that grows beats a pile of digests.

Each dated section uses this shape:

```
## <Mon YYYY> cleanup
### Decisions        - what was decided, why, when
### Still true       - specs, definitions, numbers, each with its source
### Open questions   - unanswered questions, open tasks and open comments carried over
### Lessons          - what was learned
### Parked           - work that stopped, with its status as of a date
```

Every item ends with a link to the page it came from. Archived pages still open by link, so the trail holds. Dates are absolute. Short sentences, hyphens not em-dashes, no filler. Items should not overlap and nothing durable should be left out.

Note attachments on Distill pages. A file that matters gets named in the record with its source page.

Draft everything. Write nothing to Confluence yet.

### 5. Verify

- Re-read each source against its distilled version. List what was dropped on purpose. Fix anything dropped by accident.
- Red-team the draft once: weakest claim, any status rounded up, any number without a source.
- For each page leaving the tree, list the live pages that reference it. Those links need repointing.

### 6. Approve

Show one view and stop:

- The scorecard
- A table: page, type, verdict, reason code, one-line evidence, where its knowledge goes
- The decision record draft
- Edits to Keep pages (merges and repointed links) - these change live pages, so list them
- The Ask list as direct questions

Offer one alternative per page where it fits: **retire in place**. The page stays visible with a `Retired` content status and a banner, instead of leaving the tree. Useful when history should stay browsable.

A partial yes is normal - run exactly that subset. If nobody is there to answer, stop here and leave the plan as the output.

### 7. Execute

In this order, so a failure halfway never loses knowledge:

1. Write the merges and the decision record section. Confirm each write landed.
2. Repoint links on live pages to the survivor or the decision record. Confluence has no redirects, so this is the only way old links stay useful.
3. Move Keep children out from under parents that will be archived.
4. Add a **replaced-by banner** to the top of each Distill page: `Archived <date>. Replaced by <link>.` Do it before archiving - an archived page cannot be edited until restored, and it still opens from old links with little to show it is retired.
5. Label each page to be archived: `archived-<mon>-<yyyy>`, plus `distilled` for Distill pages. No spaces in labels.
6. Archive with `archiveConfluenceContent`, leaves before parents, in batches of at most 25. After each batch, re-run the inventory search and confirm the pages left the current set. After archiving any parent, re-list its descendants.

On a failure, retry once with corrected input, then record it and move on. If the approved list runs to hundreds of pages, finish the distill and ledger here and hand the archive list to a space admin for bulk archive in the Confluence UI.

### 8. Ledger and scorecard

Append to the `Cleanup ledger` page under the space home. One row per page touched: date, title, content id, link, type, verdict, reason code, evidence, original parent id, where the knowledge went. The parent id is what lets a restore put a page back where it was.

Top of the ledger: how to undo (`unarchiveConfluenceContent` with the content id), and the scorecard before and after.

### 9. Keep it clean

A cleanup decays unless something keeps it up. Offer, do not impose:

- An owner and a review-by date on each hub and Reference page
- Confluence's own automation for inactive-page notices, where the plan includes it
- A scheduled re-run of this skill each quarter, which resumes from the ledger

## Report back

- Scorecard, before and after
- Links to the decision record and the ledger
- Anything that failed or needs a space admin
- The Ask list, still open

Do not recap the steps. Do not promise that archiving changes what Rovo or another assistant answers: archiving is documented to take a page out of the tree and quick search, while what an agent reads depends on how its knowledge is scoped. If cleaner AI answers are the goal, say so and suggest checking that scope as a separate step.
