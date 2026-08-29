# Capital Flow Relation SEC Holder Crosswalk

## Purpose

This pass applies the borrower-holder method to Relation Insurance.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-relation-sec-holder-crosswalk.csv`

## Question

`Can we turn the Ares selected-borrower Relation Insurance item into actual holder-level debt numbers?`

Yes for transaction linkage; partly for dollars.

Relation appears in SEC-filed credit-vehicle schedules under:

`AQ Sunshine, Inc. (dba Relation Insurance)`

The current evidence has two parts:

- Transaction evidence: Ares says it served as joint lead arranger and joint bookrunner for a senior secured credit facility supporting BayPine's acquisition of Relation Insurance.
- Holder evidence: Goldman Sachs BDC and Goldman Sachs Private Credit Corp. disclose Relation/AQ Sunshine debt or commitment rows.

The remaining weakness is the bridge between those two parts: the captured holder rows do not identify Ares allocation, the complete lender group, or a bank facility repayment, and they do not prove that the Goldman Sachs rows are the same facility as the BayPine/Ares transaction.

## Extracted Holder Rows

| Reporting Entity | Borrower Name | Period | Loan Type | Principal | Fair Value | Unfunded Commitment | Rate | Maturity |
|---|---|---|---|---:|---:|---:|---|---|
| Goldman Sachs BDC Inc. | AQ Sunshine, Inc. (dba Relation Insurance) | Q2 2026 | 1st Lien/Senior Secured Debt | `3.679M USD` | `3.661M USD` |  | `8.66% SOFR + 5.00%` | `07/24/33` |
| Goldman Sachs BDC Inc. | AQ Sunshine, Inc. (dba Relation Insurance) | Q2 2026 | 1st Lien/Senior Secured Debt | `0.826M USD` | `0.040M USD` |  | `8.74% SOFR + 5.00%` | `07/24/33` |
| Goldman Sachs BDC Inc. | AQ Sunshine, Inc. (dba Relation Insurance) | Q2 2026 | 1st Lien/Senior Secured Debt | `0.413M USD` | `-0.003M USD` |  | `SOFR + 5.00%` | `07/24/32` |
| Goldman Sachs BDC Inc. | AQ Sunshine, Inc. (dba Relation Insurance) | Q2 2026 | 1st Lien/Senior Secured Debt | `0.672M USD` | `0.669M USD` |  | `8.67% SOFR + 5.00%` | `07/24/31` |
| Goldman Sachs BDC Inc. | AQ Sunshine, Inc. (dba Relation Insurance) | Q2 2026 | 1st Lien/Senior Secured Debt | `0.285M USD` | `0.164M USD` |  | `8.67% SOFR + 5.00%` | `07/24/31` |
| Goldman Sachs BDC Inc. | AQ Sunshine, Inc. (dba Relation Insurance) | Q2 2026 | 1st Lien/Senior Secured Debt | `0.053M USD` | `0.017M USD` |  | `8.67% SOFR + 5.00%` | `07/24/30` |
| Goldman Sachs BDC Inc. | AQ Sunshine, Inc. (dba Relation Insurance) | Q2 2026 | Unfunded commitment |  |  | `1.196M USD` |  |  |
| Goldman Sachs Private Credit Corp. | AQ Sunshine, Inc. (dba Relation Insurance) | Q1 2026 | Unfunded commitment |  |  | `76.345M USD` |  |  |
| Goldman Sachs BDC Inc. | AQ Sunshine, Inc. (dba Relation Insurance) | Q1 2026 | Unfunded commitment |  |  | `4.738M USD` |  |  |
| Phillip Street Middle Market Lending Fund LLC | AQ Sunshine, Inc. (dba Relation Insurance) | FY2024 | 1st Lien/Senior Secured Debt | `37.673M USD` | `27.873M USD` |  | mixed SOFR spreads | `07/24/30` to `07/24/31` and `04/15/27` |

## Transaction Context

| Source | Date | What It Adds | Boundary |
|---|---|---|---|
| Ares Q2 2026 direct-lending origination release | July 31, 2026 | Ares identifies Relation Insurance / BayPine LP as a selected Q2 2026 transaction and says Ares was joint lead arranger and joint bookrunner for a senior secured credit facility supporting BayPine's acquisition. | No amount, pricing, maturity, lender allocation, or bank repayment disclosed. |
| Latham & Watkins financing note | February 18, 2026 | Latham says it represented the financing source supporting BayPine's acquisition of Relation and identifies Hybrid Capital plus Banking & Private Credit teams. | Does not name Ares or disclose the debt terms. |
| BayPine acquisition announcement | February 18, 2026 | BayPine confirms the acquisition agreement and gives operating scale: more than `90` offices, more than `230,000` clients, more than `1,000` insurance markets, and about `1,400` employees. | Financial terms were not disclosed. |

## Cleanest Number

The cleanest latest visible funded number is:

`4.548M USD`

That is the net Q2 2026 fair value across the six GSBD funded Relation/AQ Sunshine rows.

The separate current commitment trail is:

`76.345M USD GSPCC Q1 2026 unfunded commitment + 1.196M USD GSBD Q2 2026 unfunded commitment = 77.541M USD`

That commitment figure is mixed-quarter and should not be combined with funded fair value as if it were drawn debt.

## Why This Matters

Before this pass, Relation was only a named Ares selected direct-lending borrower.

After this pass, Relation has transaction-context plus lender-side debt and commitment evidence:

- Ares says the facility supported BayPine's acquisition of Relation.
- Latham confirms a financing source supported the BayPine acquisition.
- BayPine confirms the transaction and the operating-company scale.
- GSBD discloses current Q2 2026 first-lien debt rows with `4.548M USD` of net fair value.
- GSPCC discloses a much larger Q1 2026 unfunded commitment of `76.345M USD`.
- GSBD discloses Q1 2026 and Q2 2026 commitment rows, showing current lender-side capacity changed during 2026.
- Phillip Street gives historical FY2024 first-lien debt exposure of `27.873M USD` fair value.

## Claim Update

Relation strengthens this claim:

`Private credit is supporting insurance-brokerage consolidation platforms; Relation now has named Ares acquisition-financing evidence plus separate SEC-filed holder and commitment evidence.`

It does not yet prove:

- The full Relation facility size.
- Ares' funded amount.
- Whether the Q2 2026 Ares selected-borrower item was a new deal, amendment, add-on, or refinancing.
- Whether private credit replaced a bank facility.
- Whether the Goldman Sachs rows are the same debt package as the Ares/BayPine transaction.

## What To Do Next

The next Relation questions are:

| Question | Evidence Needed |
|---|---|
| Is the 07/24/33 debt connected to the BayPine/Ares 2026 transaction? | Credit agreement, rating report, amendment, lender allocation schedule, or holder footnote linking AQ Sunshine/Relation to the BayPine acquisition financing. |
| What is the full facility size? | Total debt commitment, rating-agency capital-structure table, or agent/lender allocation schedule. |
| Were banks repaid or retained? | Payoff, termination, amendment, UCC, or credit agreement evidence. |
| What did proceeds fund? | Acquisition close release, use-of-proceeds language, or borrower transaction documents. |

## Simple Version

Relation is now more than a named Ares borrower.

We can show Ares was a joint lead arranger/bookrunner for acquisition financing, and separately show `4.548M USD` of current GSBD funded fair value plus `77.541M USD` of mixed-quarter visible 2026 unfunded commitments.

What we still cannot say is that this is the whole Relation financing, that it is Ares' exact amount, or that it replaced bank credit.
