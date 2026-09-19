# Combined investment research historical macro-regime validation

Research date: `2026-09-15`

This artifact adds a historical regime panel to the current-regime macro
anchor. It tests whether the proposed affordability, duration, funding, and
liquidity mechanisms were observed across materially different U.S. inflation
and policy-rate regimes. It is a regime-consistency test, not a causal
estimate of any company's results.

The structured rows are in
[the historical-regime CSV](data/combined-investment-research-macro-historical-regime-validation-2026-09-15.csv).
The contemporaneous company bridge is in the [common-period company/regime
join](data/combined-investment-research-macro-common-period-company-regime-join-2026-09-15.csv).

The longitudinal retail bridge separately records a macro-panel source and a
company-filing source for every row, so the copied regime values and the
cash-after-property calculation can be independently re-opened:
[macro-longitudinal retail bridge](data/combined-investment-research-macro-longitudinal-retail-bridge-2026-09-15.csv).

## Official regime panel

| Period | Observation basis | Annual-average CPI-U index | Approx. annual CPI change | Year-end / latest federal-funds target range | Real average hourly earnings year-over-year | Regime reading |
| --- | --- | ---: | ---: | --- | ---: | --- |
| 2020 | Annual CPI average; December real earnings and year-end target range | `111.098` | `+1.2%` | `0%–0.25%` | `+3.7%` in December | Pandemic disruption and emergency policy produced an unusual labor-composition and liquidity regime; real hourly earnings rose while activity and funding conditions were highly abnormal |
| 2021 | Annual CPI average; December real earnings and year-end target range | `116.318` | `+4.7%` | `0%–0.25%` | `-2.4%` in December | Reopening demand and supply constraints lifted inflation while policy remained near zero; real hourly earnings compressed |
| 2022 | Annual CPI average; December real earnings and year-end target range | `125.626` | `+8.0%` | `4.25%–4.50%` | `-1.7%` in December | Inflation and rate shock squeezed household purchasing power and raised financing hurdles |
| 2023 | Annual CPI average; December real earnings and year-end target range | `130.797` | `+4.1%` | `5.25%–5.50%` | `+0.8%` in December | Disinflation began while restrictive rates remained high; real-wage pressure eased |
| 2024 | Annual CPI average; December real earnings and year-end target range | `134.655` | `+2.9%` | `4.25%–4.50%` | `+1.0%` in December | Inflation moderated, real wages recovered, and policy began easing |
| 2025 | Annual CPI average; December real earnings and year-end target range | `138.289` | `+2.7%` | `3.50%–3.75%` | `+1.1%` in December | Lower policy rate and continued positive real-wage growth supported a less restrictive consumer regime |
| 2026 current | August CPI and real earnings; July target range | Not a completed annual average | `+3.4%` year-over-year CPI | `3.50%–3.75%` in July | `-0.3%` in August | Cost pressure and real-wage softness have reappeared even while nominal demand remains resilient |

The CPI-U annual-average values are calculated from the official BLS annual
index table. The federal-funds ranges are the Federal Reserve's target ranges;
the 2026 row uses the latest July range available at the research date. The
2026 CPI and real-earnings observations are monthly current-regime readings and
must not be mixed with the completed annual rows.

The 2020 real-earnings observation is especially sensitive to pandemic labor
composition and should not be read as broad household purchasing-power proof.
It is retained because it tests whether the macro layer can label an abnormal
regime rather than smooth it away.

## Pilot-level validation

### Retail affordability

The regime panel is directionally consistent with the retail mechanism:
real-wage contraction during the 2022 inflation shock supports a trade-down
and value-seeking hypothesis; real-wage recovery during 2023–2025 is consistent
with a less constrained consumer backdrop; and the 2026 real-wage reversal
keeps affordability pressure live. The company filings show traffic,
comparable sales, mix, inventory, payables, and cash effects, but fiscal periods
and company actions differ. The panel therefore does not identify how much of
any retailer's result was caused by real wages or inflation.

### Wheaton–Antamina

