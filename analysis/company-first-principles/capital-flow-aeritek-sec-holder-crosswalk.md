# Capital Flow AeriTek SEC Holder Crosswalk

## Purpose

This pass applies the borrower-holder method to AeriTek.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-aeritek-sec-holder-crosswalk.csv`

## Question

`Can we turn the Ares selected-borrower AeriTek item into actual holder-level debt numbers?`

Yes.

AeriTek appears in multiple public credit-vehicle schedules:

- Ares Capital Corporation reports AeriTek revolver and first-lien term-loan rows in Q2 2026.
- Kayne Anderson BDC reports AeriTek first-lien loan exposure in Q3 2025, FY2025, and Q1 2026 filings.
- Ares Strategic Income Fund reports AeriTek revolver exposure in its Q1 2026 filing.

## Extracted Holder Rows

| Reporting Entity | Borrower Name | Period | Loan Type | Principal | Fair Value | Rate | Maturity |
|---|---|---|---|---:|---:|---|---|
| Ares Capital Corporation | AeriTek Global US Acquisition Inc., AeriTek Global Holdings LLC, and Minus Forty QBD Corp. | Q2 2026 | First lien senior secured revolving loan | `1.7M USD` | `1.7M USD` | `10.16% SOFR + 6.50%` | `08/2030` |
| Ares Capital Corporation | AeriTek Global US Acquisition Inc., AeriTek Global Holdings LLC, and Minus Forty QBD Corp. | Q2 2026 | First lien senior secured loans | `57.9M USD` | `57.9M USD` | mixed first-lien term-loan rows | `08/2030` |
| Kayne Anderson BDC | AeriTek Global Holdings LLC | Q1 2026 | First lien senior secured loan | `10.002M USD` | `10.002M USD` | `10.17% SOFR(Q) + 6.50%` | `08/27/2030` |
| Ares Strategic Income Fund | AeriTek Global US Acquisition Inc., AeriTek Global Holdings LLC, and Minus Forty QBD Corp. | Q1 2026 | First lien senior secured revolving loan | `1.7721M USD` | `1.7721M USD` | `10.17% SOFR(Q) + 6.50%` | `08/2030` |

The CSV also keeps Q3 2025, FY2025, and comparative rows so the history is visible without double-counting old balances as current exposure.

## Cleanest Number

The cleanest latest visible 2026 number is:

`59.6M USD ARCC Q2 2026 fair value + 10.002M USD Kayne Q1 2026 fair value + 1.7721M USD ASIF Q1 2026 fair value = 71.3741M USD`

That is visible holder exposure, not total AeriTek debt.

## Why This Matters

Before this pass, AeriTek was operating-context evidence:

- Ares listed AeriTek as a Q2 2026 selected U.S. direct-lending borrower.
- Mill Point says AeriTek acquired Continental Refrigerator and National Comfort Products, adding brands with more than `850` customers.
- The same follow-through source says it was AeriTek's third North American acquisition in less than eight months.

After this pass, AeriTek has lender-side debt evidence:

- ARCC discloses AeriTek first-lien exposure in Q2 2026.
- Kayne discloses AeriTek first-lien exposure around the same borrower and maturity.
- ASIF discloses an AeriTek revolver position, also at the same 2030 maturity.

## Claim Update

AeriTek strengthens this claim:

`Private credit is funding sponsor-backed acquisition platforms in commercial refrigeration and foodservice equipment, and the debt can be observed in SEC-filed holder schedules.`

It does not yet prove:

- Full acquisition financing size.
- Full lender group.
- Prior bank repayment.
- Whether the Ares Q2 2026 selected-borrower item was the same debt package as every holder row.
- How much of the borrowing funded acquisitions versus refinancing or working capital.

## What To Do Next

The next AeriTek questions are:

| Question | Evidence Needed |
|---|---|
| Was Ares' Q2 2026 role tied to the NRAC acquisition financing? | Financing announcement, counsel release, or rating-agency report. |
| Did banks have a prior or continuing role? | Credit agreement, UCC filings, administrative-agent references, or payoff language. |
| How much of the facility was drawn versus unfunded? | Holder commitment schedules with confirmed headings and full lender group disclosures. |
| Did the capital fund operating expansion or sponsor consolidation? | Acquisition timeline, purchase-price/use-of-proceeds evidence, and company operating metrics. |

## Simple Version

AeriTek is now more than a named Ares deal example.

We can show at least `71.3741M USD` of visible 2026 holder-level private-credit exposure across ARCC, Kayne Anderson BDC, and ASIF.

What we still cannot say is that this replaced a bank loan or equals the whole acquisition financing.
