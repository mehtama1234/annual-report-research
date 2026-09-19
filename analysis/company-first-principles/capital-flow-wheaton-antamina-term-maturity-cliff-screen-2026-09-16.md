# Wheaton–Antamina term-maturity cliff screen

Research date: `2026-09-16`

The March 26, 2026 term facility agreement requires outstanding term-facility
credit, accrued interest, and fees to be repaid at the two-year maturity date.
Wheaton's Q2 2026 financial statements report `$1.500B` gross term-loan debt
and `$472M` of revolving-facility debt at June 30, 2026, for `$1.972B` of gross
bank debt. The term loan therefore represents approximately `76.06%` of the
reported gross bank-debt balance.

## Calendar-date control

The agreement gives a two-year maturity from its defined `Closing Date`; the
April 1, 2026 BHP-PMPA cash closing is a related transaction date, not a safe
substitute for the facility's defined closing date. The workbench therefore
uses a two-year maturity window rather than silently converting the contract
into an April 1, 2028 due date. A final calendar maturity date should be taken
from the executed agreement's definition and closing certificate or a later
Wheaton debt schedule.

Conditional model date: if the April 1, 2026 transaction completion is also the
agreement-defined `Closing Date`, the two-year bullet would fall on April 1,
2028. That is a transparent scenario input, not a certified maturity date;
the legal definition and public completion announcement do not, by themselves,
expose the executed closing certificate.

## Return-model implication

The existing annual interest sensitivities describe carrying cost, but they do
not represent the principal bullet as an annual operating expense. A financed
Antamina return model must separately test whether stream cash, other Wheaton
operating cash, asset sales, refinancing, or equity funding covers the term
principal at maturity. Treating the `$1.500B` term balance as an annual cost
would be wrong; omitting the maturity principal claim would also overstate
common-owner residual cash.

The companion [maturity-bullet coverage screen](capital-flow-wheaton-antamina-term-maturity-bullet-coverage-screen-2026-09-16.md)
shows the principal claim separately against the annualized stream operating-
cash-flow proxy under explicit 0%–100% allocation sensitivities. It is an
illustrative terminal-burden display, not an Antamina debt allocation or
repayment forecast.

## Evidence boundary

This is a corporate liability-timing screen. It does not prove that the term
loan funded a particular dollar of the `$4.300B` PMPA, nor does it identify an
Antamina-specific repayment source, tax allocation, lender waterfall, or
financed IRR/NPV. The result remains `evidence-insufficient` for Q-03.

## Sources

- [SEC-hosted Non-Revolving Term Facility Credit Agreement](https://www.sec.gov/Archives/edgar/data/1323404/000106299326001700/exhibit99-2.htm)
- [Wheaton Q2 2026 financial statements](https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex993.htm)
- [Wheaton BHP Antamina closing exhibit](https://www.sec.gov/Archives/edgar/data/1323404/000127956926000263/ex991.htm)

Structured result: [term-maturity cliff CSV](data/capital-flow-wheaton-antamina-term-maturity-cliff-screen-2026-09-16.csv).
