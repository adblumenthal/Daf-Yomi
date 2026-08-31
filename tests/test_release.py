"""Zero-dependency release tests for the Daf skill."""

from __future__ import annotations

import datetime as dt
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_module(name: str, path: str):
    target = ROOT / path
    spec = importlib.util.spec_from_file_location(name, target)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SkillContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = read("SKILL.md")
        cls.readme = read("README.md")
        cls.acceptance = read("tests/acceptance-cases.md")

    def test_minimal_frontmatter_and_name(self):
        match = re.match(r"^---\n(.*?)\n---\n", self.skill, re.DOTALL)
        self.assertIsNotNone(match)
        keys = [
            line.split(":", 1)[0]
            for line in match.group(1).splitlines()
            if line and not line.startswith(" ") and ":" in line
        ]
        self.assertEqual(keys, ["name", "description"])
        self.assertIn("name: daf\n", self.skill)

    def test_exact_daf_contract(self):
        for example in (
            "/daf Chullin 23b",
            "/daf Bava Metzia 42a deep",
            "/daf Berakhot 2 beginner halacha",
        ):
            self.assertIn(example, self.skill)
        self.assertIn("Treat the named reference as authoritative", self.skill)
        self.assertIn("preview `Chullin 24a`", self.skill)

    def test_exact_range_contract(self):
        self.assertIn("/daf Chullin 23a-33b", self.skill)
        self.assertIn("inclusive same-masechet range", self.skill)
        self.assertIn("## Teach an exact-daf range", self.skill)
        self.assertIn("compact checklist of every daf or amud covered", self.skill)
        self.assertIn("Do not include Yomi dates", self.skill)

    def test_yomi_contract_and_progress(self):
        for example in (
            "/daf yomi",
            "/daf yomi yesterday",
            "/daf yomi 8/15/2025",
            "/daf yomi 8/15/2025 till today",
        ):
            self.assertIn(example, self.skill)
        self.assertIn("Plain `/daf` and `/daf yomi`", self.skill)
        self.assertIn("## Provide Yomi completion and cycle context", self.skill)
        self.assertIn("within 14 days", self.skill)
        self.assertIn("Siyum HaShas", self.skill)

    def test_progress_is_yomi_only(self):
        self.assertIn("Only in Yomi mode", self.skill)
        self.assertIn("Never add this section to exact-daf mode", self.skill)
        self.assertIn("Yomi mode preserves the original calendar and progress context", self.readme)
        self.assertIn("It does not add unrelated Daf Yomi dates or cycle statistics", self.readme)

    def test_commentary_focus_contract(self):
        for heading in ("### `rashi`", "### `tosafot`"):
            self.assertIn(heading, self.skill)
        for example in (
            "/daf Chullin 23a-33b rashi deep",
            "/daf Chullin 23a-33b tosafot halacha",
            "/daf Chullin 23a-33b rashi tosafot advanced",
            "/daf yomi tosafot deep",
        ):
            self.assertIn(example, self.skill)
        self.assertIn("`tosafot`, `tosefot`, and `tosfos`", self.skill)

    def test_bounded_fast_path_contract(self):
        self.assertIn("## Keep ordinary requests fast", self.skill)
        self.assertIn("one calendar lookup and one consolidated source retrieval", self.skill)
        self.assertIn("not every comment on the daf", self.skill)
        self.assertIn("Reserve exhaustive commentary retrieval", self.skill)
        self.assertIn("## Performance boundaries", self.acceptance)
        self.assertIn("/daf yomi tosafot", self.acceptance)

    def test_legacy_command_removed_from_current_docs(self):
        current_docs = "\n".join((self.skill, self.readme, self.acceptance))
        self.assertNotIn("/dafyomi", current_docs)

    def test_acceptance_covers_expanded_modes(self):
        for heading in (
            "## Exact-daf mode",
            "## Exact-daf ranges",
            "## Yomi mode",
            "## Yomi completion and cycle context",
            "## Commentary and study modes",
        ):
            self.assertIn(heading, self.acceptance)
        self.assertIn("Mode isolation", self.acceptance)


class CalendarHelperTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.context = load_module("yomi_context", "scripts/yomi_context.py")

    def test_record_keeps_yomi_assignment_and_special_day(self):
        record = self.context._record(
            dt.date(2026, 8, 30),
            [
                {
                    "category": "dafyomi",
                    "title": "Chullin 122",
                    "hdate": "17 Elul 5786",
                    "hebrew": "Chullin 122 Hebrew",
                    "link": "https://www.sefaria.org/Chullin.122",
                },
                {"category": "roshchodesh", "title": "Rosh Chodesh"},
            ],
        )
        self.assertEqual(record["daf"], "Chullin 122")
        self.assertEqual(record["tractate"], "Chullin")
        self.assertEqual(record["page"], 122)
        self.assertEqual(record["special_days"][0]["title"], "Rosh Chodesh")

    def test_split_daf_title_handles_spaced_masechet(self):
        self.assertEqual(
            self.context._split_daf_title("Bava Batra 42"),
            ("Bava Batra", 42),
        )

    def test_find_masechet_finish_returns_yomi_countdown(self):
        start = dt.date(2026, 8, 30)
        payload = {
            "items": [
                {"date": "2026-08-30", "category": "dafyomi", "title": "Chullin 122"},
                {"date": "2026-08-31", "category": "dafyomi", "title": "Chullin 123"},
                {"date": "2026-09-01", "category": "dafyomi", "title": "Bekhorot 2"},
            ]
        }
        original = self.context._hebcal
        self.context._hebcal = lambda *_args, **_kwargs: payload
        try:
            finish, remaining = self.context._find_masechet_finish(start, "Chullin")
        finally:
            self.context._hebcal = original
        self.assertEqual(finish, dt.date(2026, 8, 31))
        self.assertEqual(remaining, 1)


class SefariaHelperTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sefaria = load_module("sefaria_fetch", "scripts/sefaria_fetch.py")

    def test_range_urls_preserve_exact_boundaries(self):
        api_url, source_url = self.sefaria.build_urls("Chullin 23a-33b")
        self.assertIn("Chullin%2023a-33b", api_url)
        self.assertEqual(source_url, "https://www.sefaria.org/Chullin_23a-33b")

    def test_commentary_range_urls_preserve_scope(self):
        api_url, source_url = self.sefaria.build_urls("Tosafot on Chullin 23a-33b")
        self.assertIn("Tosafot%20on%20Chullin%2023a-33b", api_url)
        self.assertEqual(source_url, "https://www.sefaria.org/Tosafot_on_Chullin_23a-33b")


if __name__ == "__main__":
    unittest.main()
