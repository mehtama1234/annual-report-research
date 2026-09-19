# MF1 Gross Proceeds and Income Denominator Screen

Research date: `2026-09-17`

## Purpose

This screen tests whether the MF1 same-CUSIP packet can support a transparent
gross proceeds-plus-income diagnostic before the missing cost, lot, liability,
and remittance records arrive.

## Calculation

| Input | Amount | Treatment |
| --- | ---: | --- |
| Same-CUSIP year-end reported holding amount | `$218,271,953` | Denominator proxy only; not asserted cost basis. |
| Selected disposal/proceeds consideration | `$209,559,375` | Cash-like candidate under the corrected parser. |
| Selected disposal-row interest/dividend field | `$1,302,655` | Row field preserved as income/receipt candidate; not independently bank-verified. |
| Consideration plus row income field | `$210,862,030` | Mechanical gross screen only. |
| Consideration / holding amount | `96.01%` | Diagnostic ratio, not return. |
| Consideration plus income / holding amount | `96.61%` | Diagnostic ratio, not realized total return. |
| Mechanical difference versus holding amount | `$(7,409,923)` | Difference against reported holding amount, not gain/loss. |

## Interpretation boundary

The screen shows that the selected disposal consideration plus the selected row
income field is below the year-end reported holding amount. That difference
cannot be called a loss, because the packet does not establish acquisition
cost, lot identity, book-value column mapping sufficient for return use, accrued
income timing, fees, taxes, or liability cost. It also does not establish that
the row income field was received in the same cash period as the disposal.

The screen is therefore useful for reconciliation and anomaly review under the
quality-of-earnings/financial-shenanigans layer, but it is not a Beneish score,
fraud finding, realized return, IRR, NPV, ROIC, or Apollo cash claim.

## Promotion gate

To promote this from a denominator screen to a gross or net asset return, the
research must obtain:

1. lot-level acquisition and custody records;
2. source-confirmed book/cost basis and disposal settlement;
3. period-matched income and cash-receipt records;
4. servicing, trustee, transaction, and liability-cost deductions; and
5. legal-entity allocation through Athene and any Apollo/common-owner residual.

## Decision

`diagnostic-only — gross proceeds-plus-income screen assembled; return remains unproven`

Sources: MF1 same-CUSIP row packet detail rows `CFAASCSCRPD-0015` and
`CFAASCSCRPD-0016`; the [same-CUSIP servicing join boundary](capital-flow-apollo-athene-mf1-same-cusip-servicing-join-boundary-2026-09-17.md).

