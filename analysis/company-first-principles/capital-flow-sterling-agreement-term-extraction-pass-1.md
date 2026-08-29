# Capital Flow Sterling Agreement-Term Extraction Pass 1

## Purpose

This pass extracts actual agreement terms from Sterling Infrastructure's July `2026` Exhibit `10.1`.

The operating table is:

`analysis/company-first-principles/data/capital-flow-sterling-agreement-term-extraction-pass-1.csv`

The source agreement is:

`raw/primary-sources/capital-flow/capital-intensive-credit-agreements/sterling/exhibit101-secondamended.htm`

The question is:

`Does Sterling's actual credit agreement support the hypothesis that a backlog/acquisition platform uses a flexible secured revolver rather than single-project debt?`

## What Was Added

| Item | Count |
|---|---:|
| Agreement-term rows | `20` |
| Facility identity and size rows | `4` |
| L/C and swing-line rows | `2` |
| Pricing and fee rows | `3` |
| Use-of-proceeds and incremental-capacity rows | `3` |
| Covenant rows | `4` |
| Guarantee/collateral/JV rows | `3` |
| Governance row | `1` |

## Theme And Subtheme Interpretation

This pass takes one company, Sterling, from:

`filed-term-summary`

to:

`agreement-term-visible`

The broader CTCS-014 lane is still not project source-of-funds grade, but Sterling's credit-wrapper evidence is now meaningfully stronger.

The relevant subtheme is:

`backlog and acquisition platform funding`

The hypothesis from the funding-type map was:

`Sterling's work is less about owning one financeable asset and more about executing customer-funded projects and acquisitions, so a large reborrowable corporate credit wrapper may fit better than project debt.`

The agreement supports that hypothesis.

## Core Agreement Terms

| Term | Extracted Agreement Evidence | Interpretation |
|---|---|---|
| Borrower | Sterling Infrastructure, Inc. | Parent borrower under the agreement. |
| Administrative Agent | BMO Bank N.A. | BMO anchors the lender group and also appears as L/C Issuer and Swing Line Lender. |
| Revolving commitments | `1.500B USD` | Legally committed lender capacity, not just presentation language. |
| Termination date | July `2`, `2031` | Five-year committed platform from July `2026`. |
| Reborrowable feature | Revolving loans may be repaid and reborrowed | Fits flexible platform-liquidity use. |
| L/C sublimit | `600M USD` | Important for project guarantees, bonding-like needs, and backlog execution support. |
| Swing-line sublimit | `50M USD` | Supports short-term working-capital timing. |

## Pricing Grid

The agreement prices the revolver by Total Net Leverage Ratio.

| Total Net Leverage Ratio Level | Base-Rate Margin | SOFR / L/C Fee Margin | Commitment Fee |
|---|---:|---:|---:|
| Less than `1.00x` | `0.25%` | `1.25%` | `0.15%` |
| `1.00x` to less than `2.00x` | `0.50%` | `1.50%` | `0.20%` |
| `2.00x` to less than `3.00x` | `0.75%` | `1.75%` | `0.20%` |
| Greater than or equal to `3.00x` | `1.00%` | `2.00%` | `0.25%` |

Performance letter-of-credit fees are `67%` of the otherwise applicable L/C fee rates.

Simple read:

`Sterling's cost of capital is explicitly leverage-sensitive. The facility gives flexibility, but the pricing grid makes that flexibility more expensive as leverage rises.`

## Use Of Proceeds

The agreement explicitly permits proceeds to be used for:

- refinancing existing indebtedness
- capital expenditures
- general working capital
- permitted acquisitions
- other general corporate purposes
- prepaying existing term loans
- related fees and expenses
- other legal and proper purposes consistent with applicable laws

This matters because those are exactly the uses implied by the funding-type hypothesis.

Sterling's facility is not only a debt-refinancing event.

It is a flexible platform wrapper for:

`refinancing + capex + working capital + acquisitions + letters of credit`

## Covenants And Flexibility

| Covenant / Mechanism | Agreement Term | Why It Matters |
|---|---:|---|
| Maximum Total Net Leverage Ratio | `3.50x` | Actual leverage ceiling is now visible. |
| Material acquisition holiday | up to `4.00x` | Agreement can flex for large acquisitions. |
| Covenant holiday duration | four fiscal quarters | Acquisition flexibility is temporary, not open-ended. |
| Covenant holiday count | not more than two times during the term | The acquisition flex is limited. |
| Minimum Interest Coverage Ratio | `3.00x` | Cash-interest discipline remains in place. |
| Cash netting cap in net leverage | `50%` of EBITDA | Net leverage is not purely gross debt, but cash netting is capped. |
| Base incremental amount | greater of `500M USD` and `100%` of EBITDA | Additional capacity can exist beyond headline revolver. |
| Unlimited incremental amount | allowed if pro forma Total Net Leverage Ratio is `<= 2.00x` | Growth capacity expands if leverage remains low enough. |

Simple read:

`The agreement is built for acquisition and growth flexibility, but not unlimited freedom. Sterling can flex the platform, but leverage and interest coverage decide how far.`

## Guarantees, Collateral, And Project Boundaries

The guarantee/collateral package is broad:

- obligations are guaranteed by each direct and indirect subsidiary other than excluded subsidiaries
- obligations are secured by liens on all right, title, and interest of the borrower and guarantors in personal property, subject to agreement limits and collateral documents
- signature pages include many operating subsidiaries and acquired/platform entities, including CEC Facilities LLC and Stone Ridge Infrastructure LLC

But the agreement also has a boundary:

- excluded subsidiaries include Project Specific JVs
- investments in Project Specific JVs are permitted up to the greater of `360M USD` and `30%` of Net Worth, net of distributions

Simple read:

`The main credit wrapper is broad and secured, but project-specific structures may sit partly outside it. That is why Sterling is agreement-term-visible, not yet project-source-of-funds-grade.`

## What This Proves

This pass proves:

`Sterling's July 2026 facility is a real agreement-backed flexible secured credit platform with 1.5B USD of revolving commitments, July 2031 maturity, L/C and swing-line mechanics, leverage-based pricing, acquisition/capex/refinancing use language, financial covenants, subsidiary guarantees, broad personal-property collateral, and incremental-capacity mechanics.`

## What This Still Does Not Prove

This pass does not prove:

- which customer projects are funded by Sterling versus customers
- which backlog dollars require L/Cs or working capital
- actual revolver draw history after closing
- actual covenant cushion at each quarter end
- collateral value or borrowing availability after exclusions
- project-level margins or returns
- customer-funded backlog proof

## Simple Bottom Line

In simple words:

`Sterling now gives us real agreement proof for one funding-container hypothesis. The company did not just say it had a bigger revolver. The actual agreement shows a 1.5B USD secured platform that can support working capital, capex, acquisitions, refinancing, letters of credit, and short-term liquidity, with leverage-based pricing and covenant guardrails.`

The important boundary:

`That still does not tell us who ultimately funds each customer project in backlog.`

## Claim Status

Promote only:

`Sterling is now agreement-term-visible for its July 2026 credit wrapper.`

Do not promote:

`Sterling's backlog is proven project-funded, customer-funded, high-return, or fully converted to cash.`

## Next Pass

The next useful Sterling pass is:

`capital-flow-sterling-backlog-customer-funding-pass-1.md`

It should extract:

- contract assets and liabilities
- customer advances
- retainage
- L/C outstanding amounts
- project-specific JV use
- backlog by signed/unsigned/future-phase bucket
- cancellation rights
- customer concentration
- operating cash conversion by segment
