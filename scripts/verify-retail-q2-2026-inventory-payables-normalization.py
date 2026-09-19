#!/usr/bin/env python3
"""Verify the Q2 2026 retail inventory/payables normalization arithmetic."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "analysis/company-first-principles/combined-investment-research-retail-q2-2026-inventory-payables-normalization-2026-09-17.md"


def main() -> None:
    text = ARTIFACT.read_text(encoding="utf-8")
    markers = (
        "latest official interim filings",
        "TJX | $7.297B → $7.862B | +$565M | $(603)M | $4.575B → $5.024B | +$449M | +$470M | $116M use",
        "Target | $12.304B → $13.249B | +$945M | $(945)M | $12.622B → $13.306B | +$684M | +$612M | $261M use",
        "Walmart | $58.851B → $61.600B | +$2.749B | $(2.660)B | $63.061B → $64.318B | +$1.257B | +$1.648B | $1.492B use",
        "does not support subtracting `$116M`, `$261M`, or `$1.492B` again",
        "does not close it",
    )
    for marker in markers:
        if marker not in text:
            raise AssertionError(f"missing normalization control: {marker}")
    cases = ((7_862 - 7_297) - (5_024 - 4_575), 116), ((13_249 - 12_304) - (13_306 - 12_622), 261), ((61_600 - 58_851) - (64_318 - 63_061), 1_492)
    for actual, expected in cases:
        if actual != expected:
            raise AssertionError(f"expected mechanical use {expected}, got {actual}")
    print("retail-q2-2026-inventory-payables-normalization-ok")


if __name__ == "__main__":
    main()
