from pathlib import Path


ROOT = Path(__file__).parents[1]
ARTIFACT = ROOT / "analysis/company-first-principles/capital-flow-wheaton-antamina-q03-metal-credit-receipt-boundary-2026-09-17.md"
TABLE = ROOT / "analysis/company-first-principles/data/capital-flow-wheaton-antamina-q03-metal-credit-receipt-boundary-2026-09-17.csv"


def main():
    text = ARTIFACT.read_text()
    markers = [
        "settles through metal credits with no physical delivery",
        "BHP received `$4.3B` upfront consideration",
        "Combined Antamina attributable production was `2.319M` ounces",
        "BHP-only credited ounces",
        "Wheaton's April 1 `$4.3B`",
        "upfront closing-funds-flow direction",
        "credit issue date",
        "Wheaton bank receipt",
        "Q-03 remains `full-return-inputs-incomplete`",
        "physical delivery is not required",
        "30.375%",
        "20.25%",
        "portfolio aggregation of the BHP and legacy Glencore streams",
        "$650M",
        "approximately `$1.4B` for H1",
        "debt drawn to partially fund the BHP PMPA",
        "Q2 sales were `$150.549M`",
        "H1 sales\nwere `$277.563M`",
        "`$122.039M` of operating cash flow",
        "`$222.223M` of operating cash flow",
        "must not be assigned to the BHP PMPA",
        "capital-flow-wheaton-antamina-q03-metal-credit-receipt-boundary-2026-09-17.csv",
    ]
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise SystemExit("FAIL: missing markers: " + "; ".join(missing))
    if not TABLE.is_file():
        raise SystemExit(f"FAIL: missing structured companion: {TABLE}")
    rows = [line for line in TABLE.read_text().splitlines() if line.strip()]
    if len(rows) != 14 or not rows[0].startswith("boundary_id,evidence_gate"):
        raise SystemExit("FAIL: Q-03 receipt table must contain thirteen evidence rows")
    print("wheaton-antamina-q03-metal-credit-receipt-boundary-ok")


if __name__ == "__main__":
    main()
