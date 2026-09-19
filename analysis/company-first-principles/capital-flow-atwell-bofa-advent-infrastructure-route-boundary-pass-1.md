# Capital Flow Atwell BofA/Advent Infrastructure Route Boundary Pass 1

Research date: `2026-09-17`

## Purpose

This pass records an adjacent infrastructure-services route discovered while
testing the Ares/Frontline borrower lane. It is deliberately separate from
Ares: the local evidence identifies Advent as the equity investor and Bank of
America as the lead on the credit facility.

The route is:

`Advent investment + BofA-led credit facility -> Atwell -> engineering,
consulting and construction services -> infrastructure project capacity`

## Evidence surface

| Link | Evidence | Status | Boundary |
|---|---|---|---|
| Operating destination | Advent's March 27, 2026 announcement describes Atwell as an engineering, consulting, and construction-services provider serving power, energy, community-development, commercial, and digital-infrastructure markets. | `operating-destination-visible` | Operating description does not prove revenue, margin, backlog conversion, or owner cash. |
| Equity router | The same official announcement says Advent agreed, in partnership with management, to make a significant investment in Atwell. | `equity-investment-role-visible` | Amount, ownership percentage, purchase consideration, and funds-flow are not disclosed. |
| Intended use | Advent says the investment is intended to support talent, technology, geographic reach, service capabilities, corporate services, digital platforms, and operational infrastructure. | `directional-use-visible` | These are stated objectives, not a populated use-of-proceeds or project-return ledger. |
| Credit facility | An Atwell announcement carried by Business Wire reports a `$200M` senior credit facility led by Bank of America, with U.S. Bank, TD Bank, and Old National Bank also in the lending group. | `facility-size-and-bank-role-visible` | The announcement says terms were not disclosed; draw date, tranche split, collateral, borrower legal entity, and lender allocation remain open. |
| Borrower cash | No local source provides Atwell revenue, EBITDA, free cash flow, debt service, facility draw, or repayment. | `cash-waterfall-hold` | The route cannot be promoted to borrower cash realization or lender return. |

## QoE and financial-integrity controls

- Do not call Advent's investment a debt source.
- Do not call the reported `$200M` facility funded principal without a draw or
  closing record.
- Do not attribute the BofA-led facility to Ares/Frontline.
- Do not treat stated growth objectives as paid capex, acquired backlog, or
  project cash return.
- Do not calculate owner cash from a facility amount without borrower
  financials, interest, taxes, working capital, maintenance investment, and
  repayment claims.

These controls identify missing reconciliation objects; they are not
allegations of manipulation.

## Decision

`atwell-operating-destination-and-funding-route-visible; cash-and-return-open`

Atwell is a useful separate infrastructure-services case because it links a
named sponsor, a named bank-led facility, and a real operating control point.
It must remain outside the Ares/Frontline lender-allocation test until a credit
agreement, funds-flow, borrower financial package, and repayment record are
found.

## Sources

- [Advent Atwell investment announcement](https://www.adventinternational.com/news/atwell-partners-with-advent-international-to-accelerate-next-phase-of-growth/)
- [Preserved Advent announcement](../../raw/primary-sources/capital-flow/ares/q2-2026/follow-through/atwell-advent-2026-investment.html)
- [Atwell announcement carried by Business Wire](https://www.businesswire.com/news/home/20240125865095/en/)
- [Preserved BofA/Atwell facility record](../../raw/primary-sources/capital-flow/ares/q2-2026/follow-through/atwell-2024-bank-of-america-credit-facility-abf-journal.html)
