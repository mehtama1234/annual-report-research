# Capital Flow OBDC Source-Of-Capital Pass

## Purpose

This is the eighth execution pass from the ultimate-source document queue.

Target: Blue Owl Capital Corporation.

Question: when OBDC appears as a holder of Precinmac debt, what can we say about the capital stack behind that Blue Owl public BDC?

Extraction table:

`analysis/company-first-principles/data/capital-flow-obdc-source-of-capital-extractions.csv`

Primary sources:

- `raw/primary-sources/capital-flow/blue-owl-capital-corporation/q2-2026/obdc-2026-q2-10q.html`
- `raw/primary-sources/capital-flow/blue-owl-capital-corporation/q2-2026/obdc-q2-2026-8k-exhibit-99-1.html`
- `raw/primary-sources/capital-flow/precinmac/sec/obdc-2024-10k.html`

## Simple Answer

OBDC is a large public BDC route into middle-market private credit.

The Q2 2026 10-Q shows OBDC common stock listed on the NYSE under ticker `OBDC`, Blue Owl Credit Advisors LLC as investment adviser, and BDC/RIC status.

That upgrades the Precinmac OBDC row from “Blue Owl holder evidence” to “public BDC balance-sheet funding evidence.”

It still does not prove Blue Owl corporate-balance-sheet funding, the identity of OBDC shareholders or noteholders, the full Precinmac facility size, or a bank-replacement event.

## Vehicle Funding Snapshot

| Metric | Q2 2026 Value | Read |
|---|---:|---|
| Total investments at fair value | `14.955049B USD` | Portfolio scale. |
| Non-controlled non-affiliated investments | `12.439882B USD` | Main third-party borrower portfolio. |
| Controlled affiliated investments | `2.372421B USD` | Affiliate and joint-venture exposure context. |
| Total assets | `15.354604B USD` | Balance-sheet denominator. |
| Debt, net of debt issuance costs | `7.903533B USD` | Main leverage layer. |
| Total liabilities | `8.322845B USD` | Liabilities fund `54.21%` of assets. |
| Total net assets | `7.031759B USD` | Public BDC net-asset capital. |
| Common shares issued and outstanding | `493.142569M shares` | Public common-share channel. |
| NAV per share | `14.26 USD` | Net asset value per common share. |

Derived ratios:

| Ratio | Value | Read |
|---|---:|---|
| Debt carrying value / total assets | `51.47%` | OBDC is meaningfully levered. |
| Total liabilities / total assets | `54.21%` | Liability funding is slightly more than half the asset stack. |
| Total net assets / total assets | `45.79%` | Public BDC equity/net assets remain the other major layer. |
| Debt principal / net assets | `1.1404x` | Debt principal is a little above net assets. |

## Debt Stack

| Funding Layer | Q2 2026 Amount | Read |
|---|---:|---|
| Total aggregate principal committed | `12.242073B USD` | Debt commitments, CLOs, and unsecured notes. |
| Total outstanding principal | `8.019273B USD` | Filed debt-table principal outstanding. |
| Total debt carrying value | `7.903533B USD` | Balance-sheet debt after issuance costs. |
| Total amount available | `4.138072B USD` | Undrawn debt capacity. |
| Revolving Credit Facility commitment | `4.000B USD` | Bank/facility-style leverage. |
| Revolving Credit Facility outstanding principal | `105.500M USD` | Very low drawn revolver amount at quarter-end. |
| Revolving Credit Facility availability | `3.856721B USD` | Most of the revolver was undrawn. |
| SPV Asset Facilities outstanding principal | `996.700M USD` | Financing-subsidiary leverage. |
| CLO outstanding principal | `1.592073B USD` | Securitized/CLO funding layer. |
| Unsecured notes outstanding principal | `5.325B USD` | Largest named debt-funding layer. |
| Asset coverage per unit | `1,869 USD per 1,000 USD debt` | Regulatory leverage context. |

Selected note instruments:

| Instrument | Principal |
|---|---:|
| July 2026 Notes | `1.000B USD` |
| 2027 Notes | `500M USD` |
| April 2027 Notes | `325M USD` |
| July 2027 Notes | `250M USD` |
| 2028 Notes | `850M USD` |
| June 2028 Notes | `100M USD` |
| September 2028 Notes | `400M USD` |
| 2029 Notes | `1.000B USD` |
| 2030 Notes | `500M USD` |
| 2031 Notes | `400M USD` |

