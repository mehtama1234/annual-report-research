# Capital Flow GSBD Source-Of-Capital Pass

## Purpose

This is the sixth execution pass from the ultimate-source document queue.

Target: Goldman Sachs BDC Inc.

Question: when GSBD appears as a holder of Frontline and Relation debt, what can we say about the capital stack behind that Goldman-managed public BDC?

Extraction table:

`analysis/company-first-principles/data/capital-flow-gsbd-source-of-capital-extractions.csv`

Primary source:

- `raw/primary-sources/capital-flow/relation/sec/gsbd-2026q2-10q.html`

## Simple Answer

GSBD is a public BDC route into middle-market private credit.

The Q2 2026 filing shows GSBD common stock listed on the NYSE under ticker `GSBD`, references Goldman Sachs Asset Management LP as investment adviser, and discusses maintaining BDC and RIC status.

That upgrades Frontline and Relation GSBD rows from “Goldman Sachs holder evidence” to “public BDC balance-sheet funding evidence.”

It still does not prove Goldman Sachs corporate-balance-sheet funding, insurance funding, or the full borrower facility size.

## Vehicle Funding Snapshot

| Metric | Q2 2026 Value | Read |
|---|---:|---|
| Total investments at fair value | `3.195248B USD` | Portfolio scale. |
| Affiliated money market fund investments | `36.226M USD` | Liquidity/cash-management context. |
| Total assets | `3.287804B USD` | Balance-sheet denominator. |
| Debt, net of debt issuance costs | `1.850308B USD` | Main leverage layer. |
| Secured borrowings | `2.361M USD` | Small secured-borrowing line. |
| Total liabilities | `1.930154B USD` | Liabilities fund `58.71%` of assets. |
| Total net assets | `1.357650B USD` | Public BDC net-asset capital. |
| Common shares issued and outstanding | `112.569067M shares` | Public common-share channel. |
| NAV per share | `12.06 USD` | Net asset value per common share. |

Derived ratios:

| Ratio | Value | Read |
|---|---:|---|
| Debt carrying value / total assets | `56.28%` | GSBD is meaningfully levered. |
| Total liabilities / total assets | `58.71%` | Liability funding is more than half the asset stack. |
| Total net assets / total assets | `41.29%` | Public BDC equity/net assets remain the other major layer. |

## Debt Stack

| Funding Layer | Q2 2026 Amount | Read |
|---|---:|---|
| Total aggregate borrowing amount committed | `2.675B USD` | Revolver commitment plus notes principal. |
| Total debt carrying value | `1.850308B USD` | Filed debt-table carrying value. |
| Total debt amount available | `795.613M USD` | Undrawn debt capacity. |
| Revolving Credit Facility committed | `1.475B USD` | Bank/facility-style leverage. |
| Revolving Credit Facility carrying value | `679.641M USD` | Drawn revolver layer. |
| Unsecured notes principal outstanding | `1.200B USD` | Public/private note funding layer. |
| Asset coverage ratio | `172%` | Regulatory leverage context. |

Selected note instruments:

| Instrument | Principal | Carrying Value |
|---|---:|---:|
| 2027 Notes | `400M USD` | `396.874M USD` |
| 2029 Notes | `400M USD` | `388.565M USD` |
| 2030 Notes | `400M USD` | `385.228M USD` |

## Portfolio Context

| Metric | Q2 2026 Value | Read |
|---|---:|---|
| Cumulative originations since formation | `9.94B USD` | GSBD reports aggregate principal amount originated from formation through June 30 2026 before exits and repayments. |
| Portfolio companies | `173` | Broad middle-market borrower base. |
| Performing debt bearing floating rate | `98.9%` | Floating-rate exposure dominates. |
| Weighted average yield at fair value | `11.3%` | Portfolio yield context. |
| Weighted average leverage | `6.2x` net debt / EBITDA | Portfolio credit-risk context. |
| Median EBITDA | `73.37M USD` | Middle-market borrower scale. |

## Borrower Cases This Upgrades

| Borrower | GSBD Holder Evidence In Current Map | Upgrade From This Pass |
|---|---:|---|
| Frontline Road Safety | `17.9390M USD` fair value plus `0.6120M USD` unfunded commitment | GSBD row can be tied to a Goldman-managed public BDC with public equity, revolver borrowings, unsecured notes, and regulatory asset coverage. |
| Relation Insurance | `4.5480M USD` fair value plus `1.1960M USD` unfunded commitment | Same public-BDC funding-stack upgrade for the Relation/BayPine acquisition-financing case. |
| Current GSBD sample total | `22.4870M USD` fair value plus `1.8080M USD` unfunded | Visible GSBD borrower rows in the current holder map. |

## Claim Upgrade

Before this pass:

GSBD was a named Goldman Sachs holder in Frontline and Relation debt schedules.

After this pass:

GSBD is a public BDC funding channel with `3.287804B USD` of assets, `1.850308B USD` of debt, `1.357650B USD` of net assets, `1.475B USD` of revolving-credit-facility commitment, `679.641M USD` of drawn revolver carrying value, `1.2B USD` of unsecured notes principal, `112.569067M` common shares outstanding, and `172%` asset coverage.

## What This Still Does Not Prove

This pass does not prove:

- the ultimate common shareholders of GSBD
- holders of GSBD unsecured notes
- whether Goldman Sachs balance-sheet capital funded any borrower loan
- whether any insurance account supplied capital to GSBD
- which GSBD funding layer maps specifically to Frontline or Relation
- total facility size for Frontline or Relation
- whether private credit replaced bank credit in either case

## Current Bottom Line

For GSBD-linked borrower rows, the immediate source-of-capital answer is now a Goldman-managed public BDC balance sheet:

GSBD had `3.287804B USD` of assets, `1.850308B USD` of debt, and `1.357650B USD` of net assets at Q2 2026. Its funding stack includes a `1.475B USD` revolving credit facility, `1.2B USD` of unsecured notes principal, public common equity, and `172%` asset coverage. That supports a public-BDC private-credit channel claim for Frontline and Relation, but not a Goldman corporate, insurer-funded, total-facility, or bank-displacement claim.
