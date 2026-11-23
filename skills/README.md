# Skills

Skills are longer, tool-using workflows. A prompt tells a model how to think about one question. A skill tells an agent how to carry out a multi-step job with real tools, including when to stop and ask.

They live here, apart from the prompt library. The site build picks up every `skills/<name>/SKILL.md` and lists it under the Skills filter on [prompts.sidc.ai](https://prompts.sidc.ai/).

| Skill | What it does | Needs |
|---|---|---|
| [confluence-distill-archive](confluence-distill-archive/SKILL.md) | Cleans up a Confluence space. Judges each page on whether it is still true, moves durable knowledge into a standing decision record, then archives the rest reversibly with a ledger. | Atlassian Rovo MCP server (v2) |

## Using a skill

Each skill is a folder with a `SKILL.md`. The frontmatter `description` says when it applies. The body is the instructions.

- **Claude Code:** copy the folder into `.claude/skills/` in a project, or `~/.claude/skills/` for every project.
- **Other agents:** any tool that reads the `SKILL.md` format can load the folder as is.

## Status

`confluence-distill-archive` has been checked read-only against a live Confluence site. Its write path - banner, label, archive, ledger - has not been run end to end yet. It asks for approval before the first write and never deletes.
