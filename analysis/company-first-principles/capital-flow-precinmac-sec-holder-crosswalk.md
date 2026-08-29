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
