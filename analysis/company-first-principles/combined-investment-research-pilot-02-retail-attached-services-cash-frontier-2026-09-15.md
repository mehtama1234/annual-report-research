# Pilot 02 Retail Attached-Services Cash Frontier

Research date: `2026-09-15`

This memo adds a bounded sensitivity layer to queue item `Q-06`. It does not
claim that reported attached-service revenue is cash, nor does it change the
normalized retail owner-cash denominator.

## Mechanical frontier

Target's H1 2026 attached-service pool is `$1.141B`, composed of advertising,
credit-card profit sharing, and other revenue. Walmart's H1 FY2027 screen is
`$3.855B`, the sum of U.S., International, and Sam's Club U.S. membership and
other income. The latest consolidated filing separately reports `$3.904B` of
membership and other income; the `$49M` difference is preserved as an
unreconciled perimeter item in the [Walmart attached-income denominator
reconciliation](combined-investment-research-pilot-02-walmart-attached-income-denominator-reconciliation-2026-09-16.md).
The structured frontier applies conversion rates of `0%`, `25%`,
`50%`, `75%`, and `100%` to those reported pools:

| Company | 0% | 25% | 50% | 75% | 100% |
| --- | ---: | ---: | ---: | ---: | ---: |
| Target H1 2026 | `$0M` | `$285.25M` | `$570.5M` | `$855.75M` | `$1.141B` |
| Walmart H1 FY2027 | `$0M` | `$963.75M` | `$1.9275B` | `$2.89125B` | `$3.855B` |

These are arithmetic frontiers only. They exclude direct service labor,
fulfillment, technology, marketing, overhead, working capital, taxes, capex,
leases, debt, stock compensation, dilution, and legal-entity transfer effects.
For Target, the card route is a profit-sharing receipt while TD owns and funds
the receivables; for Walmart, membership and other income contains items beyond
membership. Therefore the 100% column is an upper-bound screen, not a plausible
owner-cash conclusion.

## Denominator discipline

Target's H1 operating cash flow is `$4.519B`; Walmart's H1 operating cash flow is
`$19.710B`. Those figures remain consolidated denominators. The frontier does
not add its mechanical values to either company's owner cash, valuation
workbench, or per-share cash table.

The useful result is a decision boundary: even if future filings support a
positive conversion rate, the rate must be tied to service-level cash receipts
and all allocated burdens before it can enter normalized owner cash. A source
that only repeats revenue or segment operating income does not pass that test.

## Proof-grade result

| Gate | Result |
| --- | --- |
| Reported attached-service pool | Proven as a revenue/income screen |
| Mechanical 0–100% frontier | Proven as sensitivity arithmetic |
| Observed attached-service cash | Not proven |
| Incremental owner cash | Excluded from normalized cash |
| Required next proof | Service-level cost, collection, working-capital, capex, tax, and legal-entity cash schedule |

## Primary source artifacts

- [Attached-services cash upgrade](combined-investment-research-pilot-02-retail-attached-services-cash-upgrade-2026-09-15.md)
- [Attached-services boundary ledger](data/combined-investment-research-pilot-02-retail-attached-services-boundary.csv)
- [Retail normalized cash screen](data/combined-investment-research-pilot-02-retail-normalized-cash-screen.csv)
