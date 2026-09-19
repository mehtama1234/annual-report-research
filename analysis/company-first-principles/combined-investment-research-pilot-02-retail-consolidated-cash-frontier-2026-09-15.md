# Pilot 02 retail consolidated cash frontier — 2026-09-15

This frontier joins two uncertainty dimensions that previously appeared in
separate workbenches: the share of property spending treated as maintenance and
the removal of a source-bounded temporary-support candidate. It is a sensitivity
map, not a normalized owner-cash conclusion.

## Formula and inputs

```text
cash frontier = OCF − (property spending × assumed maintenance share)
                − (support-removal assumption × support candidate)
```

The support candidate is not asserted to be entirely nonrecurring. No lease,
tax, dilution, attached-service, inventory, supplier-finance, or maintenance-
versus-growth conclusion is hidden inside the calculation. Stock-based
compensation is shown separately where available and is not subtracted from the
frontier a second time.

| Company / period | OCF | Property spending | Support candidate | SBC shown separately |
| --- | ---: | ---: | ---: | ---: |
| TJX H1 FY2027 | `$3.345B` | `$1.159B` | `$750M` | `$85M` |
| Target H1 2026 | `$4.519B` | `$2.404B` | `$1.364B` | `$154M` |
| Walmart H1 FY2027 | `$19.710B` | `$14.181B` | `$4.548B` | Not separately populated |

## Four-corner frontier

| Company / period | 0% maintenance, no support removal | 100% maintenance, no support removal | 0% maintenance, support removed | 100% maintenance, support removed |
| --- | ---: | ---: | ---: | ---: |
| TJX H1 FY2027 | `$3.345B` | `$2.186B` | `$2.595B` | `$1.436B` |
| Target H1 2026 | `$4.519B` | `$2.115B` | `$3.155B` | `$751M` |
| Walmart H1 FY2027 | `$19.710B` | `$5.529B` | `$15.162B` | `$981M` |

The fourth corner is a source-bounded lower screen before separately testing SBC,
tax, leases, service costs, and other claims. For Target, subtracting the
separately disclosed `$154M` SBC from that corner would produce `$597M`, matching
the existing low screen; this is a reconciliation, not an additional deduction
from the frontier.

## Company-specific capex-boundary overlay

The four-corner grid treats Walmart's full `$14.181B` H1 property spending as
potential maintenance at its lower edge. Walmart's filing separately identifies
`$1.087B` of new stores and clubs. Treating that category as a minimum growth
bucket produces a narrower, labeled classification screen:

```text
H1 OCF                                      $19.710B
- implied maintenance ceiling ($14.181B - $1.087B)  $13.094B
= OCF less implied maintenance              $6.616B
```

This is not reported owner cash. It is the cash result if all non-new-store
spending is conservatively classified as maintenance. The overlay narrows the
capex classification range but does not resolve inventory and payable timing,
supplier finance, leases, taxes, stock compensation, attached-service costs,
debt, or dilution. The structured overlay is recorded in the [capex-boundary
CSV](data/combined-investment-research-pilot-02-retail-capex-boundary-overlay-2026-09-15.csv).

## Interpretation boundary

The frontier makes the denominator uncertainty visible without choosing a
maintenance share or declaring every support item nonrecurring. It cannot solve
seasonality, inventory turns, payable and supplier-finance timing, tax, leases,
service economics, or diluted per-share cash. The values must remain outside a
promoted owner-cash valuation until the [promotion matrix](combined-investment-research-owner-cash-promotion-matrix-2026-09-15.md)
gates close.

Status: `consolidated source-bounded frontier; normalized owner cash unresolved`.

Sources: [retail capex allocation sensitivity](combined-investment-research-pilot-02-retail-capex-allocation-sensitivity.md), [retail normalized-cash screen](combined-investment-research-pilot-02-retail-normalized-cash-screen.md), [retail margin and working-capital matrix](combined-investment-research-pilot-02-retail-margin-working-capital-normalization.md), and [temporary-support artifacts](combined-investment-research-pilot-02-retail-temporary-support.md).

Structured result: [retail consolidated cash frontier CSV](data/combined-investment-research-pilot-02-retail-consolidated-cash-frontier-2026-09-15.csv).
