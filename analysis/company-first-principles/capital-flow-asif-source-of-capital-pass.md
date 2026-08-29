# Capital Flow ASIF Source-Of-Capital Pass

## Purpose

This is the third execution pass from the ultimate-source document queue.

Target: Ares Strategic Income Fund.

Question: when ASIF appears as a holder of loans to operating-company borrowers, what can we say about the capital stack and investor channel behind that vehicle?

Extraction table:

`analysis/company-first-principles/data/capital-flow-asif-source-of-capital-extractions.csv`

Primary source:

- `raw/primary-sources/capital-flow/aeritek/sec/asif-2026q1-n14-supplement.html`

## Simple Answer

ASIF is not just an Ares label.

The Q1 2026 filing describes ASIF as a Delaware statutory trust, a closed-end management investment company that has elected BDC regulation, and a RIC for tax purposes. It is externally managed by Ares Capital Management LLC, with Ares Operations LLC as administrator.

That upgrades ASIF-linked borrower rows from generic holder evidence to non-traded BDC/private-credit vehicle evidence.

It still does not prove the identity of each end investor or which funding layer supports a specific borrower loan.

## Vehicle Funding Snapshot

| Metric | Q1 2026 Value | Read |
|---|---:|---|
| Total investments at fair value | `21332.904M USD` | ASIF is a large credit vehicle, not a small side pocket. |
| Total assets | `22350.746M USD` | Balance-sheet scale behind captured borrower rows. |
| Debt carrying value | `11021.485M USD` | Roughly half the asset base is debt-funded. |
| Total liabilities | `11847.196M USD` | Liabilities fund `53.01%` of total assets. |
| Total net assets | `10503.550M USD` | Net-asset capital funds `46.99%` of total assets. |
| Asset coverage | `192%` | Regulatory leverage context for the BDC structure. |

Derived ratios:

| Ratio | Value | Read |
|---|---:|---|
| Debt carrying value / total assets | `49.31%` | ASIF is meaningfully levered. |
| Total liabilities / total assets | `53.01%` | Liability funding is slightly more than half of the asset stack. |
| Total net assets / total assets | `46.99%` | Shareholder/net-asset capital is the other major funding layer. |

## Debt Stack

| Funding Layer | Q1 2026 Principal Outstanding | Read |
|---|---:|---|
| Revolving and funding facilities | `3649.235M USD` | Bank/funding-facility style leverage. |
| CLO notes and debt | `1358.000M USD` | Structured-debt funding layer. |
| Unsecured notes | `6100.000M USD` | Largest named debt class in the extracted table. |
| Total principal amount outstanding | `11107.235M USD` | Filed debt-table total. |
| Total aggregate committed or outstanding debt instruments | `15533.000M USD` | Combines commitments and outstanding amounts, so it should not be treated as debt outstanding. |

Selected facility detail:

| Instrument | Principal Outstanding |
|---|---:|
| Revolving Credit Facility | `1461.424M USD` |
| SG Funding Facility | `1087.811M USD` |
| SB Funding Facility | `400.000M USD` |
| BNP Funding Facility | `700.000M USD` |

The SB Funding Facility also had `1125.000M USD` available at March 31 2026, with `375M USD` becoming fully available after October 29 2026.

## Shareholder And Distribution Channel

| Metric | Value | Read |
|---|---:|---|
| Class I net assets | `8350.694M USD` | Largest net-asset share class. |
| Class S net assets | `1308.956M USD` | Retail/intermediary-style distribution clue because the filing discusses servicing/distribution fees. |
| Class D net assets | `843.900M USD` | Smaller distribution-fee-bearing class. |
| NAV per share | `26.85 USD` | Same reported NAV for Class I, Class S, and Class D. |
| Common shares outstanding as of May 11 2026 | `395.313M shares` | Cover-page share count across Class I, Class S, and Class D. |

The distribution evidence matters because ASIF discusses Class S and Class D shareholder servicing/distribution fees, broker services, investor inquiries, distribution payments, reinvestments, share repurchase requests, and possible adviser-affiliate payments to selling agents or financial intermediaries.

That is a distribution-channel clue. It is not a holder list.

## Borrower Cases This Upgrades

| Borrower | ASIF Holder Evidence In Current Map | Upgrade From This Pass |
|---|---:|---|
| Frontline | `76.6927M USD` fair value | ASIF row can be tied to a large Ares-managed non-traded BDC/private-credit vehicle with debt, net assets, and distribution-channel disclosures. |
| Sunvair | `35.7504M USD` fair value | Same source-of-capital upgrade for aerospace MRO borrower exposure. |
| AeriTek | `1.7721M USD` fair value | Same vehicle-channel upgrade for refrigeration/foodservice equipment exposure. |
| MAI | `0.7263M USD` fair value | Same vehicle-channel upgrade for wealth-management consolidation exposure. |
| Current ASIF sample total | `114.9415M USD` fair value | Visible ASIF borrower rows in the current holder map. |

## Claim Upgrade

Before this pass:

ASIF was a named Ares-linked holder in several borrower schedules.

After this pass:

ASIF is a filed non-traded BDC/private-credit vehicle with `22.351B USD` of assets, `11.021B USD` of debt carrying value, `10.504B USD` of net assets, `192%` asset coverage, multiple debt facilities, CLO debt, unsecured notes, and Class I/Class S/Class D share classes.

## What This Still Does Not Prove

This pass does not prove:

- the names or types of the ultimate ASIF shareholders
- whether insurance liabilities fund ASIF shares, notes, or facilities
- whether Ares corporate balance sheet capital funds a specific loan
- which ASIF funding layer supports Frontline, Sunvair, AeriTek, or MAI
- total facility size for any borrower
- whether any borrower facility replaced bank debt

## Current Bottom Line

For ASIF-linked borrower rows, the source-of-capital answer is now stronger but still bounded:

The immediate holder channel is an Ares-managed non-traded BDC/private-credit vehicle with `22.351B USD` of assets, `11.021B USD` of debt carrying value, and `10.504B USD` of net assets at Q1 2026. Its debt stack includes funding facilities, CLO debt, and unsecured notes, while its share classes and distribution-fee disclosures point to an intermediated shareholder capital channel. The evidence supports a vehicle-channel claim, not an ultimate-investor or bank-displacement claim.
