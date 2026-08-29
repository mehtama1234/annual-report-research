# Capital Flow MAI SEC Holder Crosswalk

## Purpose

This pass applies the borrower-holder method to MAI Capital Management.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-mai-sec-holder-crosswalk.csv`

## Question

`Can we turn the Ares selected-borrower MAI Capital item into actual holder-level debt numbers?`

Yes, with a smaller visible exposure than Valcourt, Precinmac, AeriTek, or Sunvair.

MAI appears in multiple public credit-vehicle schedules:

- Ares Capital Corporation reports MAI first-lien exposure in Q2 2026.
- Ares Strategic Income Fund reports a MAI revolver row in Q1 2026.
- New Mountain Private Credit Fund reports MAI drawn first-lien rows and an undrawn commitment row in Q1 2026.
- New Mountain Guardian IV BDC provides older MAI first-lien holder history from Q3 2024.

## Extracted Holder Rows

| Reporting Entity | Borrower Name | Period | Loan Type | Principal | Fair Value | Commitment | Rate | Maturity |
|---|---|---|---|---:|---:|---:|---|---|
| Ares Capital Corporation | Mai Capital Management Intermediate LLC | Q2 2026 | First lien senior secured loans | `8.0M USD` | `8.0M USD` |  | `8.48% SOFR(Q) + 4.75%` | `08/2031` |
| Ares Strategic Income Fund | Mai Capital Management Intermediate LLC | Q1 2026 | First lien senior secured revolving loan | `0.7263M USD` | `0.7263M USD` |  | `8.45% SOFR(Q) + 4.75%` | `08/2031` |
| New Mountain Private Credit Fund | MAI Capital Management Intermediate LLC | Q1 2026 | First Lien - Drawn | `25.330M USD` | `25.330M USD` |  | `8.45% SOFR(Q) + 4.75%` | `08/2031` |
| New Mountain Private Credit Fund | MAI Capital Management Intermediate LLC | Q1 2026 | First Lien - Drawn | `1.167M USD` | `1.167M USD` |  | `8.45% SOFR(Q) + 4.75%` | `08/2031` |
| New Mountain Private Credit Fund | MAI Capital Management Intermediate LLC | Q1 2026 | First lien - Undrawn |  |  | `12.401M USD` | not applicable | `06/2027` |
| New Mountain Guardian IV BDC | MAI Capital Management Intermediate LLC | Q3 2024 | First Lien | `21.557M USD` | `21.449M USD` |  | `9.35% SOFR(Q) + 4.75%` | `08/2031` |

The CSV also keeps ARCC Q1 2026, New Mountain FY2025 comparative, and route-evidence rows separately so they are not double-counted.

## Cleanest Number

The cleanest latest visible 2026 funded number is:

`8.0M USD ARCC Q2 2026 fair value + 0.7263M USD ASIF Q1 2026 fair value + 26.497M USD New Mountain Q1 2026 drawn fair value = 35.2233M USD`

New Mountain also reports a separate `12.401M USD` undrawn commitment row.

That is visible holder exposure, not total MAI debt.

## Why This Matters

Before this pass, MAI was operating-context evidence:

- Ares listed MAI Capital Management as a Q2 2026 selected U.S. direct-lending borrower.
- The selected-borrower map classifies it as a wealth management and advisory services platform tied to a continued M&A strategy.

After this pass, MAI has lender-side debt evidence:

- ARCC discloses MAI first-lien exposure in Q2 2026.
- ASIF discloses a MAI revolver row in Q1 2026.
- New Mountain discloses larger drawn MAI first-lien rows plus an undrawn commitment row in Q1 2026.

## Claim Update

MAI strengthens this claim:

`Private credit is funding wealth-management and advisory-service consolidation platforms, and the debt can be observed in SEC-filed holder schedules.`

It does not yet prove:

- Total facility size.
- Full lender group.
- Prior bank repayment.
- Which acquisitions or operating needs were funded.
- Whether the Ares Q2 2026 selected-borrower item was an add-on, repricing, refinancing, or new money.

## What To Do Next

The next MAI questions are:

| Question | Evidence Needed |
|---|---|
| Which M&A activity was funded by the 2026 debt? | MAI acquisition timeline, sponsor release, financing announcement, or lender note. |
| Was there a prior bank facility? | UCC filings, credit agreement, payoff language, or agent references. |
| How broad is the lender syndicate? | More BDC/interval-fund schedules with matching 08/2031 maturity and SOFR + 4.75% pricing. |
| How does the debt map to operating economics? | AUM, advisor count, client assets, revenue, EBITDA, acquisition count, and integration metrics. |

## Simple Version

MAI is now more than a named Ares deal example.

We can show at least `35.2233M USD` of visible 2026 funded holder-level private-credit exposure, plus a separate `12.401M USD` undrawn commitment row.

What we still cannot say is that this replaced a bank loan or equals the whole facility.
