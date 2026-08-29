# Capital Flow Capital Source To Vehicle Bridge Pass 1

## Purpose

This pass answers the next source-of-funds question:

`When a holder vehicle appears in a borrower schedule, what can we say about the capital stack behind that vehicle, and what still cannot be tied to the borrower?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-capital-source-to-vehicle-bridge-pass-1.csv`

## Current Answer

The immediate source-of-capital answer is now split into three layers:

1. **Visible holder vehicle:** proven by borrower schedules, transaction sources, or taxonomy.
2. **Vehicle funding stack:** proven only when the vehicle's own report has been extracted.
3. **Borrower-specific source allocation:** still mostly unproven because a BDC or private-credit vehicle normally does not say which liability, note, shareholder dollar, facility, or investor funded a specific borrower loan.

The safe current answer is:

`Named borrowers are visibly financed or held through public BDCs, non-traded BDC/private-credit vehicles, direct-lending programs, registered credit funds, private funds, and arranger-only transaction sources. For ARCC, FSK, OBDC, and K-FITS, the vehicle funding stacks are now partly extracted. For most other vehicles, the channel is classified but the source stack still needs annual reports, prospectuses, funding notes, and capital-structure disclosures.`

## Vehicle Source Buckets

| Bucket | Vehicles | Current Read |
|---|---|---|
| Public BDC funding stack extracted | ARCC, FSK, OBDC, GSBD | Public BDC equity/net assets plus debt stacks, including unsecured notes, revolving or funding facilities, CLO/SPV facilities, preferred stock where applicable, and asset-coverage disclosure. |
| Non-traded / wealth-channel stack extracted | K-FITS, ASIF | Class S or multi-class shareholder equity/net assets, offering or distribution-channel mechanics, debt facilities, notes, and asset-coverage disclosure are visible. |
| Non-listed BDC / private-credit stack extracted | GSPCC | Class I, Class S, and Class D net-asset capital, revolving credit facilities, unsecured notes, and asset-coverage disclosure are visible. |
| Direct-lending program stack extracted | SDLP | ARCC/Varagon joint-venture capital, senior notes, intermediate funding notes, subordinated certificates, and members' capital are visible. |
| Vehicle channel visible, source stack needed | New Mountain Private Credit Fund, CION Ares Diversified Credit Fund | Borrower holdings or commitments are visible, but vehicle-level funding sources still need extraction. |
| Historical channel visible, current refresh needed | Cliffwater Corporate Lending Fund, Phillip Street Middle Market Lending Fund | Historical borrower exposure exists, but current exposure and source stack require refresh. |
| Prior bank denominator visible | Bank of America-led Atwell facility | Prior bank source is known, but repayment/replacement/coexistence status is unknown. |
| Arranger role visible, funded allocation needed | Ares Management Corporation | Ares transaction role is visible, but arranger role is not source-of-funds proof. |

## Extracted Funding-Stack Examples

