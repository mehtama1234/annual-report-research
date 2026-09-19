# Capital Flow Apollo Athene AMAPS Named-Cash Source Acquisition Pass 1

## Purpose

This pass tests AMAPS as the second Apollo/Athene named issuer proof route after Concord.

The core question is:

`Can Athene's statutory AMAPS cash-like proceeds and income row be connected to Apollo's AMAPS wrapper, AMAPS 1 public exposure evidence, and a named legal entity without overclaiming borrower receipt, collateral cash flow, or return?`

The structured source acquisition table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-amaps-named-cash-source-acquisition-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-amaps-named-cash-source-acquisition-diagnostic-pass-1.csv`

## Short Answer

AMAPS upgrades from a mapped issuer row to:

`platform-wrapper-and-Athene-alignment-visible; AMAPS-1-collateral/remittance/return hold`

This is stronger than a generic issuer map because four things now connect:

1. Athene statutory rows show named AMAPS 1 same-CUSIP proceeds and interest fields, including a `10/24/2025` disposal row naming `Apollo Capital Markets Partner` as counterparty for `$268.000000M` of consideration.
2. Apollo publicly describes AMAPS as its multi-asset structured-credit vehicle.
3. Apollo says AMAPS was built around Athene's need for higher-quality collateral and safe yield.
4. Apollo/Athene public investment disclosure lists AMAPS 1 LLC as a material investment-grade ABS debt concentration.

But the proof still stops before full named cash proof.

AMAPS is a pooled structured-credit wrapper. Public evidence points to collateral categories and alignment, not to exact underlying borrower receipts, trustee remittance, liability spread, or final return.

## Q2 2026 statutory same-CUSIP refresh

The official [Athene statutory-filings page](https://ir.athene.com/financial-information/statutory-filings)
provides the Q2 2026 AAIA statement. Schedule D Part 3, PDF page `2470`,
contains a new current-quarter acquisition row for the same AMAPS 1 CUSIP
`02300A-AA-8`:

| Field | Filed value | Interpretation |
| --- | ---: | --- |
| Date acquired | `06/23/2026` | Current-quarter legal-entity acquisition/addition. |
| Vendor | `ALRe Corporate AAM` | Named affiliated/reinsurance-side statutory counterparty. |
| Actual cost | `$120,700,000` | Statutory acquisition-cost candidate. |
| Par value | `$120,700,000` | Position amount associated with the row. |
| Paid for accrued interest/dividends | `$2,661,436` | Statutory acquisition settlement input, not a bank confirmation. |

This materially improves AMAPS' current-period chronology: the same named
CUSIP has a 2025 Athene disposal row naming Apollo Capital Markets Partner and
a Q2 2026 acquisition row naming ALRe Corporate AAM. It creates a more precise
legal-entity/counterparty continuity route, but it does not prove that the
acquisition settled in cash, identify the underlying economic seller, show
custody movement, or connect the row to the AMAPS 1 wrapper's collateral and
return. The row is therefore an **acquisition/continuity candidate**, not
owner cash or a realized return.

The direct statement is the [Q2 2026 AAIA statutory PDF](https://d1io3yog0oux5.cloudfront.net/_f301a7da18a01c1717e3734d3a0fe50c/athene/db/2370/22562/pdf/2Q+2026+AAIA+Statement.pdf).

## Source Acquisition Result

| Evidence Layer | Source Status | What It Adds | Remaining Hold |
|---|---|---|---|
| Athene statutory same-CUSIP proceeds | `local-source-row-visible` | Athene same-CUSIP packet shows `268.000000M USD` cash-like disposal consideration, `1.917500000B USD` year-end book value, `48.871440M USD` year-end interest income, and `3.986842M USD` disposal interest/dividends for AMAPS 1 LLC CUSIP `02300A-AA-8`; the disposal row is dated `10/24/2025` and names `Apollo Capital Markets Partner`. | The statutory counterparty/consideration fields are not a trade confirmation, settled bank receipt, legal-entity allocation, remittance report, liability release, or parent/common-owner cash proof. |
| Apollo AMAPS product definition | `public-source-found` | Apollo defines AMAPS as Apollo Multi-Asset Prime Securities, a structured credit product for diversified, higher-credit-quality assets. | Does not disclose AMAPS 1 collateral tape, noteholder allocation, trustee payments, or borrower-level use. |
| Apollo AMAPS collateral route | `public-source-found` | Apollo's comparison chart describes diversified corporate and asset-backed credit, about `45-50%` investment-grade collateral, about `9x` debt/equity leverage, and `600+` obligors. | No underlying obligor list, collateral balances, asset marks, cash collections, or loan-level use of proceeds. |
| Apollo AMAPS instrument/liquidity mechanics | `public-source-found` | Apollo's product article describes a `5-year` AMAPS note term, approximately `85%` investment-grade-rated notes, tranche-specific CUSIPs, and daily pricing/trading in a liquid secondary market. | Product-level description is not AMAPS 1's executed term, trade confirmation, custodian settlement, trustee remittance, or realized return. |
| Apollo/Athene alignment | `public-source-found` | Apollo says AMAPS was built for Athene's higher-quality collateral and safe-yield need, and says Apollo or Athene is a significant investor in each underlying AMAPS tranche. | No AMAPS 1 tranche ownership schedule or Athene-specific allocation. |
| Apollo/Athene SEC investment disclosure | `public-source-found` | Public investment disclosure lists investment-grade ABS debt issued by AMAPS 1 LLC at `2.550B USD` at December 31, 2025. | No CUSIP-level statutory entity allocation, cash receipts, collateral, or return. |
| KBRA AMAPS 5 analog | `public-analog-source-found` | Later AMAPS rating releases show how the AMAPS format can contain corporate credit, asset-backed finance, private and broadly syndicated lending, and hundreds of obligors. | AMAPS 5 is not AMAPS 1, so it cannot prove AMAPS 1 collateral or cash flows. |
| S&P Global Market Intelligence PLR context | `public-source-found` | AMAPS 1 appears in the private-letter-rated bond scrutiny context and is described as an Athene equity-backed ABS classification under the NAIC issuer-type framework. | Does not provide AMAPS 1 collateral tape, rating rationale report, or Athene cash receipt. |
| Bloomberg LEI | `public-source-found` | AMAPS 1 LLC legal identity and Delaware record are visible for document request targeting. | No ownership, noteholder, remittance, collateral, or return evidence. |
| AMAPS proof requirements | `request-package-defined` | The decisive missing document package is now explicit. | Controlled/private documents are likely required for full named cash proof. |

## Cash Movement Read

The safe cash read is:

`Athene has a statutory same-CUSIP AMAPS 1 cash-like proceeds candidate: the 10/24/2025 row names Apollo Capital Markets Partner and shows 268.000000M USD of consideration. Apollo's public AMAPS materials identify the wrapper as an Apollo structured-credit product aligned with Athene's insurance-yield needs. Apollo/Athene public investment disclosure confirms AMAPS 1 LLC as a material investment-grade ABS debt concentration. This supports wrapper, named-counterparty, legal-entity, and Athene-alignment evidence, not full borrower receipt, asset-level return, or Apollo owner-cash route.`

In simpler words:

Athene appears to hold and transact in a named AMAPS 1 note. Apollo publicly explains what AMAPS is and why it fits Athene. Apollo/Athene also publicly discloses a large AMAPS 1 concentration.

That tells us where the pipe is.

It does not tell us which underlying borrowers got the cash, how each collateral asset performed, what the trustee remitted to Athene, or what Athene earned after liability cost.

The public product mechanics sharpen the next request. If the AMAPS 1 row is
part of the described format, the controlled package should be able to identify
the exact tranche CUSIP, stated term, secondary-market trade or transfer date,
custodian/settlement account, and trustee waterfall. The article's `5-year`
term and daily-trading language are format-level expectations, not evidence
that CUSIP `02300A-AA-8` traded on a particular date or that Athene received
the `$268M` statutory consideration.

## Why AMAPS Is Different From Concord

Concord is easier to understand as a named operating borrower/wrapper case. Public sources identify a music-royalty ABS transaction, collateral pool, refinancing use, and Apollo-affiliate structuring.

AMAPS is more important as a platform-wrapper case. It appears to be a structured-credit product built to route insurance-style capital into diversified corporate and asset-backed credit exposure.

That makes AMAPS stronger on platform design and Athene alignment, but weaker on named borrower/use proof.

## Decisive Missing Documents

To promote AMAPS beyond this level, we need:

1. AMAPS 1 offering memorandum
2. tranche supplement
3. full rating rationale reports
4. collateral tape or portfolio schedule
5. trustee or noteholder remittance reports
6. payment waterfall
7. Apollo/Athene allocation records
8. Athene statutory subsidiary reconciliation
9. liability-cost and spread support

Without those documents, AMAPS cannot be called full named-cash proof.

## Source URLs

- Apollo AMAPS product article: `https://www.apollo.com/insights-news/insights/2026/05/introducing-amaps`
- Apollo/Athene SEC investment disclosure: `https://www.sec.gov/Archives/edgar/data/1527469/000152746926000013/R12.htm`
- KBRA AMAPS 5 preliminary rating release: `https://www.kbra.com/publications/KDBMTzJQ`
- KBRA AMAPS 5 final rating release: `https://www.kbra.com/publications/MSzqKhYx`
- S&P Global Market Intelligence private-letter-rated bond article: `https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/01/holdings-scrutiny-of-private-letter-rated-bonds-continue-to-climb`
- Bloomberg LEI AMAPS 1 LLC: `https://lei.bloomberg.com/leis/view/254900LXAEJYTU2O1J86`

## Safe Claim

`AMAPS is now source-acquired as an Apollo/Athene platform-wrapper and alignment case. Athene statutory evidence shows CUSIP 02300A-AA-8 disposed on 10/24/2025 with Apollo Capital Markets Partner named as counterparty, 268.000000M USD of consideration, 1.917500000B USD of year-end book value, 48.871440M USD of year-end interest income, and 3.986842M USD of disposal interest/dividends. Apollo public materials identify AMAPS as an Apollo structured-credit product aligned with Athene's collateral and safe-yield needs, and Apollo/Athene public disclosure lists AMAPS 1 LLC as a 2.550B USD investment-grade ABS debt concentration. The current evidence supports wrapper, named-counterparty, and alignment proof, not settled cash, underlying borrower receipt, trustee remittance, liability spread, or final return.`

## Decision

`amaps-platform-wrapper-and-athene-alignment-visible-collateral-remittance-return-hold`

AMAPS should stay in the Apollo/Athene prototype as a high-value wrapper case. The next move is not more broad AMAPS description; it is AMAPS 1-specific controlled document acquisition.
