# Valuation and expectation promotion matrix

Research date: `2026-09-17` (refresh)

## Purpose

This matrix connects the Damodaran-style valuation and reverse-expectation
workbenches to the evidence-grade and owner-cash controls. It prevents an
illustrative cash, FRE, SRE, or transaction-return input from being presented
as an observed investable denominator.

The structured [valuation promotion matrix CSV](data/combined-investment-research-valuation-promotion-matrix-2026-09-16.csv)
is the source of truth.

## Current decision surface

- **Wheaton–Antamina:** valuation must be transaction-level because no clean
  public segment equity allocation isolates Antamina. The $4.300B upfront
  payment is observed, but the BHP-only delivery, settlement, tax, financing,
  and return chain is not.
- **Retail:** TJX, Target, and Walmart now have an annual reported-cash
  expectation screen using the September 17 market snapshot and their latest
  fiscal-year cash-after-property denominators. The resulting `27.906x`,
  `24.913x`, and `57.471x` ratios are not normalized owner cash.
- **Apollo–Athene:** the SOTP exposes required FRE/SRE or principal value,
  but those earnings remain subject to capital, credit, regulated-entity,
  parent-receipt, preferred/NCI, dilution, and common-owner constraints.

## Promotion rule

Every valuation result remains `qualified-expectation-screen` until the
corresponding CA-06 denominator, named-cash, or return bridge is promoted.
Valuation can show what must be true; it cannot establish that the required
cash or earnings will occur. The thesis breaker is therefore the failure of
the named source-backed join, not an arbitrary multiple threshold.

Status: `valuation-promotion-partial; expectation-burdens-explicit`.

## Annual retail reported-cash refresh — 2026-09-17

The [annual reported-cash expectation screen](combined-investment-research-pilot-02-retail-annual-reported-cash-expectation-screen-2026-09-17.md)
extends the market-burden test to TJX, which had previously remained outside
the direct multiple table. This makes the three-company expectation surface
comparable on a reported fiscal-year denominator while preserving the
promotion rule: maintenance capital, working capital, attached services,
leases, taxes, dilution, and claims remain unallocated, so none of the ratios
is a normalized owner-cash multiple.