## Portfolio Context

| Metric | Q2 2026 Value | Read |
|---|---:|---|
| Portfolio companies | `229` | Broad borrower base. |
| Industries | `30` | OBDC is not a single-sector lender. |
| First-lien senior secured debt fair value | `10.937849B USD` | The main asset destination is first-lien debt. |
| First-lien senior secured debt share | `73.2%` | First-lien lending dominates the portfolio. |
| Debt investments at floating rates | `96.0%` | Floating-rate exposure dominates. |
| Weighted average total yield at fair value | `9.9%` | Portfolio yield context. |
| Non-accrual at fair value | `0.8%` | Filed credit-quality context. |
| Q2 2026 new investment commitments | `319M USD` | Current-quarter origination activity. |
| Q2 2026 sales and repayments | `747M USD` | Current-quarter portfolio turnover. |

## Joint-Venture Clue

OBDC's Credit SLF disclosure gives one deeper source-of-capital clue:

| Metric | Q2 2026 Value | Read |
|---|---:|---|
| Credit SLF investments at fair value | `2.624338B USD` | Joint-venture portfolio scale. |
| Credit SLF total debt | `2.069196B USD` | Joint-venture leverage. |
| Credit SLF members' equity | `607.155M USD` | Member-capital layer. |
| OBDC economic ownership of Credit SLF | `64.4%` | OBDC is the majority economic member. |
| State Teachers Retirement System of Ohio economic ownership of Credit SLF | `12.5%` | A named institutional participant appears in the JV member table. |

This is useful because it starts to show how public/private credit vehicles can sit beside pension/institutional capital.

But it does not prove that Credit SLF held Precinmac, or that any pension/institutional capital funded the Precinmac-specific OBDC exposure.

## Borrower Case This Upgrades

| Borrower | OBDC Holder Evidence In Current Map | Upgrade From This Pass |
|---|---:|---|
| Precinmac / Paris US Holdco Inc. dba Precinmac | `21.412M USD` fair value plus `8.372M USD` unfunded delayed-draw and revolver commitments from the captured FY2024 OBDC schedule | OBDC row can now be tied to a Blue Owl-advised public BDC with public equity, a large unsecured-note stack, SPV/CLO financing, a revolving credit facility, and regulatory asset-coverage disclosure. |

## Claim Upgrade

Before this pass:

OBDC was a named Blue Owl holder in the Precinmac crosswalk.

After this pass:

OBDC is a public BDC funding channel with `15.354604B USD` of assets, `7.903533B USD` of balance-sheet debt, `7.031759B USD` of net assets, `5.325B USD` of unsecured notes principal, `1.592073B USD` of CLO principal, `996.700M USD` of SPV asset-facility principal, a `4.000B USD` revolving credit facility, and `493.142569M` common shares outstanding.

## What This Still Does Not Prove

This pass does not prove:

- the ultimate common shareholders of OBDC
- holders of OBDC unsecured notes or CLO debt
- whether Blue Owl corporate-balance-sheet capital funded any borrower loan
- whether any insurance account supplied capital to OBDC
- whether Credit SLF or State Teachers Retirement System of Ohio funded the Precinmac exposure
- which OBDC funding layer maps specifically to Precinmac
- total facility size for Precinmac
- whether private credit replaced bank credit in Precinmac

## Current Bottom Line

For the Precinmac-linked OBDC row, the immediate source-of-capital answer is now a Blue Owl-advised public BDC balance sheet:

OBDC had `15.354604B USD` of assets, `7.903533B USD` of debt, and `7.031759B USD` of net assets at Q2 2026. Its funding stack includes `5.325B USD` of unsecured notes principal, `1.592073B USD` of CLO principal, `996.700M USD` of SPV asset-facility principal, a `4.000B USD` revolving credit facility, public common equity, and `1,869 USD per 1,000 USD debt` asset coverage. That supports a public-BDC private-credit channel claim for Precinmac, but not a Blue Owl corporate, insurer-funded, total-facility, or bank-displacement claim.
