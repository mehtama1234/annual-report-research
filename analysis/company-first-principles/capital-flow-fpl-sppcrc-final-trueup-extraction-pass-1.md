# Capital Flow FPL SPPCRC Final True-Up Extraction Pass 1

## Purpose

This page tests the next FPL cash-recovery question:

`Can FPL move from projected SPPCRC factor/true-up evidence to final true-up evidence for the same recovery period?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-sppcrc-final-trueup-extraction-pass-1.csv`

## Short Answer

Yes, partially.

The April 2026 FPL final true-up filing for Docket `20260010-EI` gives final 2025 SPPCRC recovery evidence. It changes the FPL chain from projected and actual/estimated recovery math into final true-up evidence for 2025.

The filing still does not prove full project return because it does not tie physical project output, financing source, realized earnings, and final customer-bill collection into one project/category row.

## Source Package

| Source | Local Path | Status |
|---|---|---|
| FPL 2025 SPPCRC final true-up testimony and Exhibit ALE-1, Document `01940-2026` | `raw/primary-sources/capital-flow/power-grid-pilot/nextera/fpl-rate-case/final-trueup-2025/fpl-2025-sppcrc-final-trueup-epperson-01940-2026.pdf` | fetched and extracted |
| FPL 2025 SPPCRC final true-up petition, Document `01960-2026` | `raw/primary-sources/capital-flow/power-grid-pilot/nextera/fpl-rate-case/final-trueup-2025/fpl-2025-sppcrc-final-trueup-petition-01960-2026.pdf` | fetched and checked |

## Extracted Evidence

| Family | Form | Period | Metric | Value |
|---|---|---|---|---:|
| final true-up | Direct testimony | 2025 final true-up | final net true-up over-recovery including interest | `16.579976M USD` |
| final true-up | Form 1A | 2025 final true-up | current-period over-recovery before interest | `10.068108M USD` |
| interest | Form 1A | 2025 final true-up | final interest provision | `-0.660146M USD` |
| true-up amount | Form 1A | 2025 final true-up | true-up amount to be refunded/recovered | `9.407962M USD` |
| clause revenue | Form 2A | 2025 final true-up | clause revenues net of revenue taxes | `804.620369M USD` |
| revenue requirement | Form 2A | 2025 final true-up | total jurisdictional revenue requirements | `729.233535M USD` |
| true-up collection | Form 2A | 2025 final true-up | true-up collected/refunded | `65.318726M USD` |
| category final recovery | Form 6A | 2025 final true-up | Distribution Feeder Hardening final amount | `335.693443M USD` |
| category final recovery | Form 6A | 2025 final true-up | Distribution Inspection final amount | `15.942971M USD` |
| category final recovery | Form 6A | 2025 final true-up | Transmission Inspection final amount | `23.595154M USD` |
| capital revenue requirement | Form 7A | 2025 final true-up | total jurisdictional capital investment revenue requirements | `600.314216M USD` |

## What Changed

The prior FPL pages proved:

- program/category recovery rows
- projected 2026 customer-factor math
- 2025 actual/estimated true-up math
- WACC and pre-tax carrying-charge inputs

This pass adds final 2025 true-up evidence. The same period that had an actual/estimated under-recovery of `7.172014M USD` is later filed as a final net over-recovery of `16.579976M USD` including interest.

That matters because it proves the recovery mechanism is not merely projected. It has a formal final true-up cycle.

## Workbench Upgrade

| Gate | Status After This Pass | Reason |
|---|---|---|
| CFPGW-005 customer cash recovery | pass-bridge | The workbench already had projected 2026 rate-class factors; the final true-up filing confirms the mechanism cycles into later factor calculations. |
| CFPGW-007 realized earnings/cash | partial | Final clause revenue and true-up evidence are visible, but earnings, project cash, customer receipts, and financing source are still not reconciled. |
| CFPGW-008 full pass decision | partial | FPL is the strongest regulated recovery bridge, but still below full project-return proof. |

## Safe Claim

`FPL's SPPCRC evidence now reaches final true-up status for the 2025 recovery period. The record shows final clause revenues, jurisdictional revenue requirements, true-up amounts, category final recovery rows, and capital revenue requirements. It still does not prove project-level IRR, financing source, physical output, or realized earnings.`

## Next Proof

| Need | Source Route |
|---|---|
| approval of the final 2025 true-up | PSC order in Docket `20260010-EI` after the April 2026 petition |
| approval of 2026 SPPCRC factors | extracted in `/cluster/capital-flow-fpl-sppcrc-factor-order-extraction-pass-1.md` |
| final tariff factors | order-level approval extracted; separately stamped tariff sheets or amended factors remain optional next proof |
| physical output | extracted in `/cluster/capital-flow-fpl-sppcrc-project-detail-extraction-pass-1.md` |
| earnings/cash conversion | FPL/FPSC clause true-up, segment earnings, AFUDC, depreciation, taxes, and cash-flow disclosures |

## Decision

`fpl-final-trueup-visible - FPL now has final true-up recovery evidence; later passes add final factor-order and physical-output bridge evidence, while financing source, customer receipts, and earnings/cash conversion remain unreconciled.`
