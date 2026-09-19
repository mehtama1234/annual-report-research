# Combined investment research completion audit

Research date: `2026-09-18`

This audit tests the 13 requirements in the end-to-end goal. It distinguishes a
requirement that is proven at the current pilot level from one that is merely
qualified or partial. The audit is not allowed to promote the project to done
because the arithmetic verifier passes: the remaining gap and the source path
must be visible for every row.

The structured audit is [the completion-audit CSV](data/combined-investment-research-completion-audit.csv).

The [next-evidence queue](combined-investment-research-next-evidence-queue.md)
is now a controlled handoff: its CSV carries a result class for each open
test across Q-01 through Q-13, and the pilot verifier resolves every declared
queue source artifact.

Q-11 has now received an official Florida PSC source refresh: the public 2026
SPP and SPPCRC filings confirm program identity, rate-class allocation method,
2026 billing-period authority, and the future true-up route. The May 2025
SPPCRC testimony also makes the recovery-return formula explicit—debt/equity
return grossed up for tax on average monthly net investment, including CWIP,
allocated through separation factors—while preserving the searched-negative
boundary for Distribution Inspection-specific receipts and source-of-funds
allocation. This strengthens the route but does not alter the completion grade.
The subsequent local packet recheck also covered the preserved 2025 final-true-up
petition and project-detail exhibits. It found no non-confidential category
billing determinant, invoice/collection schedule, category receivable ledger,
or source-of-funds certificate. That is a searched-negative for those specific
public packet objects, not evidence that customers did not pay or that private
workpapers do not exist.
This distinguishes a searched negative from an unavailable source and from
evidence that exists but is not sufficient for promotion.

The broader named deliverables are checked separately in the [deliverable audit](combined-investment-research-deliverable-audit.md)
and its [CSV](data/combined-investment-research-deliverable-audit.csv), so
existence of the three pilot ledgers cannot stand in for the force atlas,
source layers, reader, or other mature-system outputs.

The source-layer architecture is indexed in the [method and source registry](combined-investment-research-method-registry.md) and its checked [CSV](data/combined-investment-research-method-registry.csv).

## 2026-09-18 checkpoint refresh

The current checkpoint incorporates the latest continuation work without
changing the substantive completion result:

- Q-03 now has a dated two-sided upfront-close control: Wheaton's filed buyer
  payment date is April 1, while BHP's reported seller receipt date is April 2.
  The one-day difference remains unresolved at bank-ledger level, and
  BHP-specific metal-credit delivery, tax, allocation, and financed return
  remain open. Wheaton's Q2 financial statements also now prove the `$1.5B`
  Term Loan was actually drawn on April 1 and remained outstanding at June 30;
  the executed designated-payee and agent-to-seller funds-flow records remain
  missing. See the [payment-date reconciliation refresh](capital-flow-wheaton-antamina-bhp-payment-date-reconciliation-refresh-2026-09-18.md)
  and [credit-agreement waterfall boundary](capital-flow-wheaton-antamina-credit-agreement-waterfall-boundary-2026-09-16.md).
- CA-06 now has a [retail source-acquisition packet](combined-investment-research-retail-ca06-source-acquisition-packet-2026-09-18.md)
  naming the exact supplier-finance, maintenance/growth, lease/tax, service,
  and common-owner fields required for TJX, Target, and Walmart. Target's
  lease-liability and ROIC inputs are preserved as classification controls,
  not H1 cash deductions.
- Eliant's exact CUSIP/entity route is now bounded by a targeted public-search
  result: Apollo-related legal-entity evidence exists, but no public borrower,
  collateral, settlement, trustee, custodian, or remittance record was found.
- MF1 2025-B2 now has a short public-holder continuity screen for the B2 A
  class from September 2025 through January 2026, while the underlying tape,
  servicing reports, Athene custody, and remittance remain gated or unproven.
- Q-13 URI now carries a same-period H1 source/use and burden control from the
  June 30, 2026 10-Q: cash taxes, equipment/intangible purchases, equipment
  sale proceeds, acquisitions, debt payments, repurchases, and dividends are
  visible. The populated borrowing-base certificate, NOLV, reserves, and
  fleet-cohort/source-to-purchase allocation remain unproven.
- Q-08's AP Grange route now has a structured Tranche A cash/accrual
  crosswalk: Athene's `G2964#-AA-7` row is joined to the public
  `G2964#AA7` / `US00187RAA32` / 6.500% / `03/20/2045` instrument tuple, with
  Athene's `$343.374M` investment income separated from `$265.774M` interest
  received. The crosswalk improves identity and accrual discipline, but does
  not prove Athene lot settlement, paying-agent remittance, the `$673M` call
  allocation, borrower cash, or Apollo common-owner cash. See the [AP Grange
  Tranche A cash/accrual crosswalk](data/capital-flow-apollo-athene-ap-grange-tranche-a-cash-accrual-crosswalk-2026-09-18.csv).
- Q-03 now has a structured [financed-return source package](data/capital-flow-wheaton-antamina-q03-next-source-package-2026-09-18.csv)
  that ranks the executed Drawdown Notice, agent/seller funds flow, BHP
  metal-credit ledger, facility/tax allocation, and reserve-backed return
  model. The `$1.5B` draw is observed; the seller-account, BHP-credit,
  asset-level burden, and return joins remain open.
- Q-07 now has a structured [common-owner source package](data/capital-flow-apollo-athene-q07-next-source-package-2026-09-18.csv)
  that ranks the Athene payment confirmation, AGM receiving ledger,
  consolidation elimination, intercompany-note ledger, and parent waterfall.
  The `$0M–$110M` attribution remains sensitivity-only.
- The latest Q2 parent-receipt recheck adds a current liquidity control—`$25.4B`
  consolidated unrestricted cash, `$5.6B` available facility capacity, and no
  outstanding Athene credit-facility borrowings—but still no AGM-only receipt
  or elimination. These amounts remain non-additive to the Athene distribution
  and common-owner denominator.
- Apollo's August 24 8-K identifies an AMAPS overview deck as a possible
  affiliated-asset source, but its linked PDF could not be retrieved through
  the current public route (`403`); no content is counted until a controlled
  copy is available.
- Apollo's public AMAPS product article supplies only format-level mechanics:
  roughly five-year notes, tranche-specific CUSIPs, daily pricing/trading,
  approximately 85% investment-grade notes, and 600-plus obligors. These
  sharpen the AMAPS 1 trade/custody/waterfall request but do not prove its
  executed term, settlement, or Athene receipt.
- The Concord branch now has a current transaction-level recapitalization
  target: Apollo announced `$1.25B` of equity into a BMG subsidiary holding
  legacy Concord ABS, with the stated purpose of enabling repayment of certain
  ABS liabilities. The announcement does not identify the repaid series/class,
  payoff amount, trustee remittance, inclusion of Athene CUSIP `20633K-AN-8`,
  or Apollo/common-owner cash. See the [Concord/BMG recapitalization
  boundary](capital-flow-apollo-athene-concord-bmg-apollo-recapitalization-boundary-2026-09-18.md).
- Q-12 now has a structured [insurance named-asset source package](data/capital-flow-insurance-q12-next-source-package-2026-09-18.csv)
  that ranks Accordia top-40 selection, Apollo/Athene custody/remittance,
  servicing waterfall, liability-cost funding, and source-linked return.
  Statutory interest and consideration remain cash-back proxies.
- Q-12 also has a current Accordia legal-entity cash-flow surface from the
  official Q2 2026 verification statement: `$259.286M` ending cash,
  `$764.721M` of investment proceeds, `$906.633M` of investments acquired,
  `$288.780M` of cash-flow investment income, and `$11.411695B` of liabilities.
  The derived cash-conversion and reinvestment ratios are entity-level
  diagnostics only; the public statement does not provide the selected CUSIP
  rows or settlement/remittance allocation. See the [Accordia Q2 statutory
  cash-flow refresh](capital-flow-kkr-global-atlantic-accordia-q2-2026-statutory-cash-flow-refresh-2026-09-18.md).
- The portal-linked ALIRT exhibit was checked as a possible reinsurance
  extension; it is an unaudited notional FLIC/GA Re/GAAL attribution and does
  not replace the missing statutory liability-cost or remittance source.
- The latest targeted CA-06 public-source refresh confirms Walmart's
  repair-versus-capitalization accounting boundary and Target's mixed 2026
  investment plan, but finds no matched H1 maintenance, lease/tax, service-cost,
  or common-owner allocation. This is a searched-negative refresh, not a
  promotion or a claim that private workpapers do not exist. See the [CA-06
  source-acquisition packet](combined-investment-research-retail-ca06-source-acquisition-packet-2026-09-18.md).
- A further ordinary-language `cash paid` and lease-liability search of the
  Target and Walmart Q2 HTML filings found no supplemental matched-period
  payment schedule. Target's lease-interest ROIC and Walmart's accrued-tax and
  property-payment fields remain classification controls, not H1 cash-tax or
  operating-lease cash. See the [retail interim lease-and-tax search boundary](combined-investment-research-pilot-02-retail-interim-lease-tax-search-boundary-2026-09-16.md).
- PBF's September exchangeable financing remains issued, but the September 24
  2030-note redemption is still pre-event as of this checkpoint. The future
  request route now names the historical 2030-note trustee and paying agent.

These upgrades improve source freshness, routing, and falsifiability. They do
not promote any unresolved proxy into normalized owner cash, unrestricted
Apollo common-owner cash, or a completed asset-level return. The status remains
`12 of 13 proven; CA-06 partial`.

## Current conclusion

The system is not complete. It has a connected, source-routed architecture and
three qualified pilot chains. At the literal requirement level, 12 of the 13
definition-of-done rows are now proven: the remaining partial row is the
correct cash denominator. The burden categories in the reinvestment, financing,
liability, acquisition, and dilution row are visible, but their allocation and
return conclusions remain qualified.
The latest Q-02 profile-to-reserve cross-check, Q-03 funding-mix control, and
retail working-capital double-count control improve denominator discipline but
do not change CA-06's partial status.
The proven rows do not imply that the pilot conclusions are proven; the system
still lacks a fully reconciled cash denominator, BHP-only delivery and
settlement proof, fully normalized retail owner cash, complete Athene-related
party return allocation, unrestricted Apollo common-owner cash, asset-level
statutory return attribution, and through-cycle macro causal validation. The
new Athene statutory cash-flow upgrade and historical macro-regime panel
improves the regime-consistency test but does not eliminate that causal gap.
The latest [Apollo Debt Solutions payment-observability boundary](capital-flow-apollo-athene-apollo-debt-solutions-payment-observability-boundary-2026-09-16.md)
further separates contractual January/July payment mechanics and third-party
CUSIP visibility from an executed Athene remittance. It improves Q-08's
instrument route, but does not change the 12-of-13 result because Athene
settlement, borrower cash, liability-adjusted return, and common-owner
residual remain unproven.
The historical panel also now controls the 2023 real-earnings release revision:
the revised/summary observation used in the dataset is separated from the
initial release, with both source routes checked by the verifier.
The longitudinal retail regime bridge is now also verifier-checked: 18
company-period rows preserve the fiscal-alignment rule, reported
cash-after-property arithmetic, denominator status, and source paths. This
improves reproducibility and falsifiability, but it remains a non-causal
screen rather than through-cycle attribution.
The new [through-cycle causal-test protocol](combined-investment-research-through-cycle-causal-test-protocol-2026-09-16.md)
now makes the Q-10 promotion rule explicit for all three pilots, including
dependent observables, confound controls, required repeated evidence, and
filing-based breakers. This improves reproducibility but leaves causal
promotion unresolved.
The 2026-09-17 current-regime refresh adds the September FOMC target range,
August CPI, and July income/outlays observations to the Q-10 stress-marker
surface. They improve date control for rate, affordability, energy, and
liquidity inputs, but do not change Q-10's descriptive/non-causal status.
The new [capital-flow QoE ratio panel](combined-investment-research-quality-of-earnings-capital-flow-ratio-panel-2026-09-16.md)
also extends the financial-integrity surface beyond retail: eight
denominator-labeled Wheaton and Apollo/Athene ratios are verifier-checked,
while no ratio is promoted to owner cash, parent receipt, or asset-level return.
The QoE overlay now explicitly routes its diagnostic families to the nine
thesis-breaker rows: Wheaton settlement and financed-return tests to
`TB-WPM-01` through `03`, retail working-capital/service/capex tests to
`TB-RET-01` through `03`, and Apollo fee, legal-entity, credit, and ARI tests
to `TB-APO-01` through `03`. This closes a documentation handoff, not an
evidence gap: no breaker activates from a ratio alone, the same-entity and
same-period cash-or-claim join is still required, and the composite
accrual/Beneish-style screen remains not assembled.
The overlay's 2026-09-17 composite-gate audit now records why the pooled score
is not assembled: legal-entity/period, denominator taxonomy, total-assets and
accrual, cash/claims, and accounting-policy joins remain non-comparable across
retail, streaming, and insurance/asset-management perimeters. This strengthens
the QoE method boundary without turning diagnostics into a manipulation finding.
The retail working-capital layer also now compares same-period balance-sheet
and cash-flow signals and prohibits double counting supplier-finance balances
without settlement evidence. This strengthens CA-06 normalization but does not
close its maintenance, lease, tax, service, or owner-cash allocation gates.
The TJX, Target, Walmart, and retail-cohort histories now also carry explicit
method-level forensic promotion gates: Sloan-style diagnostics may be used
directionally, Schilit-style items remain follow-up flags, and Beneish-style
composites remain uncalculated until the accounting and cash-perimeter joins
are comparable. The pilot verifier checks those method-boundary markers so a
future writeup cannot silently promote a diagnostic ratio into a manipulation
score.
The new [retail QoE component screen](combined-investment-research-quality-of-earnings-retail-component-screen-2026-09-16.md)
assembles six same-company annual transitions from those controlled vectors,
including available receivables, revenue, D&A, PP&E, SG&A/OSG&A, claims, and
cash-conversion components. Target's missing receivables field and the cohort's
missing gross-profit and total-assets joins remain explicit, so this is a
reproducible diagnostic screen rather than a promoted Beneish-style composite.
The URI public ABL proxy bridge and Wheaton financing cash-flow upgrade are now
also arithmetic-checked by the pilot verifier. The URI bridge separately
reconciles `$2.887B` of implied facility availability with `$2.920B` of gross
unused stated capacity before constraints, while preserving the populated
borrowing-base-certificate hold. The Wheaton bridge separately verifies the
`$1.972B` H1 net debt movement and `$29.886M` cash interest observation while
preserving the missing Antamina-specific source allocation and repayment
waterfall. These checks improve reproducibility; neither promotes a corporate
proxy into asset-level cash or return evidence.
The [evidence-chain handoff matrix](combined-investment-research-evidence-chain-handoff-matrix-2026-09-16.md)
now records the same proof boundary across force, operating model, QoE, cash,
valuation, macro, capital flow, and thesis-breaker stages for all three pilots.
The latest review-layer refresh adds a [cross-sector comparison](combined-investment-research-cross-sector-comparison-2026-09-16.md)
with supporting-artifact paths and dated public-source refreshes for Apollo
parent receipts, retail capex, and retail attached services. These improve
source freshness and navigation; they do not alter the audit's `12 of 13`
requirement result or close the CA-06 denominator gap. Current retail service
and capex disclosures still lack the allocated cost, maintenance, tax,
collection, and common-owner cash joins required for promotion.
The new [interim lease-and-tax search boundary](combined-investment-research-pilot-02-retail-interim-lease-tax-search-boundary-2026-09-16.md)
also closes the current public-search question for matched H1 cash-paid lease
and tax lines: none was located in the checked TJX, Target, or Walmart interim
HTML. That is a searched-negative control, not evidence that payments did not
occur, and it does not change the `12 of 13` result because annual values cannot
be carried into H1 without period matching.
The Concord public-document recheck adds a dated security-level timely-interest
proxy through the July 2026 payment date, while the underlying transaction
pages remain login-gated. This strengthens Q-08 servicing observability without
proving Athene allocation, trustee remittance, borrower cash, or return.
The new [Target attached-service public-search boundary](combined-investment-research-pilot-02-target-attached-service-public-search-boundary-2026-09-16.md)
makes the Q-06 negative search reproducible: the Q2 2026 10-Q reports the
attached-revenue lines and aggregate cost buckets, but does not allocate
Roundel, card servicing, marketplace, membership, or Shipt costs and cash.
Those gaps
are recorded as `partial`, `qualified`, or explicit remaining upgrades rather
than hidden by the 226-gate verifier. The latest upgrades add two page-level
same-CUSIP statutory bridges for named Athene holdings and dated consideration
rows plus a statutory parent-affiliate balance-sheet/cash-flow boundary; they
also add a Q2 Apollo adjusted-share and preferred/RSU claim boundary plus a
FY2025 parent-company dividend receipt reconciled to subsidiary-distribution
proceeds, and a named Athene/ADIP related-party flow. They do not close
Athene-to-AGM attribution, borrower receipt, liability-cost, or common-owner
cash.
The [Athene corporate-structure presentation boundary](capital-flow-apollo-athene-corporate-structure-presentation-boundary-2026-09-16.md)
adds official June 30, 2026 Athene summary context—more than `$470B` of total
assets, `$37B` of regulatory capital, `$79B` of available liquidity, and
`$6.1B` of deployable capital—and records the May asset presentations as
access-controlled source routes. These observations improve the entity-capital
perimeter but do not alter the `12 of 13` result: AGM receipt, asset-level
settlement, liability-adjusted return, and common-owner residual remain open.

The latest Q-02 source refresh adds the public copy of the February 2025
Antamina NI 43-101 technical report to the Teck reserve cross-check. It gives
an explicit 2025–2036 mine-plan context and a separate Teck/Franco-Nevada
stream precedent with `29.1 Moz` delivered through 2024. This strengthens the
reserve and contractual-context evidence, but the mine-level schedule is not a
BHP-attributable payable-silver curve and the separate stream is not Wheaton
settlement evidence. Q-02 therefore remains `evidence-insufficient`; Q-03
also remains `evidence-insufficient` because the available term-loan, debt
movement, interest, and tax observations are company-level and are not
allocated to Antamina or a lender waterfall.

The Q-08 named-route sensitivity was also refreshed against the current Q2
AMAPS 1 exposure: `$2.544B` applied proportionally to the reconciled `$158.852B`
bond base and H1 `$5.749B` cost-of-funds pool implies approximately `$92.1M` of
mechanical allocated cost. This is a period-fresh denominator diagnostic, not
observed asset-level funding cost, settlement, remittance, or return; Q-08's
statutory-return gap remains open.

The subsequent Q-03 financing refresh adds the direct credit agreement,
funding-composition reconciliation, and term-maturity cliff screen to the
review path. The agreement also expressly requires all facility proceeds to
partially finance the Antamina Mine Silver Stream Acquisition. These make the
legal debt claim, contractual facility-to-use link, announced source mix, and
principal timing explicit; they do not alter the `12 of 13` result because the
PMPA seller-account transfer, exact draw-dollar path, facility-specific
repayment, Antamina allocation, and normalized common-owner cash remain
unproven.

The announced `$1.5B` term loan plus approximately `$0.9B` revolver also
reconcile to an approximately `$2.4B` planned debt-funding envelope, while the
H1 statement reports `$2.7B` of actual corporate bank-debt drawn. The difference
is deliberately left unresolved rather than assigned to Antamina, another
facility, timing, or a gross/net presentation without a facility-level ledger.

The companion Q-03 maturity-bullet coverage screen now displays the `$1.500B`
principal claim against the annualized stream cash proxy under explicit
allocation sensitivities. It is kept separate from recurring interest and from
the CA-06 annualized cash range; it improves terminal-liability visibility but
does not prove an Antamina debt share, repayment source, refinancing, or
common-owner residual.

The Apollo Q2 parent-liquidity refresh also reconciles two reported cash
surfaces: `$3.412B` in the HoldCo & Asset Management summary and `$3.415B` in
the GAAP Asset Management segment table. The `$3M` difference is preserved as
an unreconciled presentation boundary and is not assigned to Athene or common
owners.

The Q-07 financing refresh also date-controls the AHL-to-AGM note balance:
the `$280M` amount is the March 31, 2026 period-end balance, while `$279M` is
the June 30, 2026 balance and `$227M` is the December 31, 2025 comparative.
This removes a potential same-date presentation confusion, but the `$1M`
sequential movement remains only a balance-sheet observation. It does not
prove principal repayment, a dated draw, an AGM receiving-account entry, an
intercompany elimination, or common-owner cash. The completion audit therefore
keeps CA-06 and Q-07's receipt/allocation gates open.

Q-09 legal-source durability is now also improved: the definitive ARI purchase
agreement and transaction-summary exhibits are preserved locally and linked
from the closing-mechanics and transaction-terms controls. This makes the
contractual perimeter independently reproducible while leaving executed
settlement, borrower receipts, and parent allocation unresolved.

## Post-pilot expansion status

The completion audit now also records the controlled move-on work after the
three original pilots. These lanes expand method coverage; they do not replace
the pilot requirements or change the completion result.

| Expansion lane | Current status | What is proven | What remains open |
| --- | --- | --- | --- |
| Power-grid customer cash | `hold-with-strong-route-visible` | FPL category recovery, factors, true-ups, component attribution, aggregate revenue, recovery-return formula, and a historical total-SPPCRC recovery boundary; NextEra named-customer output; Plains tariff and acquisition-capital-stack evidence; AEP/Duke customer-security controls and Duke's conditionally approved, monitored Anderson County project | FPL category billing determinants and collected cash, source-of-funds allocation, project recovery/return; named customer economics for comparison routes |
| Insurance statutory named-asset income | `cash-back-proxy-visible` | Apollo/Athene legal-entity income/proceeds and named issuer routes; Accordia owned-bond book-value and interest-received rows | Lot continuity, settlement/remittance, liability-cost spread, borrower/collateral cash, parent allocation, and final return |
| Asset-backed collateral and borrowing base | `strong-proxy; certificate-hold` | URI ABL terms, eligibility filters, U.S./Canadian formula, certificate cadence, agent controls, dated availability, AR collateral-pool coverage, fleet asset scale, and OCF/capex proxies | Populated borrowing-base certificate, eligible collateral, NOLV, reserves, legal availability, source-to-purchase use, and lifecycle return |
| Expansion-lane QoE overlay | `diagnostic-only` | Twelve field-level diagnostics covering timing, capitalization, legal entity, disposal, collateral, availability, cash conversion, customer security, named-project approval, and source of funds | Comparable multi-period composites and any conclusion beyond a source-specific warning or thesis breaker |

The insurance lane's latest Bear Financing work now adds a dated `$245M`
Accordia-to-Bear Financing credit-agreement and KKR-affiliate perimeter,
FY2024/FY2025 same-CUSIP statutory continuity, and a Q2 2026 source boundary:
the accessible official Q2 verification document reports the aggregate bond
base but omits the detailed Bear Financing Schedule D row, while KKR's parent
Q2 filing provides only aggregate Global Atlantic commitment context. These
upgrades sharpen legal-entity and period controls; they do not prove draw,
disposal, settlement, borrower use, liability-adjusted spread, or owner return,
and the missing Q2 row is not treated as evidence of a sale or repayment.

The [expansion-lane QoE overlay](combined-investment-research-expansion-lane-qoe-overlay-2026-09-16.md)
is deliberately diagnostic. It does not convert a regulatory factor,
statutory interest row, stated facility capacity, or fleet cash ratio into
owner cash or a manipulation finding. The corresponding D-18 through D-98
deliverables and lane verifiers make this boundary reproducible.

## Latest extension artifacts — 2026-09-17

The audit now records the additional workbench layer completed after the
original expansion-lane checkpoint. These artifacts improve comparability,
falsifiability, and routing; they do not promote the open denominator or
receipt gates:

| Extension | New control | Current boundary |
|---|---|---|
| Q-03 Wheaton–Antamina | Metal-credit receipt object and BHP/Glencore allocation boundary | BHP-specific credit issuance, sale/receivable, bank receipt, tax, and financing allocation remain missing |
| Retail CA-06/Q-04–Q-06 | H1 denominator handoff and attached-services legal-owner/burden bridge | Matched maintenance, payment, service-cost, tax, lease, and common-owner allocation remain missing |
| Private credit | Bear Financing, Concord, and Frontline lender-allocation/cash-waterfall workbench | Funded principal, lender allocation, borrower debt service, receipt, repayment, and liability cost remain open |
| URI / asset-backed | Collateral-to-owner-cash workbench | Populated certificate, NOLV, reserves, source-to-purchase allocation, and lifecycle return remain open |
| Physical capacity | URI/Equinix/Digital Realty comparison, valuation/liquidity stress workbench, and six-breaker register | Project, collateral, lease-up, dilution, and common-owner residual objects remain company-specific and unproven |
| Industrial conversion | Structured WESCO/Fastenal H1 conversion table and Sterling project-accounting route | Reported cash conversion is visible; normalized owner cash and project collection remain open |
| Medical devices / clinical workflow | Stryker, Intuitive Surgical, and Henry Schein current-period synthesis with utilization, acquisition, restructuring, lease, securitization, and dilution controls | Company-specific cohort return, lease collection, restructuring cash, collateral availability, and per-share owner cash remain open |
| Semiconductor process control | KLA cycle-normalized cash workbench with factoring, working capital, deferred revenue, R&D, commitments, SBC, debt, and capital-return controls | Multi-year cycle normalization, factoring unwind, service economics, and per-share owner cash remain open |
| Digital infrastructure real estate | Equinix/Digital Realty funding-to-return bridge with project capital, partner funding, debt, equity issuance, commencement, and per-share claims | Named project total capital, stabilized NOI, lease-up, partner economics, and common-owner return remain open |
| Healthcare distribution | McKesson/Cencora/Cardinal denominator pass with working-capital, acquisition, legal, financing, and dilution controls | Longitudinal conversion, acquisition returns, legal cash, entity allocation, and normalized common-owner cash remain open |
| Healthcare access / care delivery | Addus payer/wage/branch bridge and BrightSpring pharmacy/provider cash bridge add distinct labor, drug-cost, service-cost, working-capital, divestiture, debt, and SBC controls | Addus branch return and normalized collection remain open; BrightSpring service-line collection, acquisition return, debt/SBC replacement, and continuing-operations common residual remain open |
| Retail CA-06 allocation boundary | TJX/Target/Walmart current-period OCF/property and burden allocation consolidation | Matched maintenance/growth, supplier-finance settlement, lease/tax cash, attached-service cost/collection, and common-owner allocation remain open |
| Medical-device company bridges | Intuitive installed-base cohort, Stryker–Inari return, and Henry Schein funding bridges | Lease collection, acquired-cohort return, restructuring cash, collateral availability, and diluted per-share owner cash remain open |
| KLA service denominator | FY2022–FY2026 cycle panel plus FY2026 installed-base filing boundary | Numeric systems-in-field, utilization, renewal, service-per-system, factoring unwind, and cycle-normalized owner cash remain open |

The [next-execution handoff](combined-investment-research-next-execution-handoff-2026-09-17.md)
is now the routing control for these extensions. It names the next joinable
source object and the stop rule for each lane. The original completion result
therefore remains `12 of 13 proven; CA-06 partial`, with the new extension
artifacts preserved as qualified, diagnostic, or evidence-insufficient rather
than silently promoted.

### Latest CA-06 filing evidence

The current retailer refresh now supports the partial result with same-period
primary-filing objects rather than only older annual context. TJX discloses
`$1.147B` of H1 operating-lease cash paid while leaving settlement amount,
maintenance capital, and service costs unresolved. Target discloses `$994M`
of tariff refunds, `$4.519B` H1 OCF, `$2.404B` property spending, and `$3.2B`
of eligible supplier-finance obligations that it says are not actual early
payments. Target further states that vendor early payment is optional and that
its remittance date can be up to 120 days from invoice date; this sharpens the
negative boundary but is not a period cash-settlement ledger. Its H1 lease cash
and maintenance/service allocation remain open.
Walmart discloses approximately `$2.9B` of tariff refunds, `$19.710B` OCF,
`$14.181B` capex, and `$5.529B` management-defined FCF, while explicitly
excluding debt service and acquisitions from that FCF definition. Across all
three, the filing evidence improves QoE and denominator control but does not
provide the matched maintenance, lease/service, settlement, and common-owner
allocation required to move CA-06 from `partial`.

