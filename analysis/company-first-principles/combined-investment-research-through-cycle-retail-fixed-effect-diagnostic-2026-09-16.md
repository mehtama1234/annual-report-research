# Through-cycle retail fixed-effect diagnostic

Research date: `2026-09-16`

## Purpose

This diagnostic adds a simple company-demeaned association to the existing
within-company direction screen. It removes each retailer's mean level before
comparing real-hourly-earnings changes with cash-after-property changes. It is
not a causal regression, significance test, or normalized owner-cash result.

The structured [fixed-effect diagnostic CSV](data/combined-investment-research-through-cycle-retail-fixed-effect-diagnostic-2026-09-16.csv)
is the source of truth. The calculation uses only nonzero real-wage-change
transitions from the existing 15-transition within-company panel: four each
for TJX, Target, and Walmart, and twelve pooled usable transitions.

## Result

The pooled company-demeaned correlation is `0.113120`, a weak positive
descriptive association. Company-level correlations are also weak: `0.210861`
for TJX, `0.198533` for Target, and `0.152991` for Walmart. The small sample,
large cash-denominator movements, fiscal/calendar overlap, capex timing,
inventory and payable cycles, promotions, tariffs, vendor terms, and store
actions prevent causal interpretation.

## Promotion boundary

This result is useful as a falsifier against a strong universal
affordability-to-cash claim: removing company scale does not produce a strong
relationship. Promotion would require more matched periods and controls for
comparable sales, traffic, mix, markdowns, support, maintenance capital,
leases, taxes, and attached services. The correct status is
`fixed-effect-descriptive-only`.
