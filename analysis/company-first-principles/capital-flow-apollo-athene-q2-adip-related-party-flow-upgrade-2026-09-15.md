# Apollo–Athene Q2 ACRA/ADIP related-party flow upgrade

Research date: `2026-09-15`

Apollo's Q2 2026 Form 10-Q adds a current-period related-party flow table for
Athene's ACRA programs. The table distinguishes capital moving from ADIP into
Athene-related ACRA entities from distributions moving back to ADIP.

## Filed flow rows

| Flow | Q2 2026 | H1 2026 | Safe interpretation |
| --- | ---: | ---: | --- |
| Contributions from ADIP | `$145M` | `$271M` | Capital entered the ACRA route from Apollo-managed ADIP funds |
| Distributions to ADIP | `$47M` | `$301M` | Capital left the ACRA route to ADIP; it is not an AGM receipt |
| Mechanical H1 net flow | `NA` | `$30M` more distributions than contributions | A within-table direction screen only; not a return or common-owner cash measure |

The filing also states that Athene holds direct and VIE-related investments in
ADIP and had additional ADIP commitments. Those facts make the legal-entity
and ownership route more specific, but they do not identify the ultimate
source of ADIP cash, the bank settlement account, or any Apollo Global
Management, Inc. receipt.

## Proof-grade boundary

```text
ADIP contribution -> ACRA/Athene legal entity -> distribution to ADIP
       visible                 visible                    visible

ADIP or ACRA cash -> AGM receiving account -> unrestricted HoldCo -> common residual
       unresolved              unresolved             unresolved
```

The `$301M` H1 distribution must not be added to Athene's `$110M` direct-parent
distribution, `$375M` common dividends, or Apollo's consolidated cash. These
are different counterparties and reporting perimeters. The flow also cannot
be netted against Athene's `$271M` contribution without a dated settlement and
legal-entity cash ledger.

## Upgrade consequence

This advances the Apollo/Athene related-party route from an annual FY2025
observation to a current Q2/H1 2026 observation. It improves the capital-source
and destination map and provides a better next test for ADIP/ACRA return and
cash attribution. It does not close Q-07 or CA-06 because the AGM receiving
account, intercompany elimination, regulated-capital availability, liability
cost, and common-owner residual remain unproved.

Status: `current-period ACRA/ADIP flow visible; AGM receipt and common-owner cash unresolved`

## Primary source

- [Apollo Q2 2026 Form 10-Q](https://ir.apollo.com/sec-filings/content/0001858681-26-000040/apo-20260630.htm)
- Local archived source: `raw/primary-sources/capital-flow/apollo/q2-2026/apollo-2026-q2-10q.pdf`

Structured claims: [Q2 ACRA/ADIP flow CSV](data/capital-flow-apollo-athene-q2-adip-related-party-flow-upgrade-2026-09-15.csv).