The [cross-sector integration matrix](annual-report-cross-sector-integration-matrix-pass-1.md)
is now recorded as D-24. The [industrial uptime first-principles synthesis](annual-report-industrial-uptime-first-principles-synthesis-pass-2-2026-09-17.md)
is now recorded as D-25 and formalizes the move-on sector handoff across
distribution, project execution, and fleet lifecycle cases. It applies the
same QoE, valuation, liquidity, and thesis-breaker controls without creating a
normalized owner-cash ranking. The matrix formalizes the breadth-to-integration handoff
across 12 themes, but its qualified status does not change the requirement
audit: the matrix routes unresolved receipt, allocation, project-return,
liability-cost, and common-owner-cash tests rather than closing them.
The [medical devices and clinical workflow first-principles synthesis](annual-report-medical-devices-clinical-workflow-first-principles-synthesis-pass-2-2026-09-17.md)
is now recorded as D-26. It formalizes the clinical workflow, installed-base,
acquisition, restructuring, QoE, valuation, liquidity, and thesis-breaker
handoff for Stryker, Intuitive, and Henry Schein without creating a normalized
owner-cash ranking.
The [TJX FY2026 owner-cash perimeter upgrade](combined-investment-research-tjx-fy2026-owner-cash-perimeter-upgrade-2026-09-17.md)
is now recorded as D-27. It adds an annual company-specific capex, tax, lease,
and repair-policy boundary while preserving the maintenance-versus-growth and
normalized-owner-cash gaps.
The [Target Q2 2026 cash-quality perimeter upgrade](combined-investment-research-target-q2-2026-cash-quality-perimeter-upgrade-2026-09-17.md)
is now recorded as D-29. It refreshes the current H1 cash, supplier-finance,
tariff-support, lease-liability, debt, dividend, and dilution controls while
preserving the maintenance, service-allocation, payment-timing, and
normalized-owner-cash gaps.
The [Walmart Q2 FY2027 cash-quality perimeter upgrade](combined-investment-research-walmart-q2-fy2027-cash-quality-perimeter-upgrade-2026-09-17.md)
is now recorded as D-28. It adds current H1 cash-flow, supplier-finance,
temporary-refund, tax-benefit, debt, NCI, and diluted-share controls while
preserving the maintenance, service-allocation, and normalized-owner-cash gaps.
The [insurance statutory named-asset first-principles synthesis](annual-report-insurance-statutory-named-asset-first-principles-synthesis-pass-2-2026-09-17.md)
is now recorded as D-30. It formalizes the statutory named-asset route from
policyholder funding through insurer legal entity, asset income/proceeds,
liability cost, remittance, and common-owner residual. It remains qualified,
does not rank insurers or platforms, and does not close the liability-adjusted
return or upstream receipt gates.
The [semiconductor process-control first-principles synthesis](annual-report-semiconductor-process-control-first-principles-synthesis-pass-2-2026-09-17.md)
is now recorded as D-31. It formalizes KLA's process-control and installed-
service route while joining customer concentration, factoring, deferred
revenue, R&D, commitments, debt, SBC, and capital returns to the owner-cash
test. It remains qualified and does not close cycle-normalized maintenance or
diluted common-owner cash.
The [digital infrastructure real-estate first-principles synthesis](annual-report-digital-infrastructure-real-estate-first-principles-synthesis-pass-2-2026-09-17.md)
is now recorded as D-32. It formalizes the Equinix/Digital Realty route from
powered capacity and interconnection through energization, lease commencement,
development capital, partner funding, debt, and diluted per-share residual.
It remains qualified and does not close project-level stabilized return or
common-owner cash.
The [healthcare distribution first-principles synthesis](annual-report-healthcare-distribution-first-principles-synthesis-pass-2-2026-09-17.md)
is now recorded as D-33. It formalizes McKesson, Cencora, and Cardinal's route
from essential-care demand through distribution scale, gross-profit spread,
working-capital settlement, acquisitions, legal claims, financing, and
dilution. It remains qualified and does not close normalized common-owner cash.
The [KLA five-year cash-cycle panel](combined-investment-research-kla-five-year-cash-cycle-panel-2026-09-17.md)
is now recorded as D-34. It joins FY2022–FY2026 SEC company-facts history and
shows the reported cash screen alongside declining OCF margin and rising
receivable/inventory exposure. It improves cycle analysis but does not close
factoring unwind, service economics, maintenance R&D, or diluted owner cash.
The [KLA installed-base denominator boundary](combined-investment-research-kla-installed-base-denominator-boundary-2026-09-17.md)
is now recorded as D-35. The FY2026 10-K names installed systems, utilization,
renewal, system mix, and FX as service drivers but does not quantify the
installed-base denominator. This preserves a searched-negative evidence
boundary rather than treating service growth as normalized owner cash.
The [retail CA-06 allocation boundary](combined-investment-research-retail-ca06-allocation-boundary-2026-09-17.md)
is now recorded as D-36. It consolidates the current TJX, Target, and Walmart
OCF/property screens and confirms that matched maintenance/growth,
supplier-finance, lease/tax, attached-service, and common-owner allocation
objects remain open. It strengthens the partial boundary without promoting a
retail cash ranking.
The [Intuitive installed-base cohort diagnostic](combined-investment-research-intuitive-installed-base-cohort-pass-2-2026-09-17.md)
is now recorded as D-37. It joins system counts, procedures,
instruments/accessories, service, and usage-based lease revenue in one
operating chain. It improves the medical-device denominator but does not close
lease collection, cohort margin, support burden, or diluted owner cash.
The [Stryker–Inari post-close return bridge](combined-investment-research-stryker-inari-acquisition-cohort-pass-2-2026-09-17.md)
is now recorded as D-38. It separates acquisition consideration,
post-close operating cash, integration, quality, regulatory, debt, and
liquidity claims from the still-missing Inari-only return.
The [Henry Schein H1 owner-cash funding bridge](combined-investment-research-henry-schein-owner-cash-funding-bridge-pass-2-2026-09-17.md)
is now recorded as D-39. It joins the thin pre-debt residual to repurchases,
debt, receivable securitization, restructuring, KKR issuance, and dilution
without asserting exact source attribution.
The [digital infrastructure project-return workbench](combined-investment-research-digital-infrastructure-project-return-workbench-2026-09-17.md)
is now recorded as D-40. It separates recurring, development, acquisition,
JV/fund, debt, partner, and equity funding surfaces while preserving the open
named-project capital, commencement, stabilized NOI, and per-share return gates.
The [URI borrowing-base collateral availability proof chase](capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.md)
is now recorded as D-41. It establishes a filed facility-level availability
bridge while preserving the open certificate, eligible-collateral, NOLV,
reserve, source-to-purchase, and lifecycle-return gates.
The [power-grid current-period synthesis](combined-investment-research-power-grid-current-period-synthesis-2026-09-17.md)
is now recorded as D-42. It consolidates NextEra/FPL, AEP, and Duke around
category recovery, named large-load obligations, and a co-owned generation
project while preserving the open billing, collection, paid-capex, financing,
shared-ownership, and common-owner return gates.
The [power-grid valuation and liquidity handoff](combined-investment-research-power-grid-valuation-liquidity-handoff-2026-09-17.md)
is now recorded as D-43. It connects market-implied recovery and rate-base
expectations to rates, construction, fuel/power access, regulatory lag,
affordability, tax-credit support, financing, and dilution without creating a
utility ranking or treating projected recovery as collected owner cash.
The [insurance statutory owner-cash promotion workbench](combined-investment-research-insurance-statutory-owner-cash-promotion-workbench-2026-09-17.md)
is now recorded as D-44. It makes the liability-adjusted return formula
explicit and preserves the open receipt, liability-cost, remittance, capital,
and common-owner allocation gates for Apollo/Athene and Accordia.
The [private-credit borrower promotion workbench](combined-investment-research-private-credit-promotion-workbench-2026-09-17.md)
is now recorded as D-45. It puts Bear Financing, Concord, and Frontline on a
common lender-to-borrower cash-waterfall schema while preserving the open
funded-principal, lender-allocation, debt-service, receipt, repayment,
liability-cost, and owner-residual gates.
The [Apollo–Athene Q2 parent-receipt attribution frontier](capital-flow-apollo-athene-q2-parent-receipt-attribution-frontier-2026-09-15.md)
is now recorded as D-46. It preserves Athene's legal-entity-level `$110M`
H1 distribution observation and quantifies a `$0M–$110M` mechanical AGM
attribution sensitivity, while keeping the dated parent receipt, HoldCo
availability, intercompany elimination, senior claims, and common-owner
residual as explicit open gates.
The [restaurant-franchise first-principles synthesis](annual-report-restaurant-franchise-first-principles-synthesis-pass-1-2026-09-17.md)
is now recorded as D-47. It extends the qualified diagnostic layer to CAVA,
Restaurant Brands International, Wingstop, and Yum, with brand/franchise
control, franchisee burden, advertising-fund perimeter, FY2025 OCF/capex,
QoE controls, and valuation/liquidity gates. The mechanical cash screens are
non-comparable and normalized common-owner cash remains open.
The [restaurant-franchise filing evidence panel](combined-investment-research-restaurant-franchise-filing-evidence-panel-2026-09-17.md)
is now recorded as D-48. It adds structured FY2025 restaurant-count,
advertising, cooperative-advertising, franchisor-cost, and franchise-tag
observations while preserving the advertising-fund, franchisee-health,
maintenance-capex, and common-owner cash boundaries.
The [restaurant-franchise owner-cash promotion workbench](combined-investment-research-restaurant-franchise-owner-cash-promotion-workbench-2026-09-17.md)
is now recorded as D-49. It converts the restaurant lane into a field-level
promotion matrix and preserves the distinction between systemwide sales,
royalty collections, advertising-fund cash, franchisee health, corporate
burden, and diluted common-owner residual.
The [restaurant current-period refresh](combined-investment-research-restaurant-current-period-refresh-2026-09-17.md)
is now recorded as D-50. It adds McDonald's and Chipotle H1 2026 OCF, PP&E,
repurchase, dividend, and unit-count facts with an explicit H1-versus-quarter
period control; the cross-company and owner-cash denominator remains
non-comparable and unpromoted.
The [insurance broker/carrier synthesis](annual-report-insurance-broker-carrier-first-principles-synthesis-pass-1-2026-09-17.md)
is now recorded as D-51. It adds Marsh McLennan, Arthur J. Gallagher, and Chubb
with distinct broker and carrier control points, FY2025 filing denominators,
QoE controls, valuation/liquidity tests, and explicit legal-entity and
non-ranking boundaries.
The [energy-midstream synthesis](annual-report-energy-midstream-first-principles-synthesis-pass-1-2026-09-17.md)
is now recorded as D-52. It adds Cheniere and Energy Transfer with distinct
LNG and network-capacity control points, FY2025 OCF/capex denominators,
QoE/financial-shenanigans controls, valuation/liquidity tests, and explicit
named-project-return and no-ranking boundaries.
The [materials/specialty-chemicals/steel synthesis](annual-report-materials-specialty-chemicals-steel-first-principles-synthesis-pass-1-2026-09-17.md)
is now recorded as D-54. It adds Ecolab, Sherwin-Williams, and Nucor with
distinct specialty-service, coatings-distribution, and steel-cycle control
points, FY2025 filing denominators, QoE controls, valuation/liquidity tests,
and explicit cycle/capex and no-ranking boundaries.
The [exchange/information infrastructure synthesis](annual-report-exchange-information-infrastructure-first-principles-synthesis-pass-1-2026-09-17.md)
is now recorded as D-53. It adds CME and S&P Global with distinct transaction,
clearing, benchmark, ratings, index, and data control points, FY2025 filing
denominators, QoE controls, valuation/liquidity tests, and explicit
collateral/acquisition and no-ranking boundaries.
The [integrated oil-and-gas synthesis](annual-report-integrated-oil-gas-first-principles-synthesis-pass-1-2026-09-17.md)
is now recorded as D-55. It adds ConocoPhillips and Exxon Mobil with distinct
upstream and integrated control points, FY2025 filing denominators,
QoE/financial-shenanigans controls, valuation/liquidity tests, and explicit
cycle, replacement-capex, reserve, and no-ranking boundaries.

## CA-06 denominator decision rule

CA-06 remains `partial` for a substantive reason. The pilots now expose a
source-backed denominator appropriate to each business model, but the evidence
does not justify one final common-owner cash number across all three:

The new [retail owner-cash input schema](capital-flow-retail-owner-cash-input-schema-2026-09-16.md)
is now included in the requirement-level evidence surface. It makes the
remaining retail fields auditable—rather than merely described in prose—while
preserving missing and partial statuses for leases, taxes, maintenance capital,
service costs, supplier-finance settlement, support recurrence, and the final
residual.

| Pilot | Current usable denominator | Why it is not yet promoted |
| --- | --- | --- |
| Wheaton–Antamina | Stream revenue, cost, depletion, and an OCF proxy plus financed/after-tax sensitivities | BHP-only delivered credits, receipt cash, Antamina tax, and debt-service allocation are missing |
| Retail cohort | Operating cash less total property spending plus explicit support, working-capital, SBC, and capex frontiers | Maintenance capital, leases, taxes, service costs, seasonality, and support recurrence are not fully allocated |
| Apollo–Athene | FRE/SRE/PII, statutory investment income, legal-entity operating cash, and explicit ANI-to-use sensitivities | Regulated/policyholder claims, asset-level liability cost, Athene-to-AGM receipt, NCI/preferred claims, and common-owner residual are not joined |

The new [CA-06 quantified allocation surface](combined-investment-research-ca06-quantified-allocation-surface-2026-09-16.md)
consolidates the existing source-backed ranges without adding them together:
Wheaton's after-tax financed allocation frontier, retail support-removal
screens, and Apollo's `$0M–$110M` parent-attribution frontier. These ranges
make uncertainty quantitative but do not close the missing settlement or
common-owner allocation records.

The Teck reserve cross-check now adds a separate mine-level burden reference
to CA-06: its 22.5% share of 2026 Antamina projected capital costs is
`$215M–$270M`, including sustaining, growth, and capitalized stripping, with
projected cash operating costs of `$255M–$310M`. The source explicitly excludes
transportation and royalties, and the figures are not allocated to BHP,
Wheaton, taxes, debt service, or silver delivery. This improves burden
visibility without changing the normalized-owner-cash grade.
The same cross-check records Teck's `$225M` proportionate Antamina borrowing
and the filing's non-recourse statement. This is a project-finance boundary,
not evidence that BHP/Wheaton or common owners bear that debt.
For Q-02 denominator control, the cross-check also records a non-promotable
Teck-to-BHP ownership scaling sensitivity (`47.145M` ounces, or `42.4305M`
after a mechanical 90% factor). Because the Teck recoverable and BHP
contained-P&P definitions are not joined, it remains outside the delivery and
valuation models.

The promotion rule is therefore: a valuation may show a reported denominator or
a source-bounded sensitivity, but it may call the result normalized owner cash
only after every applicable burden and legal-entity claim is either observed or
explicitly carried into the range. This prevents a consolidated OCF, stream
cash proxy, or segment earnings measure from being silently promoted to common
owner cash. The next CA-06 upgrade is not another company name; it is a dated
allocation or settlement record that closes one of the rows above.

The new [CA-06 owner-cash promotion matrix](combined-investment-research-ca06-promotion-matrix-2026-09-16.md)
joins those controls across all three pilots. It confirms that each pilot has
an observable or bounded base denominator but that the final owner-cash field
is still missing and the promotion status remains `allocation-sensitivity-only`.
The matrix now also states the minimum promotion bundle for each pilot: legal
entity, period, denominator, cash-or-claim object, and reconciliation path. Its
QoE and financial-shenanigans gate ties accrual, timing, capitalization,
related-party, settlement, and liability diagnostics to those joins; it treats
them as reconciliation prompts rather than a fraud score. This closes the
control architecture of the partial requirement without changing its
substantive status.

The new [annual retail cohort denominator control](combined-investment-research-pilot-02-retail-annual-cohort-denominator-control-2026-09-17.md)
adds a fiscal-year-aligned TJX/Target/Walmart comparison on reported
cash-after-property per diluted share, with lease cash, tax cash, and
supplier-finance movement carried as separate context. It improves CA-06's
comparability and prevents double counting, but does not close maintenance
capital, attached-service, seasonal, or common-owner claim allocations.
The companion [annual attached-services frontier](combined-investment-research-pilot-02-retail-annual-attached-services-cash-frontier-2026-09-17.md)
aligns Target's `$2.063B` FY2025 and Walmart's `$6.750B` FY2026 reported
service-income pools with the annual screen through a hypothetical 0–100%
conversion range. It remains evidence-insufficient because service collection
and allocated burden are not observed.

The [valuation and expectation promotion matrix](combined-investment-research-valuation-promotion-matrix-2026-09-16.md)
now ties the price-implied cash, separated-earnings, and transaction-return
screens to the same evidence grades. It keeps every valuation case at
`qualified-expectation-screen` until the linked owner-cash, receipt, return,
and claim joins are source-backed.

The [September 17 market snapshot](combined-investment-research-market-snapshot-2026-09-17.md)
refreshes the live market inputs and recalculates the retail price-implied cash
burden. This improves date control for the Damodaran expectation layer but does
not change the valuation status: the required cash remains an expectation
screen, while CA-06 owner-cash and the associated burden allocations remain
partial.
The [annual reported-cash expectation screen](combined-investment-research-pilot-02-retail-annual-reported-cash-expectation-screen-2026-09-17.md)
extends that date-controlled burden test to TJX, Target, and Walmart using
their latest fiscal-year reported cash-after-property denominators. Its
`27.906x`, `24.913x`, and `57.471x` ratios remain qualified reported-cash
screens, not normalized owner-cash multiples.

The latest Q-12/Q-13 refreshes sharpen the expansion evidence without changing
the 12-of-13 result. For MF1, CUSIP `592918-AA-4` now has a bounded statutory
holding/disposal-to-servicing join, a `$209.559M` selected cash-like
consideration row, a diagnostic `$210.862M` proceeds-plus-income screen, and a
dated CTSLink inventory of restricted distribution, bond, collateral, loan,
and servicer reports. The live CTSLink route is separately labeled MF1
`2026-FL21`, so its reporting schedule is not substituted for the MF1 2025-B2
statutory candidate without an offering/CUSIP/legal-owner crosswalk. These
observations remain below receipt, custody,
liability-cost, and owner-cash proof. For URI, the Q2 2026 10-Q now gives the
facility split directly—`$2.802B` ABL capacity net of letters of credit plus
`$85M` AR capacity—while eligible collateral, NOLV, reserves, certificate
components, source-to-purchase use, and lifecycle return remain open. CA-06
therefore remains `partial`, and the expansion lanes remain qualified rather
than promoted.

The latest retail upgrade also adds a current Target Q2/H1 attached-service
burden boundary: aggregate merchandise, fulfillment, SG&A, D&A, and temporary
tariff-refund effects are visible, while service-level allocation remains open.
The companion attached-services cash frontier now makes that open allocation
explicit: Target's `$1.141B` H1 attached-service pool and Walmart's `$3.855B`
segment subtotal are shown at 0%, 25%, 50%, 75%, and 100% conversion, while
Walmart's consolidated filing reports `$3.904B`; the `$49M` difference is now
quantified in the [attached-income denominator reconciliation](combined-investment-research-pilot-02-walmart-attached-income-denominator-reconciliation-2026-09-16.md).
Every frontier row remains labeled sensitivity-only and excluded from
normalized owner cash. This is the correct Q-06 decision surface: a future
promotion requires service-level collection plus allocated labor, fulfillment,
technology, overhead, working capital, capex, tax, and legal-entity cash—not
merely a higher reported revenue or operating-income figure.
The retail denominator layer now also contains a cross-cohort inventory/payable
balance screen for TJX, Target, and Walmart, cross-checked against each filing's
cash-flow inventory and accounts-payable rows. This improves working-capital
reconciliation without promoting the balance or cash-flow signals to recurring
owner cash.
The latest TJX Q2 capex table further sharpens CA-06's retail denominator:
H1 capex is `$1.159B` by segment and H1 operating cash flow is `$3.345B`,
producing a mechanical `$2.186B` cash-after-property screen. Because the
filing still does not split those segment amounts between replacement and
growth, the screen remains sensitivity-only and does not change CA-06's
partial status. The structured [TJX Q2 cash/capex boundary](combined-investment-research-tjx-q2-cash-capex-boundary-2026-09-18.md)
also preserves the identified tariff-refund/interchange cash drivers and the
planned `$1B` note repayment as separate quality and forward-claim controls;
neither is promoted to recurring owner cash.
The new retail margin-support transition screen also separates reported H1
gross-margin movement from disclosed tariff-refund support across TJX, Target,
and Walmart. It improves the burden test but remains a partial sensitivity because
mix, pricing, fulfillment, inventory, and recurring support are not fully
allocated.
The same lane now also records Walmart's current advertising and membership
growth signals from the Q2 earnings release and management call. The new
[Walmart call control-point memo](combined-investment-research-pilot-02-walmart-q2-management-call-control-point-upgrade-2026-09-15.md)
preserves the mechanism claims and their evidence grades: management
commentary strengthens the control-point thesis, but does not disclose
service-level cash conversion or owner cash.
Target's official Q2 2026 downloadable transcript is now also preserved as a
structured call-control-point memo: traffic, digital delivery, attached-service
growth, tariff-refund dependence, and reinvestment claims are separately graded
and routed back to the 10-Q cash and burden tests. This closes the latest-call
route gap without treating management commentary as cash proof.

The Apollo–Athene lane also now has a Q2 ARI seller-cash/debt-waterfall
boundary: aggregate sale/repayment proceeds, identified senior debt uses, and
post-sale seller cash are visible, and the full seller cash-flow statement
reconciles beginning cash to ending cash. The buyer payment ledger and borrower
collections remain open.

The [ARI liquidation-distribution boundary](capital-flow-apollo-athene-ari-liquidation-distribution-boundary-2026-09-16.md)
adds a forward-looking seller/common-owner residual estimate of `$7.75–$8.50`
per fully diluted share, excluding the separate `$3.75` dividend. The proxy
also states the expense, capital-spending, tax, reserve, and timing deductions;
the estimate is not an observed receipt and does not close the buyer-side or
Apollo-parent cash loop.

The buyer-side perimeter is now separately recorded in the [ARI acquisition
boundary](capital-flow-apollo-athene-ari-buyer-side-acquisition-boundary-2026-09-16.md):
Athene reports the April 24 completion and approximately `$8.7B` purchase, and
its commercial-mortgage balance rises by `$9.220B` from year-end. This strengthens
the buyer-side transaction boundary without promoting the aggregate balance to
loan-level collections, collateral cash, or realized return.
Athene's Q2 earnings release adds a separate management-reporting observation:
`$7.8B` of 2Q'26 and LTM AUM outflows are identified as ARI-related after the
sale, while `$5.0B` of Intel prepayment outflows are separately identified. The
[AUM outflow boundary](capital-flow-apollo-athene-ari-aum-outflow-boundary-2026-09-16.md)
improves the buyer-side perimeter, but AUM outflow is not settlement cash,
borrower repayment, or asset-level return.
The new [closing-payment mechanics boundary](capital-flow-apollo-athene-ari-closing-payment-mechanics-boundary-2026-09-16.md)
now identifies the contractual Closing Date Calculation Notice, seller-directed
payoff wires, signed settlement statement, final accounting and true-up,
designated-buyer route, and borrower payment-direction notices. These are the
decisive evidence objects for Q-09, but executed settlement, bank movement,
borrower receipts, and buyer return remain open.
The bounded [post-close proof search](capital-flow-apollo-athene-ari-post-close-proof-search-boundary-2026-09-16.md)
classifies those objects as `searched-negative` in the checked public filing
perimeter; it does not convert missing public disclosure into a conclusion that
the private records do not exist.
The [cash-perimeter delta boundary](capital-flow-apollo-athene-ari-cash-perimeter-delta-boundary-2026-09-16.md)
now separately compares the approximately `$8.6B` seller consideration with
the `$9.497267B` aggregate commercial-mortgage repayment/sale-proceeds line,
leaving the `$897.267M` difference explicitly unallocated. This improves the
numeric Q-09 boundary without promoting the difference to any cash source or
return.
The same buyer filing also reports a `$48.372B` commercial-mortgage portfolio
and a `$1.027B` 90-days-past-due/non-accrual subset marked at `$695M` fair value;
these are now a separate buyer-credit boundary and remain unallocated to ARI.

The Apollo–Athene statutory route now also includes the [SVF II Finco public
search refresh](capital-flow-apollo-athene-svf-ii-finco-public-search-refresh-2026-09-16.md)
and its [row-composition boundary](capital-flow-apollo-athene-svf-ii-finco-row-composition-boundary-2026-09-16.md).
Athene's `$2.186B` concentration cross-checks the three same-issuer year-end
Schedule D rows, while the AC-4 `$2.090B` headline is split into `$50.751M`
selected cash-like paydowns and approximately `$2.039B` tax-free-exchange /
transfer holds. This improves Q-08 denominator and parser control, but leaves
settlement, borrower cash, liability cost, and realized return unresolved.

The Wheaton–Antamina lane also now has a BHP FY2026 legal-counterparty
boundary: the stream is with a BHP wholly owned subsidiary and Antamina is not
a party. A further Q2 2026 [first-delivery receipt boundary](capital-flow-wheaton-antamina-q2-first-delivery-receipt-boundary-2026-09-15.md)
confirms that Wheaton received the first BHP-PMPA deliveries during Q2, while
preserving the combined-stream quantity and missing BHP-only metal-credit
settlement ledger.

The BHP FY2026 operational review also supplies a five-quarter and FY2026
BHP-interest payable-silver production/sales series. It improves the annual
delivery-curve proxy and prevents automatic double-counting of the 33.75%
share, but it remains separate from the metal-credit invoice and receipt
ledger.

The BHP lane now also has a clearly labeled `16.67–18.52` year mechanical
threshold-timing sensitivity. It is an expectation screen only, not a
reserve-backed life-of-mine delivery forecast.

The September Wheaton presentation adds a dual-PMPA contract reconciliation:
the new BHP agreement uses a `100M`-ounce initial threshold, while the legacy
Glencore agreement uses a `140M`-ounce threshold. This resolves an important
denominator ambiguity in the combined Antamina rows, but it does not supply
agreement-level delivery, invoice, or receipt allocation.

The local Wheaton/BHP packet was then searched for invoice, settlement,
metal-credit, receipt, delivered, and PMPA terms. It confirms the contract
mechanism, aggregate `$41M` streaming-liability settlements, and combined or
counterparty operating rows, but does not expose a BHP-PMPA-only invoice,
settlement statement, payment date, or receipt account. The aggregate amount
therefore remains a boundary, not BHP-only owner cash.

The Q-01 perimeter was subsequently widened to include the official BHP
February streaming announcement and Wheaton's closing, Q1, and Q2 SEC exhibits.
Those routes repeat the contract, first-delivery timing, and metal-credit
mechanism but still do not disclose a BHP-only quantity, invoice, settlement
date, or receipt account. The result is therefore a stronger `searched-negative`
classification for the available public perimeter, not a claim that no
settlement occurred.

The Apollo–Athene lane now also has a decomposed H1 investment-earnings bridge
with fixed-income income, alternative income, strategic-capital fees, cost of
funds, net investment spread, and an alternative-return sensitivity. It remains
a segment-level bridge rather than asset-level return or parent cash proof.

The Apollo–Athene lane now also has a named-route concentration screen for ten
same-CUSIP cash-like rows: `$2.378B` of selected non-Treasury operating or
wrapper routes versus `$551.867M` of Treasury or sovereign-liquidity rows.
This improves the order of the next statutory investigation and excludes the
Treasury rows from borrower-return claims; it does not prove source of funds,
borrower receipt, liability-cost spread, or parent cash.

The Apollo–Athene lane now also has full-range Schedule D population evidence:
`8,648` normalized rows across issuer-credit and asset-backed-security
sections. The latest coupon-decimal/NAIC-marker correction now reconciles both
located sections within one dollar, and the [aggregate-total reconciliation](capital-flow-apollo-athene-statutory-schedule-d-total-reconciliation-2026-09-16.md)
records the combined two-dollar variance against the separately stored total
reference. This proves the section-level statutory portfolio denominator and
materially advances legal-entity prioritization; it
still does not prove row-level counterparty cash, liability-cost spread,
borrower cash, or common-owner cash. The Schedule D parser audit also confirms
that residual missing book fields include legitimate blank statutory columns;
positional imputation remains disallowed. The corrected AMAPS and Concord
same-CUSIP rows also survive the full-range correction, but remain below
settled-receipt and row-level return proof. The dated lot-chronology check also
shows that same-CUSIP equality is not enough: Concord's holding acquisition
post-dates its disposal/proceeds date. A proportional named-route liability-cost
sensitivity now quantifies burden scale, but is explicitly not a period-matched
asset-level funding allocation.

The Apollo–Athene lane now also has a Q2 policyholder-liquidity and secured-
funding boundary: the filing discloses the share of net reserve liabilities
that are generally non-surrenderable or subject to surrender penalties, plus
current and prior-period repurchase-agreement payables and collateral. This
adds a company-specific liquidity transmission test, but it does not prove
stress-period surrender behavior, haircut headroom, realized sale losses,
regulated surplus, parent receipt, or common-owner cash.

The Apollo HoldCo route now also carries a parent-summary balance-sheet
context from the Q2 earnings supplement: `$3.412B` cash, `$3.467B` net
investments, `$1.511B` accrued performance-fee receivables, `$(95M)` net
clawback payable, `$(5.762B)` debt, and `$2.533B` net balance-sheet value.
These values improve parent-denominator context but remain balance-sheet
observations, not unrestricted cash, Athene-specific receipt evidence, or
common-owner cash.

The Concord public-observability route now has independent portfolio evidence
for 2024-1A, 2025-1A, and 2025-2A, including an SEC-hosted 2025-2A schedule.
The targeted search did not surface a 2025-3A observation under the checked
issue-name and CUSIP variants. This is a bounded public-source negative and
instrument cross-check; it does not prove Athene ownership, a settled lot,
trustee remittance, borrower receipt, or parent cash.

The Broadcom route now has a separate fee-timing boundary: Apollo's Q2
earnings transcript says the financing is expected to draw over multiple
quarters and the associated capital-solutions fee is recognized as drawn, with
the larger share expected in Q4 2026 and Q1–Q3 2027. That improves timing
specificity, but remains an expected management schedule rather than proof of
fee collection, cash settlement, realized margin, or common-owner cash.

## Audit rule

For each requirement, the authoritative artifact must exist, the status must
match the evidence strength, and the remaining upgrade must name the next test.
The audit can move a row upward only after a primary source and the relevant
denominator or legal-entity bridge are joined.
The upstream cash layer now also has a dated Athene legal-dividend path: `$750M`
annual intended regular common dividends, `$187M` declared for Q2 with a June
15 payment date, and `$375M` paid in H1. Board discretion and statutory,
solvency, and regulatory constraints remain explicit; Apollo receiving-account
and unrestricted common-owner cash are still not joined.

The Apollo Q2 financial supplement was subsequently searched across all eight
worksheets for dividend, cash, subsidiary, distribution, intercompany, and
parent terms. It adds no separately tagged Athene-to-AGM receipt or
subsidiary-distribution line. This narrows the public-source route but does not
prove that no transfer occurred; the dated bank/intercompany receipt remains
the required Q-07 upgrade.

Validation snapshot: on `2026-09-16`, `bash scripts/verify-insight-system.sh`
returned `insight-system-ok`; the focused pilot, deliverable, reader-route,
internal-link, and whitespace checks also passed. These results verify the
research system's structure and source navigation, not the unresolved
delivery-level, normalized-owner-cash, asset-return, or common-owner-cash
claims.

The [retail common-period normalization surface](combined-investment-research-pilot-02-retail-common-period-normalization-surface-2026-09-15.md)
now explicitly reconciles the two TJX low-screen bundles: `$1.631B` after the
payable-support signal and SBC, versus `$1.351B` after the separate
tariff/interchange candidate and SBC. Because those adjustment layers can
overlap, the audit treats them as non-additive sensitivities and does not
promote either to normalized owner cash.

The [current AMAPS 1 exposure boundary](capital-flow-apollo-athene-q2-amaps-current-exposure-boundary-2026-09-16.md)
adds a current-period concentration denominator—`0.810%` of Athene net
invested assets and `5.782%` of the look-through related-party population—while
preserving the distinction between exposure scale and asset-level return. The
Q-08 statutory-return gap therefore remains open for settled lots, collateral
cash, trustee remittance, liability-cost allocation, and realized return.

The [AOP Finance Partners public-source refresh](capital-flow-apollo-athene-aop-finance-public-source-refresh-2026-09-16.md)
adds a primary-source legal-entity bridge: Athene's 2021 Form 10-K identifies
AOP as a consolidated VIE and attributes its economic benefits and losses to
Athene after related-party management and carry. The 2025 statutory AOP rows
remain disposal-only cash-like candidates totaling approximately `$684.9M` of
consideration. This improves the named-vehicle route but does not prove lot
continuity, settlement receipt, borrower cash, liability-adjusted return, or
common-owner cash; those completion rows remain unresolved.

The [AP Hansel public-source refresh](capital-flow-apollo-athene-ap-hansel-public-source-refresh-2026-09-16.md)
adds primary Aldar evidence for an Apollo-controlled destination, land-rights
asset, distributions, and a February 2025 exit transaction overlapping the
Athene disposal window. This is a material partial upgrade, but exact CUSIP
settlement, Athene allocation, liability-adjusted return, and common-owner
cash remain unresolved.

The [AA MMF 1 public-source refresh](capital-flow-apollo-athene-aa-mmf1-public-source-refresh-2026-09-16.md)
adds Athene regulatory and Apollo filing evidence for an Apollo-related
AA MMF 1 Holdco wrapper chain around the approximately `$222.8M` statutory
candidate. Exact Ltd-to-Holdco identity, Athene settlement, borrower cash,
liability-adjusted return, and common-owner cash remain unresolved.

The [ATLAS Funding 1 public-source refresh](capital-flow-apollo-athene-atlas-funding-public-source-refresh-2026-09-16.md)
adds an Apollo-backed structured-credit platform route for two disposal-only
redemption candidates totaling approximately `$487.3M`. Apollo's primary
disclosures establish the ATLAS platform perimeter, but not exact Athene
issuer ownership, settled redemption cash, collateral proceeds, trustee
remittance, liability-adjusted return, or common-owner cash; those completion
rows remain unresolved.

The [Apollo Debt Solutions public-source refresh](capital-flow-apollo-athene-apollo-debt-solutions-public-source-refresh-2026-09-16.md)
adds an SEC-confirmed exact CUSIP, issuer, coupon, maturity, principal amount,
and trustee for the Athene disposal candidate. Exact Athene counterparty and
settlement, BDC/borrower cash, liability-adjusted return, and common-owner cash
remain unresolved.

The [FASST 2022-S5 public-source refresh](capital-flow-apollo-athene-fasst-2022-s5-public-source-refresh-2026-09-16.md)
adds public rating and trustee-route evidence for the approximately `$219.1M`
statutory candidate. Exact Athene settlement, loan-level cash, trustee
remittance, liability-adjusted return, and common-owner cash remain unresolved.

The [VMC Finance public-source refresh](capital-flow-apollo-athene-vmc-finance-public-source-refresh-2026-09-16.md)
adds a bounded Varde-linked commercial-mortgage and securitization-lineage
route for the approximately `$295.3M` `91836A-AA-4` candidate. This improves
the issuer/collateral map but does not prove Athene lot settlement, borrower or
property cash, trustee remittance, liability-adjusted return, or common-owner
cash; those completion rows remain unresolved.

The Walmart denominator refresh adds the matching lease and tax burden
observations: `$16.512B` of operating-lease obligations and a `$3.141B` H1 tax
provision on `$15.160B` of pretax income. The filing does not separately identify
H1 lease payments or cash taxes paid, so these remain burden-visibility fields
rather than owner-cash deductions.
The companion annual lease-and-tax control proves annual cash-paid burden
observations for all three retailers—TJX `$2.214B` lease cash and `$1.471B`
tax cash, Target `$529M` and `$1.091B`, and Walmart `$2.315B` and `$5.364B`—but
keeps them as denominator-calibration context. They are not subtracted again
from operating cash flow, and they cannot be carried into the current H1 owner-
cash comparison without period matching; maintenance-versus-growth capital,
service costs, supplier-finance settlement, seasonality, and the final residual
remain open.

The [Q-03 full-return input schema](capital-flow-wheaton-antamina-q03-full-return-input-schema-2026-09-16.md)
now makes the remaining after-tax financed return inputs field-level and
machine-readable. This improves the promotion test but does not change CA-06:
BHP-only delivery, settlement receipt, Antamina tax, financing allocation,
reserve-backed delivery, and source-linked IRR/NPV remain unproven.

The reproducibility check now also validates the document network itself:
`3,332` repository and sibling-repository Markdown links resolve with zero
broken filesystem links after the checker excludes the reader's intentional
virtual `/cluster/` routes. This is a source-navigation control, not evidence
that the underlying qualified investment claims are complete.

The current link audit has since added the Apollo intercompany-note balance
boundary, BHP annual-report route, Investor Day forward-profile route, dual-PMPA threshold route, post-event checklist update, method-registry update, WHCO guarantee route, Broadcom fee-timing route, cumulative Antamina cash-back proxy route, FY2026 production-calibration route, Q2 AMAPS 1 exposure route, structured AMAPS exposure route, Concord review-route update, Apollo parent-summary context, and the latest retail/Athene reviewer routes, and now reports `3,332` resolved repository and sibling-repository
Markdown links with zero broken links.
The [intercompany note longitudinal refresh](capital-flow-apollo-athene-intercompany-note-longitudinal-refresh-2026-09-16.md)
adds seven dated SEC balance observations for the direct AHL-to-AGM note route.
This materially strengthens Q-07's continuity and direction evidence, but
dated draws, repayment, use of proceeds, intercompany elimination, parent
receipt, and common-owner cash remain unresolved.

The [Q2 parent-cash perimeter reconciliation](capital-flow-apollo-athene-q2-parent-cash-perimeter-reconciliation-2026-09-16.md)
adds a non-additive denominator control for Q-07. It keeps `$25.4B`
consolidated unrestricted cash, `$3.412B` HoldCo-summary cash, `$3.415B`
Asset Management segment cash, `$110M` of H1 Athene distributions, and the
`$279M` AHL note balance in their correct scopes. This improves auditability
but does not prove parent receipt, legal availability, liability-adjusted cash,
or common-owner residual; the completion rows therefore remain unresolved.

The [BHP upfront-settlement bridge](capital-flow-wheaton-antamina-bhp-upfront-settlement-bridge-2026-09-16.md)
and the current Q-03 boundary now promote the narrow amount-and-date
observation that Wheaton reported a `$4.300B` Antamina PMPA payment on April
1, 2026, BHP reported the corresponding `$4.3B` receipt, and Wheaton disclosed
the term-loan, revolver, and cash funding mix. This is an upfront
closing-funds-flow direction, not a BHP-PMPA operating-credit, recurring
collection, tax-allocation, or full-return proof; Q-01, Q-02, Q-03, and CA-06
therefore remain below full completion.

