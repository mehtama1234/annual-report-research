# Insight Artifact Manifest

Date: 2026-08-11
Repo: `annual-report-research`
Commit when created: `205fcd6f`

Purpose:

This manifest lists the current insight-extraction artifacts, what each one is for, and what it proves about the archive's operating system.

Use this to audit whether a future run has the required guidance, examples, templates, and review pages available before it starts new research.

## Packet Inputs Used

- the current inventory of insight-system notes, guides, templates, proof pages, browser review pages, and queue artifacts
- repo-level knowledge of which artifact types are required for company, lane, proof, and handoff work
- current completeness assessment of what structural guidance exists versus what still needs application to more packets and batches
- cross-references to the existing files that define standards, examples, and review logic

## Required Insight System Layers

| Layer | Required purpose | Current artifact | Status |
|---|---|---|---|
| Operating hub | One starting point that tells future threads where to begin and how to use the system. | [insight-extraction-hub-2026-08-11.md](insight-extraction-hub-2026-08-11.md) | Present |
| Master goal | Defines the end-to-end insight extraction standard. | [master-insight-extraction-goal-2026-08-11.md](master-insight-extraction-goal-2026-08-11.md) | Present |
| Operator-ready master instruction | Gives future threads one concise but complete instruction block they can run from directly. | [end-to-end-insight-master-instruction-2026-08-11.md](end-to-end-insight-master-instruction-2026-08-11.md) | Present |
| Meaty goal | Defines the larger ambition level: packets, lane economics, proof pages, societal shifts, operating pressures, and handoff quality. | [meaty-end-to-end-insight-goal-2026-08-11.md](meaty-end-to-end-insight-goal-2026-08-11.md) | Present |
| Lane runbook | Gives the end-to-end execution sequence from lane definition through proof memos and closeout. | [lane-end-to-end-execution-runbook-2026-08-11.md](lane-end-to-end-execution-runbook-2026-08-11.md) | Present |
| Execution templates | Provides copy-ready templates for packets, profiles, ledgers, lane summaries, proof memos, thesis breakers, and closeouts, including explicit packet-input tracing and reader-test sections. | [insight-extraction-templates-2026-08-11.md](insight-extraction-templates-2026-08-11.md) | Present |
| Completion rubric | Forces future threads to prove that packets, lanes, and proof memos are actually finished rather than merely present. | [insight-completion-rubric-2026-08-11.md](insight-completion-rubric-2026-08-11.md) | Present |
| Company-level guide | Explains how to extract strategy, economics, constraints, and thesis breakers at the company level. | [company-level-strategy-insight-guide-2026-08-10.md](../analysis/cross-sector/company-level-strategy-insight-guide-2026-08-10.md) | Present |
| Industry-level guide | Explains how to read industry lanes internally. | [industry-level-strategy-guide-2026-08-10.md](../analysis/cross-sector/industry-level-strategy-guide-2026-08-10.md) | Present |
| Concrete insights map | Summarizes the cross-sector insights and points to deeper proof pages. | [concrete-insights-and-curiosity-map-2026-08-10.md](../analysis/cross-sector/concrete-insights-and-curiosity-map-2026-08-10.md) | Present |
| Metric glossary | Defines key metrics and next-filing watchlist items. | [metric-glossary-and-watchlist-2026-08-10.md](../analysis/cross-sector/metric-glossary-and-watchlist-2026-08-10.md) | Present |
| Thesis breakers | States what would weaken or disprove major themes. | [thesis-breaker-index-2026-08-10.md](../analysis/cross-sector/thesis-breaker-index-2026-08-10.md) | Present |
| Aha/curiosity layer | Captures surprising questions and weak signals. | [aha-moments-and-curiosity-questions-2026-08-10.md](../analysis/cross-sector/aha-moments-and-curiosity-questions-2026-08-10.md) | Present |
| Insight-driven queue | Prioritizes next lane/company work by insight payoff, target metrics, and thesis breakers. | [insight-driven-next-lane-queue-2026-08-11.md](insight-driven-next-lane-queue-2026-08-11.md) | Present |
| Browser entry | Gives human review access to the stack and explains how concrete insight pages should be read and audited. | [site/index.html](../site/index.html), [site/concrete-insights.html](../site/concrete-insights.html) | Present |

## Reusable Note Layer

The reusable note layer now carries the same evidence-chain standard as the main insight guides.

Machine-readable file list:

