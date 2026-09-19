# Combined Investment Research Next-Evidence Queue

Research date: `2026-09-17`

This queue records the next source-backed tests required to move the three
pilots upward in proof grade. It is intentionally a queue of documents and
reconciliations, not a list of unsupported assumptions.

## Queue operating rule

Every refresh must classify the result before changing a proof grade:

1. `source-not-found`: the named document or route is not available in the
   checked source perimeter; the claim remains open and no negative conclusion
   is allowed.
2. `searched-negative`: the named source was available and the requested field
   was searched, but the field was not disclosed; the missing field and search
   perimeter must be recorded.
3. `evidence-insufficient`: the field was found, but it does not join the
   required denominator, legal entity, period, receipt, or return; preserve the
   observation without promoting the claim.
4. `promotion-ready`: the source, denominator, period, legal route, and
   reconciliation required by the upgrade test are joined and independently
   reproducible.

The current Investor Day result is `evidence-insufficient` for Q-02's
reserve-backed curve and `searched-negative` for Q-01's BHP-only settlement
object within the archived presentation, Wheaton Q2 filing packet, and BHP
FY2026 materials. It is not evidence that no settlement occurred.

The structured queue CSV carries the same `result_class` for each Q-row, and
the pilot verifier rejects a classification drift between the machine-readable
queue and this operating rule.

