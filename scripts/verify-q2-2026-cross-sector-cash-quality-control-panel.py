from pathlib import Path


ARTIFACT = Path(__file__).parents[1] / "analysis/company-first-principles/combined-investment-research-q2-2026-cross-sector-cash-quality-control-panel-2026-09-17.md"


def main():
    text = ARTIFACT.read_text()
    markers = [
        "Fortinet H1 OCF `$2.121B`",
        "CF H1 OCF `$1.374B`",
        "Burlington H1 OCF `$334.6M`",
        "Retail denominator — TJX / Target / Walmart",
        "CA-06 partial; no ranking",
        "`$1.147B` operating-lease cash paid",
        "JPMorgan Q2 net income `$21.2B`",
        "ET Q2 adjusted EBITDA `$5.07B`",
        "COP H1 OCF `$11.729B`",
        "six different meanings",
        "Damodaran-style valuation",
        "Lyn Alden-style stress",
        "same period + same legal entity + named cash/claim object + reconciliation path",
        "q2-2026-cross-sector-cash-quality-control-panel-qualified",
    ]
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise SystemExit("FAIL: missing markers: " + "; ".join(missing))
    if text.count("| Qualified") < 3:
        raise SystemExit("FAIL: expected multiple qualified non-ranking lane statuses")
    print("q2-2026-cross-sector-cash-quality-control-panel-ok")


if __name__ == "__main__":
    main()
