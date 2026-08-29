# Capital Flow URI Yak Bond Identifier And Market-Data Boundary Pass 1

## Purpose

This pass tests whether URI's Yak note financing can be tied to security identifiers, public bond-reference pages, current market quote evidence, and later holder traces.

It answers:

`Can we move from note-term visibility to instrument-level market lookup visibility, and what does that still not prove about who funded the Yak acquisition?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-yak-bond-identifier-market-data-boundary-pass-1.csv`

## Source Boundary

This pass uses:

- SEC Exhibit `4.1` indenture dated March `11`, `2024`
- TradingView / FINRA bond reference page for `URI5769315`
- BondTerminal bond reference page for `US911365BR47`
- Cbonds and Terrapin reference pages for the Reg S line
- Public.com bond page for a current retail quote snapshot
- Schwab High Yield Bond ETF holdings page for one later fund-holder trace

This pass is:

`bond-identifier-and-market-data-boundary-visible`

It is not:

`initial-purchaser-names-visible`

or:

`institutional-spread-tape-visible`

or:

`note-investor-allocation-visible`

## Evidence Captured

| Source | Evidence | Boundary |
|---|---|---|
| SEC indenture | CUSIPs `[911365 BR4][U91139 AK8]` and ISINs `[US911365BR47][USU91139AK85]` appear in the form of note. | Primary legal identifier evidence. |
| TradingView / FINRA | `U91139AK8`, `USU91139AK85`, and FIGI `BBG01LW2W1N9` are mapped to a `6.125%` note due March `15`, `2034`. | Public bond-reference evidence; not offering allocation. |
| BondTerminal | `US911365BR47`, alternate ISIN `USU91139AK85`, `1.100B USD` issued/outstanding, semiannual coupon, callable/bullet structure. | Public bond-reference evidence; not source-of-funds schedule. |
| Cbonds / Terrapin | Reg S ticker `URI 6.125 03/15/34 REGS`, FIGI `BBG01LW2W1N9`, issued amount `1.100B USD`, senior unsecured rank. | Public reference evidence; some fields remain gated. |
| Public.com | Current page showed price `$101.97`, yield `5.71%`, next call date March `15`, `2029`, next call price `$103.07`, and liquidity score `5.0/5`. | Retail quote snapshot; yield is time-sensitive and not the original issue spread. |
| Schwab High Yield Bond ETF | As of August `21`, `2026`, SCYB listed URI CUSIP `911365BR4`, quantity `2.225M`, `0.08%` of assets, market value `$2.3M`. | Later holder trace, not initial purchaser or full holder base. |

## What This Adds

The Yak note can now be looked up by identifiers:

`CUSIP / ISIN / FIGI / ticker -> market-reference pages -> current quote snapshots -> later holder traces`

That helps answer:

`How do we find the real market instrument and follow who owns it later?`

The answer is still bounded. We can identify the note and locate at least one later public fund holding. We cannot yet name the original initial purchasers, reconstruct the order book, prove institutional allocation, extract original issue spread, or map bond proceeds to the exact Yak ABL draw.

## Safe Claim

`URI's Yak note financing is now bond-identifier-and-market-data-boundary-visible: the SEC indenture lists CUSIPs 911365 BR4 and U91139 AK8 and ISINs US911365BR47 and USU91139AK85; public bond-reference pages map the Reg S line to FIGI BBG01LW2W1N9 and ticker URI 6.125 03/15/34 REGS; a current retail quote page showed price 101.97 and yield 5.71%; and Schwab's SCYB holdings page showed a later 2.225M position in CUSIP 911365BR4 as of August 21 2026. This identifies and tracks the instrument, but it does not prove named initial purchasers, original investor allocation, institutional spread/yield tape, exact ABL draw allocation, or Matting ROIC.`

## Claims Not To Make Yet

Do not say:

- the current quote equals the original issue yield
- a retail quote page is institutional pricing tape
- one ETF holding is the note's full holder base
- a later ETF holder was an initial purchaser
- identifiers solve the ABL draw allocation
- FIGI/CUSIP visibility proves use-of-proceeds beyond the company disclosures
- the offering memorandum has been found

## Next Concrete Work

The next evidence gates are:

1. Pull original issue price, yield, and spread from an offering memorandum, pricing supplement, TRACE source, or institutional bond database.
2. Find purchase agreement or offering memorandum evidence naming the initial purchaser firms.
3. Build a later-holder crosswalk from ETF/fund/statutory schedules using `911365BR4` and `US911365BR47`.
4. Separate 144A, Reg S, and any exchange/security lifecycle events before aggregating holder evidence.
5. Compare current yield/spread to peer equipment-rental and high-yield issuers only after source timestamps are captured.

The first public later-holder crosswalk is now captured in `capital-flow-uri-yak-public-holder-crosswalk-pass-1.md`.

The expanded public later-holder crosswalk is now captured in `capital-flow-uri-yak-public-holder-crosswalk-pass-2.md`.

The first original-pricing source-boundary pass is now captured in `capital-flow-uri-yak-original-pricing-source-boundary-pass-1.md`.
