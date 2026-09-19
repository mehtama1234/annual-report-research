#!/usr/bin/env python3
"""Verify the current-period Target cash-quality boundary."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "analysis/company-first-principles/combined-investment-research-retail-target-q2-2026-cash-quality-boundary-2026-09-17.md"

def main() -> int:
    if not REPORT.is_file():
        raise SystemExit("FAIL: missing Target Q2 cash-quality boundary")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "Target's August 1, 2026 Form 10-Q",
        "`$4.519B`",
        "`$994M`",
        "`$3.2B`",
        "does not represent actual early payments",
        "up to 120 days from invoice date",
        "future promotion still requires a dated",
        "CA-06-partial; no-ranking",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: Target boundary marker missing: {marker}")
    print("retail-target-q2-2026-cash-quality-boundary-ok")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
