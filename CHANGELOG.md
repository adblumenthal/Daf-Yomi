# Changelog

All notable changes to Daf are documented here.

## 2.0.0 — 2026-08-31

Breaking command update.

### Added

- `/daf <Masechet> <daf>` for a full lesson on any exact daf or amud, independent of the Daf Yomi schedule.
- Inclusive same-masechet ranges such as `/daf Chullin 23a-33b`, grouped by perek and major sugya with a coverage checklist.
- `/daf yomi` for the current daily assignment, preserving the original guided Daf Yomi study experience.
- Plain `/daf` as a shortcut for `/daf yomi`.
- Exact-daf continuity rules that locate a request within its perek and preview the next amud or daf.
- `rashi` and `tosafot` focus modes for single dafim, exact ranges, and Yomi requests, including common Tosafot spelling variants.
- Automated release checks for command routing, exact ranges, commentary focus, documentation, and mode-specific progress behavior.

### Changed

- Renamed the skill and primary command from `/dafyomi` to `/daf`.
- Moved relative dates, explicit dates, and date-based catch-up ranges under `/daf yomi`.
- Kept masechet countdowns, siyum planning, and cycle progress in Yomi mode while excluding them from named-daf and exact-range requests.
- Updated help, examples, source guidance, UI metadata, helper behavior, and acceptance cases for the expanded command model.
- Added a bounded fast path for ordinary single-daf requests: consolidated source retrieval, selected commentary by default, and comprehensive research reserved for `deep`, `show sources`, or explicit requests.

### Removed

- Calendar and cycle-progress material from exact-daf and exact-range output.

## 1.0.0 — 2026-08-30

First public-ready release as Daf Yomi Tutor.

### Added

- Guided lesson structure with Mishnah, sugyot, Rashi/Tosafot, halacha, Aramaic, key takeaways, and review.
- `short`, `deep`, `halacha`, `beginner`, and `advanced` modes.
- Relative dates, explicit dates, and inclusive catch-up ranges.
- "Where are we?" perek/continuity context and next-page preview.
- Special-day notices.
- Masechet completion countdowns, siyum planning, and Daf Yomi cycle context.
- Hebcal and Sefaria grounding without API keys or an MCP requirement.
- Optional outside shiur links.
- Source links on demand.
- Verification and failure-state rules.
- Acceptance-test checklist.
- MIT License.
- Dedication to David and Barbara Blumenthal.
