# Capital Flow Sunvair SEC Holder Crosswalk

## Purpose

This pass applies the borrower-holder method to Sunvair Aerospace Group.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-sunvair-sec-holder-crosswalk.csv`

## Question

`Can we turn the Ares selected-borrower Sunvair item into actual holder-level debt numbers?`

Yes.

Sunvair appears in multiple public credit-vehicle schedules:

- Ares Capital Corporation reports Sunvair revolver and first-lien term-loan rows in Q2 2026.
- Ares Strategic Income Fund reports Sunvair revolver and first-lien loan rows in Q1 2026.
- CION Ares Diversified Credit Fund reports Sunvair revolver, term-loan, and delayed-draw rows in Q1 2026.

## Extracted Holder Rows

| Reporting Entity | Borrower Name | Period | Loan Type | Principal | Fair Value | Rate | Maturity |
|---|---|---|---|---:|---:|---|---|
| Ares Capital Corporation | Sunvair Aerospace Group Inc. and GB Helios Holdings L.P. | Q2 2026 | First lien senior secured revolving loan | `0.7M USD` | `0.7M USD` | `8.66% SOFR(Q) + 5.00%` | `05/2031` |
| Ares Capital Corporation | Sunvair Aerospace Group Inc. and GB Helios Holdings L.P. | Q2 2026 | First lien senior secured loans | `67.4M USD` | `67.4M USD` | mixed first-lien term-loan rows | `05/2031` |
| Ares Strategic Income Fund | Sunvair Aerospace Group Inc. and GB Helios Holdings L.P. | Q1 2026 | First lien senior secured revolving loan | `0.9833M USD` | `0.9833M USD` | `8.67% SOFR(Q) + 5.00%` | `05/2031` |
| Ares Strategic Income Fund | Sunvair Aerospace Group Inc. and GB Helios Holdings L.P. | Q1 2026 | First lien senior secured loan | `34.7671M USD` | `34.7671M USD` | `8.67% SOFR(Q) + 5.00%` | `05/2031` |
| CION Ares Diversified Credit Fund | Sunvair Aerospace Group Inc. | Q1 2026 | 1st Lien Revolving Loan | `0.087M USD` | `0.087M USD` | `8.67% SOFR(Q) + 5.00%` | `05/2031` |
| CION Ares Diversified Credit Fund | Sunvair Aerospace Group Inc. | Q1 2026 | 1st Lien Term Loan | `1.747M USD` | `1.746M USD` | `8.69% SOFR(Q) + 5.00%` | `05/2031` |
| CION Ares Diversified Credit Fund | Sunvair Aerospace Group Inc. | Q1 2026 | 1st Lien Delay Draw Term Loan | `0.691M USD` | `0.691M USD` | `8.69% SOFR(Q) + 5.00%` | `05/2031` |

The CSV also keeps ASIF 2024 and 2025 rows so the holder history is visible without double-counting prior periods.

## Cleanest Number

The cleanest latest visible 2026 number is:

`68.1M USD ARCC Q2 2026 fair value + 35.7504M USD ASIF Q1 2026 fair value + 2.524M USD CADCX Q1 2026 fair value = 106.3744M USD`

That is visible holder exposure, not total Sunvair debt.

## Why This Matters

Before this pass, Sunvair was operating-context evidence:

- Ares listed Sunvair as a Q2 2026 selected U.S. direct-lending borrower.
- The selected-borrower map classifies it as aerospace MRO services.

After this pass, Sunvair has lender-side debt evidence:

- ARCC discloses Sunvair first-lien exposure in Q2 2026.
- ASIF discloses Sunvair first-lien and revolver exposure in Q1 2026.
- CADCX discloses smaller Sunvair first-lien, revolver, and delayed-draw exposure in Q1 2026.

## Claim Update

Sunvair strengthens this claim:

`Private credit is funding aerospace maintenance, repair, and overhaul service platforms, and the debt can be observed in SEC-filed holder schedules.`

It does not yet prove:

- Total facility size.
- Full lender group.
- Prior bank repayment.
- Whether the Ares Q2 2026 selected-borrower item was an amendment, add-on, refinancing, or new money.
- How much borrowing funded acquisitions, organic capacity, refinancing, or working capital.

## What To Do Next

The next Sunvair questions are:

| Question | Evidence Needed |
|---|---|
| What happened in May 2024 when the 05/2031 debt first appears? | Sponsor release, rating-agency report, counsel release, or credit agreement. |
| Was the Q2 2026 Ares selected-borrower item an add-on or refinancing? | Ares deal note, amendment filing, rating update, or sponsor/company announcement. |
| Did banks have a prior or continuing role? | UCC filings, agent/lender list, payoff language, or bank-led revolver disclosure. |
| Does the financing support aerospace operating capacity? | Facility, repair-line, customer, capex, backlog, or acquisition evidence. |

## Simple Version

Sunvair is now more than a named Ares deal example.

We can show at least `106.3744M USD` of visible 2026 holder-level private-credit exposure across ARCC, ASIF, and CADCX.

What we still cannot say is that this replaced a bank loan or equals the whole facility.
