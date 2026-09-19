# Combined investment research: investments-repository bridge

Research date: `2026-09-15`

The annual-report-research system is connected to the sibling `investments`
repository through the article-replay, Lyn Alden/Damodaran workflow, and
hard-gate process. That connection is useful because it supplies hypotheses,
regime context, valuation questions, and explicit failure gates before the
annual-report layer is opened.

## What crosses the repository boundary

| Investments-repository artifact | Role in this goal | Boundary |
| --- | --- | --- |
| `analysis/combined-analysis-workflow.md` | Shared Lyn Alden, Damodaran, CFI, and independent-analysis workflow | Method guidance does not prove a company fact or valuation assumption |
| `analysis/hard_gate_data_acquisition_batch.csv` and related hard-gate outputs | Article-derived metric requests, evidence acquisition, and pass/block decisions | A resolved metric still needs company-period and denominator validation in this repository |
| `first_principles_alignment.html` | Article stance versus current fundamentals alignment surface | Alignment is a triage signal, not a recommendation or primary filing substitute |
| `analysis/sector-research-program-goal.md` | Broader sector-study and completion framework | Broader scope is not evidence that one of the three active pilots is complete |

## Required bridge sequence

```text
article or macro stance
  -> extracted hypothesis and named ticker/industry
  -> hard gate: exact metric, period, denominator, and source
  -> social / Inc. 5000 / IBIS context
  -> annual report or SEC filing
  -> owner-cash and liability normalization
  -> Damodaran valuation range
  -> Lyn Alden transmission and liquidity stress
  -> measurable filing-based thesis breaker
```

The bridge prevents two common errors: treating an article's confidence as
company evidence, and treating a current market/valuation screen as proof that
the article thesis was correct. A connected conclusion is allowed only when the
article or macro hypothesis survives the filing-period, denominator, cash, and
falsifier tests.

## Hard-gate operating snapshot

The sibling verification report provides an auditable state for the upstream
triage layer: `473` pattern-screen rows, `75` actionable rows, `75` source
execution rows, `75` filled execution rows, `40` `blocked_by_hard_gate`
decisions, `35` `passes_hard_gate` decisions, `701` resolved metric rows, and
`36` resolved adapters. The acquisition batch itself has zero rows, and the
remaining metric-gap file has zero rows. These counts prove that the sibling
hard-gate process is operational; they do not mean all 75 article-derived
decisions are imported into the three active pilots. The local bridge imports
only the selected affordability, commodity/liquidity, and financial-
intermediation routes, then requires fresh company-period and denominator
validation in the pilot ledgers.

This is the important handoff boundary: an upstream `passes_hard_gate` result
permits a filing test to be prioritized, not a company conclusion to be
promoted. A downstream pilot can still remain `qualified`, `partial`, or
`unresolved` after the upstream gate passes.

The current three pilots use this bridge selectively. Pilot 02 carries the
affordability/substitution hypothesis into TJX, Target, and Walmart. Pilot 01
now also carries a dated 2021 WPM commodity/liquidity article signal into the
BHP Antamina contract, delivery, financing, valuation, and falsifier tests;
the detailed handoff is in the [Pilot 01 article bridge](combined-investment-research-pilot-01-investments-article-handoff.md).
Pilot 03 uses the same hard-gate discipline for named capital flows even when
the initial hypothesis came from macro or investment-method research.

Primary local source routes:

- [Investments combined-analysis workflow](../../../investments/analysis/combined-analysis-workflow.md)
- [Investments hard-gate process](../../../investments/analysis/hard_gate_process_verification.md)
- [Investments first-principles alignment surface](../../../investments/first_principles_alignment.html)
