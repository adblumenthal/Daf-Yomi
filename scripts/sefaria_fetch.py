#!/usr/bin/env python3
"""
Fetch a Sefaria textual reference using the public v3 Texts API.

Examples:
  python sefaria_fetch.py "Chullin 118a"
  python sefaria_fetch.py "Rashi on Chullin 118a"
"""

# Created by Adam Blumenthal in honor of David and Barbara Blumenthal,
# who always pushed him to keep asking questions.

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request

BASE = "https://www.sefaria.org/api/v3/texts/"
PAGE_BASE = "https://www.sefaria.org/"


def build_urls(ref: str, version: str = "primary") -> tuple[str, str]:
    """Build API and human-readable URLs without changing the requested scope."""
    tref_api = urllib.parse.quote(ref, safe="")
    tref_page = urllib.parse.quote(ref.replace(" ", "_"), safe="_:.:-")
    query = urllib.parse.urlencode({
        "version": version,
        "fill_in_missing_segments": "1",
        "return_format": "text_only",
    })
    return BASE + tref_api + "?" + query, PAGE_BASE + tref_page

def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    p = argparse.ArgumentParser()
    p.add_argument("ref", help='Sefaria ref, e.g. "Chullin 118a"')
    p.add_argument("--version", default="primary", help='Sefaria version selector; default "primary"')
    args = p.parse_args()

    url, source_url = build_urls(args.ref, args.version)

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "daf/2.0 (+Agent Skills)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            payload = json.load(resp)
    except Exception as exc:
        print(f"Sefaria request failed: {exc}", file=sys.stderr)
        return 1

    out = {
        "requested_ref": args.ref,
        "source_url": source_url,
        "data": payload,
    }
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
