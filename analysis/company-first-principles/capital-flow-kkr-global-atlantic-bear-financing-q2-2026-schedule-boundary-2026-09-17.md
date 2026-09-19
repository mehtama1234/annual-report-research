# Capital Flow KKR Global Atlantic Bear Financing Q2 2026 Schedule Boundary

Research date: `2026-09-17`

## Purpose

This pass checks the latest official Accordia Q2 2026 document available from
Global Atlantic for the Bear Financing CUSIP. It separates a missing accessible
Schedule D from evidence of a sale, repayment, or settlement.

## Result

## 2026-09-18 official-source refresh

Global Atlantic's current financial-statements index still exposes the
Accordia Q2 2026 document as a quarterly statement verification. The linked
PDF was checked directly for `90231*-AA-0`, `2023 Bear Financing`, and
`Credit Agreement`; none appears. The document does report the aggregate bond
base, but it does not expose the detailed Schedule D row or a transaction-level
loan event.

This is a source-availability confirmation, not evidence of disposal,
repayment, transfer, or settlement. The next promotion object remains the full
Q2 statutory statement with Schedule D or a custodian/loan ledger.

Global Atlantic's Q2 2026 Accordia document is titled a quarterly statement
verification and covers the quarter ended June 30, 2026. The accessible PDF
reports aggregate bonds of `$7.371492B`, but it does not contain the detailed
Schedule D row for CUSIP `90231*-AA-0` or the text `2023 Bear Financing`.

The same Q2 verification provides a useful current legal-entity perimeter:

| Accordia aggregate field at June 30, 2026 | Amount | Safe interpretation |
|---|---:|---|
| Bonds | `$7.371492B` | Total statutory bond base; not Bear Financing exposure |
| Cash, cash equivalents, and short-term investments | `$259.286M` | Entity-level liquidity; not Bear-specific cash or unrestricted parent cash |
| Total liabilities | `$11.412B` | Senior policyholder, reinsurance, and other entity claims remain ahead of surplus |
| Surplus | `$734.357M` | Entity-level capital perimeter; not common-owner residual or Bear return |
| Payable to parent, subsidiaries, and affiliates | `$7.434M` | Related-party claim boundary; no Bear allocation |
| Funds held under coinsurance | `$4.241B` | Significant entity-level liability/funds-held boundary; not available cash |

These fields strengthen the entity-perimeter map, but must not be used to
infer Bear Financing repayment, Accordia cash receipt, or KKR common-owner
cash.

A second, targeted parent-level route was also checked: KKR's Q2 2026 Form
10-Q reports Global Atlantic's aggregate commitments to purchase or fund
investments, but the filing does not identify the Bear Financing CUSIP, a Bear
draw, a Bear-specific repayment, or a Bear cash waterfall. That aggregate
platform disclosure is therefore context only and cannot be joined to the
named Accordia position.

Therefore:

- FY2025 remains the latest accessible full Schedule D continuity point for
  the Bear Financing row;
- the Q2 2026 verification document and the KKR parent filing cannot establish
  that the position was held, sold, repaid, transferred, or settled;
- the absence of the row in this verification PDF is a source-availability
  boundary, not a searched-negative conclusion about the investment event.

## Promotion control

Do not infer a disposal from the absence of a detailed row in a verification
document. The next decisive source is the full Q2 2026 Accordia statutory
statement with Schedule D, or a custodian/loan ledger that identifies the
position and any event after December 31, 2025.

## Safe claim

`The latest official Accordia Q2 2026 verification document is available and reports the aggregate bond base, while KKR's Q2 2026 parent filing reports Global Atlantic aggregate investment commitments. Neither accessible route provides the Bear Financing CUSIP, a Bear-specific draw, repayment, or detailed Schedule D continuity. FY2025 remains the latest full row-level continuity point. This narrows the source request but proves neither disposal nor settlement.`

## Decision

`bear-financing-q2-2026-full-schedule-not-accessible; no-disposal-inference`

## Primary source

[Global Atlantic financial-statements index](https://www.globalatlantic.com/investor/financial-statements)

[Global Atlantic / Accordia Q2 2026 quarterly statement verification](https://www.globalatlantic.com/content/dam/global-atlantic/investors/financial-statements/annual-and-quarterly-statements/accordia-q2-2026-quarterly-statement-verifications.pdf)

[KKR Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1404912/000140491226000027/kkr-20260630.htm)
