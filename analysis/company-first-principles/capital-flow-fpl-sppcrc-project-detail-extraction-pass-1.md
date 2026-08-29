# Capital Flow FPL SPPCRC Project Detail Extraction Pass 1

## Purpose

This page answers the physical-output question:

`Can the FPL SPPCRC recovery bridge be tied to same-period storm-protection work actually completed, not only dollars and factor math?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-sppcrc-project-detail-extraction-pass-1.csv`

## Short Answer

Yes, at program-output level.

The Pankratz testimony and Exhibits AP-1/AP-2 for Docket `20260010-EI` provide final actual 2025 SPP project/cost evidence, physical output summaries for inspection and vegetation programs, and variance-driver categories.

This upgrades FPL from recovery/factor/final-true-up evidence into a stronger regulated recovery bridge with physical output. It still does not prove project-level IRR, financing source, customer receipts, or realized earnings.

## Source Package

| Source | Local Path | Status |
|---|---|---|
| FPL Andrew Pankratz direct testimony with Exhibits AP-1 and AP-2, Document `01941-2026` | `raw/primary-sources/capital-flow/power-grid-pilot/nextera/fpl-rate-case/project-detail-2025/fpl-2025-sppcrc-final-trueup-pankratz-ap1-ap2-01941-2026.pdf` | fetched and extracted |

Official source URL:

`https://www.floridapsc.com/pscfiles/library/filings/2026/01941-2026/01941-2026.pdf`

## Extracted Evidence

| Family | Metric | Value |
|---|---|---:|
| service footprint | customer accounts served | `6.000000M` |
| service footprint | distribution line miles | `83000 miles` |
| service footprint | distribution poles | `1400000` |
| service footprint | high-voltage transmission line miles | `9700 miles` |
| service footprint | transmission structures | `85000` |
| service footprint | substations | `932` |
| source purpose | final actual SPP projects and costs presented | `2025` |
| selection criteria | Commission-approved prioritization criteria applied | `2023 SPP` |
| Distribution Inspection | actual project count | `193199` |
| Distribution Inspection | actual capital costs | `61.500000M USD` |
| Transmission Inspection | actual project count | `84056` |
| Transmission Inspection | actual capital costs | `66.300000M USD` |
| Distribution Vegetation Management | actual miles | `18597 miles` |
| Distribution Vegetation Management | actual costs | `108.700000M USD` |
| Transmission Vegetation Management | actual miles | `9610 miles` |
| Transmission Vegetation Management | actual costs | `17.600000M USD` |
| variance control | variance categories identified | `3` |
| prudence assertion | final actual SPP costs reasonable and prudent | `2025` |

## What Changed

The earlier FPL pages proved:

- category recovery rows
- projected and final true-up math
- WACC/carrying-charge inputs
- final factor-order authorization

This pass adds the missing physical-output bridge. FPL now has same-period 2025 program-output rows for inspection project counts and vegetation miles, plus AP-2 variance categories that explain why projects or costs move between actual/estimated and final actual filings.

## Workbench Upgrade

| Gate | Status After This Pass | Reason |
|---|---|---|
| CFPGW-006 operating output | pass-bridge | AP-1 gives same-period physical output for Distribution Inspection, Transmission Inspection, and vegetation management. |
| CFPGW-007 realized earnings/cash | partial | Same-period costs and output are visible, but earnings, receipts, financing source, depreciation, taxes, and cash conversion are still not reconciled. |
| CFPGW-008 full pass decision | partial | The chain now includes physical output, but not full project-return economics. |

## Safe Claim

`FPL's SPPCRC evidence now includes 2025 program-output proof: AP-1 lists final actual inspection project counts, vegetation miles, and actual costs, while AP-2 supplies variance-driver categories. This supports a stronger regulated recovery bridge, not project-level return proof.`

## Decision

`fpl-physical-output-bridge-visible - the physical-output gap is closed at program-summary level, while earnings, cash receipts, financing source, and project-level return remain open.`
