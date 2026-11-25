---
name: confluence-distill-archive
description: Groom a Confluence space through the Atlassian Rovo v2 MCP - the Confluence adapter for the grooming-engine skill. Use whenever the user says clean up, tidy, declutter, prune, distill, consolidate, retire or archive Confluence, a space or a wiki, asks what is stale, duplicated or dead in Confluence, or wants cleaner knowledge for Rovo or other AI assistants - even if they never say the word archive.
---

# Confluence distill and archive

This is an adapter. The method lives in the **grooming-engine** skill. Load that skill first and follow its workflow. This file supplies only what is specific to Confluence.

If the engine is not available, tell the user it is needed. The short version, so nothing unsafe happens meanwhile: judge every page separately on what it says (semantic), whether it is still true and what past edits dropped (temporal), and what is lost if it goes (importance). Move durable knowledge first. Archive, never delete. Show one plan and wait for a yes before the first write.

## Scope unit

One space or one page tree per pass. If the user did not say which, list spaces with page counts and ask once.

## Tools

Use the Atlassian Rovo v2 MCP. Call `getAccessibleAtlassianResources` once and pass the cloudId as a top-level argument beside `name` and `inputs`. A Confluence URL's hostname also works as cloudId.

- Direct: `searchConfluence` (CQL), `getConfluenceContent`, `createConfluenceContent`, `updateConfluenceContent`, `getJiraIssue`.
- `executeRead`: `listConfluenceSpaces`, `getConfluenceSpace`, `listConfluenceContent`, `getConfluenceContentDescendants`, `getConfluenceContentAnalytics`, `listConfluenceContentVersions`, `getConfluenceContentVersion`, `diffConfluenceContentVersions`, `listConfluenceTasks`, `listConfluenceComments`, `listConfluenceAttachments`, `getConfluenceContentStatus`, `getContentFormatGuide`.
- `executeWrite`: `addLabelsToConfluenceContent`, `moveConfluenceContent`, `setConfluenceContentStatus`, `archiveConfluenceContent`, `unarchiveConfluenceContent`, `restoreConfluenceContentVersion`.

These names were confirmed with `discover`. The catalog changes. If a call fails as unknown, run `discover` with a plain verb-plus-object query and use what it returns. Never guess an operation name. Do not call `executeDestructive` in this workflow.

Input names that are easy to get wrong:

- `getConfluenceSpace` takes `spaceIdOrKey`.
- `getContentFormatGuide` takes `toolName`: `updateConfluencePage` or `createConfluencePage`.
- `listConfluenceComments` takes `content-id`. It reads one page per call.
- `getConfluenceContentVersion` returns only metadata unless you pass `content_format`.
- `listConfluenceContent` accepts `status: archived`. It has no status for the trash.

## Inventory

- Pages and blog posts: `searchConfluence` with `space = "KEY" AND type in (page, blogpost) ORDER BY lastmodified ASC`, paged to the end. Live docs come back as pages.
- Tree: `getConfluenceContentDescendants` from the space `homepageId`, depth 10. Gives parent ids and catches whiteboards, databases and folders.
- Archived pages: `listConfluenceContent` with the space id and `status: archived`.
- Read `detail: summary` for every page, `detail: full` only for pages that might be refreshed or distilled. A summary read also returns `totalViews` and the version number. The MCP has hourly call limits by plan.

## Signals for each axis

| Axis | Evidence in Confluence |
|---|---|
| Semantic | The page body. Duplicates by similar titles and by searching a distinctive phrase. A banner or status the page declares about itself |
| Temporal, forward | The status of any Jira issue it cites, whether linked pages still exist, whether a newer page covers the topic. Last-modified date only as a place to start. To check links, read the page as HTML. A link whose address contains `createpage.action` points to a page that no longer exists |
| Temporal, backward | `listConfluenceContentVersions`, `getConfluenceContentVersion` and `diffConfluenceContentVersions` - compare a rewritten page with its earlier versions for content that was dropped. A version message such as "rewritten" says where to look |
| Importance | `totalViews` from a summary read, `getConfluenceContentAnalytics` (an empty viewers list means nobody opened it in the window), open tasks from one `listConfluenceTasks` call with `spaceId` and `status: incomplete`, open comments from `listConfluenceComments` with `resolution-status: open`, one page per call, references from other pages, attachments |