| Queue ID | Pilot | Missing evidence | Exact next document or source | Upgrade test | Current status |
| --- | --- | --- | --- | --- | --- |
| Q-01 | Wheaton–Antamina | BHP-only metal-credit quantity and receipt | The current Wheaton Antamina portfolio page, archived September 16, 2026 Corporate Presentation, BHP February streaming announcement, Wheaton closing/Q1/Q2 exhibits, and the next Wheaton 10-Q/10-K, BHP production disclosure, or settlement statement; see the [post-event source boundary](capital-flow-wheaton-antamina-local-packet-settlement-search-boundary-2026-09-15.md), [post-Q2 public-search refresh](capital-flow-wheaton-antamina-post-q2-public-search-refresh-2026-09-16.md), and [extraction checklist](capital-flow-wheaton-antamina-investor-day-extraction-checklist-2026-09-15.md) | Reconcile BHP entitlement, actual recovered ounces, 90% payability, smelter weights/assays, PBND, BHP metal-credit quantity, invoice, quotation-period realized price, settlement date, and cash or receivable entry | First BHP-PMPA delivery is explicitly confirmed in Wheaton's Q2 MD&A; the expanded official-source search and the September 16 post-Q2 refresh confirm a searched-negative result for a BHP-only invoice, metal-credit quantity, settlement date, or receipt account. The current portfolio page, closing/Q1/Q2 exhibits, BHP announcement, and archived presentation confirm contract terms, distinguish the BHP `100M` threshold from the legacy Glencore `140M` threshold, and supply the profile proxy. The Q2 table reports `2.319M` combined attributable ounces produced and `2.063M` sold; those remain combined, while BHP-only metal-credit quantity, settlement, and receipt cash remain open |
| Q-02 | Wheaton–Antamina | Reserve-backed delivery curve | BHP reserve/production schedule or independent reserve report; checked BHP FY2026 Form 20-F, the July 2026 official BHP operational review, and Antamina NI 43-101 remain source boundaries because the public BHP materials provide historical BHP-interest silver and FY2027 copper guidance but no forward silver schedule, while the technical report lacks a BHP-tranche annual silver table | Build BHP tranche delivery curve through the 100M-ounce threshold and life-of-mine tail | Partial upgrade: BHP-share P&P reserve quantity and threshold comparison, five-quarter BHP-interest production/sales proxy, 16.67–18.52 year mechanical threshold-timing screen, 10.95–12.17 year reserve-constrained payable-duration ceiling, reserve-capped `$35/$60/$90` silver-price recovery frontier, and a new portfolio-versus-Antamina reserve-life denominator boundary now exist; the official review confirms FY2026 BHP-interest silver production/sales and FY2027 copper guidance but still does not close the reserve-backed annual silver delivery curve |
| Q-03 | Wheaton–Antamina | Financed after-tax return | Wheaton term-loan schedule, tax allocation, and lender waterfall | Recalculate IRR/NPV after interest, tax, debt service, and delivery timing | Partial upgrade: the direct credit agreement now also requires all facility proceeds to partially finance the Antamina Mine Silver Stream Acquisition; exact term-loan margin, official September 14 SOFR, actual H1 financing cash flows, company-level all-in sensitivity, a 0–100% after-tax financed allocation frontier, and a separate 0–100% maturity-bullet coverage screen are source-backed; exact draw-dollar, seller-account, Antamina tax/interest, repayment, and return allocation remain open |
| Q-04 | Retail cohort | Common-period margin and inventory normalization | Next TJX, Target, and Walmart quarterly filings plus annual vendor-income notes | Separate price, volume, mix, markdown, freight, shrink, inventory, payables, and temporary support | Partial upgrade: the cross-cohort balance screen shows TJX inventory/payable changes of `+$565M`/`+$449M` and a `-$116M` mechanical signal, Target `+$945M`/`+$684M` and `-$261M`, and Walmart `+$2.749B`/`+$1.257B` and `-$1.492B`; the new supplier-finance roll-forward shows Target `+$0.2B`/`+$0.3B` and Walmart `+$0.4B`/`+$0.7B` comparative obligation movements, without treating them as cash; full operating-asset/liability cash normalization remains open |
| Q-05 | Retail cohort | Maintenance versus growth capital | Annual capex schedules and company capital-allocation disclosures | Allocate property spending by maintenance, remodel, new stores, fulfillment, and platform; recalculate owner cash | Partial upgrade: annual category references and latest forward-spending context now exist; TJX's H1 FY2027 capex is `$1.159B` by segment—Marmaxx `$690M`, HomeGoods `$146M`, TJX Canada `$190M`, TJX International `$133M`—and its FY2027 guide is approximately `$2.2B–$2.3B`; TJX still does not split those segment amounts between replacement/maintenance and growth; TJX states ordinary maintenance/repairs are expensed as incurred; Walmart's FY2026 10-K likewise states normal repairs and maintenance are expensed as incurred and major improvements are capitalized, while its H1 filing discloses exact categories; Target's FY2025 10-K also states repair and maintenance costs are expensed as incurred and reports a `$2.835B` FY2025 cash-after-property screen, while its official 2026 plan adds approximately `$5B` of investment, more than 30 new stores, more than 130 remodels, supply-chain/technology projects, and more than `$1B` of food-and-beverage investment; Target's September official update confirms the planned 2026 store openings were completed while preserving the no-dollar-split boundary; the H1 maintenance split remains open |
| Q-06 | Retail cohort | Attached-service cash conversion | Target Roundel/card/other notes and Walmart advertising/membership/ecosystem disclosures | Join revenue, allocated costs, working capital, capex, tax, and cash collection without adding revenue one-for-one | Partial upgrade: Target payer/accounting boundary, current Q2 aggregate merchandise/fulfillment burden and temporary tariff support, Walmart segment operating denominator, ecosystem composition, H1 and annual 0–100% sensitivity frontiers, and current Walmart advertising/membership growth signals are now source-backed; service-level cash conversion remains open |
| Q-07 | Apollo–Athene | Apollo parent receipt of subsidiary distributions | Apollo parent cash-flow note, subsidiary dividend schedule, intercompany eliminations, or regulatory receipt | Tie Athene/fee-entity distributions to unrestricted HoldCo cash and parent common claims | Partial upgrade: FY2025 `ParentCompanyMember` reports `$750M` dividends received reconciled to `$750M` subsidiary-distribution proceeds; Athene Q2 reports `$32M` distributions to parent in Q2 and `$110M` in H1 alongside separate `$187M`/`$375M` common-dividend lines; the current Q2 ACRA/ADIP table adds `$145M`/`$47M` Q2 contributions/distributions and `$271M`/`$301M` H1 totals, but these are ADIP flows rather than AGM receipts; the [fee-rollforward boundary](capital-flow-apollo-athene-fee-rollforward-boundary-2026-09-15.md) adds a qualified `$779M` mechanical management-fee settlement implication from opening payable plus expense less ending payable, without treating it as Apollo cash; a new Q2 0–100% attribution frontier quantifies `$0M–$110M` without assigning it to AGM cash; Apollo Q2 identifies AHL/AAM distributions and intercompany transfers as primary HoldCo cash sources; the mechanically rerunnable accession-level XBRL check finds 29 dividend-related facts and zero upstream-receipt/intercompany/affiliate facts; Athene also discloses a direct AHL-to-AGM `$500M` note route with `$279M` receivable outstanding and zero reciprocal payable, but no draw dates or use-of-proceeds join; the new [note balance-movement boundary](capital-flow-apollo-athene-intercompany-note-balance-movement-boundary-2026-09-15.md) separates the `$52M` period-end increase from cash principal; the new [Q2 upstream source-to-destination bridge](capital-flow-apollo-athene-q2-upstream-source-destination-bridge-2026-09-15.md) makes the non-additive legal-entity perimeter explicit; the new [parent-use coverage frontier](capital-flow-apollo-athene-parent-use-coverage-frontier-2026-09-15.md) shows that even 100% attribution would cover only 7.68% of selected H1 Apollo parent uses; the refreshed [HoldCo liquidity boundary](capital-flow-apollo-q2-holdco-liquidity-intercompany-boundary-2026-09-15.md) adds a parent-summary balance-sheet context of `$3.412B` cash, `$3.467B` net investments, `$1.511B` performance-fee receivable, `$(95M)` net clawback payable, `$(5.762B)` debt, and `$2.533B` net balance-sheet value, but explicitly does not convert those balances into unrestricted or Athene-funded cash; the [Q2 parent-receipt source refresh](capital-flow-apollo-athene-q2-parent-receipt-refresh-2026-09-16.md) rechecks the current Apollo and Athene filings and preserves the searched-negative AGM-only receipt boundary while adding AHL's statement that U.S. insurance subsidiaries are not currently planned to pay dividends to their parents and that Bermuda distributions face statutory, surplus, regulatory, and financial-strength-rating constraints; segment, restricted, and VIE cash pools remain separated; AGM receiving account, parent-only cash-flow join, intercompany elimination, and common-owner residual remain open |
| Q-08 | Apollo–Athene | Legal-entity capital and credit return | Next Athene statutory Schedule D/BA schedules and statutory income exhibits | Match named holdings to income, impairment, funding cost, liability spread, and realized cash return | Partial upgrade: summary statutory bridge, full-range `8,648`-row Schedule D population, section-total reconciliation within one dollar after the coupon-decimal/NAIC-marker correction, corrected same-CUSIP AMAPS and Concord row bridges, same-CUSIP lot-chronology boundary, proportional liability-cost sensitivity, a period-matched FY2025 segment spread screen, blank-column parser boundary, named-route concentration screen, and current Q2 AMAPS 1 exposure of `$2.544B` versus `$2.550B` at year-end now exist; the refreshed wrapper denominator implies approximately `$92.1M` of mechanical H1 cost-of-funds allocation against the reconciled bond base, but this is not observed asset-level cost; lot identifiers, settled receipt, trustee remittance, period-matched asset-level liability-cost allocation, borrower cash, and parent receipt remain open |
| Q-09 | Apollo–Athene | ARI borrower repayment and collateral cash | ARI portfolio report, borrower notices, trustee reports, or next Athene investment filing; see the [buyer-side acquisition boundary](capital-flow-apollo-athene-ari-buyer-side-acquisition-boundary-2026-09-16.md), [closing-payment mechanics boundary](capital-flow-apollo-athene-ari-closing-payment-mechanics-boundary-2026-09-16.md), [post-close proof search boundary](capital-flow-apollo-athene-ari-post-close-proof-search-boundary-2026-09-16.md), and [cash-perimeter delta boundary](capital-flow-apollo-athene-ari-cash-perimeter-delta-boundary-2026-09-16.md) | Reconcile the `$8.7B` ARI transfer to borrower receipts, repayment, losses, fees, and Athene/Apollo allocation | Partial upgrade: transaction terms specify `99.7%` of total loan commitments net of asset-specific CECL reserves, exclude two loans with combined principal of `$146M` expected to repay before closing, and state no financing contingency; the definitive agreement now identifies the Closing Date Calculation Notice, seller-designated wire account(s), payoff-recipient wires, signed settlement statement, 120-day final accounting/true-up, possible designated buyer affiliates, and borrower notices directing debt service to Buyer or its designee; a bounded search of the ARI completion announcement, ARI/Apollo/Athene Q2 filings, agreement, and proxy is `searched-negative` for the executed settlement statement, wire confirmations, true-up, named designee, and borrower receipt ledger; the seller-side numeric bridge isolates a `$897.267M` mechanical difference between approximately `$8.6B` sale consideration and `$9.497267B` aggregate commercial-mortgage repayment/sale proceeds, with the separate `$67.578M` subordinate/other-lending line excluded and no attribution forced; ARI Q2 2026 confirms zero seller loans after closing, the `$46M` Chicago Hotel Loan repayment, `$335M` transferred-loan CECL write-off, and `$2.6M` sale-discount loss; Athene Q2 reports the April 24 buyer completion and approximately `$8.7B` purchase, plus a buyer-side `$48.291B` commercial-mortgage balance versus `$39.071B` at year-end, a `$9.220B` aggregate increase directionally consistent with a material acquisition, and a `$1.027B` 90-days-past-due/non-accrual subset at `$695M` fair value; the Athene Q2 earnings release separately classifies `$7.8B` of 2Q'26/LTM AUM outflows as ARI-related and `$5.0B` as Intel-related, but AUM outflow is not cash settlement or borrower return; none of these buyer portfolio figures is ARI-attributed; executed settlement, wire, designated-buyer, borrower receipts, collateral cash, loan-level attribution, true-up, and parent allocation remain open |
| Q-10 | All pilots | Through-cycle macro validation | Subsequent filings plus official inflation, rates, credit, and policy data; see the [through-cycle causal-test protocol](combined-investment-research-through-cycle-causal-test-protocol-2026-09-16.md) | Test whether the mapped macro mechanism changes demand, margin, funding, liquidity, or valuation as predicted, with repeated aligned periods and confound controls | Partial upgrade: official 2020–2026 regime panel now joins same-period 2026 company data and a multi-period retail cash-screen bridge; the new protocol defines dependent observables, principal confounds, promotion requirements, and filing-based breakers for all three pilots; the September 16 FOMC decision, August CPI, and July personal-income/outlays release refresh the current-regime inputs; the new 18-row retail panel diagnostic adds descriptive real-wage/CPI splits but is pooled and confounded; through-cycle causality remains open |
| Q-11 | Power-grid customer cash | FPL Distribution Inspection billing determinants and category receipts | Florida PSC Docket `20260010-EI` non-confidential discovery responses, Form 4P/Form 5P workpapers, and later SPPCRC actual/estimated filings; see the [FPL receipt proof chase](capital-flow-fpl-billing-determinant-category-receipt-proof-chase-pass-1.md) and the [official PSC source refresh](capital-flow-fpl-distribution-inspection-official-psc-source-refresh-2026-09-16.md) | Join category recovery to rate-class determinants, billed or collected revenue, source-of-funds allocation, and bounded return | `searched-negative`: the official 2026 SPP, SPPCRC, and Docket `20260010-EI` Form 6P filings now provide program cost/activity (`180,000` poles; `$92.1M` 2026 actual/estimated total cost as of February 2026; `$94.1M` 2027 projection), rate-class allocation method, bill period, and future true-up route, but disclose no Distribution Inspection-specific billing determinant, receipt ledger, or source-of-funds allocation. A narrowed 2026-09-17 local-source check found no additional non-confidential category billing, collection, or funding schedule; the lane is parked at `hold-with-strong-route-visible` and should be reopened only for a discovery response, supporting workpaper, or final true-up with a joinable category allocation. The new [AEP/Duke customer-security bridge](capital-flow-aep-duke-large-load-customer-security-quality-bridge-2026-09-16.md) adds primary-filed customer-security and financial-protection controls: AEP Texas reports approximately `45 GW` of LOAs, `40 GW` prospective Batch Zero load, and approximately `$2B` of financial security, while Duke describes financial protections in data-center service agreements. These improve the burden and status ladder but do not create a billed/collected-cash bridge |
| Q-12 | Insurance statutory named-asset income | Named-asset settlement, liability-cost, and remittance support for Apollo/Athene and Accordia | Statutory Schedule D/BA income and disposal exhibits plus trade confirmations, custodian/trustee reports, and legal-entity cash-flow schedules; see the [insurance statutory next dig](capital-flow-insurance-statutory-named-asset-income-next-dig-pass-1.md), the [MF1 public SEC document refresh](capital-flow-apollo-athene-mf1-public-sec-document-refresh-2026-09-16.md), and the [Accordia matched-disposal proof packet](capital-flow-kkr-global-atlantic-accordia-matched-disposal-owned-interest-proof-packet-pass-1.md) | Join legal entity, CUSIP or issuer, income/proceeds, liability cost, remittance/waterfall, and bounded return | `evidence-insufficient`: Apollo/Athene and Accordia now have named legal-entity rows, Accordia coordinate-extracted disposal columns, and a three-row owned-interest/disposal join; the MF1 public filing strengthens the Apollo-affiliated wrapper and collateral route, but settlement, lot continuity, liability-adjusted spread, borrower cash, Athene remittance, and final return remain open |
| Q-13 | Asset-backed collateral and borrowing base | Populated United Rentals borrowing-base certificate and fleet source-to-purchase return support | Current or closing Borrowing Base Certificate, collateral availability report, NOLV appraisal, reserve/L-C schedule, and fleet purchase/funding records; see the [URI collateral proof chase](capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.md), [reporting-regime boundary](capital-flow-uri-abl-borrowing-base-reporting-regime-boundary-2026-09-16.md), [collateral-eligibility bridge](capital-flow-uri-abl-collateral-eligibility-bridge-2026-09-17.md), and [structured Q-13 next-source package](data/capital-flow-uri-q13-next-source-package-2026-09-18.csv) | Join facility balance, eligible collateral, NOLV, reserves, Combined Availability, source-to-purchase use, fleet cash conversion, and lifecycle return | `evidence-insufficient`: the ABL agreement now supplies the eligibility filters, U.S./Canadian borrowing-base formula, certificate cadence, trigger logic, and agent-adjustment controls; URI's Q2 2026 10-Q supplies $2.802B capacity net of letters of credit, $1.666B debt, $2.999B total liquidity, and seasonal debt variation, but populated certificate components, legal availability, source-to-purchase allocation, and lifecycle return remain undisclosed |