- [indexes/reusable-note-layer-files-2026-08-11.txt](../indexes/reusable-note-layer-files-2026-08-11.txt)
- [indexes/historical-note-exclusion-files-2026-08-11.txt](../indexes/historical-note-exclusion-files-2026-08-11.txt)
- [indexes/historical-note-exclusion-categories-2026-08-11.tsv](../indexes/historical-note-exclusion-categories-2026-08-11.tsv)
- [note-layer-boundary-audit-2026-08-11.md](note-layer-boundary-audit-2026-08-11.md)

That reusable layer includes:

- lane and queue control notes
- kickoff briefs
- blind-spot governance notes
- archive-wide audit and mapping notes
- planning and collection-window notes
- selected reusable handoff notes that still function as durable operator guidance

The governing rule is:

- if a note is part of the archive's operating system, it should explicitly include `Packet Inputs Used`
- if a note is part of the archive's operating system, it should explicitly include `Skeptical Reader Test`

The verifier now checks this reusable-note layer directly rather than assuming the standard applies only to the main insight pages.
It now reads the reusable-note list from the machine-readable manifest above, so the enforced note boundary can be updated without editing the verifier's note inventory by hand.
It also verifies that every current top-level `notes/*.md` file belongs to exactly one of the two note manifests, so the note boundary cannot drift silently.
That partition check is delegated to the dedicated note-layer audit script so the boundary logic is maintained in one place.

## Standardization Boundary

The reusable-note standardization pass intentionally stopped before mechanically rewriting every historical handoff and every execution log.

The current cutoff is recorded in:

- [insight-note-standardization-cutoff-2026-08-11.md](insight-note-standardization-cutoff-2026-08-11.md)

That cutoff note explains:

- which note layer was standardized
- why the cutoff was deliberate
- how many remaining unstamped note files still exist
- why most of those remaining files are historical handoffs or logs rather than reusable operator guidance

The machine-readable exclusion list now lives at:

- [indexes/historical-note-exclusion-files-2026-08-11.txt](../indexes/historical-note-exclusion-files-2026-08-11.txt)
- [indexes/historical-note-exclusion-categories-2026-08-11.tsv](../indexes/historical-note-exclusion-categories-2026-08-11.tsv)

## Proof Memo Inventory

