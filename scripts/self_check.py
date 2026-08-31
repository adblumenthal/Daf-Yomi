#!/usr/bin/env python3
"""Static package self-check for Daf 2.0."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "agents/openai.yaml",
    "references/source-policy.md",
    "references/installation-notes.md",
    "scripts/yomi_context.py",
    "scripts/sefaria_fetch.py",
    "tests/acceptance-cases.md",
    "tests/test_release.py",
]


def _read(path: str) -> str:
    target = ROOT / path
    return target.read_text(encoding="utf-8") if target.exists() else ""


def _frontmatter_keys(skill: str) -> list[str]:
    match = re.match(r"^---\n(.*?)\n---\n", skill, re.DOTALL)
    if not match:
        return []
    return [
        line.split(":", 1)[0].strip()
        for line in match.group(1).splitlines()
        if line.strip() and not line.startswith((" ", "\t")) and ":" in line
    ]


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    skill = _read("SKILL.md")
    readme = _read("README.md")
    acceptance = _read("tests/acceptance-cases.md")
    yomi_helper = _read("scripts/yomi_context.py")
    current_docs = "\n".join((skill, readme, acceptance, _read("references/source-policy.md")))

    checks = {
        "valid minimal frontmatter": _frontmatter_keys(skill) == ["name", "description"],
        "skill name daf": "name: daf\n" in skill,
        "version 2.0.0": "Version 2.0.0" in skill and "Version 2.0.0" in readme,
        "dedication preserved": "David and Barbara Blumenthal" in readme,
        "exact-daf command documented": "/daf Chullin 23b" in skill and "/daf Chullin 23b" in readme,
        "exact range documented": "/daf Chullin 23a-33b" in skill and "/daf Chullin 23a-33b" in readme,
        "yomi command documented": "/daf yomi" in skill and "/daf yomi" in readme,
        "plain daf defaults to yomi": "Plain `/daf` and `/daf yomi`" in skill,
        "dates live under yomi": "/daf yomi yesterday" in skill and "/daf yomi 8/15/2025 till today" in skill,
        "commentary focus documented": "### `rashi`" in skill and "### `tosafot`" in skill,
        "expanded modes covered by acceptance cases": all(
            heading in acceptance
            for heading in (
                "Exact-daf mode",
                "Exact-daf ranges",
                "Yomi mode",
                "Yomi completion and cycle context",
                "Commentary and study modes",
            )
        ),
        "legacy command removed from current docs": "/dafyomi" not in current_docs,
        "yomi progress restored": (
            "Provide Yomi completion and cycle context" in skill
            and "days_remaining_after_requested_daf" in yomi_helper
            and "within_14_days" in yomi_helper
            and "siyum_day" in yomi_helper
        ),
        "progress isolated from exact mode": "Never add this section to exact-daf mode" in skill,
        "bounded fast path documented": (
            "Keep ordinary requests fast" in skill
            and "consolidated source retrieval" in skill
            and "Performance boundaries" in acceptance
        ),
    }

    if missing:
        print("Missing required files:")
        for path in missing:
            print(" -", path)
    for label, ok in checks.items():
        print(f"{'OK' if ok else 'FAIL'}: {label}")

    return 1 if missing or not all(checks.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
