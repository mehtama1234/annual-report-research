# Capital Flow Holder Source-Of-Funds Map

## What This Adds

The borrower rollup tells us where the loans are landing. This pass asks who is visibly holding or arranging the credit.

Machine-readable table:

`analysis/company-first-principles/data/capital-flow-holder-source-of-funds-map.csv`

The key distinction is:

- `reporting_entity` is the legal vehicle that filed or appeared in the source.
- `manager_or_platform` is the asset-manager or lending platform connected to that vehicle.
- `capital_channel` is the conservative source-of-funds label we can infer from the vehicle type.

This does not prove the ultimate investor behind every dollar. It tells us the visible channel: public BDC, non-traded BDC/private credit fund, direct-lending program, middle-market lending fund, registered credit fund, bank facility, or arranger-only evidence.

## Simple Answer

The visible funding is not coming from one place.

It is a stack:

- public BDCs
- non-traded BDCs and private-credit funds
- Ares-linked direct-lending program vehicles
- Goldman Sachs private-credit vehicles
- New Mountain and other manager-specific private-credit funds
- transaction-arranger evidence where holder dollars have not appeared yet

So the clean simple answer is:

Private credit is funding operating-company platforms through a mix of listed BDC balance sheets, non-traded/private credit vehicles, and manager-run direct-lending programs. In the current evidence set, Ares-linked vehicles are the largest visible holder channel, but KKR/FS, Goldman Sachs, Blue Owl, New Mountain, Kayne, and CION/Ares also appear.

## Channel Rollup

These amounts are from the holder/source map and are in USD millions.

| Capital Channel | Funded Fair Value | Unfunded Commitment | Rows | Read |
|---|---:|---:|---:|---|
| Direct lending program / private credit vehicle | `595.5000` | `0.0000` | `2` | Large Ares-linked SDLP exposure to Valcourt and Precinmac. |
| Public BDC | `443.2010` | `10.5800` | `10` | ARCC, FSK, GSBD, OBDC, and Kayne provide repeat holder-dollar evidence. |
| Non-traded BDC / private credit fund | `166.8635` | `130.5210` | `8` | K-FITS, ASIF, and Goldman Sachs Private Credit show mixed funded and commitment exposure. |
| Middle-market lending fund | `27.8730` | `0.0000` | `1` | Phillip Street gives historical Relation exposure. |
| Private credit fund | `26.4970` | `12.4010` | `1` | New Mountain shows MAI drawn and undrawn exposure. |
| Registered credit fund | `2.5240` | `0.0000` | `1` | CION Ares shows smaller Sunvair exposure. |
| Bank credit facility | `0.0000` | `0.0000` | `1` | Atwell has a prior `200.0000M USD` bank-facility denominator. |
| Financing arranger role only | `0.0000` | `0.0000` | `1` | Jiffy has Ares arranger evidence and a `1300.0000M USD` transaction value but no holder row yet. |

## Manager / Platform Rollup

| Manager Or Platform | Funded Fair Value | Unfunded Commitment | Rows | Notes |
|---|---:|---:|---:|---|
| Ares-linked SDLP | `595.5000` | `0.0000` | `2` | Valcourt and Precinmac. |
| Ares | `368.2415` | `0.0000` | `9` | ARCC and ASIF rows across Valcourt, Frontline, Sunvair, AeriTek, MAI, plus Jiffy arranger-only evidence. |
| KKR / FS | `187.9220` | `0.8880` | `4` | Frontline and Atwell through FSK and K-FITS. |
| Goldman Sachs | `22.4870` | `131.8410` | `4` | Frontline and Relation through GSBD and GSPCC. |
| Blue Owl | `21.4120` | `8.3720` | `1` | Precinmac / Paris US Holdco. |
| New Mountain | `26.4970` | `12.4010` | `1` | MAI Capital. |
| Kayne Anderson | `10.0020` | `0.0000` | `1` | AeriTek. |
| CION / Ares | `2.5240` | `0.0000` | `1` | Sunvair. |
| Goldman Sachs / Phillip Street | `27.8730` | `0.0000` | `1` | Historical Relation exposure. |
| Bank lender group | `0.0000` | `0.0000` | `1` | Atwell prior bank facility denominator. |

## What We Can Now Claim

The evidence supports a sharper claim:

Private credit funding of operating companies is multi-channel. The same borrower can show up across public BDCs, non-traded BDCs, private-credit funds, and direct-lending program vehicles. That means the borrower-level exposure is not just a single lender story; it is a platform-distribution story.

This is especially clear in Frontline, Sunvair, AeriTek, MAI, Atwell, Relation, and Valcourt.

## What We Cannot Yet Claim

We still cannot say:

- the ultimate investor behind every dollar
- the share of funding supplied by insurance liabilities
- total debt outstanding for each borrower
- whether banks were fully displaced
- whether every loan funded productive investment rather than acquisition finance, refinancing, working capital, or sponsor distributions

Those require another layer of evidence.

## Next Work

1. Add vehicle taxonomy.

   Build a reference table for each reporting entity: public BDC, non-traded BDC, interval fund, private BDC, joint venture/direct-lending program, insurance-account vehicle, CLO, bank, or unknown.

2. Link vehicles to capital providers.

   For each holder, collect management agreement, 10-K/10-Q description, prospectus, or annual report language showing who advises the vehicle and where capital comes from.

3. Add insurer-source proof.

   For Apollo/Athene, KKR/Global Atlantic, Brookfield, Blackstone, and Ares, bridge from insurance liabilities or insurance AUM into the actual credit vehicles where possible. Do not assume that every manager credit fund is insurance-funded.

4. Build same-borrower syndication maps.

   For each borrower, list every holder by manager and channel. The research target is to find whether one borrower is financed by a manager-only stack, a cross-manager club, or a broader syndicated lender group.

5. Add facility denominators.

   Search for rating reports, credit agreements, lender announcements, UCC filings, and legal-advisor financing notes to convert holder slices into estimated or exact total debt packages.

## Current Bottom Line

We have moved from “private credit is investing somewhere” to a more testable statement:

Private credit is visibly reaching real operating companies through several capital channels, led in this sample by Ares-linked direct-lending vehicles and public BDCs, with meaningful non-traded/private-credit vehicle participation and visible unfunded commitments. The next proof gap is ultimate source of funds and total facility size.