| Theme | Artifact | Evidence standard represented |
|---|---|---|
| AI physical capacity | [ai-physical-capacity-proof-2026-08-10.md](../analysis/cross-sector/ai-physical-capacity-proof-2026-08-10.md) | Uses company packet facts to connect AI demand to chips, networking, power, cooling, skilled trades, utilities, and backlog. |
| AI capacity burden carriers | [ai-capacity-burden-carrier-comparison-2026-08-11.md](../analysis/cross-sector/ai-capacity-burden-carrier-comparison-2026-08-11.md) | Applies the insight-driven queue's fourth priority by comparing clean capture versus burden carriers across KLA, Vertiv, Eaton, Quanta, Digital Realty, and Equinix. |
| Hidden operating infrastructure | [hidden-operating-infrastructure-proof-2026-08-10.md](../analysis/cross-sector/hidden-operating-infrastructure-proof-2026-08-10.md) | Uses exact facts from Sysco, Grainger, Ferguson, WESCO, Ecolab, and Veralto to show daily operating infrastructure. |
| Selective consumer | [selective-consumer-proof-2026-08-10.md](../analysis/cross-sector/selective-consumer-proof-2026-08-10.md) | Separates value, beauty, comfort, staples pressure, and upstream packaging pressure with exact examples. |
| Fandom, identity, participation | [fandom-identity-participation-proof-2026-08-10.md](../analysis/cross-sector/fandom-identity-participation-proof-2026-08-10.md) | Uses Disney, Netflix, Roblox, Ulta, e.l.f., Crocs, and Deckers to prove role-based consumer spending. |
| Recreation, lifestyle, and occasion demand | [recreation-lifestyle-occasion-demand-comparison-2026-08-11.md](../analysis/cross-sector/recreation-lifestyle-occasion-demand-comparison-2026-08-11.md) | Applies the insight-driven queue's second priority by comparing travel loyalty, home hosting, premium home identity, jewelry rituals, and foodservice support infrastructure. |
| Paid relationship and habit loops | [paid-relationship-and-habit-loop-comparison-2026-08-11.md](../analysis/cross-sector/paid-relationship-and-habit-loop-comparison-2026-08-11.md) | Extends the consumer and media insight stack by comparing value membership, low-ticket access, direct subscriptions, travel loyalty, and premium network membership. |
| Status, wallet, and default spend | [status-wallet-and-default-spend-comparison-2026-08-11.md](../analysis/cross-sector/status-wallet-and-default-spend-comparison-2026-08-11.md) | Extends the repeat-relationship stack by comparing premium card membership, airline miles, hotel status, and gaming wallets as spend-capture systems. |
| Continuity and maintenance economics | [continuity-and-maintenance-economics-comparison-2026-08-11.md](../analysis/cross-sector/continuity-and-maintenance-economics-comparison-2026-08-11.md) | Compares procurement, sanitation, water and quality monitoring, home care, home-medical resupply, diagnostics, and recurring field service as interruption-reduction businesses. |
| Institutional overhead and control-plane economics | [institutional-overhead-and-control-plane-comparison-2026-08-11.md](../analysis/cross-sector/institutional-overhead-and-control-plane-comparison-2026-08-11.md) | Compares workflow governance, cybersecurity, data control, market structure, and workplace-service readiness as recurring complexity-management businesses. |
| Coordination toll without asset ownership | [coordination-toll-without-asset-ownership-comparison-2026-08-11.md](../analysis/cross-sector/coordination-toll-without-asset-ownership-comparison-2026-08-11.md) | Compares travel routing, premium spend orchestration, insurance placement, and asset-light lodging standards as coordination layers on fragmented systems. |
| Closed-loop ecosystem versus open routing | [closed-loop-ecosystem-versus-open-routing-comparison-2026-08-11.md](../analysis/cross-sector/closed-loop-ecosystem-versus-open-routing-comparison-2026-08-11.md) | Compares branded rewards ecosystems with open travel-routing layers across payments, airlines, lodging, gaming, and booking platforms. |
| Access instead of ownership | [access-instead-of-ownership-comparison-2026-08-11.md](../analysis/cross-sector/access-instead-of-ownership-comparison-2026-08-11.md) | Compares value, wellness, entertainment, travel, and premium-network businesses where the recurring right to enter the system matters more than ownership of each unit. |
| Self-maintenance and confidence spend | [self-maintenance-and-confidence-spend-comparison-2026-08-11.md](../analysis/cross-sector/self-maintenance-and-confidence-spend-comparison-2026-08-11.md) | Compares household, wellness, beauty, comfort, performance, and entertainment businesses that monetize repeat upkeep and everyday readiness. |
| Discovery and decision reduction | [discovery-and-decision-reduction-comparison-2026-08-11.md](../analysis/cross-sector/discovery-and-decision-reduction-comparison-2026-08-11.md) | Compares travel, streaming, beauty, creator-platform, and franchise ecosystems that make money by helping users sort through abundance. |
| Relationship thickening and second-layer monetization | [relationship-thickening-and-second-layer-monetization-comparison-2026-08-11.md](../analysis/cross-sector/relationship-thickening-and-second-layer-monetization-comparison-2026-08-11.md) | Compares companies that start with one customer relationship and then add ads, merchant economics, marketplace, wallet, or partner revenue on top of it. |
| Standardization and simplification as product | [standardization-and-simplification-as-product-comparison-2026-08-11.md](../analysis/cross-sector/standardization-and-simplification-as-product-comparison-2026-08-11.md) | Compares businesses that make money by standardizing workflow, security, procurement, workplace readiness, or home-care continuity. |
| Delegated operations and outsourced complexity | [delegated-operations-and-outsourced-complexity-comparison-2026-08-11.md](../analysis/cross-sector/delegated-operations-and-outsourced-complexity-comparison-2026-08-11.md) | Compares businesses that win by taking over risk, workflow, workplace execution, site operations, testing flow, or home-care continuity that customers no longer want to run alone. |
| Failure avoidance and uptime economics | [failure-avoidance-and-uptime-economics-comparison-2026-08-11.md](../analysis/cross-sector/failure-avoidance-and-uptime-economics-comparison-2026-08-11.md) | Compares businesses that monetize preventing shutdowns, safety gaps, equipment bottlenecks, protection failures, and water or quality breakdowns. |
| Compliance and mandated spend economics | [compliance-and-mandated-spend-economics-comparison-2026-08-11.md](../analysis/cross-sector/compliance-and-mandated-spend-economics-comparison-2026-08-11.md) | Compares businesses that benefit when rules, standards, reimbursement, and certification requirements force recurring spend. |
| Specialist labor and certified capacity | [specialist-labor-and-certified-capacity-comparison-2026-08-11.md](../analysis/cross-sector/specialist-labor-and-certified-capacity-comparison-2026-08-11.md) | Compares businesses that benefit when trained field crews, accredited technical staff, clinicians, pharmacists, and site teams are scarce. |
| Density and local coverage as moat | [density-and-local-coverage-as-moat-comparison-2026-08-11.md](../analysis/cross-sector/density-and-local-coverage-as-moat-comparison-2026-08-11.md) | Compares businesses that become stronger because route coverage, branch reach, access points, and patient-service footprint are already dense. |
| Institutional adaptation and capability outsourcing | [institutional-adaptation-and-capability-outsourcing-comparison-2026-08-11.md](../analysis/cross-sector/institutional-adaptation-and-capability-outsourcing-comparison-2026-08-11.md) | Compares businesses that benefit when hospitals, schools, universities, agencies, and enterprises buy outside capability to modernize and scale. |
| Healthcare outside hospital | [healthcare-outside-hospital-proof-2026-08-10.md](../analysis/cross-sector/healthcare-outside-hospital-proof-2026-08-10.md) | Connects dialysis, infusion, home care, equipment, diagnostics, senior housing, and drug distribution. |
| Aging as operating reality | [aging-as-operating-reality-comparison-2026-08-11.md](../analysis/cross-sector/aging-as-operating-reality-comparison-2026-08-11.md) | Extends the healthcare queue by comparing senior housing, home support, equipment continuity, chronic treatment, diagnostics, and drug flow as one aging system. |
| Fill rate and fixed-capacity absorption | [fill-rate-and-fixed-capacity-absorption-comparison-2026-08-11.md](../analysis/cross-sector/fill-rate-and-fixed-capacity-absorption-comparison-2026-08-11.md) | Compares hotels, senior housing, healthcare property, and hybrid transport through occupancy, same-store NOI, and productive capacity allocation rather than headline sector labels. |
| Backlog visibility versus cash realization | [backlog-visibility-versus-cash-realization-comparison-2026-08-11.md](../analysis/cross-sector/backlog-visibility-versus-cash-realization-comparison-2026-08-11.md) | Compares project, infrastructure, and digital-capacity businesses where orders and backlog create visibility, but cash conversion quality still depends on execution and timing. |
| Relationship thickness inside travel and participation | [relationship-thickness-inside-travel-and-participation-comparison-2026-08-11.md](../analysis/cross-sector/relationship-thickness-inside-travel-and-participation-comparison-2026-08-11.md) | Compares airlines, lodging, gaming, routing platforms, and local-demand apps by how thickly they own repeat behavior around the same broad trip or participation spend. |
| Relationship repair through operating redesign | [relationship-repair-through-operating-redesign-comparison-2026-08-11.md](../analysis/cross-sector/relationship-repair-through-operating-redesign-comparison-2026-08-11.md) | Compares mature routine businesses that have to spend, simplify, or redesign the experience to restore the economics of an existing relationship. |
| Owned intent surfaces and partner rent | [owned-intent-surfaces-and-partner-rent-comparison-2026-08-11.md](../analysis/cross-sector/owned-intent-surfaces-and-partner-rent-comparison-2026-08-11.md) | Compares commerce, media, and interface businesses that monetize the decision surface itself by selling access to first-party intent. |
| Time compression and delegated everyday fulfillment | [time-compression-and-delegated-everyday-fulfillment-comparison-2026-08-11.md](../analysis/cross-sector/time-compression-and-delegated-everyday-fulfillment-comparison-2026-08-11.md) | Compares the companies that monetize faster, lower-friction delegation of everyday local, grocery, retail, and meal fulfillment. |
| Embedded presence inside customer operations | [embedded-presence-inside-customer-operations-comparison-2026-08-11.md](../analysis/cross-sector/embedded-presence-inside-customer-operations-comparison-2026-08-11.md) | Compares companies that become difficult to replace because they move inside the customer workflow, site, or home routine rather than serving only from outside. |
| Beauty discovery and data interface | [beauty-discovery-and-data-interface-comparison-2026-08-11.md](../analysis/cross-sector/beauty-discovery-and-data-interface-comparison-2026-08-11.md) | Compares beauty businesses where discovery, trend speed, loyalty data, and partner monetization matter as much as the underlying product. |
| Healthcare burden versus workflow | [healthcare-burden-vs-workflow-comparison-2026-08-11.md](../analysis/cross-sector/healthcare-burden-vs-workflow-comparison-2026-08-11.md) | Applies the insight-driven queue's first priority by comparing payer, hospital, scientific workflow, diagnostics/devices, and diversified drug/device roles. |
| Healthcare testing, distribution, and delivery control | [healthcare-testing-distribution-delivery-comparison-2026-08-11.md](../analysis/cross-sector/healthcare-testing-distribution-delivery-comparison-2026-08-11.md) | Extends the healthcare queue by comparing diagnostic information, lab workflow, drug flow, installed diagnostics, scientific workflow, and therapy-enabling delivery components. |
| Trust as paid product | [trust-as-paid-product-proof-2026-08-10.md](../analysis/cross-sector/trust-as-paid-product-proof-2026-08-10.md) | Explains ratings, advisory, cybersecurity, diagnostics, hygiene, water, and traceability as paid proof. |
| Trust, proof, measurement, and security | [trust-proof-measurement-security-comparison-2026-08-11.md](../analysis/cross-sector/trust-proof-measurement-security-comparison-2026-08-11.md) | Applies the insight-driven queue's third priority by comparing standards, brokers, clearing, ad verification, cybersecurity, diagnostics, hygiene, water quality, and product-control layers. |
| Relationship owner versus burden carrier | [relationship-owner-vs-burden-carrier-proof-2026-08-10.md](../analysis/cross-sector/relationship-owner-vs-burden-carrier-proof-2026-08-10.md) | Separates customer relationship control from asset, labor, debt, inventory, and regulatory burden. |
| Relationship ownership versus property burden | [relationship-ownership-versus-property-burden-comparison-2026-08-11.md](../analysis/cross-sector/relationship-ownership-versus-property-burden-comparison-2026-08-11.md) | Extends the relationship-versus-burden insight by comparing hotels, senior housing, data centers, and physical retail where the asset can either be burden or moat. |
| Commodity chains | [commodity-chain-proof-2026-08-10.md](../analysis/cross-sector/commodity-chain-proof-2026-08-10.md) | Reads copper, steel, nitrogen, chemicals, lumber, and packaging by chain. |
| Commodity chain comparison | [commodity-chain-comparison-2026-08-11.md](../analysis/cross-sector/commodity-chain-comparison-2026-08-11.md) | Applies the insight-driven queue's fifth priority by comparing copper extraction, aluminum conversion, fertilizer plus agronomy, corrugated throughput, and packaging-interface control. |
| Media attention helper comparison | [media-attention-helper-comparison-2026-08-11.md](../analysis/cross-sector/media-attention-helper-comparison-2026-08-11.md) | Applies the insight-driven queue's sixth priority by comparing direct attention owners, household interfaces, demand routing, verification, measurement, and sell-side ad infrastructure. |
| Media owner versus helper economics | [media-owner-helper-economics-comparison-2026-08-11.md](../analysis/cross-sector/media-owner-helper-economics-comparison-2026-08-11.md) | Extends the media queue by comparing direct habit owners, live-event attention owners, audio transition cases, household interfaces, proof layers, open-internet routing, and commerce-intent monetization. |
| Interface ownership and demand orchestration | [interface-ownership-and-demand-orchestration-comparison-2026-08-11.md](../analysis/cross-sector/interface-ownership-and-demand-orchestration-comparison-2026-08-11.md) | Extends the interface and taxonomy-blind-spot work by comparing booking, trust-based marketplaces, local-commerce coordination, and retail-ecosystem demand routing. |
| Point-of-use control and qualified interface | [point-of-use-control-and-qualified-interface-comparison-2026-08-11.md](../analysis/cross-sector/point-of-use-control-and-qualified-interface-comparison-2026-08-11.md) | Compares businesses that control the exact use event across dispensing, injectable therapy, procedures, monitoring, diagnostics, and payment authorization. |
| Narrow chokepoint and disproportionate consequence | [narrow-chokepoint-and-disproportionate-consequence-comparison-2026-08-11.md](../analysis/cross-sector/narrow-chokepoint-and-disproportionate-consequence-comparison-2026-08-11.md) | Compares businesses that own a small but indispensable layer where failure would create much larger downstream damage. |
| Qualification, validation, and reapproval friction | [qualification-validation-and-reapproval-friction-comparison-2026-08-11.md](../analysis/cross-sector/qualification-validation-and-reapproval-friction-comparison-2026-08-11.md) | Compares businesses that stay embedded because replacing them would force customers to reopen a validated, trained, or trusted operating system. |
| Installed base and pull-through economics | [installed-base-and-pull-through-economics-comparison-2026-08-11.md](../analysis/cross-sector/installed-base-and-pull-through-economics-comparison-2026-08-11.md) | Compares businesses where the initial placement opens the door to recurring accessories, consumables, testing, monitoring, service, or resupply economics. |
| Accepted record and auditable workflow control | [accepted-record-and-auditable-workflow-control-comparison-2026-08-11.md](../analysis/cross-sector/accepted-record-and-auditable-workflow-control-comparison-2026-08-11.md) | Compares businesses that stay central because they hold the accepted record, proof, or auditable state inside a workflow. |
| Frontline visibility and executable workflow | [frontline-visibility-and-executable-workflow-comparison-2026-08-11.md](../analysis/cross-sector/frontline-visibility-and-executable-workflow-comparison-2026-08-11.md) | Compares businesses that make frontline work visible, identifiable, and executable when physical action or live response has to happen correctly. |
| Labor production infrastructure | [labor-production-infrastructure-comparison-2026-08-11.md](../analysis/cross-sector/labor-production-infrastructure-comparison-2026-08-11.md) | Compares education and training businesses that monetize credential throughput, career readiness, and modular skill formation as labor-production systems. |
| Machine-readable operating state | [machine-readable-operating-state-comparison-2026-08-11.md](../analysis/cross-sector/machine-readable-operating-state-comparison-2026-08-11.md) | Compares businesses that convert messy physical or institutional conditions into standardized operating state that larger systems can process and govern. |
| Outsourced judgment and benchmark authority | [outsourced-judgment-and-benchmark-authority-comparison-2026-08-11.md](../analysis/cross-sector/outsourced-judgment-and-benchmark-authority-comparison-2026-08-11.md) | Compares businesses that monetize benchmark authority, risk interpretation, or portfolio implementation when institutions prefer outside judgment over rebuilding it internally. |
| Packaging as demand sensor and product interface | [packaging-as-demand-sensor-and-product-interface-comparison-2026-08-11.md](../analysis/cross-sector/packaging-as-demand-sensor-and-product-interface-comparison-2026-08-11.md) | Compares packaging businesses as upstream demand readouts, throughput systems, and interface-control layers with very different burden profiles by format. |
| Low-friction entrepreneurship infrastructure | [low-friction-entrepreneurship-infrastructure-comparison-2026-08-11.md](../analysis/cross-sector/low-friction-entrepreneurship-infrastructure-comparison-2026-08-11.md) | Compares the infrastructure layers that make small merchants, hosts, and creative sellers viable by bundling identity, trust, payments, discovery, and workflow simplification. |
| Deferred commitment and conversion infrastructure | [deferred-commitment-and-conversion-infrastructure-comparison-2026-08-11.md](../analysis/cross-sector/deferred-commitment-and-conversion-infrastructure-comparison-2026-08-11.md) | Compares businesses that get paid by reducing commitment friction through installment design, promotional financing, or booking-timing flexibility. |
| Intent capture and agentic commerce interface | [intent-capture-and-agentic-commerce-interface-comparison-2026-08-11.md](../analysis/cross-sector/intent-capture-and-agentic-commerce-interface-comparison-2026-08-11.md) | Compares the companies trying to keep commerce discoverable, trusted, and executable when AI assistants and machine-mediated interfaces sit between the customer and the seller. |
| Externally supplied inventory and participation economics | [externally-supplied-inventory-and-participation-economics-comparison-2026-08-11.md](../analysis/cross-sector/externally-supplied-inventory-and-participation-economics-comparison-2026-08-11.md) | Compares businesses whose real inventory, labor, or content is provided by outside participants and coordinated into one usable system by the platform. |
| Governance burden on participant platforms | [governance-burden-on-participant-platforms-comparison-2026-08-11.md](../analysis/cross-sector/governance-burden-on-participant-platforms-comparison-2026-08-11.md) | Compares participant-supply platforms where trust, safety, fraud control, support, and quality governance are part of the economic engine rather than secondary overhead. |
| Replenishment without subscription | [replenishment-without-subscription-comparison-2026-08-11.md](../analysis/cross-sector/replenishment-without-subscription-comparison-2026-08-11.md) | Compares businesses whose recurring relationship is maintained by refill, resupply, reorder, and inventory continuity rather than by a classic subscription contract. |
| Home as managed service endpoint | [home-as-managed-service-endpoint-comparison-2026-08-11.md](../analysis/cross-sector/home-as-managed-service-endpoint-comparison-2026-08-11.md) | Compares companies that turn the home or temporary home into a managed service endpoint for energy reliability, care continuity, pet-care routine, and trip services. |
| Portfolio surgery and burden shedding | [portfolio-surgery-and-burden-shedding-comparison-2026-08-11.md](../analysis/cross-sector/portfolio-surgery-and-burden-shedding-comparison-2026-08-11.md) | Compares companies that improve quality by selling assets, pruning categories, canceling low-return projects, or redesigning capital intensity to isolate cleaner economics. |
| Affordability engineering and value reinvestment | [affordability-engineering-and-value-reinvestment-comparison-2026-08-11.md](../analysis/cross-sector/affordability-engineering-and-value-reinvestment-comparison-2026-08-11.md) | Compares companies that actively rebuild the value equation through incentives, value architecture, reinvestment, and productivity when customers push back on price-led growth. |
| AI readiness and usable context stack | [ai-readiness-and-usable-context-stack-comparison-2026-08-11.md](../analysis/cross-sector/ai-readiness-and-usable-context-stack-comparison-2026-08-11.md) | Compares the enterprise layers that make AI usable through governed data, data modernization, context retrieval, trust governance, and runtime environment rather than raw compute alone. |
| Balance-sheet velocity and timing economics | [balance-sheet-velocity-and-timing-economics-comparison-2026-08-11.md](../analysis/cross-sector/balance-sheet-velocity-and-timing-economics-comparison-2026-08-11.md) | Compares businesses whose real edge comes from carrying inventory, receivables, deposits, or throughput timing so the rest of the system can keep functioning on time. |
| Pre-collected demand and obligation-backed visibility | [pre-collected-demand-and-obligation-backed-visibility-comparison-2026-08-11.md](../analysis/cross-sector/pre-collected-demand-and-obligation-backed-visibility-comparison-2026-08-11.md) | Compares businesses whose recurring quality is strengthened because money or contractual obligation arrives before the full service period is consumed. |
| Formalized price architecture and approved increase systems | [formalized-price-architecture-and-approved-increase-systems-comparison-2026-08-11.md](../analysis/cross-sector/formalized-price-architecture-and-approved-increase-systems-comparison-2026-08-11.md) | Compares businesses whose price or revenue growth is supported by formal mechanisms such as rate cases, recovery structures, lease resets, escalators, or protected fee rights. |
| Policy-distorted operating optics | [policy-distorted-operating-optics-comparison-2026-08-11.md](../analysis/cross-sector/policy-distorted-operating-optics-comparison-2026-08-11.md) | Compares businesses whose reported quarter needs normalization because tariff refunds, policy recoveries, or similar items distorted the headline operating signal. |
| Taxonomy blind spots | [taxonomy-blind-spots-proof-2026-08-10.md](../analysis/cross-sector/taxonomy-blind-spots-proof-2026-08-10.md) | Shows where AnnualReports taxonomy is useful but insufficient for interpretation. |

