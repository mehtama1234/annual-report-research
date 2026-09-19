# MF1 Same-CUSIP to Servicing-Route Join Boundary

Research date: `2026-09-17`

## Purpose

This pass links the corrected Athene statutory same-CUSIP packet to the MF1
public servicing route:

`Athene statutory holding -> same-CUSIP disposal/proceeds row -> MF1 issuer and servicing accounts -> borrower/trustee cash`

Only the first three links are currently source-backed.

## Row-level observation

The corrected row packet contains the following MF1 candidate:

| Field | Observed value | Boundary |
| --- | --- | --- |
| CUSIP | `592918-AA-4` | Same-CUSIP matching is not lot-level continuity. |
| Issuer/description | MF1 2025-B2 LLC, MF1 2025-B2 A, 5.362%, due 05/18/40 | Issuer identity is not Athene legal ownership by itself. |
| Year-end holding row | Schedule D Part 1, Section 2, source row `5979`, holding date `04/11/2025` | Holding row does not disclose purchase lot, custodian, or unrestricted cash. |
| Disposal/proceeds row | Schedule D Part 5, source row `6323`, dated `04/11/2025`, disposition text `Piper Jaffray 05/28/2025 Various` | Disposition text and parser classification are not a bank settlement confirmation. |
| Selected consideration | `$209,559,375` | Cash-like under the corrected parser; not a borrower receipt. |
| Related reported values | `$209,475,000` and `$1,302,655` appear in the selected row's numeric stream | Positional statutory fields remain subject to row-level source inspection and are not assigned to principal, gain, or interest beyond the packet's safe classification. |

## Route binding

The MF1 servicing agreement supplies the next contractual route: properly
identified borrower payments enter the Collection Account, specified fees and
expenses may be withdrawn, and good and available funds are remitted to the
Note Administrator/Payment Account. The same agreement also distinguishes
partitioned-loan and companion-interest cash. This makes the statutory row a
target for a cash join, not evidence that the join has occurred. The exhibit's
issuer is MF1 2026-FL21 LLC, so the route remains a separate-series mechanics
observation until it is cross-walked to the MF1 2025-B2 statutory candidate.

## Promotion status

`partial-upgrade — same-CUSIP Athene statutory row is bound to the MF1 issuer and public servicing route`

Still missing:

1. purchase, custody, and lot-continuity records;
2. Athene legal-entity ownership and allocation at the selected date;
3. borrower-level payment and Collection Account receipt;
4. trustee/Payment Account remittance and noteholder allocation;
5. servicing, financing, and policyholder-liability cost allocation; and
6. Apollo/common-owner residual cash and a bounded asset return.

## Safe claim

`Athene's corrected statutory packet contains a same-CUSIP MF1 2025-B2 row with $209.559M of selected cash-like consideration, and the public MF1 servicing agreement supplies a named collection-to-trustee route. This is a row-level source-acquisition target, not proof of lot continuity, borrower receipt, Athene remittance, liability-adjusted return, or Apollo common-owner cash.`

## Structured sources

- `analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-row-proof-packet-detail-pass-1.csv`, rows `CFAASCSCRPD-0015` and `CFAASCSCRPD-0016`
- `raw/primary-sources/capital-flow/mf1/2026-03/mf1-2025-b2-transaction-exhibit.htm`
- [MF1 servicing-waterfall mechanics boundary](capital-flow-apollo-athene-mf1-servicing-waterfall-mechanics-boundary-2026-09-17.md)
