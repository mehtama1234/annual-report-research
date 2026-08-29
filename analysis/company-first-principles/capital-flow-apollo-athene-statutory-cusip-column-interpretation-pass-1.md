# Capital Flow Apollo Athene Statutory CUSIP Column Interpretation Pass 1

## Purpose

This pass interprets the statutory Schedule D disposal-row columns for the selected Aristotle, Eliant, and AMAPS CUSIP raw-text rows.

The goal is narrow:

`confirm which selected disposal-row numeric fields can safely be treated as consideration, and identify which gain/loss fields must remain on hold.`

The structured outputs are:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cusip-column-interpretation-pass-1.csv`

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cusip-column-interpretation-diagnostic-pass-1.csv`

The builder is:

`scripts/build-athene-cusip-column-interpretation.py`

## Source Inputs

| Input | Role |
|---|---|
| Raw-text inspection rows | Provides the actual PDF-extracted statutory row text for selected disposal/proceeds rows. |
| Schedule D Part 4 headers | Anchors sold/redeemed/disposed row layout for current-year disposals. |
| Schedule D Part 5 headers | Anchors acquired-and-fully-disposed row layout. |

## Main Result

The pass interprets `6` selected disposal/proceeds rows.

| Metric | Value |
|---|---:|
| column interpretation rows | `6` |
| parser consideration confirmed rows | `6` |
| gain/loss hold rows | `4` |
| noncash exchange hold rows | `1` |
| safe cash-like consideration interpreted | `1.402283884B USD` |

## Selected Row Interpretation

| CUSIP | Source Row | Page | Disposition | Safe Consideration | Gain/Loss Status | Verdict |
|---|---|---:|---|---:|---|---|
| `00264#-AB-3` | `CFAASDDP-06154` | `6279` | Paydown | `250.704550M USD` | gain/loss not safely visible | consideration-safe paydown candidate, gain/loss hold |
| `00264#-AB-3` | `CFAASDDP-06157` | `6279` | Various | `525.327798M USD` | parser gain/loss equals consideration, column-shift hold | consideration-safe market/counterparty candidate, gain/loss hold |
| `00264#-AB-3` | `CFAASDDP-07636` | `6334` | Tax Free Exchange | `6.588486M USD` | parser gain/loss equals consideration, column-shift hold | noncash exchange hold |
| `28655*-AA-7` | `CFAASDDP-01948` | `6137` | Various | `356.444966M USD` | small `(18)` loss visible; parser missed or shifted | consideration-safe market/counterparty candidate, gain/loss hold |
| `28655*-AA-7` | `CFAASDDP-07047` | `6312` | Redemption | `1.806570M USD` | parser gain/loss equals consideration, column-shift hold | consideration-safe redemption candidate, gain/loss hold |
| `02300A-AA-8` | `CFAASDDP-06062` | `6276` | Apollo Capital Markets Partner | `268.000000M USD` | parser gain/loss equals consideration, column-shift hold | consideration-safe market/counterparty candidate, gain/loss hold |

## What This Proves

This pass proves:

1. selected disposal-row consideration fields are confirmed by schedule layout and raw token position
2. the current parser's consideration extraction is reliable for these selected rows
3. gross consideration must still be split between cash-like rows and tax-free exchange/noncash holds
4. the current realized-gain/loss parser field is not safe for most selected rows
5. small values such as `(18)` can be economically important but missed by the current thousands-only numeric tokenizer

## What This Does Not Prove

This pass does not prove:

1. final realized gain/loss for the selected rows
2. full Schedule D Part 4 or Part 5 parser correction
3. lot-level continuity between year-end holding rows and disposal rows
4. borrower cash receipt or use of proceeds
5. liability-cost spread
6. asset-level IRR, NPV, ROIC, or final cash return

## Parser Implication

The selected rows show that the next parser improvement should separate:

1. large money tokens used for consideration, par, actual cost, book value, and interest
2. small parenthetical gain/loss tokens such as `(18)`
3. noncash exchange rows from cash-like paydown, sale, redemption, and counterparty rows

The current parser can keep using the first large token as Part 4 consideration and the third large token as Part 5 consideration for these selected rows, but it should not promote `realized_gain_loss` from positional large-token logic.

## Safe Claim

`The selected Athene CUSIP column interpretation confirms consideration for 6 disposal/proceeds rows across Aristotle, Eliant, and AMAPS. It identifies 1.402283884B USD of safe cash-like consideration and keeps 4 gain/loss rows on hold because the current parser often shifts consideration-like tokens into gain/loss fields. This supports selected cash-like consideration evidence and parser-correction design, not final realized gain/loss, borrower-cash, liability-spread, or asset-return proof.`

## Decision

`apollo-athene-cusip-column-interpretation-consideration-confirmed-gainloss-hold`

Selected Apollo/Athene disposal-row consideration is now safer than before, but realized gain/loss remains a parser-correction blocker before any full asset-return claim.

