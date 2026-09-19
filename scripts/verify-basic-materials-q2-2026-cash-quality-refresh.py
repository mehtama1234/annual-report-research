#!/usr/bin/env python3
"""Verify the basic-materials Q2 2026 cash-quality refresh."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "analysis/company-first-principles/combined-investment-research-basic-materials-q2-2026-cash-quality-refresh-2026-09-17.md"


def main() -> None:
    text = ARTIFACT.read_text(encoding="utf-8")
    for marker in (
        "CF Industries, H1 2026 | $1.374B | $494M",
        "Sherwin-Williams, H1 2026 | $1.487B | $246.7M",
        "West Fraser, Q2 2026 / H1 capex | $192M Q2 operating cash | $159M H1 capex",
        "$170M litigation settlement and $50M insurance proceeds",
        "cycle-qualified; owner-cash-open; no-ranking",
        "Damodaran-style valuation",
        "Lyn Alden-\nstyle stress",
    ):
        if marker not in text:
            raise AssertionError(f"missing basic-materials control: {marker}")
    if round(1.374 - 0.494, 3) != 0.880:
        raise AssertionError("CF OCF-less-capex arithmetic failed")
    if round(1.4866 - 0.2467 - 0.0649, 4) != 1.1750:
        raise AssertionError("Sherwin-Williams cash-after-capex-and-acquisition arithmetic failed")
    print("basic-materials-q2-2026-cash-quality-refresh-ok")


if __name__ == "__main__":
    main()
