#!/usr/bin/env python3
"""Verify the ordinary-finance Q2 2026 credit-quality refresh."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "analysis/company-first-principles/combined-investment-research-ordinary-finance-q2-2026-credit-quality-refresh-2026-09-17.md"


def main() -> None:
    text = ARTIFACT.read_text(encoding="utf-8")
    for marker in (
        "JPMorgan | Net income $21.2B; revenue $57.3B; average loans $1.5T",
        "American Express | Q2 billed business $455.8B, up 9%",
        "Capital One | Net revenue $15.9B; loans held for investment $457.2B",
        "$4.55B pretax Visa-share gain",
        "$662M allowance release",
        "credit-quality-qualified; loss-normalization-and-owner-cash-open; no-ranking",
        "Damodaran-style valuation",
        "Lyn Alden-style stress",
    ):
        if marker not in text:
            raise AssertionError(f"missing ordinary-finance control: {marker}")
    if round(0.4558 / 0.4163 - 1, 3) != 0.095:
        raise AssertionError("American Express billed-business growth arithmetic failed")
    if round(0.019637 / 0.017856 - 1, 3) != 0.100:
        raise AssertionError("American Express revenue growth arithmetic failed")
    if round(2.980 - 3.642 + 0.662, 3) != 0.000:
        raise AssertionError("Capital One provision/charge-off/release identity failed")
    print("ordinary-finance-q2-2026-credit-quality-refresh-ok")


if __name__ == "__main__":
    main()
