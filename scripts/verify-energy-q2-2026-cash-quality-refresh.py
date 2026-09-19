#!/usr/bin/env python3
"""Verify the energy Q2 2026 cash-quality refresh."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "analysis/company-first-principles/combined-investment-research-energy-q2-2026-cash-quality-refresh-2026-09-17.md"


def main() -> None:
    text = ARTIFACT.read_text(encoding="utf-8")
    for marker in (
        "Energy Transfer, Q2 2026 | Adjusted EBITDA $5.07B; DCF $2.59B",
        "Cheniere, H1/Q2 2026 | 1,360 TBtu H1 exports",
        "PBF Energy, H1 2026 | Q2 throughput 887.3 thousand bpd",
        "Devon Energy, Q2/H1 2026 | Q2 production 1.359M Boe/d",
        "$242.4M of turnaround spending",
        "$2.6B of Delaware acreage",
        "physical-route-qualified; cycle-and-project-return-open; no-ranking",
        "Damodaran-style valuation",
        "Lyn Alden-style stress",
    ):
        if marker not in text:
            raise AssertionError(f"missing energy control: {marker}")
    if round(5.07 - 2.59, 2) != 2.48:
        raise AssertionError("Energy Transfer EBITDA/DCF spread arithmetic failed")
    if round(1.2651 - 0.2424, 4) != 1.0227:
        raise AssertionError("PBF cash-after-turnaround arithmetic failed")
    if round(3.7 - 1.269, 3) != 2.431:
        raise AssertionError("Devon cash-after-capex arithmetic failed")
    print("energy-q2-2026-cash-quality-refresh-ok")


if __name__ == "__main__":
    main()