The rate panel validates that a long-duration, debt-funded stream should be
tested across materially different discount-rate and financing regimes. The
2026 transaction has only a post-close operating period in the current pilot,
so historical macro rows cannot demonstrate a through-cycle Antamina response.
The correct use is to stress financing cost, discount rate, silver price, and
delivery timing separately until BHP-only settlement and Wheaton debt-service
records become available.

### Apollo–Athene

The rate panel validates the direction of the spread/liquidity mechanism:
policy rates moved down after the 2023 peak while Athene's H1 2026 reported net
investment spread was below the prior-year level. That comparison is a useful
falsifiable signal, not causal proof. Asset mix, credit losses, liability
duration, hedges, policy flows, and accounting marks can move the spread at the
same time; the parent-receipt and regulated-capital gaps remain open.

## Common-period company bridge

The 2026 current-regime row can now be joined to a same-period company panel:

| Pilot | Company / entity | Reporting period | Primary metric | Secondary metric | Tertiary metric | Correct reading |
| --- | --- | --- | ---: | ---: | ---: | --- |
| Retail | TJX | H1 FY2027 | `$3.345B` OCF | `$1.159B` property additions | `$2.186B` cash after property | Reported denominator screen, not normalized owner cash |
| Retail | Target | H1 2026 | `$4.519B` OCF | `$2.404B` property spending | `$2.115B` cash after property | Recovery and cash are visible, but tariff/payable support remains material |
| Retail | Walmart | H1 FY2027 | `$19.710B` OCF | `$14.181B` capital spending | `$5.529B` company-defined FCF | Scale cash is visible, but reinvestment and pass-through remain unresolved |
| Wheaton–Antamina | Wheaton | H1 2026 | `$222.223M` Antamina OCF proxy | `$4.300B` PMPA payment | `$32.502M` company finance costs | Stream cash and financing context are visible; allocation is not |
| Apollo–Athene | Athene | H1 2026 | `$7.8B` net investment earnings | `$5.7B` cost of funds | `1.41%` net investment spread | Insurer spread screen is visible; parent common cash is not |

This is a common-period bridge, not a pooled ranking. The metrics have different
denominators and legal-entity locations; the table exists to make those
differences explicit while attaching each observation to the same 2026 regime
row.

The 2023 real-earnings cell uses the BLS revised/summary observation of `+0.8%`.
The initial January 2024 release reported `+1.0%` for the same December 2022 to
December 2023 comparison. Both figures are preserved in the source trail; the
panel uses the revised/summary figure consistently and does not treat the small
revision as an economic turning point.

## Status and next test

`historical-regime-consistency-partial`: the official macro panel now spans
inflation, real wages, and policy rates across 2020–2026 and is joined to
pilot-specific mechanisms plus a same-period 2026 company panel. It does not
yet satisfy through-cycle causal validation. The next upgrade is a longitudinal
company panel that joins each filing's demand, margin, funding, spread,
liquidity, and owner-cash denominator to multiple regime rows without mixing
fiscal periods.

## Primary sources

- [BLS annual CPI-U index table, 2002–2025](https://www.bls.gov/pir/spm/spm_chart_2025data.htm)
- [Federal Reserve target federal-funds-rate history](https://www.federalreserve.gov/monetarypolicy/openmarket.htm)
- [BLS December 2020 real earnings release](https://www.bls.gov/news.release/archives/realer_01132021.htm)
- [BLS December 2021 real earnings release](https://www.bls.gov/news.release/archives/realer_01122022.htm)
- [BLS December 2022 real earnings release](https://www.bls.gov/news.release/archives/realer_01122023.htm)
- [BLS December 2023 real earnings initial release](https://www.bls.gov/news.release/archives/realer_01112024.htm)
- [BLS December 2023 real earnings revised/summary observation](https://www.bls.gov/opub/ted/2024/real-average-hourly-earnings-increased-0-8-percent-from-december-2022-to-december-2023.htm)
- [BLS December 2025 real earnings release](https://www.bls.gov/news.release/archives/realer_01132026.htm)
- [BLS August 2026 real earnings release](https://www.bls.gov/news.release/realer.nr0.htm)
- [BLS August 2026 CPI release](https://www.bls.gov/news.release/archives/cpi_09112026.htm)
