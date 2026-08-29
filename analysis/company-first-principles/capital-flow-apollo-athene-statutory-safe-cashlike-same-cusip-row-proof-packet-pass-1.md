# Capital Flow Apollo Athene Statutory Safe Cash-Like Same-CUSIP Row Proof Packet Pass 1

## Purpose

This pass takes the highest-dollar same-CUSIP rows from the safe cash-like proceeds summary and builds a row-level proof packet.

The question is:

`For the strongest named Athene cash-like proceeds candidates, can we show the year-end holding row and the disposal/proceeds row under the same CUSIP, with the cash-like amount separated from any noncash hold?`

The summary table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-row-proof-packet-pass-1.csv`

The row detail table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-row-proof-packet-detail-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-row-proof-packet-diagnostic-pass-1.csv`

The builder is:

`scripts/build-athene-safe-cashlike-same-cusip-row-proof-packet.py`

## Main Result

The packet selects the top `10` same-CUSIP cash-like candidates from the corrected full-universe proceeds summary.

| Metric | Value |
|---|---:|
| selected summary rows | `10` |
| selected source detail rows | `26` |
| selected year-end holding rows | `10` |
| selected disposal/proceeds rows | `16` |
| selected disposal consideration | `2.943066208B USD` |
| selected cash-like disposal consideration | `2.930192972B USD` |
| selected noncash/transfer hold consideration | `12.873236M USD` |
| selected cash-like share | `99.5626%` |
| selected year-end book value | `3.509210632B USD` |
| selected consideration / year-end book value | `83.8669%` |
| selected safe realized gain/loss | `-27 USD` |
| selected disposal interest/dividends received | `93.704267M USD` |

## Selected Named Rows

| Safe rank | CUSIP | Issuer / description | Main class | Cash-like consideration | Verdict |
|---:|---|---|---|---:|---|
| 1 | `00264#-AB-3` | AP Aristotle Holdings LLC | principal-paydown-cash-candidate | `776.0M USD` | mixed cash-like/noncash hold |
| 7 | `28655*-AA-7` | Eliant Invest Holding LP B | market-sale-or-counterparty-cash-candidate | `358.3M USD` | clean cash-like candidate |
| 8 | `00024D-AL-7` | AA Infrastructure Fund 2 LLC | mixed; includes tax-free exchange hold | `348.0M USD` | mixed cash-like/noncash hold |
| 10 | `02300A-AA-8` | AMAPS 1 LLC | market-sale-or-counterparty-cash-candidate | `268.0M USD` | clean cash-like candidate |
| 16 | `20633K-AN-8` | Concord Music Royalties LLC | market-sale-or-counterparty-cash-candidate | `229.1M USD` | clean cash-like candidate |
| 20 | `592918-AA-4` | MF1 2025-B2 LLC | market-sale-or-counterparty-cash-candidate | `209.6M USD` | clean cash-like candidate |
| 21 | `91282C-LW-9` | U.S. Treasury note/bond | market-sale-or-counterparty-cash-candidate | `190.6M USD` | clean cash-like candidate |
| 22 | `28655*-AB-5` | Eliant Invest Holding LP C | market-sale-or-counterparty-cash-candidate | `189.5M USD` | clean cash-like candidate |
| 23 | `912810-TW-8` | U.S. Treasury note/bond | market-sale-or-counterparty-cash-candidate | `182.2M USD` | clean cash-like candidate |
| 25 | `91282C-MG-3` | U.S. Treasury note/bond | market-sale-or-counterparty-cash-candidate | `179.1M USD` | clean cash-like candidate |

## What This Tells Us In Simple Terms

This is no longer just an insurance-company asset total. For these selected rows, Athene has named assets that appear in the year-end holding parser and also appear in disposal/proceeds rows.

That matters because same-CUSIP evidence is the closest public statutory route to a named cash loop:

1. Athene holds a named asset at year end
2. the same CUSIP appears in disposal/proceeds rows
3. most of the selected consideration is cash-like under the corrected parser
4. the packet preserves the exact holding and disposal rows for manual inspection
5. mixed rows are held back where tax-free exchange or transfer language appears

The cleanest next row targets are Eliant, AMAPS, Concord Music Royalties, MF1 2025-B2, and the U.S. Treasury rows. AP Aristotle remains high-dollar and important, but it is mixed because the same CUSIP also carries noncash/hold evidence.

## What This Proves

This pass proves:

1. the top corrected same-CUSIP cash-like candidates can be expanded into row-level source packets
2. selected rows show `2.930192972B USD` of cash-like proceeds under same-CUSIP matching
3. source detail rows preserve pages, row IDs, dates, disposition labels, consideration, book values, interest/dividend fields, NAIC fields where available, and raw numeric streams
4. mixed rows are not promoted to clean cash proof
5. safe realized gain/loss remains near zero because shifted parser tokens are still blocked

## What It Does Not Prove

This pass does not prove:

1. lot-level continuity across purchase, holding, and disposal
2. borrower receipt or use of proceeds
3. Apollo/Athene source-of-funds allocation into the specific asset
4. liability-cost spread
5. full realized gain/loss reconciliation
6. IRR, NPV, ROIC, cash-on-cash return, or platform profit

## Safe Claim

`The corrected Athene statutory workbench now has a 10-CUSIP same-CUSIP row proof packet covering 2.943066208B USD of selected disposal consideration, of which 2.930192972B USD is cash-like under the corrected parser. The packet connects named year-end holding rows to named disposal/proceeds rows for AP Aristotle, Eliant, AA Infrastructure Fund, AMAPS, Concord Music Royalties, MF1 2025-B2, and U.S. Treasury CUSIPs. This supports row-level cash-like proceeds inspection, not final borrower receipt, liability spread, or asset-level return proof.`

## Decision

`apollo-athene-same-cusip-cashlike-row-proof-packet-ready-for-source-row-inspection`

The next move is PDF row inspection for the clean same-CUSIP candidates and a separate mixed-row resolution pass for AP Aristotle and AA Infrastructure Fund.
