# Insurance Named-Asset Proof Ladder

Research date: `2026-09-17`

## Purpose

This ladder consolidates the strongest current named-asset observations from
the Apollo/Athene and KKR/Global Atlantic/Accordia routes. It is a comparison
surface, not a ranking or a return model.

The structured companion table is:

`analysis/company-first-principles/data/combined-investment-research-insurance-named-asset-proof-ladder-2026-09-17.csv`

The repeated chain is:

`insurance legal entity -> named security or wrapper -> book value -> statutory income -> disposal consideration -> settlement/remittance -> liability cost -> owner return`

The current evidence reaches different points in that chain for different
rows. The ladder makes those differences explicit.

## Comparable row surface

| Platform / legal entity | Named asset | Book / exposure | Statutory income | Disposal / event evidence | Current proof grade |
|---|---|---:|---:|---:|---|
| Apollo / Athene | AP Aristotle Holdings LLC, `00264#-AB-3` | `$300.834M` | `$28.318M` received interest field | `$776.032M` cash-like candidate; `$6.588M` tax-free-exchange hold | cash-like candidate; settlement and allocation open |
| Apollo / Athene | AMAPS 1 LLC Tranche A, `02300A-AA-8` | `$1.918B` | `$48.871M` interest income | `$268.000M` cash-like candidate; wrapper and Athene-alignment evidence | wrapper/proceeds proxy; collateral and remittance open |
| Apollo / Athene | Concord Music Royalties LLC, `20633K-AN-8` | not promoted in selection table | not promoted in selection table | `$229.053M` same-CUSIP cash-like consideration | borrower/wrapper/use proxy; Athene receipt open |
| KKR / Accordia | 2023 Bear Financing L.P., `90231*-AA-0` | `$202.125M` | `$17.419M` received interest | no matched current-year disposal event | issuer resolved; settlement and borrower route open |
| KKR / Accordia | Intel Corp, `458140-BM-1` | `$66.418M` | `$2.902M` received interest | `$1.406M` coordinate-extracted consideration; `$(0.192M)` gain/loss | owned-interest/disposal join; settlement open |
| KKR / Accordia | Orange SA, `685218-AB-5` | `$19.338M` | `$0.906M` received interest | `$0.146M` coordinate-extracted consideration; `$(0.010M)` gain/loss | owned-interest/disposal join; settlement open |

## What the cross-platform comparison says

Apollo/Athene currently has the stronger named-proceeds and wrapper surface:
AP Aristotle and AMAPS have large same-CUSIP consideration candidates, while
Concord has the clearest public borrower/use proxy.

Accordia currently has the cleaner row-level income and disposal-column
surface: its coordinate extraction near-reconciles the `$7.318B` owned-bond
base and joins named interest rows to statutory consideration and gain/loss.
The Bear Financing row is now issuer-visible, but it has no matched disposal
event in the current table.

Neither platform has crossed the final proof gates. The public evidence does
not yet join a named row to a custodian or bank settlement, borrower cash,
trustee remittance, period-matched liability cost, or common-owner residual.

## QoE and financial-integrity controls

The ladder is designed to prevent four common analytical errors:

1. **Income-to-cash error.** Received interest is a statutory field, not proof
   of borrower-level cash or owner cash.
2. **Consideration-to-settlement error.** Disposal consideration is a stronger
   proceeds-column observation, but it is not a bank or custodian settlement.
3. **Gain/loss-to-return error.** Realized gain/loss excludes or may not expose
   taxes, fees, lot continuity, liability funding cost, hedges, and residual
   claims.
4. **Wrapper-to-borrower error.** AMAPS, Concord, AP Aristotle, and Bear
   Financing labels identify a route or issuer; they do not by themselves
   identify the ultimate borrower, collateral cash, or use of proceeds.

These are financial-shenanigans and quality-of-earnings prompts, not fraud
findings. A diagnostic becomes promotion-ready only when the same legal entity,
period, CUSIP or instrument, cash/claim object, and reconciliation path join.

## Next promotion bundle

The minimum comparable bundle is:

1. source-page row and exact lot or position identifier;
2. instrument or financing document;
3. dated settlement or remittance record;
4. borrower/collateral use and cash-flow evidence;
5. legal-entity liability-cost or funds-held allocation; and
6. return calculation with taxes, fees, losses, and residual claims.

Until that bundle exists, the correct cross-platform conclusion is:

`Apollo/Athene shows larger named-proceeds and wrapper candidates; Accordia shows cleaner coordinate-reconciled owned-bond income and disposal columns. Both are legal-entity cash-back proxies, not completed source-to-owner-return proofs.`

## Decision

`insurance-named-asset-cross-platform-proof-ladder-visible; settlement-liability-cost-and-owner-return-open`
