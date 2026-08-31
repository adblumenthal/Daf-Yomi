#!/usr/bin/env python3
"""Static package self-check for Daf Yomi Tutor."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "references/source-policy.md",
    "references/installation-notes.md",
    "scripts/dafyomi_context.py",
    "scripts/sefaria_fetch.py",
    "tests/acceptance-cases.md",
]

def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8") if (ROOT / "SKILL.md").exists() else ""
    checks = {
        "version 1.0.0": 'version: "1.0.0"' in skill,
        "dedication in README": "David and Barbara Blumenthal" in (ROOT / "README.md").read_text(encoding="utf-8"),
        "source links on demand": "Source links on demand" in skill,
        "verification labels": "`verified`" in skill,
    }

    if missing:
        print("Missing required files:")
        for p in missing:
            print(" -", p)
    for label, ok in checks.items():
        print(f"{'OK' if ok else 'FAIL'}: {label}")

    return 1 if missing or not all(checks.values()) else 0

if __name__ == "__main__":
    raise SystemExit(main())