| Vehicle | Borrower Cases | Visible Funding Stack | Claim Upgrade | Boundary |
|---|---|---|---|---|
| ARCC | Valcourt; Sunvair; AeriTek; MAI | `30.498B USD` total assets, `15.773B USD` debt carrying value, `13.891B USD` stockholders' equity, senior securities, unsecured notes, revolvers/funding facilities, CLO notes/secured loans. | ARCC borrower rows are public-BDC balance-sheet exposure. | Not Ares corporate money, not insurance money, not borrower-specific funding allocation. |
| FSK | Frontline; Atwell | `11.994B USD` total assets, `6.471B USD` debt, `5.118B USD` stockholders' equity, `150M USD` preferred stock, unsecured notes, revolvers, CLO notes. | FSK borrower rows are public-BDC-funded private-credit exposure. | Not KKR corporate money, not Global Atlantic insurance funding, not bank displacement. |
| OBDC | Precinmac | `15.354604B USD` total assets, `7.903533B USD` debt, `7.031759B USD` net assets, unsecured notes, CLO debt, SPV asset facilities, `4.000B USD` revolver. | OBDC's Precinmac row is tied to a Blue Owl public BDC capital stack. | Not Blue Owl corporate funding, not insurer funding, not Credit SLF funding of Precinmac. |
| K-FITS | Frontline; Atwell | `1.610755B USD` total assets, `572.938M USD` debt, `1.006058B USD` shareholders' equity, Class S shares, continuous private offering, placement agents, broker/advisor distribution, three revolvers. | K-FITS is a filed non-traded/wealth-channel private-credit vehicle. | Final shareholders, insurer participation, and borrower-specific funding allocation remain unknown. |
| GSBD | Frontline; Relation | `3.287804B USD` total assets, `1.850308B USD` debt, `1.357650B USD` net assets, `1.475B USD` revolving credit facility commitment, `1.2B USD` unsecured notes principal, and `172%` asset coverage. | GSBD borrower rows are Goldman-managed public-BDC-funded private-credit exposure. | Not Goldman Sachs corporate money, not insurance funding, not borrower-specific funding allocation. |
| GSPCC | Frontline; Relation | `18.671894B USD` total assets, `8.859977B USD` debt, `9.194048B USD` net assets, Class I/Class S/Class D shares, `7.175B USD` committed revolving credit facilities, `4.010B USD` unsecured notes principal, and `202%` asset coverage. | GSPCC commitment rows are non-listed BDC/private-credit capacity exposure. | Not funded fair value, not Goldman Sachs corporate money, not final shareholder mix, not borrower-specific funding allocation. |
| ASIF | Frontline; Sunvair; AeriTek; MAI | `22.350746B USD` total assets, `11.021485B USD` debt carrying value, `10.503550B USD` net assets, funding facilities, CLO debt, unsecured notes, Class I/Class S/Class D shares, and `192%` asset coverage. | ASIF borrower rows are Ares-managed non-traded BDC/private-credit funding-stack exposure. | Not final shareholder identity, not insurance funding, not Ares corporate money, not borrower-specific funding allocation. |
| SDLP | Valcourt; Precinmac | `4.595B USD` total assets, `3.519B USD` liabilities, `3.270B USD` senior notes, `108M USD` intermediate funding notes, `1.076B USD` subordinated certificates and members' capital, ARCC/Varagon capital structure. | SDLP rows are ARCC/Varagon direct-lending-program funding-stack exposure. | Not Varagon client identities, not insurance funding, not borrower-specific funding allocation, not Q2 borrower-exit proof. |

## What This Says

This bridge lets the research say:

- a borrower row appears in a public BDC, non-traded BDC/private-credit vehicle, direct-lending program, registered fund, private fund, bank facility, or arranger-only source
- some visible vehicles have extracted funding stacks
- vehicle capital stacks often include both equity/subscription capital and debt/leverage
- borrower-level holder evidence is stronger than platform AUM, but still weaker than source-to-borrower allocation

## What This Does Not Say

Do not say:

- a BDC holder row proves the ultimate investor
- an Ares-managed vehicle means Ares corporate balance-sheet money funded the borrower
- a KKR/FS vehicle means Global Atlantic insurance liabilities funded the borrower
- a public BDC row identifies the noteholders or shareholders behind the loan
- a non-traded BDC row proves retail wealth funded the specific borrower loan
- a vehicle funding stack allocates specific liabilities to specific borrower loans

## Next Proof Order

1. Extract New Mountain Private Credit Fund and New Mountain Guardian IV documents for the MAI sponsor-adjacent channel.
2. Extract CION Ares Diversified Credit Fund annual report, prospectus, adviser/sub-adviser agreement, and leverage notes for the Sunvair registered-fund channel.
3. Refresh Cliffwater and Phillip Street current schedules before treating historical Valcourt/Relation rows as current source evidence.
4. Follow ASIF and SDLP deeper into shareholder, noteholder, facility-lender, and Varagon-client evidence where public.
5. Use borrower credit agreements or rating reports before allocating any vehicle funding stack to a specific borrower facility.

## Safe Claim

`The source-of-capital evidence now supports a layered claim: named borrowers appear in visible credit vehicles, and several of those vehicles have identifiable funding stacks made up of equity/subscription capital, unsecured notes, credit facilities, CLO/SPV funding, preferred stock, or other leverage. The evidence does not yet prove which ultimate investors or liabilities funded a specific borrower loan, so source-to-borrower allocation remains a separate proof gate.`
