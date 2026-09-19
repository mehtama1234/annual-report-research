#!/usr/bin/env python3
"""Verify arithmetic and boundary markers for the two latest retail refreshes."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKING = ROOT / "analysis/company-first-principles/combined-investment-research-retail-q2-2026-working-capital-denominator-refresh-2026-09-17.md"
CAPEX = ROOT / "analysis/company-first-principles/combined-investment-research-retail-q2-2026-capex-allocation-sensitivity-2026-09-17.md"


def require(text: str, marker: str) -> None:
    if marker not in text:
        raise AssertionError(f"missing control marker: {marker}")


def main() -> None:
    working = WORKING.read_text(encoding="utf-8")
    capex = CAPEX.read_text(encoding="utf-8")
    for marker in (
        "latest official interim filings",
        "TJX | $3.345B | $1.159B | $2.186B",
        "Target | $4.519B | $2.404B | $2.115B",
        "Walmart | $19.710B | $14.181B | $5.529B",
        "not normalized owner cash",
        "It does not close CA-06",
    ):
        require(working, marker)
    for marker in (
        "Walmart's six-month property spending of `$14.181B`",
        "New stores, expansions, and relocations | `$1.087B`",
        "The other `$13.094B` is a mixed remainder",
        "Q-05 remains `evidence-insufficient`",
    ):
        require(capex, marker)
    if 14_181 - 1_087 != 13_094:
        raise AssertionError("Walmart mixed capex remainder arithmetic failed")
    if 19_710 - 14_181 != 5_529:
        raise AssertionError("Walmart OCF-less-property arithmetic failed")
    if 3_345 - 1_159 != 2_186 or 4_519 - 2_404 != 2_115:
        raise AssertionError("TJX/Target OCF-less-property arithmetic failed")
    print("retail-q2-2026-denominator-refreshes-ok")


if __name__ == "__main__":
    main()
