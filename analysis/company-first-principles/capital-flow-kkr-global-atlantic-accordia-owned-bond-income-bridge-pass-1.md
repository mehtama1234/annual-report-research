# Capital Flow KKR Global Atlantic Accordia Owned-Bond Income Bridge Pass 1

## Purpose

This pass joins the near-reconciled Accordia coordinate owned-bond table to legal-entity income and cash-flow context.

It asks:

`Can the KKR/Global Atlantic Accordia statutory prototype move from owned-bond book-value reconciliation to row-level interest-received evidence and legal-entity income context without claiming full borrower cash return?`

The structured bridge table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-pass-1.csv`

The ranked detail table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-detail-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-diagnostic-pass-1.csv`

## Short Answer

`Accordia now has row-level owned-bond cash-back proxy evidence. The coordinate owned-bond base is 7318321094 USD. Owned Schedule D bond rows show 229507957 USD of interest received during the year and 156198987 USD of interest due/accrued. Interest received equals 37.930604% of legal-entity gross investment income, 41.750463% of summary net investment income, and a simple 3.136074% of coordinate owned-bond book value.`

## Bridge Metrics

| Metric | Value | Units |
|---|---:|---|
| Coordinate owned-bond book value | 7318321094 | USD |
| Statutory bond base | 7318322163 | USD |
| Owned-bond interest received | 229507957 | USD |
| Owned-bond interest due/accrued | 156198987 | USD |
| Gross investment income collected | 605073293 | USD |
| Summary net investment income | 549713557 | USD |
| Cash-flow net investment income | 546289441 | USD |
| Interest received / gross income | 37.930604 | percent |
| Interest received / net investment income | 41.750463 | percent |
| Interest received / owned-bond book | 3.136074 | percent |
| Private-marker interest received | 37427454 | USD |
| ABS interest received | 19581142 | USD |

## Top Named Interest-Received Rows

| ID | CUSIP | Marker Type | Book Value | Interest Received | Simple Received/Book % |
|---|---|---|---:|---:|---:|
| CFKKRGACOBIBD-001 | 90231*-AA-0 | statutory-private-marker-cusip | 202125000 | 17419245 | 8.618056 |
| CFKKRGACOBIBD-002 | 54438C-PA-4 | standard-cusip-like | 56626113 | 3093525 | 5.463071 |
| CFKKRGACOBIBD-003 | 458140-BM-1 | standard-cusip-like | 66417686 | 2902052 | 4.369396 |
| CFKKRGACOBIBD-004 | 94974B-GU-8 | standard-cusip-like | 45705863 | 2623425 | 5.739800 |
| CFKKRGACOBIBD-005 | 78486#-AA-3 | statutory-private-marker-cusip | 61250000 | 2305722 | 3.764444 |
| CFKKRGACOBIBD-006 | L9632@-AA-0 | statutory-private-marker-cusip | 21019811 | 1992125 | 9.477369 |
| CFKKRGACOBIBD-007 | 92343V-DS-0 | standard-cusip-like | 37084038 | 1692452 | 4.563829 |
| CFKKRGACOBIBD-008 | 68389X-CK-9 | standard-cusip-like | 25630607 | 1574925 | 6.144704 |
| CFKKRGACOBIBD-009 | 072024-NV-0 | standard-cusip-like | 25657269 | 1339226 | 5.219675 |
| CFKKRGACOBIBD-010 | 58013M-FA-7 | standard-cusip-like | 30494597 | 1322344 | 4.336322 |
| CFKKRGACOBIBD-011 | 91324P-DV-1 | standard-cusip-like | 32819338 | 1232250 | 3.754646 |
| CFKKRGACOBIBD-012 | 0778FP-AN-9 | standard-cusip-like | 18180937 | 1077810 | 5.928242 |

## Proof Effect

This pass moves KKR/Global Atlantic from a destination-only statutory asset map to a cash-back proxy bridge. The owned-bond universe is near-reconciled to the statutory bond base, and the same row set now carries statutory interest received and interest due/accrued fields.

The safe use is:

`Accordia owned Schedule D bonds have near-reconciled book value and row-level statutory interest-received evidence. This supports legal-entity cash-back proxy analysis, not full named borrower return proof.`

## Boundary

This is not full named-cash proof. Interest received in a statutory row does not prove borrower use of proceeds, underlying asset cash receipt, trustee remittance, liability-cost spread, funds-held waterfall, FHLB economics, collateral certificates, IRR, NPV, ROIC, or final return.

## Next Action

Use the top `40` detail rows to build `accordia-owned-bond-income-proceeds-cusip-match`: join selected CUSIPs to disposal/proceeds rows, issuer/wrapper sources, liability-cost context, and controlled-document requests where public proof stops.

## Decision

`kkr-global-atlantic-accordia-owned-bond-income-bridge-visible-cusip-proceeds-match-next`