The [retail lagged diagnostic](combined-investment-research-through-cycle-retail-lagged-diagnostic-2026-09-16.md)
adds a bounded negative test to Q-10: 7 of 15 usable transitions agree in
direction and 8 disagree. This is a reproducible falsifier of the simplest
affordability-to-cash lead, but not causal promotion because the panel is small,
pooled, and confounded and uses cash-after-property rather than normalized
owner cash.

The [medical-devices current-period synthesis](combined-investment-research-medical-devices-current-period-synthesis-2026-09-17.md)
now integrates the Stryker, Intuitive Surgical, and Henry Schein Q2/H1
refreshes. It adds no ranking: clinical adoption, recurring use, acquisition,
restructuring, lease collection, securitization, dilution, and common-owner
cash remain company-specific promotion gates.

The healthcare-distribution lane now also has three company-level promotion
artifacts: the McKesson longitudinal cash-perimeter bridge, the Cencora
OneOncology acquisition-return bridge, and the Cardinal Solaris/legal
owner-cash bridge. These strengthen period, legal-entity, and claim controls;
they do not change the original `12 of 13 proven; CA-06 partial` result.

## Latest execution audit — D-91 through D-95

The latest move-on work adds five bounded upgrades without changing the
completion grade:

- The restaurant current-period refresh separates McDonald's `$34.451B`
  franchised-sales denominator from company revenue and collected franchisor
  cash; franchisee collection and reinvestment evidence remains open.
- The insurance refresh adds Chubb's `$71.216B` net unpaid-loss liability,
  `$18.453B` reinsurance recoverable, `$11.353B` net claims paid, `$584M`
  favorable reserve development, and modeled catastrophe stress inputs.
- Q-03 adds contractual entitlement calculations of `30.375%` before the
  threshold and `20.25%` afterward, while BHP-specific credit-to-bank receipt
  evidence remains open.
- URI adds a parent-availability gate because URNA debt agreements restrict
  transfers to the holding company; the borrowing-base/NOLV and fleet-return
  gates remain open.
- PBF adds a calculated `$519.690M` principal-plus-premium floor for the
  still-pending September redemption and records the issued `$550M` 2032
  exchangeable financing with approximately `$533.6M` of net proceeds;
  settlement, accrued interest, dilution, and refinancing NPV remain open.

These updates improve the evidence chain and reader routing but do not prove
normalized common-owner cash, asset-level return, or the remaining CA-06 and
named-receipt gates. The original completion status therefore remains
`12 of 13 proven; CA-06 partial`.

