from pathlib import Path


ARTIFACT = Path(__file__).parents[1] / "analysis/company-first-principles/combined-investment-research-q2-2026-valuation-liquidity-stress-matrix-2026-09-17.md"


def main():
    text = ARTIFACT.read_text()
    markers = [
        "Broad technology — Fortinet / Cloudflare",
        "Basic materials — CF / Sherwin-Williams / West Fraser",
        "Consumer goods — Burlington / Ollie's / Lowe's",
        "Ordinary finance — JPMorgan / American Express / Capital One",
        "Energy supply route — Energy Transfer / Cheniere / PBF / Devon",
        "Integrated oil and gas — ConocoPhillips / Exxon Mobil",
        "Damodaran-style valuation object",
        "Lyn Alden-style liquidity stress",
        "Financial shenanigans are falsifiable prompts",
        "expectation-screen-qualified; liquidity-stress-open; no-ranking",
        "q2-2026-valuation-liquidity-stress-matrix-qualified",
    ]
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise SystemExit("FAIL: missing markers: " + "; ".join(missing))
    if text.count("|") < 40:
        raise SystemExit("FAIL: expected six-lane matrix content")
    print("q2-2026-valuation-liquidity-stress-matrix-ok")


if __name__ == "__main__":
    main()
