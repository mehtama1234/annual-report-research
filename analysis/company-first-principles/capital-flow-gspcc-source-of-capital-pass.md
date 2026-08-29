# Capital Flow GSPCC Source-Of-Capital Pass

## Purpose

This is the seventh execution pass from the ultimate-source document queue.

Target: Goldman Sachs Private Credit Corp.

Question: when GSPCC appears as the large unfunded-commitment holder behind Frontline and Relation, what can we say about the capital stack and distribution channel behind that Goldman private-credit vehicle?

Extraction table:

`analysis/company-first-principles/data/capital-flow-gspcc-source-of-capital-extractions.csv`

Primary sources:

- `raw/primary-sources/capital-flow/relation/sec/gspcc-2026q2-10q.html`
- `raw/primary-sources/capital-flow/relation/sec/gspcc-2026q1-r19-unfunded.html`

## Simple Answer

GSPCC is the large Goldman private-credit vehicle in this sample.

The Q2 2026 10-Q reports no exchange-listed securities, but it does report Class I, Class S, and Class D shares registered under Section 12(g). It references Goldman Sachs Asset Management LP as investment adviser and discusses BDC and RIC status.

That upgrades the GSPCC rows from large Goldman unfunded commitments to a non-listed private-credit BDC funding channel with a disclosed balance sheet, share classes, private-offering mechanics, revolver funding, note funding, and asset coverage.

It still does not prove the final investor mix, Goldman corporate-balance-sheet funding, insurance funding, or borrower-level facility size.

## Vehicle Funding Snapshot

| Metric | Q2 2026 Value | Read |
|---|---:|---|
| Total investments at fair value | `18.187575B USD` | Large private-credit portfolio. |
| Total assets | `18.671894B USD` | Balance-sheet denominator. |
| Debt, net of debt issuance costs | `8.859977B USD` | Main leverage layer. |
| Total liabilities | `9.477846B USD` | Liabilities fund `50.76%` of assets. |
| Total net assets | `9.194048B USD` | Shareholder/net-asset capital funds `49.24%` of assets. |
| NAV per share | `24.57 USD` | Same reported NAV for Class I, Class S, and Class D. |

Derived ratios:

| Ratio | Value | Read |
|---|---:|---|
| Debt carrying value / total assets | `47.45%` | GSPCC is materially levered. |
| Total liabilities / total assets | `50.76%` | Liability funding is about half the asset stack. |
| Total net assets / total assets | `49.24%` | Shareholder/net-asset capital is nearly half the funding stack. |

## Share Classes And Offering Channel

| Metric | Q2 2026 Value | Read |
|---|---:|---|
| Class I net assets | `9.188531B USD` | Almost all net assets sit in Class I in this snapshot. |
| Class S net assets | `5.115M USD` | Small but present Class S channel. |
| Class D net assets | `0.402M USD` | Small but present Class D channel. |
| Securities registered on exchange | `None` | Non-listed route, unlike GSBD. |
| Registered share classes | `Class I; Class S; Class D` | Multi-class non-traded BDC structure. |
| Offering assistance | `GS & Co.` | Goldman-related offering intermediary. |

## Debt Stack

| Funding Layer | Q2 2026 Amount | Read |
|---|---:|---|
| Total aggregate borrowing amount committed | `11.185B USD` | Revolver commitments plus note principal. |
| Total debt carrying value | `8.859977B USD` | Filed debt-table carrying value. |
| Total debt amount available | `2.195384B USD` | Undrawn debt capacity. |
| Revolving credit facilities committed | `7.175B USD` | Truist, BNPP, and MS facilities. |
| Revolving credit facilities carrying value | `4.975837B USD` | Drawn revolver layer. |
| Unsecured notes principal outstanding | `4.010B USD` | Note funding layer. |
| Asset coverage ratio | `202%` | Regulatory leverage context. |

## Portfolio And Borrower Bridge

| Metric | Value | Read |
|---|---:|---|
| Private-credit portfolio companies | `190` | Large borrower base. |
| Performing debt bearing floating rate | `97.7%` | Floating-rate exposure dominates. |
| Weighted average LTV | `44.5%` | Portfolio collateral/risk context. |
| Median EBITDA | `109.00M USD` | Middle-market borrower scale. |
| Frontline unfunded commitment | `53.6880M USD` | Visible GSPCC commitment capacity in the current holder map. |
| Relation unfunded commitment | `76.3450M USD` | Visible GSPCC commitment capacity in the current holder map. |
| Current GSPCC sample total | `130.0330M USD` unfunded | Commitment capacity, not funded fair value. |

## Claim Upgrade

Before this pass:

GSPCC was a Goldman Sachs private-credit holder with large unfunded commitments to Frontline and Relation.

After this pass:

GSPCC is a non-listed Goldman private-credit BDC channel with `18.671894B USD` of assets, `8.859977B USD` of debt, `9.194048B USD` of net assets, Class I/Class S/Class D shares, `7.175B USD` of committed revolving credit facilities, `4.010B USD` of unsecured notes principal, and `202%` asset coverage.

## What This Still Does Not Prove

This pass does not prove:

- the ultimate holders of GSPCC shares
- holders of GSPCC notes
- whether Goldman Sachs balance-sheet capital funded any borrower loan
- whether insurance accounts supplied capital to GSPCC
- whether the Q1 2026 commitment rows were drawn by Q2 2026
- total facility size for Frontline or Relation
- whether private credit replaced bank credit in either case

## Current Bottom Line

For GSPCC-linked borrower rows, the immediate source-of-capital answer is now a non-listed Goldman private-credit BDC:

GSPCC had `18.671894B USD` of assets, `8.859977B USD` of debt, and `9.194048B USD` of net assets at Q2 2026. It is funded through shareholder/net-asset capital, large revolving credit facilities, and unsecured notes. The current borrower map shows `130.0330M USD` of GSPCC unfunded commitments to Frontline and Relation. That supports a large Goldman private-credit capacity channel claim, but not a final shareholder, insurer-funded, total-facility, or bank-displacement claim.