## Browser Review Paths

Local server root:

`/home/manishmehta/ui-projects/annual-report-research`

Primary review pages:

- `http://localhost:8080/site/index.html`
- `http://localhost:8080/site/concrete-insights.html`
- `http://localhost:8080/site/viewer.html?file=notes/insight-extraction-hub-2026-08-11.md`
- `http://localhost:8080/site/viewer.html?file=notes/master-insight-extraction-goal-2026-08-11.md`
- `http://localhost:8080/site/viewer.html?file=notes/end-to-end-insight-master-instruction-2026-08-11.md`
- `http://localhost:8080/site/viewer.html?file=notes/insight-extraction-templates-2026-08-11.md`
- `http://localhost:8080/site/viewer.html?file=notes/insight-completion-rubric-2026-08-11.md`

## Audit Checks

Run these from the repo root:

```bash
bash scripts/verify-insight-system.sh
bash scripts/audit-note-layer-boundary.sh
bash scripts/audit-note-layer-boundary.sh --write-report notes/note-layer-boundary-audit-2026-08-11.md
```

The verifier checks required files, required phrases, browser-entry links, and the deeper insight-stack sections that future packets, lane summaries, and proof memos are expected to contain. If the local server is not running, the file and link-source checks still prove the repo-side structure.

It also checks that:

