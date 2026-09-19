#!/usr/bin/env python3
"""Verify the current-period URI availability/lifecycle boundary."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "analysis/company-first-principles/combined-investment-research-uri-q2-2026-availability-lifecycle-boundary-2026-09-17.md"

def main() -> int:
    if not REPORT.is_file():
        raise SystemExit("FAIL: missing URI Q2 availability/lifecycle boundary")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "United Rentals",
        "`$2.999B`",
        "`$1.779B`",
        "`$3.305B`",
        "`$1.149B`",
        "`$2.802B` ABL borrowing capacity",
        "`$85M` accounts-receivable securitization capacity",
        "populated borrowing-base certificate",
        "targeted review of the June 30, 2026 10-Q",
        "found no populated NOLV or",
        "searched-negative boundary",
        "Q-13-qualified; availability-partial; lifecycle-return-open",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: URI boundary marker missing: {marker}")
    print("uri-q2-2026-availability-lifecycle-boundary-ok")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
