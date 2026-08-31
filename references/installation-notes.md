# Installation notes for maintainers

The simplest public distribution is a GitHub repository whose root contains the `daf-yomi-tutor/` directory.

Recommended goals:
1. One-click or upload-style installation wherever the client supports it.
2. No secrets or environment variables.
3. No MCP prerequisite.
4. No package-manager prerequisite.
5. Graceful fallback if scripts cannot execute: the `SKILL.md` tells the agent which authoritative sources to use directly.

Do not hard-code a vendor-specific skill path into the portable package unless you are publishing a vendor-specific installer; paths and UI flows can change.

For a future marketplace/plugin version, keep this folder as the canonical skill and wrap it rather than forking the instructions.
