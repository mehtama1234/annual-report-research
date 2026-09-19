# Capital Flow Ares Frontline ASIF Roll-Forward

Research date: `2026-09-18`

## Purpose

This pass tests whether the Ares Strategic Income Fund's Frontline position
can be followed across consecutive public reporting periods. It distinguishes
an observable position change from proof of a borrower draw, purchase
settlement, or lender receipt.

## Same-vehicle observations

| ASIF reporting point | Principal | Amortized cost | Fair value | Terms |
|---|---:|---:|---:|---|
| March 31, 2026 | `$76.6927M` | `$76.1197M` | `$76.6927M` | SOFR(M) + `5.00%`; `2.00%` PIK; maturity `03/2032` |
| June 30, 2026 | `$96.7893M` | `$95.9022M` | `$94.9240M` | SOFR(M) + `5.00%`; `2.00%` PIK; maturity `03/2032`; related revolver undrawn |
| Reported change | `+$20.0966M` | `+$19.7825M` | `+$18.2313M` | Same named borrower/platform and maturity cluster |

## What the roll-forward proves

ASIF's public position in Frontline was larger at June 30, 2026 than at March
31, 2026, and the Q2 filing includes the same first-lien pricing, PIK, and
maturity markers. This is stronger than a single-period holder snapshot and
locates a material position change in the Q2 reporting window.

## What it does not prove

The change is not itself a cash-flow statement. Public Schedule of Investments
does not say whether the increase reflects a new draw, an incremental facility,
a secondary purchase, an assignment, PIK accretion, valuation movement, or a
borrower/entity-name transition. It also does not prove that ASIF participated
in the Ares-arranged Bain facility or that Frontline received the increase as
cash.

## Promotion test

Promote the roll-forward to a funding-event claim only if a source joins the
March-to-June change to an executed credit-agreement amendment, lender/agent
trade or assignment, settlement record, draw notice, or borrower funds-flow
schedule. Until then, the safe claim is:

`ASIF's publicly reported Frontline position increased between Q1 and Q2 2026, but the source-visible change is not classified as a borrower draw or cash receipt.`

## Decision

`asif-frontline-period-change-visible; funding-event-and-borrower-cash-open`

## Primary sources

[ASIF Q1 2026 supplement](https://www.sec.gov/Archives/edgar/data/1918712/000162828026034174/asifq1-2026nx14supplementn.htm)

[ASIF Q2 2026 supplement](https://www.sec.gov/Archives/edgar/data/1918712/000162828026054928/asifq2-202610qsupplement.htm)

