# Active pilot packet coverage matrix — 2026-09-16

This matrix tests the packet requirement for the active pilots. A packet is
not considered complete merely because a company page exists: the review must
also identify the annual filing, the relevant quarter window, results
materials, investor-relations route, source ledger, and any missing call or
legal-entity evidence.

The matrix is a coverage control, not a claim that every source is equally
deep or that management commentary is independently verified. The current
quarter additions are linked through the pilot dossiers and primary-source
artifacts; older packet baselines remain visible where the archive snapshot
predates the latest filing.

| Company / entity | Packet | Source ledger | Deep dossier | Annual filing | Three-quarter window | Results / IR route | Call transcript | Current pilot evidence | Coverage status | Remaining gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TJX | Yes | Yes | Yes | Yes | Yes: Q3 FY2026, Q4 FY2026, Q1 FY2027; Q2 FY2027 current filing added | Yes | Official Q2 FY2027 webcast/replay route; no locally preserved transcript text | H1 FY2027 10-Q and cash/burden upgrades | `active-pilot-packet-with-call-route` | Preserve the official call route or transcript text if management-language analysis is required |
| Target | Yes | Yes | Yes | Yes | Yes: Q3 2025, Q4 2025, Q1 2026; Q2 2026 added through current dossier | Yes | Official Q2 2026 downloadable transcript route; structured claim memo preserved | Q2 2026 10-Q, earnings release, call, inventory/payable, attached-service, and cash upgrades | `active-pilot-packet-current-filing-added` | Reconcile call claims to service-level cost and cash evidence |
| Walmart | Yes | Yes | Yes | Yes | Yes: Q3 2025, Q4 2025, Q1 2026; Q2 FY2027 added through current dossier | Yes | Official Q2 FY2027 management-call PDF available; structured control-point memo and claim CSV now preserved | Q2 FY2027 10-Q, earnings release, capex, ecosystem, cash, and call-control-point upgrades | `active-pilot-packet-with-call-route` | Preserve a local transcript copy only if reproducible full-text analysis is needed; separately allocate attached-service cash |
| Wheaton | Yes | Yes | Yes | Yes | Yes: Q4 2025, Q1 2026, Q2 2026 | Yes: September 2026 Corporate Presentation | No local standalone transcript; the archived webinar route has no machine-readable transcript text | Antamina payment, counterparty, delivery, financing, dual-PMPA denominator, and settlement-boundary artifacts | `active-capital-flow-packet-with-receipt-gap` | Obtain any future transcript/recording extract, BHP-PMPA settlement quantity, receipt, and return evidence |
| Apollo | Yes | Yes | Yes | Yes | Yes: Q4 2025, Q1 2026, Q2 2026 artifacts | Yes | Yes: Q4 2025, Q1 2026, Q2 2026 artifacts | Q2 10-Q, supplement, XBRL boundary, HoldCo, parent-flow, AMAPS 1 wrapper-exposure, and Concord servicing artifacts | `active-capital-flow-packet-with-entity-gap` | Join Athene source flows to AGM receipt, elimination, senior claims, and common-owner residual |
| Athene legal entity | No standalone public-company packet | Covered by Apollo ledger and statutory artifacts | Covered by Apollo/Athene dossiers | Yes: statutory annual and Q2 materials | Yes: statutory FY2025 and Q2 2026 evidence | Yes: statutory exhibits and schedules | Not applicable as a separate listed-company packet | Schedule D, statutory cash, parent-flow, ARI, and legal-dividend artifacts | `legal-entity-subpacket` | Add dated receiving-account, borrower collection, liability-cost, and distributability evidence |

Structured version: [active-pilot packet coverage CSV](data/combined-investment-research-active-pilot-packet-coverage-2026-09-15.csv).

Walmart call upgrade: [management-call control-point memo](combined-investment-research-pilot-02-walmart-q2-management-call-control-point-upgrade-2026-09-15.md) and [structured claim CSV](data/combined-investment-research-pilot-02-walmart-q2-management-call-control-point-upgrade-2026-09-15.csv).

Target call upgrade: [Q2 2026 management-call control-point memo](combined-investment-research-pilot-02-target-q2-management-call-control-point-upgrade-2026-09-15.md) and [structured claim CSV](data/combined-investment-research-pilot-02-target-q2-management-call-control-point-upgrade-2026-09-15.csv).

## Route-integrity boundary

Several older extracted packet ledgers retain virtual `/raw/...` reader routes
or absolute paths from an earlier workspace. These are intentional provenance
identities under the repository's [raw-evidence link policy](../../notes/raw-evidence-link-policy-2026-08-11.md),
not claims that a heavy raw file must be present in the checkout. The
[offload manifest](../../indexes/raw-blob-offload-manifest-2026-08-10.csv) and
[resolver](../../scripts/resolve-offloaded-raw-path.py) provide the recovery
route and Drive pointer. The active pilot's `analysis/` dossiers, SEC/IR URLs,
primary-source bundles, and checked ledger artifacts remain the authoritative
routes for current claims. D-04 remains partial because roster-wide depth and
some call-transcript/current-quarter coverage are uneven—not because an
offloaded raw artifact is automatically considered broken.

## Interpretation

The active pilot packet requirement is substantially met for the selected
cases, but not uniformly complete. TJX and Walmart have strong filing and IR
coverage while lacking locally preserved call transcripts. Target now has an
official Q2 transcript route and a structured claim memo; the remaining gap is
reconciling those management observations to service-level cost and cash
evidence. Wheaton's packet is adequate for the named
capital-flow question but remains intentionally incomplete at the receipt and
return layer. Athene is treated as a legal-entity subpacket rather than a
fictional standalone company packet, which preserves the correct entity
boundary for the Apollo case.

This matrix therefore improves D-04's evidence visibility without promoting
the broader roster-wide packet deliverable to complete.

## Newly confirmed official call routes

- [TJX Q2 FY2027 conference-call event](https://investor.tjx.com/events/event-details/second-quarter-fiscal-2027-earnings-results-conference-call)
  confirms the August 19, 2026 call and official webcast/replay route.
- [Walmart Q2 FY2027 financial-results archive](https://stock.walmart.com/financial-information/financial-results)
  lists the management-call transcript for the quarter. The direct official
  PDF route is available from that archive, although automated retrieval may
  be access-controlled.
