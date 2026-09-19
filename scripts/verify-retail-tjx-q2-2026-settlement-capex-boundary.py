#!/usr/bin/env python3
"""Verify the current-period TJX settlement and capex boundary."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "analysis/company-first-principles/combined-investment-research-retail-tjx-q2-2026-settlement-capex-boundary-2026-09-17.md"

def main() -> int:
    if not REPORT.is_file():
        raise SystemExit("FAIL: missing TJX settlement/capex boundary")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "TJX Q2 FY2027 Form 10-Q",
        "credit-card interchange-fee settlement",
        "non-recurring `$419M` gain net of legal expenses",
        "quarter ended May 2, 2026",
        "Gross cash received versus legal expenses",
        "tariff refunds",
        "`$2.2B–$2.3B`",
        "`$1.147B` of",
        "H1 operating cash flows paid for operating leases",
        "CA-06-partial",
        "temporary-support-visible; maintenance-open;",
        "2026-09-18 official Q2 source refresh",
        "does not provide a gross bank-receipt/legal-payment schedule",
        "23 net store additions in the quarter",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: TJX boundary marker missing: {marker}")
    print("retail-tjx-q2-2026-settlement-capex-boundary-ok")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
