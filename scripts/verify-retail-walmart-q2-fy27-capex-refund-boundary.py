#!/usr/bin/env python3
"""Verify the current-period Walmart capex/refund boundary."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "analysis/company-first-principles/combined-investment-research-retail-walmart-q2-fy27-capex-refund-boundary-2026-09-17.md"

def main() -> int:
    if not REPORT.is_file():
        raise SystemExit("FAIL: missing Walmart Q2 capex/refund boundary")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "Walmart's July 31, 2026 Form 10-Q",
        "`$2.9B`",
        "`$19.710B`",
        "`$14.181B`",
        "`$5.529B`",
        "excludes debt service and acquisitions",
        "CA-06-partial; no-ranking",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: Walmart boundary marker missing: {marker}")
    print("retail-walmart-q2-fy27-capex-refund-boundary-ok")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
