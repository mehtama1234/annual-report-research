# Capital Flow Apollo Athene Statutory Schedule D Full-Range Parser Pass 1

## Purpose

This pass runs the Athene statutory Schedule D parser across the full located issuer-credit and asset-backed-security ranges.

It asks:

`Can the Apollo/Athene statutory proof lane move from selected Schedule D samples to full-range named holding extraction?`

The generated companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv`

The extraction script is:

`scripts/extract-athene-statutory-detail-samples.py`

The upstream normalized sample is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-normalized-sample-pass-1.md`

The reconciliation diagnostic is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-reconciliation-diagnostic-pass-1.md`

## Short Answer

`Yes, at full-range parser-output level. The script now parses the located Schedule D Part 1 Section 1 and Section 2 ranges and generates 8,648 normalized rows after the row-start recognizer was expanded for statutory CUSIP marker characters. That includes 3,418 issuer-credit rows and 5,230 asset-backed-security rows. This is a major step from sample extraction toward legal-entity portfolio mapping, but the output is still not reconciled to final proof tolerance and cannot yet be used as final asset-level cash-return proof.`

## Full-Range Output

| Metric | Result |
|---|---:|
| Rows generated | `8,648` |
| Schedule D Part 1 Section 1 rows | `3,418` |
| Schedule D Part 1 Section 2 rows | `5,230` |
| Rows with CUSIP | `8,648` |
| Rows with detected NAIC designation | `8,495` |
| Rows with actual-cost parser output | `8,498` |
| Rows with fair-value parser output | `8,482` |
| Rows with book-value parser output | `8,289` |
| Rows with maturity-date parser output | `8,648` |

## Asset-Type Parser Labels

| Asset-Type Guess | Rows |
|---|---:|
| `issuer_credit_or_bond` | `7,800` |
| `structured_credit_or_cmbs` | `381` |
| `agency_mbs_or_abs` | `186` |
| `affiliated_or_apollo_related` | `130` |
| `us_treasury` | `100` |
| `credit_fund_or_private_credit_vehicle` | `51` |

## Reconciliation Boundary

This pass deliberately does not promote the rows to reconciled statutory holdings.

The parser reads the full located ranges, but the numeric columns are still positional output from dense PDF text. The rough book-value sums from the parser do not yet reconcile to the compact statutory verification figures:

| Schedule | Parser Book-Value Sum | Compact Verification Reference | Status |
|---|---:|---:|---|
| Schedule D Part 1 Section 1 issuer-credit | `85.158422267B USD` | `85.388493720B USD` issuer-credit obligations book/adjusted carrying value | near-reconciled, still hold |
| Schedule D Part 1 Section 2 ABS | `73.460673438B USD` | `73.463901477B USD` ABS book/adjusted carrying value | near-reconciled, still hold |

The remaining gap is much smaller, but the row boundaries and field positions still need a final tolerance policy, page/subtotal review, and income/proceeds matching before any final portfolio-total, spread, or return conclusion.

## What This Proves

This pass proves:

1. the located Schedule D ranges can be executed in bulk
2. thousands of named CUSIP rows can be extracted from the Athene legal-entity filing
3. NAIC designations are visible for most rows
4. maturity dates are visible for nearly all rows
5. the parser now has enough population to support reconciliation work

This is the first real full-range legal-entity portfolio extraction for the Apollo/Athene lane.

## What It Still Does Not Prove

It does not yet prove:

1. final Schedule D totals
2. correct numeric column assignment for every row
3. issuer-level investment income roll-up
4. realized gain/loss matching
5. borrower or originator destination
6. liability-cost spread
7. asset-level cash receipt, repayment, or return

## Decision

`apollo-athene-statutory-schedule-d-full-range-parser-ready-reconciliation-next`

The Schedule D proof lane is now full-range extraction ready. The next gate is reconciliation to Schedule D verification totals, followed by income/proceeds matching and borrower/originator classification.

## Safe Claim

`The Athene statutory parser now produces 8,648 full-range Schedule D rows across issuer-credit and ABS ranges after a statutory CUSIP marker row-start correction. It demonstrates bulk named-holding extraction from a legal-entity statutory filing and now approaches Schedule D verification totals, but it does not yet prove final reconciled totals, liability-cost spread, borrower destination, or asset-level cash return.`

## Next Work

1. Use the reconciliation diagnostic to prioritize rows and pages with missing or shifted book-value fields.
2. Improve row-boundary handling for rows with missing or wrapped numeric columns.
3. Separate issuer-credit, ABS, CMBS, CLO, infrastructure, data-center, royalty, consumer, and fund-like rows.
4. Join rows to investment-income and disposal/proceeds schedules.
5. Build the Apollo/Athene legal-entity spread bridge from liabilities, assets, income, realized gains/losses, and reserves.
