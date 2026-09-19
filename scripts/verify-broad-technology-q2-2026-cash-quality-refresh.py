#!/usr/bin/env python3
"""Verify the broad-technology Q2 2026 cash-quality refresh."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "analysis/company-first-principles/combined-investment-research-broad-technology-q2-2026-cash-quality-refresh-2026-09-17.md"


def main() -> None:
    text = ARTIFACT.read_text(encoding="utf-8")
    for marker in (
        "Fortinet, H1 2026 | $2.048B | $2.121B | $1.972B",
        "Cloudflare, H1 2026 | $1.336B | $275.9M | $140.5M",
        "Deferred revenue $7.676B, up $559.9M",
        "gross margin declined to 72% from 75%",
        "cash-quality-qualified; owner-cash-and-cycle-open; no-ranking",
        "Damodaran-style valuation",
        "Lyn Alden-style stress",
    ):
        if marker not in text:
            raise AssertionError(f"missing broad-technology control: {marker}")
    if round(2.121 - 0.149, 3) != 1.972:
        raise AssertionError("Fortinet FCF arithmetic failed")
    if round(0.275894 - 0.115192 - 0.020244, 6) != 0.140458:
        raise AssertionError("Cloudflare FCF arithmetic failed")
    print("broad-technology-q2-2026-cash-quality-refresh-ok")


if __name__ == "__main__":
    main()
