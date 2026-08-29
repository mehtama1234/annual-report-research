# Capital Flow URI Yak Senior-Note Terms Pass 1

## Purpose

This pass upgrades the Yak funding chain from instrument-level visibility to senior-note term visibility.

It answers:

`What were the actual terms of the debt URI used to finance Yak, and what remains unresolved?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-yak-senior-note-terms-pass-1.csv`

## Source Boundary

This pass uses official URI and SEC sources:

- URI March `7`, `2024` note pricing announcement
- SEC Exhibit `4.1` indenture dated March `11`, `2024`
- URI Q3 `2024` 10-Q debt note
- `capital-flow-uri-yak-acquisition-funding-chain-pass-1.md`

This pass is:

`yak-senior-note-terms-visible`

It is not:

`note-investor-allocation-visible`

or:

`full-purchase-source-and-use-visible`

## Term Sheet

| Term | Evidence |
|---|---|
| Issuer | United Rentals (North America), Inc. |
| Parent / guarantor framework | Guaranteed on a senior unsecured basis by URI and certain domestic subsidiaries. |
| Trustee | Truist Bank. |
| Principal amount | `1.100B USD` issued on the issue date. |
| Coupon | `6.125%` per annum. |
| Maturity | March `15`, `2034`. |
| Interest payment dates | March `15` and September `15`, starting September `15`, `2024`. |
| Estimated net proceeds | `1.090B USD` after initial purchasers' discounts, commissions, and estimated fees/expenses. |
| Offering format | Private offering under Rule `144A` / Regulation `S` exemptions. |
| Expected use of proceeds | Net proceeds plus ABL borrowings to finance Yak and related fees/expenses. |
| Optional redemption start | March `15`, `2029`. |
| 2029 redemption price | `103.063%` of principal plus accrued/unpaid interest. |
| 2030 redemption price | `102.042%` of principal plus accrued/unpaid interest. |
| 2031 redemption price | `101.021%` of principal plus accrued/unpaid interest. |
| 2032+ redemption price | `100.000%` of principal plus accrued/unpaid interest. |
| Equity claw | Up to `40.0%` of principal at `106.125%` on or before March `15`, `2027`, subject to conditions. |
| Change-of-control purchase price | `101%` of principal plus accrued/unpaid interest. |
| Yak special mandatory redemption | If Yak did not close by the deadline or the purchase agreement terminated, redemption at `100%` plus accrued/unpaid interest. |
| Q3 2024 carrying amount | `1.090B USD` in the Q3 `2024` debt table. |

## What This Adds

The prior Yak funding-chain pass showed:

`senior notes + ABL drawings -> Yak acquisition`

This pass shows the note was not a generic debt plug. It was a named `6.125%` senior unsecured note due `2034`, with indenture terms, trustee, guarantees, redemption provisions, private-offering status, expected net proceeds, and a Yak-specific special mandatory redemption provision.

That makes the funding chain more precise:

`Rule 144A / Reg S senior unsecured note -> 1.090B USD estimated net proceeds + ABL borrowings -> Yak acquisition and related fees`

## What Still Is Missing

The note terms still do not show:

- initial purchaser names
- investor allocation
- exact pricing spread or yield
- exact ABL draw amount
- closing-date source-and-use schedule
- borrowing-base availability at the Yak close
- whether subsequent ABL repayment/refinancing changed the effective funding mix
- ongoing Matting category ROIC

## Safe Claim

`URI's Yak note financing is now senior-note-term-visible: URNA priced 1.100B USD of 6.125% Senior Notes due March 15 2034, with estimated net proceeds of about 1.090B USD, senior unsecured guarantees by URI and certain domestic subsidiaries, Truist Bank as trustee, semiannual interest payments, optional redemption beginning March 15 2029, a 40.0% equity-claw path at 106.125% through March 15 2027, and a Yak-specific special mandatory redemption if the acquisition failed to close. The notes plus ABL borrowings funded Yak and related fees, but exact ABL draw allocation and full closing source-and-use remain undisclosed.`

## Claims Not To Make Yet

Do not say:

- the exact ABL draw amount is known
- the note buyer allocation is known
- the note offering document proves post-acquisition Matting ROIC
- the notes funded only acquired rental equipment
- the private offering terms prove a market-wide financing pattern by themselves
- estimated net proceeds equal total acquisition funding
- Q3 `2024` carrying amount equals cash proceeds

## Next Concrete Work

The next evidence gates are:

1. Use `capital-flow-uri-yak-rating-context-pass-1.md` for S&P rating-headline and recovery context.
2. Use `capital-flow-uri-yak-initial-purchaser-source-boundary-pass-1.md` for initial-purchaser role visibility.
3. Use `capital-flow-uri-yak-bond-identifier-market-data-boundary-pass-1.md` for CUSIP/ISIN/FIGI, current quote, and later holder-trace boundaries.
4. Use `capital-flow-uri-yak-public-holder-crosswalk-pass-1.md` for first later public holder traces.
5. Use `capital-flow-uri-yak-original-pricing-source-boundary-pass-1.md` for original price/yield/spread boundary.
6. Find the note offering memorandum or pricing supplement if public or cached by a source.
7. Identify named initial purchasers from any 8-K, offering material, rating report, purchase agreement, or transaction database.
8. Search for March `2024` ABL availability or draw schedule.
9. Track later filings for repayment/refinancing of Yak-related ABL draws.
