# Capital Flow FSK Source-Of-Capital Pass

## Purpose

This is the fourth execution pass from the ultimate-source document queue.

Target: FS KKR Capital Corp.

Question: when FSK appears as a holder of loans to Frontline and Atwell, what can we say about the capital stack behind that public BDC?

Extraction table:

`analysis/company-first-principles/data/capital-flow-fsk-source-of-capital-extractions.csv`

Primary source:

- `raw/primary-sources/capital-flow/atwell/sec/fsk-2026q2-10q.html`

## Simple Answer

FSK is a public BDC route into private middle-market credit.

The Q2 2026 10-Q describes FSK as an externally managed, non-diversified, closed-end management investment company that has elected BDC regulation and RIC tax treatment. It is externally managed by FS/KKR Advisor LLC.

That upgrades the Frontline and Atwell FSK rows from “named holder” to “public BDC balance-sheet funding structure.”

It still does not prove that KKR corporate-balance-sheet capital, Global Atlantic insurance liabilities, or any specific bank facility funded the borrower loans.

## Vehicle Funding Snapshot

| Metric | Q2 2026 Value | Read |
|---|---:|---|
| Total investments at fair value | `11.418B USD` | Scale of FSK investment portfolio. |
| Total assets | `11.994B USD` | Balance-sheet denominator. |
| Debt, net of deferred financing costs and discount | `6.471B USD` | Main leverage layer in the balance sheet. |
| Total liabilities | `6.726B USD` | Liability funding is `56.08%` of assets. |
| Preferred stock liquidation preference | `150M USD` | Separate preferred-stock funding layer. |
| Total stockholders' equity | `5.118B USD` | Public BDC equity layer. |
| NAV per common share | `18.30 USD` | Common-share NAV at period end. |
| Common shares outstanding as of August 5 2026 | `276.340280M shares` | Public-shareholder channel clue, not investor identity. |

Derived ratios:

| Ratio | Value | Read |
|---|---:|---|
| Debt carrying value / total assets | `53.95%` | FSK is meaningfully levered. |
| Total liabilities / total assets | `56.08%` | Liabilities fund more than half of assets. |
| Stockholders' equity / total assets | `42.67%` | Equity remains a large funding layer. |

## Debt And Senior Securities

| Funding Layer | Q2 2026 Amount | Read |
|---|---:|---|
| Total amount outstanding including preferred stock | `6.641B USD` | Filed financing-arrangements total. |
| Total amount available | `3.052B USD` | Undrawn funding capacity. |
| Revolving credit facilities outstanding | `1.098B USD` | Callowhill plus Senior Secured Revolving Credit Facility. |
| Revolving credit facilities available | `3.052B USD` | All reported availability sits in the two revolving facilities. |
| Unsecured notes outstanding | `4.650B USD` | Largest named funding class. |
| CLO notes outstanding | `743M USD` | Structured-debt layer. |
| Asset coverage per unit | `1.77x` | Equivalent to roughly `177%` asset coverage context. |

Selected instruments:

| Instrument | Outstanding | Available | Maturity |
|---|---:|---:|---|
| Callowhill Credit Facility | `365M USD` | `35M USD` | June 2 2030 |
| Senior Secured Revolving Credit Facility | `733M USD` | `3017M USD` | July 16 2030 |
| Largest unsecured notes class, 7.500% due 2031 | `900M USD` | `0` | August 1 2031 |
| CLO-2 Notes | `380M USD` | `0` | April 15 2037 |
| CLO-3 Notes | `363M USD` | `0` | January 15 2038 |

## Direct-Origination Context

| Metric | Q2 2026 Value | Read |
|---|---:|---|
| Portfolio companies in all direct originations | `223` | FSK is a broad direct-lending vehicle. |
| Total fair value of direct originations | `11.0385B USD` | Most of the portfolio is direct-originated credit. |
| Direct originations as share of total investments | `96.7%` | Strong fit with the private-credit borrower-destination thesis. |
| Non-accrual share by fair value | `3.3%` | Portfolio credit-quality context. |
| Weighted average annual yield on accruing debt investments | `9.8%` | Portfolio yield context. |

## Borrower Cases This Upgrades

| Borrower | FSK Holder Evidence In Current Map | Upgrade From This Pass |
|---|---:|---|
| Frontline Road Safety | `132.8000M USD` fair value | FSK row can be tied to a public BDC with `11.994B USD` of assets, debt facilities, unsecured notes, CLO notes, preferred stock, and common equity. |
| Atwell | `3.2000M USD` fair value plus `0.4000M USD` unfunded commitment | Same public-BDC funding-stack upgrade for the Atwell bank-replacement candidate. |
| Current FSK sample total | `136.0000M USD` fair value plus `0.4000M USD` unfunded | Visible FSK borrower rows in the current holder map. |

## Claim Upgrade

Before this pass:

FSK was a named holder of Frontline and Atwell debt in borrower schedules.

After this pass:

FSK is a public BDC funding channel with `11.994B USD` of assets, `6.471B USD` of balance-sheet debt, `5.118B USD` of stockholders' equity, `4.650B USD` of unsecured notes, `1.098B USD` of revolving-credit-facility borrowings, `743M USD` of CLO notes, and `150M USD` of preferred stock.

## What This Still Does Not Prove

This pass does not prove:

- the ultimate common shareholders of FSK
- the holders of FSK unsecured notes or CLO notes
- whether Global Atlantic or any insurer supplied capital to FSK
- whether any FSK funding layer maps specifically to Frontline or Atwell
- total facility size for Frontline or Atwell
- whether Atwell's 2026 private-credit facility repaid or replaced the 2024 Bank of America-led facility

## Current Bottom Line

For FSK-linked borrower rows, the immediate source-of-capital answer is now a public BDC balance sheet:

FSK had `11.994B USD` of assets, `6.471B USD` of debt, `5.118B USD` of common stockholders' equity, and `150M USD` of preferred stock at Q2 2026. Its funding stack includes revolving credit facilities, unsecured notes, CLO notes, preferred stock, and common equity. That is enough to classify Frontline and Atwell FSK exposure as public-BDC-funded private credit, but not enough to claim KKR corporate funding, insurance funding, or bank displacement.
