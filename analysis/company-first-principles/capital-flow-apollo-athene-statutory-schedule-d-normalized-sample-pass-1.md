# Capital Flow Apollo Athene Statutory Schedule D Normalized Sample Pass 1

## Purpose

This pass takes the repeatable Athene statutory parser prototype and turns the selected Schedule D rows into a first normalized table.

It asks:

`Can the Athene statutory statement produce named Schedule D holdings in analyzable columns instead of raw row text?`

The generated companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-normalized-sample-pass-1.csv`

The extraction script is:

`scripts/extract-athene-statutory-detail-samples.py`

The upstream parser prototype is:

`/cluster/capital-flow-apollo-athene-statutory-parser-prototype-pass-1.md`

The full-range Schedule D parser output is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.md`

## Short Answer

`Yes, at first normalized-sample level. The script now writes 50 Schedule D rows with separate fields for parser row, schedule, page, CUSIP, issuer or description, NAIC designation, asset-type guess, cost/value fields, income/received-interest fields, acquired date, maturity date, status, and boundary. This moves Apollo/Athene from raw named-holding extraction toward usable legal-entity asset analysis, but it is still not reconciled statutory proof or asset-level cash-return proof.`

## Normalized Output

| Metric | Result |
|---|---:|
| Rows generated | `50` |
| Schedule D Part 1 Section 1 rows | `25` |
| Schedule D Part 1 Section 2 rows | `25` |
| Rows with CUSIP | `50` |
| Rows with detected NAIC designation | `50` |
| Rows with actual-cost parser output | `50` |
| Rows with maturity-date parser output | `50` |

## What Is Now Visible

The normalized sample separates the Schedule D rows into these useful fields:

1. legal-entity source row
2. Schedule D section and page
3. CUSIP
4. issuer or security description
5. NAIC designation
6. rough asset type
7. actual cost
8. par value where visible in the parser
9. fair value
10. book/adjusted carrying value
11. unrealized valuation change
12. interest-income proxy
13. interest-received proxy
14. acquisition date
15. maturity date

That matters because the Apollo/Athene proof lane needs a joined chain:

`insurance liability source -> Athene legal entity -> Schedule D named holding -> statutory value/grade/income -> proceeds or cash-flow evidence -> liability-cost spread or asset return`

This pass moves the middle of that chain from source-located to parser-visible.

## Boundary

This is not a final Schedule D parser.

The current numeric columns are positional parser output from dense PDF text. They are strong enough to prove that normalization is feasible, but not strong enough to support final accounting claims.

It does not yet prove:

1. full Schedule D population
2. reconciliation to Schedule D verification totals
3. final column-level statutory values
4. borrower or originator matching
5. investment-income roll-up by issuer or asset class
6. realized gain/loss or impairment roll-up
7. liability-cost spread
8. asset-level cash return

## Decision

`apollo-athene-statutory-schedule-d-normalized-sample-ready-full-reconciliation-pending`

The normalized sample is good enough to become the first reusable Schedule D parser output. The next step is full-range Schedule D execution and reconciliation to statutory Schedule D verification totals before using the rows for investment-return claims.

## Safe Claim

`The Athene statutory parser now generates a 50-row normalized Schedule D sample from selected issuer-credit and ABS pages. It separates CUSIP, issuer/description, NAIC designation, cost/value fields, income/received-interest signals, acquisition date, and maturity date. It demonstrates that legal-entity named holdings can be converted into analyzable columns, but it does not yet prove full Schedule D totals, borrower destination, liability-cost spread, or asset-level cash return.`

## Next Work

1. Reconcile full-range parsed rows to Schedule D verification totals.
2. Improve row-boundary handling for wrapped numeric columns.
3. Add Schedule BA normalization after improving wrapped-row handling.
4. Join normalized holdings to investment-income, proceeds, impairment, and liability-cost fields.
5. Build the first Apollo/Athene legal-entity spread bridge.
