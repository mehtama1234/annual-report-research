# Capital Flow CFNSAQ-004 Statutory/Facility/Collateral Pass 1

## Purpose

This page executes the fourth row of the next-source acquisition queue.

It asks:

`Can current local sources prove statutory legal-entity holdings, borrower facility cash paths, lender schedules, or collateral availability for the insurance, private-credit, reserve-backed, receivables-backed, and pledged-share cases?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-cfnsaq-004-statutory-facility-collateral-pass-1.csv`

The queue input is:

`/cluster/capital-flow-next-source-acquisition-queue-pass-1.md`

## Short Answer

`CFNSAQ-004 is executed against the current local source set. It finds four partial facility or collateral mechanics rows: Ares/Frontline, Matador, United Rentals, and Liberty Broadband. Apollo/Athene, KKR/Global Atlantic, and Blackstone remain holds. No row reaches full statutory legal-entity, borrower facility, lender allocation, or collateral availability proof.`

## Execution Result

| Row | Target Case | Current Evidence | Result | What Still Blocks Proof |
|---|---|---|---|---|
| `CFNSAQ004-001` | Apollo/Athene | Q2 `2026` gross inflows of `22.069B USD`, Athene-attributable inflows of `17.095B USD`, net flows of `11.928B USD`, gross invested assets of `413.598B USD`, and spread-related earnings of `877M USD` | `hold-no-athene-statutory-asset-income-schedule` | Athene statutory statements, Schedule D/BA, statutory investment-income exhibit, realized gain/loss, impairments, NAIC designations, liability-cost spread |
| `CFNSAQ004-002` | KKR / Global Atlantic | Global Atlantic AUM of `220B USD`, credit AUM of `164B USD`, insurance investments of `189.204380B USD`, policy liabilities of `205.499130B USD`, and FHLB pledged assets of `9.2B USD` | `hold-no-global-atlantic-statutory-or-borrower-schedule` | Statutory legal-entity holdings, Schedule D/BA, NAIC schedules, pledged-asset eligibility, FHLB haircut/advance-rate file, borrower/facility schedule |
| `CFNSAQ004-003` | Ares / Frontline | Frontline Road Safety borrower context, Bain sponsor transaction, Ares arranger/bookrunner role, and holder-dollar proxy | `partial-borrower-facility-marker-holder-dollar-proxy` | Facility size, Ares funded allocation, lender group, use-of-proceeds funds-flow, borrower financials, repayment schedule, covenants |
| `CFNSAQ004-004` | Blackstone credit channel | Q2 `2026` Credit & Insurance AUM of `469.3B USD`, fee-earning AUM of `318.241B USD`, quarterly inflows of `31.0B USD`, LTM inflows of `143.0B USD`, and direct-lending inflows of `13.3B USD` | `hold-no-vehicle-to-borrower-facility-allocation` | Vehicle-to-borrower allocation, lender schedule, funded tranche share, use of proceeds, borrower cash, collateral file, repayment schedule |
| `CFNSAQ004-005` | Matador borrowing base | `3.250B USD` borrowing base, `2.750B USD` elected commitments, `939.000M USD` borrowings, `53.800M USD` letters of credit, and `1.180B USD` post-quarter borrowings | `partial-bank-facility-and-borrowing-base-proxy` | Lender commitment allocation, borrowing notices, borrowing-base certificate, reserve/collateral valuation, covenant certificate, acquisition cash allocation |
| `CFNSAQ004-006` | United Rentals fleet | AR collateral coverage of `125.8%`, actual SEC receivables amendment retrieved, A/R facility expiration of `2027-06-18`, Purchase Limit of `1.500B USD`, and derived bank commitment sum of `1.500B USD` | `partial-agreement-document-with-availability-hold` | Borrowing-base certificate, eligible-collateral schedule, advance rates, reserves, L/C treatment, concentration test, legal availability |
| `CFNSAQ004-007` | Liberty Broadband holdco | `19.1M` Charter shares in collateral accounts, `2.7B USD` collateral-account value, `864M USD` margin loan, `1.150B USD` term loan facility, and `359M USD` Charter Loan Facility outstanding | `partial-pledged-share-ltv-mechanics-proxy` | LTV certificate, collateral haircut, margin-loan definitions, restricted-cash split, Charter loan terms, merger funds-flow, tax allocation |

## What This Answers

This pass tests whether balance-sheet or collateral language becomes legal availability proof:

- Apollo/Athene and KKR/Global Atlantic remain below statutory legal-entity proof.
- Blackstone remains below vehicle-to-borrower allocation proof.
- Ares has a borrower/facility marker, but not facility cash-path proof.
- Matador has reserve-backed facility mechanics, but not certificate-level availability or lender allocation.
- United Rentals has agreement and bank commitment evidence, but not legal availability schedules.
- Liberty has pledged-share/LTV mechanics, but not contractual certificate and exact source split.

## Decision

`cfnsaq-004-executed-current-local-mixed-partial-hold`

The queue row is executed against current local evidence. It improves facility and collateral mechanics for selected rows, but it does not close full legal-entity, borrower-facility, or collateral availability proof.

## Safe Claim

`The current local source set shows partial facility or collateral mechanics for Ares/Frontline, Matador, United Rentals, and Liberty Broadband. Apollo/Athene, KKR/Global Atlantic, and Blackstone remain holds. No CFNSAQ-004 row proves statutory legal-entity holdings, borrower use-of-proceeds cash paths, or certificate-level collateral availability.`

## Next Work

1. Move to `CFNSAQ-005` for return model support: IRR, NPV, ROIC, reserve life, and earned return.
2. Preserve statutory/facility/collateral holds unless legal-entity schedules, borrower credit agreements, lender allocation schedules, borrowing-base certificates, LTV certificates, or collateral eligibility files are acquired.
