# MetLife Packet

Date baseline: 2026-08-10

## Snapshot

- Company: MetLife, Inc.
- Sector: Financial
- Industry: Life Insurance
- Ticker: `MET`
- Fiscal year-end: December 31
- Target annual report year: 2025
- Target quarter window:
  - quarter 1: `2Q26`
  - quarter 2: `1Q26`
  - quarter 3: `4Q25`
- Proof status in current repo: `qualified`

## Source state

- AnnualReports is used here for taxonomy and archive-confirmation context only; as of `2026-08-10`, the hosted annual package still lagged at `2024`.
- Company IR and SEC are the authoritative annual-plus-quarter chain for this packet.
- Direct local IR binary capture was blocked by Cloudflare, so the current proof standard depends more heavily on the locally saved SEC filing chain plus the verified official IR URLs recorded in `ir-source-links.md`.

## Annual report takeaways

- MetLife gives CLI 6 the large-scale life-insurance and retirement-risk-transfer model, where earnings depend on underwriting, spread income, investment results, longevity and morbidity assumptions, and disciplined capital return rather than on loan growth or rent collection.
- Full-year `2025` net income was `$3.2B`, diluted EPS was `$4.71`, adjusted EPS excluding notable items was `$8.89`, adjusted ROE was `16.0%`, and management said it returned nearly `$4.4B` to shareholders.
- The annual read is that MetLife is less a simple insurer than a global liability-and-asset management system whose strength depends on balance-sheet flexibility, investment income, pension risk transfer, and disciplined capital release.
- Compared with PNC, MetLife carries less direct credit-cycle visibility in the reported narrative and more sensitivity to investment income, reserving, product mix, and shareholder return capacity.

## Quarter-by-quarter takeaways

### Most recent quarter: 2Q26

- Results: official IR and SEC materials indicated net income of about `$705M`, diluted EPS of about `$1.09`, adjusted earnings of about `$1.6B`, and adjusted EPS of about `$2.43`.
- Operating detail: the quarter chain pointed to premiums, fees, and other revenues of about `$13.7B`, net investment income of about `$6.7B`, and a new `$3.0B` share-repurchase authorization announced on `2026-08-05`.
- Strategic read: `2Q26` shows a more mixed headline than the prior quarter, but the company is still operating from a scale-and-capital-return position rather than a distress position.
- Source note: local IR binary capture was blocked by Cloudflare, so the authoritative saved evidence for the quarter is the SEC wrapper chain plus the verified official IR URLs in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/life-insurance/metlife-inc/ir-source-links.md).

### Quarter minus 1: 1Q26

- Results: net income was `$1.1B`, diluted EPS was `$1.74`, adjusted earnings were `$1.586B`, and adjusted EPS was `$2.42`.
- Operating detail: premiums, fees, and other revenues were about `$14.315B`, net investment income was about `$5.355B`, holding-company cash and liquid assets were about `$3.9B`, ROE was `18.2%`, and adjusted ROE was `17.0%`.
- Structural read: `1Q26` showed the more attractive version of the MetLife model, where investment income, underwriting, and global diversification reinforce one another rather than offsetting weakness elsewhere.

### Quarter minus 2: 4Q25

- Results: fourth-quarter net income was `$778M`, adjusted earnings were `$1.648B`, and adjusted EPS was `$2.49`.
- Full-year readthrough: management framed `2025` around adjusted earnings durability, capital return, strong adjusted ROE, and solid liquidity, which is exactly what a life insurer needs to prove when market narratives start to focus on duration and asset sensitivity.
- Structural read: `4Q25` is the right baseline for seeing MetLife as a recurring-care-and-retirement institution rather than just an insurance label.

## Signals to feed into higher-level analysis

- Consumer and societal pattern: MetLife monetizes the need for retirement security, protection, and pension de-risking, which are slow-moving but socially persistent demands.
- Industrial pressure: investment income, reserving, and capital deployment matter more than top-line volume alone.
- Cultural shift: aging populations and institutional willingness to offload pension obligations keep supporting the life-insurance and retirement-transfer layer.
- Bigger-picture read: MetLife shows how CLI 6 should think about balance-sheet-heavy financial businesses that are not obviously cyclical each quarter but still live or die by portfolio discipline and liability management.

## Source pointers

- [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/life-insurance/metlife-inc/annualreports-verification.md)
- [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/life-insurance/metlife-inc/ir-source-links.md)
- [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/2025-10k.html)
- [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/2025-q4-8k.html)
- [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/2026-q1-10q.html)
- [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/2026-q1-8k.html)
- [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/2026-q2-10q.html)
- [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/2026-q2-8k.html)

## Evidence-status note

- The filing window used here is explicit and internally consistent with the company profile and source ledger.
- The authority ordering is explicit:
  - AnnualReports for taxonomy and archive-lag confirmation
  - company IR and SEC for the authoritative annual and quarter chain
- The main current weakness is capture method, not period definition:
  - the SEC annual and quarter filing chain is locally present
  - clean local IR binaries were not preserved because direct retrieval was Cloudflare-blocked
- The right reading standard today is:
  - strong enough for thematic interpretation and lane comparison
  - still `qualified`, not fully `proven`, for thin-lane source-authority closeout work