The 2026-09-17 SEC-source recheck also located the June 18, 2026 Amendment
No. 18 to URI's receivables purchase agreement. It confirms the AR-facility
legal route but adds no populated purchaser availability schedule, receivables
report, borrowing-base certificate, or live Combined Availability calculation.
Q-13 remains `evidence-insufficient` for certificate-grade availability and
lifecycle return.

## Move-on execution queue — industrial uptime

The industrial lane is a controlled next-cycle cohort, not a new Q-row and not
a promotion of the original thirteen tests. Its field-level source and status
are maintained in the [industrial evidence register](data/combined-investment-research-industrial-uptime-evidence-register-2026-09-17.csv).
The exact source requests and promotion tests are maintained in the [industrial
promotion action register](data/combined-investment-research-industrial-uptime-promotion-action-register-2026-09-17.csv).

| Lane | Current evidence | Next joinable object | Promotion boundary |
| --- | --- | --- | --- |
| WESCO/Fastenal conversion | H1 2026 revenue, operating income, OCF, property spending, working-capital bridge, and QoE diagnostics | Same-period collection, maintenance/service cost, supplier-finance, lease/tax, and diluted-owner claim | Do not promote OCF less property spending to normalized owner cash |
| Sterling project conversion | Signed/combined/future backlog layers, acquisition contribution, H1 OCF less capex, percentage-of-completion diagnostics | Project-level backlog-to-revenue-to-collection roll-forward with contract assets, retainage, estimate changes, and acquisition cash | Do not promote unsigned awards, future phases, or acquired growth to funded organic backlog |
| URI fleet conversion | OEC, gross rental capex, used-equipment proceeds, reported liquidity and facility split | Populated borrowing-base certificate, NOLV/reserves, utilization, replacement-capex, and source-to-purchase records | Do not promote facility-availability proxy or fleet resale to legal availability or lifecycle return |

All three lanes inherit the same move-on rule: if the decisive document is not
publicly available after a targeted search, record the missing object and move
to the next joinable candidate without substituting a nearby proxy.

### Q-11 recovery-mechanics update — 2026-09-17

The public May 1, 2025 FPL SPPCRC testimony now adds an explicit regulatory
recovery formula to the Q-11 route: capital revenue requirements include
debt/equity return grossed up for tax on average monthly net investment,
including CWIP, plus depreciation/amortization, with allocation to retail
customers through separation factors. The filing reports `$859.244393M` of
total jurisdictional 2026 requirements. This upgrades the mechanics boundary,
not the searched-negative category-receipt or source-of-funds boundary.

### Q-03 return-input schema — 2026-09-16

The new [Q-03 full-return input schema](capital-flow-wheaton-antamina-q03-full-return-input-schema-2026-09-16.md)
separates the return model into 13 required fields across contract, delivery,
price, cash receipt, funding, financing, tax, reinvestment, and return. It
labels each field as observed, partial, missing, or not assembled and names the
exact upgrade document. This makes the after-tax financed IRR/NPV promotion rule
executable without substituting company-level debt, tax, or OCF values for an
Antamina-specific cash flow.

### Q-03 funding-mix control — 2026-09-17

The Q-03 schema now separates a partial funding control from the missing
funds-flow allocation. The planned `$1.9B` cash, `$1.5B` term-loan, and `$0.9B`
revolver mix reconciles to the `$4.3B` PMPA payment; H1 corporate cash flow
also reports `$2.700B` drawn, `$728M` repaid, and `$29.886M` interest paid.
These observations tighten source, timing, and burden inputs but do not prove
which dollars reached the BHP seller account or how principal, interest, and
tax should enter an Antamina-specific return.

The 2026-09-17 live official-source recheck of Wheaton's Q2 results release,
MD&A, and transaction exhibits returned the same Q-03 boundary: the announced
cash/term-loan/revolver funding envelope and H1 corporate debt movements remain
visible, but no closing funds-flow, seller-account confirmation,
facility-specific draw allocation, asset-specific repayment, or Antamina tax
and interest schedule was found. Q-03 remains `full-return-inputs-incomplete`
for the checked public perimeter.

The [Q-03 metal-credit receipt boundary](capital-flow-wheaton-antamina-q03-metal-credit-receipt-boundary-2026-09-17.md)
now makes the settlement object precise: BHP and Wheaton document metal-credit
settlement with no physical delivery, while Wheaton's Q2 filing reports only
combined Antamina production, sales, and undelivered payable metal. The next
promotion object is therefore a BHP-specific credit issuance, credit-sale,
receivable, and bank-receipt ledger—not a physical shipment. This is a
mechanism and request-target upgrade; it does not promote combined ounces to
BHP cash or close the financed after-tax return.

A further targeted public-source pass checked the SEC-hosted Wheaton Q2
earnings release and MD&A, the filed term-facility exhibit, the Wheaton
transaction exhibit, and BHP's official transaction materials. It located no
new facility-level borrowing notice, seller-account confirmation, repayment
ledger, or Antamina-specific tax schedule beyond the artifacts already cited
above. The result is a confirmed move-on boundary, not a negative claim about
private closing records: the next Q-03 promotion object remains a joinable
funds-flow or allocation document.

### Q-04–Q-06 retail owner-cash recheck — 2026-09-17

The latest SEC-source pass rechecked TJX FY2026, Target Q2 2026, and Walmart
Q2 FY2027. Their reported operating-cash/property bridges and working-capital
disclosures remain usable, but no filing supplied the missing
maintenance-versus-growth split, matched interim lease/tax cash, or
attached-service cost/collection allocation. Q-04 through Q-06 therefore stay
`partial`; the next promotion object is a period-matched allocation or cash
schedule, not a larger reported-OCF screen. The [retail promotion action
register](data/combined-investment-research-retail-promotion-action-register-2026-09-17.csv)
now records the exact source, denominator, join, and promotion test for each
of the three rows.

The [retail H1 owner-cash denominator handoff](combined-investment-research-retail-h1-owner-cash-denominator-handoff-2026-09-17.md)
now joins the current OCF/property screens to supplier-finance timing, support,
SBC, capex growth floors, annual lease/tax context, and attached-service gaps.
It confirms the non-double-counting rule and leaves Q-04–Q-06 at `partial`:
the next useful source is a matched allocation or payment schedule, not another
reported-OCF screen.

### Q-07 common-owner input schema — 2026-09-16

The [Q-07 common-owner input schema](capital-flow-apollo-athene-q07-common-owner-input-schema-2026-09-16.md)
separates Apollo/Athene earnings, legal-entity cash, upstream distributions,
AGM receipt, intercompany elimination, note financing, legal availability,
senior claims, fee cash, parent uses, dilution, and the final residual. The
current public perimeter is searched-negative for an AGM-only receiving-account
line, while the controlled elimination schedule remains missing. The
`$0M–$110M` parent-attribution frontier therefore remains sensitivity-only
until the receipt account, elimination, and common-owner waterfall are
source-backed.

### Q-07 note-balance date control — 2026-09-17

