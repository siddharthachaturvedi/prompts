# Skills

Skills are longer, tool-using workflows. A prompt tells a model how to think about one question. A skill tells an agent how to carry out a multi-step job with real tools, including when to stop and ask.

They live here, apart from the prompt library. The site build picks up every `skills/<name>/SKILL.md` and lists it on the skills page at [prompts.sidc.ai/skills](https://prompts.sidc.ai/skills/).

| Skill | What it does | Needs |
|---|---|---|
| [grooming-engine](grooming-engine/SKILL.md) | The shared core for grooming any collection. Judges every item on three separate axes - semantic, temporal, importance - then keeps, refreshes, distills or retires it reversibly, with a ledger. | Nothing on its own. An adapter supplies the system |
| [confluence-distill-archive](confluence-distill-archive/SKILL.md) | Adapter for Confluence spaces. | grooming-engine, Atlassian Rovo MCP server (v2) |
| [prompt-library-grooming](prompt-library-grooming/SKILL.md) | Adapter for a prompt library kept in git. | grooming-engine, git |

## Using a skill

Each skill is a folder with a `SKILL.md`. The frontmatter `description` says when it applies. The body is the instructions.

- **Claude Code:** copy the folder into `.claude/skills/` in a project, or `~/.claude/skills/` for every project.
- **Other agents:** any tool that reads the `SKILL.md` format can load the folder as is.

## Status

- `grooming-engine` and `prompt-library-grooming` were run end to end on this repository. The result is in [`grooming/LEDGER.md`](../grooming/LEDGER.md).
- `confluence-distill-archive` has been checked read-only against a live Confluence site. Its write path - banner, label, archive, ledger - has not been run end to end yet. It asks for approval before the first write and never deletes.

An adapter needs the engine installed beside it. Each adapter says so at the top and carries a short safe version of the method in case the engine is missing.
