# Capital Flow FPL SPPCRC Form 4P/5P Billing-Base Extraction Pass 1

## Purpose

This pass executes the next concrete extraction from:

`/cluster/capital-flow-fpl-sppcrc-docket-billing-workpaper-map-pass-1.md`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-sppcrc-form-4p-5p-billing-base-extraction-pass-1.csv`

The question is:

`Can FPL's Form 4P and Form 5P convert SPPCRC factor authority into rate-class billing-base evidence?`

## Short Answer

Yes, with a strict boundary.

The local `fpl-2025-sppcrc-actual-estimated-projection.pdf` exposes a field-level Form `4P` and Form `5P` table for January-December `2026`.

This pass extracts `16` rows:

- `14` rate-class rows
- `1` total row
- `1` amended-filing control row

The extraction shows projected sales at meter, projected demand, load expansion, allocation percentages, demand/customer-related costs, energy-related costs, total SPPCRC cost by class, billed kW where applicable, and SPP factors.

It still does not prove actual billed revenue or collected customer cash.

In other words, this is not actual billed revenue or collected customer cash.

## What The Forms Do

| Form | What It Adds | Proof Boundary |
|---|---|---|
| Form `4P` | Calculates energy and demand allocation percentages by rate class using projected sales, demand, load factors, and loss expansion. | It is a projected allocation base, not actual billing or cash. |
| Form `5P` | Applies the allocation to demand/customer-related costs and energy-related costs, then derives SPPCRC factors by rate class. | It is factor/billing-base evidence, not actual customer receipts. |

## Extracted Totals

| Metric | Extracted Value |
|---|---:|
| Projected sales at meter | `128,430,086,092 kWh` |
| Projected avg 12 CP at meter | `21,852,220 kW` |
| Projected GCP at meter | `26,958,673 kW` |
| Projected avg 12 CP at generation | `23,510,678 kW` |
| Projected GCP at generation | `29,002,231 kW` |
| Demand/customer-related costs | `61.506076M USD` |
| Energy-related costs | `797.738317M USD` |
| Total SPPCRC projected cost pool | `859.244393M USD` |

The cost-dollar columns reconcile exactly across the rate-class rows:

`61.506076M USD + 797.738317M USD = 859.244393M USD`

The whole-number sales and demand printed totals have immaterial `1-2` unit differences versus summed extracted rate rows. Treat those as printed-table/OCR reconciliation tolerances, not economic differences.

## Largest Rate-Class Rows

| Rate Class | Projected Sales | Total SPPCRC Cost | SPP Factor |
|---|---:|---:|---:|
| RS1/RTR1 | `70.148782113B kWh` | `609.445183M USD` | `0.00869 USD/kWh` |
| GSD1/GSDT1/HLFT1/GSD1-EV | `29.307306672B kWh` | `120.643701M USD` | `1.58 USD/kW` |
| GS1/GST1 | `8.456898435B kWh` | `68.195641M USD` | `0.00806 USD/kWh` |
| GSLD1/GSLDT1/CS1/CST1/HLFT2/GSLD1-EV | `10.809337393B kWh` | `37.329588M USD` | `1.58 USD/kW` |

## What This Proves

This pass proves:

1. Form `4P` supplies rate-class projected sales and demand allocation fields.
2. Form `5P` supplies rate-class projected SPPCRC cost allocations.
3. Form `5P` produces customer-facing factor math by rate class.
4. The projected SPPCRC factor cost pool totals `859.244393M USD`.
5. Demand classes have billed-kW fields and dollar-per-kW factors.
6. Energy classes have dollar-per-kWh factors.

## What This Still Does Not Prove

This pass does not prove:

1. actual customer usage
2. actual billed dollars
3. actual collected customer cash
4. Distribution Inspection-specific receipts
5. category allocation from total SPPCRC into Distribution Inspection
6. source-of-funds allocation
7. regulatory subaccount cash
8. earned return

The extraction upgrades the chain from:

`factor authority visible`

to:

`projected billing-base and factor math visible`

It does not upgrade the chain to:

`customer cash received`

## Amended Filing Control

The FPL docket/workpaper map identifies DN `03227-2026` as amended ALE-3/ALE-4 Form `4P`/Form `5P` support.

That amended PDF is not present in the current local raw source packet.

This pass therefore includes a control row:

`CFPL45P-016`

Status:

`fetched-and-compared-followup`

The amended filing has now been fetched and compared here:

`/cluster/capital-flow-fpl-sppcrc-amended-form-4p-5p-comparison-pass-1.md`

Use this pass as the `2026` projection baseline. Use the amended comparison pass as the current `2027` corrected factor basis.

## Next Extraction

The next artifact should be:

`capital-flow-fpl-sppcrc-amended-form-4p-5p-comparison-pass-1.md`

It should fetch or locate DN `03227-2026`, then compare:

| Field | Why |
|---|---|
| rate class | Confirms row alignment. |
| projected sales at meter | Tests whether billing bases changed. |
| projected billed kW | Tests whether demand bases changed. |
| SPP factor | Tests whether customer charge changed. |
| demand/customer-related cost | Tests demand allocation change. |
| energy-related cost | Tests energy allocation change. |
| total cost by class | Tests reconciliation to the amended recovery pool. |

## Safe Claim

`FPL Form 4P and Form 5P provide projected rate-class billing-base and factor math for the 2026 SPPCRC. The local extraction shows 128.430086092B kWh of projected sales at meter and an 859.244393M USD projected SPPCRC cost pool allocated across 14 rate classes. This is billing-base proxy evidence, not actual billed revenue, collected customer cash, Distribution Inspection-specific receipts, source-of-funds allocation, or earned return.`

## Decision

`fpl-sppcrc-form-4p-5p-billing-base-extraction-ready-amended-comparison`
