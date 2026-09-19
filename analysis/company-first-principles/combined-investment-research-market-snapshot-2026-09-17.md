# Combined investment research market snapshot — 2026-09-17

Observation date: `2026-09-17` (live U.S. market-data lookup at capture)

This refresh updates the market-cap inputs used by the illustrative retail and
Apollo expectation workbenches. It does not change their normalized-cash
assumptions or promote any result to intrinsic value.

| Ticker | Company | Price | Market capitalization |
| --- | --- | ---: | ---: |
| TJX | TJX Companies | `$122.84` | `$137.212B` |
| TGT | Target | `$154.68` | `$70.627B` |
| WMT | Walmart | `$107.50` | `$857.635B` |
| APO | Apollo Global Management | `$124.53` | `$75.991B` |
| WPM | Wheaton Precious Metals | `$146.73` | `$66.515B` |

## Updated retail expectation surface

| Company | Market value | Multiple cases | Required annual cash |
| --- | ---: | --- | ---: |
| TJX | `$137.212B` | Annual reported cash-after-property screen | `27.906x` on `$4.917B` FY2026 reported cash-after-property |
| Target | `$70.627B` | `18x / 24x / 30x` | `$3.924B / $2.943B / $2.354B` |
| Walmart | `$857.635B` | `30x / 38x / 45x` | `$28.588B / $22.569B / $19.059B` |

These are market value divided by the stated illustrative cash multiple. They
are expectation burdens, not forecasts or owner-cash observations. Target's
latest H1 cash-after-property screen is `$2.115B`; Walmart's is `$5.529B`.
Neither is normalized for the open maintenance-capital, tax, lease, supplier-
finance, attached-service, seasonality, and dilution gates.

TJX's row is a reported annual cash-after-property screen, not a normalized
owner-cash multiple. Target and Walmart's multiple cases remain illustrative
expectation tests, and their annual reported-cash screens are separately
controlled in the [annual reported-cash expectation screen](combined-investment-research-pilot-02-retail-annual-reported-cash-expectation-screen-2026-09-17.md).
Wheaton remains outside a segment market-value translation because Antamina
cannot be isolated from public equity value. Apollo's separated-earnings
screen remains governed by its existing SOTP workbench and promotion matrix;
the live quote is recorded here without silently changing its held-constant
FRE/SRE/principal assumptions.

## Status and reproducibility

Status: `current-market-input; qualified-expectation-screen`.

The market quote is time-sensitive and should be refreshed before an
investment decision. Structured retail calculations are in the companion
[CSV](data/combined-investment-research-market-snapshot-2026-09-17.csv).
Historical comparison remains in the
[September 16 snapshot](combined-investment-research-market-snapshot-2026-09-16.md).

Quote routes: [TJX](https://www.nasdaq.com/market-activity/stocks/tjx),
[Target](https://www.nasdaq.com/market-activity/stocks/tgt),
[Walmart](https://www.nasdaq.com/market-activity/stocks/wmt),
[Apollo](https://www.nasdaq.com/market-activity/stocks/apo), and
[Wheaton](https://www.nasdaq.com/market-activity/stocks/wpm).
