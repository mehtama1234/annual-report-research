# Capital Flow Valcourt SEC Holder Crosswalk

## Purpose

This pass applies the Atwell and Precinmac SEC-holder method to Valcourt.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-valcourt-sec-holder-crosswalk.csv`

## Question

`Can we move Valcourt from an Ares selected-borrower mention into real holder-level debt numbers?`

Yes, with boundaries.

Valcourt appears in multiple public credit-vehicle schedules:

- Senior Direct Lending Program LLC reports Valcourt first-lien exposure in FY2024, Q4 2025, and Q1 2026 exhibits.
- Ares Capital Corporation reports a separate Valcourt/Jobs first-lien position in its Q2 2026 10-Q.
- Cliffwater Corporate Lending Fund reports earlier Valcourt first-lien, delayed-draw, and revolver exposure in an N-PORT-derived schedule.

## Extracted Holder Rows

| Reporting Entity | Borrower Name | Period | Loan Type | Par / Principal | Fair Value | Commitment | Rate | Maturity |
|---|---|---|---|---:|---:|---:|---|---|
| Senior Direct Lending Program LLC | Valcourt Holdings II LLC and Jobs Holdings Inc. | FY2024 | First lien senior secured loan | `325.9M USD` | `325.9M USD` |  | `10.4%` | `11/2029` |
| Senior Direct Lending Program LLC / Ares Capital exhibit | Valcourt Holdings II LLC | Q4 2025 | First lien senior secured loan | `342.9M USD` | `342.9M USD` |  | `9.01% (SOFR + 5.00%)` | `11/2029` |
| Senior Direct Lending Program LLC / Ares Capital exhibit | Valcourt Holdings II LLC | Q1 2026 | First lien senior secured loan | `342.0M USD` | `342.0M USD` |  | `8.81% (SOFR + 5.00%)` | `11/2029` |
| Ares Capital Corporation | Valcourt Holdings II LLC and Jobs Holdings Inc. | Q2 2026 | First lien senior secured loan | `117.6M USD` | `117.6M USD` |  | `8.39% SOFR + 4.75%` | `05/2033` |
| Cliffwater Corporate Lending Fund | Valcourt Holdings II LLC | FY2023 | First lien term loan | `41.046931M USD` | `40.287584M USD` |  | `11.267% SOFR + 5.25%` | `11/17/2029` |
| Cliffwater Corporate Lending Fund | Valcourt Holdings II LLC | FY2023 | Delayed draw | `13.537906M USD` | `-0.250445M USD` | `13.537906M USD` | `1.000%` | `11/17/2029` |
| Cliffwater Corporate Lending Fund | Valcourt Holdings II LLC | FY2023 | Revolver | `5.415162M USD` | `-0.100178M USD` | `5.415162M USD` | `0.500%` | `01/07/2027` |

The CSV also keeps comparative rows separately so the same SDLP balance is not double-counted across repeated exhibits.

## Cleanest Number

The cleanest latest visible 2026 number is:

`342.0M USD SDLP Q1 2026 fair value + 117.6M USD ARCC Q2 2026 fair value = 459.6M USD`

That is a lower-bound holder-exposure figure across visible Ares-linked filing vehicles.

It is not total Valcourt debt.

## Why This Matters

Before this pass, Valcourt was mainly operating-context evidence:

- Ares listed Valcourt as a selected Q2 2026 U.S. direct-lending borrower.
- Littlejohn describes Valcourt as a provider of building maintenance services and says the platform made `10` acquisitions in `15` months.

After this pass, Valcourt has lender-side debt evidence:

- SDLP reported Valcourt first-lien exposure above `300M USD` in FY2024, Q4 2025, and Q1 2026.
- ARCC reported `117.6M USD` of Valcourt/Jobs first-lien fair value in Q2 2026.
- Cliffwater shows earlier third-party fund exposure to the same borrower group, including term-loan and unfunded commitment rows.

## Claim Update

Valcourt strengthens the borrower-destination claim:

`Private credit is funding real operating-company roll-up platforms in commercial and professional services, including building maintenance, and the exposure can be observed in SEC-filed lender schedules.`

It does not yet prove:

- A specific bank facility was repaid.
- Banks exited the lender group.
- The full facility size.
- The use of proceeds for the Q2 2026 Ares selected-borrower item.
- Whether the 05/2033 ARCC row reflects a refinancing, extension, amendment, or separate debt tranche.

## What To Do Next

The next Valcourt questions are:

| Question | Evidence Needed |
|---|---|
| Did the 11/2029 debt roll into the 05/2033 ARCC row? | Rating-agency report, credit agreement, amendment, or lender presentation. |
| Was the Q2 2026 Ares selected-borrower item acquisition finance, refinancing, or add-on funding? | Ares deal note, sponsor release, company acquisition release, or financing announcement. |
| Were banks displaced or still involved? | UCC filings, agent/lender list, payoff language, or revolver/banking relationship disclosure. |
| Is the lending tied to the acquisition roll-up strategy? | Acquisition timeline matched to debt-date changes and sponsor/platform releases. |

## Simple Version

Valcourt is now one of the best borrower-destination cases in the capital-flow file.

We can show real SEC-filed private-credit exposure, including at least `459.6M USD` of latest visible 2026 first-lien fair value across SDLP and ARCC.

What we cannot say yet is that this replaced a bank loan.
