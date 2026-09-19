# Wheaton–Antamina financing-terms boundary upgrade

Research date: `2026-09-15`

## What the primary filings establish

Wheaton's Q2 2026 filing and related credit-agreement exhibit establish a
source-backed financing boundary for the Antamina purchase price:

- Wheaton entered a `1.500B USD` unsecured, non-revolving term loan on April
  1, 2026. The term loan has a two-year maturity, aligns with the existing
  revolving credit facility, and may be repaid at any time without penalty.
- The term facility credit agreement's Schedule H sets the Term Benchmark
  Loan margin at `1.000%`, `1.400%`, `1.650%`, or `2.050%` depending on the
  leverage-ratio level.
- The revolving credit facility was expanded to `2.500B USD`, matures June
  30, 2031, and has a `500M USD` accordion. Its pricing is based on the
  leverage ratio at SOFR plus `1.10%` to `2.15%`; the standby fee is `0.1966%`.
- Wheaton remained compliant with a capitalization-ratio covenant of no more
  than `0.60:1`.
- The transaction materials describe the `4.300B USD` BHP Antamina PMPA
  payment as funded with cash, approximately `0.900B USD` of revolver
  borrowings, and the `1.500B USD` term loan. The later Q2 balance sheet shows
  `1.500B USD` of term debt and `472M USD` of revolver debt, alongside
  `100.192M USD` of cash.
- Bank of Montreal is the administrative agent; the term-facility exhibit
  identifies the named syndicate and the Wheaton borrower entities.

## Bounded financing sensitivity

Applying only the disclosed RCF margin range to the Q2 reported `472M USD`
revolver balance gives a company-level spread-only burden of approximately
`5.192M USD` to `10.148M USD` per year:

```text
472M USD × 1.10% = 5.192M USD
472M USD × 2.15% = 10.148M USD
```

The disclosed term-loan margin range provides a second bounded screen:

```text
1,500M USD × 1.00% = 15.000M USD
1,500M USD × 2.05% = 30.750M USD
```

Using the reported Q2 revolver balance and the term-loan principal, the
combined spread-only burden is approximately `20.192M USD` to `40.898M USD`
per year before SOFR, standby and other fees, timing, amortization, and tax.
This is a company-level margin screen, not an Antamina allocation or an
all-in interest estimate.

## Current SOFR all-in company-level screen

The New York Fed reported a `3.62%` SOFR observation for September 14, 2026.
Applying that benchmark mechanically to the disclosed principal balances and
the filing-backed spread ranges gives a wider current-rate screen:

| Facility | Principal | SOFR / margin range | Mechanical annual interest range |
| --- | ---: | --- | ---: |
| Term loan | `$1.500B` | `3.62% + 1.00%–2.05%` | `$69.300M–$85.050M` |
| Revolver | `$472M` | `3.62% + 1.10%–2.15%` | `$22.278M–$27.234M` |
| Combined | `$1.972B` | — | `$91.578M–$112.284M` |

This is a benchmark-and-margin sensitivity, not reported interest expense. It
assumes the observed balances remain constant, ignores floors, fees, day-count,
repayment timing, amortization, and tax, and does not allocate either facility
to the Antamina PMPA. It improves the financing burden denominator without
creating financed-return proof.

## What this does not prove

These terms improve the financing denominator, but they do not prove the
portion of interest or principal service economically attributable to the BHP
PMPA. The public record still does not provide an Antamina-specific debt
waterfall, benchmark-rate history, effective all-in rate and fee allocation,
tax allocation, repayment ledger, or lender-level cash claim. Therefore this artifact does not
calculate a financed Antamina IRR or NPV.

## Source route

- [Wheaton Q2 2026 MD&A, SEC](https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex992.htm)
- [Wheaton Q2 2026 financial statements, SEC](https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex993.htm)
- [Non-Revolving Term Facility Credit Agreement, SEC exhibit](https://www.sec.gov/Archives/edgar/data/1323404/000106299326001700/exhibit99-2.htm), especially Schedule H applicable rates.
- [Wheaton FY2025 AIF, SEC](https://www.sec.gov/Archives/edgar/data/1323404/000119312526134908/d56281dex991.htm)
- [New York Fed SOFR data API, September 14, 2026 observation](https://markets.newyorkfed.org/api/rates/secured/sofr/last/1.json)

## Proof grade

`financing-terms-boundary-confirmed`: facility size, maturity, repayment
flexibility, term-loan and revolver margin ranges, covenant, administrative-
agent route, and company-level spread-only and current-SOFR sensitivities are
source-backed. Antamina-specific interest, tax, debt service, lender
allocation, and financed return remain open.
