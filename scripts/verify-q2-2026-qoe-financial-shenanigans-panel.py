from pathlib import Path


ARTIFACT = Path(__file__).parents[1] / "analysis/company-first-principles/combined-investment-research-q2-2026-qoe-financial-shenanigans-panel-2026-09-17.md"


def main():
    text = ARTIFACT.read_text()
    markers = [
        "Fortinet H1 deferred revenue rose `$559.9M`",
        "CF H1 OCF included `$170M` litigation",
        "Burlington included a `$55.5M` tariff refund",
        "JPMorgan had a `$4.55B` Visa-share gain",
        "ET reports adjusted EBITDA/DCF",
        "COP H1 production declined while OCF rose",
        "Retail QoE / CA-06 diagnostic boundary",
        "TJX H1 OCF included a credit-card interchange-fee settlement",
        "`$1.147B` operating-lease cash paid",
        "`$3.2B` supplier-finance obligations that were not actual early payments",
        "about `$2.9B` tariff refunds",
        "CA-06 partial; no ranking",
        "Sloan-style accrual and cash-conversion prompts",
        "Schilit-style unusual-item prompts",
        "Beneish-style composite boundary",
        "diagnostic-signal-observed; reconciliation-open; no-fraud-finding; no-ranking",
        "q2-2026-qoe-financial-shenanigans-panel-qualified",
    ]
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise SystemExit("FAIL: missing markers: " + "; ".join(missing))
    if text.count("|") < 40:
        raise SystemExit("FAIL: expected six-lane QoE table")
    print("q2-2026-qoe-financial-shenanigans-panel-ok")


if __name__ == "__main__":
    main()
