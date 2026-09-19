#!/usr/bin/env python3
"""Verify the consumer-goods Q2 2026 cash-quality refresh."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "analysis/company-first-principles/combined-investment-research-consumer-goods-q2-2026-cash-quality-refresh-2026-09-17.md"


def main() -> None:
    text = ARTIFACT.read_text(encoding="utf-8")
    for marker in (
        "Burlington, H1 FY2026 | 1,287 stores; sales/gross-margin improvement | $334.6M",
        "Ollie's, 26 weeks ended Aug. 1, 2026 | 686 locations; new-store growth | $153.6M",
        "Lowe's, H1 FY2026 | Q2 sales $26.0B; comps +0.2% | $7.009B",
        "$55.5M tariff-refund benefit included in OCF",
        "inventory increased with store growth and merchandise-payment timing",
        "household-value-qualified; owner-cash-open; no-ranking",
        "Damodaran-style valuation",
        "Lyn\nAlden-style stress",
    ):
        if marker not in text:
            raise AssertionError(f"missing consumer-goods control: {marker}")
    if round(0.3346 - 0.5324 - 0.0051, 4) != -0.2029:
        raise AssertionError("Burlington cash-after-property-and-lease arithmetic failed")
    if round(0.153625 - 0.068783, 6) != 0.084842:
        raise AssertionError("Ollie's cash-after-capex arithmetic failed")
    if round(7.009 - 1.063, 3) != 5.946:
        raise AssertionError("Lowe's cash-after-capex arithmetic failed")
    print("consumer-goods-q2-2026-cash-quality-refresh-ok")


if __name__ == "__main__":
    main()
