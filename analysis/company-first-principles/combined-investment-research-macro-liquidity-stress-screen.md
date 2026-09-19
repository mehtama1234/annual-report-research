# Combined investment research macro/liquidity stress screen

Research date: `2026-09-15`

This screen turns the transmission matrix into explicit bounded tests. It
does not forecast the macroeconomy and it does not convert illustrative
scenarios into fair values. Each row identifies the source-anchored starting
metric, the shock or stress channel, and the quantity that can—or cannot—be
recalculated with the current denominator.

The structured rows are in
[combined-investment-research-macro-liquidity-stress-screen.csv](data/combined-investment-research-macro-liquidity-stress-screen.csv).

## Cross-pilot stress results

### Retail affordability and temporary support

The existing normalized-cash screen gives a direct cash-boundary test. The
low case removes identified or candidate temporary support and selected
noncash items; the high case retains the reported cash-after-property bridge.
The range is not a normalized owner-cash conclusion because maintenance
capital, service costs, and all recurring working-capital behavior are not
fully separated.

| Company / period | Low screen | Base screen | High screen | Macro/liquidity interpretation |
| --- | ---: | ---: | ---: | --- |
| TJX FY2026 | `$4.464B` | `$4.703B` | `$4.917B` | Value demand can remain strong while temporary support and payables make reported cash look better than durable owner cash. |
| Target H1 2026 | `$0.597B` | `$1.209B` | `$2.115B` | Affordability recovery is visible, but tariff refunds, payables, share compensation, and service/capital burdens create a wide cash range. |
| Walmart H1 FY2027 | `$0.981B` | `$5.529B` | `$5.529B` | Scale and ecosystem growth are visible, but tariff and payable pass-through remains unresolved rather than silently deducted. |

### Wheaton–Antamina duration and price stress

The existing Antamina workbench applies explicit silver price, production,
horizon, stream step-down, and burden-haircut assumptions. It produces a
negative NPV in all three illustrative cases: bear `-3,951.6M USD`, base
`-2,603.4M USD`, and bull `-857.8M USD`. The result is an expectation-burden
screen, not proof that the transaction is uneconomic, because the delivery
curve, tax allocation, and debt waterfall remain incomplete.

### Apollo–Athene spread and liquidity stress

Apollo has a quantified starting point—H1 net investment earnings of `$7.8B`,
cost of funds of `$5.7B`, and a reported net investment spread of `1.41%`—but
the current evidence does not provide the asset/liability denominator needed
to translate a spread shock into parent common-owner cash. Athene also reports
`$41.617B` of policy deposits, `$14.741B` of withdrawals, and `$23.711B` of
ending cash including restricted and VIE cash. Those figures identify the
liquidity channel; they do not establish unrestricted cash available to
Apollo common owners. The stress result is therefore `denominator-held`, not
a fabricated sensitivity.

## Upgrade tests

1. Retail: separate recurring versus temporary vendor, tariff, payable, and
   service effects, then allocate maintenance capital.
2. Wheaton: replace illustrative production with BHP-only metal credits,
   realized settlement prices, taxes, interest, and debt service.
3. Apollo: obtain legal-entity spread, duration, liability-cost, capital, and
   upstream-receipt schedules before calculating a parent-owner stress.

Primary routes: [macro/liquidity transmission matrix](combined-investment-research-macro-liquidity-transmission-matrix.md), [retail normalized-cash screen](combined-investment-research-pilot-02-retail-normalized-cash-screen.md), [Antamina scenario workbench](combined-investment-research-pilot-01-antamina-scenario-workbench.md), and [Apollo common-owner bridge](combined-investment-research-pilot-03-apollo-common-owner-bridge.md).
