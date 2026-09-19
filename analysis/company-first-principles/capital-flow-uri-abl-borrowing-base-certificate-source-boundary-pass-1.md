# Capital Flow URI ABL Borrowing-Base Certificate Source Boundary Pass 1

## Purpose

This pass answers the next narrow URI question:

`Does the filed ABL agreement include the actual Borrowing Base Certificate form or live certificate values?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-abl-borrowing-base-certificate-source-boundary-pass-1.csv`

## Source

This pass uses the actual July `2025` ABL agreement:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-07-11-tm2520569d1_ex10-1.htm`

## What We Found

The agreement references a Borrowing Base Certificate substantially in the form of `Exhibit A` or another form reasonably acceptable to the Agent.

The filed text we have does not expose a populated `Exhibit A` certificate form or live certificate table.

That is a boundary, not a dead end.

The agreement also states that the Agent and Lenders received a Borrowing Base Certificate prepared as of the last business day of the calendar month ended May `31`, `2025` as a closing condition. It also required Combined Availability at closing, after giving effect to the transaction, to be at least `1.000B USD`.

## Required Certificate Fields

The agreement lets us specify the fields the missing certificate or equivalent report must contain.

| Required Field | Why It Is Required | Current Status |
|---|---|---|
| U.S. Borrowing Base | Certificate definition requires U.S. base calculation and components. | Field required; live value missing. |
| Canadian Borrowing Base | Certificate definition requires Canadian base calculation and components. | Field required; live value missing. |
| Eligible merchandise and consumables inventory value | U.S. formula uses `60%` of eligible value. | Field required; live value missing. |
| Eligible rental equipment net book value | Rental-equipment formula uses `100%` NBV limiter. | Field required; live value missing. |
| Eligible rental equipment NOLV | Rental-equipment formula uses `85%` NOLV limiter. | Field required; live value missing. |
| Pari passu debt reserves | U.S. and Canadian formulas subtract these reserves. | Field required; live value missing. |
| Other reserves / availability reserves | Formulas and Section `2.9` allow reserve deductions. | Field required; live value missing. |
| Aggregate revolver outstandings | Combined Availability subtracts outstandings. | Field required; live value missing. |
| Maximum Revolver Amount / Canadian maximum | Combined Availability and Combined Borrowing Base require cap values. | Field required; cap definitions visible. |
| Combined Borrowing Base | Output of U.S. and Canadian base calculation. | Field required; live value missing. |
| Combined Availability | Legal availability bridge output. | Field required; reset snapshot and closing minimum visible, live value missing. |
| Suppressed Availability | Combined Borrowing Base less Maximum Revolver Amount. | Field required for excess collateral cushion; live value missing. |

## Control Clues

The agreement adds several controls around those fields:

- eligibility, reserve, sublimit, or advance-rate changes that increase Combined Availability or a Borrowing Base require Supermajority Lender and Borrower consent
- the Agent has discretion over applicability of ineligibility criteria for U.S. and Canadian borrowing-base calculations
- collateral releases require updating the U.S. or Canadian borrowing base to delete released assets and preserve availability
- the May `31`, `2025` certificate existed in the closing package, but the filed exhibit text does not include its values

## What This Adds

This moves the URI ABL work from:

`borrowing-base-definition-visible`

to:

`certificate-field-map-visible`

It still does not make URI borrowing-base-grade.

The difference is:

- We now know the exact certificate/report fields to pursue.
- We do not yet have the certificate values.

## Safe Claim

`URI's filed ABL agreement does not expose the live Borrowing Base Certificate values, but it proves that a May 31 2025 certificate was delivered to the Agent and Lenders as a closing condition and that closing Combined Availability had to be at least 1.000B USD. The missing certificate should bridge eligible inventory, eligible rental-equipment NBV, eligible rental-equipment NOLV, reserves, revolver outstandings, facility caps, Combined Borrowing Base, Combined Availability, and Suppressed Availability.`

## September 18, 2026 SEC-route recheck

The filed [Fifth Amended and Restated Credit Agreement](https://www.sec.gov/Archives/edgar/data/1047166/000110465925067406/tm2520569d1_ex10-1.htm)
was rechecked for an attached or populated certificate. It confirms that
Exhibit A is the form of Borrowing Base Certificate; the agreement defines the
certificate as a component-by-component calculation of the U.S. and Canadian
borrowing bases; and it requires quarter-end certificates beginning June 30,
2025, with additional monthly certificates under the specified availability
trigger. The agreement also states that the Agent and Lenders received a May
31, 2025 certificate as a closing condition.

No live Exhibit A values, lender collateral report, or Q2 2026 certificate was
found in the filed SEC exhibit. This sharpens the acquisition boundary:

`legal certificate regime and closing-delivery fact visible; populated
certificate remains agent/lender-controlled and URI borrowing-base promotion
still unproven.`

The local SEC HTML inspection makes the omission more precise. `FORM OF
BORROWING BASE CERTIFICATE` appears in the agreement's exhibits-and-schedules
table of contents, but it does not reappear in the body as an attached exhibit;
the filing proceeds from the agreement and schedules to the signature pages.
The document therefore proves that Exhibit A is named and incorporated into the
credit-agreement architecture, not that the exhibit's field layout or any live
values were filed. This is a searched-negative about the checked SEC exhibit,
not a claim that the Agent or Lenders do not possess the form or certificates.

The related July 11, 2025 Form 8-K exhibit index narrows the public submission
perimeter further: it lists only Exhibit 10.1 (the credit agreement), Exhibit
10.2 (the U.S. security agreement), and Exhibit 10.3 (the Canadian security
agreement). Neither security-agreement companion contains a Borrowing Base
Certificate or a populated collateral-availability schedule. Thus there is no
separate certificate attachment hiding among the related exhibits in this
submission.

## Claims Not To Make Yet

Do not say:

- we have the May `31`, `2025` certificate values
- the current Q2 `2026` borrowing-base certificate is public
- the current legal availability is proven
- eligible collateral dollars are known
- reserves are known
- appraisal values are known
- all OEC is eligible collateral

## Next Concrete Work

The next URI evidence gates are:

1. Search for rating-agency reports or lender disclosures that cite borrowing-base or collateral-coverage values.
2. Search later 10-Q/10-K debt notes for availability language that can be reconciled to agreement-defined Combined Availability.
3. Look for any future URI 8-K exhibits that include certificate forms, amendments, or collateral schedules.
4. If no certificate is public, build a bounded proxy bridge from Q2 `2026` disclosed ABL balance, liquidity, fleet OEC, AR securitization collateral, and agreement formula fields while labeling it proxy-only.

The immediate public-disclosure proxy bridge is:

`analysis/company-first-principles/capital-flow-uri-abl-public-disclosure-proxy-bridge-pass-1.md`