The financing perimeter now distinguishes the AHL-to-AGM note's period-end
balances: `$280M` at March 31, 2026, `$279M` at June 30, 2026, and `$227M` at
December 31, 2025. The apparent `$279M`/`$280M` difference is therefore a
reporting-date distinction, not a same-date conflict. The one-million-dollar
sequential change remains a balance movement and is not promoted to a draw,
repayment, bank receipt, or common-owner cash. The June 30 Q2 10-Q's
no-outstanding-balance statement applies to Athene's current and previous
external credit facilities, which remains a separate instrument and direction
from the AHL receivable from AGM. The next required sources remain the note
ledger, dated draw/repayment notices, bank confirmations, elimination schedule,
and AGM use-of-proceeds records.
Apollo's FY2025 parent-only Schedule I now adds a two-sided December 31, 2025
control: AGM reports no note receivable from AHL and a `$227M` note payable to
AHL, matching AHL's `$227M` receivable. This upgrades direction and amount
corroboration only; it does not close receipt, chronology, or use-of-proceeds
evidence.
The Apollo Q2 2026 10-Q and its financial supplement were also checked for a
June 30 parent-only AGM note payable to AHL. They expose consolidated and
fund/elimination views but no separately identified parent-only note line or
receiving account. The `$279M` June 30 figure therefore remains Athene-side
evidence only; the December 31, 2025 two-sided control is still the latest
cross-entity corroboration. This is a public-source boundary, not evidence
that no June 30 AGM payable existed.

The 2026-09-17 SEC-source recheck of the Apollo and Athene Q2 filings found no
new AGM-only receiving-account, parent-only cash-flow, or controlled
intercompany-elimination record. Q-07 remains `searched-negative` for the
checked public perimeter; the next useful acquisition is a dated receipt or
Schedule I/cash ledger, not a consolidated-cash or source-side distribution
proxy.

### Move-on routing decision — 2026-09-17

The current public-source perimeter is now sufficient to stop repeating the
same searches for Q-01/Q-02, Q-07, Q-11, and the already-checked portions of
Q-12/Q-13. Those lanes remain open, but their next useful inputs are specific
new documents: a BHP-PMPA settlement object or reserve schedule, an AGM receipt
or elimination ledger, an FPL discovery/workpaper or true-up, an MF1 restricted
servicing report, or a populated borrowing-base/NOLV package. Until one of
those documents appears, their current proof grades are preserved.

The next active work should therefore target a joinable denominator or cash
object in Q-03 and CA-06/Q-04–Q-06, followed by dated settlement, repayment,
tax, lease, maintenance-capital, or attached-service allocation evidence. This
routing rule prevents a public-source absence from becoming either an
unsupported negative conclusion or an excuse to broaden the research without
closing a decision-relevant gate.

The queue is complete as a planning control when every row names both a
document and a falsifiable reconciliation. It does not imply that an open row
has been proven.

### Q-06 attached-services refresh — 2026-09-16

The [retail attached-services public-source refresh](combined-investment-research-pilot-02-retail-attached-services-public-source-refresh-2026-09-16.md)
rechecks current Target, Walmart, and TJX disclosures. Target's Roundel,
membership, and marketplace activity; Walmart's membership and advertising
layers; and TJX's exceptional interchange settlement are all visible. The
refresh remains `evidence-insufficient` because allocated service costs,
working capital, capex, tax, collection, and common-owner cash are not joined.
It changes the source perimeter and timing, not the proof grade.

### Q-06 annual frontier handoff — 2026-09-17

The [annual attached-services cash frontier](combined-investment-research-pilot-02-retail-annual-attached-services-cash-frontier-2026-09-17.md)
aligns Target FY2025's `$2.063B` and Walmart FY2026's `$6.750B` reported
attached-service pools with the annual retail denominator screen. Its 0–100%
columns are hypothetical conversion sensitivities only; they do not create
service cash, allocated cost, collection, tax, capex, working-capital, or
legal-entity evidence. Q-06 remains `evidence-insufficient`, and the next
promotion object is still a same-period service-level collection and burden
schedule.

The [retail attached-services legal-owner and burden bridge](combined-investment-research-retail-attached-services-legal-owner-burden-bridge-2026-09-17.md)
now makes the Q-06 control point explicit: Target's TD-owned card receivables,
Roundel classification choices, and Walmart's mixed membership-and-other pool
must remain separate from consolidated owner cash. The bridge improves legal
owner and burden attribution while keeping service cash `evidence-insufficient`.

The Target Q2 10-Q search also finds a consolidated `$959M` gift-card liability
and a disclosed H1 issuance/redemption roll-forward. This improves the general
customer-funding and revenue-timing perimeter, but it is not service-specific
and does not alter the Q-06 result.
The [structured gift-card boundary](combined-investment-research-pilot-02-target-gift-card-liability-boundary-2026-09-16.md)
reconciles `$1.197B + $376M - $614M = $959M` and keeps issuance separate from
observed owner cash.

### CA-06 Target current-period recheck — 2026-09-17

The [Target Q2 cash-quality perimeter upgrade](combined-investment-research-target-q2-2026-cash-quality-perimeter-upgrade-2026-09-17.md)
refreshes the six months ended August 1, 2026: `$4.519B` OCF, `$2.404B`
property spending, `$994M` tariff refunds, `$3.2B` supplier-finance-eligible
obligations, `$945M` inventory use, and `$612M` payable support. The filing
still does not disclose matched H1 cash-paid lease or cash-tax lines, a
maintenance-versus-growth split, service-level cost/collection, or a final
common-owner residual. Q-04 through Q-06 remain `partial`/`evidence-insufficient`;
the next promotion object is still a matched allocation or settlement schedule,
not another headline cash-flow screen.

The Walmart Q2 10-Q adds a parallel timing rule: Sam's Club membership fees are
deferred and recognized ratably over the one-year membership term. No
membership-only contract-liability balance or service-level cash schedule is
disclosed, so the observation remains a timing control and does not promote
the `$3.904B` H1 membership-and-other-income figure to owner cash.

TJX's Q2 10-Q adds a comparable `$825M` ending deferred-gift-card balance and
`$963M` of H1 recognized gift-card revenue, while stating that the cards are a
single homogeneous, non-separately-identifiable pool. This sharpens the
customer-funding timing perimeter but does not identify attached-service cash
or alter the Q-06 result.
The same filing dates a separate `$419M` non-recurring interchange-fee
settlement receipt to the quarter ended May 2, 2026; it remains exceptional
cash and is not used as recurring service economics.

Target's official Roundel fact sheet adds an 800-plus-person integrated team,
more than 2,000 vendor relationships, and a management-defined `$2B+` value
claim. These sharpen the control-point and labor-burden map, but “value” is not
defined as revenue, profit, or cash and remains outside the owner-cash model.

The TJX Q2 filing also permits a mechanical H1 cash-after-property screen:
`$3.345B` operating cash flow less `$1.159B` capex equals `$2.186B`. This
improves denominator precision but is not normalized owner cash; the
maintenance/growth split and other burdens remain open.

### Q-08 Concord servicing update — 2026-09-16

KBRA's July 2026 surveillance reports that Concord Series 2024-1 and
Series 2025-1/2/3 notes had received timely interest through the July quarterly
payment date. This is now recorded as `deal-level-servicing-payment-proxy` in
the Apollo ledger. It improves the current debt-service observation, but does
not identify Athene as a recipient, disclose a trustee remittance amount, or
allocate royalty collections, liability cost, principal, or return to the
Athene CUSIP. The controlled-document request remains the required upgrade.

The [current AMAPS 1 exposure boundary](capital-flow-apollo-athene-q2-amaps-current-exposure-boundary-2026-09-16.md)
adds a scale orientation to Q-08: the `$2.544B` June 30 exposure is
approximately `0.810%` of Athene's `$314.090B` net invested assets and
`5.782%` of the `$44.0B` look-through related-party investment population.
These ratios are concentration context only and do not prove ownership,
borrower cash, liability-cost allocation, or realized return.

The [Schedule D residual row-boundary inspection](capital-flow-apollo-athene-statutory-schedule-d-residual-row-boundary-inspection-2026-09-16.md)
confirms that all `61` raw candidates are duplicate or continuation text: `59`
have same-page apparent book values exactly matching already parsed holdings,
including the two largest—`A-1` on page 5904 and `ADVANCE` on page 6023—and the
remaining `NOTE` and `IO` rows are continuation-only non-book fields. None is
added to the holdings total. This closes the raw-candidate omission boundary.
The [aggregate-total reconciliation](capital-flow-apollo-athene-statutory-schedule-d-total-reconciliation-2026-09-16.md)
now permits the section and combined book-value denominator to be used with
the stated dollar-level variance, but does not promote the base to final
income, proceeds, liability-cost, or return proof.

### Q-08 same-CUSIP proceeds screen — 2026-09-17

The corrected statutory row-proof packet now provides a named-asset proceeds
screen across ten same-CUSIP routes: `$2.943066208B` of selected disposal
consideration, of which `$2.930192972B` is classified cash-like, plus
`$93.704267M` of selected disposal interest/dividends. The packet includes
AMAPS 1, Concord, AP Aristotle, Eliant, AA Infrastructure, MF1, and Treasury
routes, while holding mixed transfer rows apart. These amounts are legal-entity
Schedule D row evidence, not bank receipts, borrower repayment, liability-cost
adjusted return, or Apollo parent cash. The next join remains lot continuity,
settlement/custodian evidence, and period-matched funding cost.

### Q-08 SVF II Finco public-search update — 2026-09-16

