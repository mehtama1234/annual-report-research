# Capital Flow Frontline SEC Holder Crosswalk

## Purpose

This pass applies the borrower-holder method to Frontline Road Safety.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-frontline-sec-holder-crosswalk.csv`

## Question

`Can we turn the Ares selected-borrower Frontline item into actual holder-level debt numbers?`

Yes.

Frontline appears in SEC-filed credit-vehicle schedules under:

- `Frontline Road Safety LLC`
- `Frontline Road Safety Operations, LLC`

The current evidence is strong for holder-level exposure and operating destination. It is still weak for bank-displacement language because none of the captured sources proves a prior bank payoff, termination, or post-close lender-role map.

## Extracted Holder Rows

| Reporting Entity | Borrower Name | Period | Loan Type | Principal | Fair Value | Unfunded Commitment | Rate | Maturity |
|---|---|---|---|---:|---:|---:|---|---|
| FS KKR Capital Corp. | Frontline Road Safety LLC | Q2 2026 | First-lien senior secured loans | `136.7M USD` | `132.8M USD` |  | SOFR + `4.8%` to `5.0%`; selected PIK rows | `03/2032` |
| KKR FS Income Trust Select | Frontline Road Safety LLC | Q2 2026 | First-lien senior secured loans | `48.723M USD` | `47.936M USD` |  | SOFR + `4.8%` to `5.0%`; selected PIK rows | `03/2032` |
| Goldman Sachs BDC Inc. | Frontline Road Safety Operations LLC | Q2 2026 | First-lien senior secured loans | `19.222M USD` | `17.939M USD` |  | SOFR + `4.75%`; selected PIK rows | `03/04/32` |
| Ares Strategic Income Fund | Frontline Road Safety Operations LLC | Q1 2026 | First-lien senior secured loan | `76.6927M USD` | `76.6927M USD` |  | `8.72%` with `2.00%` PIK; SOFR(M) + `5.00%` | `03/2032` |
| Goldman Sachs Private Credit Corp. | Frontline Road Safety Operations LLC | Q1 2026 | Unfunded commitment |  |  | `53.688M USD` |  |  |
| Goldman Sachs BDC Inc. | Frontline Road Safety Operations LLC | Q2 2026 | Unfunded commitment |  |  | `0.612M USD` |  |  |

## Cleanest Number

The cleanest latest Q2 2026 funded number is:

`132.8M USD FSK + 47.936M USD K-FITS + 17.939M USD GSBD = 198.675M USD`

That is visible holder exposure, not total Frontline debt.

The broader mixed-quarter 2026 funded view is:

`198.675M USD latest Q2 holder fair value + 76.6927M USD ASIF Q1 fair value = 275.3677M USD`

That broader number is useful for showing cross-manager reach, but it is not a same-date portfolio total.

The separate visible commitment trail is:

`53.688M USD GSPCC Q1 2026 unfunded commitment + 0.612M USD GSBD Q2 2026 unfunded commitment = 54.3M USD`

## Transaction Context

| Source | Date | What It Adds | Boundary |
|---|---|---|---|
| Ares Q2 2026 direct-lending origination release | July 31, 2026 | Ares identifies Frontline Road Safety Holdings / Bain Capital as a selected Q2 2026 transaction and says Ares was lead arranger and bookrunner for a senior secured facility supporting Bain's continued growth plans for Frontline. | No amount, pricing, maturity, lender allocation, or bank repayment disclosed. |
| Bain Capital announcement | January 30, 2025 | Bain says it agreed to acquire Frontline from Sterling; Frontline was the largest U.S. pavement-marking services provider, had over `50` locations, and had approximately `1,750` employees. | Financial terms were not disclosed and the release does not identify debt financing terms. |
| Sterling sale-completion announcement | March 5, 2025 | Sterling confirms completion of the sale to Bain and describes Frontline as the largest U.S. provider of pavement marking and ancillary services. | Operating and sponsor-transaction context only. |

## Why This Matters

Before this pass, Frontline was operating-context evidence in Ares' selected-borrower list.

After this pass, Frontline has lender-side debt evidence:

- FSK discloses `132.8M USD` of current Q2 2026 Frontline fair value.
- K-FITS discloses `47.936M USD` of current Q2 2026 Frontline fair value.
- GSBD discloses `17.939M USD` of current Q2 2026 Frontline fair value.
- ASIF discloses `76.6927M USD` of Q1 2026 Frontline fair value.
- GSPCC and GSBD disclose visible 2026 unfunded commitments.

## Claim Update

Frontline strengthens this claim:

`Private credit is funding infrastructure-adjacent roadway safety services, and the exposure can be observed in SEC-filed holder schedules.`

It does not yet prove:

- Total facility size.
- Ares' funded amount.
- Full lender group.
- Whether the Ares Q2 2026 item was an add-on, amendment, or refinancing.
- Whether private credit replaced bank credit.
- Whether proceeds funded acquisitions, organic growth, capex, or liquidity.

## What To Do Next

The next Frontline questions are:

| Question | Evidence Needed |
|---|---|
| What happened around March 2025 and the March 2032 maturity debt package? | Credit agreement, rating report, counsel release, lender announcement, or capital-structure table. |
| Did the Ares Q2 2026 item add onto an existing 2025 facility? | Amendment, incremental facility notice, rating update, or holder schedule with acquisition-date detail. |
| Were banks repaid or retained? | Payoff, termination, amendment, UCC, or lender-role evidence. |
| What did proceeds fund? | Use-of-proceeds language, acquisition releases, capex plan, or working-capital disclosure. |

## Simple Version

Frontline is now a strong borrower-destination case.

We can show `198.675M USD` of latest Q2 2026 funded fair value across FSK, K-FITS, and GSBD, plus another `76.6927M USD` ASIF Q1 holder row.

What we still cannot say is that this is the whole facility, that it is Ares' exact amount, or that it replaced bank credit.
