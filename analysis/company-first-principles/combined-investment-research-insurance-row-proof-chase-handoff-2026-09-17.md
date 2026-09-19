# Insurance statutory row-proof chase handoff

Research date: `2026-09-17`

## Purpose

This handoff turns the insurance statutory owner-cash workbench into a bounded
row-level work queue. It records what the public search has already tested,
what each selected row can currently support, the next joinable document, and
the exact condition that would stop or promote the claim. It is deliberately a
chase ledger, not another summary of statutory income.

The governing chain is:

`legal entity -> named asset/CUSIP -> borrower or collateral use -> income/proceeds -> receipt or settlement -> liability cost -> credit/capital treatment -> remittance -> common-owner return`

Until the chain reaches receipt and liability cost, consideration remains a
candidate, statutory income remains an insurer-level observation, and any
platform-level return remains unproven.

## Current decision surface

| Route | Current public-search state | Strongest safe claim | Next joinable object | Promotion stop condition |
|---|---|---|---|---|
| AP Aristotle / `00264#-AB-3` | Exact Athene route searched; current instrument, 2025 paydown, borrower repayment, custodian ledger, and settlement were not found. Older Barings filings are analogs only. | Athene has a selected `$300.834M` book-value row, `$28.318M` received-interest field, and `$776.032348M` cash-like candidate; no current receipt or settlement proof. | Exact CUSIP trade confirmation, note-purchase or payoff notice, custodian settlement statement, borrower repayment record, and Athene cash receipt. | Do not promote if the document identifies only an older AP Aristotle facility, a mark, or a sale consideration without payment and lot continuity. |
| AMAPS 1 / `02300A-AA-8` | One DealX route appears access-controlled. Public Apollo/Athene disclosure confirms a `$2.550B` concentration target; AMAPS 4/5 sources are wrapper and waterfall analogs. | Athene's `$1.918B` statutory row can be compared with a public AMAPS 1 concentration target; no collateral tape, trustee remittance, allocation, or liability-adjusted return proof. | AMAPS 1 offering/tranche documents, collateral schedule, trustee remittance, Athene allocation/custody record, subsidiary reconciliation, and credited-liability-cost schedule. | Do not promote from AMAPS 4/5 analogs, public concentration, or wrapper language. A promotion requires AMAPS 1-specific cash and entity allocation. |
| Concord / `20633K-AN-8` | Public borrower/use material improves the wrapper route, but no matched Athene receipt, payoff, trustee, or allocation record is closed. | A `$229.053M` same-CUSIP cash-like consideration candidate is linked to the selected statutory row; borrower/use remains a proxy. | Note purchase or offering document, royalty-collateral schedule, borrower payment/payoff, trustee or custodian receipt, and Athene lot reconciliation. | Do not promote from borrower identity, royalty description, or same-CUSIP matching alone; payment and ownership continuity must agree. |
| Accordia private marker / `90231*-AA-0` | The issuer/security coordinate is unresolved. Existing statutory row is useful for selection, not for borrower attribution. | Accordia has a `$202.125M` / `$17.419245M` selected private-marker surface; no reliable named issuer, borrower use, receipt, or return. | Full Schedule D coordinate, statement footnote, private-placement identifier, custodian security master, and any related credit agreement. | Stop borrower analysis until the marker resolves to a legal issuer and instrument; do not infer from KKR affiliate adjacency. |
| Intel / `458140-BM-1` | CUSIP, book value, interest, and candidate disposal fields are visible; settlement and remittance remain open. | `$66.418M` book value, `$2.902M` received interest, `$1.406M` consideration candidate, and `$(0.192)M` gain/loss candidate. | Sale confirmation, maturity/payoff notice, cash receipt, lot-level Schedule D continuity, and capital/impairment treatment. | Do not call the candidate cash or return until disposal date, proceeds, gain/loss, and receipt reconcile. |
| Orange / `685218-AB-5` | Same pattern as Intel: named row and candidate disposal fields, but no payment or owner allocation. | `$19.338M` book value, `$0.906M` received interest, `$0.146M` consideration candidate, and `$(0.010)M` gain/loss candidate. | Sale confirmation, receipt ledger, lot continuity, and insurer-to-parent remittance evidence. | Do not use the realized-loss field as an after-cost return; liability cost, capital, and parent claims remain open. |

