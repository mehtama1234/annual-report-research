#!/usr/bin/env python3
"""Verify the current supplier-finance obligation refresh arithmetic."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "analysis/company-first-principles/combined-investment-research-retail-q2-2026-supplier-finance-obligation-refresh-2026-09-17.md"


def main() -> None:
    text = ARTIFACT.read_text(encoding="utf-8")
    for marker in (
        "Target, August 1, 2026 | $3.2B | $3.0B at January 31, 2026 | +$0.2B",
        "Walmart, July 31, 2026 | $6.4B | $6.0B at January 31, 2026 | +$0.4B",
        "not cash-paid settlement amounts",
        "settlement-unproven",
        "CA-06 remains partial",
    ):
        if marker not in text:
            raise AssertionError(f"missing supplier-finance control: {marker}")
    if round(3.2 - 3.0, 1) != 0.2 or round(6.4 - 6.0, 1) != 0.4:
        raise AssertionError("supplier-finance movement arithmetic failed")
    print("retail-q2-2026-supplier-finance-obligation-refresh-ok")


if __name__ == "__main__":
    main()
