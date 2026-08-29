# Capital Flow Apollo Athene Statutory CUSIP Raw Text Inspection Pass 1

## Purpose

This pass checks the raw PDF-extracted Schedule D text for the three cleanest CUSIP row proof packet targets:

1. `00264#-AB-3` AP Aristotle Holdings LLC
2. `28655*-AA-7` Eliant Invest Holding LP
3. `02300A-AA-8` AMAPS 1 LLC Tranche A Note

The goal is to test whether the selected cash-back candidate rows are actually present in the statutory PDF text, and whether the parser fields are strong enough for claim promotion.

The structured outputs are:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cusip-raw-text-inspection-pass-1.csv`

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cusip-raw-text-inspection-diagnostic-pass-1.csv`

The extractor is:

`scripts/inspect-athene-cusip-raw-text.py`

## Main Result

The raw-text inspection covers `9` source rows across `3` CUSIPs and `8` statutory PDF pages.

| Metric | Value |
|---|---:|
| raw text inspection rows | `9` |
| raw rows found | `9` |
| raw rows missing | `0` |
| short numeric stream holds | `4` |
| selected CUSIPs | `3` |
| selected pages | `8` |

This means the selected source rows exist in the PDF-extracted text. The issue is not missing rows. The issue is column semantics and row-level numeric interpretation.

## Selected Row Evidence

| CUSIP | Source Row | Page | Raw Text Result | Parser Boundary |
|---|---|---:|---|---|
| `00264#-AB-3` | year-end holding | `6025` | raw row found | Holding row has book value and income fields visible, but fair-value parser field is suspect for this ABS/private marker row. |
| `00264#-AB-3` | paydown disposal | `6279` | raw row found | Cash-like paydown candidate, but short numeric stream means gain/loss and book columns stay on hold. |
| `00264#-AB-3` | Various disposal | `6279` | raw row found | Large cash-like row with repeated `525.327798M USD` numeric fields; needs column-level interpretation. |
| `00264#-AB-3` | tax-free exchange | `6334` | raw row found | Noncash/transfer hold; should not be promoted as cash return. |
| `28655*-AA-7` | year-end holding | `5904` | raw row found | Holding row shows book/fair value around `23.238692M USD` and received amount around `23.286772M USD`. |
| `28655*-AA-7` | Various disposal | `6137` | raw row found | Large cash-like candidate with `356.444966M USD` consideration-style fields, but gain/loss interpretation is not final. |
| `28655*-AA-7` | redemption row | `6312` | raw row found | Short numeric stream hold; redemption classification visible but column semantics need inspection. |
| `02300A-AA-8` | year-end holding | `6023` | raw row found | Holding row shows `1.917500000B USD` book/fair fields and `48.871440M USD` income field. |
| `02300A-AA-8` | Apollo Capital Markets Partner disposal | `6276` | raw row found | Cash-like counterparty row with `268.000000M USD` consideration-style fields, but gain/loss parser field is not safe. |

## What This Proves

This pass proves:

1. the selected CUSIP rows are present in the raw PDF-extracted statutory text
2. the row packet did not invent the selected holding/disposal rows
3. Aristotle, Eliant, and AMAPS each have same-CUSIP holding and disposal/proceeds source text
4. the cash-like versus tax-free exchange split is source-text visible
5. the next blocker is statutory column parsing, not source discovery

## What It Does Not Prove

This pass does not prove:

1. final statutory column labels for every numeric token
2. realized gain/loss economics
3. lot-level continuity between the year-end holding and disposal lot
4. borrower receipt or use of proceeds
5. liability-cost spread
6. asset-level IRR, NPV, ROIC, or realized return

The most important warning is:

`Several disposal rows show short numeric streams or repeated consideration-like values. Those rows are real rows, but the parser cannot yet safely assign all numeric fields to book value, realized gain/loss, and income columns.`

## Best Next Proof Move

The next pass should be page-specific column inspection for the selected disposal pages:

| Page | CUSIP | Why |
|---:|---|---|
| `6279` | `00264#-AB-3` | Contains the large Aristotle paydown and Various rows. |
| `6137` | `28655*-AA-7` | Contains the large Eliant Various row. |
| `6276` | `02300A-AA-8` | Contains the AMAPS Apollo Capital Markets Partner row. |
| `6334` | `00264#-AB-3` | Contains the Aristotle tax-free exchange hold. |
| `6312` | `28655*-AA-7` | Contains the Eliant redemption row and other Part 5 rows. |

The upgrade test is:

`raw row found + page-specific column interpretation + consideration/book/gain-loss sanity + cash-like disposition + safe boundary`

## Safe Claim

`The Athene raw-text inspection confirms that the selected Aristotle, Eliant, and AMAPS CUSIP proof-packet rows are present in the statutory PDF text. All 9 selected source rows are found across 8 pages, with 4 rows flagged for short numeric-stream or column-semantics holds. This supports source-row existence and targeted column inspection, not final realized gain/loss, borrower-cash, liability-spread, or asset-return proof.`

## Decision

`apollo-athene-cusip-raw-text-inspection-source-rows-found-column-semantics-next`

The selected row proof packet is source-text supported. The next blocker is page-specific statutory column interpretation, especially for disposal rows with repeated or short numeric streams.

