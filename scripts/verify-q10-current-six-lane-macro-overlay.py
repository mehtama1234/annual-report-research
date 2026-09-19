from pathlib import Path


ARTIFACT = Path(__file__).parents[1] / "analysis/company-first-principles/combined-investment-research-q10-current-six-lane-macro-overlay-2026-09-17.md"


def main():
    text = ARTIFACT.read_text()
    markers = [
        "Broad technology — Fortinet / Cloudflare",
        "Basic materials — CF / Sherwin-Williams / West Fraser",
        "Consumer goods — Burlington / Ollie's / Lowe's",
        "Ordinary finance — JPMorgan / American Express / Capital One",
        "Energy supply route — Energy Transfer / Cheniere / PBF / Devon",
        "Integrated oil and gas — ConocoPhillips / Exxon Mobil",
        "Align the macro observation, company reporting period",
        "Use both positive and negative cases",
        "Damodaran-style valuation",
        "Lyn Alden-style",
        "macro-route-visible; company-response-observed;\ncausal-promotion-open",
        "q10-current-six-lane-macro-overlay-qualified",
    ]
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise SystemExit("FAIL: missing markers: " + "; ".join(missing))
    if text.count("|") < 40:
        raise SystemExit("FAIL: expected six-lane macro table")
    print("q10-current-six-lane-macro-overlay-ok")


if __name__ == "__main__":
    main()
