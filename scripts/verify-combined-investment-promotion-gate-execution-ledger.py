#!/usr/bin/env python3
"""Verify the object-level promotion gate execution ledger."""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "analysis/company-first-principles/combined-investment-research-promotion-gate-execution-ledger-2026-09-17.md"
DATA = ROOT / "analysis/company-first-principles/data/combined-investment-research-promotion-gate-execution-ledger-2026-09-17.csv"

def main() -> int:
    if not REPORT.is_file() or not DATA.is_file():
        raise SystemExit("FAIL: promotion-gate ledger files missing")
    text = REPORT.read_text(encoding="utf-8")
    for marker in ("## Gate register", "Q-03 Wheaton–Antamina", "CA-06 / Q-04–Q-06 retail", "Q-13 URI asset-backed", "## Operating rule", "owner-cash-open", "## Decision"):
        if marker not in text:
            raise SystemExit(f"FAIL: promotion-gate marker missing: {marker}")
    with DATA.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required_fields = ("gate", "current_evidence", "next_source_object", "promotion_test", "stop_rule")
    if len(rows) != 13 or any(not all(row.get(key, "").strip() for key in required_fields) for row in rows):
        raise SystemExit(f"FAIL: expected 13 complete promotion-gate rows, found {len(rows)}")
    expected_gates = {
        "Q-03 Wheaton-Antamina",
        "CA-06 retail",
        "Q-13 URI asset-backed",
        "PBF refinancing",
        "Private credit",
        "Physical capacity",
        "Healthcare distribution",
        "Medical devices",
        "KLA semiconductor",
        "Power grid insurance",
        "Atwell",
        "Restaurant franchising",
        "Integrated oil gas",
    }
    if {row["gate"] for row in rows} != expected_gates:
        raise SystemExit("FAIL: promotion-gate identity set changed")
    by_gate = {row["gate"]: row for row in rows}
    required_substrings = {
        "Q-03 Wheaton-Antamina": ("BHP", "same-period", "settlement"),
        "CA-06 retail": ("lease", "service", "double subtract"),
        "Q-13 URI asset-backed": ("borrowing base", "NOLV", "availability"),
        "PBF refinancing": ("trustee", "liability", "NPV"),
        "Private credit": ("lender", "borrower", "repayment"),
    }
    for gate, needles in required_substrings.items():
        row_text = " ".join(by_gate[gate][field].lower() for field in required_fields)
        if any(needle.lower() not in row_text for needle in needles):
            raise SystemExit(f"FAIL: promotion-gate boundary weakened: {gate}")
    print("combined-investment-promotion-gate-execution-ledger-ok")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
