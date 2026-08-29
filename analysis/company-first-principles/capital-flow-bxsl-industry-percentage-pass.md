# Capital Flow BXSL Industry Percentage Pass

## What This Adds

This pass upgrades BXSL from a top-ten exhibit estimate to a filed 10-Q industry distribution.

Local source:

`raw/primary-sources/capital-flow/blackstone-secured-lending-fund/q2-2026/bxsl-2026-q2-10q.html`

Local data file:

`analysis/company-first-principles/data/capital-flow-bxsl-official-industry-percentages.csv`

Parser:

`scripts/extract-bxsl-industry-percentages.py`

## Reconciliation

BXSL's Q2 2026 10-Q gives industry percentages of total investments at fair value. The parser converts each percentage to dollars using the filed total investments at fair value of `13.364295B USD`.

| Check | Result |
|---|---:|
| Industry rows extracted | `40` |
| Percentage total | `100.0%` |
| Converted fair value total | `13.364295B USD` |
| Reconciliation delta | `0.000B USD` |

## Top BXSL Industry Lanes

| BXSL Industry | Filed Share | Converted Fair Value |
|---|---:|---:|
| Software | `18.9%` | `2.526B USD` |
| Health Care Providers & Services | `10.3%` | `1.377B USD` |
| Professional Services | `10.3%` | `1.377B USD` |
| Insurance | `10.0%` | `1.336B USD` |
| Commercial Services & Supplies | `8.3%` | `1.109B USD` |
| IT Services | `4.7%` | `0.628B USD` |
| Health Care Technology | `4.5%` | `0.601B USD` |
| Diversified Consumer Services | `4.4%` | `0.588B USD` |
| Aerospace & Defense | `3.3%` | `0.441B USD` |
| Air Freight & Logistics | `3.3%` | `0.441B USD` |

## Claim Effect

This strengthens the cross-BDC destination map.

Before this pass, BXSL added only disclosed top-ten industry percentages from the earnings exhibit. After this pass, BXSL contributes a full filed 10-Q industry distribution that reconciles to 100% of total investments at fair value.

The cross-BDC comparison still has one important caveat: ARCC and OBDC provide official fair-value subtotals directly, while BXSL provides official percentages that are converted into fair-value dollars. That is strong enough for lane ranking, but borrower-level proof still needs schedule rows and transaction documents.

## Simple Version

BXSL confirms the same pattern with a cleaner source.

Its filed 10-Q says the biggest lending lanes are software, healthcare services, professional services, insurance, commercial services, IT services, healthcare technology, consumer services, aerospace/defense, and logistics.

That makes the borrower-lane thesis stronger and gives us better targets for the next source-of-funds pass.
