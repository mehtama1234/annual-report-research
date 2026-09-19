# Annual Report Research Workspace

Date baseline: 2026-08-10

This workspace is for collecting, organizing, and analyzing company annual reports, quarterly earnings materials, and cross-company themes by sector and industry.

Primary collection window for this project:

- `2025` annual reports and annual filings
- `2026` quarterly earnings materials as the primary quarterly focus
- the trailing quarter from late `2025` only when needed to complete the last three reported quarters as of `2026-08-10`

It is intentionally split into three layers:

- `raw/` - source documents and source-ledger notes
- `extracted/` - normalized company packets and extracted facts
- `analysis/` - sector, industry, and theme synthesis

This keeps raw evidence separate from downstream interpretation.

## New reader? Start here

If you just want to understand what this archive found — not continue the research — use the reader layer, not the operator briefs below:

- **Live local reader:** [http://localhost:8765/](http://localhost:8765/) — run `python3 scripts/reader-server.py 8765` first.

- [How to read this archive](/notes/how-to-read-this-archive-2026-08-12.md) — the front door: what this is, the one central idea, and where to look.
- [What this archive proves](/analysis/cross-sector/what-this-archive-proves-2026-08-12.md) — the main proven findings in plain English, each backed by named companies.
- [Four lane summaries](/analysis/cross-sector/four-lane-summaries-2026-08-12.md) — the original lane summaries; the live reader now adds software, security, industrial, and energy cohort paths.
- [Comparison library map](/analysis/cross-sector/comparison-library-map-2026-08-12.md) — a grouped index into the detailed company-by-company comparison pages.

Everything below this point is for an operator who is continuing the research.

Remote `main` currently carries the extracted, analysis, notes, and index layers, but not the heavy offloaded `raw/**` payload.
If a packet cites a raw evidence path that is no longer present in the checkout, resolve it through:

- [Raw blob offload readme](/notes/raw-blob-offload-readme-2026-08-10.md)
- [Raw evidence link policy](/notes/raw-evidence-link-policy-2026-08-11.md)
- [Legacy root reference audit](/notes/legacy-root-reference-audit-2026-08-11.md)
- `python3 scripts/resolve-offloaded-raw-path.py 'raw/.../file.ext'`
- `bash scripts/verify-raw-evidence-governance.sh`

## Current operating brief

Start here:

- [START-HERE.md](/START-HERE.md)

That file points to the active operator brief, lane instructions, next-step workflow, and current handoff.
Together those files define the end-to-end pursuit goal, the lane-level output standard, the `3` to `4` flagship-company batch rule, the handoff requirements, and the expanded lane coverage across recreation, healthcare frontier, connectivity / telecom / infra tech, and capital structures / property / conglomerates.

For the latest dated market-expectation burden surface across the expanded
lanes, use the [current expectation-screen index](/analysis/company-first-principles/combined-investment-research-current-expectation-screen-index-2026-09-18.md)
and its [structured CSV](/analysis/company-first-principles/data/combined-investment-research-current-expectation-screen-index-2026-09-18.csv).
It is a routing and denominator-control surface, not a ranking or normalized
owner-cash table.

If you want the shortest continuation-mode statement of what work is still left, which lanes matter most, and what outputs now count as real progress, use:

- [Remaining meaty end-to-end operator brief](/notes/remaining-meaty-end-to-end-operator-brief-2026-08-11.md)
- [Remaining end-to-end insight goal](/notes/remaining-end-to-end-insight-goal-2026-08-11.md)
- [Remaining insight execution board](/notes/remaining-insight-execution-board-2026-08-11.md)

If you want the explicit audit trail for why those live surfaces now default to strengthening already-open lanes rather than restarting them from zero, use:

- [Continuation mode alignment audit](/notes/continuation-mode-alignment-audit-2026-08-11.md)

For the fastest lane-selection view, use:

- [Active lane board](/notes/active-lane-board-2026-08-10.md)
- [Current execution queue](/notes/current-execution-queue-2026-08-10.md)
- [Forensic cross-sector research handoff](/notes/handoff-2026-09-13-forensic-cross-sector.md)
- [Current end-to-end research handoff](/notes/handoff-2026-09-14-end-to-end-research.md)
- [Lane-by-lane completion audit](/notes/lane-completion-audit-2026-09-14.md)
- [Combined end-to-end forensic research system](/analysis/cross-sector/combined-end-to-end-forensic-research-system-2026-09-13.md)
- [Healthcare, aging, and owner cash synthesis](/analysis/cross-sector/healthcare-aging-to-owner-cash-forensic-synthesis-2026-09-14.md)
- [AI physical capacity to owner cash synthesis](/analysis/cross-sector/ai-physical-capacity-to-owner-cash-forensic-synthesis-2026-09-14.md)
- [Financial intermediation to common-owner cash synthesis](/analysis/cross-sector/financial-intermediation-to-owner-cash-forensic-synthesis-2026-09-14.md)
- [Recreation, lifestyle, and occasion demand comparison](/analysis/cross-sector/recreation-lifestyle-occasion-demand-comparison-2026-08-11.md)
- [Backlog visibility versus cash realization synthesis](/analysis/cross-sector/backlog-visibility-to-cash-realization-forensic-synthesis-2026-09-13.md)
- [Control point versus burden carrier synthesis](/analysis/cross-sector/control-point-versus-burden-carrier-synthesis-2026-09-13.md)
- [Healthcare distribution owner-cash peer synthesis](/analysis/cross-sector/healthcare-distribution-owner-cash-peer-synthesis-2026-09-13.md)
- [Healthcare control points: clinical evidence, workflow access, and owner cash](/analysis/cross-sector/healthcare-control-points-clinical-evidence-workflow-and-owner-cash-2026-09-13.md)
- [Amazon full forensic analysis memo](/analysis/deep-company-pages/amazon-com-inc.md)
- [Alphabet full forensic analysis memo](/analysis/deep-company-pages/alphabet-inc.md)
- [Restaurant franchise and occasion forensic comparison](/analysis/cross-sector/restaurant-franchise-and-occasion-forensic-comparison-2026-09-13.md)
- [Wingstop full forensic analysis memo](/analysis/deep-company-pages/wingstop-inc.md)
- [Restaurant Brands International full forensic analysis memo](/analysis/deep-company-pages/restaurant-brands-international-inc.md)
- [Yum! Brands full forensic analysis memo](/analysis/deep-company-pages/yum-brands-inc.md)
- [CAVA full forensic analysis memo](/analysis/deep-company-pages/cava-group-inc.md)
- [Vertiv full forensic analysis memo](/analysis/deep-company-pages/vertiv-holdings-co.md)
- [Intuitive Surgical full forensic analysis memo](/analysis/deep-company-pages/intuitive-surgical-inc.md)
- [Apollo full forensic analysis memo](/analysis/deep-company-pages/apollo-global-management-inc.md)
- [Aon full forensic analysis memo](/analysis/deep-company-pages/aon-plc.md)
- [WESCO full forensic analysis memo](/analysis/deep-company-pages/wesco-international-inc.md)
- [Quanta full forensic analysis memo](/analysis/deep-company-pages/quanta-services-inc.md)
- [CME full forensic analysis memo](/analysis/deep-company-pages/cme-group-inc.md)
- [BlackRock full forensic analysis memo](/analysis/deep-company-pages/blackrock-inc.md)
- [T. Rowe Price full forensic analysis memo](/analysis/deep-company-pages/t-rowe-price-group-inc.md)
- [Marriott full forensic analysis memo](/analysis/deep-company-pages/marriott-international-inc.md)
- [Host Hotels & Resorts full forensic analysis memo](/analysis/deep-company-pages/host-hotels-resorts-inc.md)
- [Baxter full forensic analysis memo](/analysis/deep-company-pages/baxter-international-inc.md)
- [McKesson full forensic analysis memo](/analysis/deep-company-pages/mckesson-corporation.md)
- [Cencora full forensic analysis memo](/analysis/deep-company-pages/cencora-inc.md)
- [Cardinal Health full forensic analysis memo](/analysis/deep-company-pages/cardinal-health-inc.md)
- [KLA full forensic analysis memo](/analysis/deep-company-pages/kla-corporation.md)
- [F5 full forensic analysis memo](/analysis/deep-company-pages/f5-inc.md)
- [Equinix full forensic analysis memo](/analysis/deep-company-pages/equinix-inc.md)
- [Digital Realty full forensic analysis memo](/analysis/deep-company-pages/digital-realty-trust-inc.md)
- [Generac full forensic analysis memo](/analysis/deep-company-pages/generac-holdings-inc.md)
- [Chipotle full forensic analysis memo](/analysis/deep-company-pages/chipotle-mexican-grill.md)
- [McDonald's full forensic analysis memo](/analysis/deep-company-pages/mcdonalds-corporation.md)
- [Fastenal full forensic analysis memo](/analysis/deep-company-pages/fastenal-company.md)
- [Ferguson full forensic analysis memo](/analysis/deep-company-pages/ferguson-enterprises-inc.md)
- [Grainger full forensic analysis memo](/analysis/deep-company-pages/ww-grainger-inc.md)
- [Core & Main full forensic analysis memo](/analysis/deep-company-pages/core-main-inc.md)
- [Stryker full forensic analysis memo](/analysis/deep-company-pages/stryker-corporation.md)
- [Henry Schein full forensic analysis memo](/analysis/deep-company-pages/henry-schein-inc.md)
- [Comfort Systems USA full forensic analysis memo](/analysis/deep-company-pages/comfort-systems-usa-inc.md)
- [EMCOR full forensic analysis memo](/analysis/deep-company-pages/emcor-group-inc.md)
- [Sterling Infrastructure full forensic analysis memo](/analysis/deep-company-pages/sterling-infrastructure-inc.md)
- [MasTec full forensic analysis memo](/analysis/deep-company-pages/mastec-inc.md)
- [ONEOK full forensic analysis memo](/analysis/deep-company-pages/oneok-inc.md)
- [NextEra Energy full forensic analysis memo](/analysis/deep-company-pages/nextera-energy-inc.md)
- [Power demand-to-owner-cash forensic synthesis](/analysis/cross-sector/power-demand-to-owner-cash-forensic-synthesis-2026-09-13.md)
- [Cross-sector economic-control and forensic watchlist](/analysis/cross-sector/cross-sector-economic-control-and-forensic-watchlist-2026-09-13.md)
- [Company findings to cohort explanations](/analysis/cross-sector/company-and-cohort-writing-map-2026-09-14.md)
- [Semiconductor control-points forensic comparison](/analysis/cross-sector/semiconductor-control-points-forensic-comparison-2026-09-14.md)
- [Validation, assurance, and test-control comparison](/analysis/cross-sector/validation-assurance-and-test-control-comparison-2026-09-14.md)
- [Physical content, optical control, and validation economics](/analysis/cross-sector/physical-content-optical-control-comparison-2026-09-14.md)
- [Installed-base machinery versus electrical control comparison](/analysis/cross-sector/installed-base-machinery-versus-electrical-control-forensic-comparison-2026-09-13.md)
- [ASML full forensic analysis memo](/analysis/deep-company-pages/asml-holding-nv.md)
- [Lam Research full forensic analysis memo](/analysis/deep-company-pages/lam-research-corporation.md)
- [Teradyne full forensic analysis memo](/analysis/deep-company-pages/teradyne-inc.md)
- [Keysight full forensic analysis memo](/analysis/deep-company-pages/keysight-technologies-inc.md)
- [Amphenol full forensic analysis memo](/analysis/deep-company-pages/amphenol-corporation.md)
- [Corning full forensic analysis memo](/analysis/deep-company-pages/corning-inc.md)
- [Ciena full forensic analysis memo](/analysis/deep-company-pages/ciena-corporation.md)
- [Eaton full forensic analysis memo](/analysis/deep-company-pages/eaton-corporation.md)
- [Cummins full forensic analysis memo](/analysis/deep-company-pages/cummins-inc.md)
- [Caterpillar full forensic analysis memo](/analysis/deep-company-pages/caterpillar-inc.md)
- [Deep-dossier owner-cash and valuation bridge](/analysis/valuation/deep-dossier-owner-cash-bridge-2026-09-13.md)
- [Deep-dossier scenario inputs (CSV)](/analysis/valuation/deep-dossier-scenario-inputs-2026-09-13.csv)
- [Valuation-aware cross-sector research queue](/analysis/valuation/valuation-aware-cross-sector-research-queue-2026-09-13.md)
- [Deep-dossier scenario-register verifier](/scripts/verify-deep-dossier-scenario-register.py)
- [Combined investment pilot verifier](/scripts/verify-combined-investment-pilots.py)
- [Combined investment research goal](/analysis/company-first-principles/combined-investment-research-meaty-end-to-end-goal.md)
- [Current combined investment research synthesis](/analysis/company-first-principles/combined-investment-research-current-synthesis.md)
- [Combined investment research reviewer’s guide](/analysis/company-first-principles/combined-investment-research-reviewers-guide.md)
- [Combined investment research completion audit](/analysis/company-first-principles/combined-investment-research-completion-audit.md)
- [Next-cycle candidate expansion and admission controls](/analysis/company-first-principles/combined-investment-research-next-cycle-candidate-expansion-2026-09-16.md)
- [Expansion-lane quality-of-earnings overlay](/analysis/company-first-principles/combined-investment-research-expansion-lane-qoe-overlay-2026-09-16.md)
- [Industrial uptime move-on admission](/analysis/company-first-principles/combined-investment-research-industrial-uptime-move-on-admission-2026-09-17.md)
- [Industrial uptime next-cycle decision memo](/analysis/company-first-principles/combined-investment-research-industrial-uptime-next-cycle-decision-memo-2026-09-17.md)
- [Industrial uptime Sterling project cash bridge](/analysis/company-first-principles/combined-investment-research-industrial-uptime-sterling-project-cash-bridge-pass-1-2026-09-17.md)
- [Industrial uptime WESCO/Fastenal owner-cash burden bundle](/analysis/company-first-principles/combined-investment-research-industrial-uptime-wesco-fastenal-owner-cash-burden-bundle-pass-1-2026-09-17.md)
- [Industrial uptime URI fleet lifecycle bridge](/analysis/company-first-principles/combined-investment-research-industrial-uptime-uri-fleet-lifecycle-bridge-pass-1-2026-09-17.md)
- [Industrial uptime source-family handoff](/analysis/company-first-principles/combined-investment-research-industrial-uptime-source-family-handoff-2026-09-17.md)
- [Industrial uptime thesis-breaker register](/analysis/company-first-principles/combined-investment-research-industrial-uptime-thesis-breaker-register-2026-09-17.md)
- [Industrial uptime promotion action register](/analysis/company-first-principles/data/combined-investment-research-industrial-uptime-promotion-action-register-2026-09-17.csv)
- [Integrated pilot 01: Wheaton–Antamina](/analysis/company-first-principles/combined-investment-research-pilot-01-wheaton-antamina.md)
- [Pilot 01 evidence ledger (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-01-wheaton-antamina.csv)
- [Pilot 01 Antamina scenario workbench](/analysis/company-first-principles/combined-investment-research-pilot-01-antamina-scenario-workbench.md)
- [Pilot 01 Antamina scenario data (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-01-antamina-scenario-workbench.csv)
- [Pilot 01 BHP settlement-boundary upgrade](/analysis/company-first-principles/capital-flow-wheaton-antamina-bhp-fy2026-settlement-boundary-upgrade-2026-09-15.md)
- [Pilot 01 after-tax financed allocation frontier](/analysis/company-first-principles/capital-flow-wheaton-antamina-after-tax-financed-allocation-frontier-2026-09-15.md)
- [Pilot 01 reserve-constrained delivery ceiling](/analysis/company-first-principles/capital-flow-wheaton-antamina-reserve-constrained-delivery-ceiling-2026-09-15.md)
- [Integrated pilot 02: Affordability, substitution, and retail value](/analysis/company-first-principles/combined-investment-research-pilot-02-affordability-value.md)
- [Pilot 02 evidence ledger (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-02-affordability-value.csv)
- [Pilot 02 retail valuation workbench (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-02-retail-valuation-workbench.csv)
- [Pilot 02 retail owner-cash bridge](/analysis/company-first-principles/combined-investment-research-pilot-02-retail-owner-cash-bridge.md)
- [Pilot 02 retail owner-cash bridge (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-02-retail-owner-cash-bridge.csv)
- [Pilot 02 TJX H1 FY2027 temporary-support bridge](/analysis/company-first-principles/combined-investment-research-pilot-02-tjx-h1-temporary-support.md)
- [Pilot 02 retail cash-quality support-dependency screen](/analysis/company-first-principles/combined-investment-research-pilot-02-retail-cash-quality-support-dependency-2026-09-15.md)
- [Pilot 02 retail capex-classification boundary](/analysis/company-first-principles/combined-investment-research-pilot-02-retail-capex-classification.md)
- [Pilot 02 retail burden normalization](/analysis/company-first-principles/combined-investment-research-pilot-02-retail-burden-normalization.md)
- [Pilot 02 retail burden normalization (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-02-retail-burden-normalization.csv)
- [Pilot 02 retail normalized-cash screen](/analysis/company-first-principles/combined-investment-research-pilot-02-retail-normalized-cash-screen.md)
- [Pilot 02 retail normalized-cash screen (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-02-retail-normalized-cash-screen.csv)
- [Pilot 02 annual retail cash per diluted share](/analysis/company-first-principles/combined-investment-research-pilot-02-retail-annual-per-share-cash.md)
- [Pilot 02 annual retail cash per diluted share (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-02-retail-annual-per-share-cash.csv)
- [Integrated pilot 03: Apollo–Athene origination to common-owner cash](/analysis/company-first-principles/combined-investment-research-pilot-03-apollo-athene.md)
- [Pilot 03 evidence ledger (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-03-apollo-athene.csv)
- [Pilot 03 Apollo SOTP workbench (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-03-apollo-sotp-workbench.csv)
- [Pilot 03 Apollo common-owner bridge](/analysis/company-first-principles/combined-investment-research-pilot-03-apollo-common-owner-bridge.md)
- [Pilot 03 Apollo common-owner bridge data (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-03-apollo-common-owner-bridge.csv)
- [Pilot 03 Apollo–Athene related-party return bridge](/analysis/company-first-principles/combined-investment-research-pilot-03-apollo-related-party-return-bridge.md)
- [Pilot 03 Apollo–Athene related-party return bridge (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-03-apollo-related-party-return-bridge.csv)
- [Pilot 03 Apollo/Athene fee and asset-transfer upgrade](/analysis/company-first-principles/capital-flow-apollo-athene-related-party-fee-transfer-upgrade-2026-09-15.md)
- [Pilot 03 Apollo/Athene credit-quality return boundary](/analysis/company-first-principles/capital-flow-apollo-athene-credit-quality-return-boundary-2026-09-15.md)
- [Pilot 03 Q2 parent-receipt attribution frontier](/analysis/company-first-principles/capital-flow-apollo-athene-q2-parent-receipt-attribution-frontier-2026-09-15.md)
- [Pilot 03 Apollo–Athene named-asset return routes](/analysis/company-first-principles/combined-investment-research-pilot-03-apollo-named-asset-return-routes.md)
- [Pilot 03 Apollo–Athene named-asset return routes (CSV)](/analysis/company-first-principles/data/combined-investment-research-pilot-03-apollo-named-asset-return-routes.csv)

## Why this exists

Two existing projects already cover adjacent work:

- `ibis-industries/` is the industry-synthesis layer
- `projects/Misc/ui-projects/strategy-under-a-force/` is the theme and company-dossier layer

This workspace fills the missing middle: a disciplined repository of annual reports, 10-Ks, 10-Qs, earnings releases, and call materials organized by sector, industry, and company.

For the current cross-project fit, see:

- [Annual report stack alignment](/analysis/annual-report-stack-alignment-2026-08-09.md)

## Folder layout

```text
annual-report-research/
  raw/
    annualreports/
    company-ir/
    sec/
    earnings-calls/
  extracted/
  analysis/
    sectors/
    industries/
    themes/
  indexes/
  templates/
  notes/
```

## Source policy

Use sources in this order:

1. Company investor-relations pages
2. SEC filings and exhibits
3. Earnings press releases and transcripts
4. AnnualReports.com for annual-report discovery, sector tags, industry tags, and archive convenience

Do not treat AnnualReports.com as the only source of truth for the last three quarters. Use company IR or SEC as the primary evidence for `2026` quarterlies and any required late-`2025` trailing quarter.

Just as important: the work is not only document collection.
The archive is also expected to identify recurring consumer trends, cultural and societal shifts, industrial and operating pressures, capital-allocation behavior, and cross-company patterns that repeat across the lane.
That includes participation systems, franchise or IP monetization, loyalty and habit formation, reimbursement or workflow control, infrastructure bottlenecks, and the broader social or institutional changes that keep showing up across multiple management teams.
The archive should keep distinguishing who is bearing the burden stack and who is capturing the cleaner economics.
If a batch can name the annual report and quarter chain but cannot explain the repeated behavior shift, pressure pattern, and monetization logic across several companies, that batch is still incomplete.

The packet fields should do explicit analytical work:

- annual takeaways + latest three-quarter chain
  - prove: what changed and whether the direction is strengthening, weakening, or persisting
- plain-English operating model
  - prove: what job the company really performs in the system
- strategy read
  - prove: how management is responding to the pressure or opportunity
- growth engine + economic lever
  - prove: what is really carrying the story and what actually moves the economics
- operating constraint
  - prove: where the system is strained
- exact supporting facts
  - prove: the claim directly rather than by implication
- burden-versus-beneficiary interpretation
  - prove: who gets cleaner economics and who absorbs the messy work
- thesis breaker + watchlist
  - prove: the work is falsifiable and ready for continuation

Different claim types also need different proof burdens:

- consumer claim
  - show: what behavior changed and which facts prove it
- cultural or societal claim
  - show: which real-life pressure is creating demand and why it is broader than one company
- industrial or operating claim
  - show: where the strain sits and what happens economically when that pressure changes
- technical or infrastructure claim
  - show: where software is the control layer and where physical bottlenecks still decide outcomes
- capital or balance-sheet claim
  - show: who must carry property, inventory, debt, or financing burden to keep the system working
- cross-company pattern claim
  - show: exact support from at least three companies and what evidence would weaken the broader pattern

## Minimum company packet

Each covered company should end up with:

- sector
- industry
- ticker
- exchange
- fiscal year-end
- latest annual report
- latest 10-K or 20-F
- last three quarterly earnings releases
- last three quarterly 10-Qs or equivalent
- notes on what changed
- a thematic read on the bigger pattern the company helps prove

For most calendar-year reporters, the expected quarterly window is:

- `2026 Q2`
- `2026 Q1`
- `2025 Q4`

For off-calendar fiscal reporters, use the latest three reported fiscal quarters available as of `2026-08-10`, keeping the same principle: prioritize `2026` quarters and pull in late `2025` only when required. Label them precisely.

## Operating rule

Every analysis claim should point back to a dated source in `raw/` or a row in the source ledger.

Shared repo-wide indexes should not be updated continuously during exploration.
Do that at the end of a coherent batch or leave the batch ready for later integration.

## Insight-System Maintenance

For the note-boundary and insight-system audit layer:

- run the full linked audit stack with:
  - `bash scripts/run-insight-audit-stack.sh`
- refresh the committed boundary report and rerun the linked audit stack with:
  - `bash scripts/refresh-note-layer-boundary.sh`
- run only the direct boundary audit with:
  - `bash scripts/audit-note-layer-boundary.sh`
- run only the audit-stack terminology audit with:
  - `bash scripts/audit-audit-stack-terminology.sh`
- run only the maintenance-doc audit with:
  - `bash scripts/audit-maintenance-doc-stack.sh`
- run only the reusable-note maintenance-visibility audit with:
  - `bash scripts/audit-reusable-note-maintenance-visibility.sh`
- run only the historical-note maintenance-isolation audit with:
  - `bash scripts/audit-historical-note-maintenance-isolation.sh`
- run only the continuation-link audit with:
  - `bash scripts/audit-continuation-mode-links.sh`
- run only the remaining-brief link audit with:
  - `bash scripts/audit-remaining-brief-links.sh`
- run only the remaining-stack link audit with:
  - `bash scripts/audit-remaining-stack-links.sh`
- run only the browser review-link audit with:
  - `bash scripts/audit-browser-review-links.sh`
- run only the full insight-system verifier with:
  - `bash scripts/verify-insight-system.sh`

## Cross-Framework Company Pages

Build per-company pages that route the annual-report roster through local
annual-report evidence, the Damodaran method library, Lyn Alden-style
macro/liquidity methods, and other investor/strategy frameworks:

```bash
python3 scripts/build-cross-framework-company-pages.py
python3 scripts/verify-cross-framework-company-pages.py
python3 scripts/verify-deep-dossier-scenario-register.py
python3 scripts/verify-combined-investment-pilots.py
```

Generated artifacts:

- `analysis/deep-company-pages/*.md`
- `analysis/cross-framework-company-method-registry.json`
- `analysis/cross-framework-company-method-report.md`
- `site/cross-framework-companies/index.html`
- `site/cross-framework-companies/companies/*.html`
- `site/cross-framework-companies/data/*.json`

The first finished end-to-end exemplar pair is:

- [McDonald's Corporation](/site/cross-framework-companies/companies/mcdonalds-corporation.html)
- [Chipotle Mexican Grill](/site/cross-framework-companies/companies/chipotle-mexican-grill.html)

Those two pages define the template to scale: company conclusion, investor
conclusion, plain-English memo, framework findings, Damodaran/Lyn routing,
annual and quarterly evidence, business-model mechanisms, what would prove the
conclusion wrong, next filing watchlist, source register, and a peer comparison
bridge.

For the finished exemplars, the real prose source is the markdown memo under
`analysis/deep-company-pages/`. Edit those memos first, then rebuild the HTML.

The generated pages use three status tiers:

- `detailed-first-principles` - a rich `company-analysis.json` exists and is
  folded into the page.
- `packet-backed` - a local `company-packet.md` exists and supplies annual,
  quarterly, and signal takeaways.
- `roster-workbench` - only the roster row is available, so the page is an
  explicit workbench for the next evidence pass.
