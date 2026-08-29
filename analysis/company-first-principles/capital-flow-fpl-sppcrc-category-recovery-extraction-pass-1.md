# Capital Flow FPL SPPCRC Category Recovery Extraction Pass 1

## Purpose

This page answers the next project-return workbench question for FPL:

`Can FPL move from recovery-framework-visible to category-recovery-table-visible?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-sppcrc-category-recovery-extraction-pass-1.csv`

## Short Answer

Yes, partially.

The FPL Storm Protection Plan Cost Recovery Clause filing exposes category-level recovery evidence. It does not just say FPL has a regulated recovery framework; it gives named program categories, actual/estimated dollars, projected dollars, expenditures, additions to plant, and recoverable expense rows.

This upgrades the FPL workbench from framework evidence toward category-level capital/recovery evidence, but it still does not prove full project return.

## Extracted Evidence

| Category | Form | Period | Metric | Value | Workbench Gate |
|---|---|---|---|---:|---|
| Distribution Feeder Hardening | Form 6E | 2025 actual/estimated | annual capital investment cost / jurisdictional revenue requirement | `334.058644M USD` | CFPGW-001 |
| Distribution Feeder Hardening | Form 6E | 2025 projection | projected annual capital investment cost / jurisdictional revenue requirement | `317.412173M USD` | CFPGW-001 |
| Overhead Hardening Capital Investment Programs | Form 6E | 2025 actual/estimated | subtotal annual capital investment cost / jurisdictional revenue requirement | `397.926574M USD` | CFPGW-001 |
| Distribution Inspection | Form 7E | 2025 actual/estimated | expenditures | `38.500000M USD` | CFPGW-002 |
| Distribution Inspection | Form 7E | 2025 actual/estimated | additions to plant | `58.131189M USD` | CFPGW-002 |
| Distribution Inspection | Form 7E | 2025 actual/estimated | total system recoverable expenses | `16.835584M USD` | CFPGW-007 |
| Transmission Inspection | Form 7E | 2025 actual/estimated | expenditures | `48.373799M USD` | CFPGW-002 |
| Transmission Inspection | Form 7E | 2025 actual/estimated | additions to plant | `54.672380M USD` | CFPGW-002 |
| Transmission Inspection | Form 7E | 2025 actual/estimated | total system recoverable expenses | `22.954303M USD` | CFPGW-007 |
| Distribution Inspection | Form 3P | 2026 projection | expenditures | `45.400000M USD` | CFPGW-002 |
| Distribution Inspection | Form 3P | 2026 projection | additions to plant | `44.634260M USD` | CFPGW-002 |
| Distribution Inspection | Form 3P | 2026 projection | total system recoverable expenses | `21.638259M USD` | CFPGW-007 |
| Transmission Inspection | Form 3P | 2026 projection | expenditures | `49.524332M USD` | CFPGW-002 |
| Transmission Inspection | Form 3P | 2026 projection | additions to plant | `50.304709M USD` | CFPGW-002 |
| Transmission Inspection | Form 3P | 2026 projection | total system recoverable expenses | `28.255747M USD` | CFPGW-007 |
| Distribution Vegetation Management | Form 2P | 2026 projection | O&M program total | `116.592072M USD` | CFPGW-005 |
| Transmission Vegetation Management | Form 2P | 2026 projection | jurisdictional O&M amount | `14.911735M USD` | CFPGW-005 |

## Workbench Upgrade

This extraction changes the FPL decision layer:

| Gate | Prior Status | New Status | Reason |
|---|---|---|---|
| CFPGW-001 capital category selected | partial | pass-bridge | SPPCRC program categories are now named and quantified. |
| CFPGW-002 capital use amount | partial | pass-bridge | Forms 7E and 3P expose expenditures and additions to plant by inspection category. |
| CFPGW-005 customer cash recovery | partial | partial | O&M and revenue-requirement rows are visible, but tariff factors and collections are not. |
| CFPGW-007 realized earnings/cash | missing | partial | Recoverable expenses are visible by category, but realized collected revenue and earnings are still absent. |
| CFPGW-008 full pass decision | partial | partial | The FPL chain is stronger but still below full project-return-grade proof. |

## What This Answers

`FPL has category-level regulated recovery evidence for storm-protection programs. The filing names categories and exposes projected and actual/estimated capital-use and recoverable-expense rows. This is stronger than a recovery-framework claim because the dollars can be tested by program category.`

## What It Does Not Answer

Do not use this page to claim:

- FPL has full project-level IRR proof
- the SPPCRC revenue requirement equals realized cash collected from customers
- every FPL capital item is recoverable on the same terms
- category recoverable expenses equal shareholder earnings
- the filing proves the financing source for each project

## Next Proof

The next step is a same-category cash schedule:

| Need | Source Route |
|---|---|
| customer-class rates or clause factors | PSC tariff sheets, SPPCRC factor orders, and revised tariff filings |
| actual recovery / true-up | later SPPCRC true-up forms and FPL earnings or clause filings |
| allowed return inside category calculation | SPPCRC WACC/capital-structure forms and MFR schedules |
| physical output | storm-hardening miles/assets, inspection units, substations, or feeder-level program tables |
| financing source | FPL debt/equity issuance notes, construction work in progress, and utility capex financing disclosures |

## Decision

`fpl-sppcrc-category-recovery-visible - FPL now has category-level capital-use and recoverable-expense evidence, but not realized project-return proof.`
