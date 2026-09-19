# Apollo–Athene Same-CUSIP Lot Chronology Boundary

Research date: `2026-09-15`

## Purpose

Test whether same-CUSIP presence is enough to establish lot continuity between
the corrected Schedule D holding row and a dated disposal/proceeds row.

## Evidence

| Route | Holding-side acquired date | Disposal/proceeds date | Result |
| --- | --- | --- | --- |
| AMAPS `02300A-AA-8` | `07/31/2025` | `10/24/2025` | Chronology is possible, but no lot identifier or settlement record is present |
| Concord `20633K-AN-8` | `10/29/2025` | `07/01/2025` | Holding-side acquisition follows the disposal/proceeds date; same-CUSIP equality cannot establish lot continuity |

## Conclusion

The corrected parser strengthens the row fields but does not convert an
identifier match into a settled cash loop. The Concord chronology is an
explicit falsifier for the shortcut “same CUSIP equals the same lot.” The
AMAPS chronology is directionally consistent but still lacks a lot identifier,
custodian settlement, or receipt record.

## Boundary

This is a chronology and anti-overclaim control. It does not prove that either
statutory consideration amount settled as cash, nor does it identify borrower
collateral cash, Athene allocation, liability cost, or Apollo common-owner
cash.

## Next test

Obtain Schedule D lot identifiers, custodian/trade confirmations, settlement
dates, and receiving-account evidence before promoting either route to a
settled receipt or realized-return claim.