The [SVF II Finco public-search refresh](capital-flow-apollo-athene-svf-ii-finco-public-search-refresh-2026-09-16.md)
confirms that the CIK `1527469` filing is Athene Holding Ltd.'s 2025 Form
10-K. Its concentration table reports `$2.186B` of SVF II Finco investments,
and the three year-end Schedule D rows for `G7741@-AC-4`, `G7741@-AD-2`, and
`G7741@-AE-0` reconcile to approximately that amount. `G7741@-AC-4` carries a
`$2.090B` aggregate consideration field. The detailed AC-4 rows classify only
`$50.751M` as selected cash-like paydown candidates and approximately
`$2.039B` as tax-free-exchange/transfer holds. This is a stronger
issuer/denominator cross-check but a smaller cash claim and is classified `evidence-insufficient`: it
does not prove a bank settlement, borrower repayment, collateral proceeds,
trustee remittance, liability-cost allocation, or realized return. The next
request is the note/refinancing record, paydown notice, trade confirmation,
custodian ledger, borrower payoff record, and trustee support.
The [row-composition boundary](capital-flow-apollo-athene-svf-ii-finco-row-composition-boundary-2026-09-16.md)
now records the five underlying AC-4 rows and their `$50.751M` cash-like /
`$2.039B` transfer split.

The [Concord 2022-1 public-source refresh](capital-flow-apollo-athene-concord-2022-1-public-source-refresh-2026-09-16.md)
adds a bounded public context route for the `$624.9M` disposal-only
`20633K-AA-6` candidate. The official Concord announcement supports the
music-rights collateral and acquisition-financing context, and independent
statutory statements cross-check the CUSIP. The route remains
`evidence-insufficient` for Athene ownership, settlement, remittance, and
return; the offering memorandum, trustee reports, and exact settlement ledger
remain the next documents.

The [AA Infrastructure Fund 2 public-source refresh](capital-flow-apollo-athene-aa-infrastructure-public-source-refresh-2026-09-16.md)
adds a historical related-entity observation for the approximately `$348.0M`
`00024D-AL-7` candidate. It improves the infrastructure-wrapper map but
remains `evidence-insufficient` for current Athene ownership, settlement,
project cash, and return; current statutory, fund, project, and custodian
records remain required.

The [PK AirFinance public-source refresh](capital-flow-apollo-athene-pk-airfinance-public-source-refresh-2026-09-16.md)
adds a high-leverage platform route for the PAF 2020 disposal candidates:
Apollo acquired the platform and Athene acquired the existing loan portfolio;
PK describes aircraft/engine-secured lending and ABS servicing. The route
remains `evidence-insufficient` for exact CUSIP settlement, borrower cash,
remittance, and return. Offering memoranda, collateral schedules, trustee
reports, and Athene trade/settlement records are the next documents.

The [AOP Finance Partners public-source refresh](capital-flow-apollo-athene-aop-finance-public-source-refresh-2026-09-16.md)
adds a legal-entity and economic-benefit route for the two AOP disposal-only
CUSIPs. Athene's 2021 Form 10-K identifies AOP as a consolidated VIE and
reports `$747M` of AOP investment-fund assets, with Athene receiving the
economic benefits and losses after related-party management and carry. The
2025 statutory candidates total approximately `$684.9M` of consideration and
`$51.8M` of interest/dividend fields. This remains `evidence-insufficient`
for current lot continuity, paydown versus sale, settlement, borrower cash,
liability-adjusted return, and Apollo common-owner cash. AOP offering,
administrator/trustee, custodian, trade-confirmation, and borrower records are
the next documents; AOP II is kept as a separate route.

The [VMC Finance public-source refresh](capital-flow-apollo-athene-vmc-finance-public-source-refresh-2026-09-16.md)
adds a bounded Varde-linked commercial-mortgage route for `91836A-AA-4`, an
approximately `$295.3M` disposal-only Paydown candidate. A later SEC CMBS
term sheet references VMC 2023-PV1 as a previous securitization, but public
sources do not prove the Athene lot, borrower/property cash, settlement,
remittance, liability-adjusted return, or Apollo common-owner cash. The
original offering, mortgage schedule, trustee reports, and Athene custodian
records remain the next documents.

The [ATLAS Funding 1 public-source refresh](capital-flow-apollo-athene-atlas-funding-public-source-refresh-2026-09-16.md)
adds an Apollo-backed structured-credit platform route for two `Redemption 100`
disposal-only candidates totaling approximately `$487.3M`. Apollo describes
ATLAS SP Partners as majority owned by Apollo funds and focused on warehouse
finance and securitization. Exact Athene legal-entity ownership, class-level
collateral, settled redemption, remittance, liability-adjusted return, and
common-owner cash remain open; the Funding 1 offering, waterfall, trustee, and
Athene custodian records are the next documents.

The [AA MMF 1 public-source refresh](capital-flow-apollo-athene-aa-mmf1-public-source-refresh-2026-09-16.md)
adds a `partial-upgrade` for `000249-AA-0`, an approximately `$222.8M`
disposal-only Paydown candidate. Athene regulatory exhibits identify AA MMF 1
Holdco LP and an Apollo Principal Holdings chain, with Apollo's current 10-K
providing a GP cross-check. Exact Ltd-to-Holdco identity, Athene ownership,
settlement, borrower cash, liability-adjusted return, and common-owner cash
remain open; organizational documents, offering materials, trustee reports,
and custodian records are next.

The [FASST 2022-S5 public-source refresh](capital-flow-apollo-athene-fasst-2022-s5-public-source-refresh-2026-09-16.md)
adds a `partial-upgrade` for `317384-AA-3`, an approximately `$219.1M`
disposal-only Paydown candidate. Public rating material confirms FASST
2022-S5's mortgage-backed-note class structure, and U.S. Bank's portal provides
a controlled trustee-report route. Athene settlement, loan-level cash,
remittance, liability-adjusted return, and common-owner cash remain open; the
offering, tape, trustee reports, and custodian ledger are next.

The [Apollo Debt Solutions public-source refresh](capital-flow-apollo-athene-apollo-debt-solutions-public-source-refresh-2026-09-16.md)
adds an exact instrument-level route for `03770D-AC-7`: the SEC indenture
confirms CUSIP `03770DAC7`, issuer, 6.700% coupon, July 29, 2031 maturity,
`$600M` initial principal, and U.S. Bank Trust trustee. The new [payment-
observability boundary](capital-flow-apollo-athene-apollo-debt-solutions-payment-observability-boundary-2026-09-16.md)
separates contractual January/July payment mechanics and third-party CUSIP
observability from an executed remittance. The `$215.8M` Athene row remains a
`Various` market-sale candidate; counterparty, settlement, BDC cash, borrower
repayment, liability-adjusted return, and common-owner cash remain open.
Athene trade/custodian records, trustee history, and BDC debt and portfolio
schedules are next.

The issuer bridge also records H1 financing movements: `$398.539M` dividends
paid, `$782.527M` common-stock issuance proceeds, `$4.715B` debt issuance,
`$2.032B` long-term debt repayments, and `$1.617B` net financing cash flow.
These improve issuer-level cash visibility but do not join the Athene candidate
to a settled receipt or Apollo common-owner residual.
The visible financing lines total `$3.067B` before other uses against `$1.617B`
reported net financing cash flow, leaving a `$1.450B` unexplained financing-use
residual. The complete financing statement and notes are now a specific next
reconciliation object; the residual is not assigned to Athene or Apollo.

The companion [coupon-carry sensitivity](capital-flow-apollo-athene-apollo-debt-solutions-coupon-carry-sensitivity-2026-09-16.md)
adds a par-equivalent gross annual carry proxy of approximately `$14.461M` from
the stated `6.700%` coupon and `$215.832M` consideration candidate. This is an
illustrative input only; it does not establish lot continuity, coupon receipt,
settlement, liability cost, or realized return.

The [issuer cash/return bridge](capital-flow-apollo-athene-apollo-debt-solutions-issuer-cash-return-bridge-2026-09-16.md)
adds Q2 2026 issuer-level structured facts, including `$312.890M` of H1 cash
interest paid, `$599.045M` of net investment income, `$857.638M` of cash, and
`$16.568B` of debt face amount. These constrain the BDC funding perimeter but
do not allocate cash or return to Athene's note; trade, custodian, trustee, and
liability-cost records remain the next proof objects.

The [BHP FY2026 payable-silver quantity boundary](capital-flow-wheaton-antamina-bhp-fy2026-payable-silver-quantity-boundary-2026-09-16.md)
adds a BHP-only annual calibration: BHP reports `5.588M` troy ounces of
payable silver in concentrate for its `33.75%` Antamina interest, while the
PMPA states a `90%` payable factor. The table records both a `5.029M` forward
factor application and a `6.209M` reverse-factor gross-equivalent screen, each
only for calibration. Neither is a metal-credit transfer, invoice, settlement,
or receipt, and the BHP/smelter payable convention still requires
reconciliation.