The [cash logistics and managed-services valuation/liquidity workbench](combined-investment-research-brinks-cash-logistics-managed-services-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct annual-report lane for The Brink's Company. It keeps cash
routes, AMS/DRS contracts, labor, fleet, security claims, acquisition funding,
debt, and dilution separate from recurring-service growth, adjusted EBITDA,
free cash flow, and synergies. This is D-471; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The [mid-tier copper-gold and project-partnership valuation/liquidity workbench](combined-investment-research-hudbay-copper-gold-project-partnership-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct annual-report lane for Hudbay Minerals. It keeps copper, gold
credits, grades, concentrate logistics, JV proceeds, project funding,
permitting, sustaining capital, reclamation, debt, and dilution separate from
production, cash cost, adjusted EBITDA, free cash flow, and guidance. This is
D-470; the lane remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [nicotine transition and regulated-habit valuation/liquidity workbench](combined-investment-research-philip-morris-nicotine-transition-valuation-liquidity-workbench-2026-09-18.md)
adds a genuinely distinct annual-report lane for Philip Morris International.
It keeps combustibles, smoke-free migration, adult-user counts, excise taxes,
authorizations, manufacturing, litigation, debt, and dilution separate from
mix, users, shipments, adjusted EPS, dividends, and buybacks. This is D-469;
the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [creator imaging and hardware-to-workflow valuation/liquidity workbench](combined-investment-research-gopro-creator-imaging-workflow-valuation-liquidity-workbench-2026-09-18.md)
adds a genuinely distinct annual-report lane for GoPro. It keeps camera
sell-through, subscription collection, component commitments, inventory,
tariffs, product reinvestment, strategic alternatives, debt, and dilution
separate from units, subscribers, adjusted EBITDA, and roadmap claims. This is
D-468; the lane remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [Martin Marietta aggregates and infrastructure valuation/liquidity workbench](combined-investment-research-martin-marietta-aggregates-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into local quarry scarcity, freight, realized price per ton,
purchase-accounting noise, portfolio reshaping, infrastructure demand, borrowing
capacity, and diluted common residual. Shipments, EBITDA, OCF, FCF, and acquisition
proceeds remain diagnostic rather than normalized owner cash until price/mix,
replacement, acquisition-return, financing, and residual joins are evidenced. This is
D-426; the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Allegion physical access and security valuation/liquidity workbench](combined-investment-research-allegion-physical-access-security-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into installed access systems, electronics and software adoption,
Americas non-residential demand, regional mix, productivity, warranty, acquisition
effects, debt, and dilution. Revenue, adjusted EPS, available cash flow, and guidance
remain diagnostic until collection, installed-base, replacement, reinvestment,
financing, and residual joins are evidenced. This is D-427; the lane remains
qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The [Kraft Heinz packaged-food turnaround valuation/liquidity workbench](combined-investment-research-kraft-heinz-packaged-food-turnaround-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into center-store brands, volume and share, price/value architecture,
marketing and R&D reinvestment, affordability, commodity and tariff pressure, dividend
funding, debt, and dilution. Organic sales, adjusted earnings, FCF, and guidance remain
diagnostic until volume, share, reinvestment-return, working-capital, financing, and
residual joins are evidenced. This is D-428; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Teck diversified metals and copper-growth valuation/liquidity workbench](combined-investment-research-teck-diversified-metals-copper-growth-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into copper grades and production, QB reliability, zinc and Trail
smelting, steelmaking coal, critical-minerals processing, Anglo Teck merger execution,
mine replacement, capex, net cash, debt, and dilution. Production, EBITDA, OCF, FCF,
dividends, guidance, and merger synergies remain diagnostic until commodity, project,
processing, financing, merger, and residual joins are evidenced. This is D-429; the
lane remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The [CRH connected infrastructure materials valuation/liquidity workbench](combined-investment-research-crh-connected-infrastructure-materials-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into roads, water, utility products, pricing, portfolio churn, Arcosa
funding, residential weakness, capex, net debt, and dilution. Revenue, EBITDA, margins,
FCF, and acquisition proceeds remain diagnostic until price/volume, capital,
acquisition, financing, and residual joins are evidenced. This is D-430; the lane
remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The [Wiley authoritative knowledge and AI licensing valuation/liquidity workbench](combined-investment-research-wiley-authoritative-knowledge-ai-licensing-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Research and Learning, institutional subscriptions, open access,
AI licensing, rights ownership, recurring contracts, editorial investment, portfolio
simplification, debt, and dilution. AI revenue, adjusted EBITDA, EPS, OCF, and FCF
remain diagnostic until retention, rights, collection, reinvestment, financing, and
residual joins are evidenced. This is D-431; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Omnicom integrated advertising and attention valuation/liquidity workbench](combined-investment-research-omnicom-integrated-advertising-attention-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into client budgets, media pass-through, creative labor, data and
identity, AI measurement, IPG integration, talent retention, restructuring, debt, and
dilution. Organic growth, adjusted EBITA, EPS, FCF, and merger synergies remain
diagnostic until client, pass-through, integration, reinvestment, financing, and
residual joins are evidenced. This is D-432; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Brady workplace identification and safety valuation/liquidity workbench](combined-investment-research-brady-workplace-identification-safety-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into labels, signage, printers, software, lockout-tagout, safety
devices, regional mix, product innovation, acquisitions, working capital, debt, and
dilution. Sales, organic growth, adjusted EPS, OCF, and FCF remain diagnostic until
collection, workflow, replacement, innovation, financing, and residual joins are
evidenced. This is D-433; the lane remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [licensed collectibles and multiplatform play valuation/liquidity workbench](combined-investment-research-toys-fandom-play-valuation-liquidity-workbench-2026-09-18.md)
adds a genuinely distinct annual-report lane for Funko and Spin Master. It
keeps licensing guarantees, tariff normalization, inventory, retailer timing,
content and digital reinvestment, debt, and dilution separate from sales,
adjusted EBITDA, property counts, and digital users. This is D-467; the lane
remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Scholastic children’s reading and school-channel valuation/liquidity workbench](combined-investment-research-scholastic-childrens-reading-school-channel-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Book Fairs, Book Clubs, Trade, Education, Entertainment, school
and family relationships, franchise IP, sale-leasebacks, capital returns, debt, and
dilution. Revenue, Book Fair growth, adjusted EBITDA, FCF, and repurchases remain
diagnostic until school-channel, title, content, facility, financing, and residual joins
are evidenced. This is D-434; the lane remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Clear Channel Outdoor physical attention valuation/liquidity workbench](combined-investment-research-clear-channel-outdoor-physical-attention-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into billboards, transit, airports, street furniture, digital
conversion, advertiser collection, municipal contracts, capex, asset sales, merger
consideration, interest, debt, and dilution. Revenue, adjusted EBITDA, AFFO, guidance,
asset-sale proceeds, and merger value remain diagnostic until utilization, contract,
capex, interest, financing, and residual joins are evidenced. This is D-435; the lane
remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The [Nexxen CTV, programmatic, and data valuation/liquidity workbench](combined-investment-research-nexxen-ctv-programmatic-data-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into DSP and SSP economics, CTV inventory, ACR data, smart-TV
home-screen activation, data licensing, partner concentration, privacy, cloud costs,
cash, debt, and dilution. Programmatic revenue, contribution ex-TAC, adjusted EBITDA,
guidance, and data agreements remain diagnostic until CTV, rights, settlement,
retention, privacy, financing, and residual joins are evidenced. This is D-436; the
lane remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The [iHeartMedia audio and podcast attention valuation/liquidity workbench](combined-investment-research-iheart-audio-podcast-attention-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into broadcast radio, podcasts, digital audio, events, audience scale,
programmatic selling, data and attribution, political revenue, non-cash trade,
liquidity, leverage, and dilution. Revenue, adjusted EBITDA, FCF, audience scale,
guidance, and podcast growth remain diagnostic until collection, ex-political,
content, liquidity, financing, and residual joins are evidenced. This is D-437; the
lane remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The [Sirius XM paid audio and Pandora valuation/liquidity workbench](combined-investment-research-siriusxm-paid-audio-pandora-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into paid subscribers, churn, in-car distribution, premium content,
Pandora advertising and subscriptions, podcasting, royalties, free cash flow, debt, and
dilution. Subscribers, revenue, adjusted EBITDA, FCF, guidance, audience scale, and
capital returns remain diagnostic until retention, royalties, collection, distribution,
financing, and residual joins are evidenced. This is D-438; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Kohl’s department-store turnaround valuation/liquidity workbench](combined-investment-research-kohls-department-store-turnaround-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into department-store traffic, comparable sales, inventory and
markdowns, Sephora, loyalty and credit, omnichannel fulfillment, leases, debt, and
dilution. Sales, EPS, operating cash flow, and guidance remain diagnostic until demand,
inventory, Sephora, lease, financing, and residual joins are evidenced. This is D-439;
the lane remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The [APi Group safety and specialty-services valuation/liquidity workbench](combined-investment-research-api-group-safety-specialty-services-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into recurring inspection, monitoring, project execution, backlog,
field labor, acquisitions, cash conversion, debt, and dilution. Revenue, adjusted
EBITDA, backlog, adjusted FCF, guidance, and capital returns remain diagnostic until
recurring-service, project, labor, acquisition, financing, and residual joins are
evidenced. This is D-440; the lane remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Wyndham economy and midscale franchise valuation/liquidity workbench](combined-investment-research-wyndham-economy-midscale-franchise-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into franchise fees, RevPAR, room growth, pipeline quality, ancillary
revenue, franchisee health, FeePAR, fee deferrals, debt, and dilution. Rooms, pipeline,
adjusted EBITDA, FCF, guidance, and capital returns remain diagnostic until franchisee,
opening, collection, financing, and residual joins are evidenced. This is D-441; the
lane remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The [DraftKings real-money participation valuation/liquidity workbench](combined-investment-research-draftkings-real-money-participation-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into sportsbook handle, hold, promotions, iGaming, fantasy, lottery,
prediction markets, user retention, state licenses, payment settlement, cash, debt, and
dilution. Revenue, MUPs, ARPMUP, handle, adjusted EBITDA, guidance, and capital returns
remain diagnostic until hold, promotion, regulation, collection, financing, and
residual joins are evidenced. This is D-442; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [American Eagle and Aerie apparel valuation/liquidity workbench](combined-investment-research-american-eagle-aerie-apparel-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Aerie growth, American Eagle relevance, comparable sales,
inventory and markdowns, stores, digital demand, leases, capital returns, debt, and
dilution. Sales, comps, EPS, and guidance remain diagnostic until brand, inventory,
lease, financing, and residual joins are evidenced. This is D-443; the lane remains
qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The [Urban Outfitters and Nuuly lifestyle valuation/liquidity workbench](combined-investment-research-urban-outfitters-nuuly-lifestyle-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Anthropologie, Free People, Urban Outfitters, Nuuly, subscription
and rental utilization, wholesale, inventory, returns, tariffs, stores, digital demand,
leases, debt, and dilution. Revenue, comps, subscription growth, and guidance remain
diagnostic until banner, rental, inventory, returns, lease, financing, and residual
joins are evidenced. This is D-444; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Xerox installed-base and workflow-services valuation/liquidity workbench](combined-investment-research-xerox-installed-base-workflow-services-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into equipment, post-sale service, managed print, workflow and IT
attachment, financing, page volumes, replacement cycles, Lexmark and ITsavvy
integration, tariffs, debt, and dilution. Revenue, adjusted operating income, post-sale
mix, FCF, and synergies remain diagnostic until post-sale retention, replacement,
financing, integration, and residual joins are evidenced. This is D-445; the lane
remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The [Las Vegas Sands integrated-resort valuation/liquidity workbench](combined-investment-research-las-vegas-sands-integrated-resort-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Marina Bay Sands, Macao, gaming hold and volume, hotels,
conventions, luxury retail, concessions, expansion capex, debt, buybacks, and dilution.
Revenue, property EBITDA, gaming volume, guidance, dividends, buybacks, and expansion
value remain diagnostic until hold, concession, tourism, capex, financing, and residual
joins are evidenced. This is D-446; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Caesars Rewards and digital gaming valuation/liquidity workbench](combined-investment-research-caesars-rewards-digital-gaming-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into regional and Las Vegas gaming, Rewards, universal wallet,
sportsbook, iGaming, Racebook, property capex, leases, debt, interest, and dilution.
Revenue, adjusted EBITDA, digital growth, Rewards members, guidance, dividends, and
buybacks remain diagnostic until hold, rewards, wallet, capex, financing, and residual
joins are evidenced. This is D-447; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Electronic Arts live-services and franchise valuation/liquidity workbench](combined-investment-research-electronic-arts-live-services-franchise-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into full-game launches, live services, net bookings, player
engagement, EA SPORTS FC, Apex, Battlefield, deferred revenue, licensing, development
costs, merger costs, debt, and dilution. Net bookings, revenue, live-service growth,
adjusted EBITDA, guidance, and capital returns remain diagnostic until player, content,
development, licensing, financing, and residual joins are evidenced. This is D-448; the
lane remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The [Take-Two recurrent digital worlds valuation/liquidity workbench](combined-investment-research-take-two-recurrent-digital-worlds-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into full-game launches, recurrent consumer spending, net bookings,
GTA, NBA 2K, Zynga mobile, player retention, development capitalization, licensing,
deferred revenue, debt, and dilution. Net bookings, revenue, recurrent spending,
adjusted EBITDA, guidance, and tentpole launch value remain diagnostic until player,
content, development, licensing, financing, and residual joins are evidenced. This is
D-449; the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [NetApp hybrid-cloud data-platform valuation/liquidity workbench](combined-investment-research-netapp-hybrid-cloud-data-platform-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into hybrid-cloud systems, public-cloud services, support, software,
all-flash demand, billings, deferred revenue, channel distribution, receivables, debt,
and dilution. Revenue, services growth, billings, adjusted earnings, OCF, FCF, AI
demand, and capital returns remain diagnostic until cloud-service margin, collection,
channel, reinvestment, financing, and residual joins are evidenced. This is D-450; the
lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Ivanhoe African copper buildout valuation/liquidity workbench](combined-investment-research-ivanhoe-african-copper-buildout-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Kamoa-Kakula attributable cash, Kipushi inventory, Platreef
construction, smelter ramp, corridor logistics, JV accounting, project finance, taxes,
debt, and dilution. Copper production, JV revenue, adjusted EBITDA, OCF, project
guidance, and copper price remain diagnostic until attribution, inventory, ramp,
funding, tax, and residual joins are evidenced. This is D-451; the lane remains
qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Dow chemicals restructuring valuation/liquidity workbench](combined-investment-research-dow-chemicals-restructuring-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into polyethylene and feedstock exposure, downstream applications,
segment spreads, plant closures, cost programs, working capital, environmental claims,
dividends, debt, and dilution. Revenue, operating EBITDA, guidance, cost savings,
adjusted earnings, OCF, and dividends remain diagnostic until through-cycle spreads,
cash timing, claims, financing, and residual joins are evidenced. This is D-452; the
lane remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Lennar land-light homebuilder valuation/liquidity workbench](combined-investment-research-lennar-land-light-homebuilder-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into deliveries, orders, backlog, incentives, mortgage affordability,
cycle time, land exposure, mortgage/title capture, multifamily, working capital, debt,
and dilution. Deliveries, backlog, revenue, adjusted earnings, OCF, guidance, and
buybacks remain diagnostic until cancellations, inventory, land, financing, collection,
and residual joins are evidenced. This is D-453; the lane remains qualified, unranked,
and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Instacart grocery and retail-media valuation/liquidity workbench](combined-investment-research-instacart-grocery-retail-media-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into GTV, orders, shopper and retailer settlement, advertising,
Storefront software, in-store technology, AI products, acquisitions, working capital,
and dilution. GTV, orders, active customers, advertising revenue, adjusted EBITDA,
OCF, and buybacks remain diagnostic until settlement, retention, technology cost,
financing, and residual joins are evidenced. This is D-454; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [ICU Medical infusion and consumables valuation/liquidity workbench](combined-investment-research-icu-medical-infusion-consumables-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into infusion-system placement, recurring consumables, Vital Care,
hospital and distributor channels, safety-stock inventory, tariffs, quality spending,
acquisitions, debt, and dilution. Revenue, adjusted EBITDA, EPS, OCF, guidance, and
buybacks remain diagnostic until attachment, inventory, quality, supplier, financing,
and residual joins are evidenced. This is D-455; the lane remains qualified, unranked,
and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Quest Diagnostics laboratory-network valuation/liquidity workbench](combined-investment-research-quest-diagnostics-laboratory-network-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into requisition volume, routine and advanced assays, payer and
employer channels, consumer testing, logistics density, lab automation, acquisitions,
reimbursement, connectivity, debt, and dilution. Revenue, test volume, adjusted EPS,
OCF, guidance, and buybacks remain diagnostic until revenue-per-test, collection,
productivity, reimbursement, financing, and residual joins are evidenced. This is D-456;
the lane remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Taboola open-web performance-advertising valuation/liquidity workbench](combined-investment-research-taboola-open-web-performance-advertising-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into advertiser outcomes, ex-TAC gross profit, publisher and OEM
settlements, traffic concentration, AI products, data, sales costs, working capital,
debt, and dilution. Revenue, ex-TAC gross profit, adjusted EBITDA, free cash flow,
guidance, and buybacks remain diagnostic until advertiser retention, partner settlement,
traffic quality, financing, and residual joins are evidenced. This is D-457; the lane
remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Warby Parker omnichannel eyewear valuation/liquidity workbench](combined-investment-research-warby-parker-omnichannel-eyewear-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into active customers, ARPC, stores, exams, contacts, insurance,
tariffs, lens mix, Intelligent Eyewear, retail expansion, working capital, and dilution.
Revenue, active customers, ARPC, adjusted EBITDA, OCF, guidance, and buybacks remain
diagnostic until repeat, care, insurance, inventory, store, financing, and residual
joins are evidenced. This is D-458; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [GoDaddy small-business digital-presence valuation/liquidity workbench](combined-investment-research-godaddy-smb-digital-presence-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into domains, hosting, websites, commerce, payments, subscriptions,
customer care, AI tools, bookings, gross payments volume, working capital, debt, and
dilution. Revenue, ARR, ARPU, GPV, adjusted EBITDA, FCF, guidance, and buybacks remain
diagnostic until renewal, retention, payment, support, financing, and residual joins
are evidenced. This is D-459; the lane remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Liberty Global connectivity holding-company valuation/liquidity workbench](combined-investment-research-liberty-global-connectivity-holding-company-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into subscriber and ARPU economics, network investment, JV
distributions, listed stakes, infrastructure monetization, asset sales, debt, portfolio
governance, and dilution. Revenue, connections, ARPU, adjusted metrics, OCF, guidance,
and repurchases remain diagnostic until churn, JV, capex, disposal, financing, and
residual joins are evidenced. This is D-460; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Sunstone hotel redevelopment REIT valuation/liquidity workbench](combined-investment-research-sunstone-hotel-redevelopment-reit-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into property RevPAR, occupancy, ADR, renovations, redevelopment
ramps, asset sales, hotel capex, debt, dividends, buybacks, and dilution. RevPAR,
ADR, occupancy, Adjusted EBITDAre, FFO, guidance, and buybacks remain diagnostic until
property collection, redevelopment, capex, financing, and residual joins are evidenced.
This is D-461; the lane remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [Shentel regional fiber buildout valuation/liquidity workbench](combined-investment-research-shentel-regional-fiber-buildout-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into homes passed, penetration, Glo Fiber additions, incumbent
broadband runoff, grants, carrier/backhaul exposure, capex, debt, and dilution. Revenue,
homes passed, adjusted EBITDA, guidance, OCF, and fiber growth remain diagnostic until
penetration, grant, capex, legacy, financing, and residual joins are evidenced. This is
D-462; the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Avanos specialty clinical-supply valuation/liquidity workbench](combined-investment-research-avanos-specialty-clinical-supply-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into enteral nutrition, neonatal care, pain management, procedure
utilization, hospital/distributor routing, transformation savings, the pending
take-private, working capital, debt, and dilution. Revenue, adjusted EPS, adjusted
EBITDA, OCF, guidance, and sale consideration remain diagnostic until clinical
attachment, cash conversion, transformation, transaction, financing, and residual
joins are evidenced. This is D-463; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Epson office-edge and precision-hardware valuation/liquidity workbench](combined-investment-research-epson-office-edge-precision-hardware-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into printers, ink and consumables, office fleets, projectors,
industrial printing, robotics, wearables, tariffs, energy efficiency, impairment,
capex, and dilution. Revenue, business profit, shipments, adjusted metrics, guidance,
and buybacks remain diagnostic until consumables attachment, fleet, segment margin,
inventory, financing, and residual joins are evidenced. This is D-464; the lane remains
qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Becton Dickinson institutional workflow valuation/liquidity workbench](combined-investment-research-becton-dickinson-institutional-workflow-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into medication delivery, specimen management, connected care,
prefillable drug delivery, interventional products, the Waters perimeter change, debt,
repurchases, quality spending, and dilution. Revenue, adjusted EPS, segment growth,
OCF, guidance, and repurchases remain diagnostic until workflow attachment, perimeter,
quality, financing, and residual joins are evidenced. This is D-465; the lane remains
qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [PubMatic sell-side ad-tech valuation/liquidity workbench](combined-investment-research-pubmatic-sell-side-adtech-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into publisher settlement, demand quality, CTV/mobile/app mix,
impressions, AI-powered deals, platform concentration, working capital, repurchases,
and dilution. Revenue, impressions, adjusted EBITDA, free cash flow, guidance, and
buybacks remain diagnostic until take-rate quality, publisher settlement, demand
diversification, financing, and residual joins are evidenced. This is D-466; the lane
remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Etsy two-sided marketplace and trust infrastructure valuation/liquidity workbench](combined-investment-research-etsy-two-sided-marketplace-valuation-liquidity-workbench-2026-09-18.md)
adds buyer and seller liquidity, GMS, take rate, payments, advertising, seller
services, discovery, trust and safety, cross-border shipping, tariffs, AI-mediated
commerce, working capital, debt, and dilution. It keeps GMS, active buyers, active
sellers, take rate, revenue, adjusted EBITDA, guidance, and buybacks out of normalized
owner cash until payment, settlement, retention, trust, financing, and diluted-
residual joins are evidenced. This is D-401; the cohort remains qualified, unranked,
and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Magnite programmatic advertising and CTV valuation/liquidity workbench](combined-investment-research-magnite-programmatic-ctv-valuation-liquidity-workbench-2026-09-18.md)
adds CTV, DV+, contribution ex-TAC, gross billings, traffic-acquisition pass-throughs,
publisher and buyer relationships, take rates, receivables, AI tooling, regulation,
acquisitions, debt, and dilution. It keeps gross revenue, contribution, CTV growth,
adjusted EBITDA, FCF, guidance, and buybacks out of normalized owner cash until
supply-path, collection, take-rate, platform-cost, financing, and diluted-residual
joins are evidenced. This is D-400; the cohort remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Southwest low-cost airline transformation valuation/liquidity workbench](combined-investment-research-southwest-low-cost-airline-transformation-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct airline-transformation company object covering base fares, bags,
assigned and extra-legroom seating, Rapid Rewards, managed-business revenue,
fleet, utilization, fuel, labor, maintenance, airport commitments, technology,
debt, and dilution. Passengers, revenue, unit revenue, adjusted EBIT, OCF, FCF,
loyalty members, and repurchases remain outside normalized owner cash until
collection, fleet, transformation, and common-residual joins are evidenced. This
is D-425; the lane remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [New York Times trust, subscription, and bundle valuation/liquidity workbench](combined-investment-research-nyt-trust-subscription-bundle-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct direct-information company object covering subscriptions,
newsroom investment, The Athletic, Audio, Cooking, Games, Wirecutter,
advertising, affiliate and licensing revenue, content rights, churn, product
bundles, debt, and dilution. Subscribers, ARPU, revenue, adjusted earnings,
OCF, FCF, and ad growth remain outside normalized owner cash until collection,
retention, content, reinvestment, and common-residual joins are evidenced. This
is D-424; the lane remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [Loews subsidiary allocator valuation/liquidity workbench](combined-investment-research-loews-subsidiary-allocator-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific holding-company object covering CNA, Boardwalk
Pipelines, Loews Hotels, Altium Packaging, subsidiary distributions, insurance
reserves, energy infrastructure, hospitality, packaging, parent liquidity,
debt, and dilution. Subsidiary earnings, asset values, OCF, dividends, and
repurchases remain outside normalized owner cash until legal-entity cash,
reinvestment, claims, and common-residual joins are evidenced. This is D-423;
the lane remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Cigna benefits and pharmacy-services valuation/liquidity workbench](combined-investment-research-cigna-benefits-pharmacy-services-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific payer-and-services object covering Cigna
Healthcare, Evernorth, pharmacy and specialty services, employer and government
lives, medical-cost trend, rebates, claims reserves, client retention, capital,
debt, and dilution. Covered lives, revenue, adjusted earnings, medical margin,
OCF, FCF, and repurchases remain outside normalized owner cash until claims,
rebate, collection, capital, and common-residual joins are evidenced. This is
D-422; the lane remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [Hilton asset-light lodging and loyalty valuation/liquidity workbench](combined-investment-research-hilton-asset-light-lodging-loyalty-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific hospitality object covering franchising,
management, RevPAR, room additions, pipeline conversion, Hilton Honors, owner
economics, digital booking, guarantees, debt, and dilution. Rooms, pipeline,
RevPAR, adjusted EBITDA, OCF, FCF, and buybacks remain outside normalized owner
cash until fee collection, owner funding, opening, reinvestment, and
common-residual joins are evidenced. This is D-421; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [GEO outsourced secure-services valuation/liquidity workbench](combined-investment-research-geo-outsourced-secure-services-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct institutional-capacity company object covering secure facilities,
processing, reentry, transportation, electronic monitoring, case management,
healthcare, government contracts, idle capacity, labor, debt, claims, and
dilution. Beds, participants, revenue, adjusted EBITDA, OCF, FCF, guidance, and
repurchases remain outside normalized owner cash until contract, staffing,
capacity, claims, and common-residual joins are evidenced. This is D-420; the
lane remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Regeneron concentrated-biologics valuation/liquidity workbench](combined-investment-research-regeneron-concentrated-biologics-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific biotech object covering Dupixent, EYLEA, other
franchises, label expansion, clinical development, acquired IPR&D,
manufacturing, payer access, patent and litigation exposure, debt, and dilution.
Product revenue, prescriptions, EPS, adjusted earnings, OCF, FCF, milestones,
and buybacks remain outside normalized owner cash until collection, franchise,
pipeline, claims, and common-residual joins are evidenced. This is D-419; the
lane remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [JPMorgan deposit, credit, and capital valuation/liquidity workbench](combined-investment-research-jpmorgan-deposit-credit-capital-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific money-center-bank object covering deposits,
lending, securities, markets, payments, investment banking, credit losses,
capital and liquidity, technology, legal claims, debt, and dilution. Deposits,
loan growth, revenue, EPS, and repurchases remain outside normalized owner cash
until credit, funding, capital, liquidity, and common-residual joins are
evidenced. This is D-418; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Walmart omnichannel ecosystem valuation/liquidity workbench](combined-investment-research-walmart-omnichannel-ecosystem-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct mass-retail ecosystem company object covering merchandise,
eCommerce, membership, advertising, marketplace, fulfillment, financial
services, inventory, supplier terms, stores, labor, debt, and dilution. Revenue,
eCommerce, advertising, membership fees, adjusted income, OCF, FCF, and
repurchases remain outside normalized owner cash until collection, fulfillment,
reinvestment, and common-residual joins are evidenced. This is D-417; the lane
remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [BHP copper and bulk-materials portfolio valuation/liquidity workbench](combined-investment-research-bhp-copper-bulk-materials-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific mining allocator object covering copper, iron
ore, potash, production, grades, recoveries, unit costs, mine life, portfolio
recycling, permitting, capex, debt, and dilution. Production, EBITDA, OCF, FCF,
dividends, and divestiture proceeds remain outside normalized owner cash until
commodity, project, funding, and common-residual joins are evidenced. This is
D-416; the lane remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [Fujifilm diversified imaging, materials, and workflow valuation/liquidity workbench](combined-investment-research-fujifilm-diversified-imaging-materials-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct diversified-interface and materials company object covering
Healthcare, Electronics, Business Innovation, Imaging, bio-CDMO, semiconductor
materials, workflow renewal, raw materials, fixed-cost absorption, debt, and
dilution. Segment revenue, operating income, OCF, FCF, and portfolio breadth
remain outside normalized owner cash until segment collection, capacity,
reinvestment, and common-residual joins are evidenced. This is D-415; the lane
remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Costco membership warehouse valuation/liquidity workbench](combined-investment-research-costco-membership-warehouse-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct membership-funded warehouse company object covering merchandise
sales, membership fees, renewal, traffic, digitally enabled sales, gasoline,
pharmacy, private label, inventory, supplier terms, real estate, labor, debt,
and dilution. Sales, membership fees, OCF, FCF, and repurchases remain outside
normalized owner cash until collection, renewal, inventory, reinvestment, and
common-residual joins are evidenced. This is D-414; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Franklin Resources hybrid asset-management valuation/liquidity workbench](combined-investment-research-franklin-resources-hybrid-asset-management-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific asset-management object covering public
markets, ETFs, SMAs, alternatives, private markets, AUM flows, fee rates,
distribution, Western Asset remediation, debt, and dilution. AUM, inflows,
revenue, adjusted earnings, OCF, FCF, and repurchases remain outside normalized
owner cash until fee collection, retention, deployment, remediation, and
common-residual joins are evidenced. This is D-413; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Netflix subscription video and advertising valuation/liquidity workbench](combined-investment-research-netflix-subscription-video-advertising-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct recurring-attention company object covering memberships,
retention, pricing, advertising, content commitments, production and licensing,
amortization, regional economics, live and gaming investment, debt, and
dilution. Memberships, viewing hours, revenue, margin, OCF, FCF, and ad revenue
remain outside normalized owner cash until collection, content-return,
reinvestment, and common-residual joins are evidenced. This is D-412; the lane
remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Labcorp diagnostics and biopharma-laboratory valuation/liquidity workbench](combined-investment-research-labcorp-diagnostics-biopharma-labs-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct healthcare-infrastructure company object covering routine and
specialty diagnostics, Biopharma Laboratory Services, specimen volume, payer
collection, trial contracts, central-lab throughput, labor, automation, quality,
acquisitions, debt, and dilution. Test volume, revenue, adjusted earnings, OCF,
FCF, and guidance remain outside normalized owner cash until collection,
delivery, reinvestment, and common-residual joins are evidenced. This is D-411;
the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Kroger grocery, loyalty, and retail-media valuation/liquidity workbench](combined-investment-research-kroger-grocery-loyalty-retail-media-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct grocery-and-data-platform company object covering basket
sell-through, loyalty, Kroger Precision Marketing, eCommerce, pharmacy, fuel,
private label, inventory, supplier terms, stores, debt, and dilution. Sales,
eCommerce growth, retail-media profit, adjusted FIFO profit, OCF, FCF, and
repurchases remain outside normalized owner cash until collection, inventory,
reinvestment, and common-residual joins are evidenced. This is D-410; the lane
remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Insulet automated insulin-delivery valuation/liquidity workbench](combined-investment-research-insulet-automated-insulin-delivery-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct recurring-therapy and consumables company object covering Pods,
software and algorithms, reimbursement, pharmacy access, active-user retention,
CGM integration, manufacturing, quality, clinical gates, debt, and dilution.
Pods shipped, active users, revenue, adjusted income, OCF, FCF, and guidance
remain outside normalized owner cash until collection, reimbursement, quality,
reinvestment, and common-residual joins are evidenced. This is D-409; the lane
remains qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Teva generics and innovative-pharma transition valuation/liquidity workbench](combined-investment-research-teva-generics-innovative-pharma-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct global drug-access and portfolio-transition company object
covering generics, biosimilars, innovative brands, manufacturing, R&D, patent
and litigation exposure, transformation, debt, and dilution. Product revenue,
prescriptions, adjusted EBITDA, guidance, OCF, FCF, and milestones remain
outside normalized owner cash until collection, launch-return, claims, and
common-residual joins are evidenced. This is D-408; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Delta network airline and loyalty valuation/liquidity workbench](combined-investment-research-delta-network-airline-loyalty-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct network-airline company object covering passenger and premium
economics, SkyMiles, American Express remuneration, award travel, fleet, fuel,
labor, maintenance, deferred revenue, debt, and dilution. Passenger revenue,
loyalty members, adjusted income, OCF, FCF, and partner remuneration remain
outside normalized owner cash until collection, award, fleet, and common-
residual joins are evidenced. This is D-407; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Tenet hospital and ambulatory-care valuation/liquidity workbench](combined-investment-research-tenet-hospital-ambulatory-care-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct provider-system company object covering hospitals, outpatient
care, USPI ambulatory surgery, payer mix, acuity, supplemental Medicaid
revenue, labor, facility investment, debt, and dilution. Admissions, adjusted
EBITDA, adjusted FCF, revenue, and portfolio growth remain outside normalized
owner cash until collection, reimbursement, reinvestment, and common-residual
joins are evidenced. This is D-406; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Spotify recurring-audio platform valuation/liquidity workbench](combined-investment-research-spotify-recurring-audio-platform-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct cultural-subscription company object covering Premium billing,
ad-supported reach, royalty and creator settlement, podcasts, audiobooks,
recommendation and AI investment, content returns, debt, and dilution. MAUs,
subscribers, revenue, gross margin, FCF, and creator payouts remain outside
normalized owner cash until collection, payout, reinvestment, and common-
residual joins are evidenced. This is D-403; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Gallagher brokerage and risk-advisory valuation/liquidity workbench](combined-investment-research-arthur-gallagher-brokerage-risk-advisory-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct fee-based insurance-distribution company object covering
brokerage, risk management, producer retention, acquisition cohorts, integration
cash, working capital, debt, and dilution. Revenue, organic fee growth, adjusted
earnings, OCF, and acquisitions remain outside normalized owner cash until
collection, cohort-return, integration, and common-residual joins are evidenced.
This is D-404; the lane remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [HP endpoint and printing valuation/liquidity workbench](combined-investment-research-hp-endpoint-printing-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct mature-hardware company object covering Personal Systems,
Printing, endpoint sell-through, channel inventory, supplies attachment,
tariffs, restructuring, debt, and dilution. Revenue, units, adjusted EPS, OCF,
FCF, and repurchases remain outside normalized owner cash until collection,
inventory, reinvestment, and common-residual joins are evidenced. This is D-405;
the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Apple device ecosystem valuation/liquidity workbench](combined-investment-research-apple-device-ecosystem-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct device-and-services company object covering sell-through,
installed-base retention, Services collection, supplier commitments, R&D,
tariffs, regulation, capital returns, debt, and dilution. Device units,
Services margin, OCF, FCF, and buybacks remain outside normalized owner cash
until collection, reinvestment, regulatory, and common-residual joins are
evidenced. This is D-402; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Con Edison urban regulated utility valuation/liquidity workbench](combined-investment-research-con-ed-urban-regulated-utility-valuation-liquidity-workbench-2026-09-18.md)
adds electric, gas, steam, transmission, holding-company activity, rate-base
recovery, customer collections, affordability, reliability, resilience, substations,
capital programs, forward equity, debt, and dilution. It keeps utility EPS, rate-base
growth, capex, OCF, guidance, dividends, and share issuance out of normalized owner
cash until recovery, collection, regulatory, financing, and diluted-residual joins are
evidenced. This is D-399; the cohort remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Chewy autoship and pet-care commerce valuation/liquidity workbench](combined-investment-research-chewy-autoship-pet-care-valuation-liquidity-workbench-2026-09-18.md)
adds merchandise, Autoship, pharmacy and prescriptions, active customers, net sales
per customer, fulfillment, inventory, customer acquisition, service attachment, debt,
and dilution. It keeps active customers, Autoship share, net sales, adjusted EBITDA,
FCF, guidance, and buybacks out of normalized owner cash until retention, collection,
fulfillment, pharmacy, financing, and diluted-residual joins are evidenced. This is
D-398; the cohort remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [SBA Communications tower-leasing valuation/liquidity workbench](combined-investment-research-sba-tower-leasing-valuation-liquidity-workbench-2026-09-18.md)
adds site leasing, domestic and international towers, carrier amendments, tenant
density, land control, churn, FX, acquisitions, AFFO, capex, debt, REIT distributions,
and dilution. It keeps site count, mobile traffic, AFFO, adjusted EBITDA, backlog,
guidance, and dividends out of normalized owner cash until carrier, land, capital,
financing, and diluted-residual joins are evidenced. This is D-397; the cohort
remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Macy's omnichannel portfolio and retail-credit valuation/liquidity workbench](combined-investment-research-macys-omnichannel-portfolio-valuation-liquidity-workbench-2026-09-18.md)
adds Macy's, Bloomingdale's, Bluemercury, merchandise sell-through, digital and
marketplace activity, Macy's Media Network, credit-card revenue, inventory, markdowns,
stores, leases, real estate, debt, and dilution. It keeps comparable sales, adjusted
EBITDA, credit-card revenue, media revenue, OCF, guidance, and buybacks out of
normalized owner cash until banner, sell-through, credit, collection, lease,
financing, and diluted-residual joins are evidenced. This is D-396; the cohort
remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Church & Dwight routine-use brands and portfolio valuation/liquidity workbench](combined-investment-research-church-dwight-routine-use-brands-valuation-liquidity-workbench-2026-09-18.md)
adds routine-use sell-through, retailer and eCommerce collections, brand support,
innovation, input costs, portfolio pruning, tuck-in acquisitions, inventory, debt,
claims, and dilution. It keeps organic growth, online mix, adjusted EPS, OCF,
guidance, and buybacks out of normalized owner cash until sell-through, collection,
acquisition-return, financing, and diluted-residual joins are evidenced. This is
D-395; the cohort remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [Bank of America deposit, credit, and capital valuation/liquidity workbench](combined-investment-research-bank-of-america-deposit-credit-valuation-liquidity-workbench-2026-09-18.md)
adds deposits, loans and leases, net interest income, markets and fee businesses,
credit losses, securities duration, liquidity, capital ratios, regulatory constraints,
technology, legal claims, capital return, and dilution. It keeps deposits, loan
growth, revenue, EPS, bank OCF, guidance, and buybacks out of normalized owner cash
until asset-quality, capital, funding, regulatory, and diluted-residual joins are
evidenced. This is D-394; the cohort remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [National CineMedia physical-attention and cinema advertising valuation/liquidity workbench](combined-investment-research-national-cinemedia-physical-attention-valuation-liquidity-workbench-2026-09-18.md)
adds cinema-screen inventory, exhibitor relationships, attendance, advertiser
demand, revenue per attendee, measurement, movie-slate timing, transformation,
leases, debt, and dilution. It keeps attendance, revenue, adjusted OIBDA, audience
reach, cost savings, and guidance out of normalized owner cash until slate,
exhibitor, collection, fixed-cost, financing, and diluted-residual joins are
evidenced. This is D-393; the cohort remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Sun Country hybrid airline and cargo valuation/liquidity workbench](combined-investment-research-sun-country-hybrid-airline-cargo-valuation-liquidity-workbench-2026-09-18.md)
adds scheduled passenger, charter, and Amazon cargo flying, fleet and crew
utilization, fuel, labor, aircraft ownership and leases, maintenance, customer
concentration, merger consideration, debt, and dilution. It keeps passengers,
departures, cargo revenue, adjusted EBITDA, OCF, and merger value out of normalized
owner cash until mix, utilization, maintenance, financing, merger, and diluted-
residual joins are evidenced. This is D-392; the cohort remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Alnylam RNAi therapeutics and franchise valuation/liquidity workbench](combined-investment-research-alnylam-rnai-therapeutics-valuation-liquidity-workbench-2026-09-18.md)
adds TTR and rare-franchise products, diagnosis, reimbursement, label expansion,
partner and royalty economics, launch costs, pipeline trials, manufacturing, debt,
claims, and dilution. It keeps product revenue, prescriptions, guidance, milestones,
profitability, and buybacks out of normalized owner cash until franchise, access,
collection, pipeline, partner, financing, and diluted-residual joins are evidenced.
This is D-391; the cohort remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [First Solar thin-film manufacturing and contracted-energy-hardware valuation/liquidity workbench](combined-investment-research-first-solar-thin-film-manufacturing-valuation-liquidity-workbench-2026-09-18.md)
adds thin-film modules, factory ramp, contracted backlog, customer deposits, delivery
and termination risk, domestic policy support, third-party volume, underutilization,
capex, working capital, claims, and dilution. It keeps gigawatts, module volume,
adjusted EBITDA, tax credits, net cash, guidance, and buybacks out of normalized
owner cash until contract, acceptance, policy, factory, collection, financing, and
diluted-residual joins are evidenced. This is D-390; the cohort remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Valmont utility structures, coatings, and irrigation valuation/liquidity workbench](combined-investment-research-valmont-utility-structures-coatings-valuation-liquidity-workbench-2026-09-18.md)
adds utility structures, coatings, telecommunications, irrigation, water, backlog,
steel and tariff exposure, ConcealFab, portfolio exits, claims, debt, and dilution.
It keeps backlog, infrastructure demand, adjusted operating income, guidance, OCF,
and buybacks out of normalized owner cash until segment, acceptance, collection,
capacity, financing, and diluted-residual joins are evidenced. This is D-389; the
cohort remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [D.R. Horton homebuilder and housing-finance valuation/liquidity workbench](combined-investment-research-dr-horton-homebuilder-valuation-liquidity-workbench-2026-09-18.md)
adds closings, orders, cancellations, incentives, land and lot control, construction
inventory, rental operations, Forestar, mortgage/title activity, debt, and dilution.
It keeps orders, backlog, closing volume, revenue, EPS, operating cash flow, and
repurchases out of normalized owner cash until affordability, incentive, inventory,
delivery, financing, and diluted-residual joins are evidenced. This is D-388; the
cohort remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Medpace clinical-trial infrastructure valuation/liquidity workbench](combined-investment-research-medpace-clinical-trial-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
adds trial design, patient and site execution, regulatory coordination, sponsor
awards, backlog, book-to-bill, employee capacity, study costs, claims, and dilution.
It keeps awards, backlog, book-to-bill, revenue, EBITDA, and repurchases out of
normalized owner cash until delivery, cancellation, sponsor, collection, utilization,
and diluted-residual joins are evidenced. This is D-387; the cohort remains
qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [UPS parcel-network and logistics valuation/liquidity workbench](combined-investment-research-ups-parcel-network-valuation-liquidity-workbench-2026-09-18.md)
adds package density, mix, labor, aircraft and vehicle assets, automation, Amazon
concentration, network redesign, transformation charges, capex, leases, debt, and
dilution. It keeps package volume, adjusted operating profit, guidance, operating
cash flow, and buybacks out of normalized owner cash until density, collection,
transformation, reinvestment, financing, and diluted-residual joins are evidenced.
This is D-386; the cohort remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Zebra enterprise data-capture and workflow valuation/liquidity workbench](combined-investment-research-zebra-enterprise-data-capture-valuation-liquidity-workbench-2026-09-18.md)
adds Connected Frontline and Asset Visibility and Automation, installed devices,
supplies, services, software, channel inventory, customer modernization, Elo and
Photoneo integration, debt, and dilution. It keeps revenue, segment growth, device
volume, adjusted EPS, and buybacks out of normalized owner cash until attachment,
collection, acquisition-return, financing, and diluted-residual joins are evidenced.
This is D-384; the cohort remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Nutrien agricultural-inputs and crop-cycle valuation/liquidity workbench](combined-investment-research-nutrien-agricultural-inputs-valuation-liquidity-workbench-2026-09-18.md)
adds potash, nitrogen, phosphate, retail agronomy, fertilizer prices, natural gas,
grower credit, mine and plant reliability, portfolio exits, capex, debt, and dilution.
It keeps tonnage, fertilizer prices, adjusted EBITDA, dividends, repurchases, and
divestiture proceeds out of normalized owner cash until crop-cycle, collection,
maintenance, financing, and diluted-residual joins are evidenced. This is D-385;
the cohort remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Choice Hotels franchise and conversion valuation/liquidity workbench](combined-investment-research-choice-hotels-franchise-conversion-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct practical-lodging franchise perimeter: franchise fees, conversions,
extended stay, RevPAR, owner economics, pipeline, franchisee lending, debt, claims,
and dilution. Rooms, pipeline, agreements awarded, RevPAR, adjusted EBITDA,
guidance, and buybacks remain diagnostic until franchisee, opening, fee, financing,
and common-residual joins are evidenced. This is D-383; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Sonoco packaging platform valuation/liquidity workbench](combined-investment-research-sonoco-packaging-platform-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct multi-format packaging perimeter: Consumer Packaging, Industrial
Paper Packaging, paperboard, metal, recycled fiber, plant utilization, price-cost,
Eviosys, ThermoSafe, capex, debt, claims, and dilution. Sales, adjusted EBITDA,
guidance, operating cash flow, and buybacks remain diagnostic until format,
price-cost, integration, financing, and common-residual joins are evidenced. This
is D-382; the lane remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [Guardant liquid biopsy and screening valuation/liquidity workbench](combined-investment-research-guardant-liquid-biopsy-screening-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct precision-oncology information perimeter: oncology, Shield
screening, biopharma/data, test volume, reimbursement, clinical validation, lab
capacity, cash burn, debt, claims, and dilution. Revenue growth, test volume,
Shield tests, guidance, adjusted metrics, and buybacks remain diagnostic until
reimbursement, screening, collection, cost, financing, and common-residual joins
are evidenced. This is D-381; the lane remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Gannett local-news and digital transition valuation/liquidity workbench](combined-investment-research-gannett-local-news-digital-transition-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct local-information perimeter: print, digital subscriptions,
advertising, LocaliQ, audience traffic, AI licensing, restructuring, pension/debt
claims, and dilution. Revenue, digital mix, visitors, subscriptions, adjusted
EBITDA, guidance, and turnaround claims remain diagnostic until renewal, traffic,
collection, financing, and common-residual joins are evidenced. This is D-380; the
lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Adtalem/Covista healthcare education valuation/liquidity workbench](combined-investment-research-adtalem-covista-healthcare-education-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct regulated workforce-education perimeter: Walden, Chamberlain,
Medical and Veterinary, enrollment, revenue per student, outcomes, clinical sites,
faculty, regulation, debt, claims, and dilution. Enrollment, adjusted EBITDA,
guidance, program growth, and buybacks remain diagnostic until retention, outcomes,
tuition, compliance, financing, and common-residual joins are evidenced. This is
D-379; the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [MGM destination gaming and digital valuation/liquidity workbench](combined-investment-research-mgm-destination-gaming-digital-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct diversified resort-platform perimeter: Las Vegas, regional gaming,
Macau, MGM Digital, BetMGM affiliates, occupancy, casino hold, resort capex, Osaka
development, debt, claims, and dilution. Revenue, occupancy, adjusted EBITDA,
guidance, property sales, and buybacks remain diagnostic until segment, hold,
digital, development, financing, and common-residual joins are evidenced. This is
D-378; the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Robert Half staffing and Protiviti valuation/liquidity workbench](combined-investment-research-robert-half-staffing-protiviti-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct labor-market intermediary perimeter: contract talent, permanent
placement, Protiviti, bill rates, utilization, wages, collections, receivables,
restructuring, debt, dividends, and dilution. Revenue, sequential growth,
placements, adjusted EPS, guidance, and dividends remain diagnostic until labor,
utilization, collection, financing, and common-residual joins are evidenced. This
is D-377; the lane remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [O-I Glass furnace packaging valuation/liquidity workbench](combined-investment-research-oi-glass-furnace-packaging-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct glass-container manufacturing perimeter: Americas and Europe,
furnaces, cullet, energy, utilization, regional pricing, Fit to Win, impairment,
capex, debt, claims, and dilution. Volume, segment operating profit, Fit to Win
benefits, adjusted EBITDA, guidance, and buybacks remain diagnostic until furnace,
energy, utilization, financing, and common-residual joins are evidenced. This is
D-376; the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [First Quantum copper restart valuation/liquidity workbench](combined-investment-research-first-quantum-copper-restart-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct concentrated-mining perimeter: Kansanshi, Sentinel, Enterprise,
Cobre Panama, nickel, grades, throughput, stockpiles, hedges, fuel, FX, capex,
jurisdiction, debt, claims, and dilution. Production, copper price, EBITDA,
guidance, reserves, and buybacks remain diagnostic until mine, restart, cost,
jurisdiction, financing, and common-residual joins are evidenced. This is D-375;
the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Stagwell AI agency platform valuation/liquidity workbench](combined-investment-research-stagwell-ai-agency-platform-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct challenger-agency perimeter: net revenue, client retention, digital
transformation, advocacy, The Machine, Marketing Cloud, data, labor, acquisitions,
working capital, debt, and dilution. Gross revenue, net new business, adjusted
EBITDA, guidance, AI claims, and buybacks remain diagnostic until net-revenue,
retention, software, collection, and common-residual joins are evidenced. This is
D-374; the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Eastman Kodak print and materials valuation/liquidity workbench](combined-investment-research-eastman-kodak-print-materials-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct legacy-imaging and industrial-substrate perimeter: Print, AM&C,
film, workflow, silver and aluminum, inventory, restructuring, legacy claims, term
debt, and dilution. Revenue, gross profit, operational EBITDA, guidance, turnaround
claims, and buybacks remain diagnostic until recurring-usage, input, inventory,
claims, and common-residual joins are evidenced. This is D-373; the lane remains
qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The [Comscore audience measurement valuation/liquidity workbench](combined-investment-research-comscore-audience-measurement-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct measurement-infrastructure perimeter: cross-platform, local-TV,
Proximic, syndicated panels, data rights, customer renewal, recapitalization,
preferred claims, debt, and dilution. Revenue, cross-platform growth, local-TV
growth, adjusted EBITDA, guidance, and buybacks remain diagnostic until renewal,
collection, data-cost, financing, and common-residual joins are evidenced. This is
D-372; the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Carnival cruise, destination, and wallet valuation/liquidity workbench](combined-investment-research-carnival-cruise-destination-wallet-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct capital-heavy travel perimeter: bookings, customer deposits,
occupancy, ticket yield, onboard and pre-cruise spend, fuel, fleet capex, debt,
legal structure, claims, and dilution. Revenue, bookings, deposits, occupancy,
adjusted EBITDA, guidance, and buybacks remain diagnostic until yield, delivery,
deposit, fleet, financing, and common-residual joins are evidenced. This is D-371;
the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Ionis antisense commercial platform valuation/liquidity workbench](combined-investment-research-ionis-antisense-commercial-platform-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct biotechnology IP-monetization perimeter: owned products, royalties,
collaborations, milestones, TRYNGOLZA, clinical trials, launch costs, partner
economics, cash burn, debt, and dilution. Revenue, milestones, royalties, guidance,
pipeline catalysts, adjusted metrics, and buybacks remain diagnostic until franchise,
partner, trial, collection, and common-residual joins are evidenced. This is D-370;
the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Commercial Metals rebar and construction valuation/liquidity workbench](combined-investment-research-commercial-metals-rebar-construction-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct recycled-steel and construction-solutions perimeter: scrap spreads,
rebar, fabrication, precast, backlog, acquisitions, capex, leverage, Europe/CBAM
exposure, claims, and dilution. Revenue, steel margins, adjusted EBITDA, guidance,
backlog, and buybacks remain diagnostic until scrap, project, acquisition-return,
financing, and common-residual joins are evidenced. This is D-369; the lane remains
qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The [Reliance metals service-center valuation/liquidity workbench](combined-investment-research-reliance-metals-service-center-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct downstream distribution perimeter: tons, value-added processing,
mill purchases, price and FIFO effects, inventory, branch density, acquisitions,
capex, debt, capital returns, and dilution. Tons, price, sales, FIFO earnings,
adjusted EPS, guidance, and buybacks remain diagnostic until processing, inventory,
collection, financing, and common-residual joins are evidenced. This is D-368; the
lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Knife River aggregates and contracting valuation/liquidity workbench](combined-investment-research-knife-river-aggregates-contracting-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct reserve-and-project-conversion perimeter: aggregate tons, reserve
life, downstream pull-through, public backlog, pricing, contracting, acquisitions,
capex, leverage, project claims, and dilution. Revenue, backlog, pricing, adjusted
EBITDA, guidance, and public-funding share remain diagnostic until acceptance,
collection, reserve, financing, and common-residual joins are evidenced. This is
D-367; the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Chemed hospice and service-route valuation/liquidity workbench](combined-investment-research-chemed-hospice-rotorooter-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct mixed-service perimeter: VITAS admissions, census, acuity,
Medicare Cap, clinical labor, collections, Roto-Rooter route economics, parent
allocation, debt, claims, and dilution. Admissions, census, adjusted EBITDA,
guidance, consolidated revenue, and buybacks remain diagnostic until payer,
segment, labor, collection, and common-residual joins are evidenced. This is D-366;
the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [West Pharmaceutical drug-delivery components valuation/liquidity workbench](combined-investment-research-west-pharmaceutical-drug-delivery-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct healthcare physical-interface perimeter: HVP Components, delivery
systems, customer qualification, sterile manufacturing, validation, quality,
capacity, capex, debt, claims, and dilution. Revenue growth, HVP volume, adjusted
EPS, guidance, and buybacks remain diagnostic until program-acceptance, collection,
quality-spend, capacity, and common-residual joins are evidenced. This is D-365;
the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Mueller Industries metal fabrication valuation/liquidity workbench](combined-investment-research-mueller-industries-metal-fabrication-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct fabricated-components perimeter: copper, brass, aluminum, unit
volume, price pass-through, hedges, Piping Systems, Industrial Metals, Climate,
acquisitions, capex, debt, and dilution. Revenue, price growth, operating income,
adjusted metrics, guidance, and repurchases remain diagnostic until volume, spread,
collection, hedge, acquisition-return, and common-residual joins are evidenced.
This is D-364; the lane remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [electronics distribution, working-capital financing, and channel-control valuation/liquidity workbench](combined-investment-research-arrow-electronics-distribution-financing-valuation-liquidity-workbench-2026-09-18.md)
adds Arrow Electronics as D-309, separating its thin-margin technology channel,
inventory turns, customer collection, supplier protection, receivable
securitization/factoring, financing cost, debt, and diluted common residual from
Avnet. The lane remains qualified, unranked, and owner-cash-open; completion
remains `12 of 13 proven; CA-06 partial`.

The new [accelerated-computing platform valuation/liquidity workbench](combined-investment-research-accelerated-computing-platform-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into NVIDIA's architecture/software and AI-infrastructure
control point. It keeps Data Center growth separate from product-transition
inventory, supplier commitments, customer financing, export exposure, AI-cloud
guarantees, investment gains, SBC, debt, and dilution. This is D-231; the lane
remains qualified, unranked, and owner-cash-open until same-period collection,
sell-through, partner-utilization, required-reinvestment, and common-residual
joins are evidenced. Completion remains `12 of 13 proven; CA-06 partial`.

The new [engine and power-systems valuation/liquidity workbench](combined-investment-research-engine-power-systems-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Cummins' five-segment engine, components, distribution,
power, and transition model. It keeps data-center demand separate from
warranty, emissions, inventory, receivables, Accelera charges, debt, and
dilution. This is D-232; the lane remains qualified, unranked, and
owner-cash-open until same-period service, collection, warranty, compliance,
transition-return, and common-residual joins are evidenced. Completion remains
`12 of 13 proven; CA-06 partial`.

The new [AI systems distribution and financing valuation/liquidity workbench](combined-investment-research-ai-systems-distribution-financing-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Dell's customer-facing AI systems and financing control
point. It keeps AI orders and backlog separate from hardware margin, financing
receivables, operating leases, inventory, customer credit, supplier terms,
warranty, debt, SBC, and dilution. This is D-233; the lane remains qualified,
unranked, and owner-cash-open until same-period shipment, collection, credit,
services, lease, and common-residual joins are evidenced. Completion remains
`12 of 13 proven; CA-06 partial`.

The new [oilfield-services valuation/liquidity workbench](combined-investment-research-oilfield-services-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Halliburton's service-execution and customer-capex
control point. It keeps production activity separate from service utilization,
fleet renewal, receivables, inventory, international collection, claims, debt,
and dilution. This is D-234; the lane remains qualified, unranked, and
owner-cash-open until same-period service, collection, renewal, cycle, and
common-residual joins are evidenced. Completion remains `12 of 13 proven;
CA-06 partial`.

The [mining and commodity-marketing valuation/liquidity workbench](combined-investment-research-mining-commodity-marketing-valuation-liquidity-workbench-2026-09-18.md)
extends Glencore through industrial-asset cash, Marketing Adjusted EBIT,
inventory funding, net funding, working-capital releases, copper project
capital, partner claims, leases, debt, and common-owner tests. It keeps FFO,
production, marketing earnings, asset sales, dividends, and buybacks out of
normalized owner cash until through-cycle, funding, project-return, and
per-share joins are evidenced. This is D-293; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The [regional relationship-bank valuation/liquidity workbench](combined-investment-research-regional-relationship-bank-valuation-liquidity-workbench-2026-09-18.md)
The [retirement insurance and PGIM asset-management valuation/liquidity workbench](combined-investment-research-retirement-insurance-pgim-valuation-liquidity-workbench-2026-09-18.md)
The [civil construction and materials-integration valuation/liquidity workbench](combined-investment-research-civil-materials-integration-valuation-liquidity-workbench-2026-09-18.md)
The [polyolefin feedstock and footprint-repair valuation/liquidity workbench](combined-investment-research-polyolefin-feedstock-footprint-valuation-liquidity-workbench-2026-09-18.md)
The [ETF and index asset-management valuation/liquidity workbench](combined-investment-research-etf-index-asset-management-valuation-liquidity-workbench-2026-09-18.md)
The [multi-asset gold and reserve-renewal valuation/liquidity workbench](combined-investment-research-multi-asset-gold-reserve-renewal-valuation-liquidity-workbench-2026-09-18.md)
The [iron ore, base metals, and trust-repair valuation/liquidity workbench](combined-investment-research-iron-ore-base-metals-trust-repair-valuation-liquidity-workbench-2026-09-18.md)
now extends Vale through iron-ore corridor economics, Base Metals project returns,
all-in sustaining cost, Samarco/Brumadinho and dam claims, expanded net debt, and
diluted common residual. This is D-303; the lane remains qualified, unranked, and
owner-cash-open until same-period cost, legacy-claim, project-return, and common-
residual joins are evidenced. Completion remains `12 of 13 proven; CA-06 partial`.
The [regulated water/gas and merger-funding valuation/liquidity workbench](combined-investment-research-regulated-water-gas-merger-valuation-liquidity-workbench-2026-09-18.md)
The [active and retirement asset-management valuation/liquidity workbench](combined-investment-research-active-retirement-asset-management-valuation-liquidity-workbench-2026-09-18.md)
extends T. Rowe Price through fee-paying AUM, net flows, fee rates, market
appreciation, retirement distribution, product mix, talent, technology, capital
returns, and diluted common tests. It keeps AUM, adjusted EPS, dividends, and
repurchases out of normalized common cash until fee, flow, retention, talent,
product, and per-share joins are evidenced. This is D-302; the lane remains
qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.
extends Essential through water/gas rate recovery, renewal and compliance
capital, customer contributions, collections, PFAS settlement, acquisition
cohorts, merger approval/integration, debt, dividends, and diluted common
tests. It keeps rate base, connections, settlement proceeds, OCF, and merger
scale out of normalized owner cash until recovery, collection, capital, PFAS,
merger, and per-share joins are evidenced. This is D-301; the lane remains
qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.
extends Kinross through mine-level production, grade/recovery, AISC,
sustaining/development capital, reserves, renewal projects, repatriation/tax,
reclamation, debt, buybacks, and diluted common tests. It keeps production,
FCF, impairment reversals, dividends, and capital returns out of normalized
owner cash until mid-cycle price/cost, reserve, project-return, cash-location,
and per-share joins are evidenced. This is D-300; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.
extends Invesco through fee-paying AUM, product flows, fee rates, QQQ
concentration, active/fixed-income runoff, China JV economics, private-market
marks, impairment, technology, capital returns, and diluted common tests. It
keeps AUM, adjusted earnings, market appreciation, dividends, and repurchases
out of normalized common cash until fee, flow, distribution, impairment, and
per-share joins are evidenced. This is D-299; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.
extends LyondellBasell through regional feedstock, product spreads, utilization,
plant renewal, European exits, Cash Improvement Plan savings, working capital,
JV distributions, environmental obligations, debt, and diluted common tests.
It keeps EBITDA, plan targets, OCF, asset-sale proceeds, dividends, and
repurchases out of normalized owner cash until mid-cycle, footprint, capital,
and per-share joins are evidenced. This is D-298; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.
extends Granite through CAP conversion, contract assets, retainage, project
estimates, materials integration, equipment/plant capital, acquisitions, JV/NCI
claims, convertible debt, and diluted common tests. It keeps CAP, adjusted
EBITDA, OCF, and recurring-capital residual out of normalized owner cash until
starts, final margin, collection, acquisition return, leverage, and per-share
joins are evidenced. This is D-297; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Natera precision diagnostics valuation/liquidity workbench](combined-investment-research-natera-precision-diagnostics-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct molecular-information perimeter: Signatera, Panorama, Horizon,
Prospera, payer coverage, test volume, oncology mix, evidence, laboratory capacity,
collections, debt, and dilution. Test growth, guidance, ASP, revenue, and adjusted
metrics remain diagnostic until reimbursement, assay-cost, evidence-spend, and
common-residual joins are evidenced. This is D-360; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Pure/Everpure enterprise data cloud and subscription storage valuation/liquidity workbench](combined-investment-research-pure-everpure-enterprise-data-cloud-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct governed-storage perimeter: flash, subscription ARR, RPO,
Evergreen//One, Enterprise Data Cloud, hybrid-cloud control, AI data management,
1touch integration, cloud cost, debt, and dilution. Revenue, subscription ARR,
RPO, gross margin, FCF, AI demand, and buybacks remain diagnostic until renewal,
RPO, service-cost, collection, and common-residual joins are evidenced. This is
D-359; the lane remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [Western Digital HDD, persistent storage, and data-retention infrastructure valuation/liquidity workbench](combined-investment-research-western-digital-hdd-persistent-storage-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct storage perimeter: HDD, hyperscale, persistent data, capacity,
utilization, post-Sandisk structure, inventory, manufacturing, debt, dividends,
and dilution. Revenue, capacity, exabytes, gross margin, adjusted EPS, FCF,
dividends, and buybacks remain diagnostic until capacity, utilization, product,
collection, and common-residual joins are evidenced. This is D-358; the lane
remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [TTM Technologies printed-circuit-board and advanced-interconnect valuation/liquidity workbench](combined-investment-research-ttm-technologies-pcb-interconnect-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct hardware-substrate perimeter: PCBs, substrates, RF and
microelectronics, customer qualification, backlog, book-to-bill, AI networking,
A&D programs, capacity, acquisitions, working capital, debt, and dilution. Revenue,
book-to-bill, backlog, data-center growth, adjusted EBITDA, FCF, and acquisitions
remain diagnostic until qualification, capacity, program, collection, and
common-residual joins are evidenced. This is D-357; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [American Express closed-loop membership, premium payments, and credit valuation/liquidity workbench](combined-investment-research-amex-closed-loop-membership-payments-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct payments perimeter: card members, merchants, billed business,
fees, rewards, credit, travel and dining, first-party data, agentic commerce,
funding, CET1, and dilution. Revenue, billed business, card acquisitions, fee
growth, EPS, membership, and buybacks remain diagnostic until spend, fee, rewards,
credit, capital, and common-residual joins are evidenced. This is D-356; the lane
remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Southern Copper copper, smelting, and by-product mine-system valuation/liquidity workbench](combined-investment-research-southern-copper-peru-mexico-byproduct-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct copper-system perimeter: Peru/Mexico mine cohorts, copper,
molybdenum, zinc, silver, smelting, grades, recoveries, expansion capex,
jurisdiction, debt, and dilution. Production, price, adjusted EBITDA, net cash
cost, FCF, dividends, and buybacks remain diagnostic until grade, recovery,
smelter, jurisdiction, capex, shipment, collection, and common-residual joins are
evidenced. This is D-355; the lane remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Crown Holdings rigid packaging valuation/liquidity workbench](combined-investment-research-crown-holdings-rigid-packaging-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct packaging-infrastructure perimeter: beverage, food, aerosol,
closures, tooling, volume, plant utilization, metal and energy pass-through, capex,
leverage, adjusted FCF, buybacks, and dilution. Volume, adjusted EBITDA, adjusted
EPS, adjusted FCF, guidance, and buybacks remain diagnostic until throughput,
utilization, financing, capex, and common-residual joins are evidenced. This is
D-363; the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Crown Castle tower infrastructure valuation/liquidity workbench](combined-investment-research-crown-castle-tower-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct domestic communications-infrastructure perimeter: tower billings,
carrier churn, DISH and Sprint effects, fiber and small-cell disposal, maintenance
capital, debt, REIT distributions, AFFO, sale proceeds, and dilution. AFFO,
Adjusted EBITDA, organic contribution, site counts, sale proceeds, and dividend
capacity remain diagnostic until tower-collection, capex, financing, and common-
residual joins are evidenced. This is D-361; the lane remains qualified, unranked,
and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Pool specialty distribution valuation/liquidity workbench](combined-investment-research-pool-specialty-distribution-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct branch-based wholesale perimeter: maintenance and repair mix,
branch density, supplier purchases, inventory, early buys, receivable aging,
facility borrowings, seasonal working capital, capex, debt, and dilution. Sales
growth, maintenance mix, gross profit, operating cash flow, and repurchases remain
diagnostic until product-mix, collection, financing, and common-residual joins are
evidenced. This is D-362; the lane remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Fox live sports, news, affiliate fees, and AVOD valuation/liquidity workbench](combined-investment-research-fox-live-sports-news-avod-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct national-attention perimeter: live rights, sports and news,
affiliate fees, advertising, Tubi, FOX One, Roku integration, content commitments,
debt, and dilution. Revenue, affiliate fees, advertising, adjusted EBITDA,
audience, Tubi growth, sports rights, and buybacks remain diagnostic until rights,
collection, content-cost, and common-residual joins are evidenced. This is D-354;
the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Constellation nuclear and clean-generation platform valuation/liquidity workbench](combined-investment-research-constellation-nuclear-clean-generation-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct generation perimeter: nuclear and clean fleet, PPAs, merchant
sales, Calpine integration, Crane restart, licensing, data-center co-location,
maintenance, debt, and dilution. Adjusted earnings, generation, PPAs, capacity,
data-center agreements, dividends, and buybacks remain diagnostic until fleet,
PPA, restart, collection, and common-residual joins are evidenced. This is D-353;
the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Stride online K–12, career learning, and institutional education valuation/liquidity workbench](combined-investment-research-stride-online-k12-career-learning-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct institutional-education perimeter: General Education, Career
Learning, adult and employer programs, enrollment, public funding, district
contracts, curriculum, instructional labor, regulation, impairment, debt, and
dilution. Enrollment, revenue per enrollment, Career Learning growth, adjusted
EBITDA, FCF, impairments, and buybacks remain diagnostic until funding, persistence,
contract, compliance, and common-residual joins are evidenced. This is D-352; the
lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [CBRE real-estate services and critical-infrastructure intermediation valuation/liquidity workbench](combined-investment-research-cbre-real-estate-services-critical-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct property-services perimeter: brokerage, facilities, project
management, mortgage, investment management, critical infrastructure, commissions,
subcontractors, working capital, debt, and dilution. Core EPS, FCF, critical-
infrastructure growth, AUM, transaction volume, and acquisitions remain diagnostic
until fee collection, project delivery, mortgage credit, and common-residual joins
are evidenced. This is D-351; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [AvalonBay residential apartment REIT and merger valuation/liquidity workbench](combined-investment-research-avalonbay-residential-apartment-reit-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct housing perimeter: rent collection, occupancy, concessions,
same-store NOI, development, maintenance, apartment supply, Equity Residential
merger economics, debt, dividends, and dilution. FFO, Core FFO, same-store NOI,
occupancy, rent growth, development yield, dividends, and share issuance remain
diagnostic until rent, maintenance, development, merger, and common-residual joins
are evidenced. This is D-350; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Domino's digital ordering, franchise, and supply-chain valuation/liquidity workbench](combined-investment-research-dominos-digital-ordering-franchise-supply-chain-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct restaurant-network perimeter: digital orders, franchise royalties,
supply-chain throughput, store growth, franchisee health, DPC Dash remeasurement,
debt, and dilution. Retail sales, digital penetration, store count, royalties,
supply-chain revenue, EPS, and buybacks remain diagnostic until order-flow,
franchisee, supply-chain, collection, and common-residual joins are evidenced. This
is D-349; the lane remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [Expedia travel marketplace, B2B distribution, and loyalty valuation/liquidity workbench](combined-investment-research-expedia-travel-marketplace-b2b-loyalty-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct travel-intermediary perimeter: B2C, B2B, agency, merchant,
advertising, One Key, supplier settlement, refunds, payment timing, debt, and
dilution. Gross bookings, room nights, revenue, B2B growth, advertising, adjusted
EBITDA, FCF, loyalty adoption, and buybacks remain diagnostic until supplier,
payment, refund, collection, and common-residual joins are evidenced. This is
D-348; the lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Nexstar local broadcasting, retransmission, and political-cycle valuation/liquidity workbench](combined-investment-research-nexstar-local-broadcast-retransmission-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct hybrid-media perimeter: local stations, retransmission, political
and non-political advertising, NewsNation, The CW, TEGNA integration, programming,
debt, audience, and dilution. Revenue, distribution, advertising, ratings,
adjusted EBITDA, political advertising, and buybacks remain diagnostic until
carriage, ad-collection, political-normalization, and common-residual joins are
evidenced. This is D-347; the lane remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Bath & Body Works specialty retail, loyalty, and brand-repair valuation/liquidity workbench](combined-investment-research-bath-body-works-specialty-retail-brand-repair-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct repair-oriented retail perimeter: stores, direct, international,
loyalty, product, inventory, markdowns, seasonal demand, Consumer First Formula,
debt, and dilution. Sales, loyalty members, store count, adjusted EPS, settlement
benefits, and buybacks remain diagnostic until sell-through, inventory, collection,
and common-residual joins are evidenced. This is D-346; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Pan American Silver silver-weighted mine portfolio and acquisition valuation/liquidity workbench](combined-investment-research-pan-american-silver-mine-portfolio-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct precious-metals perimeter: silver, gold, mine cohorts, Juanicipio,
reserve and grade, sustaining and growth capex, jurisdiction, debt, dividends, and
dilution. Production, attributable revenue, adjusted earnings, AISC, FCF, dividends,
and buybacks remain diagnostic until mine-cohort, capex, reserve, shipment,
collection, and common-residual joins are evidenced. This is D-345; the lane remains
qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Clearwater Paper paperboard packaging and mill-cycle valuation/liquidity workbench](combined-investment-research-clearwater-paperboard-packaging-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct materials perimeter: SBS price and volume, mill operating rates,
outages, fiber and energy, restructuring, tissue divestiture, working capital,
liquidity, debt, and dilution. Volumes, pricing, adjusted EBITDA, cost savings,
guidance, buybacks, and impairment remain diagnostic until mill-cycle, maintenance,
shipment, collection, and common-residual joins are evidenced. This is D-344; the
lane remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [U.S. Bancorp diversified payments and fee-bank valuation/liquidity workbench](combined-investment-research-us-bancorp-payments-fee-bank-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct financial-utility perimeter: deposits, loans, payments, treasury,
trust, fee revenue, credit losses, reserves, CET1, liquidity, technology, dividends,
and dilution. NII, net revenue, fee growth, EPS, adjusted earnings, and buybacks
remain diagnostic until deposit, credit, capital, and common-residual joins are
evidenced. This is D-343; the lane remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Criteo commerce media and AI shopping-interface valuation/liquidity workbench](combined-investment-research-criteo-commerce-media-ai-shopping-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct transaction-adjacent attention perimeter: retail media, retailer and
brand settlement, contribution ex-TAC, client concentration, AI shopping interfaces,
measurement, debt, and dilution. Revenue, media spend, contribution ex-TAC, adjusted
EBITDA, FCF, and AI partnerships remain diagnostic until campaign billing, collection,
conversion, and common-residual joins are evidenced. This is D-342; the lane remains
qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Playtika mobile gaming, live-ops, and direct-billing valuation/liquidity workbench](combined-investment-research-playtika-mobile-gaming-live-ops-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct digital-participation perimeter: title cohorts, payers, DTC
collections, platform fees, live ops, SuperPlay integration and earnout, marketing,
debt, and dilution. Revenue, DTC mix, payer metrics, adjusted EBITDA, earnout
remeasurement, and buybacks remain diagnostic until title, payer, earnout, billing,
and common-residual joins are evidenced. This is D-341; the lane remains qualified,
unranked, and owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Outbrain/Teads open-internet, CTV, and advertising middleware valuation/liquidity workbench](combined-investment-research-teads-open-internet-ctv-adtech-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct attention-infrastructure perimeter: advertiser and publisher
settlement, TAC, CTV, measurement, ex-TAC gross profit, integration, bridge debt,
impairment, restructuring, and dilution. Revenue, ex-TAC gross profit, CTV growth,
adjusted EBITDA, adjusted FCF, and synergies remain diagnostic until settlement,
collection, and common-residual joins are evidenced. This is D-340; the lane
remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Viasat satellite connectivity and orbital infrastructure valuation/liquidity workbench](combined-investment-research-viasat-satellite-connectivity-orbital-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct physical-connectivity perimeter: aviation, maritime, government and
defense, fixed broadband, satellites, spectrum, launch, service entry, backlog, RPO,
leverage, capex, debt, and dilution. Revenue, backlog, RPO, adjusted EBITDA,
endpoints, subscribers, and FCF remain diagnostic until fleet, service-entry,
collection, and common-residual joins are evidenced. This is D-339; the lane
remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Coursera learning marketplace and human-capital platform valuation/liquidity workbench](combined-investment-research-coursera-learning-marketplace-human-capital-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct education-platform perimeter: Consumer, Enterprise, degree and
partner economics, learners, subscribers, NRR, Udemy integration, AI delivery,
synergies, working capital, debt, and dilution. Learner counts, revenue, adjusted
EBITDA, FCF, synergies, and buybacks remain diagnostic until retention, collection,
integration, and common-residual joins are evidenced. This is D-338; the lane
remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [VeriSign DNS registry control and internet infrastructure valuation/liquidity workbench](combined-investment-research-verisign-dns-registry-control-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct digital-control-point perimeter: `.com/.net` contracts, domain
cohorts, renewals, pricing, deferred revenue, DNS uptime, cybersecurity, governance,
carrier commitments, debt, and dilution. Domain counts, OCF, FCF, and buybacks
remain diagnostic until registrar-remittance, continuity, and common-residual joins
are evidenced. This is D-337; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [CACI defense mission systems and federal technology valuation/liquidity workbench](combined-investment-research-caci-defense-mission-systems-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct federal-technology perimeter: mission software, electronic warfare,
space sensing, awards, backlog, funded backlog, cleared labor, ARKA integration,
working capital, debt, and dilution. Awards, backlog, EBITDA, adjusted EPS, and
FCF remain diagnostic until program-conversion, collection, and common-residual
joins are evidenced. This is D-336; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [Live Nation live-events, ticketing, and sponsorship valuation/liquidity workbench](combined-investment-research-live-nation-live-events-ticketing-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct experience-economy perimeter: concerts, Ticketmaster, sponsorship,
attendance, deferred revenue, artist and promoter settlement, venue investment,
legal accruals, debt, and dilution. Revenue, AOI, attendance, tickets, GTV, and
deferred revenue remain diagnostic until settlement and common-residual joins are
evidenced. This is D-335; the lane remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.
extends Prudential through policyholder claims, reserves, investment spread,
PGIM flows and fee rates, statutory capital, subsidiary remittances, parent
liquidity, debt, and diluted common tests. It keeps adjusted operating income,
AUM, book value, dividends, and repurchases out of normalized common return
until liability, capital-transfer, parent-liquidity, and per-share joins are
evidenced. This is D-296; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.
extends M&T through deposit beta, NIM normalization, commercial and CRE credit,
reserves, securities liquidity, treasury/payment investment, CET1, capital
returns, and diluted common tests. It keeps EPS, deposits, loan growth, NIM,
ROTCE, dividends, and repurchases out of normalized common return until
funding, credit, liquidity, capital, technology, and per-share joins are
evidenced. This is D-295; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [luxury home and destination retail valuation/liquidity workbench](combined-investment-research-luxury-home-destination-retail-valuation-liquidity-workbench-2026-09-18.md)
extends RH through order formation, product conversion, inventory aging,
galleries, design services, hospitality, housing sensitivity, leases, debt,
stock compensation, and diluted common tests. It keeps demand, revenue,
adjusted earnings, OCF, and buybacks out of normalized owner cash until order-
conversion, inventory, gallery-return, hospitality, maintenance, and residual
joins are evidenced. This is D-294; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [database and cloud-infrastructure valuation/liquidity workbench](combined-investment-research-database-cloud-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
The new [enterprise software, AI capacity, and owner-cash valuation/liquidity workbench](combined-investment-research-microsoft-ai-capacity-owner-cash-valuation-liquidity-workbench-2026-09-18.md)
adds Microsoft as D-304, extending the audit through software renewal, Azure
utilization, Copilot conversion, RPO collection, capacity capital, serving cost,
SBC, investment gains, and diluted common residual. The lane remains qualified,
unranked, and owner-cash-open; completion remains `12 of 13 proven; CA-06 partial`.
extends the goal into Oracle's installed-database and financed-cloud control
point. It keeps RPO and cloud revenue separate from customer prepayments,
customer-supplied hardware, capex, depreciation, debt, leases, preferred
claims, SBC, and dilution. This is D-235; the lane remains qualified,
unranked, and owner-cash-open until same-period utilization, delivery, margin,
financing, replacement, and common-residual joins are evidenced. Completion
remains `12 of 13 proven; CA-06 partial`.

The new [generation and grid equipment valuation/liquidity workbench](combined-investment-research-generation-grid-equipment-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into GE Vernova's equipment and installed-service control
point. It keeps RPO and deposits separate from project margin, contract
liabilities, inventory, Prolec GE integration, wind losses, warranty, pensions,
debt, and dilution. This is D-236; the lane remains qualified, unranked, and
owner-cash-open until same-period project, service, collection,
acquisition-return, and common-residual joins are evidenced. Completion remains
`12 of 13 proven; CA-06 partial`.

The new [life insurance and retirement-capital valuation/liquidity workbench](combined-investment-research-life-insurance-retirement-capital-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into MetLife's long-duration liability and regulated-capital
control point. It keeps adjusted earnings and investment income separate from
policyholder benefits, reserves, reinsurance, statutory capital, subsidiary
dividends, holding-company cash, debt, and dilution. This is D-237; the lane
remains qualified, unranked, and owner-cash-open until same-period liability,
capital, distribution, and common-residual joins are evidenced. Completion
remains `12 of 13 proven; CA-06 partial`.

The new [environmental and process equipment valuation/liquidity workbench](combined-investment-research-environmental-process-equipment-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into CECO's engineered project and compliance control point.
It keeps backlog and adjusted EBITDA separate from GAAP cash conversion,
contract assets, inventory, project acceptance, Thermon integration,
divestiture gains, debt, SBC, and dilution. This is D-238; the lane remains
qualified, unranked, and owner-cash-open until same-period project, collection,
integration-return, and common-residual joins are evidenced. Completion remains
`12 of 13 proven; CA-06 partial`.

The new [permanent-capital conglomerate valuation/liquidity workbench](combined-investment-research-permanent-capital-conglomerate-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Berkshire Hathaway's look-through capital-allocation
control point. It keeps operating earnings and float separate from claims,
railroad and utility renewal, regulated capital, subsidiary cash, parent
liquidity, acquisitions, taxes, debt, and dilution. This is D-239; the lane
remains qualified, unranked, and owner-cash-open until same-period segment
capital, remittance, allocation-return, and common-residual joins are evidenced.
Completion remains `12 of 13 proven; CA-06 partial`.

The new [diversified clinical-products valuation/liquidity workbench](combined-investment-research-diversified-clinical-products-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Abbott's multi-segment clinical-products control point.
It keeps sales and adjusted EPS separate from segment utilization,
reimbursement, instrument placement, Exact Sciences acquisition return,
integration, amortization, quality, debt, SBC, and dilution. This is D-240; the
lane remains qualified, unranked, and owner-cash-open until same-period segment,
acquired-return, reimbursement, collection, and common-residual joins are
evidenced. Completion remains `12 of 13 proven; CA-06 partial`.

The new [hospital consumables and infusion valuation/liquidity workbench](combined-investment-research-hospital-consumables-infusion-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Baxter's post-divestiture hospital-supply control point.
It keeps sales and adjusted EPS separate from product holds, quality
remediation, inventory, working capital, Kidney Care proceeds, stranded costs,
debt, leases, and dilution. This is D-241; the lane remains qualified,
unranked, and owner-cash-open until same-period quality, collection, debt,
post-separation, and common-residual joins are evidenced. Completion remains
`12 of 13 proven; CA-06 partial`.

The new [infrastructure engineering and program-management valuation/liquidity workbench](combined-investment-research-infrastructure-engineering-program-management-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Jacobs' technical-design and program-management control
point. It keeps gross backlog and adjusted EBITDA separate from pass-through
revenue, adjusted-net conversion, project margin, contract assets, receivables,
PA acquisition return, employee consideration, debt, SBC, and dilution. This is
D-242; the lane remains qualified, unranked, and owner-cash-open until
same-period project, collection, acquisition-return, and common-residual joins
are evidenced. Completion remains `12 of 13 proven; CA-06 partial`.

The new [integrated commerce and cloud platform valuation/liquidity workbench](combined-investment-research-integrated-commerce-cloud-platform-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Amazon's shared commerce, fulfillment, advertising,
subscription, and AWS control point. It keeps AWS profit and OCF separate from
full capex and lease burden, inventory/payables timing, seller settlements,
labor, legal claims, debt, SBC, and dilution. This is D-243; the lane remains
qualified, unranked, and owner-cash-open until same-period full-capital-return,
working-capital, lease, and common-residual joins are evidenced. Completion
remains `12 of 13 proven; CA-06 partial`.

The new [global technology-services valuation/liquidity workbench](combined-investment-research-global-technology-services-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Accenture's global implementation and managed-services
control point. It keeps bookings and adjusted margin separate from delivery,
utilization, labor/training, renewal, receivables, deferred revenue,
acquisition return, optimization cost, SBC, and dilution. This is D-244; the
lane remains qualified, unranked, and owner-cash-open until same-period
delivery, collection, labor, renewal, acquisition-return, and common-residual
joins are evidenced. Completion remains `12 of 13 proven; CA-06 partial`.

The new [power-management and aerospace-systems valuation/liquidity workbench](combined-investment-research-power-management-aerospace-systems-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Eaton's diversified electrical and aerospace control
point. It keeps orders, backlog, and adjusted EPS separate from billed
collection, unbilled receivables, inventory, acquisition cohorts, PP&E,
Mobility separation costs, debt, capital returns, SBC, and dilution. This is
D-245; the lane remains qualified, unranked, and owner-cash-open until
same-period billed cash, acquisition-return, separation, debt, and common-
residual joins are evidenced. Completion remains `12 of 13 proven; CA-06
partial`.

The new [senior-living operator valuation/liquidity workbench](combined-investment-research-senior-living-operator-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Brookdale's community-operator control point. It keeps
occupancy, RevPAR, and adjusted EBITDA separate from resident affordability,
care labor, agency staffing, leases, maintenance and life-safety capital,
quality, debt, and dilution. This is D-246; the lane remains qualified,
unranked, and owner-cash-open until same-period community contribution,
staffing, property cash, lease, quality, and common-residual joins are
evidenced. Completion remains `12 of 13 proven; CA-06 partial`.

The new [search, advertising, and cloud platform valuation/liquidity workbench](combined-investment-research-search-advertising-cloud-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Alphabet's Search/YouTube and Cloud control point. It
keeps operating income and ad growth separate from traffic acquisition, AI query
cost, Cloud utilization, extreme capex, shared AI research, Other Bets,
regulation, SBC, and dilution. This is D-247; the lane remains qualified,
unranked, and owner-cash-open until same-period incremental-return, legal,
capex, and common-residual joins are evidenced. Completion remains `12 of 13
proven; CA-06 partial`.

The new [enterprise security platform valuation/liquidity workbench](combined-investment-research-enterprise-security-platform-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Palo Alto Networks' security-consolidation control point.
It keeps ARR, RPO, and subscription mix separate from organic retention,
cross-sell, hosting/support cost, threat research, CyberArk/Chronosphere
integration, customer credits, remediation, SBC, and dilution. This is D-248;
the lane remains qualified, unranked, and owner-cash-open until same-period
organic, collection, integration-return, incident, and common-residual joins
are evidenced. Completion remains `12 of 13 proven; CA-06 partial`.

The new [data-cloud consumption valuation/liquidity workbench](combined-investment-research-data-cloud-consumption-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Snowflake's governed data-control and consumption model.
It keeps product revenue, NRR, RPO, and prepaid capacity separate from
cloud/GPU/inference cost, capitalized software, deferred commissions, SBC, and
dilution. This is D-249; the lane remains qualified, unranked, and
owner-cash-open until same-period usage, delivery-margin, collection, and
common-residual joins are evidenced.

The new [infrastructure design and program-management valuation/liquidity workbench](combined-investment-research-infrastructure-design-program-management-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into AECOM's fee-bearing infrastructure model. It keeps
adjusted NSR separate from gross/pass-through revenue and backlog, and tests
project estimates, receivables, contract assets, claims, regional collection,
acquisitions, joint ventures, debt, and dilution. This is D-263; the lane
remains qualified, unranked, and owner-cash-open until same-period
project-conversion and common-residual joins are evidenced.

The new [thrift-to-business-bank valuation/liquidity workbench](combined-investment-research-thrift-to-business-bank-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into WaFd's deposit-funded transition. It keeps transaction
deposits, borrowings, business banking, legacy real-estate credit, reserves,
NIM, efficiency, capital, liquidity, tangible value, and repurchases distinct.
This is D-264; the lane remains qualified, unranked, and owner-cash-open until
same-period deposit-credit-capital and common-residual joins are evidenced.

The new [public-market asset-management valuation/liquidity workbench](combined-investment-research-public-market-asset-management-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Franklin Resources' fee-paying product platform. It
keeps legacy active, ETF/SMA, alternatives, Western Asset, market appreciation,
flows, fee rates, talent, distribution, remediation, technology, debt, and
dilution distinct. This is D-265; the lane remains qualified, unranked, and
owner-cash-open until same-period fee-paying-flow and common-residual joins are
evidenced.

The new [field-execution digital-infrastructure valuation/liquidity workbench](combined-investment-research-field-execution-digital-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Dycom's downstream execution model. It keeps MSA and
firm backlog, customer concentration, crews, equipment, receivables, contract
assets, insurance, surety, Power Solutions integration, debt, and dilution
distinct. This is D-266; the lane remains qualified, unranked, and
owner-cash-open until same-period funded-start, collection, acquisition-return,
and common-residual joins are evidenced.

The new [wildfire-liability regulated-utility valuation/liquidity workbench](combined-investment-research-wildfire-liability-regulated-utility-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Edison International's catastrophe-exposed utility
model. It keeps placed-in-service rate base, resilience capex, wildfire claims,
insurance/Wildfire Fund cash, regulatory assets, securitization, affordability,
debt, preferred claims, and dilution distinct. This is D-267; the lane remains
qualified, unranked, and owner-cash-open until same-period recovery,
catastrophe-liquidity, and common-residual joins are evidenced.

The new [custom silicon and optical-interconnect valuation/liquidity workbench](combined-investment-research-custom-silicon-optical-interconnect-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Marvell's design-win-to-shipment model. It keeps custom
compute, optics, switching, qualification, customer concentration, inventory,
R&D, Celestial AI integration, debt, SBC, and dilution distinct. This is D-268;
the lane remains qualified, unranked, and owner-cash-open until same-period
volume, acceptance, collection, acquisition-return, and common-residual joins
are evidenced.

The new [royalty and streaming valuation/liquidity workbench](combined-investment-research-royalty-streaming-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Franco-Nevada's contractual resource model. It keeps
producing, development, and optionality cohorts, GEOs, commodity mix, operator
production/payment, counterparty and permitting risk, Cobre Panama,
acquisitions, taxes, dividends, and dilution distinct. This is D-269; the lane
remains qualified, unranked, and owner-cash-open until same-period asset-level
production, payment, acquisition-return, and common-residual joins are
evidenced.

The new [security trust and trust-recovery valuation/liquidity workbench](combined-investment-research-security-trust-recovery-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into CrowdStrike's security-control model. It keeps endpoint,
cloud, identity, and data telemetry, renewal, module expansion, deferred
revenue, cloud/AI cost, incident/remediation, SBC, acquisitions, and dilution
distinct. This is D-270; the lane remains qualified, unranked, and
owner-cash-open until same-period retention, incident, and common-residual
joins are evidenced.

The new [hotel property-owner valuation/liquidity workbench](combined-investment-research-hotel-property-owner-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Apple Hospitality's physical hotel model. It keeps room
inventory, occupancy, ADR, RevPAR, property EBITDA, management/brand fees,
labor, insurance, renovation, dispositions, debt, REIT obligations, and
dilution distinct. This is D-271; the lane remains qualified, unranked, and
owner-cash-open until same-period property-margin, replacement-capital,
fixed-charge, and common-residual joins are evidenced.

The new [healthcare middle-layer and delegated-risk valuation/liquidity workbench](combined-investment-research-healthcare-middle-layer-delegated-risk-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Astrana's provider/payer coordination model. It keeps
Care Partners, Care Delivery, Care Enablement, retained margin per patient,
medical cost, claims, provider payments, subsidiary capital, Prospect
integration, debt, and dilution distinct. This is D-272; the lane remains
qualified, unranked, and owner-cash-open until same-period retained-margin,
delegated-risk, collection, and common-residual joins are evidenced.

The new [lifestyle retail and inventory-cash valuation/liquidity workbench](combined-investment-research-lifestyle-retail-inventory-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Williams-Sonoma's multi-brand design-led retail model. It
keeps transactions, repeat demand, brand/channel mix, inventory turns,
markdowns, tariffs, freight, vendor terms, stores, e-commerce, services,
leases, buybacks, and dilution distinct. This is D-273; the lane remains
qualified, unranked, and owner-cash-open until same-period inventory-cash,
service-contribution, and common-residual joins are evidenced.

The new [single-asset gold mine valuation/liquidity workbench](combined-investment-research-single-asset-gold-mine-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Lundin Gold's concentrated Fruta del Norte operating
mine. It keeps production, realized gold price, grade/recovery, AISC, taxes,
profit sharing, sustaining/development capital, reserve/mine life, Ecuador,
district options, dividends, and dilution distinct. This is D-274; the lane
remains qualified, unranked, and owner-cash-open until same-period production-
cost, renewal-capital, country, reserve, and common-residual joins are evidenced.

The new [travel distribution and payments valuation/liquidity workbench](combined-investment-research-travel-distribution-payments-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Booking Holdings' travel-interface model. It keeps
agency/merchant mix, supplier settlement, payments, refunds, fraud, marketing,
support, direct/app/loyalty, Connected Trip, debt, SBC, and dilution distinct.
This is D-275; the lane remains qualified, unranked, and owner-cash-open until
same-period retained-contribution, settlement, customer-acquisition, and
common-residual joins are evidenced.

The new [diversified mining and commodity portfolio valuation/liquidity workbench](combined-investment-research-diversified-mining-commodity-portfolio-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into BHP's copper-centered diversified mining model. It keeps
asset-level price/volume/grade/cost, sustaining and growth capital, ownership,
JV and non-controlling cash, Samarco, closure, debt, dividends, and dilution
distinct. This is D-276; the lane remains qualified, unranked, and owner-cash-
open until same-period asset-level return, ownership-adjusted cash, project-
capital, claim, and common-residual joins are evidenced.

The new [pharma and MedTech portfolio-renewal valuation/liquidity workbench](combined-investment-research-pharma-medtech-portfolio-renewal-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Johnson & Johnson's two-engine healthcare portfolio. It
keeps product lifecycle, patent/exclusivity, pipeline, internal and acquired
R&D, MedTech procedure and quality economics, litigation, working capital,
debt, dividends, and dilution distinct. This is D-277; the lane remains
qualified, unranked, and owner-cash-open until same-period portfolio-renewal,
litigation-cash, and common-residual joins are evidenced.

The new [LNG liquefaction and export infrastructure valuation/liquidity workbench](combined-investment-research-lng-liquefaction-export-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Cheniere's train-level export model. It keeps contracted
and merchant volumes, train availability, feedgas, derivative cash and marks,
maintenance and growth capital, Stage 3, counterparties, debt, buybacks, and
dilution distinct. This is D-278; the lane remains qualified, unranked, and
owner-cash-open until same-period train-return, capital-cycle, settlement, and
common-residual joins are evidenced.

The new [edge network and application-security valuation/liquidity workbench](combined-investment-research-edge-network-application-security-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Cloudflare's distributed network-control model. It keeps
retention, RPO conversion, traffic/workload, network cost, platform attachment,
support, restructuring, SBC, leases, debt, and dilution distinct. This is
D-279; the lane remains qualified, unranked, and owner-cash-open until
same-period network-return, margin, conversion, and diluted common-residual
joins are evidenced.

The new [installed network and subscription-platform valuation/liquidity workbench](combined-investment-research-installed-network-subscription-platform-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Cisco's mature enterprise network platform. It keeps
installed-base renewal, subscription/RPO delivery, AI-order shipment, hardware
and software mix, inventory, receivables, Splunk integration, support, SBC,
debt, and dilution distinct. This is D-280; the lane remains qualified,
unranked, and owner-cash-open until same-period shipment, subscription,
acquisition-return, and common-residual joins are evidenced.

The new [upstream shale and resource-play valuation/liquidity workbench](combined-investment-research-upstream-shale-resource-play-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into EOG Resources' basin-level upstream model. It keeps
product mix, realized price, decline, drilling, reserve replacement, gathering,
impairments, environmental obligations, SBC, dividends, and dilution distinct.
This is D-281; the lane remains qualified, unranked, and owner-cash-open until
same-period mid-cycle, reserve-renewal, infrastructure, and common-residual
joins are evidenced.

The new [data-center power and thermal systems valuation/liquidity workbench](combined-investment-research-data-center-power-thermal-systems-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Vertiv's physical deployment and uptime model. It keeps
backlog shipment, project margin, working capital, product/service mix,
warranty, service labor, capacity, PurgeRite return, debt, SBC, and dilution
distinct. This is D-282; the lane remains qualified, unranked, and
owner-cash-open until same-period backlog-conversion, capacity-return, and
common-residual joins are evidenced.

The new [Forrester research and AI-transition valuation/liquidity workbench](combined-investment-research-forrester-research-ai-transition-valuation-liquidity-workbench-2026-09-18.md)
extends the institutional-research lane with a negative-transition case beside
Gartner. It keeps contract value, renewals, billings, deferred revenue,
research, consulting, events, AI delivery, goodwill impairment, restructuring,
office capital, debt, SBC, and dilution distinct. This is D-283; the lane
remains qualified, unranked, and owner-cash-open until same-period contract-
stabilization, AI-return, liquidity, and common-residual joins are evidenced.

The new [heavy equipment, dealer channel, and finance valuation/liquidity workbench](combined-investment-research-heavy-equipment-dealer-finance-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Caterpillar's machine ecosystem. It keeps backlog,
equipment and service mix, dealer inventory, Cat Financial receivables, credit
losses, warranty, tariffs, capex, debt, SBC, and dilution distinct. This is
D-284; the lane remains qualified, unranked, and owner-cash-open until
same-period end-user conversion, dealer-health, finance-credit, cycle, and
common-residual joins are evidenced.

The new [focused copper mine and smelter valuation/liquidity workbench](combined-investment-research-focused-copper-mine-smelter-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Freeport-McMoRan's copper-focused mine and processing
model. It keeps grade/recovery, byproduct credits, Grasberg restart, smelter
conversion, operating rights, Indonesia cash restrictions, environmental and
project capital, debt, dividends, and dilution distinct. This is D-285; the
lane remains qualified, unranked, and owner-cash-open until same-period
full-cost, restart, operating-rights, and common-residual joins are evidenced.

The new [deposit franchise and consumer-credit valuation/liquidity workbench](combined-investment-research-deposit-franchise-consumer-credit-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Bank of America's money-center bank model. It keeps
deposits and beta, funding, loans, credit migration, reserves, charge-offs,
markets, technology/control costs, liquidity, CET1, stress capital, dividends,
and dilution distinct. This is D-286; the lane remains qualified, unranked,
and owner-cash-open until same-period risk-adjusted common-return, credit,
funding, capital, and per-share joins are evidenced.

The new [diversified gold producer and portfolio-renewal valuation/liquidity workbench](combined-investment-research-diversified-gold-producer-portfolio-renewal-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Newmont's mine-portfolio model. It keeps mine-level
production, grade/recovery, byproducts, sustaining and growth capital, project
returns, reserves, closure, divestitures, host-country terms, debt, dividends,
and dilution distinct. This is D-287; the lane remains qualified, unranked,
and owner-cash-open until same-period full-cycle, portfolio-renewal, closure,
and common-residual joins are evidenced.

The new [global transaction-bank turnaround valuation/liquidity workbench](combined-investment-research-global-transaction-bank-turnaround-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Citigroup's global institutional-network model. It keeps
Services, Markets, Banking, Wealth, USCC cards, control and technology cost,
credit, divestiture residuals, liquidity, CET1, stress capital, dividends, and
dilution distinct. This is D-288; the lane remains qualified, unranked, and
owner-cash-open until same-period turnaround, control-cost, credit, capital,
and common-residual joins are evidenced.

The new [regional regulated utility and large-load valuation/liquidity workbench](combined-investment-research-regional-regulated-utility-large-load-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Alliant Energy's regional regulated franchise. It keeps
energized load, customer funding, construction, in-service recovery, allowed
versus earned return, affordability, debt/equity, storm/environmental cash,
dividends, and dilution distinct. This is D-289; the lane remains qualified,
unranked, and owner-cash-open until same-period project-recovery, financing,
affordability, and common-residual joins are evidenced.

The new [procedure-led MedTech acquisition and lifecycle valuation/liquidity workbench](combined-investment-research-procedure-medtech-acquisition-lifecycle-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Boston Scientific's cardiovascular and MedSurg portfolio.
It keeps procedure adoption, reimbursement, price/mix, clinical quality, R&D,
acquisition-return, inventory, receivables, debt, SBC, and dilution distinct.
This is D-290; the lane remains qualified, unranked, and owner-cash-open until
same-period lifecycle, quality, acquisition-return, and common-residual joins
are evidenced.

The new [semiconductor materials-engineering valuation/liquidity workbench](combined-investment-research-semiconductor-materials-engineering-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Applied Materials' qualified-process and installed-
service model. It keeps tool acceptance, AGS attachment, contract-liability
conversion, inventory, foundry/memory mix, China/export, R&D, facility capex,
customer concentration, SBC, and dilution distinct. This is D-291; the lane
remains qualified, unranked, and owner-cash-open until same-period process,
service, export, concentration, and common-residual joins are evidenced.

The [waterworks and municipal distribution valuation/liquidity workbench](combined-investment-research-waterworks-municipal-distribution-valuation-liquidity-workbench-2026-09-18.md)
extends Core & Main through project timing, branch density, inventory,
supplier rebates, acquisitions, greenfields, TRA, NCI, debt, and Class A cash
tests. It keeps sales, adjusted EBITDA, OCF, and repurchases out of normalized
owner cash until inventory, collection, acquisition-return, ownership-claim,
and diluted residual joins are evidenced. This is D-292; the lane remains
qualified, unranked, and owner-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The new [engineered materials and acetyl-chain valuation/liquidity workbench](combined-investment-research-engineered-materials-acetyl-chain-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Celanese's Engineered Materials and Acetyl Chain model.
It keeps adjusted EBITDA and adjusted EPS separate from segment price/volume/
mix, qualification, utilization, closure and environmental cash, working
capital, restructuring, goodwill, refinancing, debt, and dilution. This is
D-251; the lane remains qualified, unranked, and owner-cash-open until
same-period mid-cycle margin, closure, debt, and common-residual joins are
evidenced.

The new [home medical equipment and recurring-resupply valuation/liquidity workbench](combined-investment-research-home-medical-equipment-resupply-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into AdaptHealth's home-continuity and resupply model. It
keeps patient count and organic revenue separate from active resupply, paid
claims, payer authorization, capitated utilization, delivery and field service,
inventory, receivables, goodwill, divestiture, debt, and dilution. This is
D-254; the lane remains qualified, unranked, and owner-cash-open until
same-period resupply, contract, collection, impairment, and common-residual
joins are evidenced.

The new [custom electrical systems and project-conversion valuation/liquidity workbench](combined-investment-research-custom-electrical-systems-project-conversion-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Powell Industries' custom electrical-system model. It
keeps bookings and backlog separate from project margin, milestone billing,
contract assets and liabilities, receivables, fixed-price execution, warranty,
end-market mix, facility expansion, letters of credit, acquisitions, and
dilution. This is D-255; the lane remains qualified, unranked, and
owner-cash-open until same-period conversion, collection, capacity-return, and
common-residual joins are evidenced.

The new [AI underwriting and lending-marketplace valuation/liquidity workbench](combined-investment-research-ai-underwriting-lending-marketplace-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Upstart's partner-funded underwriting model. It keeps
originations and automation separate from funded-loan quality, partner capital,
fee rates, loan-sale terms, retained exposure, repurchase and indemnity claims,
fair-lending compliance, technology cost, SBC, and dilution. This is D-256; the
lane remains qualified, unranked, and owner-cash-open until same-period credit,
funding, collection, and common-residual joins are evidenced.

The new [local-commerce delivery marketplace valuation/liquidity workbench](combined-investment-research-local-commerce-delivery-marketplace-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into DoorDash's consumer-merchant-Dasher model. It keeps GOV,
orders, members, and advertising separate from retained contribution per order,
merchant and Dasher health, delivery labor, refunds, insurance, regulatory cost,
Deliveroo integration, capitalized software, SBC, processor funds, and dilution.
This is D-257; the lane remains qualified, unranked, and owner-cash-open until
same-period contribution, settlement, integration, and common-residual joins
are evidenced.

The new [refining, renewable fuels, and specialty-products valuation/liquidity workbench](combined-investment-research-refining-specialty-products-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into HF Sinclair's downstream model. It keeps refining
earnings and credits separate from crack spreads, utilization, turnarounds,
inventory valuation, derivative settlement, renewable policy, specialty cash,
separation costs, environmental obligations, debt, and dilution. This is
D-258; the lane remains qualified, unranked, and owner-cash-open until
same-period mid-cycle, settlement, separation, and common-residual joins are
evidenced.

The new [custom silicon and infrastructure-software valuation/liquidity workbench](combined-investment-research-custom-silicon-infrastructure-software-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Broadcom's custom-ASIC and software model. It keeps AI
and software revenue separate from design-in durability, customer concentration,
renewal and migration, supplier commitments, acquisition integration, debt,
acquisition amortization, SBC, and dilution. This is D-259; the lane remains
qualified, unranked, and owner-cash-open until same-period design-win, renewal,
acquisition-return, and common-residual joins are evidenced.

The new [regulated electric/gas rate-base valuation/liquidity workbench](combined-investment-research-regulated-electric-gas-rate-base-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Fortis's multi-jurisdiction regulated-utility model. It
keeps planned rate base and capex separate from placed-in-service recovery,
allowed returns, regulatory lag, project approval, financing, affordability,
storm/wildfire, currency, subsidiary capital, debt, dividends, and dilution.
This is D-260; the lane remains qualified, unranked, and owner-cash-open until
same-period recovery, earned-return, financing, and common-residual joins are
evidenced.

The new [packaged meals and snacks valuation/liquidity workbench](combined-investment-research-packaged-meals-snacks-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into The Campbell's Company's packaged-food model. It keeps
Meals & Beverages and Snacks separate from in-market volume, retailer shelf and
trade promotion, price/volume/mix, ingredients, packaging, freight, brand
investment, Rao's/Sovos return, inventory, debt, and dilution. This is D-261;
the lane remains qualified, unranked, and owner-cash-open until same-period
volume, margin, portfolio-return, and common-residual joins are evidenced.

The new [full-service dining direct-operator valuation/liquidity workbench](combined-investment-research-full-service-dining-direct-operator-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Darden's company-operated restaurant system. It keeps
traffic, price/mix, food, labor, occupancy, maintenance/remodel capital,
new-unit returns, Chuy's integration, leases, debt, and dilution distinct from
franchise royalties. This is D-262; the lane remains qualified, unranked, and
owner-cash-open until same-period traffic, unit-return, capital, lease, and
common-residual joins are evidenced.

The new [integrated midstream hydrocarbon-logistics valuation/liquidity workbench](combined-investment-research-integrated-midstream-hydrocarbon-logistics-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into ONEOK's integrated midstream control point. It keeps
throughput and adjusted EBITDA separate from organic/acquired volume,
maintenance and growth capex, affiliate distributions, commodity-linked
optimization, working capital, debt, project utilization, and dilution. This
is D-250; the lane remains qualified, unranked, and owner-cash-open until
same-period collected cash, project-return, affiliate-cash, leverage, and
common-residual joins are evidenced.

The new [specialty underwriting, float, and decentralized-capital valuation/liquidity workbench](combined-investment-research-specialty-underwriting-float-conglomerate-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Markel's specialty-insurance and operating-company
capital-allocation model. It keeps premiums and combined ratio separate from
current-year losses, reserve development, catastrophe and reinsurance exposure,
invested-asset liquidity, subsidiary capital, operating-company returns, parent
debt, and dilution. This is D-252; the lane remains qualified, unranked, and
owner-cash-open until same-period reserve, recovery, asset-liquidity,
subsidiary-capital, and common-residual joins are evidenced.

The new [semiconductor deposition, etch, and installed-service valuation/liquidity workbench](combined-investment-research-semiconductor-deposition-etch-service-valuation-liquidity-workbench-2026-09-18.md)
extends the goal into Lam Research's process-equipment and installed-service
model. It keeps systems and support revenue separate from customer acceptance,
deferred revenue, Japan-held inventory, customer concentration, China/export
exposure, R&D, labs, supplier commitments, capacity, SBC, and dilution. This is
D-253; the lane remains qualified, unranked, and owner-cash-open until
same-period acceptance, reinvestment, policy, and common-residual joins are
evidenced.

The [healthcare distribution valuation/liquidity workbench](combined-investment-research-healthcare-distribution-valuation-liquidity-workbench-2026-09-17.md)
now extends McKesson, Cencora, and Cardinal from period-labeled distribution
cash and legal-claim diagnostics into company-specific valuation,
reinvestment, liquidity, and thesis-breaker objects. It keeps payable-supported
McKesson liquidity, Cencora acquisition cohorts, and Cardinal legal/acquisition
claims separate and does not promote adjusted FCF, OCF, acquisition scale,
repurchases, or revenue into normalized owner cash. This is D-154; the lane
remains qualified, unranked, and period/cohort-normalization-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [industrial uptime valuation/liquidity workbench](combined-investment-research-industrial-uptime-valuation-liquidity-workbench-2026-09-17.md)
now extends Sterling, WESCO, Fastenal, and URI from conversion, backlog, and
fleet diagnostics into company-specific valuation, reinvestment, liquidity,
and thesis-breaker objects. It keeps project execution, electrical
distribution, replenishment service, and fleet lifecycle economics separate
and does not promote backlog, OCF-less-capex, utilization, resale proceeds, or
reported FCF into normalized owner cash. This is D-155; the lane remains
qualified, unranked, and denominator-and-lifecycle-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [internet edge and security valuation/liquidity workbench](combined-investment-research-edge-security-valuation-liquidity-workbench-2026-09-17.md)
now moves Akamai, Zscaler, and Fastly from company-analysis observations into
separate delivery-transition, cloud-policy, and programmable-edge valuation,
reinvestment, liquidity, and thesis-breaker objects. It keeps ARR, RPO,
bookings, security growth, traffic, capacity commitments, and reported FCF
out of normalized owner cash until collection, capacity cost, retention or
usage cohorts, SBC replacement, debt, and diluted common residual are joined.
This is D-156; the lane remains qualified, unranked, and contract-visibility-
and-capacity-normalization-open. Completion remains `12 of 13 proven; CA-06
partial`.

The new [specialty construction contractors valuation/liquidity workbench](combined-investment-research-specialty-construction-contractors-valuation-liquidity-workbench-2026-09-17.md)
extends EMCOR, Comfort Systems, Quanta, MasTec, and Primoris through project
execution, labor and materials, contract assets and liabilities, retainage,
cost-to-complete estimates, acquisitions, claims, debt, and dilution. It keeps
backlog, RPO, awards, contract liabilities, adjusted EBITDA, and reported OCF
out of normalized owner cash until project collection, final margin, required
equipment/labor reinvestment, and diluted common residual are joined. This is
D-174; the lane remains qualified, unranked, and specialty-contractor-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The new [lithography-control valuation/liquidity workbench](combined-investment-research-lithography-control-valuation-liquidity-workbench-2026-09-18.md)
adds ASML as a distinct semiconductor-equipment control point, separate from
KLA's process-control lane. It tests system and installed-base service,
acceptance, customer concentration, China/export policy, backlog conversion,
supplier capacity, R&D, and next-generation investment. It keeps systems
revenue, backlog, service revenue, gross margin, and reported OCF out of
normalized owner cash until acceptance, collection, reinvestment, and diluted
common residual are joined. This is D-178; the lane remains qualified,
unranked, and lithography-control-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The new [life-science tools and laboratory workflow valuation/liquidity workbench](combined-investment-research-life-science-tools-valuation-liquidity-workbench-2026-09-18.md)
adds Thermo Fisher as a distinct installed-workflow lane, separate from medical
devices and biopharma franchises. It tests instruments, consumables, services,
pharma-services utilization, replacement/capacity capex, quality, acquisitions,
working capital, debt, SBC, and dilution. It keeps revenue, reported FCF, and
acquisition-adjusted screens out of normalized owner cash until utilization,
collection, replacement, and diluted common-residual joins are evidenced. This
is D-179; the lane remains qualified, unranked, and life-science-tools-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The new [electronic test and measurement valuation/liquidity workbench](combined-investment-research-electronic-test-measurement-valuation-liquidity-workbench-2026-09-18.md)
adds Keysight and Teradyne as a distinct instrumentation and production-test
lane, separate from ASML lithography and KLA process control. It tests test
acceptance, software/service attachment, customer deposits, semiconductor and
robotics cycles, R&D, inventory, acquisitions, debt, SBC, and dilution. It
keeps orders, revenue, contract liabilities, reported OCF, and FCF out of
normalized owner cash until workflow collection, cycle-normalized utilization,
required reinvestment, and diluted common-residual joins are evidenced. This is
D-180; the lane remains qualified, unranked, and electronic-test-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The new [digital advertising and measurement valuation/liquidity workbench](combined-investment-research-digital-advertising-measurement-valuation-liquidity-workbench-2026-09-18.md)
adds The Trade Desk and DoubleVerify as a distinct advertiser-decisioning and
independent-measurement lane. It keeps gross spend, measured transactions,
take-rate/fee economics, platform access, identity/privacy, data/cloud cost,
customer collection, merger terms, SBC, and dilution out of normalized owner
cash until transaction settlement, platform-cost, privacy/legal, and diluted
common-residual joins are evidenced. This is D-181; the lane remains qualified,
unranked, and digital-advertising-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The new [foodservice distribution valuation/liquidity workbench](combined-investment-research-foodservice-distribution-valuation-liquidity-workbench-2026-09-18.md)
adds Sysco and US Foods as a distinct route-density and procurement lane,
separate from healthcare distribution and branded staples. It tests cases,
price/mix, vendor consideration, inventory, receivables, customer credit,
warehouse/fleet labor, fuel, ordering technology, acquisitions, debt, and
dilution. It keeps sales, cases, gross profit, vendor rebates, reported OCF,
and FCF out of normalized owner cash until route collection, working-capital,
renewal-capital, credit, and diluted common-residual joins are evidenced. This
is D-182; the lane remains qualified, unranked, and foodservice-distribution-
cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [consumer-credit platforms valuation/liquidity workbench](combined-investment-research-consumer-credit-platforms-valuation-liquidity-workbench-2026-09-18.md)
adds Affirm and Synchrony as a distinct merchant-linked credit lane, separate
from regional banks and ordinary payments. It tests GMV/purchase volume,
merchant conversion, receivables, provisions, charge-offs, funding,
securitization, partner settlement, capital, SBC, and dilution. It keeps
activity, NIM, loan sales, reported OCF, and buybacks out of normalized owner
cash until credit, funding, capital, and diluted common-residual joins are
evidenced. This is D-183; the lane remains qualified, unranked, and
consumer-credit-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [enterprise workflow software valuation/liquidity workbench](combined-investment-research-enterprise-workflow-software-valuation-liquidity-workbench-2026-09-18.md)
adds Adobe and ServiceNow as a distinct embedded-workflow software lane. It
tests renewal, seat/module and usage expansion, AI monetization, deferred
revenue and commissions, cloud/support cost, R&D, SBC, acquisitions, debt, and
dilution. It keeps ARR, RPO, ACV, reported OCF, FCF, and buybacks out of
normalized owner cash until renewal, collection, delivery-cost, and diluted
common-residual joins are evidenced. This is D-184; the lane remains qualified,
unranked, and enterprise-workflow-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The new [semiconductor manufacturing valuation/liquidity workbench](combined-investment-research-semiconductor-manufacturing-valuation-liquidity-workbench-2026-09-18.md)
adds Micron and Intel as a distinct wafer/fab manufacturing lane, separate from
ASML lithography, KLA process control, and electronic test. It tests memory
pricing, HBM/DRAM/NAND yield, fab utilization, foundry production, inventory,
capex, incentives, export controls, debt, government-linked dilution, and
common residual. It keeps revenue, gross margin, AI contracts, foundry
announcements, reported OCF, and FCF out of normalized owner cash until
qualified production, capex return, and diluted common-residual joins are
evidenced. This is D-185; the lane remains qualified, unranked, and
semiconductor-manufacturing-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The new [agricultural inputs, retail, and potash valuation/liquidity workbench](combined-investment-research-agricultural-inputs-retail-potash-valuation-liquidity-workbench-2026-09-18.md)
The new [phosphate, potash, and Brazil-execution valuation/liquidity workbench](combined-investment-research-phosphate-potash-brazil-execution-valuation-liquidity-workbench-2026-09-18.md)
adds Mosaic as D-305, keeping phosphate conversion, potash mining, sulfur/ammonia
inputs, inventory, Brazil working capital, curtailment, environmental claims,
debt, and diluted common residual separate from Nutrien. The lane remains
qualified, unranked, and owner-cash-open; completion remains `12 of 13 proven; CA-06 partial`.

The [logistics real estate, embedded-rent, and strategic-capital valuation/liquidity workbench](combined-investment-research-prologis-logistics-property-capital-valuation-liquidity-workbench-2026-09-18.md)
adds Prologis as D-311, separating industrial/logistics occupancy, lease rollover,
tenant collection, recurring capital, development, strategic-capital partnerships,
data-center power pipeline, debt, cap rates, and diluted common residual from
healthcare-property and hotel REITs. The lane remains qualified, unranked, and
owner-cash-open; completion remains `12 of 13 proven; CA-06 partial`.

The [consumer-health, routine-care, and transaction-overhang valuation/liquidity workbench](combined-investment-research-kenvue-consumer-health-routine-care-valuation-liquidity-workbench-2026-09-18.md)
adds Kenvue as D-312, separating category incidence, retailer/e-commerce
sell-through, brand and quality investment, segment mix, transaction costs, debt,
and diluted common residual from packaged-food and general staple models. The
lane remains qualified, unranked, and owner-cash-open; completion remains `12 of 13 proven; CA-06 partial`.

The [integrated steel, automotive-contract, and fixed-cost-cycle valuation/liquidity workbench](combined-investment-research-cleveland-cliffs-integrated-steel-contract-cycle-valuation-liquidity-workbench-2026-09-18.md)
adds Cleveland-Cliffs as D-313, separating integrated iron ore, pellets, DRI,
steel, downstream conversion, contract lag, automotive volume, utilization,
energy/labor, pension/OPEB, capex, debt, and diluted common residual from Nucor.
The lane remains qualified, unranked, and owner-cash-open; completion remains `12 of 13 proven; CA-06 partial`.

The [sensing, imaging, and mission-systems valuation/liquidity workbench](combined-investment-research-teledyne-sensing-imaging-mission-systems-valuation-liquidity-workbench-2026-09-18.md)
adds Teledyne as D-314, separating Digital Imaging, Instrumentation, Aerospace
and Defense Electronics, Engineered Systems, backlog acceptance, program margin,
R&D, acquisition return, debt, and diluted common residual from adjacent test,
interconnect, and defense routes. The lane remains qualified, unranked, and
owner-cash-open; completion remains `12 of 13 proven; CA-06 partial`.

The [residential solar and storage subscriber-financing valuation/liquidity workbench](combined-investment-research-sunrun-residential-solar-storage-subscriber-financing-valuation-liquidity-workbench-2026-09-18.md)
adds Sunrun as D-315, separating subscriber value and contracted net earning
assets from installation, customer collection, churn, storage utilization,
tax-credit and safe-harbor support, project finance, recourse debt, and diluted
common residual. The lane remains qualified, unranked, and owner-cash-open;
completion remains `12 of 13 proven; CA-06 partial`.

The [travel marketplace, trust, and payments valuation/liquidity workbench](combined-investment-research-airbnb-travel-marketplace-trust-payments-valuation-liquidity-workbench-2026-09-18.md)
adds Airbnb as D-316, separating GBV and nights from host/guest settlement,
retained take rate, payment processing, refunds, trust and safety, support,
regulation, hotels, services, experiences, AI infrastructure, and diluted
common residual. The lane remains qualified, unranked, and owner-cash-open;
completion remains `12 of 13 proven; CA-06 partial`.

The [route-based workplace services and UniFirst valuation/liquidity workbench](combined-investment-research-cintas-route-workplace-services-unifirst-valuation-liquidity-workbench-2026-09-18.md)
adds Cintas as D-317, separating route revenue and service density from garment
and fleet renewal, plant labor, customer retention, first-aid and fire claims,
UniFirst funding and integration, debt, and diluted common residual. The lane
remains qualified, unranked, and owner-cash-open; completion remains `12 of 13
proven; CA-06 partial`.

The [imaging workflow and device-cycle valuation/liquidity workbench](combined-investment-research-canon-imaging-workflow-device-cycle-valuation-liquidity-workbench-2026-09-18.md)
adds Canon as D-318, separating camera and network-camera sell-through from
printing, medical and industrial qualification, inventory, service/consumables,
R&D, plant renewal, memory and tariff effects, debt, and diluted common
residual. The lane remains qualified, unranked, and owner-cash-open; completion
remains `12 of 13 proven; CA-06 partial`.

The [appliance-plus-subscription cybersecurity valuation/liquidity workbench](combined-investment-research-fortinet-appliance-subscription-security-valuation-liquidity-workbench-2026-09-18.md)
adds Fortinet as D-319, separating product and service revenue, billings, and
deferred revenue from appliance sell-through, channel inventory, SASE/OT/AI
delivery, threat intelligence, R&D, SBC, warranty, debt, and diluted common
residual. The lane remains qualified, unranked, and owner-cash-open; completion
remains `12 of 13 proven; CA-06 partial`.

The [cement, carbon, and urbanization valuation/liquidity workbench](combined-investment-research-cemex-cement-carbon-urbanization-valuation-liquidity-workbench-2026-09-18.md)
adds CEMEX as D-320, separating cement, ready-mix, and aggregates price/volume
from kiln and quarry renewal, energy and freight, carbon obligations, public
program timing, housing, AI-linked industrial demand, portfolio changes,
impairment, debt, and diluted common residual. The lane remains qualified,
unranked, and owner-cash-open; completion remains `12 of 13 proven; CA-06
partial`.

The [appliance replacement-cycle and liquidity valuation workbench](combined-investment-research-whirlpool-appliance-replacement-liquidity-valuation-workbench-2026-09-18.md)
adds Whirlpool as D-321, separating units and retailer sell-through from
housing, consumer credit, promotions, plant utilization, tariffs, domestic
sourcing, warranty, restructuring, debt refinancing, and diluted common
residual. The lane remains qualified, unranked, and owner-cash-open; completion
remains `12 of 13 proven; CA-06 partial`.

The [partner enrollment and workforce-education services valuation/liquidity workbench](combined-investment-research-grand-canyon-education-partner-enrollment-valuation-liquidity-workbench-2026-09-18.md)
adds Grand Canyon Education as D-322, separating enrollment and service revenue
from persistence, revenue per student, partner contract changes, online delivery,
off-campus sites, ABSN capacity, compliance, litigation, reinvestment, and
diluted common residual. The lane remains qualified, unranked, and owner-cash-
open; completion remains `12 of 13 proven; CA-06 partial`.

The [alumina, aluminum, and energy conversion valuation/liquidity workbench](combined-investment-research-alcoa-alumina-aluminum-energy-valuation-liquidity-workbench-2026-09-18.md)
adds Alcoa as D-323, separating alumina, aluminum, bauxite, and energy
price/volume from power, smelter/refinery renewal, restarts, closures,
remediation, carbon, JV funding, portfolio proceeds, debt, and diluted common
residual. The lane remains qualified, unranked, and owner-cash-open; completion
remains `12 of 13 proven; CA-06 partial`.

The [accessible-luxury brand-house valuation/liquidity workbench](combined-investment-research-tapestry-accessible-luxury-brand-house-valuation-liquidity-workbench-2026-09-18.md)
adds Tapestry as D-324, separating Coach and Kate Spade brand demand from
full-price sell-through, direct-to-consumer conversion, Gen Z acquisition,
inventory and markdowns, stores, China/Europe, tariffs, licensing,
restructuring, debt, and diluted common residual. The lane remains qualified,
unranked, and owner-cash-open; completion remains `12 of 13 proven; CA-06
partial`.

The [electronics retail, marketplace, and services valuation/liquidity workbench](combined-investment-research-best-buy-electronics-marketplace-services-valuation-liquidity-workbench-2026-09-18.md)
adds Best Buy as D-325, separating device-category sell-through and comparable
sales from vendor funding, inventory, Geek Squad/services, Marketplace, Best Buy
Ads, delivery, repair, trade-in, leases, debt, and diluted common residual. The
lane remains qualified, unranked, and owner-cash-open; completion remains `12 of
13 proven; CA-06 partial`.

The [discount-variety multi-price value-format valuation/liquidity workbench](combined-investment-research-dollar-tree-multiprice-value-format-valuation-liquidity-workbench-2026-09-18.md)
adds Dollar Tree as D-326, separating traffic, ticket, and multi-price store
economics from units/sell-through, promotions, inventory, shrink, Dollar Tree
3.0 conversions, supply chain, Family Dollar separation, leases, debt, and
diluted common residual. The lane remains qualified, unranked, and owner-cash-
open; completion remains `12 of 13 proven; CA-06 partial`.

The [consumables-heavy neighborhood convenience valuation/liquidity workbench](combined-investment-research-dollar-general-consumables-convenience-valuation-liquidity-workbench-2026-09-18.md)
adds Dollar General as D-327, separating traffic and consumables mix from
inventory per store, shrink, labor, Project Renovate/Elevate, new stores,
closures, private label, DG Media, supply chain, leases, debt, and diluted
common residual. The lane remains qualified, unranked, and owner-cash-open;
completion remains `12 of 13 proven; CA-06 partial`.

The [beauty, fragrance, and portfolio-renovation valuation/liquidity workbench](combined-investment-research-coty-beauty-fragrance-portfolio-valuation-liquidity-workbench-2026-09-18.md)
adds Coty as D-328, separating fragrance and cosmetics sell-through from
Consumer Beauty weakness, licensing, retailer inventory, innovation, marketing,
e-commerce, strategic review, restructuring, FX, debt, and diluted common
residual. The lane remains qualified, unranked, and owner-cash-open; completion
remains `12 of 13 proven; CA-06 partial`.

The [wellness-community performance apparel valuation/liquidity workbench](combined-investment-research-lululemon-wellness-community-apparel-valuation-liquidity-workbench-2026-09-18.md)
adds lululemon as D-329, separating Americas repair work and international
growth from full-price sell-through, product innovation, community marketing,
inventory and markdowns, store/digital productivity, sourcing, FX, tariffs,
leases, debt, and diluted common residual. The lane remains qualified,
unranked, and owner-cash-open; completion remains `12 of 13 proven; CA-06
partial`.

The [branded participation, ceremony, and franchise valuation/liquidity workbench](combined-investment-research-build-a-bear-participation-franchise-valuation-liquidity-workbench-2026-09-18.md)
adds Build-A-Bear as D-330, separating ceremony and experience economics from
direct stores, partner and franchise channels, licensed product, gifting,
inventory, tariffs, Vietnam sourcing, occupancy, leases, and diluted common
residual. The lane remains qualified, unranked, and owner-cash-open; completion
remains `12 of 13 proven; CA-06 partial`.

The [IP-driven play, entertainment, and digital-games valuation/liquidity workbench](combined-investment-research-mattel-ip-entertainment-digital-games-valuation-liquidity-workbench-2026-09-18.md)
adds Mattel as D-331, separating toy sell-through and gross billings from
theatrical releases, licensing, Mattel163, mobile games, DTC, first-party data,
inventory, product claims, strategic investments, debt, and diluted common
residual. The lane remains qualified, unranked, and owner-cash-open; completion
remains `12 of 13 proven; CA-06 partial`.

The [monitored security subscription and smart-home valuation/liquidity workbench](combined-investment-research-adt-monitored-security-subscription-valuation-liquidity-workbench-2026-09-18.md)
adds ADT as D-332, separating RMR and monitoring cash from installation,
attrition, customer-acquisition payback, ADT+, Google Nest/Yale, ambient
sensing, service, debt/swaps, and diluted common residual. The lane remains
qualified, unranked, and owner-cash-open; completion remains `12 of 13 proven;
CA-06 partial`.

The [identification, safety, and traceability valuation/liquidity workbench](combined-investment-research-brady-identification-safety-traceability-valuation-liquidity-workbench-2026-09-18.md)
adds Brady as D-333, separating identification, safety, traceability,
printer/software, and consumables economics from product sell-through, regional
divergence, acquisitions, R&D, inventory, compliance, debt, and diluted common
residual. The lane remains qualified, unranked, and owner-cash-open; completion
remains `12 of 13 proven; CA-06 partial`.

adds Nutrien as a distinct integrated crop-input and farmer-retail lane. It
keeps FCF, EBITDA, production, retail growth, supplier-financing cash,
dividends, and buybacks out of normalized owner cash until segment price/volume/
cost, mine/plant renewal, supplier terms, inventory, receivables, environmental
obligations, exits, debt, and diluted common residual joins are evidenced. This
is D-230; the lane remains qualified, unranked, and agricultural-inputs-cash-
open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [institutional custody and asset-servicing valuation/liquidity workbench](combined-investment-research-institutional-custody-asset-servicing-valuation-liquidity-workbench-2026-09-18.md)
adds State Street as a distinct custody, administration, securities-processing,
and institutional-bank lane. It keeps AUC/A, AUM, fee revenue, EPS, OCF, and
buybacks out of normalized owner cash until fee rate, client retention,
activity, technology/control investment, collateral, liquidity, regulatory
capital, NII/FX normalization, and diluted common residual joins are evidenced.
This is D-229; the lane remains qualified, unranked, and custody-servicing-
cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [climate-control HVAC and service valuation/liquidity workbench](combined-investment-research-climate-control-hvac-service-valuation-liquidity-workbench-2026-09-18.md)
adds Trane Technologies as a distinct cooling, controls, retrofit, and
installed-service lane. It keeps bookings, backlog, adjusted EPS, OCF, FCF
conversion, and buybacks out of normalized owner cash until service attachment,
project acceptance, collection, technician/warranty economics, inventory,
acquisition return, incentive cash, debt, and diluted common residual joins are
evidenced. This is D-228; the lane remains qualified, unranked, and climate-
control-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [coffeehouse routine-demand valuation/liquidity workbench](combined-investment-research-coffeehouse-routine-demand-valuation-liquidity-workbench-2026-09-18.md)
adds Starbucks as a distinct company-operated coffeehouse and loyalty lane. It
keeps comparable sales, ticket, adjusted earnings, OCF, dividends, and buybacks
out of normalized owner cash until transactions, store contribution,
labor/service, Rewards/stored-value settlement, maintenance/remodels, closures,
debt, and diluted common residual joins are evidenced. This is D-227; the lane
remains qualified, unranked, and coffeehouse-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The new [diversified mining and metals valuation/liquidity workbench](combined-investment-research-diversified-mining-metals-valuation-liquidity-workbench-2026-09-18.md)
adds Rio Tinto as a distinct mine-and-logistics portfolio lane. It keeps
production, EBITDA, FCF, first ore, critical-minerals growth, and dividends
out of normalized owner cash until mid-cycle price, grade/recovery, reserve
replacement, sustaining/project capital, partner funding, rehabilitation,
debt, and diluted common residual joins are evidenced. This is D-226; the lane
remains qualified, unranked, and diversified-mining-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The new [chlorovinyl and chlor-alkali chemicals valuation/liquidity workbench](combined-investment-research-chlorovinyl-chloralkali-chemicals-valuation-liquidity-workbench-2026-09-18.md)
adds Westlake as a distinct integrated chemical-cycle lane. It keeps EBITDA,
spreads, OCF, improvement-plan savings, and dividends out of normalized owner
cash until HIP/PEM mid-cycle margin, utilization, sustaining capital,
shutdown/remediation, inventory, ACI return, debt, environmental claims, and
diluted common residual joins are evidenced. This is D-225; the lane remains
qualified, unranked, and chlorovinyl-chemical-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The new [industrial automation installed-base valuation/liquidity workbench](combined-investment-research-industrial-automation-installed-base-valuation-liquidity-workbench-2026-09-18.md)
adds Honeywell as a distinct post-separation controls and service/software
lane. It keeps backlog, adjusted EPS, OCF, installed-base claims, and buybacks
out of normalized owner cash until delivered and renewed revenue, normalized
cash, capex/R&D, acquisition return, pension, legal claims, standalone cost,
debt, and diluted common residual joins are evidenced. This is D-224; the lane
remains qualified, unranked, and industrial-automation-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The new [energy-beverage brand and distribution valuation/liquidity workbench](combined-investment-research-energy-beverage-brand-distribution-valuation-liquidity-workbench-2026-09-18.md)
adds Monster Beverage as a distinct repeat-consumption and bottler-dependent
brand lane. It keeps cases, sales, gross margin, adjusted earnings, OCF, and
buybacks out of normalized owner cash until consumer sell-through, net revenue
per case, promotion, bottler settlement, working capital, continuing-brand
economics, SBC, and diluted common residual joins are evidenced. This is D-223;
the lane remains qualified, unranked, and energy-beverage-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The new [senior-housing healthcare REIT valuation/liquidity workbench](combined-investment-research-senior-housing-healthcare-reit-valuation-liquidity-workbench-2026-09-18.md)
adds Welltower as a distinct senior-housing and healthcare-property lane. It
keeps normalized FFO, same-store NOI, occupancy, investment volume, and
dividends out of normalized owner cash until operator coverage, resident
collection, recurring property capital, acquisition/development return, debt,
cap rates, preferred claims, NAV, and diluted common residual joins are
evidenced. This is D-222; the lane remains qualified, unranked, and
senior-housing-reit-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The [Ventas healthcare-property operating-platform valuation/liquidity workbench](combined-investment-research-ventas-healthcare-property-capital-valuation-liquidity-workbench-2026-09-18.md)
adds Ventas as D-307, separating its SHOP/OM&R/NNN mix, operator coverage,
property capital, acquisition and development cohorts, equity-forward funding,
debt, and diluted common residual from Welltower. The lane remains qualified,
unranked, and owner-cash-open; completion remains `12 of 13 proven; CA-06 partial`.

The new [spin-off engineering and mission-technology valuation/liquidity workbench](combined-investment-research-spin-off-engineering-mission-technology-valuation-liquidity-workbench-2026-09-18.md)
adds KBR as a distinct two-engine separation lane. It keeps backlog, options,
adjusted earnings, OCF, and buybacks out of normalized owner cash until funded
conversion, contract type and margin, affiliate availability, separation cost,
standalone debt and pension, and diluted common residual joins are evidenced.
This is D-221; the lane remains qualified, unranked, and spin-off-engineering-
cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [milestone jewelry retail valuation/liquidity workbench](combined-investment-research-milestone-jewelry-retail-valuation-liquidity-workbench-2026-09-18.md)
adds Signet Jewelers as a distinct occasion-driven jewelry and inventory lane.
It keeps same-store sales, AUR, adjusted earnings, FCF, and buybacks out of
normalized owner cash until unit demand, inventory turns, markdowns,
commodity/tariff cost, maintenance, restructuring, SBC, and diluted common
residual joins are evidenced. This is D-220; the lane remains qualified,
unranked, and milestone-jewelry-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The new [hospital operations valuation/liquidity workbench](combined-investment-research-hospital-operations-valuation-liquidity-workbench-2026-09-18.md)
adds HCA Healthcare as a distinct care-delivery lane, separate from payers,
distributors, devices, and life-science tools. It tests admissions, acuity,
payer mix and collection, labor, supplies, staffed capacity, replacement/growth
capex, acquisitions, noncontrolling interests, interest, debt, litigation, and
dilution. It keeps revenue, admissions, reported OCF, and buybacks out of
normalized owner cash until payer collection, capacity renewal, NCI, debt, and
diluted common-residual joins are evidenced. This is D-186; the lane remains
qualified, unranked, and hospital-operations-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The new [healthcare payment workflow valuation/liquidity workbench](combined-investment-research-healthcare-payment-workflow-valuation-liquidity-workbench-2026-09-18.md)
adds Waystar as a distinct healthcare-administration software lane, separate
from hospital operations, payers, distributors, care delivery, and devices. It
tests provider versus patient-payment mix, third-party processing cost,
collection, deferred revenue, Iodine acquisition return, product investment,
debt, SBC, and diluted common residual. It keeps revenue, NRR, adjusted EBITDA,
OCF, and transaction volume out of normalized owner cash until mix, collection,
acquisition, debt, and per-share cash joins are evidenced. This is D-187; the
lane remains qualified, unranked, and healthcare-payment-workflow-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The new [precious-metals streaming valuation/liquidity workbench](combined-investment-research-precious-metals-streaming-valuation-liquidity-workbench-2026-09-18.md)
adds Wheaton Precious Metals as a distinct contractual-stream lane, separate
from direct mine operators, materials manufacturers, and integrated energy. It
tests delivered and collected metal, upfront stream payments, payable costs,
operator delivery, reserve curves, Antamina return, debt, dividends, taxes, and
diluted common residual. It keeps GEOs, revenue, OCF, low PP&E capex, and
annualized stream screens out of normalized owner cash until delivery,
acquisition-return, leverage, and per-share cash joins are evidenced. This is
D-188; the lane remains qualified, unranked, and precious-metals-streaming-
cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [nuclear-fuel-cycle valuation/liquidity workbench](combined-investment-research-nuclear-fuel-cycle-valuation-liquidity-workbench-2026-09-18.md)
adds Cameco as a distinct uranium-mining, inventory, conversion, and
Westinghouse lane, separate from merchant power, generic mining, oil and gas,
and materials-cycle economics. It tests production and deliveries, contract
pricing, procurement, inventory replacement, sustaining capital, Fuel Services,
Westinghouse equity earnings and distributions, reclamation, debt, export
controls, and diluted common residual. It keeps production, deliveries,
realized price, OCF, equity-method earnings, inventory gains, and dividends out
of normalized owner cash until replacement-cost, sustaining-capital, JV-return,
reclamation, and per-share cash joins are evidenced. This is D-206; the lane
remains qualified, unranked, and nuclear-fuel-cycle-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The new [electronic interconnect content valuation/liquidity workbench](combined-investment-research-electronic-interconnect-content-valuation-liquidity-workbench-2026-09-18.md)
adds Amphenol as a distinct connector, sensor, cable, antenna, and power-
interconnect lane, separate from electronics distribution, semiconductor
manufacturing, networking control, and test equipment. It tests qualified
design-in, organic versus acquired growth, orders, book-to-bill, inventory,
capacity, tariffs, acquisition integration, debt, SBC, and diluted common
residual. It keeps sales, orders, adjusted margin, EPS accretion, OCF, and
buybacks out of normalized owner cash until shipment, collection, inventory,
acquisition-return, tariff-normalization, and per-share cash joins are
evidenced. This is D-207; the lane remains qualified, unranked, and
electronic-interconnect-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The new [merchant-commerce operating-system valuation/liquidity workbench](combined-investment-research-merchant-commerce-operating-system-valuation-liquidity-workbench-2026-09-18.md)
adds Shopify as a distinct merchant-workflow platform, separate from eBay's
goods marketplace, enterprise workflow software, and ordinary consumer credit.
It tests subscription retention, merchant-solutions mix, GMV, Payments
penetration, processing and fraud cost, merchant lending, settlement
obligations, AI/platform investment, SBC, and diluted common residual. It keeps
GMV, Payments penetration, revenue, adjusted earnings, OCF, and buybacks out of
normalized owner cash until merchant survival, payment contribution, credit,
settlement, SBC, and per-share cash joins are evidenced. This is D-208; the
lane remains qualified, unranked, and merchant-commerce-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The new [integrated device ecosystem valuation/liquidity workbench](combined-investment-research-integrated-device-ecosystem-valuation-liquidity-workbench-2026-09-18.md)
adds Apple as a distinct premium-device and Services ecosystem lane, separate
from merchant commerce, enterprise workflow software, transaction marketplaces,
and electronic interconnect content. It tests device replacement, installed-
base retention, Services attachment and take rate, platform costs, R&D,
silicon, supply chain, tariffs, China, regulation, SBC, and diluted common
residual. It keeps installed base, Services growth/margin, revenue, adjusted
earnings, OCF, and buybacks out of normalized owner cash until replacement,
normalized take-rate, reinvestment, regulatory, and per-share cash joins are
evidenced. This is D-209; the lane remains qualified, unranked, and
integrated-device-ecosystem-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The new [mobility and delivery marketplace valuation/liquidity workbench](combined-investment-research-mobility-delivery-marketplace-valuation-liquidity-workbench-2026-09-18.md)
adds Uber as a distinct ride/order coordination and membership platform,
separate from travel booking, lodging, e-commerce marketplaces, and merchant-
commerce software. It tests gross bookings versus retained revenue,
driver/courier and merchant settlements, incentives, insurance, payments,
refunds, membership, legal obligations, autonomous-vehicle partners, SBC, and
diluted common residual. It keeps gross bookings, trips, MAPCs, adjusted
EBITDA, FCF, and membership out of normalized owner cash until retained
contribution, supply/insurance, legal, AV-return, and per-share cash joins are
evidenced. This is D-210; the lane remains qualified, unranked, and
mobility-delivery-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The new [qualified grid components valuation/liquidity workbench](combined-investment-research-qualified-grid-components-valuation-liquidity-workbench-2026-09-18.md)
adds Hubbell as a distinct qualified electrical-infrastructure components lane,
separate from regulated utilities, power generation, Amphenol interconnects,
and industrial distribution. It tests Utility Solutions, Electrical Solutions,
grid infrastructure, automation, meters, firm backlog, price versus unit
volume, channel inventory, acquisitions, pension, debt, and diluted common
residual. It keeps sales, backlog, adjusted EPS, OCF, and buybacks out of
normalized owner cash until shipment, collection, volume, acquisition-return,
and per-share cash joins are evidenced. This is D-211; the lane remains
qualified, unranked, and qualified-grid-components-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The new [commercial landscape services valuation/liquidity workbench](combined-investment-research-commercial-landscape-services-valuation-liquidity-workbench-2026-09-18.md)
adds BrightView as a distinct maintenance-contract and outdoor-site-services
lane, separate from ABM facility services, pest-control routes, environmental
services, and specialty construction. It tests Maintenance versus Development,
H-2B labor, route density, fleet renewal, weather, working capital, receivables
financing, debt, leases, preferred claims, and diluted common residual. It keeps
revenue, adjusted EBITDA, adjusted FCF, OCF, equipment-sale proceeds, and
buybacks out of normalized owner cash until renewal, staffing, fleet,
collection, leverage, preferred, and per-share cash joins are evidenced. This
is D-212; the lane remains qualified, unranked, and commercial-landscape-cash-
open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [holding-company subsidiary cash valuation/liquidity workbench](combined-investment-research-holding-company-subsidiary-cash-valuation-liquidity-workbench-2026-09-18.md)
adds Loews as a distinct diversified ownership and capital-allocation lane,
separate from operating-company insurance, pipelines, hotels, packaging, and
asset management. It tests CNA reserves and capital, Boardwalk maintenance and
debt, hotel renovation, packaging working capital, subsidiary remittance,
parent overhead and tax, trapped cash, minority claims, holding-company
discount, and diluted common residual. It keeps consolidated earnings,
dividends, OCF, book value, and buybacks out of normalized owner cash until
subsidiary-capital, parent-remittance, maintenance, tax, and look-through
per-share joins are evidenced. This is D-215; the lane remains qualified,
unranked, and holding-company-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The new [specialty-glass and optical-connectivity valuation/liquidity workbench](combined-investment-research-specialty-glass-optical-connectivity-valuation-liquidity-workbench-2026-09-18.md)
adds Corning as a distinct physical-materials and manufacturing-capacity lane,
separate from active networking equipment, electronic interconnects, and
semiconductor fabrication. It keeps optical growth, customer agreements,
adjusted FCF, and OCF out of normalized owner cash until utilization, capacity
return, working-capital, delivery-obligation, claims, and diluted common
residual joins are evidenced. This is D-216; the lane remains qualified,
unranked, and specialty-glass-capacity-open. Completion remains `12 of 13
proven; CA-06 partial`.

The new [industrial-electrical protection and cooling valuation/liquidity workbench](combined-investment-research-industrial-electrical-protection-cooling-valuation-liquidity-workbench-2026-09-18.md)
adds nVent Electric as a distinct qualified-interface and thermal-management
lane. It keeps sales growth, backlog, adjusted EPS, reported FCF, and
divestiture proceeds out of normalized owner cash until organic/acquired
growth, shipment and collection, liquid-cooling capacity and warranty,
integration, debt, and diluted common residual joins are evidenced. This is
D-217; the lane remains qualified, unranked, and industrial-electrical-
capacity-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [institutional consulting and managed-services valuation/liquidity workbench](combined-investment-research-institutional-consulting-managed-services-valuation-liquidity-workbench-2026-09-18.md)
adds Huron Consulting Group as a distinct professional-labor and institutional
workflow lane. It keeps RBR, adjusted EBITDA, GAAP earnings, OCF, and buybacks
out of normalized owner cash until utilization, client collection, managed-
services renewal, software, acquisition-return, SBC, and diluted common
residual joins are evidenced. This is D-218; the lane remains qualified,
unranked, and institutional-consulting-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The new [home-furnishings marketplace and logistics valuation/liquidity workbench](combined-investment-research-home-furnishings-marketplace-logistics-valuation-liquidity-workbench-2026-09-18.md)
adds Wayfair as a distinct bulky-goods marketplace and delivery-network lane.
It keeps customers, orders, gross profit, adjusted EBITDA, OCF, and buybacks
out of normalized owner cash until order-level contribution, supplier health,
delivery and return cost, network capacity, leases, SBC, and diluted common
residual joins are evidenced. This is D-219; the lane remains qualified,
unranked, and home-marketplace-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The new [Agency mortgage-REIT carry and book-value valuation/liquidity workbench](combined-investment-research-agency-mortgage-reit-carry-valuation-liquidity-workbench-2026-09-18.md)
adds AGNC Investment as a distinct levered Agency RMBS/TBA asset-liability
spread lane, separate from banks, insurers, asset managers, and operating
companies. It tests repo funding, mortgage spreads, prepayment, duration,
hedges, comprehensive income, tangible book value, leverage, collateral,
dividend coverage, capital issuance, and diluted common residual. It keeps
spread income, economic return, book value, dividends, and yield out of
normalized owner cash until funding, hedge, book-value, leverage, and per-share
cash joins are evidenced. This is D-213; the lane remains qualified, unranked,
and agency-mortgage-reit-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The new [exchange, clearing, and collateral valuation/liquidity workbench](combined-investment-research-exchange-clearing-collateral-valuation-liquidity-workbench-2026-09-18.md)
adds CME Group as a distinct derivatives-exchange and central-counterparty
clearing lane, separate from information vendors, banks, brokers, and ordinary
financial companies. It tests transaction/clearing fees, market data, volume
and rate per contract, client collateral, collateral-interest income, clearing
obligations, technology, cyber, regulation, dividends, SBC, and diluted common
residual. It keeps client collateral, volume, OCF, investment income,
dividends, and buybacks out of normalized owner cash until core-fee, collateral,
clearing-obligation, rate-normalization, and per-share cash joins are evidenced.
This is D-214; the lane remains qualified, unranked, and exchange-clearing-cash-
open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [recurring pest-control routes valuation/liquidity workbench](combined-investment-research-recurring-pest-control-routes-valuation-liquidity-workbench-2026-09-18.md)
adds Rollins as a distinct local route-service lane, separate from environmental
services, healthcare access, industrial distribution, and software. It tests
organic versus acquired growth, customer retention, technician productivity,
customer-acquisition cost, claims, chemicals, vehicles, receivables, unearned
service obligations, acquisitions, debt, SBC, and diluted common residual. It
keeps recurring revenue, OCF, FCF, and buybacks out of normalized owner cash
until route, collection, and acquired-cohort return joins are evidenced. This
is D-189; the lane remains qualified, unranked, and recurring-pest-control-
cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [membership-franchise wellness valuation/liquidity workbench](combined-investment-research-membership-franchise-wellness-valuation-liquidity-workbench-2026-09-18.md)
adds Planet Fitness as a distinct affordable-membership and franchise-network
lane, separate from restaurant franchising, recurring route services, consumer
goods, and software. It tests member retention, attendance, price/mix,
franchisee returns, club openings, support and technology, equipment, debt,
SBC, buybacks, and diluted common residual. It keeps members, systemwide sales,
club count, adjusted EBITDA, OCF, and repurchases out of normalized owner cash
until retention, franchisee-health, support-cost, and per-share cash joins are
evidenced. This is D-190; the lane remains qualified, unranked, and
membership-franchise-wellness-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The new [transaction marketplace valuation/liquidity workbench](combined-investment-research-transaction-marketplace-valuation-liquidity-workbench-2026-09-18.md)
adds eBay as a distinct goods-marketplace lane, separate from travel
marketplaces, advertising measurement, participation platforms, and retailers.
It tests GMV conversion, take rate, buyer/seller retention, payments, fraud and
transaction losses, advertising, capitalized platform development, Depop and
other acquisitions, debt, SBC, buybacks, and diluted common residual. It keeps
GMV, active buyers, advertising, OCF, and repurchases out of normalized owner
cash until trust, collection, platform-replacement, acquisition-return, and
per-share cash joins are evidenced. This is D-191; the lane remains qualified,
unranked, and transaction-marketplace-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The new [agribusiness crop-flow valuation/liquidity workbench](combined-investment-research-agribusiness-crop-flow-valuation-liquidity-workbench-2026-09-18.md)
adds Bunge Global as a distinct crop-origination, processing, merchandising,
and commodity-finance lane, separate from agricultural inputs, foodservice
distribution, materials, and direct commodity producers. It tests realized
spreads, inventory and receivables, freight, productive capex, Viterra
integration, debt, collateral, policy, dividends, and diluted common residual.
It keeps revenue, adjusted EBIT/EPS, mark-to-market changes, synergies, OCF,
and buybacks out of normalized owner cash until realized-spread,
working-capital, acquisition-return, leverage, and per-share cash joins are
evidenced. This is D-192; the lane remains qualified, unranked, and
agribusiness-crop-flow-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The new [franchise media and experiences valuation/liquidity workbench](combined-investment-research-franchise-media-experiences-valuation-liquidity-workbench-2026-09-18.md)
adds Walt Disney as a distinct IP, streaming, sports, parks, cruise, and
experiences lane, separate from travel platforms, advertising measurement,
consumer staples, membership franchises, and transaction marketplaces. It
tests content and rights returns, streaming contribution, attendance and
per-capita spend, maintenance/growth capacity, corporate costs, debt, NCI,
taxes, dividends, and diluted common residual. It keeps segment income,
subscribers, attendance, OCF, and buybacks out of normalized owner cash until
content, rights, capacity-renewal, and per-share cash joins are evidenced. This
is D-193; the lane remains qualified, unranked, and
franchise-media-experiences-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The new [asset-integrity inspection valuation/liquidity workbench](combined-investment-research-asset-integrity-inspection-valuation-liquidity-workbench-2026-09-18.md)
adds MISTRAS Group as a distinct certified inspection, monitoring, and
technical-services lane, separate from environmental services, specialty
construction, industrial distribution, and electronic test. It tests recurring
program renewal, technician utilization, collection, contract assets,
software/data, accreditation, capex, claims, debt, and diluted common residual.
It keeps revenue, adjusted EBITDA, gross margin, OCF, FCF, and aerospace/defense
growth out of normalized owner cash until collection, technician,
capability-repair, leverage, and per-share cash joins are evidenced. This is
D-194; the lane remains qualified, unranked, and
asset-integrity-inspection-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The new [talent advisory and professional services valuation/liquidity workbench](combined-investment-research-talent-advisory-professional-services-valuation-liquidity-workbench-2026-09-18.md)
adds Korn Ferry as a distinct executive-search, interim-capacity, consulting,
Digital, and RPO lane, separate from enterprise workflow software, technical
inspection, healthcare staffing, and recurring route services. It tests
solution-level mix, remaining-fee conversion, professional utilization,
compensation, collection, platform investment, acquisitions, debt, SBC, and
diluted common residual. It keeps remaining fees, bookings, adjusted EBITDA,
OCF, and buybacks out of normalized owner cash until delivery, utilization,
collection, and per-share cash joins are evidenced. This is D-195; the lane
remains qualified, unranked, and talent-advisory-professional-services-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The new [electronics distribution valuation/liquidity workbench](combined-investment-research-electronics-distribution-valuation-liquidity-workbench-2026-09-18.md)
adds Avnet as a distinct component-availability and design-support lane,
separate from industrial procurement, semiconductor manufacturing, electronic
test, and networking control. It tests Electronic Components versus Farnell
mix, inventory velocity, receivables, supplier return rights, obsolescence,
design support, warehouses, debt, taxes, SBC, and diluted common residual. It
keeps sales, gross margin, adjusted EPS, inventory days, OCF, and buybacks out
of normalized owner cash until inventory, supplier-protection, collection,
debt, and per-share cash joins are evidenced. This is D-196; the lane remains
qualified, unranked, and electronics-distribution-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The new [qualified dispensing and packaging valuation/liquidity workbench](combined-investment-research-qualified-dispensing-packaging-valuation-liquidity-workbench-2026-09-18.md)
adds AptarGroup as a distinct qualified component and dosing-interface lane,
separate from medical devices, consumer staples, semiconductor hardware, and
industrial chemicals. It tests Pharma, Beauty, and Closures mix, customer
qualification, product launches, quality and clean-room investment, materials,
plant utilization, tooling, capex, acquisitions, debt, SBC, and diluted common
residual. It keeps sales, adjusted EBITDA/EPS, Pharma growth, OCF, and buybacks
out of normalized owner cash until core demand, qualification returns, quality
investment, and per-share cash joins are evidenced. This is D-197; the lane
remains qualified, unranked, and qualified-dispensing-packaging-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The new [crop-protection chemistry valuation/liquidity workbench](combined-investment-research-crop-protection-chemistry-valuation-liquidity-workbench-2026-09-18.md)
adds FMC as a distinct crop-protection chemistry and leveraged portfolio-repair
lane, separate from fertilizer, agribusiness processing, materials, and
industrial chemicals. It tests active-ingredient life cycles, registrations,
price/volume, formulation, manufacturing reset, inventory, receivable
factoring, restructuring, India/portfolio changes, debt, and diluted common
residual. It keeps adjusted EBITDA, new-product sales, factoring, OCF, and
asset-sale proceeds out of normalized owner cash until product replacement,
working-capital, leverage, and per-share cash joins are evidenced. This is
D-198; the lane remains qualified, unranked, and crop-protection-chemistry-
cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [distributed resilience power valuation/liquidity workbench](combined-investment-research-distributed-resilience-power-valuation-liquidity-workbench-2026-09-18.md)
adds Generac as a distinct distributed backup-power, controls, storage, and
monitoring lane, separate from merchant power, utilities, grid infrastructure,
industrial uptime, and equipment rental. It tests residential versus C&I and
data-center demand, backlog conversion, inventory, warranty, dealer/service,
factory capacity, tariffs, legal claims, capex, debt, SBC, and diluted common
residual. It keeps backlog, adjusted EBITDA, C&I growth, tariff refunds, OCF,
and buybacks out of normalized owner cash until shipment, collection, warranty,
margin-after-refund, and per-share cash joins are evidenced. This is D-199; the
lane remains qualified, unranked, and distributed-resilience-power-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The new [institutional research and advisory valuation/liquidity workbench](combined-investment-research-institutional-research-advisory-valuation-liquidity-workbench-2026-09-18.md)
adds Gartner as a distinct decision-support, Insights, conference, and
consulting lane, separate from enterprise workflow software, talent advisory,
insurance brokerage, and advertising measurement. It tests contract value,
renewal and wallet retention, conference attendance, consulting utilization,
deferred revenue/commissions, analyst labor, collection, debt, SBC, repurchases,
and diluted common residual. It keeps contract value, retention, adjusted
EBITDA, OCF, and buybacks out of normalized owner cash until renewal, mix, cash
normalization, and per-share cash joins are evidenced. This is D-200; the lane
remains qualified, unranked, and institutional-research-advisory-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The new [satellite connectivity valuation/liquidity workbench](combined-investment-research-satellite-connectivity-valuation-liquidity-workbench-2026-09-18.md)
adds Iridium Communications as a distinct orbital network and recurring-service
lane, separate from terrestrial networking, distributed power, merchant
generation, and enterprise software. It tests service and government renewal,
subscriber cohorts, direct-to-device economics, constellation and ground
replacement, launch/insurance, spectrum, engineering/equipment, debt, SBC,
and diluted common residual. It keeps subscribers, service revenue, backlog,
OCF, and buybacks out of normalized owner cash until service collection,
constellation reserve, replacement, leverage, and per-share cash joins are
evidenced. This is D-201; the lane remains qualified, unranked, and
satellite-connectivity-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The new [connected-operations IoT valuation/liquidity workbench](combined-investment-research-connected-operations-iot-valuation-liquidity-workbench-2026-09-18.md)
adds Samsara as a distinct connected-device and physical-workflow lane,
separate from enterprise workflow software, satellite connectivity, industrial
uptime, and equipment rental. It tests ARR and renewal, device activation and
replacement, inventory, cellular/cloud/AI cost, implementation, support,
commissions, customer ROI, SBC, capex, and diluted common residual. It keeps
ARR, non-GAAP margin, AI adoption, OCF, FCF, and buybacks out of normalized
owner cash until hardware renewal, GAAP cash, customer ROI, and per-share cash
joins are evidenced. This is D-202; the lane remains qualified, unranked, and
connected-operations-iot-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The new [facility services and building operations valuation/liquidity workbench](combined-investment-research-facility-services-valuation-liquidity-workbench-2026-09-18.md)
adds ABM Industries as a distinct outsourced facility-operations lane, separate
from construction, industrial distribution, environmental services, healthcare,
and recurring route businesses. It tests staffing, wage recovery, bookings,
receivables and unbilled work, claims, technical mix, equipment, acquisitions,
contingent consideration, leases, debt, and diluted common residual. It keeps
revenue, bookings, adjusted EBITDA, OCF, and buybacks out of normalized owner
cash until billing, service, acquisition-return, and cash-per-site joins are
evidenced. This is D-203; the lane remains qualified, unranked, and
facility-services-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The new [industrial gases and project-capital valuation/liquidity workbench](combined-investment-research-industrial-gases-project-capital-valuation-liquidity-workbench-2026-09-18.md)
adds Air Products as a distinct mature industrial-gas and clean-energy project
lane, separate from generic materials and chemicals. It tests on-site and
merchant gas contracts, utilization, energy pass-through, maintenance capital,
hydrogen projects, JV funding, partner support, non-recourse debt, project
cancellations, separation obligations, dividends, and diluted common residual.
It keeps adjusted operating income, contract visibility, OCF, and project
spending out of normalized owner cash until core-return, project-funding,
parent-liquidity, and per-share cash joins are evidenced. This is D-204; the
lane remains qualified, unranked, and industrial-gases-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The new [mission-critical public-safety workflow valuation/liquidity workbench](combined-investment-research-mission-critical-public-safety-workflow-valuation-liquidity-workbench-2026-09-18.md)
adds Motorola Solutions as a distinct institutional safety and response-
workflow lane, separate from defense mission systems, passive connectivity, and
general networking. It tests radio and broadband networks, dispatch,
video/evidence, cybersecurity, managed services, backlog acceptance,
implementation, acquisitions, earnouts, goodwill, debt, SBC, and diluted
common residual. It keeps backlog, software/services growth, adjusted EPS,
OCF, and buybacks out of normalized owner cash until acceptance, collection,
acquired-return, support-cost, and per-share cash joins are evidenced. This is
D-205; the lane remains qualified, unranked, and mission-critical-workflow-
cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [insurance risk and brokerage valuation/liquidity workbench](combined-investment-research-insurance-risk-brokerage-valuation-liquidity-workbench-2026-09-18.md)
extends Chubb, Aon, and Marsh McLennan while keeping carrier underwriting and
policyholder liabilities separate from fee-led brokerage and advisory cash. It
tests premiums, claims, reserves, reinsurance, float, statutory capital,
commission/fee collection, receivables, talent, acquisitions, debt, pensions,
and dilution. It keeps premiums, float, combined ratio, organic growth, and
reported OCF out of normalized owner cash until claims or fee-settlement and
common-residual joins are evidenced. This is D-176; the lane remains qualified,
unranked, and insurance-risk-brokerage-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The new [rail network valuation/liquidity workbench](combined-investment-research-rail-network-valuation-liquidity-workbench-2026-09-18.md)
adds Union Pacific through carloads, price/mix, fuel, labor, service, safety,
maintenance and capacity capital, terminals, technology, debt, and the proposed
Norfolk Southern combination. It keeps operating ratio, pricing, reported OCF,
dividends, and buybacks out of normalized owner cash until network renewal,
collection, merger obligations, and diluted common residual are joined. This is
D-177; the lane remains qualified, unranked, and rail-network-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The new [regional and commercial banking valuation/liquidity workbench](combined-investment-research-regional-banks-valuation-liquidity-workbench-2026-09-18.md)
extends PNC, Truist, U.S. Bancorp, and Regions through deposit beta, loan
underwriting, credit losses, securities/liquidity, merger repair, payments
investment, CET1 capital, and tangible-common value. It does not apply an
industrial OCF framework to banks and keeps NII, ROTCE, deposits, loan growth,
CET1, dividends, and buybacks out of normalized owner cash until company-
specific capital, credit, and diluted common-residual joins are evidenced. This
is D-175; the lane remains qualified, unranked, and regional-bank-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [built-environment channel valuation/liquidity workbench](combined-investment-research-built-environment-channels-valuation-liquidity-workbench-2026-09-17.md)
now extends Core & Main, Watsco, Builders FirstSource, and Ferguson into
separate waterworks, HVAC replacement, builder-workflow, and contractor-repair
valuation, reinvestment, liquidity, and thesis-breaker objects. It keeps sales,
branch counts, adjusted EBITDA, repair mix, and reported OCF out of normalized
owner cash until inventory settlement, acquisition return, maintenance/growth
capital, debt, and diluted common residual are joined. This is D-157; the lane
remains qualified, unranked, and channel-cohort-and-working-capital-
normalization-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [participation platform valuation/liquidity workbench](combined-investment-research-participation-platform-valuation-liquidity-workbench-2026-09-17.md)
now routes Roblox into a separate cohort, creator-payout, virtual-economy,
trust-and-safety, governance-cost, liquidity, and dilution object. It keeps
DAUs, hours, bookings, revenue growth, developer activity, and reported FCF
out of normalized owner cash until bookings-to-collection, developer
settlement, payer and age cohorts, infrastructure, safety, SBC replacement,
debt, and diluted common residual are joined. This is D-158; the lane remains
qualified, unranked, and cohort-monetization-and-governance-cost-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [agricultural-inputs and forest-products valuation/liquidity workbench](combined-investment-research-agricultural-inputs-forest-products-valuation-liquidity-workbench-2026-09-17.md)
now routes CF Industries and West Fraser as separate nitrogen-to-food and
wood-products-to-housing physical commodity objects. It keeps production,
adjusted EBITDA, OCF, FCF, repurchases, and dividends out of normalized owner
cash until realized-price/netback or lumber-price/mix, plant/mill uptime,
maintenance and modernization, project/offtake return, debt, and diluted
common residual are joined. This is D-159; the lane remains qualified,
unranked, and commodity-cycle-and-replacement-normalization-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The [asset-management platforms valuation/liquidity workbench](combined-investment-research-asset-management-platforms-valuation-liquidity-workbench-2026-09-17.md)
now routes BlackRock, Blackstone, and Brookfield as separate public-markets,
private-markets, and operating-real-asset objects. It keeps AUM, flows,
fee-related earnings, distributable earnings, carried interest, owned-asset
income, insurance capital, and adjusted EPS out of normalized common-owner cash
until fee collection, realizations, compensation, leverage, legal-entity
claims, and dilution are joined. This is D-160; the lane remains qualified,
unranked, and fee-realization-and-legal-entity-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [private-markets fee, carry, and credit-platform valuation/liquidity workbench](combined-investment-research-carlyle-fee-carry-private-credit-valuation-liquidity-workbench-2026-09-18.md)
adds The Carlyle Group as D-308, separating fee-earning AUM, FRE, realized versus
accrued carry, private-credit losses, partner allocations, available capital,
parent liquidity, debt, and diluted common residual from existing asset-manager
objects. The lane remains qualified, unranked, and owner-cash-open; completion
remains `12 of 13 proven; CA-06 partial`.

The [builder cloud and inference valuation/liquidity workbench](combined-investment-research-builder-cloud-valuation-liquidity-workbench-2026-09-17.md)
now routes DigitalOcean into a separate builder-cloud and AI-inference object.
It keeps ARR, RPO, AI customer ARR, revenue growth, and reported OCF out of
normalized owner cash until collection, RPO conversion, inference capacity
cost, hardware/data-center commitments, customer cohorts, debt, SBC
replacement, and diluted common residual are joined. This is D-161; the lane
remains qualified, unranked, and AI-capacity-and-RPO-normalization-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [merchant power and generation valuation/liquidity workbench](combined-investment-research-merchant-power-generation-valuation-liquidity-workbench-2026-09-17.md)
now routes Constellation, Exelon, NRG, and Vistra as separate clean-generation,
regulated-wires, customer-backed-power, and merchant-fleet objects. It keeps
MW, availability, adjusted EBITDA, FCFbG, signed load, and PPAs out of
normalized owner cash until generation or regulated collection, hedge/PPA
settlement, project funding, maintenance, acquisitions, debt, and diluted
common residual are joined. This is D-162; the lane remains qualified,
unranked, and availability-recovery-and-project-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [industrial procurement valuation/liquidity workbench](combined-investment-research-industrial-procurement-valuation-liquidity-workbench-2026-09-17.md)
now routes Applied, MSC Industrial, and Grainger as separate technical,
plant-floor, and high-touch/digital procurement objects. It keeps sales,
customer counts, branches, vending, and reported OCF out of normalized owner
cash until engineered-service collection, vending/In-Plant economics,
inventory and supplier settlement, fulfillment, acquisition return, debt, SBC,
and diluted common residual are joined. This is D-163; the lane remains
qualified, unranked, and embedded-service-and-working-capital-normalization-
open. Completion remains `12 of 13 proven; CA-06 partial`.

The [managed-care payer valuation/liquidity workbench](combined-investment-research-managed-care-payer-valuation-liquidity-workbench-2026-09-17.md)
now routes UnitedHealth and Cigna as separate risk-bearing benefits, claims,
pharmacy, reserve, policy, trust, and dilution objects. It keeps revenue,
membership, MCR, adjusted EPS, SG&A, and OCF out of normalized owner cash until
premium/service collection, claims paid and unpaid, reserve development,
pharmacy economics, provider payments, cyber, capital, debt, and diluted common
residual are joined. This is D-164; the lane remains qualified, unranked, and
claims-pharmacy-and-legal-entity-cash-open. Completion remains `12 of 13
proven; CA-06 partial`.

The [frontier company-packet valuation/liquidity workbench](combined-investment-research-frontier-company-packets-valuation-liquidity-workbench-2026-09-17.md)
now routes Host Hotels, F5, Veralto, and Caterpillar as separate property,
application-control, measurement, and installed-base objects. It keeps
RevPAR/FFO, ARR, OCF conversion, backlog, dealer inventory, finance
receivables, asset-sale gains, acquisition cash, and capital returns out of
normalized owner cash until company-specific collection, replacement capital,
claims, debt, and diluted residual are joined. This is D-165; the lane remains
qualified, unranked, and property-control-software-measurement-installed-base-
cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [networking-control valuation/liquidity workbench](combined-investment-research-networking-control-valuation-liquidity-workbench-2026-09-17.md)
extends Arista Networks and Ciena through AI-fabric control, deferred-revenue
normalization, backlog conversion, acceptance, inventory quality, acquisitions,
and dilution. It keeps revenue, orders, backlog, deferred revenue, reported
OCF, and buybacks out of normalized owner cash until same-entity collection,
required reinvestment, funding, claims, and diluted common residual are joined.
This is D-170; the lane remains qualified, unranked, and networking-control-
cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [defense and mission-systems valuation/liquidity workbench](combined-investment-research-defense-mission-systems-valuation-liquidity-workbench-2026-09-17.md)
extends CACI, Leidos, and Northrop Grumman through funded-backlog conversion,
cleared labor, contract assets, cost-to-complete estimates, program loss
provisions, acquisitions, pension, and dilution. It keeps backlog, awards,
adjusted EBITDA, and reported OCF out of normalized owner cash until program
delivery, collection, required reinvestment, funding obligations, and diluted
common residual are joined. This is D-171; the lane remains qualified,
unranked, and defense-mission-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The [freight and logistics valuation/liquidity workbench](combined-investment-research-freight-logistics-valuation-liquidity-workbench-2026-09-17.md)
now routes C.H. Robinson and UPS as contrasting asset-light brokerage and
asset-heavy parcel/network objects. It keeps gross billed revenue, shipment or
package counts, adjusted FCF, disposal proceeds, and reported OCF out of
normalized owner cash until shipper/carrier or labor settlement, working-
capital normalization, fleet/network capital, transformation, acquisitions,
debt, and diluted common residual are joined. This is D-167; the lane remains
qualified, unranked, and shipment-density-and-network-reinvestment-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [travel and lodging platforms valuation/liquidity workbench](combined-investment-research-travel-lodging-platforms-valuation-liquidity-workbench-2026-09-17.md)
now routes Airbnb, Booking, Marriott, Hilton, and Sunstone as distinct
marketplace, brand/loyalty, and property-owner objects. It keeps GBV, bookings,
rooms, pipeline, RevPAR, FFO, loyalty points, contract fees, host/supplier
payouts, property renewal, and common cash out of normalized owner cash until
booking/property collection, settlement, loyalty and contract claims,
replacement capital, debt, and diluted common residual are joined. This is
D-168; the lane remains qualified, unranked, and marketplace-brand-property-
and-loyalty-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [branded consumer staples valuation/liquidity workbench](combined-investment-research-branded-consumer-staples-valuation-liquidity-workbench-2026-09-17.md)
now routes Coca-Cola, PepsiCo, Brown-Forman, and Colgate-Palmolive as separate
beverage, food/distribution, premium-spirits, and habitual/pet-care objects. It
keeps unit cases, price/mix, brand revenue, FCF, dividends, and buybacks out of
normalized owner cash until sell-through/collection, bottler or distributor
settlement, inventory and working capital, brand/plant/aging reinvestment,
acquisition return, debt, and diluted common residual are joined. This is D-169;
the lane remains qualified, unranked, and volume-price-channel-and-
reinvestment-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The [packaged-food, brand-repair, and household-value valuation/liquidity workbench](combined-investment-research-packaged-food-brand-repair-valuation-liquidity-workbench-2026-09-18.md)
adds General Mills as D-306, separating packaged-food, pet-food, and foodservice
volume, trade spending, household penetration, inventory, brand/plant capital,
restructuring, debt, and diluted common residual from the existing staple models.
The lane remains qualified, unranked, and owner-cash-open; completion remains `12 of 13 proven; CA-06 partial`.

The [athletic brand, channel-balance, and inventory-repair valuation/liquidity workbench](combined-investment-research-nike-brand-channel-inventory-valuation-liquidity-workbench-2026-09-18.md)
adds NIKE as D-310, separating wholesale/direct sell-through, traffic/conversion,
product mix, inventory, markdowns, tariff recovery, brand investment, debt, and
diluted common residual from existing retail and staple models. The lane remains
qualified, unranked, and owner-cash-open; completion remains `12 of 13 proven; CA-06 partial`.

The [environmental-services valuation/liquidity workbench](combined-investment-research-environmental-services-valuation-liquidity-workbench-2026-09-17.md)
now routes Waste Management, Republic Services, Casella, and Clean Harbors as
separate national-route, regional-landfill, recycling/RNG, and hazardous-
treatment objects. It keeps adjusted FCF, route density, landfill capacity,
sustainability projects, acquisitions, closure obligations, and environmental
liabilities out of normalized owner cash until collection, replacement capital,
claims, debt, and diluted common residual are joined. This is D-166; the lane
remains qualified, unranked, and route-capacity-liability-and-replacement-
cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The new [regulated water infrastructure valuation/liquidity workbench](combined-investment-research-regulated-water-valuation-liquidity-workbench-2026-09-17.md)
adds American Water Works through renewal and compliance capex, rate-case lag,
customer contributions, collections, affordability, PFAS/lead obligations,
acquisitions, debt, dividends, and dilution. It keeps connections, rate-base
plans, revenue, and OCF-less-capex out of normalized owner cash until regulatory
recovery, customer payment, required renewal, environmental claims, and diluted
common residual are joined. This is D-172; the lane remains qualified,
unranked, and regulated-water-cash-open. Completion remains `12 of 13 proven;
CA-06 partial`.

The new [biopharma franchise valuation/liquidity workbench](combined-investment-research-biopharma-franchise-valuation-liquidity-workbench-2026-09-17.md)
adds Regeneron through Dupixent and EYLEA concentration, collaboration
settlement, R&D and clinical replacement, manufacturing, patent defense,
pricing, litigation, SBC, and dilution. It keeps product sales, collaboration
revenue, pipeline milestones, and reported OCF out of normalized owner cash
until collection, replacement-cost, claims, funding, and diluted common
residual are joined. This is D-173; the lane remains qualified, unranked, and
biopharma-franchise-cash-open. Completion remains `12 of 13 proven; CA-06
partial`.

The shared QoE and cash-quality panels now include URI as a separate
asset-backed capacity lane. Stated liquidity, receivables collateral, fleet
purchases, sale proceeds, parent cash, URNA transfer restrictions, and lifecycle
return remain distinct; the populated borrowing-base/NOLV certificate remains
missing. This improves Q-13 method coverage without promoting capacity or
resale to owner cash. Completion remains `12 of 13 proven; CA-06 partial`.

The valuation/liquidity stress matrix now carries URI as a distinct
physical-capacity rental lane. Its valuation object is cohort-level rental
yield, utilization, useful life, resale, and replacement—not consolidated FCF
alone. The H1 bridge of `$3.305B` OCF, `$2.885B` rental/non-rental purchases,
and `$706M` equipment-sale proceeds is retained as reported cash evidence, while
the `$2.999B` stated liquidity, `$2.802B` ABL capacity, `$1.779B` receivables
collateral, borrowing-base eligibility, and URNA transfer restrictions remain
separate funding and owner-availability gates. This is D-136. Completion remains
`12 of 13 proven; CA-06 partial`.

The valuation and execution layers now separate PBF's completed June 2026
2028-note redemption from the September 14 conditional notice and September
17 issuance of 2032 exchangeable notes. The still-pending redemption carries a
calculated `$519.690M` principal-plus-premium floor before accrued interest;
the issued financing reports approximately `$533.6M` of net proceeds and its
dilution must be modeled separately. The June source/use and post-redemption
liquidity evidence is not reused as September settlement proof or refinancing
NPV. This is D-137.
Completion remains `12 of 13 proven; CA-06 partial`.

The shared QoE and cross-sector cash-quality panels now carry the same PBF
separation: June's completed redemption is a source/use fact, while September's
2032 exchangeable financing is issued but the 2030-note settlement remains
pending, with a `$519.690M` pre-interest floor, fee/tax/ABL questions, and
exchangeable dilution. This keeps the financial-shenanigans prompt tied to a
concrete reconciliation instead of counting issuance proceeds or an unsettled
redemption as recurring project economics. This is D-138. Completion remains
`12 of 13 proven; CA-06 partial`.

The [healthcare access valuation/liquidity workbench](combined-investment-research-healthcare-access-valuation-liquidity-workbench-2026-09-17.md)
now extends the healthcare route through business-specific valuation objects,
reinvestment burdens, funding stresses, and thesis breakers. It separates
UnitedHealth/Cigna claims and reserve economics from DaVita treatment and NCI
cash, Option Care therapy collection, Addus labor/payer economics, BrightSpring
acquisition/interest/SBC burden, and Enhabit's private-company boundary. This is
D-139; the cohort remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The new healthcare workbench is now linked from both shared Q2 control panels,
so its payer, treatment, infusion, labor, acquisition, and private-transition
denominators route into the common QoE and cash-quality review without being
pooled. This is D-140; the healthcare route remains qualified and its
same-entity cash joins remain open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [UnitedHealth Q2 medical-cost-payable roll-forward pass 2](annual-report-unitedhealth-q2-2026-medical-cost-payable-rollforward-pass-2.md)
adds the filing's same-entity six-month liability/payment arithmetic: `$148.847B`
of reported medical costs, `$149.320B` of medical payments, `$38.930B` ending
medical costs payable, `$26.5B` IBNR, and `$1.250B` favorable prior-year
development. It strengthens the payer cash-quality diagnostic but does not
provide a segment/legal-entity claims waterfall or common-owner cash bridge.
The cohort remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Cigna Q2 unpaid-claims and cash bridge pass 2](annual-report-cigna-q2-2026-unpaid-claims-cash-bridge-pass-2.md)
adds a second payer-specific same-period bridge: `$15.825B` of Cigna
Healthcare incurred claims, `$14.834B` paid claims, `$5.228B` ending unpaid
claims, and `$268M` favorable prior-year development. It also preserves the
broader receivable-factoring boundary (`$1.5B` sold, `$0.9B` uncollected, and
`$0.3B` collected but not remitted). This strengthens payer cash-quality proof
without closing risk-adjustment, pharmacy/service, legal-entity, or common-owner
cash allocation. The cohort remains qualified, unranked, and owner-cash-open.
Completion remains `12 of 13 proven; CA-06 partial`.

The [ordinary-finance valuation/liquidity workbench](combined-investment-research-ordinary-finance-valuation-liquidity-workbench-2026-09-17.md)
now extends JPMorgan, American Express, and Capital One from credit-quality
observations into loss-adjusted valuation objects, required capital, funding
stress, and filing-based breakers. It keeps deposits, billed business,
pre-provision earnings, reserve releases, integration costs, and exceptional
gains separate from distributable common economics. This is D-141; the cohort
remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [integrated oil and gas valuation/liquidity workbench](combined-investment-research-integrated-oil-gas-valuation-liquidity-workbench-2026-09-17.md)
now extends ConocoPhillips and Exxon Mobil from current-period production and
cash diagnostics into company-specific through-cycle valuation, replacement,
liquidity, and thesis-breaker objects. It keeps upstream/LNG separate from
integrated downstream and trading economics and does not promote production,
segment earnings, mechanical OCF-less-capex, dividends, or repurchases into
normalized owner cash. This is D-151; the lane remains qualified, unranked,
and cycle-and-replacement-open. Completion remains `12 of 13 proven; CA-06
partial`.

The [power-grid valuation/liquidity workbench](combined-investment-research-power-grid-valuation-liquidity-workbench-2026-09-17.md)
now extends NextEra/FPL, AEP, and Duke from customer-cash and regulatory
diagnostics into company-specific valuation, reinvestment, liquidity, and
thesis-breaker objects. It keeps FPL category recovery, AEP large-load/tariff
obligations, and Duke's co-owned Anderson County project separate, and does
not promote approved recovery, signed load, capacity, OCF, debt capacity, or
tax-credit proceeds into common-owner cash. This is D-152; the lane remains
qualified, unranked, and collection-and-return-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [materials, chemicals, and steel valuation/liquidity workbench](combined-investment-research-materials-chemicals-steel-valuation-liquidity-workbench-2026-09-17.md)
now extends Ecolab, Sherwin-Williams, and Nucor from current-period control
points and cash-quality diagnostics into company-specific valuation,
reinvestment, liquidity, and thesis-breaker objects. It keeps embedded
chemistry/service, coatings/distribution, and steel capacity separate and does
not promote revenue, volume, EBITDA, OCF, price/mix, buybacks, or dividends
into normalized owner cash. This is D-153; the lane remains qualified,
unranked, and cycle/acquisition/capex-owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [consumer-goods valuation/liquidity workbench](combined-investment-research-consumer-goods-valuation-liquidity-workbench-2026-09-17.md)
now extends Burlington, Ollie's, and Lowe's through store-level valuation,
inventory and markdown quality, replacement capital, debt/lease claims,
household stress, and filing-based breakers. It keeps tariff refunds, sales,
store counts, OCF-less-capex, and repurchases out of normalized owner cash
until the mature-store and common-residual joins are evidenced. This is D-142;
the cohort remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [medical-devices valuation/liquidity workbench](combined-investment-research-medical-devices-valuation-liquidity-workbench-2026-09-17.md)
now extends Stryker, Intuitive Surgical, and Henry Schein through acquisition-
cohort return, installed-base utilization, lease collection, securitization,
restructuring, funding, and diluted-share tests. It keeps procedure growth,
systems, adjusted EPS, OCF, and repurchases out of normalized owner cash until
the company-specific collection and residual joins are evidenced. This is
D-143; the cohort remains qualified, unranked, and owner-cash-open. Completion
remains `12 of 13 proven; CA-06 partial`.

The authoritative deliverable registry now matches the verifier's actual
scope: its completion-audit row records 98 deliverables rather than the stale
23-deliverable wording. The registry, prose audit, and verifier now agree on
the same count; this is D-144 and changes consistency, not completion status.
Completion remains `12 of 13 proven; CA-06 partial`.

The shared QoE and cross-sector cash-quality panels now include Enhabit as a
distinct private-transition lane, preserving its final public Q1 baseline and
routing payer, labor, settlement, refinancing, debt, capex, sponsor, and
legal-entity questions separately. This improves cross-sector method coverage
without creating a pooled healthcare or owner-cash ranking. Completion remains
`12 of 13 proven; CA-06 partial`.

The Enhabit route now adds the CMS FY2027 hospice reimbursement breaker: a
`2.3%` payment update, `$36,174.75` aggregate cap, `1.7%` quality-reporting
penalty, and nine-measure service/spending variation index. These are external
payer and quality inputs, not Enhabit-specific cash or post-close collection
proof. Completion remains `12 of 13 proven; CA-06 partial`.

The Enhabit care-delivery pass records its final public Q1 baseline—`$35.2M`
OCF, `$(2.6M)` investing cash, `$(26.6M)` financing cash, and a `$17.7M`
non-recurring settlement gain—alongside payer and segment-labor controls. The
May 15 acquisition converted Enhabit to private status, so no public Q2 series
is inferred; post-close collection, labor, debt, capex, and sponsor claims
remain open. Completion remains `12 of 13 proven; CA-06 partial`.

The Walmart Q2 capex/refund pass adds gain-contingency recognition and segment
comparability controls: the `$2.9B` refund is realized and recorded against
cost of sales, while February 2026 overhead-allocation changes and channel mix
limit pooled segment comparisons. These improve CA-06 safeguards without
proving recurring margin or owner cash. Completion remains
`12 of 13 proven; CA-06 partial`.

The Target Q2 cash-quality pass adds a supplier-finance lifecycle and
financing-claim control: eligible obligations rose from `$3.0B` to `$3.2B`,
H1 accounts payable supplied `$612M` of mixed cash, and `$1.0B` of unsecured
debt was repaid in April. The filing says eligible supplier-finance balances
are not actual early payments, so these remain timing and claim evidence rather
than extra OCF deductions. Completion remains `12 of 13 proven; CA-06 partial`.

The TJX cash-flow classification pass now records that settlement proceeds are
inside operating activities, while the `$390M` prepaid/other-current-assets
movement is mixed and cannot substitute for gross settlement cash. This
strengthens the CA-06 double-counting and QoE control; gross cash, legal
expense, tax, and maintenance-capital allocation remain open. Completion
remains `12 of 13 proven; CA-06 partial`.

The public-use allocation pass now separates BHP's `$4.3B` Antamina receipt
from the approximately `$4.8B` combined asset-realization figure and group
net-debt outcome. No public transaction-level allocation to debt repayment,
growth capital, tax, dividends, or legal-entity residual cash was found. The
Q-03 public-use stop rule is stronger, while recurring BHP-PMPA receipt and
return proof remain open. Completion remains `12 of 13 proven; CA-06 partial`.

The BHP FY2026 20-F now strengthens Q-03 with completed recipient-side proof:
BHP records the Wheaton stream as completed, `$4.3B` of upfront consideration
received, and the proceeds in net financing cash-flow analysis. This closes the
upfront receipt and issuer-period-classification boundary, but recurring
BHP-PMPA credit issuance, sale/receivable, bank collection, tax, and
facility-allocation proof remain open. Completion remains
`12 of 13 proven; CA-06 partial`.

The healthcare-access current-period refresh now adds primary-source medical-
cost, claims-liability, reserve-development, treatment-volume, and disclosed
FCF controls for UnitedHealth, Cigna, and DaVita. These strengthen the care-
delivery route but leave affordability, outcomes, reimbursement durability,
labor, maintenance capital, NCI, and common-owner cash open. Completion remains
`12 of 13 proven; CA-06 partial`.

The healthcare-access refresh now adds Option Care and Addus primary-source
cash, receivable, repurchase, service-revenue, office-footprint, and gross-
margin controls. Alternate-site and home-care economics remain qualified until
therapy-level collection/margin, labor/rate, branch-return, quality, and
common-owner cash joins are available. Completion remains
`12 of 13 proven; CA-06 partial`.

BrightSpring now adds primary-source complex-patient pharmacy/provider cash,
acquisition, interest, SBC, adjusted-EBITDA, leverage, and divestiture-perimeter
controls to the healthcare-access cohort. Continuing-operations conversion,
labor, service margin, debt, and common-owner cash remain open. Completion
remains `12 of 13 proven; CA-06 partial`.

The broad-technology handoff now adds Fortinet and Cloudflare as distinct
service/platform cash-quality cases: deferred revenue, billings, RPO, SBC,
infrastructure, capitalized software, acquisitions, and debt remain separate
claims. The cohort remains no-ranking and owner-cash-open; completion remains
`12 of 13 proven; CA-06 partial`.

The healthcare-distribution handoff now carries current-period McKesson,
Cencora, and Cardinal evidence into the reader-facing audit: working-capital
funding and Apollo preferred claims, acquisition-heavy specialty expansion,
opioid/legal cash, capex, debt, and shareholder distributions remain separate
period-labeled claims. The cohort remains no-ranking and normalized-owner-cash
open; completion remains `12 of 13 proven; CA-06 partial`.

The healthcare-access and care-delivery cluster is now distinct from the
healthcare-distribution cohort in the reader-facing audit. Benefits/pharmacy,
dialysis, infusion, home-care, and skilled-care routes retain separate
reimbursement, medical-cost, claims, labor, quality, trust, regulation, and
legal-entity cash questions. Scale and adjusted income remain qualified
observations; completion remains `12 of 13 proven; CA-06 partial`.

The digital-infrastructure handoff now carries Equinix and Digital Realty's
current-period capital burden into the reader-facing audit: PP&E, development,
recurring capex, acquisitions, ATM equity, debt, backlog, signed rent, and
partner/fund claims remain separate. Project commencement, stabilized NOI,
maintenance allocation, and diluted common-owner residual remain open; the
cohort remains no-ranking and completion remains
`12 of 13 proven; CA-06 partial`.

The insurance broker/carrier handoff now carries Chubb's current-period
underwriting cash and reserve/liability surface into the reader-facing audit:
premium growth, operating cash, unpaid losses, reinsurance recoverables,
claims paid, favorable development, catastrophe exposure, and statutory capital
remain separate claims. Reserve adequacy, collectibility, legal-entity
availability, and common-owner residual remain open; completion remains
`12 of 13 proven; CA-06 partial`.

The exchange-and-information-infrastructure handoff now carries CME and S&P
Global's current-period control surfaces into the reader-facing audit:
collateral and guaranty-fund balances, clearing liquidity, disposition and
acquisition proceeds, intangible amortization, SBC, volume, market-data growth,
and reported FCF remain separate claims. Clearing-risk, acquired-cohort return,
organic cash, and diluted common-owner residual remain open; completion remains
`12 of 13 proven; CA-06 partial`.

The restaurant-franchise handoff now carries McDonald's current franchised-
sales and owner-cash perimeter into the reader-facing audit: systemwide and
franchised sales, royalty/fee collection, franchisee health, closures,
delinquency, remodel/technology reinvestment, OCF, PP&E, repurchases, and
dividends remain separate claims. Franchisee cash conversion and normalized
common-owner residual remain open; completion remains
`12 of 13 proven; CA-06 partial`.

The QoE/financial-shenanigans panel now covers the expanded healthcare,
digital-infrastructure, insurance/statutory, exchange/information, and
restaurant lanes in addition to the earlier current-sector controls. Each
signal has a named reconciliation and promotion boundary; the pooled
Beneish-style score remains intentionally unassembled because legal entities,
periods, denominators, and accounting perimeters are not comparable.
Completion remains `12 of 13 proven; CA-06 partial`.

The cross-sector cash-quality panel now includes the expanded healthcare,
digital-infrastructure, insurance/statutory, exchange/information, and
restaurant lanes with explicit distortion and owner-cash questions. It remains
a qualified control map, not a pooled valuation or forensic ranking; each lane
retains its own legal entity, period, denominator, and promotion object.
Completion remains `12 of 13 proven; CA-06 partial`.

The valuation/liquidity stress matrix now carries the expanded healthcare,
digital, insurance, exchange, and restaurant lanes through business-specific
valuation objects, reinvestment burdens, liquidity stresses, and filing-based
thesis breakers. It remains an expectation and stress workbench rather than
proof of normalized owner cash or a cross-sector ranking. Completion remains
`12 of 13 proven; CA-06 partial`.

The ordinary-finance handoff now adds JPMorgan, American Express, and Capital
One as distinct loss-normalization cases: exceptional gains, billed activity,
credit costs, write-offs, reserve releases, integration, capital, and dilution
remain separate. The cohort remains no-ranking and common-owner-cash-open;
completion remains `12 of 13 proven; CA-06 partial`.

The consumer-goods handoff now adds Burlington, Ollie's, and Lowe's as a
qualified household-value cohort: tariff-supported cash, inventory/store
investment, service capital, shareholder distributions, and bond maturities
remain separate owner-cash claims. The cohort remains no-ranking and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.

The integrated oil-and-gas handoff now adds ConocoPhillips and Exxon as
distinct physical-asset cases: ConocoPhillips combines `$11.729B` H1 OCF,
`$5.972B` capital/investments, and declining production; Exxon combines
`$32.260B` OCF, `$12.997B` PP&E additions, and `$3.857B` working-capital use.
Price, replacement, claims, and integrated-margin normalization remain open;
no ranking is promoted. Completion remains `12 of 13 proven; CA-06 partial`.

## Latest execution audit — D-102 through D-103

The materials refresh and Q-03 filing follow-up add two bounded extensions:

- Ecolab and Nucor now carry explicit working-capital, capex, acquisition/SBC,
  project-capital, and cycle controls; neither is promoted to through-cycle
  owner cash or a cross-sector return ranking.
- Wheaton's Q2 segment note adds combined Antamina sales and operating cash for
  Q2 and H1, strengthening the same-entity denominator while preserving the
  BHP-versus-Glencore allocation boundary. The BHP-specific credit issue,
  sale/receivable, bank collection, tax, and facility-allocation objects remain
  open.

These updates improve the evidence chain without changing the completion
status: `12 of 13 proven; CA-06 partial`.

The private-credit route now surfaces the Bear Financing Q2 source boundary in
the execution audit: the official Accordia verification document reports an
aggregate `$7.371492B` bond base but omits the detailed `90231*-AA-0` row. The
absence is not a disposal, repayment, or settlement signal; the lender,
borrower, receipt, debt-service, and liability-cost joins remain open. The
completion status remains `12 of 13 proven; CA-06 partial`.

The industrial-conversion handoff now surfaces Sterling, WESCO, and Fastenal
as distinct qualified cases: Sterling's `$110.623M` residual follows visible
H1 growth uses, WESCO shows a Q2 cash-conversion decline, and Fastenal shows
69.4% OCF conversion of net income. These remain diagnostic project and
distribution controls; acquisition cohorts, maintenance burden, claims, and
common-owner cash are not proven. The completion status remains
`12 of 13 proven; CA-06 partial`.

The CA-06 route now has a quantified TJX settlement and tariff-support
boundary: the Q2 FY2027 filing reports a non-recurring `$419M` gain net of
legal expenses, places receipt of related amounts in the quarter ended May 2,
2026, and quantifies `$331M` of IEEPA refunds, `$112M` of related incremental
bonus accruals, and a `$219M` net Q2 benefit. This improves the period-matched
temporary-support control, but gross settlement cash/legal expenses, tax,
refund recurrence, maintenance-capital allocation, and common-owner cash
remain open. The completion status remains `12 of 13 proven; CA-06 partial`.

The Q-13 URI review records a searched-negative for the June 30, 2026 public
10-Q: covenant availability is disclosed, but no populated NOLV or equipment
borrowing-base schedule appears in the checked filing. This sharpens the stop
rule and leaves the private certificate, source-to-purchase, and fleet-return
objects open. The completion status remains `12 of 13 proven; CA-06 partial`.

The power-grid current-period handoff now carries the distinct FPL, AEP, and
Duke funding surfaces into the reader-facing execution audit: FPL `$5.388B`
OCF versus `$5.780B` capex, AEP `$3.421B` versus `$5.606B` construction, and
Duke `$4.272B` versus `$8.240B` capex. These remain qualified regulatory and
customer-cash routes; billing, collection, paid-capital allocation, and
common-owner return are not promoted. Completion remains
`12 of 13 proven; CA-06 partial`.

The PBF refinancing route now includes the Q2 2026 period-matched
post-redemption liquidity boundary: more than `$3.5B` operational liquidity,
more than `$800M` cash, and approximately `$2.7B` revolver availability. The
source/use and completed-redemption proof is stronger, but trustee settlement,
accrued interest, cash priority, fees/tax, borrowing-base composition, and
refinery-level return remain open. Completion remains
`12 of 13 proven; CA-06 partial`.

The consistency pass reconciles the prose deliverable count with the
authoritative deliverable CSV and verifier: `90` deliverables are checked. The
stale `74` wording was corrected; this changes documentation consistency only
and not the completion result, which remains `12 of 13 proven; CA-06 partial`.

The [DaVita Q2 treatment-to-cash bridge pass 2](annual-report-davita-q2-2026-treatment-to-cash-bridge-pass-2.md)
adds a qualified care-site denominator: H1 `14.256M` treatments, `$416.71`
revenue per treatment, `$811M` operating cash, `$197M` maintenance capital,
`$75M` development capital, `$150M` NCI distributions, and `$396M` disclosed
FCF. The filing also shows `$1.561B` of NCI subject to put provisions and
incremental debt funding. This closes the treatment-to-disclosed-FCF
diagnostic, but payer collection, risk-contract economics, debt, tax, NCI-put,
and common-owner allocation remain open. Completion remains
`12 of 13 proven; CA-06 partial`.

The [Option Care Q2 therapy-collection and margin bridge pass 2](annual-report-option-care-q2-2026-therapy-collection-margin-bridge-pass-2.md)
adds payer-category revenue, therapy-mix, gross-profit, billing-delay,
unbilled-receivable, working-capital, capex, debt, lease, tax, and repurchase
controls. The Q2 filing reports `$529M` H1 gross profit, `18.5%` Q2 gross
margin, `$154.9M` earned but unbilled receivables, and an estimated `$55M` CID
therapy-mix headwind. Payer-level collection and therapy-level margin remain
open; repurchases and inventory release are not promoted to owner cash.
Completion remains `12 of 13 proven; CA-06 partial`.

The [Addus Q2 payer, wage, branch, and cash bridge pass 2](annual-report-addus-q2-2026-payer-wage-branch-cash-bridge-pass-2.md)
adds a distinct home-care control: personal-care gross margin of `28.3%`, H1
government/MCO payer mix of `50.0%`/`47.3%`, Illinois rate and wage references,
`$92.376M` H1 OCF, `$145.123M` ending AR, `$12.182M` HomeCourt acquisition cash,
and `$3.050M` PP&E/technology cash. It explicitly preserves the filing's AR and
payroll/AP timing warning and keeps the `$77.144M` OCF-less-acquisition/PP&E
screen out of normalized owner cash. This is D-145; Addus is qualified for the
payer/wage/branch diagnostic, while branch return, normalized collection, and
common-owner residual remain open. Completion remains `12 of 13 proven; CA-06
partial`.

The [BrightSpring Q2 pharmacy/provider cash bridge pass 2](annual-report-brightspring-q2-2026-pharmacy-provider-cash-bridge-pass-2.md)
adds a second distinct care-delivery denominator: H1 Pharmacy Solutions and
Provider Services revenue of `$6.579B` and `$908M`, segment EBITDA of `$490M`,
`$166.859M` OCF, `$1.139B` AR, `$575M` inventory, `$50.576M` PP&E, `$42.203M`
acquisitions, `$810.908M` Community Living sale proceeds, `$320.491M` debt
repayment, and `$120M` repurchases. It keeps the divestiture proceeds and
adjusted-earnings/SBC burden out of recurring common-owner cash. This is D-146;
BrightSpring is qualified for the pharmacy/provider diagnostic, while service-
line collection, acquisition return, debt/SBC replacement, and common residual
remain open. Completion remains `12 of 13 proven; CA-06 partial`.

The full named-verifier sweep now passes across the Q-03 metal-credit and
receivable boundaries, URI collateral and lifecycle routes, PBF settlement and
exchangeable financing, Ares/Frontline, Q-10 macro, retail TJX/Target/Walmart,
power-grid, insurance, asset-backed, integrated-oil, exchange, materials,
digital-real-estate, promotion-ledger, and expansion QoE controls. The Apollo
Q2 PDF route also confirms the `$799M` fund-distribution observation and the
`$2.040B` broader investing line. This is D-147; it strengthens verification
coverage without changing any evidence grade or closing CA-06.

The URI public-source perimeter now also includes the official Q2 2026 investor
presentation. It adds fleet, branch, productivity, maintenance, and
capital-allocation context but no eligible-collateral, advance-rate, NOLV,
reserve, or populated borrowing-base schedule. This is D-148; it strengthens
the searched-negative boundary without promoting Q-13 or changing the
`12 of 13 proven; CA-06 partial` result.

Target's August 14, 2026 Form 8-K and five-year credit agreement now add a
post-quarter-end financing boundary: Target Corporation is the borrower on
`$4.0B` of aggregate commitments, with proceeds permitted for general
corporate purposes. The agreement proves a legal funding backstop and use-of-
proceeds perimeter, but the checked materials do not prove a draw, receipt,
operating allocation, repayment, or common-owner cash. This is D-149; it
strengthens CA-06/Q-06 liquidity stress without closing the maintenance,
settlement, lease/tax, service-cost, or owner-cash gates. Completion remains
`12 of 13 proven; CA-06 partial`.

The [restaurant-franchise valuation/liquidity workbench](combined-investment-research-restaurant-franchise-valuation-liquidity-workbench-2026-09-17.md)
now extends the CAVA, Restaurant Brands International, Wingstop, Yum,
McDonald's, and Chipotle lane through company-specific valuation objects,
reinvestment denominators, franchisee/company-store liquidity stresses, and
filing-based thesis breakers. It keeps the FY2025 and H1 2026 periods separate
and does not promote systemwide sales, royalties, OCF, dividends, or
repurchases into normalized owner cash. This is D-150; the restaurant lane
remains qualified, unranked, and owner-cash-open. Completion remains
`12 of 13 proven; CA-06 partial`.
The [Avista hydro-sensitive regulated utility valuation/liquidity workbench](combined-investment-research-avista-hydro-sensitive-regulated-utility-valuation-liquidity-workbench-2026-09-18.md)
adds a genuinely different utility perimeter: hydro and weather exposure, mixed
electric-and-gas customers, rate-base recovery, large-customer procurement, capex,
wildfire and reliability obligations, debt, and dilution. Utility EPS, guidance,
capex, and customer counts remain diagnostic until collection and common-residual
joins are evidenced. This is D-334; the lane remains qualified, unranked, and
owner-cash-open. Completion remains `12 of 13 proven; CA-06 partial`.
