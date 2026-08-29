# Capital Flow Vehicle Capital Stack Decomposition Pass 1

## Purpose

This pass resolves `CFARQ-009`:

`Can public BDC and adjacent BDC/private-credit holder rows be upgraded from vehicle-visible evidence to vehicle funding-stack evidence?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-vehicle-capital-stack-decomposition-pass-1.csv`

## Resolution Outcome

`upgrade-with-boundary - target vehicle funding stacks visible, borrower-specific source allocation still missing`

The queue item passes at the vehicle-stack level. ARCC, FSK, OBDC, GSBD, and GSPCC each now have same-period vehicle-level evidence for asset base, debt/leverage, equity or net assets, asset-coverage context, and borrower or commitment links.

The upgrade is bounded. A BDC funding stack does not identify which shareholder dollar, noteholder dollar, bank facility, CLO/SPV facility, or subscription dollar funded a specific borrower loan. Borrower-specific source allocation remains a separate proof gate.

## Target Vehicle Summary

| Vehicle | Channel | Period | Assets | Debt | Equity / Net Assets | Asset Coverage | Borrower Links | Status |
|---|---|---|---:|---:|---:|---|---|---|
| Ares Capital Corporation | public BDC | Q2 2026 | `30.498000B USD` | `15.773000B USD` | `13.891000B USD` | `186%` | Valcourt; Sunvair; AeriTek; MAI Capital | source-stack visible |
| FS KKR Capital Corp. | public BDC | Q2 2026 | `11.994000B USD` | `6.471000B USD` | `5.118000B USD` | `1.77x` | Frontline Road Safety; Atwell | source-stack visible |
| Blue Owl Capital Corporation | public BDC | Q2 2026 | `15.354604B USD` | `7.903533B USD` | `7.031759B USD` | `186.9% equivalent` | Precinmac | source-stack visible |
| Goldman Sachs BDC Inc. | public BDC | Q2 2026 | `3.287804B USD` | `1.850308B USD` | `1.357650B USD` | `172%` | Frontline Road Safety; Relation Insurance | source-stack visible |
| Goldman Sachs Private Credit Corp. | non-listed BDC / private credit vehicle | Q2 2026 | `18.671894B USD` | `8.859977B USD` | `9.194048B USD` | `202%` | Frontline Road Safety; Relation Insurance commitments | source-stack visible |

GSPCC is included because the queue target named it, but it should not be described as an exchange-listed public BDC. It is a non-listed BDC/private-credit vehicle with Class I, Class S, and Class D share classes.

## What This Answers

The source-of-capital answer can now move up one level for these vehicles:

`Selected borrower rows are not only named holder rows. They sit inside disclosed BDC or BDC-like vehicle capital stacks made up of shareholder/net-asset capital, unsecured notes, revolving or funding facilities, CLO/SPV debt, preferred stock where applicable, and regulatory asset-coverage constraints.`

This is stronger than platform AUM and stronger than a borrower schedule alone.

## Borrower Upgrades

| Borrower | Vehicle Stack Now Visible | Claim Upgrade |
|---|---|---|
| Valcourt | ARCC; SDLP separately outside this public-BDC pass | Q2 2026 ARCC Valcourt exposure is public-BDC funding-stack visible. |
| Sunvair | ARCC | Q2 2026 ARCC Sunvair exposure is public-BDC funding-stack visible. |
| AeriTek | ARCC | Q2 2026 ARCC AeriTek exposure is public-BDC funding-stack visible. |
| MAI Capital | ARCC; New Mountain and ASIF remain separate vehicle-channel questions | Q2 2026 ARCC MAI exposure is public-BDC funding-stack visible. |
| Frontline Road Safety | FSK; GSBD; GSPCC commitment channel | Frontline has public-BDC and non-listed BDC/private-credit funding-stack visibility, while facility mapping remains incomplete. |
| Atwell | FSK | FSK's Atwell rows are public-BDC funding-stack visible, but the bank-replacement test remains unresolved. |
| Precinmac | OBDC | OBDC's Precinmac row is Blue Owl-advised public-BDC funding-stack visible. |
| Relation Insurance | GSBD; GSPCC commitment channel | Relation has Goldman public-BDC and non-listed BDC/private-credit funding-stack visibility, while row-to-facility mapping remains incomplete. |

## What This Does Not Answer

This pass does not prove:

- ultimate common shareholder identity
- noteholder identity
- insurance-liability funding
- manager corporate-balance-sheet funding
- which funding layer financed a specific borrower position
- total facility size for any borrower
- bank replacement at borrower level
- final use of proceeds

## Claim Upgrade

Before this pass, the safe language was:

`Holder vehicles are visible, but source stacks are only partly extracted.`

After this pass, the safer upgraded language is:

`For ARCC, FSK, OBDC, GSBD, and GSPCC, the visible borrower rows can be tied to disclosed vehicle capital stacks. The immediate source channel is a BDC or BDC-like balance sheet funded by equity or net assets plus leverage layers such as unsecured notes, revolvers, credit facilities, CLO/SPV financing, preferred stock where applicable, and subscription/share-class capital where applicable.`

## Boundary Language

Use this boundary in external writing:

`Vehicle-stack visibility is not ultimate-source allocation. A BDC balance sheet can show the mix of equity, debt, notes, facilities, and other leverage behind a portfolio, but it usually does not say which liability or investor funded a named borrower loan.`

## Next Source Targets

| Target | Why It Matters |
|---|---|
| Shareholder and noteholder evidence for ARCC, FSK, OBDC, and GSBD | Moves from balance-sheet stack to ultimate investor or liability owner. |
| GSPCC subscription and shareholder concentration disclosures | Clarifies the non-listed BDC/private-credit investor channel. |
| Revolver and funding-facility lender tables | Shows where banks remain at the vehicle-financing layer even when borrower loans are private credit. |
| CLO/SPV collateral notes | Tests whether any borrower positions can be tied to financing subsidiaries. |
| Borrower credit agreements and rating reports | Still required to allocate facility size, lender group, use of proceeds, and bank role. |

## Safe Answer

`CFARQ-009 upgrades the source-of-capital answer one level. For ARCC, FSK, OBDC, GSBD, and GSPCC, borrower or commitment rows are now tied to disclosed vehicle capital stacks. The evidence supports public-BDC or non-listed BDC/private-credit funding-stack language, but not ultimate shareholder, noteholder, insurance-liability, corporate-balance-sheet, borrower-specific funding allocation, facility-size, use-of-proceeds, or bank-replacement claims.`
