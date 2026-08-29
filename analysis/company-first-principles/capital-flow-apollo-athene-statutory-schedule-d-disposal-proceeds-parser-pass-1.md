# Capital Flow Apollo Athene Statutory Schedule D Disposal Proceeds Parser Pass 1

## Purpose

This pass moves Apollo/Athene from entity-level proceeds evidence to a named disposal worklist.

It asks:

`Can the Athene statutory Schedule D disposal pages produce named sold, redeemed, matured, paydown, or otherwise disposed rows with consideration and gain/loss fields?`

The generated companion tables are:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-parser-pass-1.csv`

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-diagnostic-pass-1.csv`

The extraction script is:

`scripts/extract-athene-schedule-d-disposals.py`

The upstream income/cash bridge is:

`/cluster/capital-flow-apollo-athene-statutory-legal-entity-income-cash-bridge-pass-1.md`

## Short Answer

`Yes, at named disposal worklist level. The parser extracts 7,655 Schedule D disposal rows: 6,250 from Part 4 and 1,405 from Part 5. The combined first-pass parser consideration total is 72.807523483B USD versus the statutory disposal consideration reference of 72.140293824B USD, or 100.9249% coverage. That is close enough to prove the disposal pages can generate a named proceeds worklist, but not close enough to prove final realized-return accounting.`

## Parser Output

| Metric | Result |
|---|---:|
| Schedule D Part 4 rows | `6,250` |
| Schedule D Part 5 rows | `1,405` |
| Total disposal parser rows | `7,655` |
| Part 4 parser consideration | `45.516400075B USD` |
| Part 5 parser consideration | `27.291123408B USD` |
| Combined parser consideration | `72.807523483B USD` |
| Statutory disposal consideration reference | `72.140293824B USD` |
| Difference | `667.229659M USD` |
| Coverage | `100.9249%` |

## Why This Matters

The prior bridge showed:

`54.035221430B USD` of bond sale/maturity/repayment proceeds on the cash-flow statement.

The compact Schedule D verification showed:

`72.140293824B USD` of consideration for bonds and stocks disposed.

This pass adds the named-row layer under that summary:

`CUSIP / issuer -> disposal date -> purchaser or disposition type -> consideration -> book value at disposal -> realized gain/loss -> interest/dividends received`

That is the right next step toward answering:

`which assets produced cash back?`

## Examples

| Row | Page | CUSIP | Issuer / Description | Disposal Date | Purchaser / Type | Consideration |
|---|---:|---|---|---|---|---:|
| `CFAASDDP-00001` | `6074` | `912810-TT-5` | United States Treasury Note/Bond | `03/10/2025` | Goldman Sachs | `5.580938M USD` |
| `CFAASDDP-00002` | `6074` | `912810-TT-5` | United States Treasury Note/Bond | `09/18/2025` | ACRA RE 2A Surplus AAM | `90.165632M USD` |
| `CFAASDDP-00003` | `6074` | `912810-TU-2` | United States Treasury Note/Bond | `03/10/2025` | Various | `50.414512M USD` |
| `CFAASDDP-06142` | `6279` | `20633K-AA-6` | Concord Music Royalties LLC | current-year disposal row | parser visible | `550.000000M USD` |
| `CFAASDDP-06157` | `6279` | `00264#-AB-3` | AP Aristotle Holdings LLC(Old) | current-year disposal row | parser visible | `525.327798M USD` |
| `CFAASDDP-07630` | `6334` | `L0187*-AA-0` | AP Alkaios Luxembourg SARL | current-year acquired and disposed row | Tax Free Exchange | `2.594729570B USD` |

## Reconciliation Status

| Scope | Parser Rows | Parser Consideration | Reference | Coverage | Status |
|---|---:|---:|---:|---:|---|
| Schedule D Part 4 | `6,250` | `45.516400075B USD` | `72.140293824B USD` | `63.0943%` | not standalone reconciled |
| Schedule D Part 5 | `1,405` | `27.291123408B USD` | `72.140293824B USD` | `37.8306%` | not standalone reconciled |
| Schedule D Part 4 plus Part 5 | `7,655` | `72.807523483B USD` | `72.140293824B USD` | `100.9249%` | near-reconciled hold |

## What It Proves

This pass proves:

1. Schedule D Part 4 and Part 5 can be parsed into thousands of named disposal rows
2. consideration/proceeds fields are visible at row level
3. disposal dates and purchaser/disposition labels are often visible
4. realized gain/loss and interest/dividend fields are present in the raw numeric stream
5. the combined consideration parser is close to the statutory disposal consideration reference

## What It Still Does Not Prove

It does not yet prove:

1. final disposal consideration reconciliation
2. final realized gain/loss reconciliation
3. clean purchaser labels for every row
4. whether Part 5 rows require additional subtotal or duplicate treatment
5. matching between year-end holdings and disposed holdings
6. borrower cash receipt or asset-level return
7. liability-cost spread

## Decision

`apollo-athene-statutory-schedule-d-disposal-proceeds-parser-near-reconciled-worklist-hold`

The disposal/proceeds parser is useful as a named cash-back worklist, but it must stay below final realized-return proof until consideration, book-at-disposal, gain/loss, and interest/dividend fields reconcile.

## Safe Claim

`Athene Schedule D Part 4 and Part 5 now produce 7,655 named disposal/proceeds parser rows. The first-pass combined consideration sum is 72.807523483B USD versus a 72.140293824B USD statutory reference, or 100.9249% coverage. This supports named proceeds worklist language, not final realized-return, borrower-cash, or spread proof.`

## Next Work

1. Reconcile Part 4/Part 5 subtotal treatment to the `72.140293824B USD` statutory consideration total.
2. Add gain/loss-specific diagnostics against the final Schedule D total line.
3. Match disposal rows to the near-reconciled Schedule D holdings table by CUSIP and issuer.
4. Separate maturity, paydown, redemption, tax-free exchange, sale, affiliate transfer, and internal ACRA disposition types.
5. Use matched rows to build the first CUSIP-level cash-back sample.
