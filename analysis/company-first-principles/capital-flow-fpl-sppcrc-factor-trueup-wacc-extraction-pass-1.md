# Capital Flow FPL SPPCRC Factor/True-Up/WACC Extraction Pass 1

## Purpose

This page takes the next FPL question after category recovery:

`Can the SPPCRC filing connect category-level recovery evidence to customer-charge factors, true-up mechanics, and carrying-charge inputs?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-sppcrc-factor-trueup-wacc-extraction-pass-1.csv`

## Short Answer

Yes, as bridge evidence.

The same FPL SPPCRC filing includes:

- 2025 actual/estimated true-up rows
- clause revenue and jurisdictional revenue-requirement rows
- 2026 projected cost-recovery factors by rate class
- retail separation factors
- WACC and pre-tax weighted-cost inputs

This improves the FPL chain from category-recovery-visible to customer-factor/carrying-charge-visible. It still does not prove actual customer cash collected, category earnings, financing source, or project-level IRR.

## Extracted Evidence

| Family | Form | Period | Metric | Value |
|---|---|---|---|---:|
| true-up | Testimony / Form 1E | 2025 actual/estimated | current-period under-recovery before interest | `6.200197M USD` |
| true-up | Testimony / Form 1E | 2025 actual/estimated | interest provision | `0.971817M USD` |
| true-up | Testimony / Form 1E | 2025 actual/estimated | total under-recovery including interest | `7.172014M USD` |
| clause revenue | Form 2E | 2025 actual/estimated | clause revenues net of revenue taxes | `792.990494M USD` |
| revenue requirement | Form 2E | 2025 actual/estimated | total jurisdictional revenue requirements | `733.871964M USD` |
| true-up | Form 2E | 2025 actual/estimated | true-up collected or refunded | `65.318726M USD` |
| cost recovery factor | Form 5P | 2026 projection | RS1/RTR1 SPP factor | `0.00869 USD/kWh` |
| cost recovery factor | Form 5P | 2026 projection | GS1/GST1 SPP factor | `0.00806 USD/kWh` |
| cost recovery factor | Form 5P | 2026 projection | GSD1/GSDT1 demand SPP factor | `1.58 USD/kW` |
| cost recovery factor | Form 5P | 2026 projection | total SPPCRC cost by rate class | `859.244393M USD` |
| carrying charge | Form 8E | 2025 Jan-Feb | WACC total weighted cost | `7.0210%` |
| carrying charge | Form 8E | 2025 Mar-Dec | WACC total weighted cost | `7.0347%` |
| carrying charge | Form 7P | 2026 projection | WACC total weighted cost | `7.0891%` |
| carrying charge | Form 7P | 2026 projection | pre-tax total weighted cost | `8.9464%` |
| separation factor | Exhibit RLH-4 | 2026 forecast | transmission demand retail separation factor | `0.884813` |
| separation factor | Exhibit RLH-4 | 2026 forecast | distribution demand retail separation factor | `1.000000` |

## Workbench Upgrade

This extraction improves two FPL gates:

| Gate | Prior Status | New Status | Reason |
|---|---|---|---|
| CFPGW-004 allowed return input | pass-bridge | pass-bridge | WACC and pre-tax weighted-cost inputs are now directly extracted from Forms 8E and 7P. |
| CFPGW-005 customer cash recovery | partial | pass-bridge | Form 5P exposes projected 2026 SPPCRC cost-recovery factors by rate class and reconciles them to the `859.244393M USD` total cost pool. |
| CFPGW-007 realized earnings/cash | partial | partial | Clause revenues and true-up mechanics are visible, but final collections and category earnings are still not proven. |

## Current Answer

`FPL now has a regulated recovery chain that reaches category rows, WACC/carrying-charge inputs, rate-class factor mechanics, and true-up math. That is strong customer-charge bridge evidence, but it remains below realized-return proof because final collections, earnings, financing source, and physical project output are not yet tied to one category.`

## Remaining Open Questions

| Question | Why It Matters | Next Source |
|---|---|---|
| Were the projected 2026 factors approved exactly as filed? | Filed factors are stronger than no factor, but final tariff/factor approval is the true cash-collection gate. | PSC order approving SPPCRC factors and final tariff sheets. |
| What physical work produced the recovery dollars? | Return proof needs the asset/output denominator, not just recovery math. | Storm-protection program progress reports, hardening miles, inspections, substation mitigation tables, and construction status schedules. |
| What was actually collected and trued up later? | True-up filings turn projected factors into realized recovery evidence. | 2026 actual/estimated and final true-up filings submitted after the recovery period. |
| What financing source funded the category capital? | Capital source-to-use is still separate from cost recovery. | FPL debt/equity issuance disclosures, CWIP/rate-base schedules, and utility capex funding notes. |

## Decision

`fpl-customer-factor-carrying-charge-visible - SPPCRC factor, true-up, and WACC rows improve the FPL bridge, but realized project-return proof remains open.`