- lane summaries name which packet inputs they rely on
- proof memos declare packet inputs used before making the conclusion
- proof memos include a reader test
- browser review pages explain how to read concrete support rather than only listing themes
- reusable operating notes include both `Packet Inputs Used` and `Skeptical Reader Test`
- the note-standardization cutoff remains documented as part of the insight system boundary
- every current top-level note file is covered by exactly one of the reusable or historical manifests

The dedicated note-layer audit script prints the current partition counts and fails if:

- any top-level note file is outside both manifests
- any manifest entry no longer points to a current top-level note file
- the manifest union no longer matches the top-level note inventory
- a historically excluded note drifts into having both standardized sections without being reclassified
- the historical exclusion category map no longer matches the historical exclusion file list or uses an invalid category label
- the committed note-boundary report no longer matches a freshly generated report from the same manifests

Manual equivalent:

```bash
test -s notes/insight-extraction-hub-2026-08-11.md
test -s notes/master-insight-extraction-goal-2026-08-11.md
test -s notes/end-to-end-insight-master-instruction-2026-08-11.md
test -s notes/meaty-end-to-end-insight-goal-2026-08-11.md
test -s notes/lane-end-to-end-execution-runbook-2026-08-11.md
test -s notes/insight-extraction-templates-2026-08-11.md
test -s notes/insight-completion-rubric-2026-08-11.md
test -s notes/insight-artifact-manifest-2026-08-11.md
test -s notes/insight-note-standardization-cutoff-2026-08-11.md
test -s notes/insight-driven-next-lane-queue-2026-08-11.md
test -s notes/note-layer-boundary-audit-2026-08-11.md
test -s indexes/reusable-note-layer-files-2026-08-11.txt
test -s indexes/historical-note-exclusion-files-2026-08-11.txt
test -s indexes/historical-note-exclusion-categories-2026-08-11.tsv
test -s scripts/audit-note-layer-boundary.sh
test -s analysis/cross-sector/company-level-strategy-insight-guide-2026-08-10.md
test -s analysis/cross-sector/industry-level-strategy-guide-2026-08-10.md
test -s analysis/cross-sector/metric-glossary-and-watchlist-2026-08-10.md
test -s analysis/cross-sector/thesis-breaker-index-2026-08-10.md
test -s analysis/cross-sector/aha-moments-and-curiosity-questions-2026-08-10.md
test -s site/index.html
test -s site/concrete-insights.html
```

