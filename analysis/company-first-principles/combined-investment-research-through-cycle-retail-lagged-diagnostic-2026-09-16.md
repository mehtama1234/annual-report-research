# Through-cycle retail lagged diagnostic

Research date: `2026-09-16`

## Purpose

The proposed affordability mechanism should have a lead: the prior period's
real-wage condition should help predict the following period's cash-after-
property change. This diagnostic applies that lagged sign test to the existing
retail bridge, excluding transitions with zero prior real-wage change or zero
cash change.

## Result

Among 15 usable transitions, the prior real-wage sign and following cash-screen
change agree in `7` cases and disagree in `8`. Positive prior real-wage rows
split `4/4`; negative prior real-wage rows split `3/4`.

| Prior real-wage condition | Usable transitions | Same direction | Opposite direction | Result |
| --- | ---: | ---: | ---: | --- |
| Positive | 8 | 4 | 4 | `descriptive-mechanism-screen` |
| Negative | 7 | 3 | 4 | `descriptive-mechanism-screen` |
| Total | 15 | 7 | 8 | `descriptive-mechanism-screen` |

The lagged test does not show a stable lead in this small panel. It is useful
as a falsifier: a simple prior-real-wage-to-next-cash story is not sufficient
to explain the observed transitions. Fiscal-year overlap, capex timing,
inventory and vendor terms, tariffs/refunds, promotions, store actions, and
attached services remain uncontrolled. The cash field is also a reported
cash-after-property screen rather than normalized owner cash.

## Promotion boundary

Status: `lagged descriptive screen; causal promotion not earned`.

Promotion requires matched fiscal periods, company-specific demand metrics,
explicit support and working-capital controls, maintenance-capital allocation,
and enough repeated observations to distinguish the macro signal from company
actions and accounting timing.

Structured result: [lagged diagnostic CSV](data/combined-investment-research-through-cycle-retail-lagged-diagnostic-2026-09-16.csv).
Source panel: [longitudinal retail bridge](data/combined-investment-research-macro-longitudinal-retail-bridge-2026-09-15.csv).
