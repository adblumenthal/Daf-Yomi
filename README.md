# Daf — portable Agent Skill

**Version 2.0.0**

A source-grounded Talmud tutor with two simple entry points:

- `/daf Chullin 23b` teaches that exact daf or amud, independent of the Daf Yomi schedule.
- `/daf Chullin 23a-33b` creates a grouped catch-up lesson across that exact inclusive range.
- `/daf yomi` teaches today's Daf Yomi assignment.

Plain `/daf` is a shortcut for `/daf yomi`. The skill explains the Mishnah and major sugyot, makes the Gemara's logic clear, highlights useful Rashi and Tosafot, connects relevant halacha, teaches Aramaic, gives three key takeaways and review questions, and previews the next material.

## Dedication

Created by **Adam Blumenthal** in honor of his mother and father, **David and Barbara Blumenthal**, who always pushed him to keep asking questions.

That spirit is part of the goal of this skill: learning a daf should not stop at *what* the Gemara says, but should keep asking *why*, *how*, and *what follows from it*.

## Command guide

### Study any daf

- `/daf Chullin 23b`
- `/daf Chullin 23a-33b`
- `/daf Bava Metzia 42a deep`
- `/daf Bava Metzia 42a-45b tosafot deep`
- `/daf Berakhot 2 beginner halacha`
- `/daf Sanhedrin 17b show sources`

The requested reference is taught directly, even when it is not part of the current Daf Yomi cycle. A reference ending in `a` or `b` limits the lesson to that amud; a reference without an amud letter requests the whole daf when supported by the source.

Exact ranges stay within one masechet and are inclusive. `/daf Chullin 23a-33b` covers every amud from 23a through 33b, groups the material by perek and major sugya, and includes a compact coverage checklist. It does not add unrelated Daf Yomi dates or cycle statistics.

### Follow Daf Yomi

- `/daf`
- `/daf yomi`
- `/daf yomi yesterday`
- `/daf yomi 8/15/2025`
- `/daf yomi 2025-08-15`
- `/daf yomi yesterday short`
- `/daf yomi 8/15/2025 till today short`

Date syntax belongs after `yomi`. Plain `/daf` and `/daf yomi` use the user's current local date.

Yomi mode preserves the original calendar and progress context: current-masechet days remaining, exact completion dates and siyum-planning reminders when close, final-daf notices, and full-cycle progress when reliably available. This material appears only in Yomi mode, not when studying a named page or exact range.

### Study modes

Both exact-daf and Yomi requests support:

- `short` — compact lesson
- `deep` — expanded shakla v'tarya and commentaries
- `halacha` — emphasize the path to practical halacha
- `beginner` — explain terminology and logical steps
- `advanced` — emphasize Rishonim, conceptual distinctions, and exact references
- `rashi` — expand the most important Rashi comments and how they shape the peshat
- `tosafot` / `tosefot` / `tosfos` — expand major questions, answers, parallels, and consequences
- `show sources` — provide direct source links

Modifiers can be combined for a page, range, or Yomi request, such as `/daf Chullin 23a-33b rashi tosafot advanced`, `/daf Chullin 23b advanced deep`, or `/daf yomi halacha beginner`.

Ordinary requests use a streamlined source path. A `rashi` or `tosafot` modifier selects the most important comments without exhaustively retrieving every commentary passage. Add `deep` or `show sources` when you want broader research and more extensive source verification.

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
3. Upload the complete `Daf` repository folder or release package.
4. Install or enable the skill.

Availability depends on plan, workspace settings, surface, and rollout.

## Install in another Agent-Skills-compatible client

Install or copy the complete repository folder into the location your client uses for Agent Skills. Keep `SKILL.md`, `scripts/`, `references/`, and `agents/` together.

The package follows the open Agent Skills directory format:

- `SKILL.md` — required instructions and trigger metadata
- `agents/openai.yaml` — optional UI metadata
- `scripts/` — zero-dependency source and calendar helpers
- `references/` — supporting source and installation guidance
- `tests/` — release acceptance coverage

## Data sources

- **Hebcal**: Daf Yomi assignments, Hebrew dates, and Jewish-calendar context for Yomi mode.
- **Sefaria**: primary Jewish texts and commentaries for both exact-daf and Yomi modes.

These services are called at runtime; their text and data are not bundled into this repository.

## Quality checks

Run:

```bash
python scripts/self_check.py
```

Then review `tests/acceptance-cases.md`. It covers exact-daf routing, exact ranges, Daf Yomi dates and ranges, Rashi/Tosafot focus, study modes, Yomi-only completion context, source behavior, and special days.

## Publishing

This project is released under the **MIT License**. See `LICENSE`.

See `CHANGELOG.md` for release history and the 2.0 command migration notes.