Check browser links:

```bash
curl -fsS http://localhost:8080/site/index.html | rg 'Insight extraction hub|Master insight extraction goal|Operator-ready master instruction|Insight extraction templates'
curl -fsS http://localhost:8080/site/concrete-insights.html | rg 'Insight extraction hub|Master insight extraction goal|Operator-ready master instruction|Insight extraction templates'
curl -fsS http://localhost:8080/notes/insight-extraction-hub-2026-08-11.md | rg 'Workflow For A New Company|Workflow For A New Lane|Workflow For A New Theme'
rg 'Insight Stack|Insight Stack Across The Lane|Packet Inputs Used For Lane Insight|Packet Inputs Used|Reader Test|Beneficiaries And Burden Carriers|Why This Matters Now' notes/insight-extraction-templates-2026-08-11.md
rg 'consumer behavior shift|relationship-owner versus burden-carrier split|consumer, cultural, societal, industrial, technical, or capital-structure meaning is explicit' notes/lane-end-to-end-execution-runbook-2026-08-11.md
rg 'capital pattern without saying how the filing evidence supports it|who benefits and who carries burden' notes/insight-completion-rubric-2026-08-11.md
curl -fsS http://localhost:8080/site/concrete-insights.html | rg 'How To Read An Insight Here|What Counts As Concrete Support'
```

