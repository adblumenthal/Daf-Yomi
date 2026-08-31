# Installation notes for maintainers

The public GitHub repository is the skill root. Keep `SKILL.md` at the repository root; do not nest a second `Daf/` directory inside it.

Recommended goals:

1. Preserve both `/daf <Masechet> <daf>` and `/daf yomi` behavior in every distribution.
2. Support one-click or upload-style installation wherever the client permits it.
3. Require no secrets, environment variables, MCP server, or package manager.
4. Keep `SKILL.md`, `agents/`, `scripts/`, and `references/` together.
5. Fall back gracefully when scripts cannot execute: `SKILL.md` identifies the authoritative sources the agent should use directly.

Do not hard-code a vendor-specific skill path into the portable package unless publishing a vendor-specific installer; paths and UI flows can change.

For a future marketplace or plugin version, wrap this repository rather than forking the teaching instructions.
