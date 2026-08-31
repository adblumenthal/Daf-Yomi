# Daf Yomi Tutor — portable Agent Skill

**Version 1.0.0**

A guided Daf Yomi skill that does more than tell you the day's daf: it gives perek/yesterday context, structures the Mishnah and sugyot, explains why the Gemara cares, highlights useful Rashi/Tosafot, connects relevant halacha, teaches Aramaic, gives key takeaways and review questions, previews tomorrow, supports catch-up ranges, learner levels, and masechet siyum planning.

## Dedication

Created by **Adam Blumenthal** in honor of his mother and father, **David and Barbara Blumenthal**, who always pushed him to keep asking questions.

That spirit is part of the goal of this skill: Daf Yomi should not just tell you *what* the Gemara says, but help you keep asking *why*, *how*, and *what follows from it*.

## Designed for easy installation

- No Sefaria account
- No API key
- No MCP server
- No pip/npm dependencies
- One skill folder
- Open Agent Skills `SKILL.md` format

The helper scripts use Python 3's standard library and public Hebcal/Sefaria HTTP APIs.

## Install in ChatGPT Skills

Where Skills are available:

1. Open **Plugins → Skills**.
2. Choose **Create → Upload from your computer**.
3. Upload the `daf-yomi-tutor` skill folder/package supplied here.
4. Install/enable the skill.

Availability depends on plan, workspace settings, surface, and rollout.

## Install in another Agent-Skills-compatible client

Install or copy the entire `daf-yomi-tutor/` directory into the location your client uses for Agent Skills. Keep `SKILL.md`, `scripts/`, and `references/` together.

The skill follows the open Agent Skills directory format:
- `SKILL.md` — required instructions/metadata
- `scripts/` — optional executable helpers
- `references/` — supporting guidance

## Example prompts

- `/dafyomi`
- `/dafyomi yesterday`
- `/dafyomi 8/15/2025`
- `/dafyomi short`
- `/dafyomi deep halacha`
- `/dafyomi beginner short`
- `/dafyomi advanced deep`
- `/dafyomi 8/15/2025 till today short`

## Data sources

- **Hebcal**: Daf Yomi assignment, Hebrew dates, and Jewish-calendar context.
- **Sefaria**: primary Jewish texts and commentaries for source verification.

These services are called at runtime; their text/data is not bundled into this repository.

## Publishing

This project is released under the **MIT License**. See `LICENSE`.

The canonical portable skill is the `daf-yomi-tutor/` folder. Vendor-specific wrappers should point to or package this folder rather than fork the teaching instructions.

## Quality checks

Before a release, review `tests/acceptance-cases.md`. It contains representative prompts for date handling, catch-up ranges, siyum planning, special days, learner modes, source links, and source-failure behavior.

See `CHANGELOG.md` for release history.