The [AP Hansel public-source refresh](capital-flow-apollo-athene-ap-hansel-public-source-refresh-2026-09-16.md)
produces a `partial-upgrade` for the `G2963@-AA-0` route. Aldar identifies AP
Hansel SPV LLC as wholly owned by Apollo Capital Management, describes the
`2.6M`-square-meter, 20-year land-rights structure, reports Hansel dividends,
and records a February 5, 2025 `$493.226M` Class B share repurchase. The exit
timing overlaps the Athene disposal window, but exact CUSIP settlement,
Athene allocation, proportional participation, liability-adjusted return, and
common-owner cash remain open. Share-transfer, settlement, bank, custodian,
DLSPA, valuation, and allocation records are the next documents.

The [AOP Finance Partners public-source refresh](capital-flow-apollo-athene-aop-finance-public-source-refresh-2026-09-16.md)
adds a legal-entity and economic-benefit route for the two AOP disposal-only
CUSIPs. Athene's 2021 Form 10-K identifies AOP as a consolidated VIE and
reports `$747M` of AOP investment-fund assets, with Athene receiving the
economic benefits and losses after related-party management and carry. The
2025 statutory candidates total approximately `$684.9M` of consideration and
`$51.8M` of interest/dividend fields. This remains `evidence-insufficient`
for current lot continuity, paydown versus sale, settlement, borrower cash,
liability-adjusted return, and Apollo common-owner cash. AOP offering,
administrator/trustee, custodian, trade-confirmation, and borrower records are
the next documents; AOP II is kept as a separate route.

An [official SEC N-PORT observation](capital-flow-apollo-athene-concord-sec-nport-holder-observation-2026-09-16.md)
now independently identifies the Concord 2024-1A security by CUSIP
`20633KAE8` and reports a 200,000-unit position valued at `$197.038M`. This
adds an instrument-level cross-check to Q-08, but the 2024-1A filing cannot be
substituted for the Athene 2025-3A statutory row (`20633K-AN-8`) and does not
close settled-lot, custodian, remittance, receipt, or return evidence.

### Q-01/Q-02 live-source update — 2026-09-16

### Q-01 BHP cash-flow source precision — 2026-09-17

BHP's FY2026 annual report now has a source-precision control for the
recipient-side event: `$4.300B` received on April 2, 2026, `$4.300B` of
streaming-arrangement proceeds in financing cash flow, and `$41M` of reported
streaming-liability settlements. The cash-flow arithmetic reconciles reported
net financing outflow of `$3.280B` to approximately `$(7.539B)` of non-stream
financing lines plus the stream proceeds less settlements. BHP also states the
`33.75%` / `90%` payable tranche, `100M`-ounce threshold, post-threshold
`22.5%` tranche, metal-credit settlement, and absence of a minimum delivery
requirement. This tightens Q-01's date, legal-counterparty, tranche, and
classification controls, but does not identify the BHP-only credits, invoice,
settlement-date allocation of the `$41M`, Wheaton receipt, or Q-02 reserve-
backed annual curve.

The [SEC-hosted term facility credit agreement](capital-flow-wheaton-antamina-credit-agreement-waterfall-boundary-2026-09-16.md)
also upgrades Q-03's financing source perimeter. It names the two Wheaton
borrowers and Bank of Montreal administrative-agent route, sets the `$1.5B`
non-revolving facility and two-year maturity, specifies SOFR-plus-leverage
pricing and maturity repayment, and includes a `0.60:1` capitalization
covenant. It remains a credit-document boundary rather than a PMPA funds-flow
or Antamina-specific repayment allocation.
The targeted public-source search across the agreement, Q1/Q2 reports,
closing announcement, and Q2 statements is `searched-negative` for an executed
drawdown notice, payment instruction, seller-account confirmation, lender
remittance, or asset-specific repayment ledger. This classification applies
only to the checked public perimeter.
The companion [term-maturity cliff screen](capital-flow-wheaton-antamina-term-maturity-cliff-screen-2026-09-16.md)
separates the `$1.500B` term-loan bullet from annual interest expense and
shows it represented approximately `76.06%` of Q2 gross bank debt. This adds a
principal-timing claim to the return model without assigning the debt to
Antamina.

Teck's 2025 Annual Information Form adds an independent Antamina reserve
cross-check: `528.4 Mt` total Proven and Probable reserves and `31.430 Moz`
recoverable silver attributable to Teck's `22.5%` interest, with a 2026
life-of-mine-plan context and an expected mine-life endpoint through `2036`.
The [Teck reserve cross-check](capital-flow-wheaton-antamina-teck-reserve-cross-check-2026-09-16.md)
advances Q-02's source perimeter but remains `evidence-insufficient` because
the Teck denominator is not interchangeable with the BHP `33.75%` tranche and
does not provide the BHP payable, delivery, or settlement curve.
The underlying [Antamina NI 43-101 technical report](https://minedocs.com/28/Antamina-TR-12312024.pdf)
adds a mine-level 2025–2036 schedule context and documents Teck's separate
Franco-Nevada stream precedent, including 29.1 Moz delivered through 2024.
Neither observation supplies the annual BHP/Wheaton payable-silver curve, so
the next reconciliation remains owner tranche → payable factor → annual
production → contract-threshold timing.

### Q-02 forward-profile versus reserve-ceiling cross-check — 2026-09-17

The Investor Day profile of `6.0M` ounces per year for five years and `5.4M`
for ten years implies `57.0M` ounces over the first ten years. Compared with
the mechanical `59.13M` payable-ounce ceiling from `65.7M` contained BHP-
interest ounces at a 90% factor, the profile consumes approximately `96.4%`
of that ceiling and leaves `2.13M` ounces. This is a bounded consistency
screen, not a reserve-backed delivery curve: the profile, reserve definition,
PMPA payability, and settlement ledger are not yet joined.

BHP's FY2026 Note 29 now adds an entity-level [Antamina associate economics
 boundary](capital-flow-wheaton-antamina-bhp-associate-economics-boundary-2026-09-16.md):
 FY2026 Antamina revenue of `$7.473B`, 100% profit of `$3.029B`, BHP
 equity-accounted profit of `$1.022B`, and 100% net assets of `$5.531B`.
 These improve the operator/equity-owner burden denominator, but the aggregate
 `$895M` equity-investment dividend line is not assigned to Antamina and no
 silver-stream, metal-credit, or Wheaton receipt is implied.

The NI 43-101 also supplies a [mine-plan burden schedule](capital-flow-wheaton-antamina-mine-plan-burden-schedule-2026-09-16.md)
for 2025–2036: `$14.681B` of real operating costs and `$4.022B` of nominal
capital costs, with 2036 marked as a partial year. This is useful for an
operator-burden sensitivity and reserve-support screen, but it is not a BHP
silver-tranche cost allocation and cannot be subtracted directly from Wheaton
stream revenue.

