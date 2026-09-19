# KKR / Global Atlantic Accordia matched-disposal settlement request packet pass 1

Research date: `2026-09-18`

## Purpose

This packet converts the three coordinate-extracted Accordia disposal rows into
specific source requests. It is the next Q-12 proof object after the statutory
owned-interest/disposal join; it does not treat statutory consideration as
settlement cash.

The structured companion is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-matched-disposal-settlement-request-packet-pass-1.csv`

## Named requests

| CUSIP | Issuer | Disposal date | Statutory consideration | Required next source |
|---|---|---:|---:|---|
| `458140-BM-1` | Intel Corp | `05/15/2025` | `$1,406,099` | Broker confirmation, custodian settlement, lot ledger, and Accordia cash-receipt entry |
| `202795-JY-7` | Commonwealth Edison Co | `11/13/2025` | `$957` | Broker confirmation, custodian settlement, lot ledger, and Accordia cash-receipt entry |
| `685218-AB-5` | Orange SA | `01/21/2025` | `$145,523` | Broker confirmation, custodian settlement, lot ledger, and Accordia cash-receipt entry |

## Promotion test

Promotion requires the same legal entity, CUSIP, lot, disposal date,
consideration, settlement date, receiving account or custodian record, and
cash amount to reconcile. A second layer must join the proceeds to liability
cost, fees, taxes, reinsurance/funds-held routing, and a bounded residual
return.

## Current boundary

The coordinate extraction proves statutory consideration, book value at
disposal, realized gain/loss, and disposal-row interest/dividends. It does not
prove broker settlement, lot continuity, borrower use, trustee remittance,
liability-adjusted spread, or KKR/Global Atlantic owner cash.

## Decision

`accordia-matched-disposal-settlement-request-ready; receipt-lot-liability-cost-and-return-open`

