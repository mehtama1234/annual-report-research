# Capital Flow FPL SPPCRC Factor Order Extraction Pass 1

## Purpose

This page answers the order-level customer-charge question:

`Did the Florida PSC approve FPL's 2026 SPPCRC factors and tariff authority, or did the work only have projected factor math?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-sppcrc-factor-order-extraction-pass-1.csv`

## Short Answer

Yes.

Order `PSC-2025-0439-FOF-EI`, issued November 24, 2025, approves storm cost recovery amounts and related tariffs and establishes storm cost recovery factors for January 2026 through December 2026. This moves the FPL SPPCRC chain beyond projected Form 5P math into final order-level factor authorization.

It still does not prove customer receipts, category earnings, financing source, or project IRR.

## Source Package

| Source | Local Path | Status |
|---|---|---|
| Florida PSC Order `PSC-2025-0439-FOF-EI`, Document `15236-2025` | `raw/primary-sources/capital-flow/power-grid-pilot/nextera/fpl-rate-case/factor-order-2026/fpl-2026-sppcrc-factor-order-psc-2025-0439.pdf` | fetched and extracted |

Official source URL:

`https://www.floridapsc.com/pscfiles/library/filings/2025/15236-2025/15236-2025.pdf`

## Extracted Evidence

| Family | Period | Metric | Value |
|---|---|---|---:|
| order identity | November 24 2025 | Order `PSC-2025-0439-FOF-EI` | `2025-0439` |
| order scope | January 2026 through December 2026 | storm cost recovery amounts, related tariffs, and factors approved | `2026` |
| approved cost recovery | 2026 projection | settlement-approved scenario including true-up | `984.084441M USD` |
| approved cost recovery | 2026 projection | settlement-declined scenario including true-up | `858.030231M USD` |
| rate-class factor | 2026 | RS1/RTR1 | `0.00868 USD/kWh` |
| rate-class factor | 2026 | GS1/GST1 | `0.00805 USD/kWh` |
| rate-class factor | 2026 | GSD1/GSDT1/HLFT1/GSD1-EV | `1.57 USD/kW` |
| rate-class factor | 2026 | GSLD1/GSLDT1/CS1/CST1/HLFT2/GSLD1-EV | `1.58 USD/kW` |
| rate-class factor | 2026 | GSLD2/GSLDT2/CS2/CST2/HLFT3 | `1.46 USD/kW` |
| rate-class factor | 2026 | MET | `1.89 USD/kW` |
| rate-class factor | 2026 | OL1/SL1/SL1M/PL1/OSI/II | `0.00278 USD/kWh` |
| rate-class factor | 2026 | SL2/SL2M/GSCU1 | `0.02290 USD/kWh` |
| effective billing period | January 2026 through December 2026 | first January billing cycle through last December billing cycle | `12 months` |
| tariff authorization | January 2026 through December 2026 | revised tariffs approved and utilities authorized to apply factors | `2026` |

## What Changed

Before this pass, the FPL customer-cash bridge had projected factor math from Form 5P and true-up evidence, but the workbench still listed the final factor/tariff order as a source gap.

This pass closes the order-level part of that gap. The remaining limitation is narrower: separate stamped tariff sheets and actual customer receipts are still not extracted.

## Workbench Upgrade

| Gate | Status After This Pass | Reason |
|---|---|---|
| CFPGW-003 regulatory authority | pass-bridge | The order directly approves the SPPCRC factor/recovery package for the 2026 period. |
| CFPGW-005 customer cash recovery | pass-bridge | Final rate-class factors, effective billing period, and tariff authorization are now extracted. |
| CFPGW-008 full pass decision | partial | Order-level factor approval is visible, but customer receipts, financing source, earnings, and project-level return are not reconciled. |

## Safe Claim

`FPL's 2026 SPPCRC customer-charge bridge is final-factor-order visible: the Florida PSC approved storm cost recovery amounts, related tariffs, and storm cost recovery factors for January 2026 through December 2026. This is not proof of realized collections, financing source, earned return, or project-level IRR.`

## Decision

`fpl-final-factor-order-visible - the final factor/tariff authorization gap is closed at the order level, while separate tariff sheets and actual collection evidence remain open.`
