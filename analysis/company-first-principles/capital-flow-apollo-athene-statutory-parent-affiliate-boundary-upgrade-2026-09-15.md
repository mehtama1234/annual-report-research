# Apollo–Athene statutory parent-affiliate boundary upgrade

Research date: `2026-09-15`

## Purpose

This pass tightens the parent-access question using Athene Annuity and Life
Company's 2025 statutory statement. It records the legal-entity receivable and
payable balances involving the parent, subsidiaries, and affiliates, then
separates those balances from cash-flow lines that cannot be attributed to
Apollo HoldCo.

Primary source:

`raw/primary-sources/capital-flow/apollo/athene/statutory/2025/athene-annuity-and-life-company-2025-statutory-statement.pdf`

Relevant pages are the statutory assets page `3`, liabilities page `4`, and
cash-flow pages `6–7`.

## Evidence

| Boundary | 2025 | 2024 | Safe interpretation |
| --- | ---: | ---: | --- |
| Receivables from parent, subsidiaries, and affiliates, assets page 3 line 23 | `$4.553M` | `$22.537M` | Athene had a separately reported current receivable bucket from related entities; it is not a dated Apollo receipt or dividend. |
| Payable to parent, subsidiaries, and affiliates, liabilities page 4 line 24.04 | `$142.863M` | `$52.270M` | Athene had a separately reported current payable bucket to related entities; it is not proof of the recipient, settlement date, or unrestricted parent cash. |
| Cash-flow line 16.5, dividends to stockholders | blank / no amount reported | blank / no amount reported | The statutory cash-flow page does not provide a quantified stockholder-dividend line that can be used as an Apollo receipt. |
| Cash-flow line 16.6, other cash provided/applied | `$11.331B` | `$53.921B` | Aggregate residual financing/miscellaneous cash line; it cannot be assigned to Apollo, NCI, policyholders, or a named asset without a subsidiary ledger. |
| Supplemental intercompany tax settlement, page 7 line 20.0019 | `$415.722M` operating | — | An intercompany cash/tax mechanism is visible, but its payer, recipient, elimination, and HoldCo availability are not identified in this statement. |

## What this proves

1. The statutory legal entity has explicit related-party balance-sheet
   buckets, distinct from unrestricted cash.
2. The related-party payable grew by `$90.592M` year over year, while the
   related-party receivable declined by `$17.984M`.
3. The statement contains aggregate cash-flow lines and an intercompany tax
   settlement, but not a dated Athene-to-Apollo receipt line.
4. A parent-access model must join the statutory subsidiary ledger, dividend
   declaration/approval, intercompany elimination, receiving-account cash, and
   common-owner claims before calling cash distributable.

## Deliberate boundary

This does not prove that Apollo received no cash. It proves only that this
Athene statutory statement does not identify a dated Apollo receipt or a
common-owner residual. Receivables, payables, and the `$11.331B` other-cash
line must not be relabeled as parent cash.

The correct grade is `statutory-parent-affiliate-boundary-visible`.

The structured row is promoted into the canonical Apollo ledger as `APO-073`.

## Next upgrade

Join Athene dividend declarations and legal-capacity schedules to an Apollo
parent-only cash-flow or intercompany ledger. The decisive proof is a dated
receiving-account entry or an elimination schedule that identifies the amount
available to Apollo common owners after NCI, preferred claims, debt, tax, and
regulatory constraints.
