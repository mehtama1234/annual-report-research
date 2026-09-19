from pathlib import Path


ARTIFACT = Path(__file__).parents[1] / "analysis/company-first-principles/combined-investment-research-integrated-oil-gas-q2-2026-cash-quality-refresh-2026-09-17.md"


def main():
    text = ARTIFACT.read_text()
    markers = [
        "ConocoPhillips | H1 2026 operating cash flow `$11.729B`",
        "Exxon Mobil | H1 2026 operating cash flow `$32.260B`",
        "H1 production `2.278M BOE/d`, down from `2.391M BOE/d`",
        "H1 oil-equivalent production `4.554M BOE/d`, down from `4.591M BOE/d`",
        "`$5.757B` for ConocoPhillips (`$11.729B - $5.972B`)",
        "`$19.263B`",
        "`$81M` Surmont contingent-consideration payment",
        "`$1.199B` upstream identified-item loss",
        "`$3.857B`",
        "Damodaran-style valuation",
        "Lyn Alden-style stress",
        "physical-asset-qualified; cycle-and-replacement-open; no-ranking",
        "integrated-oil-gas-q2-2026-cash-quality-refresh-qualified",
    ]
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise SystemExit("FAIL: missing markers: " + "; ".join(missing))

    if round(11.729 - 5.972, 3) != 5.757:
        raise SystemExit("FAIL: ConocoPhillips residual arithmetic")
    if round(32.260 - 12.997, 3) != 19.263:
        raise SystemExit("FAIL: Exxon Mobil residual arithmetic")

    print("integrated-oil-gas-q2-2026-cash-quality-refresh-ok")


if __name__ == "__main__":
    main()
