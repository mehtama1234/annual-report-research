# Capital Flow Apollo Athene Statutory Parser Prototype Pass 1

## Purpose

This pass converts the Athene statutory detail sample into a repeatable parser prototype.

It asks:

`Can we automatically pull named Schedule BA and Schedule D holding rows from the Athene Annuity and Life Company 2025 statutory statement?`

The generated companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-parser-prototype-pass-1.csv`

The first normalized Schedule D output is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-normalized-sample-pass-1.md`

The extraction script is:

`scripts/extract-athene-statutory-detail-samples.py`

The upstream detail sample is:

`/cluster/capital-flow-apollo-athene-statutory-detail-sample-extraction-pass-1.md`

## Short Answer

`Yes, at prototype level. The script extracts 72 repeatable named holding rows from selected Schedule BA and Schedule D detail pages after the row-start recognizer was expanded for statutory CUSIP markers. It captures schedule, page, CUSIP/identifier, raw holding terms, detected NAIC designation, rough asset-type classification, first numeric values, proof use, and boundary. This moves the work from hand-picked examples toward repeatable statutory extraction, but it is still not a final parser because column-level numeric normalization and full-range reconciliation are pending.`

## Parser Output

| Metric | Result |
|---|---:|
| Rows generated | `72` |
| Schedule BA Part 1 rows | `8` |
| Schedule BA Part 2 rows | `14` |
| Schedule D issuer-credit rows | `25` |
| Schedule D ABS rows | `25` |
| Rows with detected NAIC designation | `63` |

## Asset-Type Classification

| Asset-Type Guess | Rows |
|---|---:|
| `us_treasury` | `25` |
| `agency_mbs_or_abs` | `25` |
| `affiliated_or_apollo_related` | `10` |
| `schedule_ba_other_invested_asset` | `7` |
| `structured_credit_or_cmbs` | `3` |
| `credit_fund_or_private_credit_vehicle` | `2` |

## What The Prototype Proves

The parser proves four important things:

1. the PDF text has usable row boundaries for many Schedule D/BA detail rows
2. named CUSIP/identifier rows can be extracted repeatedly
3. NAIC designations can be detected on most Schedule D rows
4. raw value strings and terms can be preserved for later schedule-specific normalization

That gives the Apollo/Athene proof path a practical next step:

`legal-entity statutory statement -> parsed named holdings -> normalized income/value/credit fields -> liability-cost spread bridge`

## What It Still Does Not Prove

This prototype is not the final extraction.

It does not yet prove:

1. complete Schedule BA Part 1 population
2. complete Schedule D issuer-credit population
3. complete Schedule D ABS population
4. final column-level actual cost, par, fair value, book value, income, received interest, and impairment values
5. reconciliation to Schedule D/BA summary totals
6. borrower or originator mapping
7. liability-cost spread
8. asset-level cash return

The main technical limitation is that Schedule BA lines can wrap and subtotal lines can merge into holding rows. Schedule D rows are cleaner, but numeric columns still need schedule-specific parsing instead of generic first-number capture.

## Decision

`apollo-athene-statutory-parser-prototype-ready-column-normalization-next`

The parser prototype is good enough to move from manual samples to repeatable extraction. The next step is column normalization and broader page-range execution.

## Safe Claim

`The Athene statutory parser prototype generates 72 repeatable named holding rows from selected Schedule BA and Schedule D pages after the row-start recognizer was expanded for statutory CUSIP marker characters. It demonstrates extraction feasibility and preserves CUSIP, holding text, detected NAIC designation, rough asset type, and raw numeric fields. It does not yet prove full statutory holdings, reconciled asset totals, liability-cost spread, borrower destination, or asset-level cash return.`

## Next Work

1. Improve Schedule BA row-boundary handling for wrapped rows and subtotal boundaries.
2. Add schedule-specific numeric parsers for Schedule D issuer-credit obligations and ABS rows.
3. Run the parser across pages `5836-5911`, `5912-6027`, and `5813-5829`.
4. Reconcile parsed rows to Schedule D/BA summary totals before promoting any holding-level conclusion.
