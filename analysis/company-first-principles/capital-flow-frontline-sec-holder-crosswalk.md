# Capital Flow Frontline SEC Holder Crosswalk

## Purpose

This pass applies the borrower-holder method to Frontline Road Safety.

The current overlap control is documented in the [tranche identity and overlap boundary](capital-flow-frontline-tranche-identity-overlap-boundary-2026-09-18.md), with a [structured companion](data/capital-flow-frontline-tranche-identity-overlap-boundary-2026-09-18.csv).

The operating data file is:

`analysis/company-first-principles/data/capital-flow-frontline-sec-holder-crosswalk.csv`

## Question

`Can we turn the Ares selected-borrower Frontline item into actual holder-level debt numbers?`

Yes.

Frontline appears in SEC-filed credit-vehicle schedules under:

- `Frontline Road Safety LLC`
- `Frontline Road Safety Operations, LLC`

The current evidence is strong for holder-level exposure and operating destination. It is still weak for bank-displacement language because none of the captured sources proves a prior bank payoff, termination, or post-close lender-role map.

## 2026-09-18 targeted holder refresh

Blackstone Private Credit Fund's Q2 2026 Form 10-Q adds five `Frontline Road
Safety, LLC` first-lien rows totaling `$29.112M` principal, `$28.983M`
amortized cost, and `$28.524M` fair value. The rows show `SOFR + 4.75%`, an
effective yield of `8.39%` including `2.00%` PIK, and a March 4, 2032 maturity.

This is additional same-period syndication visibility, not a change to the
controlled denominator. The BCRED rows remain outside the controlled total
until borrower-name, tranche, facility, and overlap controls reconcile them
against FSK, K-FITS, GSBD, and BXSL. See the [BCRED holder refresh](capital-flow-ares-frontline-bcred-holder-refresh-2026-09-18.md)
and its [structured companion](data/capital-flow-ares-frontline-bcred-holder-refresh-2026-09-18.csv).

The same Q2 filing cycle also exposes a Goldman Sachs Private Credit Corp.
Frontline Road Safety Operations first-lien row with `$40.625M` par and
`$38.594M` fair value at a March 2032 maturity. This row is likewise held
outside the controlled denominator pending facility and overlap mapping.

Ares Capital Corporation's own Q2 2026 filing adds approximately `$23.9M` of
Frontline fair value across three funded rows, including a June 2026
acquisition-date row. This upgrades the source-of-capital layer from
arranger-only to Ares-managed vehicle exposure, while remaining outside the
controlled denominator until legal-entity, tranche, and facility overlap are
reconciled.

Ares Strategic Income Fund's Q2 2026 supplement adds a larger current-period
Ares-managed position: `$96.7893M` principal, `$95.9022M` amortized cost, and
`$94.9240M` fair value for a Frontline first-lien senior secured loan. The
related revolving row is undrawn. This is direct Ares-managed holder evidence,
not proof that the position is the Ares-arranged Bain facility or that the
reported fair value equals borrower cash received. The [ASIF roll-forward](capital-flow-ares-frontline-asif-rollforward-2026-09-18.md)
measures the Q1-to-Q2 position change while keeping the funding-event claim on
hold.

The expanded SEC search adds three more direct Q2 2026 holder observations:

- KKR Enhanced US Direct Lending Fund-L reports a Frontline revolver plus base,
  delayed-draw, and add-on first-lien rows totaling `$60.247M` par and
  `$54.449M` fair value. The schedule identifies a May 2025 add-on and an
  October 2025 delayed-draw row, which adds tranche chronology but does not
  prove borrower cash movement.
- Sixth Street Lending Partners reports a `$40.625M` par / `$38.594M` fair
  value first-lien row and a separate `$121.875M` undrawn Frontline delayed-
  draw commitment.
- West Bay BDC reports `$2.790M` of Frontline fair value.
- KKR FS Income Trust reports five Frontline first-lien rows totaling
  `$58.126M` par and `$57.019M` fair value, plus `$4.559M` of commitment
  capacity.
- Cliffwater Corporate Lending Fund reports multiple Frontline first-lien
  positions totaling approximately `$54.050M` principal and `$51.863M` fair
  value across 2031 revolver and 2032 term/delayed-draw rows.

These observations expand same-period public holder breadth; they do not
replace the controlled denominator or prove that all rows are non-overlapping
pieces of one facility.

## Extracted Holder Rows

| Reporting Entity | Borrower Name | Period | Loan Type | Principal | Fair Value | Unfunded Commitment | Rate | Maturity |
|---|---|---|---|---:|---:|---:|---|---|
| Ares Capital Corporation | Frontline Road Safety Operations LLC | Q2 2026 | First-lien senior secured loan / revolving loan rows | `24.2M USD` | `23.9M USD` |  | SOFR + `5.00%`; `8.64%` effective yield on term rows, selected PIK | `03/2032` |
| Ares Strategic Income Fund | Frontline Road Safety Operations LLC | Q2 2026 | First-lien senior secured loan | `96.7893M USD` | `94.9240M USD` |  | SOFR + `5.00%`; `8.64%` effective yield including `2.00%` PIK | `03/2032` |
| FS KKR Capital Corp. | Frontline Road Safety LLC | Q2 2026 | First-lien senior secured loans | `136.7M USD` | `132.8M USD` |  | SOFR + `4.8%` to `5.0%`; selected PIK rows | `03/2032` |
| KKR FS Income Trust Select | Frontline Road Safety LLC | Q2 2026 | First-lien senior secured loans | `48.723M USD` | `47.936M USD` |  | SOFR + `4.8%` to `5.0%`; selected PIK rows | `03/2032` |
| Goldman Sachs BDC Inc. | Frontline Road Safety Operations LLC | Q2 2026 | First-lien senior secured loans | `19.222M USD` | `17.939M USD` |  | SOFR + `4.75%`; selected PIK rows | `03/04/32` |
| Goldman Sachs Private Credit Corp. | Frontline Road Safety Operations LLC | Q2 2026 | First-lien loan | `40.625M USD` | `38.594M USD` |  | SOFR + `5.00%`; `8.64%` effective yield | `03/2032` |
| KKR Enhanced US Direct Lending Fund-L Inc. | Frontline Road Safety LLC | Q2 2026 | First-lien revolver and term/delayed-draw loans | `60.247M USD` | `54.449M USD` |  | SOFR + `2.50%` to `4.75%`; selected PIK rows | `03/04/2032` |
| KKR FS Income Trust | Frontline Road Safety LLC | Q2 2026 | First-lien term and delayed-draw loans | `58.126M USD` | `57.019M USD` | `4.559M USD` | SOFR + `4.8%` to `7.0%`; selected PIK rows | `03/2032` |
| Cliffwater Corporate Lending Fund | Frontline Road Safety Operations LLC | Q2 2026 | Multiple first-lien revolver, term, and delayed-draw rows | `54.050M USD` | `51.863M USD` |  | SOFR + `4.75%`; selected `2.00%` PIK rows | `03/2031` and `03/2032` |
| Sixth Street Lending Partners | Frontline Road Safety Operations LLC | Q2 2026 | First-lien loan | `40.625M USD` | `38.594M USD` | `121.875M USD` | SOFR + `5.00%`; `8.64%` effective yield | `03/2032` |
| West Bay BDC LLC | Frontline Road Safety Operations LLC | Q2 2026 | First-lien loan | `2.790M USD` | `2.790M USD` |  | S + `4.75%`; `2.00%` PIK | `03/04/2032` |
| Blackstone Secured Lending Fund | Frontline Road Safety LLC | Q2 2026 | First-lien senior secured loans | `33.005M USD` | `32.292M USD` |  | SOFR + `4.75%`; selected PIK rows | `03/04/2032` |
| Oak Hill Advisors | Frontline Road Safety Holdings II LLC | Q2 2026 | 2026 delayed-draw term loan |  |  | `3.750M USD` |  | `03/04/2032` |
| Ares Strategic Income Fund | Frontline Road Safety Operations LLC | Q1 2026 | First-lien senior secured loan | `76.6927M USD` | `76.6927M USD` |  | `8.72%` with `2.00%` PIK; SOFR(M) + `5.00%` | `03/2032` |
| Goldman Sachs Private Credit Corp. | Frontline Road Safety Operations LLC | Q1 2026 | Unfunded commitment |  |  | `53.688M USD` |  |  |
| Goldman Sachs BDC Inc. | Frontline Road Safety Operations LLC | Q2 2026 | Unfunded commitment |  |  | `0.612M USD` |  |  |

## Cleanest Number

The cleanest latest Q2 2026 funded number is:

`132.8M USD FSK + 47.936M USD K-FITS + 17.939M USD GSBD = 198.675M USD`

That is visible holder exposure, not total Frontline debt.

The crosswalk now also records additional same-period breadth evidence that is
kept outside that controlled three-vehicle denominator: ARCC, ASIF, BXSL,
BCRED, GSPCC, KKR Enhanced, KKR FS Income Trust, Cliffwater, Sixth Street, and West Bay add current-period
holder rows; OHA and Sixth Street add delayed-draw commitment rows. The
generated same-period view totals `$622.824M` of reported fair value and
`$130.796M` of reported unfunded commitments across those visible rows. This
is a breadth metric, not total Frontline debt, because borrower-name, facility,
tranche, and overlap controls remain incomplete.

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

Frontline is now a strong borrower-destination case with broader public holder
visibility than the controlled lower-bound total alone implies.

We can show `198.675M USD` of latest Q2 2026 funded fair value across FSK,
K-FITS, and GSBD, plus another `76.6927M USD` ASIF Q1 holder row. Additional
Q2 SEC schedules add BXSL fair value and OHA unfunded commitment evidence, but
those are held outside the controlled lower-bound denominator pending overlap
and facility mapping.

What we still cannot say is that this is the whole facility, that it is Ares' exact amount, or that it replaced bank credit.
