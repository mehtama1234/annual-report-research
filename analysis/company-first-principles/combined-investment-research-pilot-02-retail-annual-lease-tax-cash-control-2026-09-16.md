# Pilot 02 retail annual lease-and-tax cash control

Research date: `2026-09-16`

## Question

Do the annual filings expose cash lease payments and cash taxes for the TJX,
Target, and Walmart reported cash-after-property screens?

## Result

`partial-upgrade` for annual burden visibility. The FY2026/FY2025 filings
disclose cash paid for operating leases and income taxes for all three
companies:

| Company | Annual period | Reported cash after property | Operating lease cash paid | Income taxes paid | Operating lease liabilities |
| --- | --- | ---: | ---: | ---: | ---: |
| TJX | FY2026 | `$4.917B` | `$2.214B` | `$1.471B` | `$10.620B` |
| Target | FY2025 | `$2.835B` | `$0.529B` | `$1.091B` | `$3.834B` |
| Walmart | FY2026 | `$14.923B` | `$2.315B` | `$5.364B` | `$15.572B` |

As a diagnostic scale comparison, lease cash represented approximately `45.0%`,
`18.7%`, and `15.5%` of reported cash-after-property for TJX, Target, and
Walmart respectively; cash taxes represented approximately `29.9%`, `38.5%`,
and `35.9%`. These ratios are mechanical context, not owner-cash deductions.

These are denominator controls, not additional deductions to be blindly
subtracted from operating cash flow. Operating cash flow is already after the
ordinary cash operating expenses, including cash lease payments and cash taxes.
The table therefore improves burden visibility and timing calibration without
double counting either item.

## What this improves

The annual cohort now has a source-backed distinction between:

1. cash after property spending;
2. cash taxes actually paid rather than tax provision;
3. operating lease cash actually paid rather than only the lease-liability
   balance; and
4. the remaining maintenance-capital, supplier-finance, service-cost,
   working-capital, seasonality, dilution, and legal-entity allocation gaps.

The annual control does not close the current H1 owner-cash question. The
annual periods do not match the current H1 comparison, and the filings do not
provide a complete maintenance-versus-growth allocation or a fully normalized
common-owner waterfall. Lease liabilities are also not the same thing as
current-period lease cash.

## Safe use

Use the disclosed lease cash and tax cash to check denominator completeness
and to calibrate annual burden ranges. Do not subtract them again from an
operating-cash-flow figure unless the model first reconstructs a pre-payment
cash measure. Do not treat annual cash-after-property less these amounts as an
owner-cash result.

## Primary sources

- [TJX FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm)
- [Target FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/tgt-20260131.htm)
- [Walmart FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm)

Structured result: [annual lease-and-tax cash CSV](data/combined-investment-research-pilot-02-retail-annual-lease-tax-cash-control-2026-09-16.csv).
