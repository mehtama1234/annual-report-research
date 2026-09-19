# Apollo–Athene Corrected Same-CUSIP Row Confirmation

Research date: `2026-09-15`

## Purpose

Recheck the AMAPS and Concord named routes against the corrected, section-
reconciled Schedule D parser rather than relying only on the earlier positional
prototype.

## Evidence

| Route | Corrected holding row | Proceeds/disposal row | Row-level conclusion |
| --- | --- | --- | --- |
| AMAPS 1 LLC Tranche A Note, CUSIP `02300A-AA-8` | Page `6023`; book `$1,917,500,000`; interest income `$48,871,440`; maturity `07/31/2070` | Page `6276`; dated `10/24/2025`; Apollo Capital Markets Partner; consideration `$268,000,000`; interest/dividends `$3,986,842` | Corrected full-range holding fields and disposal fields agree with the same-CUSIP bridge |
| Concord Music Royalties LLC TUNES 2025-3A A, CUSIP `20633K-AN-8` | Page `6025`; book `$215,167,585`; fair value `$218,928,093`; interest income `$3,313,275`; maturity `07/20/2075` | Page `6334`; dated `07/01/2025`; Santander US Capital Markets L / AARE Surplus AAM; consideration `$229,053,398`; disposal book `$224,990,141`; interest/dividends `$4,733,250` | Corrected full-range holding fields and disposal fields agree with the same-CUSIP bridge |

## What this proves

The two named routes survive the corrected parser and can now be used as
row-level inputs to the next return-allocation join. The section-total
reconciliation makes the holding-side book and income fields materially more
reliable than the earlier sample-only output.

## Boundary

Same-CUSIP presence does not prove lot continuity, settlement receipt, trustee
remittance, borrower collateral cash, Athene subsidiary allocation, liability
funding cost, or Apollo common-owner cash. The consideration remains a
cash-like statutory candidate, not a settled receipt.

## Next test

Join the two rows to dated settlement/custodian records, disposal lot dates,
collateral remittance, liability-cost allocation, and parent receipt routes.