## Request order

1. Request the exact CUSIP and legal-entity document set for AP Aristotle,
   AMAPS 1, and Concord before expanding the public search.
2. For each row, obtain one settlement or receipt object and one lot-continuity
   object. A source that proves identity but not payment does not close the row.
3. Add the insurer liability bridge: credited rate, funds-held or reinsurance
   balance, policyholder liability allocation, taxes, fees, and RBC/capital
   usage.
4. Reconcile subsidiary cash to parent distributions, fees, preferred/NCI
   claims, and common residual.
5. Only then calculate cash-on-cash return, IRR, NPV, ROIC, or a ranking.

## Evidence discipline

- Publicly confirmed platform concentration is not a subsidiary receipt.
- Statutory interest received is not borrower repayment.
- A same-CUSIP candidate is not a settlement unless amount, date, lot, and
  payment route agree.
- A wrapper name is not proof of ultimate borrower, collateral, or use of
  proceeds.
- Realized gain/loss is not an owner return without liability cost, taxes,
  capital, and remittance.
- Older analog filings are retained as context and never merged into the
  current Athene instrument.

## Handoff decision

The insurance lane remains `qualified; no-ranking`. The next useful work is
controlled-document or custodian-level row proof for AP Aristotle, AMAPS 1, and
Concord, followed by the Accordia marker resolution. Broad description search
has diminishing value because the highest-value public routes are now bounded:
AP Aristotle is searched-negative for the exact current route, and AMAPS 1 is
access-controlled or analog-only for the required proof families.

The machine-readable queue is in the [row-proof chase table](data/combined-investment-research-insurance-row-proof-chase-handoff-2026-09-17.csv).

The [latest Accordia coordinate extraction](capital-flow-kkr-global-atlantic-accordia-matched-disposal-coordinate-extraction-pass-1.md)
strengthens the Intel, Commonwealth Edison, and Orange rows to
`coordinate-disposal-columns-visible`. It records aggregate statutory
consideration of `1.552579M USD`, book/adjusted carrying value at disposal of
`1.754251M USD`, and realized gain/loss of `-201.672K USD`. The upgrade remains
below settlement-cash proof: custodian receipt, lot continuity, borrower use,
liability-cost spread, remittance waterfall, collateral, and return remain open.

The parallel [Athene raw-text inspection](capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-raw-text-inspection-pass-1.md)
found all `19` selected statutory rows across `8` CUSIPs and `14` pages; `17`
are inspection-ready and `2` require page-specific column interpretation. The
result strengthens source-row availability while preserving the hold on column
semantics, borrower receipt, liability spread, and return.

The [Concord public document acquisition attempt](capital-flow-apollo-athene-concord-public-document-acquisition-attempt-pass-1.md)
tested all `8` controlled-document families. It located `3` access-controlled
offering/indenture/rating routes and `2` public use-of-proceeds or collateral
proxies, but produced `0` Athene-receipt upgrades and `0` return-model upgrades.
The next action is controlled-document access and trustee/Athene requests, not
another broad public search.

For the Accordia comparison route, the [matched-disposal settlement request packet](capital-flow-kkr-global-atlantic-accordia-matched-disposal-settlement-request-packet-pass-1.md)
now names the three CUSIPs, disposal dates, statutory consideration, and the
broker/custodian, lot-continuity, cash-receipt, and liability-cost records
needed for promotion. This is a source request, not settlement proof.

## Related records

- [Insurance statutory owner-cash promotion workbench](combined-investment-research-insurance-statutory-owner-cash-promotion-workbench-2026-09-17.md)
- [AP Aristotle public-search refresh](capital-flow-apollo-athene-aristotle-public-search-refresh-2026-09-16.md)
- [AMAPS public document acquisition attempt](capital-flow-apollo-athene-amaps-public-document-acquisition-attempt-pass-1.md)
- [Apollo/KKR statutory named-asset selection](capital-flow-apollo-kkr-statutory-named-asset-selection-pass-1.md)
- [Concord public document acquisition attempt](capital-flow-apollo-athene-concord-public-document-acquisition-attempt-pass-1.md)
- [Accordia matched-disposal settlement request packet](capital-flow-kkr-global-atlantic-accordia-matched-disposal-settlement-request-packet-pass-1.md)
