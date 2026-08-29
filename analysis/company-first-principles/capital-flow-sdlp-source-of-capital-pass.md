# Capital Flow SDLP Source-Of-Capital Pass

## Purpose

This is the second execution pass from the ultimate-source document queue.

Target: Senior Direct Lending Program LLC.

Question: when SDLP appears as a large holder of middle-market borrower loans, what can we say about the capital stack behind that vehicle?

Extraction table:

`analysis/company-first-principles/data/capital-flow-sdlp-source-of-capital-extractions.csv`

Primary sources:

- `raw/primary-sources/capital-flow/ares-capital/q2-2026/arcc-2026-q2-10q.html`
- `raw/primary-sources/capital-flow/ares-capital/q2-2026/arcc-sdlp-2026q2-ex99-1.html`

## Simple Answer

SDLP is not just a generic Ares bucket.

ARCC describes SDLP as a joint venture with Varagon that makes first-lien senior secured loans, including stretch senior and unitranche loans, primarily to U.S. middle-market companies.

The funding stack is clearer now:

- ARCC provides capital through SDLP subordinated certificates.
- Varagon and its clients provide capital through senior notes, intermediate funding notes, and SDLP certificates.
- ARCC owned `87.5%` of outstanding SDLP certificates at June 30 2026.
- A Varagon client owned the remaining `12.5%` of outstanding SDLP certificates.

That lets us upgrade SDLP from “Ares-linked holder” to “ARCC/Varagon joint-venture direct-lending vehicle with disclosed note and certificate funding layers.”

## Vehicle Funding Snapshot

| Metric | Q2 2026 Value | Read |
|---|---:|---|
| Total agreed capital available to SDLP | `6150M USD` | ARCC plus Varagon and clients had agreed to make this capital available. |
| ARCC agreed capital available to SDLP | `1444M USD` | ARCC's committed availability share. |
| Total capital funded to SDLP | `4889M USD` | Funded vehicle capital at principal amount. |
| ARCC capital funded to SDLP | `1322M USD` | ARCC-funded portion at principal amount. |
| Total unfunded capital commitments to SDLP | `260M USD` | Approved delayed-draw commitments, subject to conditions. |
| ARCC unfunded capital commitments to SDLP | `60M USD` | ARCC share of those unfunded commitments. |

Derived ratios:

| Ratio | Value | Read |
|---|---:|---|
| ARCC share of funded SDLP capital | `27.04%` | ARCC supplies a meaningful minority of total funded SDLP capital. |
| ARCC share of unfunded SDLP commitments | `23.08%` | ARCC also supplies part of remaining SDLP delayed-draw commitment capacity. |
| ARCC share of SDLP certificates | `87.5%` | Certificate ownership is much higher than ARCC's funded-capital share because the SDLP also has senior-note and intermediate-note capital. |

## Balance-Sheet Snapshot

| Metric | Q2 2026 Value | Source |
|---|---:|---|
| Investments at fair value | `4309M USD` | ARCC selected SDLP financial information and Exhibit 99.1 |
| Total assets | `4595M USD` | ARCC selected SDLP financial information |
| Senior notes | `3270M USD` | ARCC selected SDLP financial information |
| Intermediate funding notes | `108M USD` | ARCC selected SDLP financial information |
| Total liabilities | `3519M USD` | ARCC selected SDLP financial information |
| Subordinated certificates and members' capital | `1076M USD` | ARCC selected SDLP financial information |

Derived structure:

| Ratio | Value | Read |
|---|---:|---|
| Liabilities / assets | `76.58%` | SDLP is mainly funded through liabilities, especially senior notes. |
| Subordinated certificates and members' capital / assets | `23.42%` | Junior/member capital is the smaller funding layer. |
| Investments / subordinated certificates and members' capital | `4.0046x` | A rough leverage-style view of investment fair value versus junior/member capital. |

## Borrower Cases This Upgrades

| Borrower | Prior SDLP Holder Evidence | Upgrade From This Pass |
|---|---|---|
| Valcourt | SDLP Q1 2026 fair value of `342.0M USD`; FY2024 and Q4 2025 route history | SDLP can now be described as an ARCC/Varagon joint-venture direct-lending vehicle with senior-note, intermediate-note, and certificate/member-capital layers. |
| Precinmac | SDLP FY2024 fair value of `253.5M USD` | Same source-of-capital upgrade for historical SDLP exposure. |

## Q2 Borrower Refresh Note

The fetched Q2 2026 SDLP Exhibit 99.1 did not show Valcourt, Precinmac, Trimaster, or Paris US Holdco in local text search.

That should not be overstated as a sale or repayment. It means the current SDLP source-of-capital pass is stronger than the Q2 borrower-refresh pass. A full schedule reconciliation would be needed before treating the missing names as an exit signal.

## Claim Upgrade

Before this pass:

SDLP was a large Ares-linked holder channel for Valcourt and Precinmac.

After this pass:

SDLP is a named ARCC/Varagon joint-venture direct-lending vehicle. Its disclosed Q2 2026 capital stack includes `3270M USD` of senior notes, `108M USD` of intermediate funding notes, and `1076M USD` of subordinated certificates and members' capital.

## What This Still Does Not Prove

This pass does not prove:

- the identities of Varagon's clients
- whether insurance liabilities fund any SDLP notes or certificates
- which funding layer supports any specific borrower loan
- total facility size for Valcourt or Precinmac
- whether borrower debt replaced bank debt
- whether Q2 absence of a borrower name means exit, payoff, amendment, or parser/search limitation

## Next SDLP Work

The next useful documents are:

- SDLP formation or ownership agreement
- Varagon client or financing disclosures, if public
- rating reports on SDLP senior notes
- any ARCC annual-report footnote with more detailed SDLP capital terms
- borrower credit agreements or rating reports for Valcourt and Precinmac

## Current Bottom Line

For SDLP-linked borrower rows, the source-of-capital answer is now substantially better:

The immediate holder channel is an ARCC/Varagon joint-venture direct-lending vehicle with `4.595B USD` of assets, `3.519B USD` of liabilities, and `1.076B USD` of subordinated certificates plus members' capital. ARCC is the dominant certificate holder but only about `27.04%` of total funded SDLP capital, because senior notes and intermediate funding notes are major funding layers.
