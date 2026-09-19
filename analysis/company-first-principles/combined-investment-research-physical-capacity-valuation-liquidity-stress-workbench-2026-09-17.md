# Physical-capacity valuation and liquidity-stress workbench

Research date: `2026-09-17`

## Purpose

This workbench carries the physical-capacity comparison through the two
remaining end-to-end layers: Damodaran-style price-implied expectations and
Lyn Alden-style liquidity transmission. It uses stress mechanisms and required
fields rather than inventing intrinsic values from reported cash screens.

## Common valuation rule

For each lane:

`value = present value of source-backed common-owner cash after required reinvestment, funding, claims, and dilution`

The numerator cannot be populated from OCF, AFFO, FFO, backlog, facility
capacity, or resale proceeds alone. Those are diagnostic inputs until the
relevant project, collateral, or lifecycle object is source-backed.

## Stress transmission matrix

| Stress | URI fleet access | Equinix powered capacity | Digital Realty development |
|---|---|---|---|
| Higher rates / tighter credit | ABL interest, fleet funding, acquisition hurdle, and customer rental demand | Project debt, construction finance, JV/VIE funding, and lease-up hurdle | Development debt, ATM dependence, preferred/OP-unit burden, and cap-rate expansion |
| Inflation / labor and materials | Fleet purchase prices, maintenance, delivery labor, and resale values | Power, construction, equipment, and interconnection cost | Power, construction, equipment, and leasing cost |
| Demand delay | Lower utilization and slower rental starts; used-equipment inventory risk | Delayed energization, customer fit-out, and commencement | Delayed commencement, backlog conversion, and development-in-process aging |
| Liquidity reversal | Borrowing-base haircuts, reserves, and reduced used-equipment recovery | Parent/JV funding, commitments, and refinancing access | Equity dilution, private-capital reliance, and project funding availability |
| Accounting/QoE pressure | Resale gains, depreciation, capex classification, working capital | AFFO add-backs, recurring-capex definition, and VIE/JV presentation | FFO add-backs, development costs, acquisition accounting, and partner economics |

## Damodaran-style expectation fields

| Lane | Base-case numerator | Reinvestment field | Terminal/continuity field | Price-implied breaker |
|---|---|---|---|---|
| URI | Fleet rental cash after normalized replacement, maintenance, debt, tax, and claims | Replacement versus growth fleet capex plus working-capital and acquisition needs | Utilization, used-equipment recovery, fleet age, and borrowing-base durability | Required fleet return exceeds achievable rental spread after funding and resale stress |
| Equinix | Project/common-owner cash after power, recurring capex, lease-up, debt, JV/VIE, and dilution | Total project capital, recurring capital, leasing commissions, and partner funding | Commencement, stabilized yield, retention, and interconnection density | Implied growth requires project yield or lease-up that does not cover capital and funding claims |
| Digital Realty | Development/common-owner cash after power, lease-up, project debt, preferred/OP units, and dilution | Development capex, indirect capitalized costs, private capital, and recurring capex | Backlog conversion, commencement, stabilized NOI, and capital-market access | Implied growth requires backlog or FFO conversion without enough project return or common residual |

## Promotion status

| Required field | URI | Equinix | Digital Realty |
|---|---|---|---|
| Same-period operating cash | observed | observed | observed |
| Capital deployment | observed but replacement/growth unresolved | observed but project detail incomplete | observed with development component |
| Funding perimeter | facility proxy; certificate missing | debt/JV/VIE commitments partial | debt/ATM/private capital partial |
| Customer or project conversion | utilization/productivity partial | bookings/commencement partial | backlog/commencement partial |
| Common-owner numerator | missing | missing | missing |
| Valuation status | qualified expectation screen | qualified expectation screen | qualified expectation screen |
| Liquidity status | facility-availability proxy | funding-stress map | funding-stress map |

## Decision rules

1. A stress case may reduce a numerator or increase a capital claim, but it
   cannot create an observed return.
2. A higher reported non-GAAP metric does not clear a funding or dilution
   burden.
3. A financing facility is a source of optionality only after legal availability
   and collateral eligibility are proven.
4. Backlog and bookings enter a valuation case only after commencement,
   collection, project cost, and capital ownership are joined.
5. A thesis breaker requires a filing-based observation that changes the same
   entity's cash, claim, or funding mechanism—not a macro headline alone.

## Decision

The physical-capacity cohort is now `qualified-expectation-and-liquidity;
owner-cash-promotion-open; no-ranking`. The workbench completes the handoff
from force and control point through cash, valuation, and macro stress while
preserving the exact missing source objects for each company.

## Related records

- [Physical-capacity cash-conversion comparison](combined-investment-research-physical-capacity-cash-conversion-comparison-2026-09-17.md)
- [URI collateral-to-owner-cash promotion workbench](combined-investment-research-uri-collateral-to-owner-cash-promotion-workbench-2026-09-17.md)
- [Digital-infrastructure project-return workbench](combined-investment-research-digital-infrastructure-project-return-workbench-2026-09-17.md)
- [Industrial uptime valuation and macro handoff](combined-investment-research-industrial-uptime-valuation-macro-handoff-2026-09-17.md)

Structured workbench: [valuation/liquidity stress table](data/combined-investment-research-physical-capacity-valuation-liquidity-stress-workbench-2026-09-17.csv).