Confluence is ground truth and Jira status drifts. Read Jira as evidence. Never change Jira as part of this. When a refresh copies a Jira status onto a page, name Jira and date the read. Issues that were all edited within minutes of each other may be staged, not worked.

## Types

| Type | Examples | How it goes stale |
|---|---|---|
| Hub | Space home, index pages | Refresh it, never archive it |
| Record | Decisions, post-incident reviews, lessons learned, submitted documents, notices held on file | It does not. Age is irrelevant |
| Reference | Specs, how-tos, configuration, boilerplate | When the thing it describes changes |
| Working | Drafts, meeting notes, plans, status pages | When the work ends |
| Scaffold | Empty or untitled docs, untouched templates, test artifacts | It was never alive |

Overrides:

- A page with open tasks or open comments is live work. Keep or Ask, never a silent Archive.
- A page that declares its own status - a "sample data" banner, a "source of record" note - is deliberate. Keep.
- Someone else's page, or one edited in the last 30 days: Ask.
- A parent with live children cannot be archived as is. Move the keepers out first, or keep the parent.

## Verbs

- **Refresh.** Edit the page in place, in this order:
  1. Call `getContentFormatGuide` once, and `getConfluenceSpace` for space instructions.
  2. Read the page as HTML with `draft: true` and keep its `snapshotToken`. If the draft read fails with a server error, read the published page and use that token.
  3. Change single nodes with `edits` (`replaceNode`, `insertNodeBefore`), keyed by `data-local-id`. Do not resend the whole body. Take the ids from the same read as the token. A published read and a draft read give different ids.
  4. Send the call with `dryRun: true` and read the HTML it returns. Then send the same call without it.
  5. Confirm with `diffConfluenceContentVersions` between the old version and the new one.
- **Dates.** Write each date as `<time datetime="YYYY-MM-DD">`. A Markdown read drops dates, so check them in HTML.
- **Undo a refresh.** Restore the earlier version from the page history, or with `restoreConfluenceContentVersion`.
- **Survivor.** The Keep page that owns the topic.
- **Record.** One standing page per space titled `Decision record`, under the space home. Each pass appends a dated section: Decisions, Still true, Open questions, Lessons, Parked.
- **Retire.** `archiveConfluenceContent`, one page per call, leaves before parents, at most 25 per batch. After each batch re-run the inventory search and confirm the pages left the current set.
- **Undo.** `unarchiveConfluenceContent` with the content id.
- **Retire in place.** When history should stay browsable, set a `Retired` content status and a banner instead of archiving.

## Pointers

Confluence has no redirects.

- Add a banner to the top of each distilled page before archiving it: `Archived <date>. Replaced by <link>.` An archived page cannot be edited until restored.
- Repoint links on live pages to the survivor or the record. These edits change kept pages, so list them in the plan.
- Label each archived page `archived-<mon>-<yyyy>`, plus `distilled` where its content moved. Labels cannot contain spaces.

## Approval surface

The plan in chat. Nothing is written until the user says yes.

## Ledger location

A `Cleanup ledger` page under the space home. Create it with `createConfluenceContent`, `contentType: page`, and a parent of the space id plus the `homepageId`. Add the original parent id to each row so a restore can put the page back where it was.

## Known limits

- **Tested so far.** Inventory, refresh in place and the ledger page have run on a live space. Banner, label, move, archive, unarchive and version restore have not.
- **The trash cannot be listed.** A deleted page is invisible here. Say so, and ask the owner to check the space trash.
- **Markdown reads are lossy.** They drop dates and link targets. Use HTML for anything you will edit or verify.
- **No backlinks operation.** A text search for the title can miss link macros. Say the reference check is partial.
- **Labels can be added, but no remove-label operation was found.** Treat labels as permanent. Never label Keep pages.
- **Archive takes one content id, with no option for children.** Go leaves first and re-list descendants after archiving any parent.
- **Account mismatch.** The connector can sign in as a different account than the content owner. `currentUser()` filters then return nothing, silently. Scope by space, not by person.
- **Permissions.** Ordinary users can usually archive only their own pages. On a permission error do not retry. Collect those pages for a space admin. For hundreds of pages, hand the approved list to a space admin for bulk archive in the Confluence UI.
- **AI answers.** Archiving is documented to take a page out of the tree and quick search. What Rovo or another assistant reads depends on how its knowledge is scoped. Do not promise that archiving changes its answers.
