# Capital Flow Apollo Athene Aristotle Mixed Row Resolution Pass 1

## Purpose

This pass executes the first next action from:

`/cluster/capital-flow-apollo-athene-row-level-proof-packet-pass-1.md`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-aristotle-mixed-row-resolution-pass-1.csv`

The question is:

`Can AP Aristotle be separated into cash-like and noncash buckets before it is used as the largest Apollo/Athene row-level proof target?`

## Short Answer

Yes.

AP Aristotle can now be separated into:

| Bucket | Amount |
|---|---:|
| Cash-like consideration candidate | `776.032348M USD` |
| Noncash / tax-free-exchange hold | `6.588486M USD` |
| Disposal interest/dividends on cash-like rows | `11.663548M USD` |
| Disposal interest/dividends on noncash hold row | `38.433K USD` |

That is useful, but it is not final cash proof.

The safe current status is:

`mixed_row_resolution_complete_cash_proof_hold`

In simple words:

`AP Aristotle is still the biggest Apollo/Athene named-row candidate, but only the paydown and Various rows should be carried forward as cash-like consideration candidates. The tax-free exchange row stays out of the cash bucket. Gain/loss, settlement, borrower use, allocation, liability spread, and return remain unproved.`

## Row-Level Split

| Source Row | Page | Label | Safe Consideration | Interest / Dividends | Resolution |
|---|---:|---|---:|---:|---|
| `CFAASDFR-8588` | `6025` | year-end holding | n/a | `28.317574M USD` parser received-interest field | holding context visible |
| `CFAASDDP-06154` | `6279` | Paydown | `250.704550M USD` | `5.270263M USD` | cash-like candidate |
| `CFAASDDP-06157` | `6279` | Various | `525.327798M USD` | `6.393285M USD` | cash-like candidate |
| `CFAASDDP-07636` | `6334` | Interest Capitalization / Tax Free Exchange | `6.588486M USD` | `38.433K USD` | noncash/transfer hold |

## What Gets Promoted

Only this gets promoted:

`250.704550M USD + 525.327798M USD = 776.032348M USD cash-like AP Aristotle consideration candidate`

That means AP Aristotle remains eligible for a source-acquisition packet.

The target documents are:

1. AP Aristotle note purchase or offering documents
2. borrower/use support
3. paydown or repayment notice
4. counterparty or transaction support for the `Various` row
5. Athene allocation or custodian support
6. liability-cost schedule

## What Stays Held

The `6.588486M USD` tax-free-exchange row stays out of the cash-like bucket.

Gain/loss also stays held.

Why:

The column interpretation pass already showed that the current parser can safely confirm consideration for the selected rows, but gain/loss fields are not safe where repeated consideration-like tokens may have shifted into gain/loss positions.

So the safe AP Aristotle treatment is:

| Field | Status |
|---|---|
| named CUSIP and issuer | visible |
| year-end holding | visible |
| book value | visible, still subject to full parser reconciliation |
| cash-like consideration | visible for two rows |
| tax-free exchange | visible and excluded from cash bucket |
| gain/loss | held |
| borrower receipt | missing |
| borrower use | missing |
| Athene allocation/custodian cash | missing |
| liability-cost spread | missing |
| final return | missing |

## Why This Matters

Before this pass, AP Aristotle was both attractive and risky.

Attractive because it is the largest selected Apollo/Athene same-CUSIP cash-like candidate.

Risky because the same CUSIP also carried tax-free-exchange evidence.

This pass makes the treatment cleaner:

`cash-like paydown/sale bucket separated from noncash/tax-free exchange bucket`

That prevents a sloppy claim like:

`AP Aristotle proved 782.620834M USD of cash return.`

That is too broad.

The safer statement is:

`AP Aristotle has 776.032348M USD of cash-like consideration candidates and 6.588486M USD of tax-free-exchange/noncash hold evidence in the selected statutory rows.`

## What This Proves

This pass proves:

1. the AP Aristotle holding row is visible in the Athene statutory packet
2. the AP Aristotle paydown row can be kept as a cash-like consideration candidate
3. the AP Aristotle Various row can be kept as a cash-like consideration candidate
4. the AP Aristotle tax-free-exchange row must remain a noncash hold
5. the cash-like bucket and noncash bucket should not be merged

## What This Does Not Prove

This pass does not prove:

1. actual bank settlement
2. borrower receipt
3. borrower use of proceeds
4. noteholder remittance
5. Athene-specific allocation or custodian cash movement
6. lot-level continuity
7. realized gain/loss
8. liability-cost spread
9. IRR, NPV, ROIC, cash-on-cash return, or platform profit

## Next Action

The next artifact should be:

`capital-flow-apollo-athene-aristotle-source-acquisition-packet-pass-1.md`

That pass should search or request:

| Source | Why |
|---|---|
| AP Aristotle note purchase or offering document | Identifies the instrument and financing terms. |
| borrower/use evidence | Shows what the original financing funded. |
| paydown or repayment notice | Tests whether paydown cash is real and how it moved. |
| transaction or counterparty support for `Various` row | Clarifies whether this was sale, transfer, repayment, or other counterparty movement. |
| Athene allocation/custodian support | Proves whether cash moved to Athene or only appears in statutory accounting. |
| liability-cost schedule | Needed for spread/return comparison. |
| return model | Needed before any final investment-return claim. |

## Safe Claim

`AP Aristotle is now resolved for proof-targeting but not promoted to full cash proof. The selected Athene statutory rows support 776.032348M USD of cash-like AP Aristotle consideration candidates across a Paydown row and a Various row, while 6.588486M USD tied to Interest Capitalization / Tax Free Exchange remains a noncash or transfer hold. This supports a source-acquisition packet, not borrower receipt, settlement cash, Athene allocation, liability-cost spread, realized gain/loss, or final return.`

## Decision

`apollo-athene-aristotle-mixed-row-resolution-ready-source-acquisition-packet`
