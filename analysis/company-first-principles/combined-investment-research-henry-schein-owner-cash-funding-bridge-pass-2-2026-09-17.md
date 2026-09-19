# Henry Schein H1 2026 owner-cash funding bridge — pass 2 — 2026-09-17

## Decision

Henry Schein's H1 filing now supports a direct funding test: the visible
pre-debt residual was approximately `$30M`, while repurchases were `$325M` and
gross debt/credit-line issuance exceeded the residual. This does not prove
that every repurchase was debt-funded, but it proves that “surplus cash funded
the buyback” is not an admissible conclusion without the complete cash and
financing waterfall.

Status: `funding-bridge-pass-2; securitization-collateral-visible; normalized-owner-cash-open; no-ranking`.

## H1 2026 waterfall

```text
operating cash flow                                  $145M
  - property and equipment                            $55M
  - capitalized software                              $30M
  - acquisitions/equity investments                   $30M
  = visible pre-debt residual                          $30M

H1 share repurchases                                  $325M
net bank-credit-line borrowing                        $261M
long-term debt issued                                 $144M
long-term debt repaid                                  $50M
```

The `$295M` difference between repurchases and the visible pre-debt residual is
a funding gap screen, not a source attribution. The reported financing flow
also includes other items and is a net cash-use figure, so the exact path must
be reconstructed from beginning cash, borrowing, debt service, distributions,
share issuance, and other financing lines.

## Receivable collateral and liquidity boundary

The U.S. trade-receivable securitization had a `$450M` purchase limit and
`$430M` outstanding, or approximately 95.6% utilization, backed by `$526M` of
certain receivables. This is a material liquidity source and a senior claim;
it is not equivalent to unrestricted common-owner cash. The model must test
availability after eligibility, dilution, reserves, customer credit, and
collections, and must avoid counting the same receivables as both collateral
support and freely distributable operating cash.

H1 working capital consumed `$116M` through receivables and `$49M` through
inventory, partly offset by `$79M` of accounts payable/accrued-expense funding.
Receivables were `$1.763B`, inventory `$2.059B`, DSO rose to 45.7 days from
44.7, and inventory turns declined to 4.6 from 4.7. These are direct QoE
signals, but seasonality and acquisition mix still require a multi-period
bridge.

## Restructuring, KKR, and adjustment controls

H1 restructuring charges were `$41M` and the 2024 Plan remains active through
2027. The charge cannot be deducted a second time from OCF without a cash-paid
and remaining-obligation schedule, but it also cannot be normalized away from
adjusted EPS without that schedule. KKR invested `$250M` for 3,285,152 shares;
issuance, ASR/repurchase activity, diluted shares, and governance rights belong
in the same per-share waterfall.

The key financial-shenanigans test is therefore not whether any individual
line is improper. It is whether adjusted EPS improvement, repurchases, and
reported liquidity are being evaluated after recurring restructuring,
working-capital funding, collateral seniority, debt service, software/property
reinvestment, acquisitions, and dilution are all visible.

## Promotion gate and thesis breaker

Promotion requires: cash-paid restructuring and remaining-obligation schedule;
seasonal-normalized receivable/inventory cycle; securitization eligibility,
reserves, and availability; debt/repurchase cash waterfall; maintenance versus
growth software/property allocation; acquisition return; and KKR/ASR diluted
share treatment.

The thesis breaker is activated if sales and adjusted EPS grow while the
pre-debt residual remains thin, receivable collateral utilization rises,
working-capital turns deteriorate, and repurchases require increasing debt or
secured liquidity. This is a filing-based falsifier, not a fraud conclusion.

Structured companion: [Henry Schein H1 funding table](data/combined-investment-research-henry-schein-owner-cash-funding-bridge-pass-2-2026-09-17.csv).

Sources: [Henry Schein Q2 2026 restructuring/liquidity refresh](combined-investment-research-henry-schein-q2-2026-restructuring-liquidity-refresh-2026-09-17.md), [FY2025 waterfall](combined-investment-research-henry-schein-restructuring-liquidity-waterfall-pass-1-2026-09-17.md), and [Q2 2026 Form 10-Q](../../raw/sec/healthcare/medical-instruments-supplies/henry-schein-inc/2026-q2-10q.html).
