# Capital Flow KKR Global Atlantic Accordia Matched Disposal Coordinate Extraction Pass 1

## Purpose

This pass coordinate-extracts the three Accordia Schedule D Part 4 disposal rows that matched top owned-bond interest-received CUSIPs.

It asks:

`Can the KKR/Global Atlantic Accordia proof stack move from raw same-CUSIP disposal tokens to coordinate-column disposal amounts for named CUSIPs without claiming final settlement cash or return?`

The structured table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-matched-disposal-coordinate-extraction-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-matched-disposal-coordinate-extraction-diagnostic-pass-1.csv`

## Short Answer

`The three same-CUSIP disposal candidates now have coordinate-column statutory disposal amounts. Consideration sums to 1552579 USD, book/adjusted carrying value at disposal sums to 1754251 USD, realized gain/loss on disposal sums to -201672 USD, and disposal-row interest/dividends received sums to 29251 USD. This is proceeds-column evidence, not settlement cash, waterfall, liability-spread, or final return proof.`

## Extracted Disposal Rows

| ID | CUSIP | Issuer | Consideration | Book at Disposal | Realized Gain/Loss | Interest/Dividends |
|---|---|---|---:|---:|---:|---:|
| CFKKRGACDCE-001 | 458140-BM-1 | INTEL CORP | 1406099 | 1597788 | (191689) | 25385 |
| CFKKRGACDCE-002 | 202795-JY-7 | COMMONWEALTH EDISON CO | 957 | 998 | (41) | 16 |
| CFKKRGACDCE-003 | 685218-AB-5 | ORANGE SA | 145523 | 155465 | (9942) | 3850 |

## Diagnostics

| Metric | Value | Units |
|---|---:|---|
| Coordinate disposal rows | 3 | count |
| Rows with consideration | 3 | count |
| Raw parser money-token count | 17 | count |
| Coordinate source-token count | 26 | count |
| Consideration sum | 1552579 | USD |
| Book at disposal sum | 1754251 | USD |
| Realized gain/loss sum | -201672 | USD |
| Interest/dividends received sum | 29251 | USD |
| Plain-number token recovery rows | 3 | count |
| Full named cash proof upgrades | 0 | count |

## Proof Effect

This pass upgrades the three disposal candidates from raw-token holds to coordinate-column statutory disposal rows. It also recovers plain-number row values that the raw parser undercounted, most visibly on the Commonwealth Edison row.

The safe use is:

`Accordia has coordinate-column disposal evidence for Intel, Commonwealth Edison, and Orange same-CUSIP rows. These rows show statutory consideration, book value at disposal, realized gain/loss, and interest/dividend fields, but they do not prove settlement cash, lot-level continuity, borrower use, liability-cost spread, waterfall, collateral certificates, or return.`

## Boundary

This is not full named-cash proof. Statutory disposal consideration is a stronger proceeds-column signal than raw tokens, but it is not a custodian receipt, bank statement, trustee remittance, liability waterfall, collateral certificate, IRR, NPV, ROIC, or KKR platform profit bridge.

## Next Action

Build `accordia-matched-disposal-owned-interest-proof-packet`: join these disposal rows back to the owned interest rows, legal-entity income bridge, issuer/wrapper context, and controlled-document gaps.

## Decision

`kkr-global-atlantic-accordia-matched-disposal-coordinate-columns-visible-proof-packet-next`
