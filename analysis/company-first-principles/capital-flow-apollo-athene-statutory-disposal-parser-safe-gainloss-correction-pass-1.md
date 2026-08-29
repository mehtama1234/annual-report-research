# Capital Flow Apollo Athene Statutory Disposal Parser Safe Gain/Loss Correction Pass 1

## Purpose

This pass applies the selected CUSIP column-interpretation lesson back to the full Athene Schedule D disposal/proceeds parser.

The correction is narrow and conservative:

`keep consideration extraction, add disposition/cash-likeness classification, and stop promoting shifted large-token values as realized gain/loss.`

The corrected parser output remains:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-parser-pass-1.csv`

The correction diagnostic is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-disposal-parser-safe-gainloss-correction-pass-1.csv`

The updated parser is:

`scripts/extract-athene-schedule-d-disposals.py`

## What Changed

The disposal/proceeds parser now appends four safer fields:

| Field | Meaning |
|---|---|
| `economic_disposition_class` | Classifies the row as paydown, market/counterparty sale, redemption/call, maturity, tax-free exchange hold, security withdrawal hold, direct/private transfer hold, or unclassified hold. |
| `row_cash_likeness` | Separates cash-like candidates from noncash/transfer holds. |
| `safe_realized_gain_loss` | Promotes only independently visible small parenthetical gain/loss values. |
| `gain_loss_interpretation_status` | Explains why a gain/loss value is safe, not visible, shifted, or not promoted. |

The old `realized_gain_loss` field remains in the CSV for audit continuity, but downstream proof tables now prefer `safe_realized_gain_loss`.

## Main Result

The regenerated parser still has `7,655` disposal/proceeds rows and the same consideration tie:

| Scope | Parser Consideration | Statutory Reference | Coverage |
|---|---:|---:|---:|
| Schedule D Part 4 plus Part 5 | `72.807523483B USD` | `72.140293824B USD` | `100.9249%` |

The schema expands from `18` to `22` columns.

## Cash-Likeness Classification

| Classification | Rows |
|---|---:|
| cash-like candidate | `7,396` |
| noncash-or-transfer hold | `259` |

## Economic Disposition Classes

| Class | Rows |
|---|---:|
| principal-paydown-cash-candidate | `3,636` |
| market-sale-or-counterparty-cash-candidate | `3,258` |
| redemption-or-call-cash-candidate | `389` |
| tax-free-exchange-hold | `186` |
| maturity-proceeds-cash-candidate | `113` |
| security-withdrawal-hold | `45` |
| direct-or-private-transfer-hold | `21` |
| unclassified-hold | `7` |

## Gain/Loss Control

| Gain/Loss Status | Rows |
|---|---:|
| legacy-positional-gain-loss-not-promoted | `6,010` |
| parser-gain-loss-equals-consideration-column-shift-hold | `717` |
| small-parenthetical-gain-loss-visible | `542` |
| gain-loss-not-visible | `386` |

The safe realized gain/loss sum is only:

`-168,096 USD`

That number is not a full Schedule D realized gain/loss total. It is the sum of only the independently visible small parenthetical values captured by the conservative rule.

## Downstream Effect

The dependent CUSIP outputs were regenerated.

The most important downstream correction is in the first row-level proof packet:

| Metric | Before | After |
|---|---:|---:|
| selected gross disposal consideration | `3.851152934B USD` | `3.851152934B USD` |
| selected cash-like disposal consideration | `1.569389612B USD` | `1.569389612B USD` |
| selected realized gain/loss field | `3.355092753B USD` | `-18 USD` |

That is the proof-control point. The old row-packet gain/loss number was shifted-token noise. The corrected downstream table now refuses to promote it.

## What This Proves

This pass proves:

1. consideration extraction remains stable after the safer parser correction
2. disposition classification can be applied across the full `7,655` row disposal/proceeds universe
3. downstream tables can separate cash-like rows from noncash/transfer holds
4. legacy realized-gain/loss values should not be used for return claims
5. selected-row proof packets now avoid the prior false gain/loss promotion

## What It Does Not Prove

This pass does not prove:

1. final full Schedule D gain/loss reconciliation
2. final lot-level asset return
3. borrower receipt or use of proceeds
4. liability-cost spread
5. IRR, NPV, ROIC, or cash-on-cash return

## Safe Claim

`The Athene disposal/proceeds parser now preserves the 7,655-row consideration worklist while adding disposition class, cash-likeness, safe gain/loss, and gain/loss status controls. The full parser still ties to 100.9249% of the statutory disposal consideration reference, but downstream proof tables now avoid using shifted large-token values as realized gain/loss. This supports cash-like consideration classification and parser-quality control, not final realized-return, borrower-cash, or liability-spread proof.`

## Decision

`apollo-athene-disposal-parser-safe-gainloss-corrected-consideration-stable`

The Apollo/Athene statutory prototype now has safer full-universe disposal/proceeds classification. The next proof move is full Schedule D gain/loss reconciliation or selected-row PDF/column inspection for cash-like consideration candidates.

