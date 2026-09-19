# Capital Flow Precinmac SEC Holder Crosswalk

## Purpose

This pass repeats the Atwell SEC-holder method for Precinmac.

The question is:

`Can we find reported lender-side debt rows for another Ares selected direct-lending borrower?`

Crosswalk table:

`analysis/company-first-principles/data/capital-flow-precinmac-sec-holder-crosswalk.csv`

## Sources

| Source | Filing | Local Path |
|---|---|---|
| Senior Direct Lending Program LLC | FY2024 SEC exhibit / annual report schedule | `raw/primary-sources/capital-flow/precinmac/sec/sdlp-2024-annual-report-ex99-1.html` |
| Blue Owl Capital Corporation | FY2024 SEC 10-K HTML | `raw/primary-sources/capital-flow/precinmac/sec/obdc-2024-10k.html` |

The two filings use different borrower labels:

- SDLP: `Precinmac (US) Holdings Inc. and Trimaster Manufacturing Inc.`
- OBDC: `Paris US Holdco, Inc. (dba Precinmac)`

That distinction matters. The crosswalk treats them as Precinmac-related holder evidence, not as one confirmed identical facility.

## Sponsor / ownership context refresh

Precinmac's October 2024 acquisition announcement identifies Centerbridge as
the incoming owner and says the seller-side investor group included Pine Island
Capital Partners, Bain Capital's Private Credit Group, and Compass Partners
Capital. The announcement says financial terms of the private transaction were
not disclosed and does not describe debt, lender allocation, repayment, or
borrower cash.

This adds dated private-credit ownership context to the holder route. It does
not establish that Bain Capital Credit funded the current OBDC rows, that the
2026 Ares incremental commitment funded the acquisition, or that any bank was
replaced.

## Extracted Rows

| Reporting Entity | Borrower Label | Loan Type | Amount | Fair Value | Commitment | Rate | Maturity |
|---|---|---|---:|---:|---:|---|---|
| Senior Direct Lending Program LLC | Precinmac (US) Holdings Inc. and Trimaster Manufacturing Inc. | First lien senior secured loan | `256.1M USD` | `253.5M USD` |  | `11.5%` | `08/2027` |
| Blue Owl Capital Corporation | Paris US Holdco, Inc. (dba Precinmac) | First lien senior secured loan | `21.628M USD` | `21.412M USD` |  | SOFR + `5.00%` | `12/2031` |
| Blue Owl Capital Corporation | Paris US Holdco, Inc. (dba Precinmac) | First lien senior secured delayed draw term loan |  | `-0.028M USD` | `5.581M USD` | not disclosed in unfunded table | `12/2026` |
| Blue Owl Capital Corporation | Paris US Holdco, Inc. (dba Precinmac) | First lien senior secured revolving loan |  | `-0.028M USD` | `2.791M USD` | not disclosed in unfunded table | `12/2031` |

Combined disclosed funded/par exposure:

`277.728M USD`

Combined disclosed funded fair value:

`274.884M USD`

Combined disclosed unfunded commitments:

`8.372M USD`

## Claim Impact

Before this pass, Precinmac was mainly operating-context evidence:

`advanced manufacturing -> aerospace, defense, space, semiconductor, power -> 9 facilities`

After this pass, Precinmac has lender-side evidence too:

`Ares-linked SDLP holder row -> Blue Owl holder row -> funded debt plus unfunded commitments`

This is a stronger borrower-destination case than Atwell in one respect: the disclosed holder exposure is much larger.

But it is weaker in another respect: the extracted rows are FY2024 and do not prove the specific 2026 Ares selected-borrower transaction, incremental facility, or refinancing event.

## Current Q2 2026 holder refresh

The June 30, 2026 Blue Owl Capital Corporation Form 10-Q adds a current
holder snapshot under the Paris US Holdco, Inc. (dba Precinmac) name. It
reports four first-lien rows, all maturing December 2, 2031:

| Row marker | Par | Cost | Fair value | Pricing |
|---|---:|---:|---:|---|
| 1 | `$169.596M` | `$168.224M` | `$165.780M` | SOFR + `4.75%` |
| 2 | `$88.245M` | `$14.066M` | `$13.605M` | SOFR + `5.00%` |
| 3 | `$44.269M` | `$43.869M` | `$43.273M` | SOFR + `4.75%` |
| 4 | `$22.160M` | `$1.488M` | `$1.163M` | SOFR + `4.75%` |

The four reported rows sum to `$324.270M` par, `$227.647M` cost, and
`$223.821M` fair value. These are reported holder rows, not a promoted
funded-facility total: the unusual par-to-cost differences and footnotes must
be resolved before treating the rows as borrower-funded principal, and the
filing does not identify the full lender group, Ares allocation, borrower
receipt, use of proceeds, or bank payoff.

This is a current-period upgrade from the prior FY2024 crosswalk, not a bank-
replacement conclusion.

The ownership context remains separate from the current lender rows: sponsor
or seller identity is not a source-of-funds allocation.

## What This Proves

This proves:

- Precinmac-related borrower names appear in public credit-vehicle schedules.
- SDLP reported a `253.5M USD` fair-value first-lien Precinmac/Trimaster loan.
- OBDC reported a `21.412M USD` fair-value Paris US Holdco dba Precinmac first-lien loan.
- OBDC also reported `5.581M USD` delayed-draw and `2.791M USD` revolving unfunded commitments.

## What This Still Does Not Prove

This does not prove:

- Whether Ares' 2026 Precinmac selected-borrower item was a new loan, add-on, amendment, refinancing, or follow-on commitment.
- Whether any bank facility was repaid.
- Whether the SDLP and OBDC rows are parts of one facility or different credit structures.
- The full lender group.
- The full facility size after Centerbridge's 2024 acquisition and any later 2026 financing.

## Safer Claim

`Precinmac is now a stronger private-credit borrower-destination case because public credit-vehicle schedules disclose sizable first-lien debt exposure and unfunded commitments tied to Precinmac-related borrower names. It is not yet a bank-replacement case and not yet a 2026 transaction-use-of-proceeds case.`

## Simple Version

Precinmac gives us real debt numbers:

`274.884M USD of funded fair value plus 8.372M USD of unfunded commitments in the public holder rows captured so far.`

That makes it a strong example of private credit funding an industrial borrower.

It does not yet tell us whether banks were replaced.

## Source refresh

- [Precinmac announcement: acquisition by Centerbridge Partners](https://www.precinmac.com/news/precinmacacquired)
