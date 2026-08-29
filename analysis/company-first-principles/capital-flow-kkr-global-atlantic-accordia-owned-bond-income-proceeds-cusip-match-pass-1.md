# Capital Flow KKR Global Atlantic Accordia Owned-Bond Income Proceeds CUSIP Match Pass 1

## Purpose

This pass takes the top `40` Accordia owned-bond interest-received rows and tests whether the same CUSIPs also appear in current-year acquisition, sale, redemption, disposal, or acquired-and-fully-disposed sections of the raw Accordia Schedule D parser.

It asks:

`Which high-interest KKR/Global Atlantic Accordia owned-bond rows have same-CUSIP acquisition or disposal continuity, and where does public statutory proof still stop before proceeds are promoted?`

The match table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-pass-1.csv`

The event table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-event-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-diagnostic-pass-1.csv`

## Short Answer

`The top 40 Accordia owned-bond interest-received rows now have a same-CUSIP continuity worklist. Ten rows have same-CUSIP current-year events: seven acquisition-context rows and three disposal/proceeds-candidate rows. The matched-event rows carry 13851356 USD of owned-bond interest received, including 4868177 USD on disposal-candidate rows. No row is upgraded to full named-cash proof because the acquisition/disposal event rows are still raw-token evidence, not coordinate-reconciled proceeds columns.`

## Diagnostics

| Metric | Value | Units |
|---|---:|---|
| Match rows | 40 | count |
| Same-CUSIP event rows | 10 | count |
| Top rows with any event | 10 | count |
| Rows with same-CUSIP acquisition | 7 | count |
| Rows with same-CUSIP disposal | 3 | count |
| Interest received on top 40 rows | 63974606 | USD |
| Interest received on rows with any event | 13851356 | USD |
| Interest received on disposal-candidate rows | 4868177 | USD |
| Raw event money-token sum | 390795706 | USD-token-sum |
| Largest raw event token | 55230000 | USD-token |
| Full named cash proof upgrades | 0 | count |

## Top Match Rows

| ID | CUSIP | Issuer/Description | Interest Received | Event Rows | Continuity Status |
|---|---|---|---:|---:|---|
| CFKKRGACOBIPCM-001 | 90231*-AA-0 |  | 17419245 | 0 | owned-interest-only-no-current-proceeds-event |
| CFKKRGACOBIPCM-002 | 54438C-PA-4 | LOS ANGELES CALIF CMNTY COLLEGE DIST | 3093525 | 0 | owned-interest-only-no-current-proceeds-event |
| CFKKRGACOBIPCM-003 | 458140-BM-1 | INTEL CORP | 2902052 | 1 | owned-interest-plus-disposal-same-cusip-visible |
| CFKKRGACOBIPCM-004 | 94974B-GU-8 | WELLS FARGO & CO | 2623425 | 1 | owned-interest-plus-acquisition-same-cusip-visible |
| CFKKRGACOBIPCM-005 | 78486#-AA-3 |  | 2305722 | 0 | owned-interest-only-no-current-proceeds-event |
| CFKKRGACOBIPCM-006 | L9632@-AA-0 |  | 1992125 | 0 | owned-interest-only-no-current-proceeds-event |
| CFKKRGACOBIPCM-007 | 92343V-DS-0 | VERIZON COMMUNICATIONS INC | 1692452 | 0 | owned-interest-only-no-current-proceeds-event |
| CFKKRGACOBIPCM-008 | 68389X-CK-9 | ORACLE CORP | 1574925 | 1 | owned-interest-plus-acquisition-same-cusip-visible |
| CFKKRGACOBIPCM-009 | 072024-NV-0 | BAY AREA TOLL AUTH CALIF TOLL BRDG REV | 1339226 | 0 | owned-interest-only-no-current-proceeds-event |
| CFKKRGACOBIPCM-010 | 58013M-FA-7 | MCDONALD'S CORP | 1322344 | 0 | owned-interest-only-no-current-proceeds-event |
| CFKKRGACOBIPCM-011 | 91324P-DV-1 | UNITEDHEALTH GROUP INC | 1232250 | 0 | owned-interest-only-no-current-proceeds-event |
| CFKKRGACOBIPCM-012 | 0778FP-AN-9 | BELL TELEPHONE COMPANY OF CANADA OR BELL | 1077810 | 1 | owned-interest-plus-acquisition-same-cusip-visible |

## Proof Effect

This pass upgrades the next work from a general proceeds search to a named CUSIP worklist. The best immediate targets are the three disposal/proceeds-candidate CUSIPs because they already connect owned interest-received rows to same-CUSIP sale/redeemed/disposed rows in the raw parser.

The safe use is:

`Accordia top interest-received owned-bond rows now have same-CUSIP acquisition/disposal continuity flags. Three rows are disposal/proceeds candidates, but the event rows remain raw-token evidence until coordinate column extraction reconciles consideration, book value, gain/loss, and interest/dividend fields.`

## Boundary

This is not full named-cash proof. Same-CUSIP continuity does not prove lot-level identity, consideration, settlement cash, borrower receipt/use, trustee remittance, liability-cost spread, funds-held waterfall, collateral certificates, IRR, NPV, ROIC, or KKR platform profit.

## Next Action

Run `accordia-disposal-coordinate-column-extraction-for-matched-cusips` on the matched disposal pages, then reconcile event tokens to statutory disposal columns before any proceeds or gain/loss claim.

## Decision

`kkr-global-atlantic-accordia-income-proceeds-cusip-match-visible-disposal-coordinate-extraction-next`