## Current Completeness Assessment

The insight operating system now has:

- master goal
- operator-ready master instruction
- meaty end-to-end goal
- lane execution runbook
- hub
- templates
- completion rubric
- company-level guide
- industry-level guide
- proof memo examples
- concrete insight map
- metric glossary and watchlist
- thesis breaker index
- aha and curiosity page
- insight-driven next-lane queue
- browser access

Remaining work is not structural setup. Remaining work is applying this standard across more company packets and lane batches.

## Skeptical Reader Test

- Does this manifest make clear which artifact layers actually exist and what each one contributes to the evidence chain?
- Can a skeptical reader tell whether the repo has guidance, templates, examples, review pages, and a next-move queue?
- Does it distinguish structural setup from the remaining application work?
- What missing artifact or weak layer would make this manifest overstate the repo's readiness?

## Next Best Use

For any new company:

1. Open the hub.
2. Use the packet template.
3. Use the company-level strategy guide.
4. Pull exact annual and quarterly facts.
5. Add thesis breakers and watchlist metrics.
6. Tie the company to at least one lane or cross-company theme.

For any new lane:

1. Pick 4-8 flagship names.
2. Complete packets.
3. Build the lane summary.
4. Add comparison table.
5. Extract repeated themes.
6. Add aha moments, watchlist metrics, and thesis breakers.
7. Commit and record the hash.
