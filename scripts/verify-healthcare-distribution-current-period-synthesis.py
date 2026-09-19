#!/usr/bin/env python3
"""Verify the healthcare-distribution current-period synthesis."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "analysis/company-first-principles/combined-investment-research-healthcare-distribution-current-period-synthesis-2026-09-17.md"


def main() -> int:
    if not REPORT.is_file():
        raise SystemExit(f"FAIL: missing healthcare-distribution synthesis: {REPORT.relative_to(ROOT)}")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "McKesson",
        "Cencora",
        "Cardinal Health",
        "These periods are deliberately not treated as a pooled ratio panel",
        "normalized-owner-cash-open; no-ranking",
        "The next decisive objects are",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: healthcare-distribution marker missing: {marker}")
    print("healthcare-distribution-current-period-synthesis-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
