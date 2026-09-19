# Wheaton–Antamina company-burden boundary upgrade

Research date: `2026-09-15`

Wheaton's Q2 2026 filing provides corporate-level burden rows that belong
beside, but must not be subtracted directly from, the Antamina stream proxy.

| Burden or denominator | H1/Q2 2026 value | Safe interpretation |
| --- | ---: | --- |
| Antamina operating cash-flow proxy | `$222.223M` H1 | Stream-level pre-tax, pre-interest cash proxy |
| Wheaton finance costs | `$32.502M` H1 | Corporate financing burden; no Antamina allocation disclosed |
| Wheaton income-tax expense | `$210.876M` H1 | Corporate tax burden; no Antamina allocation disclosed |
| Cash and cash equivalents | `$100.192M` at June 30 | Corporate cash denominator, not a restricted PMPA account or owner residual |
| Gross bank debt | `$1.972B` at June 30 | Corporate debt scale around the PMPA funding event |
| Term loan | `$1.500B` at June 30 | Named facility associated with partial PMPA funding context |
| Revolver debt | `$472M` at June 30 | Additional corporate funding balance |

The correct bridge is therefore:

```text
Antamina stream OCF proxy
  -> corporate tax / finance / debt context
  -> Antamina-specific allocation: not disclosed
  -> after-tax financed owner cash: unresolved
```

The corporate rows improve burden visibility and prevent an unbounded “pre-tax,
pre-interest” label from being mistaken for owner cash. They do not support
allocating all tax or finance cost to Antamina, nor do they prove debt-service
coverage or lender repayment.

Source: [Wheaton Q2 2026 net-cash-return pass](capital-flow-wheaton-antamina-net-cash-return-pass-1.md) and [Q2 2026 SEC debt/cash extraction](capital-flow-wheaton-6k-ifrs-debt-cash-extraction-pass-1.md).
