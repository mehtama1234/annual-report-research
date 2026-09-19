# Capital Flow KKR Global Atlantic Accordia matched-disposal owned-interest proof packet pass 1

## Purpose

This packet joins the three Accordia Schedule D Part 4 disposal rows whose
CUSIPs also appear in the top owned-bond interest-received ranking. It combines
the legal entity, owned-bond book value and interest received, disposal
consideration, book value at disposal, realized gain/loss, and event date in one
controlled worklist. The structured [packet table](data/capital-flow-kkr-global-atlantic-accordia-matched-disposal-owned-interest-proof-packet-pass-1.csv)
preserves the source distinction between statutory row evidence and settlement
cash.

## Joined result

| CUSIP | Issuer | Owned book value | Owned interest received | Disposal consideration | Book at disposal | Realized gain/loss |
|---|---|---:|---:|---:|---:|---:|
| `458140-BM-1` | Intel Corp | `$66.418M` | `$2.902M` | `$1.406M` | `$1.598M` | `$(0.192M)` |
| `202795-JY-7` | Commonwealth Edison Co | `$20.041M` | `$1.060M` | `$0.001M` | `$0.001M` | `$(0.000M)` |
| `685218-AB-5` | Orange SA | `$19.338M` | `$0.906M` | `$0.146M` | `$0.155M` | `$(0.010M)` |

Across the packet, the three rows carry `$1,552,579` of statutory disposal
consideration, `$1,754,251` of book value at disposal, `$(201,672)` of
realized gain/loss, and `$29,251` of disposal-row interest/dividends. The
figures are coordinate-extracted statutory fields, not bank receipts.

## Proof effect

Current structured status: `coordinate-owned-interest-disposal-join-visible`.

This advances the KKR/Accordia lane from:

`owned interest row + raw same-CUSIP event token`

to:

`Accordia legal entity -> named owned security -> interest received -> named disposal row -> statutory consideration and gain/loss`

That is a stronger legal-entity proceeds proxy and a useful comparison case for
Apollo/Athene. It does not prove lot-level continuity, broker settlement,
borrower use, trustee remittance, liability-cost spread, reinsurance or
funds-held waterfall, or KKR/Global Atlantic platform return.

## Hold controls

- The disposal consideration is not treated as collected cash without a
  custodian, broker, bank, or settlement record.
- The realized gain/loss is not treated as economic return without resolving
  tax, fees, lot basis, and liability funding cost.
- The owned-bond interest-received field is not treated as borrower-level cash
  or platform profit.
- No common-owner or KKR cash claim is promoted from this packet.

## Next falsifiable upgrade

Acquire the underlying Schedule D source pages or custodian/broker settlement
support for the three dates, then test lot continuity and cash settlement. In
parallel, join the rows to Accordia liability-cost, reinsurance/funds-held,
and legal-entity cash-flow schedules. Promotion requires the same CUSIP, legal
entity, period, disposal consideration, settlement cash, funding cost, and
return numerator to reconcile.

## Decision

`accordia-matched-disposal-owned-interest-join-visible; settlement-and-return-unproven`

## Source artifacts

- [Owned-bond income/proceeds CUSIP match](data/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-pass-1.csv)
- [Coordinate disposal extraction](capital-flow-kkr-global-atlantic-accordia-matched-disposal-coordinate-extraction-pass-1.md)
- [Accordia owned-bond income bridge](capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-pass-1.md)
