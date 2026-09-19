# New-sector valuation expectation register — 2026-09-17

The structured [valuation expectation CSV](data/combined-investment-research-new-sector-valuation-expectation-register-2026-09-17.csv)
is the source of truth for the six new company lanes. It records what the
market may be capitalizing against the currently visible reported denominator;
it is not a ranking and none of the denominators is normalized owner cash.

## What the screen says

| Company | Screen | Main required assumption |
| --- | ---: | --- |
| McKesson | `20.037x` reported OCF less PP&E/software | Specialty mix and working-capital cash survive claims and acquisition needs |
| Cencora | `18.914x` reported OCF less capex | Acquisition-led specialty growth earns more than its funding and integration burden |
| Cardinal Health | `29.071x` reported OCF less capex | Post-acquisition and post-contract-loss cash survives debt and legal claims |
| KLA | `63.286x` OCF less PP&E | Service and process-control economics remain strong through a semiconductor cycle |
| Equinix | `28.123x` OCF less recurring capex | Network density funds growth capex, power, leases, debt, and JV claims |
| Digital Realty | `26.641x` Core FFO | Backlog converts on schedule at stabilized yields after development and financing claims |

The screens are deliberately denominator-specific. Healthcare uses reported
cash-after-capex; KLA uses cash-after-PP&E; Equinix uses the management
recurring-capex screen; Digital Realty uses Core FFO because the packet's
reported public comparison is REIT-specific. These cannot be used as a pooled
multiple ranking.

## Promotion rule

The screen may inform a reverse valuation, but it cannot clear a thesis breaker
until the named owner-cash, reinvestment, claim, dilution, and legal-entity
fields are source-backed. A multiple that appears lower because it uses a
temporary working-capital benefit, non-GAAP add-back, partner funding, or
unfunded backlog remains a qualified expectation input.

Status: `six-lane-expectation-surface; qualified; no-ranking`
