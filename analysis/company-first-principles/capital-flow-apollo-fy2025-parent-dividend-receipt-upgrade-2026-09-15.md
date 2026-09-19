# Apollo FY2025 Parent Dividend-Receipt Upgrade

Research date: `2026-09-15`

This pass inspects Apollo's FY2025 10-K XBRL contexts rather than relying on a
consolidated cash total. The relevant facts use the explicit
`srt:ParentCompanyMember` context (`c-1604`) for the year ended December 31,
2025.

## Parent-only receipt facts

Primary source:

`raw/primary-sources/capital-flow/apollo/fy-2025/apollo-2025-10k.html`

| Parent-company fact | FY2025 amount | Interpretation |
| --- | ---: | --- |
| Proceeds from dividends received | `$750M` | Parent-company dividend receipt is visible |
| Proceeds from distribution from subsidiary investing activities | `$750M` | Custom Apollo parent-company distribution line reconciles to the receipt |
| Payments related to distribution to subsidiary investing activities | `$148M` | A separate parent-company distribution-related outflow remains visible |
| Common-stock dividends paid | `$1.201B` | Parent-level common cash use |
| Preferred-stock dividends paid | `$97M` | Parent-level preferred cash claim ahead of common residual |

The two receipt lines agree at `$750M`. This is stronger than the prior
policy-level statement that subsidiaries are an expected source of parent
liquidity: it shows a parent-company receipt field in the filed cash-flow
taxonomy.

## Boundary

The `ParentCompanyMember` context does not identify which subsidiary paid the
`$750M`, whether Athene supplied all or part of it, the date of each transfer,
the receiving bank account, or the intercompany elimination. It therefore does
not support the claim that Athene's `$375M` H1 2026 common dividend schedule
reached AGM, nor does it prove that the parent receipt became cash available to
Apollo common owners after debt, tax, preferred, NCI, repurchase, and retained-
capital claims.

The parent cash-use lines also cannot be netted into a distributable common
return without the source priority and legal-entity waterfall.

## Safe grade

`parent-only-dividend-receipt-visible` — FY2025 parent-company receipt and
matching subsidiary-distribution proceeds are source-backed and reconciled.
Athene attribution, transfer timing, unrestricted availability, and the final
common-owner residual remain open.