BHP's newly available FY2026 public-filing set is represented by the official
[Form 20-F route](https://www.sec.gov/Archives/edgar/data/811809/000119312526354647/bhp-20260630.htm)
and a locally preserved [Form 6-K results artifact](../../raw/primary-sources/capital-flow/bhp/fy2026/bhp-fy2026-20f.htm),
as summarized in the [public-filing boundary memo](capital-flow-wheaton-antamina-bhp-fy2026-annual-report-boundary-2026-09-16.md).
It adds the April 2, 2026 `$4.3B` receipt date, confirms metal-credit
settlement with no physical delivery and no minimum/fixed delivery requirement,
and gives FY2027 copper/zinc guidance. The report also says the stream's future
For metric precision, Wheaton's Q2 operating table separately reports `2.319M`
combined attributable silver ounces produced and `2.063M` sold; the narrative's
`837,000` figure is a silver-ounce-equivalent GEO production increase, not the
BHP-only metal-credit quantity. The combined production/sales figures therefore
do not close Q-01's settlement or receipt requirement.

The 2026-09-17 live official-source recheck of Wheaton's portfolio/Q2 filing
and BHP's FY2026 filing returned the same bounded result: contract terms,
effective date, first-delivery/combined-production observations, and BHP's
`$4.300B` receipt remain visible, but no BHP-only credited ounces, invoice,
settlement price/date, payment account, or receivable entry was found. Q-01's
searched-negative classification is current for the checked public perimeter.
production estimate uses risked reserves/resources that are not yet proved.
These facts strengthen the legal/accounting boundary but do not close the
BHP-only silver quantity, invoice, settlement, receipt, or reserve-backed
annual delivery curve.

The [silver-production basis cross-check](capital-flow-wheaton-antamina-silver-production-basis-cross-check-2026-09-16.md)
adds official Antamina operator observations for 2023 (`360 t`) and 2024
(`0.35 Kt`) plus an official BHP 2025 BHP-share observation of `5.4 Moz`.
Because the units and ownership bases differ, they remain separate historical
proxies; the cross-check does not promote any one of them to a payable-ounce,
metal-credit, or receipt schedule.

The [BHP-share conversion screen](capital-flow-wheaton-antamina-bhp-share-conversion-screen-2026-09-16.md)
now makes the ownership and payable-factor math explicit: the 2023 and 2024
operator observations mechanically imply `3.906 Moz` and `3.798 Moz` of BHP
share, or `3.516 Moz` and `3.418 Moz` after a 90% payable sensitivity. The
2025 BHP-reported `5.4 Moz` remains a separate direct observation. None of
these rows is treated as a metal-credit settlement or cash receipt.

The TJX Q-05 refinement now has a dedicated [forward-capex category boundary](combined-investment-research-pilot-02-tjx-forward-capex-category-boundary-2026-09-15.md): the FY2026 10-K quantifies the FY2027 guide into approximately `$1.000B` renovations, `$992M` offices/distribution/IT, and `$222M` new stores, while H1 maintenance allocation remains open.

### Q-05 cohort growth-floor control — 2026-09-17

The capex boundary now carries an explicit comparable growth-floor field:
Walmart has a `$1.087B` H1 new-stores/clubs category; TJX has a forward
FY2027 `$222M` new-stores category that cannot be substituted for H1; and
Target has no disclosed H1 dollar floor even though its filing names remodels
and new stores. The Target blank is not zero growth spending, and Walmart's
`$13.094B` remainder is not maintenance. The remaining Q-05 upgrade is a
period-matched maintenance-versus-growth allocation with working-capital,
lease, tax, dilution, and service-cost treatment.

### Q-04 same-period QoE double-count control — 2026-09-17

The cohort inventory/payable screen now places balance and cash-flow signals
side by side: TJX `-$116M` versus `-$133M`, Target `-$261M` versus `-$333M`,
and Walmart `-$1.492B` versus `-$1.012B`. The differences remain timing,
presentation, and broader working-capital reconciliation fields. The control
prohibits subtracting period-end supplier-finance balances—or their mechanical
changes—from operating cash without a settlement-date bridge. This strengthens
the QoE layer while leaving recurring owner cash unresolved.

The new [annual lease-and-tax cash control](combined-investment-research-pilot-02-retail-annual-lease-tax-cash-control-2026-09-16.md)
adds annual cash-paid observations for all three retailers: TJX `$2.214B`
lease cash and `$1.471B` taxes, Target `$529M` and `$1.091B`, and Walmart
`$2.315B` and `$5.364B`. These amounts are already embedded in operating cash
flow and are therefore denominator controls rather than extra deductions. The
annual/H1 period mismatch and maintenance, supplier-finance, service-cost,
seasonality, and dilution allocations remain open.

The companion [interim lease-and-tax search boundary](combined-investment-research-pilot-02-retail-interim-lease-tax-search-boundary-2026-09-16.md)
checks the latest TJX, Target, and Walmart Q2/H1 filings and records a bounded
result: TJX reports `$1.147B` of H1 operating-lease cash paid, while TJX cash
taxes and comparable Target/Walmart interim lease/tax cash remain open.
Interim operating-cash, lease-liability, tax-provision, and accrued-tax
observations remain visible, but annual cash-paid values must not be
interpolated into H1 owner cash. The next upgrade is matched Target/Walmart
payment disclosure, TJX cash-tax disclosure, or another company-period
allocation schedule.

The Target Q-05 denominator is now explicitly separated in the [retail capex
refresh](combined-investment-research-pilot-02-retail-capex-public-source-refresh-2026-09-16.md): H1 property-and-equipment expenditures were `$2.404B`, total investing
cash use was `$2.397B` after `$7M` of other investing activity, and `$2.115B`
is the derived `$4.519B` operating-cash-less-property screen. The derived
screen is not Target-reported capex or normalized owner cash; the H1
maintenance-versus-growth allocation remains open.

### Q-10 through-cycle panel upgrade — 2026-09-16

The retail macro bridge now spans 18 company-period observations across Target,
Walmart, and TJX from FY2020 through FY2026. The added FY2020–FY2022 rows use
official SEC XBRL company-facts values for operating cash flow and property
spending, making the pandemic, inflation-shock, and restrictive-rate periods
visible in the same cash-after-property screen. Target reaches a negative
`$1.510B` screen in FY2022, while Walmart and TJX remain positive but
compressed. This improves the falsifier surface, but fiscal overlap, capex
composition, working capital, support, and company actions prevent causal or
normalized-owner-cash conclusions. The next test remains a period-matched
bridge for services, maintenance capital, leases, taxes, and capital access.

The historical panel's 2023 real-earnings source is now reconciliation-controlled:
the dataset retains the revised/summary `+0.8%` observation, while the initial
January 2024 BLS release's `+1.0%` figure is preserved as a separate source
observation. This prevents a release revision from being mistaken for a regime
change and is enforced by the pilot verifier. It does not change Q-10's
through-cycle causal status.

### Q-04 margin-support update — 2026-09-16

The [retail margin-support transition screen](combined-investment-research-pilot-02-retail-margin-support-transition-2026-09-16.md)
now compares H1 reported and support-removed gross margins across TJX, Target,
and Walmart. TJX's reported `32.4%` margin versus `30.1%` prior period becomes
`31.3%` after the `$331M` tariff-refund candidate; Target's reported `31.4%`
margin versus `28.6%` prior period becomes
`29.5%` after the disclosed `$994M` tariff refund; Walmart's reported `24.9%`
versus `24.3%` becomes `24.1%` after approximately `$2.9B` of disclosed
refunds. This is a partial cohort sensitivity, not recurring gross-margin or
owner-cash proof; mix, pricing, fulfillment, inventory, and future support
remain open.

### Q-09 seller-side upgrade

The current ARI Q2 2026 Form 10-Q now supplies a seller-side cash/debt
waterfall artifact: `$9.497267B` of commercial-loan repayment/sale proceeds,
`$746.250M` of term-loan principal repayment, `$500M` of senior-note
repayment, and `$1.239480B` of ending cash. This advances the seller leg of
Q-09, but the queue remains open for the Athene payment ledger, borrower-level
collections, collateral proceeds, and buyer-to-Apollo allocation.

The companion cash-flow reconciliation now closes the seller-entity arithmetic
check: `$139.825M` beginning cash plus operating, investing, financing, and FX
flows reconciles to `$1.239480B` ending cash. This does not close Q-09's
buyer-side borrower-cash or Apollo-parent-receipt test.

The legal perimeter is now reproducible from preserved local copies of the
[definitive purchase agreement Exhibit 2.1](../../raw/primary-sources/capital-flow/apollo/ari/2026-01/ari-definitive-purchase-agreement-ex21.htm)
and [transaction-summary Exhibit 99.1](../../raw/primary-sources/capital-flow/apollo/ari/2026-01/ari-transaction-summary-ex991.htm).
These improve source durability; they do not substitute for the missing
executed settlement, wire, borrower, or parent-receipt records.

The [ARI liquidation-distribution boundary](capital-flow-apollo-athene-ari-liquidation-distribution-boundary-2026-09-16.md)
adds a seller/common-owner residual estimate of `$7.75–$8.50` per fully
diluted share, excluding the separate `$3.75` July dividend. It is a
forward-looking ARI liquidation estimate with stated expense, tax, reserve,
and timing deductions; it does not close Athene borrower repayment,
collateral cash, or Apollo parent receipt. A September 16 check of the latest
ARI Q2 filing and proxy also found no approved-plan notice or actual
liquidating distribution; the estimate remains conditional.
The definitive proxy schedules the special meeting for September 29, 2026, so
the next decisive source is the meeting-result 8-K or a later liquidation
filing.
The 2026-09-17 SEC-source recheck confirms that the meeting remains scheduled
and the `$7.75–$8.50` range remains conditional. Q-09 is now time-gated on the
post-vote filing: test approval, revised reserves, initial distribution, and
any Apollo/Athene cash allocation; do not add the estimate to observed cash.

The [named-issuer source-acquisition boundary](capital-flow-apollo-athene-named-issuer-source-acquisition-2026-09-16.md)
also preserves Apollo's AMAPS wrapper description, Concord's `$1.765B`
music-rights ABS announcement, and the MF1 servicing agreement's
collection-account and collateral-servicing mechanics. These sharpen the
wrapper/use context for three same-CUSIP routes, including an MF1 data-procedures
artifact that identifies 23 collateral interests and 74 mortgaged properties,
while tranche/loan collateral,
Athene allocation, remittance, and liability-cost evidence remain open.

The [private-credit public-search boundary](capital-flow-apollo-athene-private-credit-public-search-boundary-2026-09-16.md)
also records a bounded searched-negative result for Eliant and AP Aristotle.
The newer [AP Aristotle public-search refresh](capital-flow-apollo-athene-aristotle-public-search-refresh-2026-09-16.md)
separates two older SEC borrower-name analogs from the absent 2025 Athene
instrument and settlement. This is a public-perimeter finding, not evidence
that private borrower or repayment records do not exist.

For MF1, the [remittance-access boundary](capital-flow-apollo-athene-mf1-remittance-access-boundary-2026-09-16.md)
now identifies a current CTSLink CREFC/servicer-report route as
`located-access-controlled`; the route is an acquisition lead, not remittance
evidence.

The [MF1 collateral-attribute inventory](capital-flow-apollo-athene-mf1-collateral-attribute-inventory-2026-09-16.md)
now names the loan/property fields required for the next acquisition: funded
and cut-off balances, future-funding conditions, rate protections, maturity and
extension terms, occupancy, property type, and cross-collateralization. It
improves request precision without treating the schema as disclosed loan cash.
The underlying workbook is specifically identified in the public exhibit as
“MF1 2025-B2 Data Tape CSR.xlsx,” provided April 2, 2025, for the April 9,
2025 cut-off; the exhibit does not attach or link it, so obtaining that named
workbook is now the first collateral-data upgrade before attempting loan-level
cash attribution.

### Apollo Broadcom fee-timing update — 2026-09-16

The [fee-timing boundary](capital-flow-apollo-broadcom-capital-solutions-fee-timing-boundary-2026-09-16.md)
now records Apollo management's expectation that the $35B Broadcom financing
will draw over multiple quarters, with the associated fee recognized as drawn
and weighted toward Q4 2026 and Q1–Q3 2027. The timing is now source-backed,
but fee collection, cash settlement, realized margin, and common-owner
attribution remain open.
### Q-07 intercompany-note longitudinal refresh — 2026-09-16

The [intercompany note longitudinal refresh](capital-flow-apollo-athene-intercompany-note-longitudinal-refresh-2026-09-16.md)
adds seven dated AHL note-receivable observations from `$78M` at December 31,
2022 through `$279M` at June 30, 2026. It confirms a recurring AHL-creditor /
AGM-borrower route within a disclosed `$500M` facility. It does not convert
period-end balance changes into dated cash draws, dividend receipts, or
unrestricted common-owner cash; the note ledger, bank confirmations, use of
proceeds, and intercompany eliminations remain the next proof objects.

### Q-07 parent-cash perimeter reconciliation — 2026-09-16

The [parent-cash perimeter reconciliation](capital-flow-apollo-athene-q2-parent-cash-perimeter-reconciliation-2026-09-16.md)
separates consolidated unrestricted cash, HoldCo-summary cash, Asset Management
segment cash, Athene upstream distributions, the AHL-to-AGM note balance, and
parent-level cash uses. This prevents the `$110M` H1 distribution, the `$279M`
period-end note balance, and the `$3.412B`/`$3.415B` parent presentations from
being added together or promoted to common-owner cash. Parent receipt,
intercompany elimination, legal availability, liability cost, and common-owner
residual remain open.

### Q-10 retail lagged falsifier — 2026-09-16

The [lagged diagnostic](combined-investment-research-through-cycle-retail-lagged-diagnostic-2026-09-16.md)
records 7 same-direction versus 8 opposite-direction transitions among 15
usable observations. The simple prior-real-wage-to-next-cash mechanism therefore
does not earn promotion. The next test must add company-specific demand, margin,
inventory, vendor-term, support, maintenance-capital, and attached-service
controls across repeated aligned periods.

### Q-01 BHP upfront-settlement bridge — 2026-09-16

The [upfront-settlement bridge](capital-flow-wheaton-antamina-bhp-upfront-settlement-bridge-2026-09-16.md)
now isolates a narrow promotion-ready observation: Wheaton reports the named
`$4.300B` Antamina PMPA payment, while BHP's FY2026 Note 24.3 reports receipt
of `$4.3B` on April 2, 2026. This strengthens the dated transaction source/use
leg, but amount-and-date consistency is not an independent wire match and does
not prove BHP-PMPA metal-credit ounces, invoice, operating receipt, or return.

### Q-13 facility-availability upgrade — 2026-09-17

URI's Q2 2026 10-Q now discloses the facility split behind the liquidity
bridge: `$2.802B` of ABL borrowing capacity net of letters of credit and `$85M`
of accounts-receivable securitization capacity. The `$2.887B` total reconciles
to `$2.999B` of total liquidity less `$112M` of cash. This upgrades Q-13 from an
implied-liquidity proxy to `facility-availability-visible`; it still does not
provide eligible equipment, NOLV, reserves, U.S./Canadian borrowing-base
components, or a populated Combined Borrowing Base/Combined Availability
certificate. Q-13 remains `evidence-insufficient` for certificate-grade legal
availability and fleet lifecycle return.

### Q-12 MF1 servicing-waterfall mechanics upgrade — 2026-09-17

The new [MF1 servicing-waterfall mechanics boundary](capital-flow-apollo-athene-mf1-servicing-waterfall-mechanics-boundary-2026-09-17.md)
extracts the public agreement's named issuer, Collection Account, two-business-
day deposit rule, Note Administrator/Payment Account remittance route, fee and
expense deductions, partitioned-loan treatment, and noteholder reporting path.
This creates the schema for a future borrower-to-trustee cash join. It does not
prove Athene ownership, a CUSIP or companion-interest holding, actual borrower
cash, remittance, liability-adjusted return, or Apollo common-owner cash;
Q-12 remains `evidence-insufficient`.

The [MF1 same-CUSIP servicing join boundary](capital-flow-apollo-athene-mf1-same-cusip-servicing-join-boundary-2026-09-17.md)
now binds CUSIP `592918-AA-4` to the MF1 issuer and public collection route.
The corrected statutory packet shows a same-CUSIP holding/disposal pair with
`$209.559M` of selected cash-like consideration; the servicing agreement
supplies the collection-to-trustee mechanics. This is a material row-level
upgrade, but lot continuity, Athene custody, borrower receipt, trustee
remittance, liability cost, and Apollo residual remain open.

The [MF1 gross proceeds/income denominator screen](capital-flow-apollo-athene-mf1-gross-proceeds-income-denominator-screen-2026-09-17.md)
adds a bounded diagnostic: `$209.559M` selected consideration plus `$1.303M`
of the selected row's interest/dividend field equals `$210.862M`, or `96.61%`
of the `$218.272M` year-end reported holding amount. The denominator is not
proven cost basis and the income is not independently receipt-verified, so this
is a QoE/reconciliation screen only; Q-12 remains `evidence-insufficient`.

The refreshed [MF1 remittance-access boundary](capital-flow-apollo-athene-mf1-remittance-access-boundary-2026-09-16.md)
now records the live CTSLink inventory: August 18, 2026 Distribution Date,
Bond Level, Collateral Summary, and Loan Periodic reports, plus a revised
August 21 Restricted Servicer Report. All are sign-in/certification gated; the
September 18 next cycle is only scheduled. This sharpens the next acquisition
request but does not promote Q-12 beyond `evidence-insufficient`.

The live MF1CAP page also exposes a separate `MF1 2026-FL21` series with the
same August 18 / September 18 reporting cadence and restricted-report status.
Because the statutory candidate is `MF1 2025-B2 LLC` / CUSIP `592918-AA-4`,
the 2026-FL21 schedule is retained as a separate legal-series observation and
cannot be substituted for a 2025-B2 remittance or Athene receipt without an
offering/CUSIP/legal-owner crosswalk.

The 2026-09-17 CTSLink recheck makes the next action time-gated: revisit the
2025-B2 series after the listed September 18, `10:00` publication time and
either acquire a permitted report or preserve the post-publication access
boundary. Until then, no remittance, trustee distribution, or borrower cash is
added to Q-12.

The cross-platform [insurance named-asset proof ladder](combined-investment-research-insurance-named-asset-proof-ladder-2026-09-17.md)
and [private-credit borrower proof ladder](combined-investment-research-private-credit-borrower-proof-ladder-2026-09-17.md)
now provide the interim comparison control while the MF1 publication window is
pending. They preserve the distinction between statutory ownership, wrapper or
facility purpose, borrower use, settlement, remittance, liability cost, and
owner return; they do not change Q-12's `evidence-insufficient` result.

The [latest retail Q2 lease-and-tax search boundary](combined-investment-research-retail-latest-q2-2026-lease-tax-search-boundary-2026-09-17.md)
rechecks the official August 2026 TJX and Target filings and July 2026 Walmart
filing. TJX reports `$1.147B` of H1 operating-lease cash paid, while Target and
Walmart do not provide comparable interim cash-paid lease/tax schedules.
Lease liabilities, noncash additions, provisions, and accrual movements remain
visible controls, not substitutes for the missing cash-paid objects; Q-05 and
Q-06 therefore remain `evidence-insufficient` for promotion.
