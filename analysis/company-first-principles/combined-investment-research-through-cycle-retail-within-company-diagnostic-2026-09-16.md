# Through-cycle retail within-company diagnostic

Research date: `2026-09-16`

## Purpose

This diagnostic removes the largest pooled-panel distortion—company scale—by
comparing each retailer with its own prior fiscal-period observation. It tests
whether changes in real hourly earnings and changes in the reported
cash-after-property screen move in the same direction. It is still descriptive:
fiscal periods overlap calendar years, and the cash denominator is not
normalized owner cash.

## Result

Across the 15 within-company transitions, real hourly earnings changed in 12
transitions. The cash screen moved in the same direction in `6` and the
opposite direction in `6`; in `3` transitions real hourly earnings were
unchanged. This is a split result, not a stable causal relationship.

| Test | Transitions | Same direction | Opposite direction | No real-wage change | Result |
| --- | ---: | ---: | ---: | ---: | --- |
| Retailer-fixed, year-over-year transition screen | 15 | 6 | 6 | 3 | `descriptive-mechanism-screen` |

Examples of contrary evidence include Target's FY2022-to-FY2023 cash-screen
recovery while real hourly earnings were unchanged, and Target's FY2024-to-
FY2025 cash-screen decline while real hourly earnings improved. Walmart's
FY2025-to-FY2026 recovery is directionally consistent with the proposed
mechanism, but company actions and capital-cycle timing remain unresolved.

## Promotion boundary

The within-company result is stronger than a pooled mean comparison because it
does not compare Walmart's scale with TJX or Target. It still cannot identify
affordability causality. The next promotion step requires matched fiscal
periods with comparable sales, traffic, mix, markdowns, inventory/payables,
temporary support, maintenance capital, attached services, leases, taxes, and
store actions. A subsequent filing must be able to break the proposed demand-
to-cash mechanism, not merely show another coincident cash change.

Status: `within-company descriptive screen; causal promotion not earned`.

Structured transitions: [within-company diagnostic CSV](data/combined-investment-research-through-cycle-retail-within-company-diagnostic-2026-09-16.csv).
Source panel: [longitudinal retail bridge](data/combined-investment-research-macro-longitudinal-retail-bridge-2026-09-15.csv).
