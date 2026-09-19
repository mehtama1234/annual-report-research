# Longitudinal retail cash/regime bridge — 2026-09-15

This artifact joins the reported retail cash-after-property screen to the
official macro regime panel over multiple fiscal periods. It is a timing and
falsifier bridge, not a causal regression: fiscal years do not exactly match
calendar years, and the cash screen is not normalized owner cash.

## Method

For each retailer, the fiscal period is assigned to the calendar regime that
covers most of the fiscal year. The join preserves the reported operating-cash
flow-less-property denominator already used in the retail owner-cash bridge.
It does not silently adjust for inventory, vendor terms, tariffs, leases,
maintenance capital, taxes, stock compensation, or attached-service costs.

The test question is:

> When inflation, policy rates, and real wages move through different regimes,
> does the reported cash screen change in a way that is at least consistent
> with the proposed affordability and financing mechanisms, and what contrary
> result would require investigation?

## Joined panel

The structured rows are in the [longitudinal bridge CSV](data/combined-investment-research-macro-longitudinal-retail-bridge-2026-09-15.csv).

The panel shows cash-screen variation across regimes, but the variation cannot
be attributed to macro conditions alone. Retail-specific pricing, inventory
timing, vendor financing, acquisitions, capex cycle, tariffs, and company
mixes remain confounders.

## Falsifiable reading

- A falling cash screen during a disinflationary or real-wage-recovery regime
  would not automatically disprove the affordability mechanism; company
  execution and reinvestment could dominate.
- A resilient cash screen during an inflation/real-wage squeeze is evidence
  consistent with value positioning, but it is not proof of causal pricing
  power or durable owner cash.
- A future period with comparable fiscal timing, weaker real wages, and a
  simultaneous deterioration in traffic, margin, inventory conversion, and
  cash would be a stronger test of the affordability thesis.
- The same-period test must be rerun after the next filings, with reported
  burdens and temporary benefits separated before any valuation promotion.

## Current grade

`longitudinal-regime-bridge-partial`: the macro panel is now attached to
multiple company-period cash screens with an explicit fiscal-alignment rule.
This improves reproducibility and falsifiability but does not close causal
attribution or normalized owner-cash proof.

## Sources

- [Historical macro-regime validation](combined-investment-research-macro-historical-regime-validation-2026-09-15.md)
- [Retail owner-cash bridge](combined-investment-research-pilot-02-retail-owner-cash-bridge.md)
- [Retail burden normalization](combined-investment-research-pilot-02-retail-burden-normalization.md)
