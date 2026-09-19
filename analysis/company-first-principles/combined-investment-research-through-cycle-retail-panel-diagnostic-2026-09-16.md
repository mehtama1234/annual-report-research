# Through-cycle retail panel diagnostic

Research date: `2026-09-16`

## Purpose

This diagnostic applies a bounded descriptive test to the 18-row retail
longitudinal bridge. It asks whether the existing cash-after-property screen
moves differently in periods of positive versus negative real hourly earnings,
and in higher versus lower CPI regimes. It is a diagnostic of the proposed
mechanism, not causal identification and not normalized owner cash.

## Results

| Split | Observations | Mean cash after property ($M) | Median ($M) | Descriptive difference |
| --- | ---: | ---: | ---: | ---: |
| Real hourly earnings positive | 11 | 7,813.7 | 4,917.0 | +631.3M versus negative-real-earnings periods |
| Real hourly earnings negative | 7 | 7,182.4 | 3,994.0 | Reference group |
| CPI at least 4% | 12 | 7,401.6 | 4,405.5 | -499.9M versus CPI below 4% |
| CPI below 4% | 6 | 7,901.5 | 6,396.5 | Reference group |

The two splits point in different directions: cash-after-property is modestly
higher in positive-real-earnings observations, but lower in the higher-CPI
observations. That is compatible with an affordability mechanism, but the
pooled result is not a causal estimate. Walmart's scale materially affects the
mean, fiscal years overlap calendar years, and capex, inventory, vendor terms,
tariff support, promotions, store actions, services, and acquisitions are not
controlled in this diagnostic.

## Interpretation and promotion boundary

The result earns `descriptive-mechanism-screen`, not `promotion-ready`. It
adds a falsifiable quantitative checkpoint to the Q-10 protocol:

- the mechanism is not contradicted by the real-wage split;
- the CPI split shows that inflation pressure can dominate a simple real-wage
  comparison; and
- the pooled averages cannot rank the companies or establish that affordability
  caused cash outcomes.

Promotion still requires company-fixed-effect or matched-period analysis,
period-specific comparable sales and traffic, inventory/payable and support
controls, maintenance-capital allocation, and a subsequent filing breaker.
The underlying cash field remains a reported cash-after-property screen rather
than normalized common-owner cash.

Structured results: [panel diagnostic CSV](data/combined-investment-research-through-cycle-retail-panel-diagnostic-2026-09-16.csv).

Source panel: [longitudinal retail bridge](data/combined-investment-research-macro-longitudinal-retail-bridge-2026-09-15.csv),
with macro fields routed to the [historical regime validation](combined-investment-research-macro-historical-regime-validation-2026-09-15.md).
