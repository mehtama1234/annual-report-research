# Capital Flow Apollo Athene Statutory CUSIP Row Proof Packet Pass 1

## Purpose

This pass executes the first row-level proof packet from the Apollo/Athene high-dollar CUSIP inspection queue.

It takes the first `5` tier-1 same-CUSIP cash-back candidates and pulls the underlying Schedule D holding and disposal/proceeds rows into one proof packet.

The structured outputs are:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cusip-row-proof-packet-pass-1.csv`

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cusip-row-proof-packet-detail-pass-1.csv`

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cusip-row-proof-packet-diagnostic-pass-1.csv`

The builder is:

`scripts/build-athene-cusip-row-proof-packet.py`

## Source Inputs

| Input | Role |
|---|---|
| CUSIP high-dollar inspection table | Selects the first `5` tier-1 same-CUSIP cash candidates. |
| Schedule D full-range holdings parser | Supplies year-end holding rows. |
| Schedule D disposal/proceeds parser | Supplies disposal/proceeds rows, dates, consideration, book/gain/loss-style fields, and disposition labels. |

## Selected CUSIPs

| Proof Packet | CUSIP | Description Sample | Disposition Class |
|---|---|---|---|
| `CFAASCBCRP-001` | `G7741@-AC-4` | SVF II Finco Cayman LP | principal-paydown-cash-candidate |
| `CFAASCBCRP-002` | `00264#-AB-3` | AP Aristotle Holdings LLC | principal-paydown-cash-candidate |
| `CFAASCBCRP-003` | `28655*-AA-7` | Eliant Invest Holding LP | market-sale-or-counterparty-cash-candidate |
| `CFAASCBCRP-004` | `Q7457#-AA-9` | Turbin Finance Trust 2024-1 | principal-paydown-cash-candidate |
| `CFAASCBCRP-005` | `02300A-AA-8` | AMAPS 1 LLC Tranche A Note | market-sale-or-counterparty-cash-candidate |

## Main Result

The proof packet has:

| Metric | Value |
|---|---:|
| summary rows | `5` |
| detail rows | `20` |
| selected year-end holding rows | `5` |
| selected disposal/proceeds rows | `15` |
| selected gross disposal consideration | `3.851152934B USD` |
| selected cash-like disposal consideration | `1.569389612B USD` |
| cash-like share of selected consideration | `40.7512%` |
| selected year-end book value | `3.727673982B USD` |
| selected gross consideration to year-end book ratio | `1.033125x` |

## Why The Cash-Like Split Matters

The high-dollar CUSIP match said these five rows were tier-1 candidates. The row-level packet shows why candidate status is not final proof.

Several CUSIPs contain multiple disposal rows with mixed economics. For example:

| CUSIP | Gross Consideration | Cash-Like Consideration | Noncash/Transfer Hold | What Happened |
|---|---:|---:|---:|---|
| `G7741@-AC-4` | `2.089548152B USD` | `50.751045M USD` | `2.038797107B USD` | Small paydown rows plus very large tax-free exchange rows. |
| `00264#-AB-3` | `782.620834M USD` | `776.032348M USD` | `6.588486M USD` | Mostly paydown/market-sale style rows, with one tax-free exchange hold. |
| `28655*-AA-7` | `358.251536M USD` | `358.251536M USD` | `0` | Market/counterparty and redemption-style rows. |
| `Q7457#-AA-9` | `352.732412M USD` | `116.354683M USD` | `236.377729M USD` | Paydown/redemption rows plus a large tax-free exchange hold. |
| `02300A-AA-8` | `268.000000M USD` | `268.000000M USD` | `0` | Market/counterparty-style row with Apollo Capital Markets Partner label. |

The key finding is:

`The row-level packet cuts the first five high-dollar tier-1 candidates from 3.851152934B USD of gross consideration to 1.569389612B USD of cash-like consideration after tax-free exchange rows are separated.`

## What This Proves

This pass proves:

1. the selected CUSIPs exist in both year-end Schedule D holdings and disposal/proceeds outputs
2. the source row counts are visible for each selected CUSIP
3. the disposal rows have dates, pages, consideration, and disposition labels
4. mixed CUSIP economics can be separated row by row
5. the next row-level proof work should focus on cash-like rows, not gross consideration totals

## What It Does Not Prove

This pass does not prove:

1. lot-level continuity between the year-end holding and each disposal row
2. final statutory consideration reconciliation for each CUSIP
3. final realized gain/loss, because some positional parser fields still appear suspect
4. borrower receipt or borrower use of proceeds
5. liability-cost spread
6. IRR, NPV, ROIC, or final asset-level return

The `realized_gain_loss` column is especially a hold. Several selected rows show realized gain/loss values that equal or nearly equal consideration, which is a parser-position warning, not an economic conclusion.

## Best Next Rows

The cleanest immediate cash-like row inspections are:

| CUSIP | Source Rows | Why It Is Next |
|---|---|---|
| `00264#-AB-3` | `1` holding row, `3` disposal rows | Mostly cash-like consideration after a small tax-free exchange hold. |
| `28655*-AA-7` | `1` holding row, `2` disposal rows | Cash-like rows only in this packet; useful for market-sale/redeem classification. |
| `02300A-AA-8` | `1` holding row, `1` disposal row | Clean row count and Apollo counterparty label, but fund/security cash is not borrower cash. |
| `Q7457#-AA-9` | `1` holding row, `4` disposal rows | Mixed paydown/redemption/exchange case; good classification test. |
| `G7741@-AC-4` | `1` holding row, `5` disposal rows | Large headline consideration, but mostly tax-free exchange hold after row-level split. |

## Safe Claim

`The first Athene CUSIP row proof packet inspects five tier-1 same-CUSIP cash-back candidates. It links five year-end holding rows to fifteen disposal/proceeds rows. Those rows have 3.851152934B USD of gross disposal consideration, but only 1.569389612B USD is currently cash-like after tax-free exchange rows are separated. This supports row-level cash-back candidate selection and parser-quality control, not final realized gain/loss, borrower-cash, liability-spread, or asset-return proof.`

## Decision

`apollo-athene-cusip-row-proof-packet-ready-cashlike-split-reconciliation-next`

The Apollo/Athene prototype has moved from high-dollar ranking to row-level cash-like filtering. The next proof move is manual/PDF row inspection for `00264#-AB-3`, `28655*-AA-7`, and `02300A-AA-8` before any asset-return claim is promoted.

