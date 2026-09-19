# Capital Flow Apollo Athene Statutory Safe Cash-Like Same-CUSIP Raw Text Inspection Pass 1

## Purpose

This pass inspects the raw statutory PDF text behind the clean same-CUSIP cash-like row proof packet.

The question is:

`For the clean same-CUSIP cash-like Athene candidates, are the selected holding and disposal/proceeds rows actually present in the statutory PDF text, and which rows still need column-level review?`

The inspection table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-raw-text-inspection-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-raw-text-inspection-diagnostic-pass-1.csv`

The inspector is:

`scripts/inspect-athene-safe-cashlike-same-cusip-raw-text.py`

## Main Result

The inspection covers the `8` clean candidates from the `10` same-CUSIP packet.

| Metric | Value |
|---|---:|
| raw text inspection rows | `19` |
| clean packet count | `8` |
| selected CUSIPs | `8` |
| selected pages | `14` |
| raw rows found | `19` |
| raw rows missing | `0` |
| disposal/proceeds rows | `11` |
| year-end holding rows | `8` |
| inspection-ready rows | `17` |
| short numeric-stream holds | `2` |

## Selected CUSIP Coverage

| CUSIP | Row types found | Pages | Status |
|---|---|---|---|
| `28655*-AA-7` | holding plus disposal/proceeds | `5904`, `6137`, `6312` | found; one short numeric-stream hold |
| `02300A-AA-8` | holding plus disposal/proceeds | `6023`, `6276` | found; one short numeric-stream hold |
| `20633K-AN-8` | holding plus disposal/proceeds | `6025`, `6334` | found; inspection-ready |
| `592918-AA-4` | holding plus disposal/proceeds | `5979`, `6323` | found; inspection-ready |
| `91282C-LW-9` | holding plus disposal/proceeds | `5837`, `6075`, `6284` | found; inspection-ready |
| `28655*-AB-5` | holding plus disposal/proceeds | `5904`, `6137`, `6312` | found; inspection-ready |
| `912810-TW-8` | holding plus disposal/proceeds | `5836`, `6074` | found; inspection-ready |
| `91282C-MG-3` | holding plus disposal/proceeds | `5837`, `6284` | found; inspection-ready |

## Rows Requiring Column Review

Two rows are found but still need tighter column interpretation:

| CUSIP | Source row | Page | Reason |
|---|---|---:|---|
| `28655*-AA-7` | `CFAASDDP-07047` | `6312` | disposal/proceeds row found, but the raw numeric stream has only `5` money tokens |
| `02300A-AA-8` | `CFAASDDP-06062` | `6276` | disposal/proceeds row found, but the raw numeric stream has only `5` money tokens |

The important point is that neither blocker is a missing-source blocker. Both rows exist in the PDF text. The blocker is column semantics and visual/layout interpretation.

## What This Tells Us In Simple Terms

We are no longer guessing from a summary table. For the clean same-CUSIP candidates, the rows are present in the actual Athene statutory PDF text.

That means the Apollo/Athene proof path now has:

1. a near-reconciled Schedule D holding map
2. a corrected disposal/proceeds parser
3. a full-universe cash-like proceeds summary
4. a top same-CUSIP row packet
5. raw PDF row availability for the clean same-CUSIP candidates

The next gap is not whether the rows exist. The next gap is whether the columns can be visually or layout-accurately interpreted enough to promote consideration, book value, interest, and any safe gain/loss for individual rows.

## What This Proves

This pass proves:

1. all `19` selected clean-candidate source rows are found in the statutory PDF text
2. all `8` clean same-CUSIP candidates have both year-end holding and disposal/proceeds row text available
3. most selected rows are ready for column-level inspection
4. the remaining holds are narrow and page-specific
5. no selected clean candidate failed because the source row was missing

## What It Does Not Prove

This pass does not prove:

1. final column semantics for all selected rows
2. final realized gain/loss
3. lot-level continuity
4. borrower receipt or use of proceeds
5. Apollo/Athene source-of-funds allocation
6. liability-cost spread
7. IRR, NPV, ROIC, cash-on-cash return, or platform profit

## Safe Claim

`The clean Athene same-CUSIP cash-like candidate packet now has raw statutory PDF row support: all 19 selected holding and disposal/proceeds rows were found across 8 CUSIPs and 14 pages, with 17 rows inspection-ready and 2 rows held for page-specific column interpretation. This supports source-row availability for named cash-like proceeds inspection, not final borrower receipt, liability spread, or asset-level return proof.`

## Decision

`apollo-athene-clean-same-cusip-raw-text-found-column-review-next`

The next move is page-specific column/image inspection for pages `6276` and `6312`, then borrower/issuer mapping for the clean non-Treasury candidates.

The [native coordinate diagnostic](data/capital-flow-apollo-athene-statutory-schedule-d-coordinate-column-diagnostic-2026-09-15.csv)
now captures both held rows after expanding the CUSIP pattern to preserve the
source's `*` marker. Page `6276` exposes the AMAPS row's positioned values
including `268,000,000` and `3,986,842`; page `6312` exposes the Eliant row's
positioned values including `1,806,570` and `43,047`. These are native
coordinate observations only; they are not yet assigned to accounting columns.
