# Capital Flow FPL SPPCRC Amended Form 4P/5P Comparison Pass 1

## Purpose

This pass executes the follow-up from:

`/cluster/capital-flow-fpl-sppcrc-form-4p-5p-billing-base-extraction-pass-1.md`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-sppcrc-amended-form-4p-5p-comparison-pass-1.csv`

The question is:

`Did DN 03227-2026 change the FPL 2027 SPPCRC Form 4P/Form 5P billing-base and factor math, and what is now the current factor basis?`

## Short Answer

Yes.

DN `03227-2026` is now local and parsed. It amends the original DN `02560-2026` Form `4P`/Form `5P` support for the January-December `2027` SPPCRC factor period.

The filing letter states the reason: FPL identified an inadvertent formula error in load-factor calculations. The error affected retail separation factors and rate-class allocations, but did not change the total costs FPL sought to recover through the `2027` SPPCRC factors.

This pass compares `15` rows:

- `14` rate classes
- `1` total row

## Source Files

| Filing | Local Source | Role |
|---|---|---|
| DN `02560-2026` | `raw/primary-sources/capital-flow/power-grid-pilot/nextera/fpl-rate-case/current-sppcrc-2026/fpl-2026-sppcrc-epperson-factor-workpapers-02560-2026.pdf` | Original 2027 Form `4P`/Form `5P` factor support. |
| DN `03227-2026` | `raw/primary-sources/capital-flow/power-grid-pilot/nextera/fpl-rate-case/amended-factor-2026/fpl-2026-sppcrc-amended-form-4p-5p-03227-2026.pdf` | Corrected 2027 Form `4P`/Form `5P` factor support. |

## What Changed

The total projected SPPCRC cost pool did not change:

`1.104884879B USD`

The allocation across rate classes did change.

The biggest practical changes are in demand-billed classes:

| Rate Class | Original Factor | Corrected Factor | Direction |
|---|---:|---:|---|
| GSD1/GSDT1/HLFT1/GSD1-EV | `2.76 USD/kW` | `1.98 USD/kW` | Down |
| GSLD1/GSLDT1/CS1/CST1/HLFT2/GSLD-1EV | `2.49 USD/kW` | `1.98 USD/kW` | Down |
| GSLD2/GSLDT2/CS2/CST2/HLFT3/GSLD-2EV | `2.40 USD/kW` | `1.82 USD/kW` | Down |
| CILC D/CILC G | `2.37 USD/kW` | `1.83 USD/kW` | Down |
| MET | `3.26 USD/kW` | `2.37 USD/kW` | Down |

Several energy-billed classes changed upward or downward by smaller absolute amounts:

| Rate Class | Original Factor | Corrected Factor |
|---|---:|---:|
| RS1/RTR1/RS-2EV | `0.01084 USD/kWh` | `0.01088 USD/kWh` |
| GS1/GST1 | `0.01032 USD/kWh` | `0.01022 USD/kWh` |
| OS2 | `0.02239 USD/kWh` | `0.02879 USD/kWh` |
| OL1/SL1/SL1M/PL1/OSI/II | `0.00448 USD/kWh` | `0.00619 USD/kWh` |
| SL2/SL2M/GSCU1 | `0.01010 USD/kWh` | `0.01043 USD/kWh` |

## Reconciliation Notes

Corrected Form `5P` reconciles exactly:

`76.334573M USD + 1.028550306B USD = 1.104884879B USD`

The original Form `5P` class rows sum to `1.104884881B USD`, which is `2 USD` above the printed total. Treat this as an immaterial source-table/OCR/rounding tolerance.

The important economic point is not the `2 USD` tolerance. The important point is that the corrected filing keeps the total recovery pool unchanged while reallocating costs and factors among rate classes.

## Proof Upgrade

This pass upgrades FPL from:

`amended Form 4P/Form 5P support is source-visible but not local`

to:

`amended Form 4P/Form 5P source is local, parsed, and compared`

It also resolves the stale source-gap control from the prior Form `4P`/Form `5P` extraction.

## What This Still Does Not Prove

This is still not receipt proof.

It does not prove:

1. actual customer usage
2. actual billed dollars
3. actual collected customer cash
4. Distribution Inspection-specific receipts
5. category allocation from total SPPCRC to Distribution Inspection
6. source-of-funds allocation
7. regulatory subaccount cash
8. earned return

The corrected factors tell us how projected customer charges are calculated. They do not show that customers were actually billed or paid.

## Next Extraction

The next artifact should be:

`capital-flow-fpl-sppcrc-2027-factor-to-category-reconciliation-pass-1.md`

Now executed at:

`/cluster/capital-flow-fpl-sppcrc-2027-factor-to-category-reconciliation-pass-1.md`

It should test whether the corrected `2027` rate-class factor pool can be reconciled to:

| Target | Why It Matters |
|---|---|
| Form 2 projected clause revenue | Bridges factor math to projected aggregate revenue. |
| Form 4P/Form 5P corrected billing bases | Confirms the current customer-charge basis. |
| Distribution Inspection category recovery | Tests whether any category allocation support exists. |
| Actual/final true-up rows in later filings | Separates projection from billed/collected results. |

## Safe Claim

`FPL DN 03227-2026 corrects the 2027 SPPCRC Form 4P/Form 5P allocation and factor math. The corrected filing leaves the total projected recovery pool unchanged at 1.104884879B USD but changes rate-class allocations and several customer factors, especially demand-class factors. This is corrected projected billing-factor evidence, not actual billed revenue, collected customer cash, Distribution Inspection-specific receipts, source-of-funds allocation, or earned return.`

## Decision

`fpl-sppcrc-amended-form-4p-5p-comparison-ready-factor-to-category-reconciliation`
