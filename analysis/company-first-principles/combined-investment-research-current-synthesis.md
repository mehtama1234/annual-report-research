# Combined Investment Research System: Current End-to-End Synthesis

Date: 2026-09-18

This is the reader-facing integration of the three active pilots under the
[meaty end-to-end goal](combined-investment-research-meaty-end-to-end-goal.md).
It answers what the system currently proves, what it only qualifies, and what
primary evidence is still required.

## Current execution perimeter — 2026-09-18

The remaining promotion work is concentrated in five controlled routes:

- [Q-03 financed-return source package](capital-flow-wheaton-antamina-q03-next-source-package-2026-09-18.md)
  for the Drawdown Notice, seller funds flow, BHP credits, financing/tax
  allocation, and source-linked return.
- [Q-07 common-owner source package](capital-flow-apollo-athene-q07-next-source-package-2026-09-18.md)
  for the Athene payment, AGM receipt, elimination, intercompany note, and
  common-owner waterfall.
- [AP Grange settlement source package](capital-flow-apollo-athene-ap-grange-next-source-package-2026-09-18.md)
  for the issuer call, Athene lot, remittance, and after-cost return.
- [Q-12 insurance named-asset source package](capital-flow-insurance-q12-next-source-package-2026-09-18.md)
  for Accordia/Athene named holdings, servicing, liability cost, and return.
- [CA-06 retail source-acquisition packet](combined-investment-research-retail-ca06-source-acquisition-packet-2026-09-18.md)
  for matched H1 supplier-finance, maintenance/growth, lease/tax,
  attached-service, and common-owner fields.

These are acquisition routes, not completed evidence. Each retains an explicit
stop rule and prevents a nearby proxy from entering owner cash or return.

## 2026-09-18 Schedule D reconciliation correction

The Athene year-end 2025 statutory Schedule D parser was rerun across its full
located range. It now emits `8,648` rows and ties the compact statutory
book-value references within `$1` for issuer-credit, `$1` for ABS, and `$2`
combined. This is a substantial improvement from the prior stale residual-gap
diagnostic. The aggregate tie is not treated as final row-level accounting
proof: `192` page diagnostics still identify `11` high-priority and `25`
medium-priority ABS column-correction pages, and investment income, proceeds,
liability cost, borrower receipt, and return joins remain open. See the
[correction pass](capital-flow-apollo-athene-statutory-schedule-d-reconciliation-correction-pass-2-2026-09-18.md).

The adjacent Athene Schedule BA range is now also extracted: `368` named rows
across Parts 1–3 on pages `5813–5835`, with `188` Part 1 year-end owned-asset
rows, `96` Part 2 additions, and `84` Part 3 disposals/transfers/repayments.
The Part 1 detail control shows `$17,461,797,562` of apparent book/adjusted
carrying value, one dollar below the verification control; the `$17,387,119,006`
statement/net-admitted value is a distinct column. This advances the route from
a summary BA balance to a named population, but row-level BA column mapping,
income/distribution matching, and owner-cash proof remain open. See the [BA
full-range parser pass](capital-flow-apollo-athene-statutory-schedule-ba-full-range-parser-pass-1.md).
The coordinate-column upgrade now identifies `436` Part 1 table rows and sums
`432` visible book values to `$17,461,797,566`, a `$4` difference from the
detail control; four source-sparse book cells remain blank and are not imputed.
Actual cost ties exactly and fair value is within `$1`; after a token-center
column repair, Part 1 income and additional commitment now tie within `$1`
(`$237,086,006` versus `$237,086,005` and `$4,368,051,290` versus
`$4,368,051,289`). They remain statutory control figures, not promoted cash
receipts or owner cash.
The corrected Part 2 coordinate population now ties acquisition cost within
`$1` and additional investment exactly; those rows remain event-level review
data and are not added to year-end BA assets.
The corrected Part 3 coordinate pass adds `168` disposal/transfer/repayment
rows across pages `5830–5835`, including `65` same-CUSIP matches to Part 1.
The visible disposal-consideration sum is `$4,417,190,618`, within `$2` of the
page-450 verification control of `$4,417,190,620`; extracted total gain/loss is
`$(73,966,794)`, within `$3` of the control. This is statutory continuity
evidence, not proof of bank settlement, borrower repayment, or Apollo owner cash.
For the `84` blank-CUSIP events, a candidate-only name bridge finds `33` unique
high-coverage candidates, `42` ambiguous/partial candidates, and `9` without a
strong candidate. These remain unpromoted until page-row, lot, identifier, and
amount agreement is proven.
The consolidated event ledger classifies `61` rows with Part 1 + Part 2 + Part
3 continuity, `4` Part 1 + Part 3 rows, `17` Part 2 + Part 3 rows, `2` unmatched
CUSIPs, and `84` blank-CUSIP events. Visible disposal book value is `$4.395B`
against `$4.417B` consideration, still only a statutory event screen.
The continuity ledger adds a quantitative same-identifier screen: `4` Part 3
rows are within `$1` of summed Part 1 book value, `6` within `$1M`, and `55`
have a larger or multi-lot delta; this prioritizes lot review but does not prove
same-lot identity, settlement, borrower repayment, or Apollo cash.
The resulting ten-row review queue is documented in the [BA lot-review queue](capital-flow-apollo-athene-statutory-schedule-ba-lot-review-queue-pass-1.md).
The source-row enrichment explicitly labels only 5 of those 10 events as
`Sale`; the remaining 5 have no visible disposal-nature label in the compact
text layer and remain unresolved event types.
The broader coordinate-controlled sale queue identifies `57` rows whose
disposal-nature column is exactly `Sale`, totaling `$1.848B` of consideration;
it is the next settlement-search priority and not owner-cash evidence.
Crosswalking those rows to the Schedule D disposal parser finds only 3
same-CUSIP matches: two are `Security Withdraw` transfer holds and one is a
different-perimeter cash-like candidate. This prevents treating the BA sale
queue as Schedule D cash without transaction-level proof.
The targeted local-source search for the five largest BA sales found no
independent settlement, custodian, trustee, or borrower-receipt document; the
result is recorded in the [settlement-search boundary](capital-flow-apollo-athene-ba-sale-settlement-search-boundary-pass-1.md).
The first three high-dollar Schedule D CUSIP candidates were then checked
against raw row text and schedule-specific numeric layout. Six disposal rows
have source-supported consideration; one `$6.588M` tax-free exchange is held
out, leaving `$1.402B` of consideration as a cash-like statutory candidate
pool. This is a column-proof upgrade only: settlement, borrower receipt,
legal-entity cash, liability release, and Apollo owner cash remain unproven.
See the [CUSIP row-column proof pass](capital-flow-apollo-athene-statutory-cusip-row-column-proof-pass-2-2026-09-18.md).
An Apollo March 2022 Form 10-Q now adds historical AP Aristotle wrapper
context: it identifies AP Aristotle Holdings LLC in a consolidated-VIE
concentration of approximately `$1.167B`. The historical observation is not
joined to the 2025 CUSIP, so it strengthens legal-entity routing only and is
not added to the current candidate pool. See the [historical wrapper-source
refresh](capital-flow-apollo-athene-aristotle-historical-wrapper-source-refresh-2026-09-18.md).
The adjacent AP Grange route now has a stronger current-period public fact:
Athene says AP Grange called its ABS debt in Q2 2026 and recognized a `$673M`
gain. The filing's `$5.080B` issuer/concentration perimeter does not reconcile
to the 2025 Schedule BA `G2964#-AB-5` Tranche B row (`$411.999M` Part 1 book,
`$313,313` Part 3 consideration, blank disposal nature), so the gain is not
promoted to that row's cash or return. See the [AP Grange call-to-statutory
bridge](capital-flow-apollo-athene-ap-grange-call-statutory-bridge-pass-1-2026-09-18.md).
The same control is preserved in the [machine-readable AP Grange
call/statutory ledger](data/capital-flow-apollo-athene-ap-grange-call-statutory-bridge-pass-1-2026-09-18.csv), which keeps issuer-level concentration and gain separate from the statutory Tranche B event rows.
The route now separates a larger Schedule D AP Grange Tranche A position:
`G2964#-AA-7` carries `$3.638B` book value, `$343.374M` investment income,
`6.500%` coupon, and `03/20/2045` maturity. A public N-2/A independently
corroborates an AP Grange 6.50% / 03/20/2045 instrument family, but not
Athene's lot or settlement. See the [Tranche A public-instrument
crosswalk](capital-flow-apollo-athene-ap-grange-tranche-a-public-instrument-crosswalk-pass-1-2026-09-18.md).
The crosswalk closes the public instrument-identity join only as a full tuple:
Apollo's AP Grange transaction summary maps `G2964#AA7` / ISIN `US00187RAA32`
to the same 6.50% 03/20/2045 notes, matching Athene's statutory
`G2964#-AA-7` marker. SSGA N-PORT filings independently corroborate public
CUSIP `00187RAA3` and the instrument terms. Visually similar statutory
`G2964*-AA-7` rows elsewhere carry different issuer labels or coupons, so the
prefix is not treated as a unique security key by itself. The tuple supports
instrument identity, but not Athene's lot settlement, paying-agent receipt, or
cash allocation.
The official Q2 2026 AAIA statutory statement adds the strongest current
legal-entity event: Schedule D Part 4, PDF page `2490`, records
`G2964#-AA-7` disposed on `04/10/2026` to `Various` for `$4.052553175B` of
consideration, against `$3.691539180B` book value at disposal, with a
`$4.308961M` row-level loss and `$414.342613M` of bond interest received during
the year. A targeted scan of the Q2 Schedule D Part 3/4 range found no
`G2964#-AB-5` or second AP Grange row. This upgrades Q-08 to an exact dated
statutory-disposition candidate, but not settled bank cash: purchaser,
paying-agent, redemption classification, gain allocation, liability cost, and
Apollo-owner cash remain unproven. See the [Q2 statutory settlement candidate](capital-flow-apollo-athene-ap-grange-call-statutory-bridge-pass-1-2026-09-18.md).
The next-source package ranks the exact issuer call, Athene custody/remittance,
post-call statutory, Apollo-wrapper, and after-cost waterfall objects needed to
promote Q-08; until one is obtained, the route remains settlement-unproven.
See the [AP Grange settlement source package](capital-flow-apollo-athene-ap-grange-next-source-package-2026-09-18.md).
An independent KEMI statutory statement describes deferred interest and
principal provisions for `G2964#AA7`, creating a cash-versus-accrual control:
Athene's `$343.374M` investment income cannot be treated as collected cash
against `$265.774M` of interest received without a lot-level schedule.
The 2025 Schedule D Part 4 rows also show `$2.249993M` of Tranche A
consideration to Apollo Global Securities, LLC and `$33.489724M` to the
AARe–Sony Life [Block] Trust. Apollo's 2025 10-K and AGS's own SEC financials
place AGS inside Apollo's consolidated subsidiary/broker-dealer perimeter, so
the first row is a named Athene-to-Apollo-affiliate counterparty route. It is
still statutory consideration, not proven settlement or parent/common-owner
cash; the AARe–Sony Life row remains separate. See the [AP Grange
counterparty bridge](capital-flow-apollo-athene-ap-grange-prepayment-cross-entity-bridge-pass-2-2026-09-18.md).
AGS's 2025 public financials add a visible broker-dealer balance-sheet
perimeter—`$455.585M` cash, `$13.825M` related-party receivables, `$7.640M`
underwriting-fee receivables, and `$23.206M` related-party payables—and describe
underwriting, private-placement, asset-backed-security, and proprietary trading
activities. Apollo's Q2 2026 10-Q also describes current AGS underwriting and
firm-bid roles. These facts strengthen the legal-entity and role map, but no
source allocates any AGS balance to the `$2.249993M` AP Grange consideration;
they are not settlement or parent-cash proof. See the [AGS financial-perimeter
boundary](capital-flow-apollo-athene-ap-grange-prepayment-cross-entity-bridge-pass-2-2026-09-18.md).
Apollo's Q2 2026 10-Q adds a cross-entity flow fact: credit-strategy net flows
included approximately `$5.0B` of redemptions related to the AP Grange
prepayment. This links the issuer call to an Apollo fund-flow perimeter, but
not yet to an Athene bank receipt, exact tranche allocation, or parent cash.
Athene's filed June 30 concentration table no longer lists AP Grange, while
the comparative December 31 table shows `$5.080B` and attributes the change to
the Q2 call. Because this is a concentration screen, it is a timing/perimeter
control rather than proof that every residual AP Grange position was zero.
An independent KKR holder roll-forward also shows its AP Grange position
absent at June 30 after a March 31 holding, corroborating a Q2 market-side
realization/restructuring window without proving Athene settlement.
Principal Life's March 31, 2026 statutory statement adds an independent
redemption-date control: it records `G2964#-AA-7` as redeemed on March 20,
2026 with a reported `$860.097M` amount. This narrows the timing and scale of
an external-holder redemption, but it is not Athene's lot, trustee remittance,
or bank receipt and is not added to the Apollo/Athene cash bridge. Brighthouse
Life reports the same identifier/date/coupon/maturity with a `$226.341M`
redemption, but labels the issuer Intel rather than AP Grange; it is retained
as identifier/date corroboration with an unresolved legal-issuer naming
conflict, not as a second confirmed AP Grange holding.
See the [AP Grange prepayment cross-entity bridge](capital-flow-apollo-athene-ap-grange-prepayment-cross-entity-bridge-pass-2-2026-09-18.md).

The AP Grange call-settlement search was bounded on 2026-09-18. Targeted
searches found no public call notice, paying-agent remittance, tranche-level
redemption statement, or Athene custody allocation. The official anchors
remain Athene's `$673M` Q2 gain and Apollo's approximately `$5.0B` credit-
strategy redemption flow; neither is a bank receipt or owner-return proof.
See the [AP Grange call-settlement search boundary](capital-flow-apollo-athene-ap-grange-call-settlement-search-boundary-pass-3-2026-09-18.md).
The Schedule D interest-column parser was also repaired on 2026-09-18: it now
anchors income and received-interest fields to the acquisition-date columns,
so payment-at-maturity is not misclassified as received interest. The corrected
full-range population reports `$6.230478121B` of received interest; AP Grange
Tranche A `G2964#-AA-7` shows `$7.219623M` of interest income and `$230.263772M`
received, while Treasury Strip `912803-DM-2` has source-visible blanks. The
page-18 collected bond-category total of `$8.127852536B` is not treated as a
reconciliation target: its `$1.897374415B` difference from Schedule D remains
an explicit category/perimeter join diagnostic. See the [interest-column repair
pass](capital-flow-apollo-athene-statutory-schedule-d-interest-column-repair-pass-1.md).
The corrected row population also ties the filing's Schedule D subtotal rows:
issuer-credit obligations contribute `$888.305M` of income and `$3.007B` of
received interest, while asset-backed securities contribute `$616.145M` and
`$3.224B`. The combined `$1.504B` / `$6.230B` totals have zero difference to
the source subtotals, so the remaining gap is not currently a missing-row
problem. See the [Schedule D interest subtotal control](capital-flow-apollo-athene-statutory-schedule-d-interest-subtotal-control-pass-1.md).
The source-defined population boundary is now explicit: page 18 is a full-year
income exhibit, Part 1 is the December 31 owned population, and Parts 4–5 are
current-year disposed and acquired-then-disposed populations. This makes
disposed-asset income a concrete next reconciliation object without assigning
any amount of the residual to it. See the [income population boundary pass](capital-flow-apollo-athene-statutory-income-population-boundary-pass-1.md).
The Part 4/5 subtotal then closes the collected-bond bridge to within `$2`:
Part 1 received interest of `$6.230478121B` plus Part 4/5 bond
interest/dividends of `$2.207402908B`, less the page-18 net footnote adjustment
of `$310.028491M`, reconstructs `$8.127852538B` against page 18's
`$8.127852536B`. This is a near-exact statutory legal-entity reconciliation,
not borrower remittance or Apollo owner cash. See the [page-18/Schedule D income
reconciliation pass 3](capital-flow-apollo-athene-statutory-page18-schedule-d-income-reconciliation-pass-3.md).
The same statutory statement also reports `$5.890696798B` of interest and
adjustments on contract or deposit-type contract funds. This creates a
same-entity, same-period liability-burden screen: `$12.732699320B` net
investment income less that line equals `$6.842002522B`, or `53.7357%` of net
investment income. It is not yet a normalized spread or owner-cash result; the
line lacks product allocation, credited-rate, hedging, capital, tax, and
expense detail. See the [liability-interest burden bridge](capital-flow-apollo-athene-statutory-liability-interest-burden-bridge-pass-1.md).
The line can now be allocated at business-line level: individual annuities
account for `$5.882288174B` and group annuities for `$8.408625M`, summing to
within one dollar of the summary line. Exhibit 7 separately reports
`$2.649832829B` of deposit-type-contract investment earnings credited and a
`$64.259784362B` net after-reinsurance ending balance. These are allocation and
scale controls only, not product-level credited-rate, normalized-spread, or
owner-cash evidence. See the [line-of-business liability allocation pass](capital-flow-apollo-athene-statutory-liability-interest-by-line-of-business-pass-1.md).
The statutory notes also identify the hedge layer: options, futures, variance
swaps, swaptions for minimum crediting-rate exposure, and interest-rate swaps
for asset/liability mismatches. Gross derivative assets are `$2.482135218B`,
including `$2.479627050B` admitted. This is hedge-mechanism and scale evidence,
not quantified hedge cost, settlement, product attribution, or owner cash. See
the [derivative hedge boundary pass](capital-flow-apollo-athene-statutory-derivative-hedge-boundary-pass-1.md).
Schedule DB pages 464–491 now add direct derivative turnover controls: `$2.009B`
of termination consideration, `$(491.016M)` of termination gain/loss,
`$3.284B` of unrealized valuation change, and `$108.756M` of cumulative futures
cash change. Its book-value and fair-value verification closes within `$1`.
These remain derivative cash/valuation controls, not normalized hedge return,
policyholder-cost allocation, or owner cash. See the [Schedule DB verification
pass](capital-flow-apollo-athene-statutory-schedule-db-verification-pass-1.md).
Pages 465–489 also yield a conservative `735`-row Part C component ledger that
preserves derivative identifiers, instrument types, cash-instrument CUSIPs, and
descriptions. It includes the source-visible `592918-AE-6 / MF1 2025-B2 B`
identity join under `04687#AB4`; merged dotted columns are held as sparse or
ambiguous rather than imputed. This is a named-component review surface, not
settlement, counterparty remittance, or owner-cash proof. See the [Part C
ledger](data/capital-flow-apollo-athene-statutory-schedule-db-part-c-ledger-pass-1.csv).
An exact-CUSIP crosswalk now joins `728` of the `735` Part C rows to Schedule D,
covering `586` unique CUSIPs and `743` crosswalk rows. It joins MF1 2025-B2,
AMAPS 1, Atlas, Varde, and Ares components to Schedule D book value, income,
and received-interest fields. This is a named holding/income identity bridge,
not derivative settlement, borrower remittance, liability allocation, or owner
cash proof. See the [Part C–Schedule D crosswalk](capital-flow-apollo-athene-statutory-schedule-db-part-c-schedule-d-crosswalk-pass-1.md).
The next control narrows that identity join to `52` named MF1, AMAPS, Atlas,
Varde, and Ares CUSIPs. It sums only unambiguous Part C component candidates,
keeps one ambiguous row explicit, and places those component amounts beside
Schedule D book, fair, income, and received-interest fields. The component
versus holding differences are perimeter signals, not lot-settlement matches;
the [named-lot control ledger](data/capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-control-pass-1.csv)
does not prove derivative settlement, custody remittance, liability allocation,
borrower repayment, or Apollo owner cash.
The resulting acquisition queue retains all `52` routes, with `8` Tier A,
`30` Tier B, and `14` Tier C requests. Tier A prioritizes the largest
statutory holdings, material received-interest controls, and source-column
ambiguity; its requested object is a specific custody, trustee/paying-agent,
settlement, or lot-level income-allocation record. See the [named-lot
acquisition queue](data/capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-acquisition-queue-pass-1.csv)
and [queue memo](capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-acquisition-queue-pass-1.md).
The underlying PDF footnote identifies bond discount accrual, premium
amortization, and accrued-interest paid on purchases as separate page-18
components. The [page-18 / Schedule D perimeter bridge pass 2](capital-flow-apollo-athene-statutory-page18-schedule-d-perimeter-bridge-pass-2.md)
therefore keeps the `$392.923968M` comparison against the sum of both Schedule
D fields as a definition diagnostic, not a cash reconciliation.
The legal-entity bridge therefore keeps the BA verification total of
`$4.417190618B` separate from aggregate bond proceeds of `$54.035221430B` and
mortgage-loan proceeds of `$12.676073505B`; no source allocation supports adding
those amounts or attributing them to Apollo.
The income join has a separate quality-of-earnings break: Part 1 row-level
investment income reconciles to positive `$237.086M`, while page 18 reports
Other invested assets income of `$(185.080M)` collected and `$(132.205M)` earned.
The [BA income-category boundary](capital-flow-apollo-athene-statutory-ba-income-category-boundary-pass-1.md)
keeps this as an unresolved perimeter/definition issue rather than a cash or
loss claim.
The [Part 1 income review queue](capital-flow-apollo-athene-statutory-schedule-ba-part1-income-review-queue-pass-1.md)
prioritizes the top 30 positive rows, which contribute `$182.801M` or `77.10%`
of the parsed Part 1 income total. Blank-identifier alternatives and unusual
book/income rows mean this is a source-review order, not a yield ranking.
Eleven of the top 30 have visible Part 3 events, but only five have an exact
coordinate-column `Sale` signal; the income-to-event link remains a statutory
screen, not collected cash or same-lot proof.
The coordinate-column upgrade now identifies `436` Part 1 table rows and sums
`432` visible book values to `$17,461,797,566`, a `$4` difference from the
detail control; four source-sparse book cells remain blank and are not imputed.

## 2026-09-18 Q-03 source refresh

The latest official BHP FY2026 operational review and Wheaton Q2 2026 release
were rechecked against the BHP–Antamina receipt gate. Wheaton separately
identifies `$4.3B` of BHP Antamina within `$4.5B` of Q2 net upfront stream
payments, while its `157,600` GEO produced-but-not-yet-delivered figure is
company-wide. BHP's operational review supplies Antamina copper/zinc and the
`33.75%` BHP interest boundary, but neither source supplies BHP-specific
metal-credit units, sale/receivable, bank collection, tax, or facility
allocation. Q-03 therefore remains qualified and receipt-open; the next useful
object is a transaction-level settlement, delivery, reserve, lender, or cash
allocation schedule, not another broad operating-release search.
The [payment-date reconciliation refresh](capital-flow-wheaton-antamina-bhp-payment-date-reconciliation-refresh-2026-09-18.md)
adds a narrow two-sided close control: Wheaton's filed closing exhibit reports
the `$4.3B` buyer-side payment on April 1, while BHP's FY2026 20-F reports the
`$4.300B` seller-side receipt on April 2. The same named PMPA and April 1
effective date align, but no public bank value-date or funds-flow record
resolves the one-day difference. This strengthens the upfront transaction
bridge without advancing BHP-only metal-credit, delivery, tax, allocation, or
full-return proof.
The [BHP investor-transcript valuation boundary](capital-flow-wheaton-antamina-bhp-investor-transcript-valuation-boundary-2026-09-18.md)
adds a separate qualitative valuation control: an analyst presented a
reserve-only negative-IRR framing, while BHP management described the deal as
specific to non-core silver and an Antamina mine plan that incorporated life
extensions. This is valuation context and a thesis-breaker input, not a
source-backed PMPA IRR, NPV, delivery curve, tax allocation, or financing
waterfall.

For a guided review of the writeups and recurring themes, start with the
[reviewer's guide](combined-investment-research-reviewers-guide.md).
The structured [five-theme status map](data/combined-investment-research-theme-status-map-2026-09-16.csv)
provides the compact review index: affordability/substitution, scarce physical
assets and contractual control, institutional capital, valuation/reinvestment,
and macro/liquidity transmission. Each theme points to a representative
writeup, an integrated pilot route, a current grade, and one decisive open
question.

The [force-to-company atlas](combined-investment-research-force-to-company-atlas-2026-09-15.md)
now joins the social, Inc. 5000, IBIS, macro, filing, and pilot handoffs with
explicit boundaries. The [method and source registry](combined-investment-research-method-registry.md)
indexes the social, Inc. 5000, IBIS, filing, Damodaran, Lyn Alden,
capital-flow, reader, and completion-audit layers with an explicit boundary for
each one.
The new [expansion-lane cross-sector comparison](combined-investment-research-expansion-lane-cross-sector-comparison-2026-09-17.md)
extends the original three-pilot comparison into power grid, digital
infrastructure, industrial uptime, medical devices, healthcare distribution,
insurance/private credit, and physical-capacity lanes. It preserves
sector-specific denominators and promotion gates rather than creating an
unsupported pooled ranking.
The companion [source-family route ledger](data/combined-investment-research-source-family-routes-2026-09-16.csv)
preserves the exact primary route and connected artifact for each upstream
It now separately records the official BLS expenditure anchor used alongside
Fed SHED, preserving the distinction between macro corroboration and retailer
filing proof.

The [next-evidence queue](combined-investment-research-next-evidence-queue.md)
turns the remaining gaps into ten document-specific reconciliation tests. Its
structured CSV now assigns every row a machine-audited result class—such as
searched-negative or evidence-insufficient—and the pilot verifier checks both
that classification and the existence of each queue source artifact.

The [undercovered-industry theme synthesis](annual-report-undercovered-industry-theme-synthesis-pass-1.md)
and its [deep-dive work order](annual-report-undercovered-industry-deep-dive-work-order-pass-1.md)
has now been executed at the article-theme level across all eight ranked
families: services/cultural consumption, consumer goods/household identity,
basic materials/input scarcity, real estate/scarce locations, broad
technology, healthcare care infrastructure, energy affordability, and
ordinary finance. These additions broaden the social and industry map while
keeping the stronger cash, valuation, liquidity, and named-cash gates
sector-specific and explicitly open where the packets do not close them.

The [cross-sector integration matrix](annual-report-cross-sector-integration-matrix-pass-1.md)
now connects those eight families to the four established pillars—affordability,
contractual control, institutional capital, and permissioned power capital.
For each theme it names the payer, burden carrier, correct operating
denominator, QoE/financial-shenanigans reconciliation prompt, owner-cash and
valuation object, macro/liquidity route, and decisive breaker. This is the
current bridge from article breadth back to the end-to-end investment chain;
it is not a pooled sector ranking.

The [capital-flow graph](capital-flow-end-to-end-graph-pass-1.md) also records
a concrete energy/refinancing upgrade: PBF's Q2 filing identifies `$492.1M` of
net 2034-note proceeds and the June 25, 2026 redemption of all `$801.6M` of
2028 notes using those proceeds plus available cash. This reaches completed
source/use visibility, but not trustee settlement, accrued-interest, cash-on-
hand allocation, fee/tax, post-redemption liquidity, or refinery-level return
proof. The new [PBF post-redemption liquidity boundary](capital-flow-pbf-q2-post-redemption-liquidity-boundary-2026-09-17.md)
now adds period-matched operational liquidity of more than `$3.5B`, including
more than `$800M` cash and approximately `$2.7B` of revolver availability;
trustee settlement, accrued interest, cash-on-hand allocation, fee/tax, and
refinery-level return remain open. The consolidated H1 financing statement also shows `$500.0M` of
new-note proceeds, `$(801.6M)` of redemption, `$1.100B` of revolver borrowings,
and `$(1.200B)` of revolver repayments; these are period financing movements,
not an account-level trustee settlement or source-priority cash bridge.

The [BHP FY2026 upfront receipt and use boundary](capital-flow-wheaton-antamina-bhp-fy2026-upfront-receipt-use-boundary-2026-09-17.md)
strengthens Q-03 on the recipient side: BHP's FY2026 20-F records completion
of the Wheaton stream, `$4.3B` of upfront consideration received, and the
proceeds' inclusion in net financing cash-flow analysis. This closes the
completed-upfront-receipt and issuer-period-classification question, but not
the recurring BHP-PMPA metal-credit, sale/receivable, bank-collection, tax, or
facility-allocation chain. The `$4.3B` remains a transaction source/use item,
not recurring Antamina owner cash.
The exact cash-flow statement separately reports `$4.300B` of proceeds from the
streaming-arrangement liability, `$41M` of settlements of that liability, and
`$(3.280B)` of net financing cash flows. This tightens the BHP period and
classification control, but still does not identify bank timing, internal use,
or recurring BHP-PMPA metal-credit collection.

The [BHP public allocation stop boundary](capital-flow-wheaton-antamina-bhp-public-allocation-stop-boundary-2026-09-17.md)
also separates the `$4.3B` stream receipt from BHP's approximately `$4.8B`
combined asset-realization figure and period-end net-debt outcome. The public
record does not allocate debt repayment, growth capital, tax, dividends, or
legal-entity residual cash to Antamina, so Q-03 has a stronger searched-negative
stop rule for use-of-proceeds attribution rather than a promoted asset-level
return.

The linked [PBF official 8-K financing-mechanics pass](capital-flow-pbf-official-8k-financing-mechanics-pass-2-2026-09-17.md)
strengthens that route with the co-issuer, trustee, paying-agent, and
financing-activities map. It also preserves the closing 8-K's approximately
`$492.7M` net-proceeds figure beside the later Q2 10-Q's `$492.1M` period-end
figure. This is a documented transaction reconciliation, not trustee-settlement
or refinancing-NPV proof.

The graph also adds a separate [Atwell BofA/Advent route boundary](capital-flow-atwell-bofa-advent-infrastructure-route-boundary-pass-1.md):
Advent's official investment announcement and an Atwell announcement carried
by Business Wire identify a BofA-led `$200M` facility and infrastructure-
services funding context, while the
borrower draw, allocation, cash flow, and repayment remain open. This route is
kept separate from Ares/Frontline so sponsor, bank, and private-credit roles
are not conflated.

## The chain now exists

```text
social behavior / macro force
  -> industry control point
  -> private-company discovery or public-company cohort
  -> annual-report operating model
  -> owner-cash bridge
  -> Damodaran expectation screen
  -> Lyn Alden liquidity test
  -> capital wrapper / legal entity / asset
  -> cash transfer and burden map
  -> falsifier and next filing
```

The chain is not equally deep at every node. The system's central discipline is
to preserve those differences rather than call the entire chain proven because
one upstream signal or downstream metric is strong.

The [evidence-chain handoff matrix](combined-investment-research-evidence-chain-handoff-matrix-2026-09-16.md)
now makes that discipline machine-checkable across the three pilots. Each row
maps force, control point, filing, operating model, QoE, owner cash, valuation,
macro, capital flow, and thesis-breaker status, with a named bottleneck and
safe claim. All three owner-cash stages remain `partial`.

The latest Concord route adds two bounded observations. KBRA's July 2026
surveillance says the Concord 2024-1 and 2025-1/2/3 notes had received timely
interest through the July payment date, strengthening the wrapper's
deal-level debt-service boundary. Separately, an official SEC N-PORT filing
independently identifies a Concord 2024-1A security by CUSIP and reports a
200,000-unit, `$197.038M` position. That filing improves instrument
observability and cross-checkability. A later John Hancock N-PORT-P observation
also identifies Concord 2025-2A, CUSIP `20633KAL2`, with `250,000` principal
units and approximately `$253.6M` reported value as of October 31, 2025. The
an independent SEC-hosted schedule also corroborates 2025-2A at `$1.293B`
principal and approximately `$1.319B` value. These public observations broaden
Series 2025-family visibility; a newer John Hancock quarterly report adds a
February 28, 2026 2025-2A observation at `$14.561M` par and `$14.999229M`
reported value. These public observations broaden Series 2025-family
visibility, but none
proves Athene ownership of 2025-3A, a settled lot, trustee remittance, or cash
receipt. The Athene-specific receipt, trustee waterfall, royalty collections,
liability-cost allocation, and asset-level return remain open.
The latest targeted public search also surfaced SEC-hosted 2025-1A portfolio
schedules but no 2025-3A observation under the checked issue-name and CUSIP
variants. That is a bounded public-observability negative, not a claim that the
2025-3A security does not exist or that Athene did not hold it.
The exact Athene Concord candidate has since been identified in two independent
2025 statutory statements: CUSIP `20633K-AN-8` is labeled `TUNES 253 A - ABS`,
while Athene's own row identifies it as `TUNES 2025-3A A`, 6.311%, maturing
07/20/2075, with `$225M` par. The outside statements also show a July 1, 2025
acquisition record. This removes the prior public
CUSIP-to-series ambiguity at the instrument-family level. It still does not
prove Athene's trade settlement, trustee remittance, borrower bank receipt,
specific tranche allocation, liability cost, or asset-level return. See the
[exact CUSIP/series identity refresh](capital-flow-apollo-athene-concord-cusip-series-identity-refresh-2026-09-18.md).

The Concord route now has a current recapitalization anchor: Bertelsmann's
September 1, 2026 combination announcement says Apollo's `$1.25B` equity at a
BMG subsidiary creates the basis for future refinancing and repayment of
BMG/Concord ABS liabilities; Apollo's September 17 announcement says the
investment enables repayment of certain outstanding ABS liabilities. This
advances the legal-entity/source-use perimeter, but neither announcement
proves that a particular repayment has settled, identifies the repaid series
or class, joins payment to Athene's `20633K-AN-8` position, or proves trustee
remittance or Apollo common-owner cash.
See the [BMG/Apollo recapitalization boundary](capital-flow-apollo-athene-concord-bmg-apollo-recapitalization-boundary-2026-09-18.md).
KBRA's July 21, 2026 affirmation covers Series 2025-3 and says the securities
had received timely interest through the July 2026 quarterly payment date;
the full report is gated and exposes no principal/payoff or remittance table.
This is a pre-recapitalization performance anchor, not a principal settlement
or Athene receipt.
DLA Piper separately describes the legacy Concord ABS in the BMG subsidiary as
approximately `$2.5B` and says it assisted with amendments to the Concord ABS
structure. That improves the liability/amendment perimeter but does not name
the amended classes or prove settlement.

## Source roles and current evidence

| Source family | What it contributes now | Evidence boundary |
| --- | --- | --- |
| Social research | `33` affordability/substitution signals and qualitative behavior hypotheses, independently checked against official Fed SHED and BLS expenditure evidence | The external affordability force is corroborated, but there is still no population-to-retailer attribution or causal proof |
| Inc. 5000 research | `1,553` mapped subpattern assignments, `1,777` unique 2026 companies, and `$87.3B` summed mapped revenue | Discovery context, not consumer adoption or owner cash |
| IBIS Industries | Industry, adjacency, macro-force, and bottleneck context, explicitly handed off into Pilot 02 filing tests for the hollow middle, margin vise, and channel shift | Not exact company-period financial proof; the handoff creates tests, not validation |
| Investments article bridge | Dated WPM/Franco-Nevada/Sandstorm thesis families and failure regimes routed into Pilot 01 contract, delivery, financing, valuation, and falsifier gates | Directional investment context, not primary evidence of the Antamina cash flow or return |
| Annual reports / SEC / IR | Named company metrics, liabilities, capital, fees, cash flow, legal-entity boundaries, and parent-balance-sheet context | Reported facts still require denominator and attribution analysis |
| Damodaran layer | Normalized cash, multiples, SOTP, reinvestment, and expectation-burden screens refreshed against a dated market snapshot | Cash and reinvestment assumptions remain analytical until validated by future filings |
| Lyn Alden layer | Inflation, rates, funding, credit, policyholder liquidity, affordability, and monetary-regime tests plus a historical 2020–2026 regime panel, an 18-row FY2020–FY2026 longitudinal retail cash-screen bridge, same-period 2026 company join, and current-regime observed responses | Macro mechanism and regime consistency still do not prove through-cycle resilience or causality |
| Capital-flow layer | Wheaton/BHP and Apollo/Athene named payment, entity, exposure, and transfer evidence | Private delivery, waterfall, and common-owner residuals remain open |

## Pilot status matrix

| Pilot | Starting force | Control point | Cash evidence | Valuation evidence | Current grade | Decisive open gate |
| --- | --- | --- | --- | --- | --- | --- |
| Affordability / TJX / Target / Walmart | Trading down, substitution, constrained choice | Buying flexibility, planned assortment, or broad low-price availability | All three now have reported OCF-less-property bridges plus common-period cash, margin/working-capital normalization, lease/dilution/capex, annual capex-reference proxy, H1 capex-direction gates, capex-allocation sensitivity, supplier-finance, attached-service boundary and mix screen, and cohort-operating maps; the new attached-services cash upgrade adds Target's TD payer/burden map and Roundel accounting boundary plus Walmart's segment operating denominator and ecosystem composition; TJX H1 FY2027 bridge now added; the post-financing residual screen adds disclosed Target/Walmart debt repayment beside support and SBC sensitivities | Target/Walmart illustrative cash screens; TJX remains intentionally not-comparable until owner-cash normalization is complete | Qualified multi-source | Normalize inventory, markdown, lease cash, maintenance-capital, dilution, supplier-finance settlement, attached-service costs, and debt/claim timing without double counting |
| Wheaton / Antamina | Capital concentration in scarce long-life physical assets | Contractual silver stream that transfers much mine operating burden to operator | Two-sided `$4.3B` upfront payment/proceeds confirmation; BHP-only `33.75%`/`100M-ounce` contract tranche, public `6.0M`/`5.4M` BHP production-profile proxy, BHP-interest `65.7M` P&P reserve quantity with mechanical threshold screen, new `10.95–12.17` year reserve-constrained payable-duration ceiling, Q2/H1 incremental production signal, BHP FY2026 annual and Q4 BHP-interest production/sales proxy, `16.67–18.52` year mechanical threshold-timing screen, exact term-loan margin, official September 14 SOFR, actual H1 `$2.700B` debt draw, `$728M` repayment, `$29.886M` interest paid, `$5.118M` debt-issue costs, company-level `$20.192M–$40.898M` spread-only and `$91.578M–$112.284M` mechanical all-in burden screens, financed-return frontier, new 0–100% after-tax financed allocation frontier, corporate burden context, metal-credit settlement mechanism and accounting proof-object boundary, first BHP-PMPA deliveries, and `$41M` liability settlement visible; combined-stream revenue/cash proxy | Incremental BHP scenario screen; threshold timing and reserve duration remain mechanical, annual series remains a counterparty production/sales proxy, financed and after-tax frontiers remain company-level allocation sensitivities; bull remains below discounted break-even | Qualified named-asset case | Reserve-backed life-of-mine delivery curve, quantity-level BHP-only metal credits, smelter/assay and PMPA payability reconciliation, tax/interest allocation, lender funds-flow allocation, and debt waterfall |
| Apollo / Athene | Institutional retirement and private-credit capital | Origination-to-insurance-liability and fee-platform route | FRE/SRE/PII bridge; Athene transfers; related-party exposure/fee/payable/asset-transfer/spread/distribution bridge; current Q2 ACRA/ADIP flow of `$145M` contributions and `$47M` distributions, with H1 `$271M`/`$301M` totals; entity-dividend boundary; segment/restricted/VIE cash-pool boundary; 2025 Athene statutory asset/liability, investment-income, operating-cash, investment-turnover, and 96.46% income-to-cash screen; legal-entity income/cash bridge with 97.08% collected-income screen; FY2025 annual corroboration of the Athene-to-AGM dividend source route and legal restrictions; bounded statutory gross-yield screens; H1 spread-dollar/compression screen; completed ARI sale/seller cash-use, collateral-control, zero seller-loan balance, `$46M` named repayment, `$335M` CECL write-off, `$2.6M` sale-discount loss, and `$8.6B`/`$8.7B`/approximately `$9B` perimeter-reconciliation boundaries; impairment boundary; named statutory consideration and interest rows; two page-level same-CUSIP holding-to-consideration bridges for AMAPS 1 and Concord; current Q2 AMAPS 1 wrapper exposure of `$2.544B` versus `$2.550B` at year-end; Athene statutory parent-affiliate receivable/payable and intercompany-cash boundary; Q2 2026 adjusted-share denominator and preferred/RSU claim bridge; new dated Q2 parent-flow observation, `$0M–$110M` receipt-attribution frontier, non-additive upstream source-to-destination bridge, parent-summary balance-sheet context of `$3.412B` cash, `$3.467B` net investments, `$1.511B` performance-fee receivable, `$(95M)` net clawback payable, `$(5.762B)` debt, and `$2.533B` net balance-sheet value; and a September 16 public-filing refresh preserving the AGM-only receipt boundary | Separated FRE/SRE/PII SOTP against dated market snapshot | Qualified financial-intermediation case | Fee cash collected at parent, regulated capital, upstream receipt allocation, Athene borrower repayment/collateral cash, asset-level liability-cost-adjusted returns, and common-owner cash |

The [Q2 policyholder-liquidity and repo-burden boundary](capital-flow-apollo-athene-q2-policyholder-liquidity-repo-burden-boundary-2026-09-15.md)
adds a measured liquidity transmission layer: contract non-surrenderability,
surrender penalties, repo payables, and collateral are visible, while actual
surrenders, haircuts, margin calls, realized sale losses, and parent cash remain
unproven.

For the Wheaton–Antamina pilot, the new [BHP–Antamina associate economics
boundary](capital-flow-wheaton-antamina-bhp-associate-economics-boundary-2026-09-16.md)
adds FY2026 operator revenue, profit, net assets, and BHP's equity-accounted
share as a distinct denominator. The aggregate equity-investment dividend line
is intentionally left unallocated, so it does not get promoted into either
Antamina cash or Wheaton stream receipts.

The Apollo–Athene lane now also has a [buyer-side ARI acquisition boundary](capital-flow-apollo-athene-ari-buyer-side-acquisition-boundary-2026-09-16.md): Athene's Q2 filing reports completion of the approximately `$8.7B` commercial-mortgage portfolio purchase from ARI on April 24, while Athene's aggregate commercial-mortgage balance increased from `$39.071B` to `$48.291B`. The same filing exposes a `$48.372B` commercial-mortgage portfolio and a `$1.027B` 90-days-past-due/non-accrual subset marked at `$695M` fair value. This improves transaction and credit-perimeter control, but the aggregate balances are not ARI loan-level attribution and do not prove borrower collections, collateral cash, liability-cost-adjusted return, or Apollo common-owner cash.

The [Schedule D residual row-boundary inspection](capital-flow-apollo-athene-statutory-schedule-d-residual-row-boundary-inspection-2026-09-16.md)
now classifies all `61` raw candidates as duplicate or continuation risks: `59`
same-page book-value matches, including the two largest (`A-1` on page 5904 and
`ADVANCE` on page 6023), plus two continuation-only non-book fields on pages
5972 and 5976. None is added to the holdings total. The current full-range
parser now reproduces the two statutory section references within `$1` each
and the separately stored combined reference within `$2`, so the aggregate
Schedule D book-value denominator is reconciled; row-level income, proceeds,
liability-cost, borrower-cash, and return proof remain open.

The new [SVF II Finco public-search refresh](capital-flow-apollo-athene-svf-ii-finco-public-search-refresh-2026-09-16.md)
adds a named-issuer denominator cross-check to Q-08. Athene's 2025 Form 10-K
reports a `$2.186B` SVF II Finco concentration, while the three year-end
Schedule D SVF II Finco rows sum to approximately the same amount. The
`G7741@-AC-4` row carries a `$2.090B` aggregate consideration field, but the
detailed rows currently classify only `$50.751M` as selected cash-like paydown
candidates and approximately `$2.039B` as tax-free-exchange/transfer holds.
This strengthens issuer and instrument observability while reducing the cash
claim; it does not prove a settlement account, borrower repayment, collateral
cash, liability-cost allocation, or realized return, and remains
`evidence-insufficient`.
The linked [row-composition boundary](capital-flow-apollo-athene-svf-ii-finco-row-composition-boundary-2026-09-16.md)
reconciles the five AC-4 rows and prevents the `$2.090B` mixed field from
entering a cash-return calculation as if it were a receipt.

The latest [retail demand-to-cash bridge](combined-investment-research-pilot-02-retail-demand-to-cash-bridge-2026-09-15.md)
now makes the affordability thesis inspectable at each handoff: social and
macro signal, comparable sales or traffic, attached-service and channel
metrics, operating cash, property spending, and unresolved owner-cash fields.
It strengthens the causal test without treating reported demand or cash-after-
property as normalized common-owner cash.

The [through-cycle causal-test protocol](combined-investment-research-through-cycle-causal-test-protocol-2026-09-16.md)
now provides the cross-pilot readiness checkpoint. Retail has a bounded lagged
diagnostic with `7` same-direction and `8` opposite-direction transitions, so
the simple affordability-to-cash lead fails promotion. Wheaton–Antamina has
only a post-close operating window; its rate and silver-price rows are stress
inputs, not repeated observations of the BHP tranche. Apollo–Athene has
period-matched spread and liquidity screens, but no repeated route-level
realized-cash and parent-receipt series. Across all three pilots, promotion
still requires repeated aligned periods, measured confound controls, and a
filing-based breaker.

## What is genuinely proven

The current system can support these conclusions:

1. Social and private-company research can generate disciplined research leads
   when its claims are labeled as directional.
2. The same force can be connected to a public-company cohort without treating
   discovery data as financial proof.
3. Different business models require different owner-cash denominators.
4. Wheaton's Antamina transaction has a publicly corroborated upfront cash
   loop and a strong named-asset stream-economics proxy.
5. Apollo's fee, spread, principal, insurance, NCI, preferred, policyholder,
   related-party, and capital-transfer layers can be separated and tested.
6. A valuation screen is more useful when it exposes the price-implied burden
   than when it produces an unsupported target price.
7. The repository can preserve source paths, evidence grades, missing upgrades,
   arithmetic checks, and falsifiers in structured artifacts.

## What remains qualified or unresolved

The system does not yet prove:

- that the social affordability signals represent a population or cause the
  mapped Inc. 5000 growth;
- that TJX, Target, or Walmart converts the hypothesized behavior into durable
  common-owner cash under normalized inventory and capital conditions;
- that the BHP Antamina PMPA's delivered ounces and settlement cash can be
  separated from the Glencore stream;
- that Antamina's after-tax and debt-adjusted return earns an acceptable IRR;
- that Apollo's consolidated or Athene cash is freely available to Apollo
  common owners; or
- that Apollo/Athene related-party exposures earn a clean, realized,
  risk-adjusted return after credit, capital, policyholder, NCI, and liquidity
  burdens.

## Completion audit against the goal

| Goal requirement | Current evidence | Status |
| --- | --- | --- |
| Social / macro force named and dated | Pilot 02 social theme and dated local sources | Qualified |
| Industry control point explained | All three pilots include burden/control maps | Proven at pilot level |
| Company or cohort selection reason | Pilot selection sections and source ledgers | Proven |
| Primary filing evidence traceable | SEC/IR artifacts and local source routes | Proven for active pilots |
| Operating model identifies payer and burden carrier | Retail, stream, and insurance models | Proven at model level |
| Reported performance reconciled to cash denominator | Apollo ANI bridge; Antamina pre-tax proxy; FY2024-FY2026 and H1 FY2027 retail OCF-less-property bridges; TJX temporary-support screen and normalization boundary | Partial |
| Reinvestment, financing, liabilities, dilution visible | Apollo and Antamina strong; Apollo Q2 adjusted-share denominator now explicitly includes preferred and RSU claims; retail burden map now populated but maintenance/growth and service economics remain incomplete | Partial |
| Damodaran valuation range and reinvestment assumptions | Three workbenches and SOTP plus the dated [September 17 market snapshot](combined-investment-research-market-snapshot-2026-09-17.md) | Qualified / illustrative |
| Lyn Alden macro/liquidity mechanism linked | Pilot-specific macro tests, dated official external macro/liquidity anchor, historical 2020–2026 regime panel, and current-regime validation across all three pilots | Qualified |
| Capital-flow proof grade prevents overclaiming | 226 structured evidence gates and verifiers, including page-level same-CUSIP, corrected same-CUSIP row bridges, same-CUSIP lot-chronology boundary, named-route liability-cost sensitivity, a period-matched FY2025 segment spread screen, an Athene buyer-side ARI portfolio-expansion boundary, the ARI Q2 seller-cash/debt-waterfall and internally reconciled cash-flow boundaries, the ARI transaction cash-consideration boundary, the ARI buyer-side acquisition and aggregate-balance boundary, the new ARI buyer-side credit boundary, the combined-stream cumulative cash-back proxy boundary, the full-year BHP-interest silver-production denominator boundary, the current-period AMAPS 1 wrapper-exposure boundary, Concord deal-level timely-interest servicing boundary, the TJX maintenance-expense accounting boundary, dated legal-dividend path, statutory parent-affiliate, BHP legal-counterparty, Apollo dilution-denominator, parent-only receipt, Athene/ADIP related-party-flow, current-period ACRA/ADIP flow, Athene investment-earnings attribution, Apollo named-route concentration, Athene full-range Schedule D population, Schedule D section-total reconciliation, blank-column parser boundary, small-parenthetical gain/loss boundary, Target attached-service burden boundaries, the retail attached-service cash-conversion frontier, the H1 TJX cash-quality screen, the retail forward-spending context gate, the Target 2026 capital-plan boundary, the Apollo–Athene parent-receipt attribution frontier, the Apollo–Athene parent-use coverage frontier, the Athene Q2 parent-flow observation, the Apollo Q2 HoldCo liquidity/intercompany boundary, the Apollo Q2 XBRL parent-receipt boundary, the Athene-to-AGM intercompany-note route, the Q2 financial-supplement source boundary, the new Q2 parent-receipt attribution frontier, the Wheaton–Antamina local-packet settlement boundary, the metal-credit accounting settlement-proof object boundary, the post-close Antamina sale-event and settlement-input boundary, the Wheaton company-level funding-envelope boundary, the Walmart FCF denominator limitation boundary, the Wheaton after-tax financed allocation frontier, the Wheaton reserve-constrained delivery ceiling, the retail cash-quality support-dependency screen, the longitudinal retail cash/regime bridge, the retail common-period normalization surface, the Inc. 5000 retail attached-services bridge, the Wheaton Investor Day forward-profile boundary, the dual Antamina PMPA threshold reconciliation, the Apollo–Athene WHCO guarantee boundary, the Apollo Broadcom fee-timing boundary, and the BHP upfront amount/date settlement bridge | Proven as system control |
| Price-implied expectation explicit | Retail and Apollo reverse-implied cash/earnings bridge plus Antamina transaction-level burden screen against the dated market snapshot | Qualified |

The [current expectation-screen index](combined-investment-research-current-expectation-screen-index-2026-09-18.md)
now consolidates the refreshed company screens across logistics, industrial
distribution, project execution, fleet, semiconductor control/materials,
digital infrastructure, materials, licensed play, and healthcare distribution.
It is explicitly not a ranking: denominators mix EV/equity value, TTM/H1/9M
periods, management FCF, reported OCF, and USD/CAD. Its value is to expose the
next source-backed burden join for each company.
| Filing-based thesis breaker | All three pilots have prose falsifier sections plus a checked nine-row cross-pilot [thesis-breaker register](combined-investment-research-thesis-breaker-register.md) | Proven as a structured control; triggers remain active-qualified |
| Reproducible source path | Ledger verifier checks source artifacts | Proven for checked artifacts |

The new [CA-06 quantified allocation surface](combined-investment-research-ca06-quantified-allocation-surface-2026-09-16.md)
consolidates the existing ranges: Wheaton annualized after-tax financed cash
of `-$42.310M` to `$444.446M`, retail reported-to-conservative screens, and an
Apollo/Athene parent-attribution frontier of `$0M–$110M`. These rows are
non-additive sensitivities; none is promoted to observed normalized owner cash.

The new [CA-06 owner-cash promotion matrix](combined-investment-research-ca06-promotion-matrix-2026-09-16.md)
joins the denominator controls across Wheaton–Antamina, the retail cohort, and
Apollo–Athene. Each row has a reported or bounded base, but final owner cash
remains missing and every pilot stays `allocation-sensitivity-only` until a
dated allocation, settlement, receipt, or waterfall closes the applicable
perimeter.

For the active retail lane, the [Q-04–Q-06 promotion action register](data/combined-investment-research-retail-promotion-action-register-2026-09-17.csv)
turns that boundary into three executable tests: settlement-date working
capital, maintenance-versus-growth capital, and service-level collection with
allocated burden. The register keeps all three rows `partial`; it is a routing
tool for the next filing or schedule, not a new owner-cash estimate.

The [TJX settlement cash-flow classification boundary](combined-investment-research-retail-tjx-q2-2026-settlement-capex-boundary-2026-09-17.md)
now records that the `$419M` net gain is reflected in operating activities,
while the `$390M` decrease in prepaid and other current assets is a mixed
working-capital line rather than a settlement receipt proxy. This strengthens
the QoE control against annualizing H1 OCF or subtracting the same settlement
twice; gross cash, legal expense, tax, and maintenance-capital allocation
remain open.

The September 18 official TJX Q2 source refresh adds the release's `$2.2B`
Q2 operating-cash-flow observation, `$2.4B` H1 shareholder-return observation,
the 4% FY2028 store-opening objective, and 23 net Q2 store additions. It does
not add a gross settlement bank-receipt/legal-payment schedule or a same-period
maintenance-versus-growth capex allocation. These are stronger direction and
date controls, not a CA-06 promotion; the TJX label remains
`temporary-support-visible; maintenance-open; owner-cash-open`.

The [valuation and expectation promotion matrix](combined-investment-research-valuation-promotion-matrix-2026-09-16.md)
now joins the market-implied expectation bridge to the CA-06 and thesis-breaker
controls. Target and Walmart's required cash, Apollo's required FRE/SRE or
principal value, and Wheaton's transaction-level burden are all explicit, but
remain `qualified-expectation-screen` inputs until the corresponding cash,
receipt, return, and claim joins are source-backed.

The latest ledger refresh adds the Apollo–Athene policyholder-liquidity and
repo-burden boundary, the Q2 company-distribution route, the retail cohort inventory/payable screen, the TJX forward capex category boundary, and a
parent-level Apollo HoldCo & Asset Management balance-sheet context: `$3.412B`
cash, `$3.467B` net investments, `$1.511B` performance-fee receivable,
`$(95M)` net clawback payable, `$(5.762B)` debt, and `$2.533B` reported net
balance-sheet value. The current checked pilot-gate total is `225`; these
remain qualified liquidity and source-boundary mechanisms rather than proof of
stress, Athene receipt, unrestricted cash, or common-owner cash.
The same Q2 materials separately report `$3.415B` in the GAAP Asset Management
segment cash line, a `$3M` presentation difference from the HoldCo summary;
the two figures are retained as distinct scope observations rather than
averaged or assigned to Athene.

Apollo's [FY2025 parent-funding disclosure](https://www.sec.gov/Archives/edgar/data/1858681/000185868126000013/apo-20251231.htm)
provides the matching legal-availability rule: AGM's primary funding source is
subsidiary distributions and other intercompany transfers, but subsidiary
distributions depend on applicable law, surplus and minimum-solvency
requirements, and prior AHL preferred-stock distributions. This constrains the
common-owner cash denominator without converting the Q2 Athene distribution
into an observed AGM receipt.

The older long-form gate enumeration in the completion-audit table retains its
original `203` label as a historical description. The authoritative current
count is the verifier-backed `225` total stated in the current control row and
surfaced in the reader and reviewer controls.

The immediately preceding refresh paragraphs used `207` and `208` as
historical refresh counts. The current authoritative verifier-backed total is
`225` after the independent SEC N-PORT Concord instrument-observability gate,
Apollo Broadcom fee-timing-boundary, combined-stream cumulative cash-back proxy,
ARI buyer-side credit-boundary, BHP full-year production-denominator, current
AMAPS 1 wrapper-exposure, Concord deal-level timely-interest servicing, and TJX
maintenance-expense accounting gates were added.

The Apollo Q2 fund-distribution route is a separate company-level observation:
the 10-Q reports `$799M` of fund distributions to the Company and a broader
`$2.040B` investment-fund/equity-method cash-flow line. Neither amount is
substituted for Athene's `$110M` H1 distribution-to-parent observation, and
neither is promoted to unrestricted AGM or common-owner cash without payer,
receiving-account, elimination, and claim-availability evidence.

The new [intercompany-note balance boundary](capital-flow-apollo-athene-intercompany-note-balance-movement-boundary-2026-09-15.md)
adds a period-end control to that route: the AHL receivable from AGM rose from
`$227M` to `$279M`, a mechanical `$52M` increase within a `$500M` facility.
Because the filing does not separate draws, repayments, accrued interest, or
bank settlement, the movement remains a balance-sheet observation rather than
cash available to Apollo common owners.

The new [WHCO guarantee boundary](capital-flow-apollo-athene-broadcom-anthropic-whco-guarantee-boundary-2026-09-16.md)
turns the Broadcom/Anthropic compute-financing reference into a named legal
route: Apollo-managed WHCO has the purchase obligation, committed financing is
expected to fund it, and Athene provides a limited guarantee if WHCO defaults.
This identifies a contingent regulated-entity burden, but does not prove
Apollo-funded cash, lender proceeds, asset ownership, guarantee utilization,
or common-owner return.

The related [Broadcom fee-timing boundary](capital-flow-apollo-broadcom-capital-solutions-fee-timing-boundary-2026-09-16.md)
adds an important timing constraint: Apollo management says the $35B financing
will be drawn over multiple quarters and that the associated capital-solutions
fee is recognized as drawn, with the larger share expected in Q4 2026 and
Q1–Q3 2027. This is a management timing expectation, not proof of fee
collection, cash settlement, margin, or common-owner realization.

The new [BHP FY2026 annual-report boundary](capital-flow-wheaton-antamina-bhp-fy2026-annual-report-boundary-2026-09-16.md)
adds a dated April 2, 2026 upfront-receipt observation, confirms metal-credit
settlement and no minimum delivery requirement, and records FY2027 copper/zinc
guidance without converting either into a silver delivery forecast. BHP's
future-volume estimate explicitly uses risked reserves/resources that are not
yet proved, so the reserve-backed annual delivery curve remains open. The
[FY2026 source manifest](data/capital-flow-wheaton-antamina-bhp-fy2026-source-manifest-2026-09-16.csv)
also separates the locally preserved canonical Form 20-F from the separately
preserved Form 6-K results artifact, preventing the two public-filing
boundaries from being treated as one document.

The Wheaton Q2 contract table adds an aggregate cash-realization anchor: the
Antamina row reports `$1.171862B` of cash flow generated to date, `56.718M`
units received and sold to date, and `1.412M` of Q2 payable metal produced but
not delivered. These figures span both the BHP and Glencore streams, so they
strengthen the combined-stream cash/timing bridge without becoming BHP-only
settlement cash.

The new [Wheaton Investor Day forward-profile boundary](capital-flow-wheaton-antamina-investor-day-forward-profile-boundary-2026-09-16.md)
reconfirms the BHP-specific `6.0 Moz` first-five-year and `5.4 Moz`
first-ten-year production-profile inputs, and records Antamina's expected
decline from `18%` of 2025 actual to `12%` of 2030 expected portfolio GEO mix.
These are explicitly management presentation inputs for expectation and
concentration analysis, not realized BHP-only credits, reserve-backed annual
delivery, or settlement cash.

The [BHP-share conversion screen](capital-flow-wheaton-antamina-bhp-share-conversion-screen-2026-09-16.md)
now places the 2023–2024 operator observations beside the directly reported
2025 BHP-share figure and the purchaser's 6.0/5.4 Moz forward profile. Its
mechanical 90% payable sensitivities are kept separate from realized metal
credits, invoices, and receipts.

The [Antamina scenario workbench](combined-investment-research-pilot-01-antamina-scenario-workbench.md)
now calibrates its base case to the disclosed `5.4 Moz` first-ten-year profile
and its bull case to the disclosed `6.0 Moz` first-five-year profile, applying
the contractual post-threshold step-down in the modeled tail. The resulting
NPV/IRR outputs remain illustrative expectation-burden screens: the base case
is `-$2.661B` / `-3.2%` and the bull case is `-$1.514B` / `1.5%` before a
source-backed tax and financing waterfall.

The purchaser-side reserve table is now locally preserved with the acquisition
exhibit, so the `65.7M` BHP-interest contained-ounce input and the 6.0/5.4 Moz
profile can be rechecked from one primary artifact. This improves source
durability but does not convert reserves or profile estimates into delivered
metal credits or cash receipts.

The profile-to-reserve cross-check now places the Investor Day `6.0M`/`5.4M`
forward profile beside the `59.13M` mechanical payable-ounce ceiling: the
first-ten-year profile sums to `57.0M`, or approximately `96.4%` of the ceiling,
leaving `2.13M` ounces under the stated-basis case. This is a consistency
sensitivity only; it does not make the management profile reserve-backed or
convert it into BHP-PMPA credits, invoices, or receipts.

The [BHP FY2026 payable-silver quantity boundary](capital-flow-wheaton-antamina-bhp-fy2026-payable-silver-quantity-boundary-2026-09-16.md)
adds a separate BHP-only annual operating denominator: `5.588M` troy ounces of
payable silver in concentrate for BHP's `33.75%` Antamina interest. The
calibration table records both a `5.029M` forward application of the PMPA's
stated `90%` factor and a `6.209M` reverse-factor gross-equivalent screen.
Neither is a settled quantity. This calibrates the threshold analysis without
assigning combined-stream output to BHP or claiming a PMPA metal-credit
transfer, invoice, settlement, or receipt.

The September 17 public-search refresh rechecked the BHP FY2026 filing against
the Wheaton Q2 packet. BHP's `$4.300B` receipt on April 2, `$4.300B` streaming
proceeds, and `$41M` liability settlements now have an explicit recipient-side
cash-flow classification control, alongside the `33.75%` / `90%` tranche,
`100M`-ounce threshold, and post-threshold `22.5%` terms. The refresh adds no
BHP-only credit quantity, invoice, settlement-price/date allocation, or
Wheaton receipt account; Q-01 remains searched-negative for that decisive
public object.

## Next work in priority order

1. Obtain a quantity-level BHP-PMPA-only metal-credit settlement schedule or
   record its public unavailability after each subsequent filing. Wheaton's Q2
   2026 report now confirms first BHP-PMPA deliveries, but only on a combined
   Antamina basis. BHP's FY2026 report confirms metal-credit settlement, no
   physical delivery, no minimum/fixed delivery requirement, and a `$41M`
   liability settlement,
   but not the ounces or invoice allocation. The BHP FY2026 operational review
now adds a five-quarter BHP-interest production/sales series and a FY2026
total; use it as a counterparty delivery-curve proxy, not as the Wheaton
metal-credit ledger. The Q4 proxy was also corrected to avoid applying the
33.75% BHP ownership factor twice: BHP's table already reports its attributable
interest. The separate 90% factor remains only a mechanical payability screen.
2. Complete the common TJX/Target/Walmart operating table. All three now have
   annual reported cash bridges; TJX also has an H1 FY2027 bridge and a
   source-bounded temporary-support screen. The remaining upgrade is
   maintenance-versus-growth capital, leases, dilution, markdown, and
   attached-service normalization across the cohort.
3. Separate Athene-related-party investment returns, impairment, fees, and
   distributions from Apollo parent cash.
4. Refresh the dated market inputs and rerun all valuation screens when the
   next filing/price snapshot is available.
5. Promote a pilot only when its missing upgrade is source-backed, not because
   its narrative has become more persuasive.

The first retail owner-cash bridge is now captured in the [retail bridge memo](combined-investment-research-pilot-02-retail-owner-cash-bridge.md)
and its [structured CSV](data/combined-investment-research-pilot-02-retail-owner-cash-bridge.csv).
TJX's FY2024-FY2026, Target's FY2023-FY2025 and H1 2026, and Walmart's
FY2024-FY2026 and H1 FY2027 OCF-less-property values reconcile directly. The bridge records
Target's inventory, payable, supplier-finance, and tariff-refund boundaries and
Walmart's inventory, payable, capex, tax-timing, and company-defined-FCF
boundaries. TJX's annual filing-backed cash fields and H1 FY2027 cash bridge
are now populated. The H1 bridge is qualified because tariff refunds and a
credit-card interchange-fee settlement increased operating cash flow;
normalized owner-cash fields remain open.

The [common-period cash matrix](combined-investment-research-pilot-02-retail-common-period-cash-matrix.md)
now also carries filed net-sales denominators and the mechanical
cash-after-property percentage of sales: TJX `7.409%`, Target `4.069%`, and
Walmart `1.528%` for the selected first-half periods. These ratios improve
scale comparability, but they remain reported-denominator screens because
temporary support, working-capital timing, leases, maintenance capital,
taxes, service costs, and dilution are not fully normalized.

The same matrix now records a gross-margin basis for the selected periods:
TJX's `32.376%` is calculated from filed sales and cost of sales including
buying and occupancy, while Target's `31.4%` and Walmart's `24.9%` are reported
gross-margin rates that include disclosed tariff-refund effects. These are
operating-quality inputs, not normalized margin conclusions.

The retail normalization review now explicitly reconciles two TJX low-screen
bundles: `$1.631B` after the `$470M` payable-support signal and `$85M` SBC, versus
`$1.351B` after the separate `$750M` tariff/interchange candidate and `$85M` SBC.
They are not additive deductions; the first leaves tariff/interchange treatment
unresolved, while the second is a temporary-support stress case. Neither is
promoted to normalized owner cash.
The matrix also carries a mechanical ex-support screen of `31.254%` for TJX,
`29.479%` for Target, and `24.054%` for Walmart after removing the recorded or
source-bounded tariff benefit. Those figures are sensitivity outputs; TJX's
tariff amount is explicitly a candidate support amount and Walmart's refund is
approximately disclosed, so none is promoted to recurring margin.

The new [TJX temporary-support bridge](combined-investment-research-pilot-02-tjx-h1-temporary-support.md)
isolates `$331M` of H1 tariff refunds and the `$419M` net accounting gain from
the interchange-fee settlement as a `$750M` mechanical support screen. The
FY2026 10-K identifies `$470M` of gross gain and `$51M` of legal expense; the
H1 filing confirms settlement-related amounts entered operating activities but
does not isolate the bank receipt. Its illustrative low, base, and high H1
cash screens are `$1.351B`, `$2.101B`, and `$2.186B`; these are sensitivity
cases, not observed or promoted owner cash.

The [retail capex-classification boundary](combined-investment-research-pilot-02-retail-capex-classification.md)
now records the latest filing evidence without manufacturing maintenance splits:
TJX identifies H1 uses and states that ordinary maintenance and repairs are
expensed as incurred, but does not quantify the maintenance content of
capitalized renovations; Target identifies remodels
and new stores as drivers but does not disclose the H1 allocation; its FY2025
10-K likewise states that repair and maintenance costs are expensed as
incurred and reports a `$2.835B` FY2025 cash-after-property screen; while
Walmart discloses exact H1 category amounts across platform, remodel, new-store,
and international spending and its FY2026 10-K states that normal repairs are
expensed while major improvements are capitalized. That accounting boundary
prevents a second generic maintenance deduction, but it does not classify the
capitalized categories. Total property spending remains the defensible
denominator until a quantified maintenance schedule appears. The latest
forward-spending refinement adds TJX's approximately `$2.2B–$2.3B` FY2027
capital-spending guide, including approximately `$1.000B` renovations, `$992M`
offices/distribution/IT, and `$222M` new stores, and confirms that Target's H1
direction remains qualitative; these improve burden visibility without
changing the owner-cash grade.
The same TJX Q2 filing gives an exact H1 capex total of `$1.159B`, split by
segment as Marmaxx `$690M`, HomeGoods `$146M`, TJX Canada `$190M`, and TJX
International `$133M`. The segment split improves the burden denominator but
does not separate replacement/maintenance from growth within those amounts.
TJX's H1 operating cash flow of `$3.345B` less that capex produces a mechanical
`$2.186B` cash-after-property screen; it remains outside normalized owner cash
until maintenance, tax, lease, and other burden allocation is resolved.
The [TJX Q2 cash/capex boundary](combined-investment-research-tjx-q2-cash-capex-boundary-2026-09-18.md)
also records the filing's identified tariff-refund and credit-card interchange
drivers, the planned `$1B` September-note repayment, and the `$2.2B–$2.3B`
FY2027 capex guide as separate cash-quality and forward-claim controls.
The [September 16 public-source refresh](combined-investment-research-pilot-02-retail-capex-public-source-refresh-2026-09-16.md)
adds Target's `$1.4B` Q2 capex observation and rechecks the current TJX,
Target, and Walmart routes; it still finds no company-wide maintenance ledger.
Target's official store-investment strategy separately frames remodels and new
stores as long-term growth investment, so the category direction can carry a
`strategic-growth-context` label. This still does not allocate Target's H1
spending or establish the maintenance/replacement share.
The FY2025 10-K was separately tested for an annual dollar category table; its
MD&A and cash-flow disclosures do not replace the older approximate category
reference with a filing-backed split. That historical mix therefore remains
context only and cannot be used to prorate H1 2026 or label existing-store
capital as maintenance.
The companion [Target attached-service public-search boundary](combined-investment-research-pilot-02-target-attached-service-public-search-boundary-2026-09-16.md)
now applies the same control to Q-06: the latest 10-Q's revenue and aggregate
burden fields are preserved, while service-level allocation is classified as a
searched-negative public result and remains outside owner cash.
The same filing discloses a consolidated `$959M` gift-card liability and H1
issuance/redemption roll-forward; this is retained as a customer-funding and
revenue-timing boundary, not attributed to attached services or added to owner
cash.
The [structured Target gift-card boundary](combined-investment-research-pilot-02-target-gift-card-liability-boundary-2026-09-16.md)
reconciles the disclosed `$1.197B` beginning liability, `$376M` issued, and
`$614M` recognized from the beginning liability to the `$959M` ending balance.

The September 18 [retail known-growth-floor frontier](combined-investment-research-retail-known-growth-floor-frontier-2026-09-18.md)
adds a same-period capex control without relabeling mixed spending. TJX's H1
OCF less property is `$2.186B` with a `$222M` disclosed new-store floor;
Target's is `$2.115B` with no quantified H1 growth floor; and Walmart's is
`$5.529B` with a `$1.087B` new-store/expansion/relocation floor. The remaining
property pools are `$937M`, `$2.404B`, and `$13.094B`, respectively, but remain
unallocated. This strengthens Q-05's denominator boundary while preserving
CA-06 as partial and all three retail screens as unranked.
Target's official Q2 call further identifies the `$2.4B` H1 deployment as
incremental investment in new stores, full-store remodels, supply chain, and
technology, and separately describes higher field-team hours, training,
incentive compensation, and capital-project spending in SG&A. It still does
not provide dollar maintenance allocation or attached-service cost and
collection joins, so these remain classification and burden controls rather
than normalized owner cash.

The September 18 [H1 attached-services frontier](combined-investment-research-retail-h1-attached-services-frontier-2026-09-18.md)
adds the same-period Q-06 surface: Target's `$1.141B` pool comprises `$525M`
advertising, `$269M` credit-card profit sharing, and `$347M` other revenue;
Walmart reports `$3.904B` consolidated membership and other income versus a
`$3.855B` segment subtotal. These are consolidated operating inputs, not an
increment to OCF or owner cash. TD card ownership, mixed Walmart composition,
allocated service costs, capital, tax, and remittance remain unresolved, so
Q-06 and CA-06 stay partial.
Walmart's Q2 call also records the burden side: tariff refunds were reinvested
in price, higher depreciation followed capex, self-insurance costs increased,
and management expects more than `$2B` of incremental FY2027 fuel-related
costs plus Vibe integration cost. These are normalization inputs, not
period-matched service costs or additional H1 deductions; the associated
collection, allocation, and common-owner joins remain open.

The September 18 [supplier-finance settlement frontier](combined-investment-research-retail-supplier-finance-settlement-frontier-2026-09-18.md)
strengthens Q-04's non-double-counting rule. Target's `$3.2B` versus `$3.0B`
eligible-obligation movement and Walmart's `$6.4B` versus `$6.0B` movement are
not cash-paid settlement schedules; their `$612M` and `$1.257B` payable sources
remain within reported OCF. Target's Q2 filing expressly says the eligible
balance does not represent actual early payments and that actual early
payments have historically been lower. Walmart provides the confirmed-invoice
payment mechanics but not the period-matched settlement waterfall. The
frontier records `$0M–$200M` and `$0M–$400M` hypothetical attribution ranges
without promoting any amount to owner cash. TJX's absent comparable note
remains an unresolved source route.

The official September 18 interim HTML recheck also preserves the lease/tax
boundary: Target has no matched H1 cash-paid lease or tax line; Walmart's
`$(211)M` accrued-income-tax movement is not taxes paid; and TJX's `$5M` lease-
liability and tax recoverable/payable movements are not dedicated cash lines.
The inline-XBRL tag recheck also found no dedicated Target/Walmart
`PaymentsOfIncomeTaxes`, `OperatingLeasePayments`, or equivalent H1 cash fact.
The lease/tax gap is now a precise HTML-plus-inline-XBRL searched-negative for
the checked public objects, not an invitation to import annual cash into H1.

The [retail burden-normalization memo](combined-investment-research-pilot-02-retail-burden-normalization.md), [supplier-finance boundary](combined-investment-research-pilot-02-retail-supplier-finance-boundary.md), and [attached-services boundary](combined-investment-research-pilot-02-retail-attached-services-boundary.md)
now adds filing-backed lease, diluted-share, capital-return, and capex-category
fields. TJX reports `$10.620B` of operating lease liabilities and `$2.214B` of
operating-lease cash paid; Target reports `$3.733B` of operating lease
liabilities and `456.2M` H1 diluted shares; Walmart reports `$16.512B` of
operating lease obligations, `7,989M` H1 diluted shares, and `$14.181B` of H1
capex split across platform, remodel, new-store, and international categories.
These are burden inputs, not deductions already proven to produce normalized
owner cash.
The [attached-services public-source refresh](combined-investment-research-pilot-02-retail-attached-services-public-source-refresh-2026-09-16.md)
rechecks the current Target, Walmart, and TJX disclosures and preserves the
rule that ancillary revenue is not added one-for-one to owner cash.
Walmart's latest filing also states that Sam's Club membership fees are
deferred and recognized ratably over the one-year membership term. Because no
membership-only liability or service-level collection schedule is disclosed,
this is retained as a timing boundary rather than treated as period cash.
TJX's latest filing adds a comparable `$825M` deferred-gift-card balance and
`$963M` of H1 recognized gift-card revenue, but says the cards are one
homogeneous pool that is not separately identifiable. This remains a
customer-funding timing boundary, not attached-service or owner-cash evidence.
TJX's H1 filing identifies a dated interchange-fee settlement whose related
amounts were received during the quarter ended May 2, 2026. The `$419M` figure
is the net accounting gain, not a separately quantified bank receipt, and is
retained as an exceptional-support sensitivity rather than recurring
attached-service economics.
Target's official Roundel fact sheet adds an 800-plus-person integrated team,
more than 2,000 vendors, and a management-defined `$2B+` value claim. The
claim is not defined as GAAP revenue, profit, or cash, so it strengthens the
control-point and labor-burden narrative without entering owner cash.

The [Walmart known-growth capex boundary](combined-investment-research-pilot-02-walmart-known-growth-capex-boundary.md)
uses the separately disclosed `$1.087B` new-stores-and-clubs category as a
qualified growth-capital floor. Under the narrow classification that all other
H1 capex is maintenance, the implied OCF-after-maintenance floor is `$6.616B`,
versus `$5.529B` under the mechanical OCF-less-total-capex bridge. This narrows
the capex range but remains an inference and not normalized owner cash.

The [normalized-cash screen](combined-investment-research-pilot-02-retail-normalized-cash-screen.md)
now applies only source-bounded adjustments. The illustrative low/base/high
screens are TJX `$4.464B/$4.703B/$4.917B`, Target H1 `$0.597B/$1.209B/$2.115B`,
and Walmart H1 `$3.881B/$5.529B/$5.529B`. These periods are not directly
comparable and the values are not promoted to owner cash; they expose the
known tariff, payable, stock-compensation, and supplier-term sensitivity.

The [common-period normalization surface](combined-investment-research-pilot-02-retail-common-period-normalization-surface-2026-09-15.md)
now makes the full burden stack auditable in one place. Its source-bounded
stacked residual screen is `$1.351B` for TJX, `($0.473B)` for Target, and
`($1.322B)` for Walmart after the disclosed support candidate, selected
stock-compensation sensitivity, and debt-principal repayment. These are stress
screens rather than observed negative owner cash: the support and working-
capital signals can overlap, while maintenance capital, leases, taxes,
seasonality, attached-service costs, and dilution remain unresolved.

The companion [per-diluted-share sensitivity](combined-investment-research-pilot-02-retail-stacked-residual-per-share-sensitivity-2026-09-16.md)
translates the same numerator without changing its proof grade: TJX `$1.208`,
Target `($1.036)`, and Walmart `($0.165)` per diluted share. This gives the
Damodaran and price-implied layers a transparent stress frontier, but neither
the numerator nor the per-share result is normalized owner cash or a direct
investment ranking.

The [Walmart H1 denominator control](combined-investment-research-pilot-02-walmart-h1-owner-cash-denominator-control-2026-09-15.md)
now joins the filing's exact capex categories, `$2.303B` debt repayment,
`$5.104B` repurchases, and `7.989B` diluted-share denominator to the
`$5.529B` cash-after-property screen. The same control now records Walmart's
`$16.512B` operating-lease obligation balance and `$3.141B` H1 tax provision
against `$15.160B` pretax income; neither is treated as a cash deduction because
separate H1 lease payments and cash taxes paid remain undisclosed. It improves
the owner-claim bridge but does not promote the result to normalized owner cash:
maintenance allocation, payment timing, supplier finance, attached-service
costs, and seasonality remain open.

The [Target H1 denominator control](combined-investment-research-pilot-02-target-h1-owner-cash-denominator-control-2026-09-15.md)
adds the corresponding `$1.070B` debt reduction, `$1.034B` dividends,
`$154M` share-based compensation, `456.2M` diluted-share denominator, and
`$3.2B` supplier-finance-eligible vendor obligations to Target's `$2.115B`
cash-after-property screen. The source distinction is now explicit: H1
property-and-equipment spending was `$2.404B`, while total investing cash use
was `$2.397B` after `$7M` of other investing activity; `$2.115B` is the
derived `$4.519B` operating-cash-less-property figure, not reported capex.
The current-period maintenance-capital split and normalized owner-cash result
remain held. The same filing recheck now records `$3.733B` of operating-lease
liabilities and `$172M` of trailing-twelve-month lease interest in Target's
ROIC presentation, while H1 cash lease payments are not separately disclosed;
it also records an `$835M` H1 tax provision and `23.9%` effective rate without
an H1 cash-tax line. These sharpen burden visibility but are not additional
cash deductions until payment timing is joined.

The [Target Q2 2026 cash-quality perimeter upgrade](combined-investment-research-target-q2-2026-cash-quality-perimeter-upgrade-2026-09-17.md)
refreshes the CA-06 row through August 1, 2026. It adds the current `$4.519B`
OCF, `$2.404B` property spending, `$994M` tariff-refund support, `$3.2B`
supplier-finance obligation balance, debt/dividend/SBC claims, and the
current lease-liability perimeter. H1 cash-paid lease and tax lines,
maintenance allocation, service costs, and normalized owner cash remain open.

Target's August 14, 2026 five-year credit agreement adds a post-quarter-end
liquidity boundary to the same lane: Target Corporation is the borrower on
`$4.0B` of aggregate commitments, and the agreement permits general corporate
use of loan proceeds. The checked filing does not evidence a draw, receipt,
operating use, or repayment, so the facility is a legal funding backstop and
stress input—not H1 cash, capex funding, supplier-finance settlement, or
common-owner cash. The [Target Q2 cash-quality boundary](combined-investment-research-retail-target-q2-2026-cash-quality-boundary-2026-09-17.md)
records the borrower, use-of-proceeds, covenant, and replacement-facility
perimeter.

The [retail cohort denominator control](combined-investment-research-pilot-02-retail-cohort-owner-cash-denominator-control-2026-09-15.md)
now puts TJX, Target, and Walmart on one source-bounded residual surface while
keeping the periods and denominators explicitly non-comparable. The safe
cohort conclusion is that reported cash bridges exist; normalized common-owner
cash is not ranked.

The annual [cash-per-diluted-share table](combined-investment-research-pilot-02-retail-annual-per-share-cash.md)
now reconciles reported cash after property spending to diluted shares: TJX
`$4.359`, Target `$6.223`, and Walmart `$1.860` per diluted share. This is a
common reported denominator, not a ranking or valuation conclusion; lease,
working-capital, tax, maintenance-capex, and attached-service differences remain
material.

The new [annual lease-and-tax cash control](combined-investment-research-pilot-02-retail-annual-lease-tax-cash-control-2026-09-16.md)
adds cash-paid observations that are missing from the current H1 burden rows:
TJX paid `$2.214B` of operating-lease cash and `$1.471B` of income taxes in
FY2026; Target paid `$529M` and `$1.091B` in FY2025; and Walmart paid `$2.315B`
and `$5.364B` in FY2026. These are already inside operating cash flow and are
not subtracted again. The control improves annual burden visibility, but the
annual/H1 mismatch and maintenance-capital, supplier-finance, service-cost,
seasonality, dilution, and normalized owner-cash allocations remain open.

The [Q-03 full-return input schema](capital-flow-wheaton-antamina-q03-full-return-input-schema-2026-09-16.md)
turns the Wheaton financing gap into 13 model-input fields spanning entitlement,
delivery, realized price, receipt, funding, debt service, tax, reserve life,
and IRR/NPV. It does not fill missing fields with company-level proxies; it
defines the source, period, denominator, and upgrade document required before
promotion.

The [Q-07 common-owner input schema](capital-flow-apollo-athene-q07-common-owner-input-schema-2026-09-16.md)
applies the same discipline to Apollo–Athene: it separates earnings, legal
availability, subsidiary distribution, AGM receipt, intercompany elimination,
senior claims, dilution, and the final common-owner residual. The checked
public filing and supplement perimeter is now explicitly `searched-negative`
for an AGM-only receiving-account line, while the controlled elimination
schedule remains missing. The `$0M–$110M` attribution range therefore remains
a sensitivity, not a dated receipt or common-owner waterfall. The new [Athene
2026 credit-agreement purpose perimeter](capital-flow-apollo-athene-2026-credit-agreement-purpose-perimeter-2026-09-17.md)
adds a `$1.750B` AHL/Athene facility, borrower perimeter, permitted-use, and
affiliate-transaction control. Athene's Q2 10-Q also reports no amounts
outstanding under the current or previous external credit facilities at June
30, 2026. That closes the external revolving-facility draw hypothesis at the
quarter end, but not the separate intercompany-note or AGM-receipt question.

The new [retail cohort owner-cash input schema](capital-flow-retail-owner-cash-input-schema-2026-09-16.md)
turns CA-06 into a field-level checklist across reported cash, working capital,
temporary support, supplier finance, leases, taxes, reinvestment, attached
services, senior claims, dilution, and the final residual. It preserves the
first screen—operating cash flow less total property spending—while withholding
normalized owner cash until the missing period-matched fields are joined.

The new [quality-of-earnings and financial-shenanigans overlay](combined-investment-research-quality-of-earnings-financial-shenanigans-overlay-2026-09-16.md)
formalizes the existing tests for accrual quality, working-capital timing,
capitalization, temporary support, dilution, revenue timing, related-party
flows, and legal-entity cash. It keeps the cross-pilot composite accrual screen
not-assembled and treats unusual ratios as falsifiable diagnostics rather than
fraud findings.
The overlay now also provides an explicit QoE-to-thesis-breaker handoff: BHP
settlement and financed-return tests route to `TB-WPM-01` through `03`, retail
working-capital/service/capex warnings route to `TB-RET-01` through `03`, and
Apollo fee, legal-entity, credit, and ARI warnings route to `TB-APO-01` through
`03`. No breaker is activated by a ratio alone; each still requires a
same-entity, same-period, cash-or-claim reconciliation.

The [CA-06 promotion matrix](combined-investment-research-ca06-promotion-matrix-2026-09-16.md)
now makes that same standard operational across the three pilots. A promotion
requires a joinable legal entity, period, denominator, cash-or-claim object,
and reconciliation path; the required bundle differs by business model. QoE
and financial-shenanigans diagnostics can block, bound, or break a thesis, but
they cannot promote a denominator on their own. Missing source objects remain
`allocation-sensitivity-only` and are routed to the next evidence queue.

The retail working-capital layer now adds a same-period QoE double-count
control: balance-sheet signals of `-$116M` / `-$261M` / `-$1.492B` for TJX,
Target, and Walmart sit beside cash-flow signals of `-$133M` / `-$333M` /
`-$1.012B`. These are diagnostic differences, not additive owner-cash
adjustments. Period-end supplier-finance balances remain excluded unless a
settlement-date bridge joins them to cash.

The companion [composite QoE input schema](combined-investment-research-quality-of-earnings-composite-input-schema-2026-09-16.md)
now distinguishes partial annual-vector coverage from fields still missing
across the longitudinal panel. Target receivables, Walmart's non-identical
OSG&A, claim/taxonomy joins, and transaction boundaries remain explicit. It is
the acquisition and promotion queue for the future cross-pilot accrual screen,
not an implied score.

The first assembled QoE component is the [18-row retail cash-conversion
screen](combined-investment-research-quality-of-earnings-retail-cash-conversion-screen-2026-09-16.md).
It identifies one negative cash-after-property stress observation and several
conversion declines, but it is not an accrual or fraud score; the missing
net-income and balance-sheet vector keeps the composite diagnostic open.

The narrower [current retail earnings-to-cash screen](combined-investment-research-quality-of-earnings-current-retail-earnings-cash-screen-2026-09-16.md)
now joins H1 net income to operating cash and property spending for all three
retailers. It improves the current-period QoE input surface while preserving
the Walmart noncontrolling-interest boundary and the unresolved normalized
owner-cash and historical accrual questions.

The companion [current retail composite input panel](combined-investment-research-quality-of-earnings-current-retail-composite-input-panel-2026-09-16.md)
fills the directly disclosed H1 revenue, earnings, receivable, inventory,
payable, current-asset, PP&E, D&A, dilution, OCF, and property-spending fields
for the three retailers. It keeps Target receivables, Target's clean combined
debt/lease claim, Walmart SG&A, and Walmart SBC missing where the filings do
not provide a comparable isolated field. This advances the input surface but
does not assemble a multi-period composite accrual score or promote any row to
normalized owner cash.

The [current retail diagnostic ratio panel](combined-investment-research-quality-of-earnings-current-retail-diagnostic-ratio-panel-2026-09-16.md)
now adds comparable OCF conversion, post-property conversion, capex intensity,
inventory-versus-payable timing, D&A, SBC, and debt/lease-claim ratios. It is
diagnostic rather than a Beneish score: Target claim burden, Walmart SBC and
SG&A, and the full multi-period accrual vector remain missing or partial.

The [forensic QoE methods map](combined-investment-research-quality-of-earnings-forensic-methods-map-2026-09-16.md)
now makes the method layer explicit: Sloan-style accrual persistence, the
Beneish input family, Schilit-style warning families, cash-earnings quality,
revenue timing, and related-party/perimeter review are each tied to an
evidence route and promotion rule. This prevents the project from using
“financial shenanigans” as an impressionistic label.

The first historical vector is now assembled for [TJX FY2024–FY2026](combined-investment-research-quality-of-earnings-tjx-historical-vector-2026-09-16.md).
It joins annual earnings, OCF, property additions, inventory/payable cash
effects, D&A, SG&A, SBC, diluted shares, equity-investment purchases, and
debt/lease claims. OCF/NI declines across the period while the FY2026
inventory-minus-payable cash burden widens; these are diagnostic prompts, not
evidence of manipulation. The vector remains company-specific until comparable
Target and Walmart histories are assembled.

The second historical vector is now assembled for [Target FY2023–FY2025](combined-investment-research-quality-of-earnings-target-historical-vector-2026-09-16.md).
It preserves Target's missing receivable field and partial current-lease
perimeter rather than treating “other current assets” or total liabilities as
substitutes. Target's OCF/NI declines and claims/OCF rises across the annual
period; the result is a diagnostic burden signal, not an earnings-management
finding.

The third historical vector is now assembled for [Walmart FY2024–FY2026](combined-investment-research-quality-of-earnings-walmart-historical-vector-2026-09-16.md).
It keeps consolidated net income, Walmart-attributable net income, and
noncontrolling interest separate; adds supplier-finance obligations,
transaction cash, dilution, and Walmart's property-only FCF convention; and
flags Walmart OSG&A as non-equivalent to the TJX/Target SG&A fields. The
three-company history is now materially stronger, but the cohort-level
composite remains held until taxonomy normalization and the remaining
receivable, lease, tax, maintenance-capital, and owner-cash joins are closed.

The [retail QoE comparability bridge](combined-investment-research-quality-of-earnings-retail-comparability-bridge-2026-09-16.md)
now makes that boundary machine-readable across all nine annual rows. It
promotes the property-only cash screen to `comparable-diagnostic`, while
keeping the composite accrual result `not-promotable` because Target
receivables, Walmart OSG&A, lease/claim perimeters, fiscal alignment, and
transaction taxonomy are not yet fully joined.

The [retail QoE trend diagnostics](combined-investment-research-quality-of-earnings-retail-trend-diagnostics-2026-09-16.md)
now converts those vectors into a follow-up register. Target and Walmart are
high-priority diagnostic cases because post-property conversion weakened while
claims or SBC burdens rose; TJX is medium priority because conversion softened
but claims/OCF improved. These are document-prioritization signals, not fraud
findings or a normalized ranking.

The new [retail QoE transition panel](combined-investment-research-quality-of-earnings-retail-transition-panel-2026-09-16.md)
assembles six adjacent-period same-company transitions with raw ratio changes
for working capital, cash conversion, post-property cash, capex intensity,
claims, and SBC. It makes the financial-shenanigans review reproducible at the
transition level while keeping the composite score `not-promotable` because
Target receivables, Walmart OSG&A, claim perimeters, transaction taxonomy, and
legal-entity cash joins remain incomplete.

The companion [capital-flow QoE ratio panel](combined-investment-research-quality-of-earnings-capital-flow-ratio-panel-2026-09-16.md)
extends the same discipline to Wheaton–Antamina and Apollo–Athene. It records
denominator-labeled screens for stream OCF, BHP liability settlement, Athene
cash-to-earned investment income, fee roll-forward settlement, and bond
turnover. These are diagnostic ratios—not owner cash, cross-pilot rankings, or
proof of a completed receipt or return.

The [expansion-lane QoE overlay](combined-investment-research-expansion-lane-qoe-overlay-2026-09-16.md)
now applies the same boundaries to the next-cycle power-grid, insurance
statutory, and asset-backed lanes. It adds twelve field-level diagnostics for
recovery timing, statutory income, disposal realization, legal availability,
collateral eligibility, fleet cash conversion, and source-of-funds allocation;
it explicitly remains a diagnostic register rather than a manipulation score.

The companion [interim lease-and-tax search boundary](combined-investment-research-pilot-02-retail-interim-lease-tax-search-boundary-2026-09-16.md)
checks the latest Q2/H1 filings and records a bounded result: TJX reports
`$1.147B` of H1 operating-lease cash paid, while no matched-period cash-tax
line is located for TJX and no comparable cash-paid lease/tax schedule is
located for Target or Walmart; the Target and Walmart inline-XBRL tag search
also found no dedicated cash-payment fact. This does not prove that unreported
payments were zero; it prevents annual observations from being carried into H1
as matched-period owner cash.

The Concord public-document recheck adds a separate Q-08 servicing boundary:
KBRA's July 2026 surveillance page provides a dated quarterly-payment scope and
timely-interest proxy for Series 2024-1 and Series 2025-1/2/3, while the linked
transaction pages redirect to login and do not expose the underlying tables.
This is security-level servicing evidence only; it does not prove Athene
ownership, trustee remittance, borrower collections, or liability-adjusted
return.
The companion [power-grid evidence panel](combined-investment-research-power-grid-customer-cash-evidence-panel-2026-09-17.md)
puts the three routes on one denominator-controlled page: FPL's category
recovery, AEP's load-to-rate-base pathway, and Duke's named Anderson County
project. Each remains collection-and-return-open.

The [attached-services boundary](combined-investment-research-pilot-02-retail-attached-services-boundary.md)
records Target H1 advertising revenue of `$525M`, credit-card profit sharing of
`$269M`, and other revenue of `$347M`, alongside Walmart U.S. membership and
other income of `$1.676B`, Walmart International of `$851M`, and Sam's Club of
`$1.328B`. Walmart also identifies selected advertising, fulfillment, and data
insights within its e-commerce ecosystem. These figures prove attached-service
control points, not standalone margin or owner cash; allocated costs, capex,
working capital, tax, and cash collection remain open.

The [Target Q2 burden-boundary upgrade](combined-investment-research-pilot-02-target-q2-attached-service-burden-boundary-2026-09-15.md)
adds the current Q2/H1 denominator screen: attached revenue is `$592M` in Q2
and `$1.141B` in H1, while merchandising cost of sales is `$15.775B` and
`$32.053B`, supply-chain and digital-fulfillment cost is `$1.828B` and
`$3.611B`, and a temporary `$994M` IEEPA tariff refund reduced cost of sales.
These costs and benefits are company-level or aggregate; they do not allocate
service-level cash conversion, and the temporary refund is not recurring owner
cash.

The [Target Q2 management-call control-point memo](combined-investment-research-pilot-02-target-q2-management-call-control-point-upgrade-2026-09-15.md)
now preserves the official transcript's traffic, digital-delivery,
non-merchandise, tariff-refund, and reinvestment observations. These claims
strengthen the operating-mechanism narrative, but remain management evidence;
service-level cost and owner-cash conversion are still held.

The [attached-services cash frontier](combined-investment-research-pilot-02-retail-attached-services-cash-frontier-2026-09-15.md)
quantifies the unresolved conversion variable from 0% to 100% for the
disclosed Target and Walmart pools. For Walmart, the frontier uses the
`$3.855B` subtotal of three disclosed segment rows, while the consolidated
filing reports `$3.904B`; the `$49M` difference is preserved in the [attached-
income denominator reconciliation](combined-investment-research-pilot-02-walmart-attached-income-denominator-reconciliation-2026-09-16.md).
The frontier remains sensitivity-only: no value enters normalized owner cash
until service-level collection and burden allocation are source-backed.

The [Target inventory/payable balance-change screen](combined-investment-research-pilot-02-target-inventory-payable-balance-screen-2026-09-15.md)
adds a mechanical H1 working-capital signal: inventory rose `$945M` from
January 31 to August 1, 2026 while accounts payable rose `$684M`, producing a
`-$261M` two-line balance signal. It is a useful burden indicator, not a
replacement for the full operating-asset/liability cash-flow reconciliation.

The [cross-cohort inventory/payable balance and cash-flow screen](combined-investment-research-pilot-02-retail-cohort-inventory-payable-balance-screen-2026-09-15.md)
extends that test across TJX, Target, and Walmart and cross-checks the balance
signals against each filing's cash-flow rows. The direction is consistent with
working-capital pressure, but balance changes and cash-flow effects differ
because of timing and presentation; neither is promoted to recurring owner cash.

The [retail consolidated cash frontier](combined-investment-research-pilot-02-retail-consolidated-cash-frontier-2026-09-15.md)
now joins maintenance-capital and support-removal sensitivities. Under the
four-corner screen, the support-removed/full-maintenance values are `$1.436B`
for TJX, `$751M` for Target, and `$981M` for Walmart before separately testing
tax, leases, services, dilution, and seasonality. These are bounded screens,
not promoted owner cash.

The current Walmart Q2 earnings release adds an operating-growth signal to
this control-point map: Walmart U.S. advertising grew `38%`, Walmart Connect
grew `43%` excluding VIZIO, and global membership-fee revenue grew `17%`.
These rates support the service/cultural-consumption thesis but disclose
neither service-level dollars nor the costs, taxes, capex, collection timing,
and legal-entity transfers needed for owner cash. They therefore do not change
the normalized-cash exclusion.

The [BHP legal-counterparty boundary upgrade](capital-flow-wheaton-antamina-bhp-legal-counterparty-boundary-upgrade-2026-09-15.md)
adds the FY2026 annual-report distinction that the stream is with a BHP
wholly owned subsidiary and that Antamina is not a party. This separates the
stream obligation from the Antamina joint-venture and customer perimeter, but
does not produce a BHP-only metal-credit invoice or cash receipt.

The [Q2 first-delivery receipt boundary](capital-flow-wheaton-antamina-q2-first-delivery-receipt-boundary-2026-09-15.md)
upgrades the delivery evidence: Wheaton explicitly says it received its first
BHP-PMPA deliveries during Q2 2026. The reported `2.319M` produced and
`2.063M` sold Antamina silver ounces remain a combined Glencore/BHP quantity,
however, so BHP-only ounces,
metal-credit settlement, ongoing payment, and receipt cash remain unresolved.
The same Q2 financial statements report combined Antamina stream revenue of
`$150.549M`, profit of `$77.323M`, operating cash flow of `$122.039M`, and
stream assets of `$4.708B` for the quarter; the roll-forward shows `$5.201B`
of cost and `$492.6M` of accumulated depletion. These figures anchor the first-
delivery period's combined economics, but they are not BHP-only settlement
cash or a common-owner cash denominator.
Wheaton's accounting policy further states that precious-metal credit revenue
is recognized when the credits are sold and control transfers to the customer;
for concentrate sales, final settlement uses recovered ounces, confirmed
smelter weights, settlement assays, and the quotation period. This defines the
missing accounting event chain, but the Q2 Antamina segment does not identify
the BHP-only credit sale, invoice, or collection entry.

The detailed receipt-boundary review also records an interpretation control:
the Q2 MD&A's statement that monthly silver delivery occurred throughout 2026
appears in the Mineral Park development-stage update, not the Antamina update.
It is therefore excluded from the BHP-Antamina delivery and settlement proof.

The post-Q2 source refresh also checks BHP's April 2026 operational review,
which updates Antamina copper guidance to `150–160 kt` for FY26 without
providing an annual silver forecast or BHP-PMPA delivery schedule. That source
improves mine-operating context only; copper guidance is not converted into a
silver delivery or Wheaton-cash assumption.

The [BHP threshold-timing screen](capital-flow-wheaton-antamina-bhp-threshold-timing-screen-2026-09-15.md)
uses the reported BHP-interest series and transaction profile to bound a
mechanical `16.67–18.52` year timing range for the `100M`-ounce step-down. It
is a sensitivity input only; it does not replace reserve-backed delivery,
payability, or settlement evidence.

The [reserve-capped upfront-recovery frontier](capital-flow-wheaton-antamina-reserve-capped-upfront-recovery-frontier-2026-09-15.md)
now translates the `65.7M` contained-ounce reserve input and `90%` payable
factor into a bounded recovery screen. At `$90/oz`, the current disclosed
reserve quantity produces `$4.257B` of gross stream cash before burden, or
`99.01%` of the `$4.300B` upfront payment; a 20% burden haircut reduces that
to `$3.406B`. This is an expectation-burden screen, not an IRR or mine-life
forecast, and does not include reserve conversion or the settlement ledger.

The [Teck reserve cross-check](capital-flow-wheaton-antamina-teck-reserve-cross-check-2026-09-16.md)
adds an independent joint-venture reserve reference, 2026 life-of-mine-plan
context, an expected mine-life endpoint through `2036`, and the public copy of
the underlying technical report's 2025–2036 mine-plan context. The report also
documents Teck's separate Franco-Nevada silver stream and `29.1 Moz` delivered
through 2024. Its `22.5%`
attributable recoverable-silver denominator is not
interchangeable with the BHP `33.75%` tranche table, and its mine-level schedule
is not an annual BHP payable-silver curve, so Q-02 remains
evidence-insufficient for a reserve-backed delivery curve. The AIF also gives a
useful CA-06 mine-burden reference: Teck's 22.5% share of 2026 Antamina
capital costs is `$215M–$270M`, including `$110M–$135M` sustaining,
`$15M–$20M` growth, and `$90M–$115M` capitalized stripping, alongside
`$255M–$310M` projected cash operating costs. These figures exclude
transportation and royalties and belong to Teck's owner-share perimeter; they
are not assigned to BHP, Wheaton, taxes, debt service, or silver delivery.
Teck also reports `$225M` of proportionate Antamina borrowings and says the
project facilities are non-recourse to Teck and the other sponsors. That makes
mine-level debt visible while keeping sponsor recourse and stream-level debt
allocation separate.
For denominator control, a non-promotable scale sensitivity of Teck's
`31.430 Moz` at 22.5% to `47.145 Moz` at 33.75%, or `42.4305 Moz` after a
mechanical 90% factor, is retained only to show the size of the unjoined
bridge. The Teck recoverable-silver and BHP contained-P&P definitions are not
interchangeable and the sensitivity does not enter the delivery curve.

The new [credit-agreement waterfall boundary](capital-flow-wheaton-antamina-credit-agreement-waterfall-boundary-2026-09-16.md)
adds direct agreement-level Q-03 evidence: named borrowers and lenders,
`$1.5B` facility size, two-year maturity, SOFR-plus-leverage pricing, maturity
repayment, a `0.60:1` capitalization covenant, and a contractual requirement
that all facility proceeds partially finance the Antamina acquisition. Wheaton's
filed Q2 financial statements now separately prove the executed borrowing:
the `$1.5B` Term Loan was drawn on April 1, 2026 and `$1.5B` remained gross
outstanding at June 30. This closes the facility-availability-versus-actual-
draw distinction, but it does not identify the executed designated-payee
instruction, agent-to-seller transfer, Antamina tax or interest, or repayment
waterfall, so financed after-tax return remains unproven.

The February closing announcement also identifies top-level BHP and holding-
company guarantees: parent recourse is capped at the upfront deposit and
reduces after certain ounces are received, while holding-company recourse is
unlimited. This improves the counterparty-credit and recourse map, but does
not prove a guarantee claim, delivered ounces, settlement cash, or an
after-tax return.

The [term-maturity cliff screen](capital-flow-wheaton-antamina-term-maturity-cliff-screen-2026-09-16.md)
keeps the `$1.500B` two-year principal bullet separate from annual interest
expense and shows it at approximately `76.06%` of Q2 gross bank debt. The
financing-flow reconciliation also preserves the announced `$1.9B` cash,
`$1.5B` term-loan, and `$0.9B` revolver composition that sums to the `$4.3B`
PMPA payment. Q2's `$1.972B` gross balance does not identify facility-specific
repayment or seller-account allocation, so this remains a funding-composition
screen rather than funds-flow proof. The same H1 cash-flow statement reports
`$2.700B` drawn, `$728M` repaid, `$5.118M` of debt-issue costs, and `$29.886M`
of interest paid. Those are actual corporate financing observations that
improve the burden screen, but remain unallocated to the PMPA and cannot be
used as asset-level debt service. The companion [maturity-bullet coverage
screen](capital-flow-wheaton-antamina-term-maturity-bullet-coverage-screen-2026-09-16.md)
shows the same principal against the annualized stream operating-cash-flow
proxy under explicit 0%–100% allocation sensitivities; it is an illustrative
terminal-liability screen, not an Antamina repayment forecast.

The debt-envelope comparison is intentionally kept separate from that funding
mix. The announced `$1.5B` term loan plus approximately `$0.9B` revolver implies
approximately `$2.4B` of planned debt funding, whereas the H1 statement reports
`$2.7B` of actual corporate bank debt drawn. The approximately `$0.3B` difference
is unresolved: it is not assigned to the Antamina purchase, another facility,
timing, or a gross-versus-net presentation without a facility-level ledger.
This is a useful control against silently treating a corporate-period debt
movement as the asset-level source of funds.

The [reserve-life denominator boundary](capital-flow-wheaton-antamina-reserve-life-denominator-boundary-2026-09-15.md)
also separates Wheaton's portfolio-wide `23-year` P&P mine-life statistic from
the Antamina-specific reserve context through approximately `2036`. The
portfolio statistic is not allowed to become a BHP-PMPA delivery-tail input.

The [Athene Q2 investment-earnings attribution upgrade](capital-flow-apollo-athene-q2-investment-earnings-attribution-upgrade-2026-09-15.md)
adds a current segment-level bridge: H1 fixed-income and other investment
income of `$7.237B`, alternatives of `$558M`, strategic capital-management fees
of `$73M`, cost of funds of `$5.749B`, and net investment spread of `$2.119B`.
It also records the `$264M` alternative-return delta to management's long-term
assumption. This improves return attribution without proving named-asset
returns or Apollo parent cash.

The Apollo/Athene [related-party return bridge](combined-investment-research-pilot-03-apollo-related-party-return-bridge.md)
now separates exposure, fee expense, period-end fee payable, a named `$8.7B`
ARI-to-Athene commercial-mortgage transfer, insurer-level spread, claimant
distributions, credit-quality signals, and impairment. The evidence rejects the shortcut “Athene fees
equal Apollo cash,” but does not yet prove category-level realized returns or
upstream common-owner cash.

The [Apollo–Athene fee-rollforward boundary](capital-flow-apollo-athene-fee-rollforward-boundary-2026-09-15.md)
adds a qualified mechanical `$779M` management-fee settlement implication from
the opening payable, H1 fee expense, and ending payable. It does not identify
the settlement account, recipient legal entity, intercompany eliminations, or
Apollo common-owner cash.

The [AOP Finance Partners public-source refresh](capital-flow-apollo-athene-aop-finance-public-source-refresh-2026-09-16.md)
adds a historical legal-entity and economic-benefit join for the two AOP
disposal-only candidates. Athene's 2021 Form 10-K identifies AOP as a
consolidated VIE, reports `$747M` of AOP investment-fund assets, and says
Athene received the economic benefits and losses subject to related-party
management and carry economics. The 2025 statutory rows total approximately
`$684.9M` of consideration and `$51.8M` of interest/dividend fields. This is a
stronger Athene economic-perimeter observation, but it does not prove current
ownership, paydown versus sale, settlement, borrower cash, liability-adjusted
return, or Apollo common-owner cash; AOP II remains a separate vehicle.

The [VMC Finance public-source refresh](capital-flow-apollo-athene-vmc-finance-public-source-refresh-2026-09-16.md)
adds a bounded commercial-mortgage route for `91836A-AA-4`, an approximately
`$295.3M` disposal-only Paydown candidate. Public deal data places VMC
2023-PV1 in a Varde-linked CMBS context, and a later SEC CMBS term sheet
references the deal as a previous securitization for a mortgage in a later
pool. This improves issuer and collateral-lineage observability but does not
prove Athene settlement, borrower/property cash, remittance, liability-adjusted
return, or common-owner cash.

The [ATLAS Funding 1 public-source refresh](capital-flow-apollo-athene-atlas-funding-public-source-refresh-2026-09-16.md)
adds an Apollo-backed structured-credit platform route for two disposal-only
redemption candidates, `04941*-AB-0` and `04941*-AD-6`, totaling approximately
`$487.3M` of consideration. Apollo's own disclosures describe ATLAS SP Partners
as a majority-Apollo-owned warehouse-finance and securitized-products business.
The platform join is material, but it does not prove exact issuer ownership by
Athene, settled redemption cash, collateral proceeds, liability-adjusted
return, or Apollo common-owner cash.

The [AP Hansel public-source refresh](capital-flow-apollo-athene-ap-hansel-public-source-refresh-2026-09-16.md)
produces a stronger destination and timing bridge. Aldar's official report
identifies AP Hansel SPV LLC as wholly owned by Apollo Capital Management,
describes a 20-year land-rights structure over `2.6M` square meters, reports
Hansel dividends, and records a February 5, 2025 Class B share repurchase for
`$493.226M`. That timing overlaps the Athene `G2963@-AA-0` disposal window and
the name matches the Apollo-controlled vehicle. It still does not prove exact
CUSIP settlement, Athene allocation, proportional participation, liability-
adjusted return, or Apollo common-owner cash.

The [AA MMF 1 public-source refresh](capital-flow-apollo-athene-aa-mmf1-public-source-refresh-2026-09-16.md)
adds a wrapper-level upgrade for `000249-AA-0`, an approximately `$222.8M`
disposal-only Paydown candidate. Athene regulatory exhibits identify AA MMF 1
Holdco LP and an Apollo Principal Holdings ownership chain, while Apollo's
current 10-K cross-checks the Holdco GP. This strengthens the Apollo wrapper
route, but AA MMF 1 Ltd versus Holdco identity, exact Athene ownership,
settlement, borrower cash, liability-adjusted return, and common-owner cash
remain open.

The [FASST 2022-S5 public-source refresh](capital-flow-apollo-athene-fasst-2022-s5-public-source-refresh-2026-09-16.md)
adds an RMBS issuer and trustee route for `317384-AA-3`, an approximately
`$219.1M` disposal-only Paydown candidate. Public rating material identifies
the FASST 2022-S5 mortgage-backed-note class structure, while U.S. Bank's
reporting portal establishes a controlled trustee-report route. The public
record still does not prove Athene settlement, loan-level mortgage cash,
trustee remittance, liability-adjusted return, or common-owner cash.

The [Apollo Debt Solutions public-source refresh](capital-flow-apollo-athene-apollo-debt-solutions-public-source-refresh-2026-09-16.md)
adds an exact instrument-level route for `03770D-AC-7`. The SEC indenture
confirms CUSIP `03770DAC7`, Apollo Debt Solutions BDC as issuer, a 6.700% coupon,
July 29, 2031 maturity, `$600M` initial principal, and U.S. Bank Trust as
trustee. The Athene `$215.8M` disposal remains a `Various` market-sale
candidate: exact counterparty, settlement, BDC cash, borrower repayment,
liability-adjusted return, and Apollo common-owner cash remain unproven.

The new [Apollo Debt Solutions payment-observability boundary](capital-flow-apollo-athene-apollo-debt-solutions-payment-observability-boundary-2026-09-16.md)
separates the note's contractual January/July payment schedule from an
executed remittance. Third-party statutory holdings make the exact CUSIP
publicly observable, but they are not Athene records and do not identify the
disposal counterparty. No public trustee remittance, Athene custodian
settlement ledger, or note-level payment allocation was located in the checked
perimeter.

The companion [coupon-carry sensitivity](capital-flow-apollo-athene-apollo-debt-solutions-coupon-carry-sensitivity-2026-09-16.md)
shows a par-equivalent gross carry proxy of approximately `$14.461M` annually;
it remains excluded from realized income and owner cash because lot, holding
period, settlement, loss, funding-cost, and liability-cost evidence is absent.

The same issuer bridge now captures `$398.539M` of H1 dividends paid, `$782.527M`
of common-stock issuance proceeds, `$4.715B` of debt issuance proceeds,
`$2.032B` of long-term debt repayments, and `$1.617B` of net financing cash
flow. These are issuer financing movements, not evidence of an Apollo receipt,
Athene allocation, or common-owner residual.
The visible financing components reconcile to `$3.067B` before other uses,
versus `$1.617B` reported net financing cash flow, leaving a `$1.450B`
unattributed financing-use gap. This is preserved as a reconciliation object,
not assigned to Athene or Apollo owners.

The new [issuer cash/return bridge](capital-flow-apollo-athene-apollo-debt-solutions-issuer-cash-return-bridge-2026-09-16.md)
adds Q2 2026 issuer-level facts, including `$312.890M` of H1 cash interest
paid, alongside gross and net investment income, cash, and debt scale. This
improves the funding-burden boundary but does not allocate that cash outflow to
Athene's note or prove a net asset return.

The [named-asset route map](combined-investment-research-pilot-03-apollo-named-asset-return-routes.md)
adds three concrete statutory routes: Concord as a borrower/wrapper/use proxy,
AMAPS 1 as a platform-wrapper/Athene-alignment proxy, and AP Aristotle as a
cash-like statutory candidate after separating its tax-free-exchange row. All
three remain below full remittance, liability-spread, and common-owner-return
proof.

The [Eliant legal-entity bridge](capital-flow-apollo-athene-eliant-legal-entity-bridge-refresh-2026-09-18.md)
adds a separate legal-perimeter upgrade: Apollo's SEC subsidiary exhibit and
Athene's Q3 2025 organizational schedule both list Eliant Invest Holding/GP and
related Apollo Eliant management entities. Athene's exact Eliant CUSIPs carry
cash-like consideration candidates of `$358.252M` and `$189.464M` across
separate tranches. The underlying borrower, event classification, settlement,
remittance, liability spread, and return remain open.
The [public-search boundary](capital-flow-apollo-athene-eliant-public-search-boundary-pass-2-2026-09-18.md)
now records a targeted searched-negative result for the exact CUSIP fragments,
Eliant/Apollo entity names, and public offering, borrower, collateral,
settlement, trustee, custodian, and remittance routes. FINRA BrokerCheck adds
relationship context for Eliant entities but does not provide cash evidence.
Apollo's original Eliant launch announcement adds platform-level context:
Eliant was described as owning inventory, BNP Paribas as providing debt and
receivables financing, Athene as primary capital provider, and Apollo as
investment manager. That explains the expected multi-entity control-point
architecture but does not map either current statutory row to a borrower,
inventory pool, financing draw, payoff, or remittance.
The two statutory consideration fields therefore remain candidates only; the
next useful object is an authorized custody/trustee record or transaction-level
borrower/payoff document.

The [AP Aristotle public-search refresh](capital-flow-apollo-athene-aristotle-public-search-refresh-2026-09-16.md)
now classifies the exact current route as `searched-negative`: public SEC
results found only older AP Aristotle borrower-name analogs, not the Athene
2025 instrument, paydown settlement, or receipt record. Those analogs remain
historical context and are excluded from the current Athene return model.

The [AP Aristotle source-acquisition packet](capital-flow-apollo-athene-aristotle-source-acquisition-packet-pass-1.md)
now turns that bounded result into an executable queue. It separates the
`776.032348M` statutory cash-like candidate from the `6.588486M` tax-free-
exchange hold and names the settlement, `Various`-event classification,
borrower-use, Athene custody/allocation, liability-cost, and return documents
needed for promotion. AP Aristotle remains source-request-ready, not full cash
proof.

The KKR comparison's [private-marker issuer-resolution pass](capital-flow-kkr-global-atlantic-accordia-private-marker-issuer-resolution-pass-1.md)
now resolves the highest-interest private-marker row at source-text level:
CUSIP `90231*-AA-0` is labeled `2023 Bear Financing L.P.` on Schedule D page
`240`, with `$202.125M` of book value and `$17.419245M` of statutory interest
received. This improves issuer targeting, but does not prove the full legal
instrument, borrower use, settlement, liability-cost spread, or return.

The [insurance named-asset proof ladder](combined-investment-research-insurance-named-asset-proof-ladder-2026-09-17.md)
now compares the strongest Apollo/Athene and Accordia rows on one surface.
Apollo/Athene has the larger named-proceeds and wrapper candidates; Accordia
has the cleaner coordinate-reconciled owned-bond income and disposal columns.
The ladder explicitly blocks income-to-cash, consideration-to-settlement,
gain/loss-to-return, and wrapper-to-borrower overclaims.

The [Bear Financing source-acquisition packet](capital-flow-kkr-global-atlantic-accordia-bear-financing-source-acquisition-packet-pass-1.md)
now turns Accordia's source-visible `2023 Bear Financing L.P.` row into a
document-level request. It preserves the `$17.419245M` statutory interest as an
income proxy and names the custody, borrower-use, event-history, liability-cost,
and residual-return records needed before promotion.

The [Bear Financing public credit-agreement refresh](capital-flow-kkr-global-atlantic-bear-financing-public-credit-agreement-refresh-2026-09-17.md)
adds a primary-filed January 5, 2024 `$245M` senior-loan commitment and a
two-entity KKR affiliate perimeter. The matching FY2024 Schedule D row and
later FY2025 row improve instrument and period continuity, but draw, borrower
use, cash settlement, liability cost, and return remain open.

The [FY2025 continuity refresh](capital-flow-kkr-global-atlantic-bear-financing-fy2025-continuity-refresh-2026-09-17.md)
now sets the two-period control explicitly: book value remains `$202.125M`,
while fair value, effective rate, and interest received change. The increase
from `$11.604153M` to `$17.419245M` is retained as statutory income evidence,
not promoted to a loan-level cash settlement or realized return.

The [Q2 2026 schedule boundary](capital-flow-kkr-global-atlantic-bear-financing-q2-2026-schedule-boundary-2026-09-17.md)
checks the latest official Accordia verification document and the KKR parent
Q2 2026 Form 10-Q. Accordia reports the aggregate bond base but omits the
detailed Bear Financing CUSIP; KKR reports aggregate Global Atlantic investment
commitments but no Bear-specific draw, repayment, or cash waterfall. FY2025
remains the latest full row-level point; no disposal or repayment is inferred.

The [private-credit borrower proof ladder](combined-investment-research-private-credit-borrower-proof-ladder-2026-09-17.md)
now connects Bear Financing's statutory ownership, Concord's borrower/wrapper
route, and Ares/Frontline's acquisition-facility role. It shows that the three
routes start from different sides of the capital-flow graph and all still lack
the lender-allocation, settlement, debt-service, and liability-adjusted-return
join.

The [Ares/Frontline primary-source refresh](capital-flow-ares-frontline-primary-source-refresh-2026-09-17.md)
now dates the route with Ares' Q1 2025 acquisition-facility release, Q2 2026
continued-growth release, and an SEC-filed Frontline II instrument marker. This
strengthens borrower-purpose and instrument observability, but not Ares-funded
allocation, closing cash, debt service, repayment, or lender return.

The statutory cash-like column review separately resolves two sparse Athene
same-CUSIP rows: `$269.806570M` of interpreted consideration and `$4.029889M`
of interpreted interest/dividends. These fields strengthen named statutory
proceeds evidence, but blank gain/loss fields, borrower receipt, custodian
allocation, liability spread, and final return remain unresolved.

The [same-CUSIP statutory bridge upgrade](capital-flow-apollo-athene-statutory-same-cusip-bridge-upgrade-2026-09-15.md)
now makes the page-level route explicit for AMAPS 1 CUSIP `02300A-AA-8` and
Concord CUSIP `20633K-AN-8`: each has a year-end holding row and a dated
Schedule D consideration row in the same Athene statutory source. This is a
stronger legal-entity route than a generic wrapper map, but it remains below
settlement receipt, borrower-use, liability-cost, and final-return proof.
The AMAPS disposal row is specifically dated `10/24/2025`, names `Apollo
Capital Markets Partner`, and shows `$268M` of consideration plus `$3.987M` of
disposal interest/dividends. Those are named statutory counterparty and
consideration fields, not proof of settled bank cash, liability release, or
Apollo common-owner cash; the [AMAPS named-cash ledger](data/capital-flow-apollo-athene-amaps-named-cash-source-acquisition-pass-1.csv)
and [corrected-row confirmation](capital-flow-apollo-athene-same-cusip-corrected-row-confirmation-2026-09-15.md)
preserve that boundary.

The Q2 2026 AAIA statement adds a same-CUSIP continuity point: Schedule D Part
3, PDF page `2470`, records `02300A-AA-8` acquired on `06/23/2026` from
`ALRe Corporate AAM` for `$120.700M` actual cost and par value, plus
`$2.661M` paid for accrued interest/dividends. This strengthens the current
Athene legal-entity and affiliated-counterparty chronology, but remains an
acquisition/continuity candidate rather than settled cash, custody transfer,
collateral receipt, or AMAPS return proof.

The corrected same-CUSIP row-proof packet expands the named statutory proceeds
screen to ten routes: `$2.943066208B` selected disposal consideration,
`$2.930192972B` classified cash-like, and `$93.704267M` of selected disposal
interest/dividends. Mixed transfer rows remain held apart. These are Schedule D
row-level observations, not bank receipts, borrower repayment, liability-cost
adjusted return, or Apollo parent cash.

The [Concord 2022-1 public-source refresh](capital-flow-apollo-athene-concord-2022-1-public-source-refresh-2026-09-16.md)
adds a separate Q-08 route for the `$624.9M` disposal-only `20633K-AA-6`
candidate. Concord's official announcement supplies the music-rights ABS,
more-than-one-million-copyright collateral, and acquisition-financing context;
independent insurer statements cross-check the exact TUNES 2022-1A identifier.
This improves issuer observability but does not prove Athene ownership,
settlement cash, royalty remittance, or realized return.

The [AA Infrastructure Fund 2 public-source refresh](capital-flow-apollo-athene-aa-infrastructure-public-source-refresh-2026-09-16.md)
adds a historical Athene Annuity and Life Company observation for the
`00024D-AL-7` route: AA Infrastructure Fund 2 LLC was listed at `$762.348M`
and `0.3%` of admitted assets at December 31, 2024, with a related depositor
entity also named. This improves wrapper observability but does not prove
current Athene ownership, project cash, settlement, or Apollo return.

The [PK AirFinance public-source refresh](capital-flow-apollo-athene-pk-airfinance-public-source-refresh-2026-09-16.md)
adds a stronger Apollo/Athene platform join for the PK AirFinance statutory
rows. Apollo's acquisition announcement separates platform ownership from
Athene's acquisition of the existing loan portfolio, while PK's official
website supplies aircraft/engine collateral, portfolio-scale, and ABS context.
This improves the economic destination map for the approximately `$497.7M`,
`$434.2M`, and `$256.0M` PAF 2020 candidates, but does not prove exact-CUSIP
settlement, borrower repayment, remittance, liability-adjusted return, or
Apollo common-owner cash.

The [AOP Finance Partners public-source refresh](capital-flow-apollo-athene-aop-finance-public-source-refresh-2026-09-16.md)
adds a historical legal-entity and economic-benefit join for the two AOP
disposal-only candidates. Athene's 2021 Form 10-K identifies AOP as a
consolidated VIE, reports `$747M` of AOP investment-fund assets, and says
Athene received the economic benefits and losses subject to related-party
management and carry economics. The 2025 statutory rows total approximately
`$684.9M` of consideration and `$51.8M` of interest/dividend fields. This is a
stronger Athene economic-perimeter observation, but it does not prove current
ownership, paydown versus sale, settlement, borrower cash, liability-adjusted
return, or Apollo common-owner cash; AOP II remains a separate vehicle.

The [statutory parent-affiliate boundary upgrade](capital-flow-apollo-athene-statutory-parent-affiliate-boundary-upgrade-2026-09-15.md)
adds Athene's FY2025 `$4.553M` related-party receivable, `$142.863M` related-
party payable, `$11.331B` aggregate other-cash line, and `$415.722M`
intercompany tax settlement. These are legal-entity boundary facts, not an
Apollo receipt; the statement still lacks a dated parent-only cash entry.

The [Q2 share-claim and dilution boundary upgrade](capital-flow-apollo-q2-share-claim-dilution-boundary-upgrade-2026-09-15.md)
adds Apollo's Q2 2026 `575.972M` GAAP common shares, `14.588M` mandatory-
convertible preferred underlying shares, `17.073M` vested RSUs, `15.922M`
unvested RSUs eligible for dividend equivalents, and `623.554M` adjusted net-
income shares. The `47.583M` mechanical gap is a per-share claim screen, not
proof of HoldCo cash or an instrument-specific economic dilution forecast.

The [FY2025 parent dividend-receipt upgrade](capital-flow-apollo-fy2025-parent-dividend-receipt-upgrade-2026-09-15.md)
adds a parent-company XBRL receipt: `$750M` of proceeds from dividends received
matches `$750M` of subsidiary-investing-distribution proceeds in the explicit
`ParentCompanyMember` context. This is now parent-only receipt evidence, but it
does not identify Athene as the payer, the transfer date or receiving account,
or the amount available to Apollo common owners.

The [parent-receipt attribution frontier](capital-flow-apollo-athene-parent-receipt-attribution-frontier-2026-09-15.md)
now shows the mechanical `$0M`–`$750M` range produced by 0%–100% Athene
attribution of that parent receipt. The range is a sensitivity control only:
Athene payer identity, transfer timing, receiving account, intercompany
elimination, regulatory availability, and the final common-owner residual are
still unproven.

The [Athene/ADIP related-party flow upgrade](capital-flow-apollo-fy2025-athene-adip-related-party-flow-upgrade-2026-09-15.md)
adds the FY2025 table's `$466M` of contributions from ADIP and `$444M` of
distributions to ADIP. The XBRL context identifies Athene and Apollo Athene
Dedicated Investment Programs, but the distribution is not labeled as an AGM
receipt and cannot be netted into common-owner cash.

The [Q2 ACRA/ADIP flow upgrade](capital-flow-apollo-athene-q2-adip-related-party-flow-upgrade-2026-09-15.md)
extends that route into the current period: Q2 shows `$145M` of contributions
from ADIP and `$47M` of distributions to ADIP; H1 shows `$271M` and `$301M`,
respectively. These are named current-period related-party flows, not AGM
receipts. They cannot be added to Athene's direct-parent distribution or
Apollo's consolidated cash without a dated settlement, receiving-account, and
intercompany-elimination bridge.

The retail attached-service layer now carries direct filing routes in its
structured boundary: Target advertising, card profit sharing, and other
revenue, plus Walmart U.S., International, and Sam's Club membership and other
income. The [attached-services boundary](combined-investment-research-pilot-02-retail-attached-services-boundary.md)
keeps the amounts as control-point evidence and excludes them from normalized
owner cash until cost, capital, working-capital, tax, and collection records
are allocated.

The ARI buyer-side transaction layer now carries a structured [transaction-
terms boundary](capital-flow-apollo-athene-ari-transaction-cash-consideration-boundary-2026-09-15.md):
the 99.7% commitment-based pricing rule, asset-specific CECL netting, the
$146M pre-closing repayment perimeter, and no financing contingency are
source-backed. The final settlement account, borrower collections, and
Athene-to-Apollo cash route remain separate open tests.

The companion [closing-payment mechanics boundary](capital-flow-apollo-athene-ari-closing-payment-mechanics-boundary-2026-09-16.md)
now identifies the decisive objects in that open test: the Closing Date
Calculation Notice, seller-designated account(s), payoff-recipient wires,
approved settlement statement, 120-day final accounting and true-up, any
designated buyer affiliate, and borrower notices directing post-transfer debt
service to Buyer or its designee. These contractual mechanics sharpen the
collection route but do not substitute for executed settlement, bank, borrower,
or liability-cost evidence.

The [post-close proof search boundary](capital-flow-apollo-athene-ari-post-close-proof-search-boundary-2026-09-16.md)
records the result of searching the bounded ARI, Apollo, Athene, agreement, and
proxy perimeter: the executed settlement statement, wire confirmations,
true-up, named designee, and borrower receipt ledger were not found in the
public post-close materials checked. This is `searched-negative` for that
public perimeter, not evidence that private closing or servicing records do
not exist.

The [named-issuer source-acquisition boundary](capital-flow-apollo-athene-named-issuer-source-acquisition-2026-09-16.md)
now preserves Apollo AMAPS, Concord music-rights ABS, and MF1 servicing/data-
procedures artifacts tied to same-CUSIP routes. For MF1, the [remittance-access
boundary](capital-flow-apollo-athene-mf1-remittance-access-boundary-2026-09-16.md)
records CTSLink CREFC and restricted-servicer reports as a located but
sign-in-gated route. These artifacts improve issuer, collateral, and servicing
context; they do not prove Athene-specific remittance, borrower cash, or
liability-adjusted return.
The Q2 2026 AAIA Schedule D scan adds current named-asset controls: Atlas A
`04940#-AA-9` and Atlas B `04940#-AB-7` show `04/23/2026` redemptions totaling
`$970.000M` of consideration, while MF1 2025-B2 A `592918-AA-4` has both a
`06/23/2026` acquisition row and a separate `06/12/2026` disposal row. AMAPS 1
also has a current `06/23/2026` acquisition row. These are legal-entity
statutory proceeds/acquisition candidates and continuity controls, not trustee
remittance, bank settlement, liability-cost, or return proof. See the [Q-12
named-asset source package](capital-flow-insurance-q12-next-source-package-2026-09-18.md).
The bounded public settlement recheck for both Atlas identifiers, the
`04/23/2026` date, and the combined `$970.000M` amount found no matching
issuer, trustee, paying-agent, counterparty, bank/remittance, or holder-side
settlement record. Keep the paired redemption as a high-quality dated
statutory disposition candidate, not Athene cash received or common-owner
cash.

The [cash-perimeter delta boundary](capital-flow-apollo-athene-ari-cash-perimeter-delta-boundary-2026-09-16.md)
also isolates the approximately `$897.267M` mechanical difference between
ARI's approximately `$8.6B` sale consideration and its `$9.497267B`
commercial-mortgage repayment/sale-proceeds line. The filing also identifies a
`$46M` Chicago hotel loan that repaid after closing, reinforcing that the cash-
flow category is not a clean closing-wire measure. The difference is explicitly
unallocated; it is not treated as accrued interest, borrower repayment, fee,
true-up, Athene funding, or Apollo cash.

Athene's Q2 earnings release adds a buyer-management cross-check: `$7.8B` of
2Q'26 and LTM AUM outflows are identified as related to ARI after the portfolio
sale, while `$5.0B` of Intel prepayment outflows are separately identified. The
[AUM outflow boundary](capital-flow-apollo-athene-ari-aum-outflow-boundary-2026-09-16.md)
keeps this as an AUM classification, not a purchase-price wire, borrower
repayment, cash receipt, or asset-level return.

The [ARI liquidation-distribution boundary](capital-flow-apollo-athene-ari-liquidation-distribution-boundary-2026-09-16.md)
adds a separate seller/common-owner residual estimate of `$7.75–$8.50` per
fully diluted share, excluding the `$3.75` July dividend. Because the range is
unaudited, forward-looking, and dependent on asset sales, expenses, taxes,
reserves, and timing, it is not treated as observed cash or as Athene/Apollo
parent receipt.

The 2026-09-17 SEC-source recheck confirms that the ARI dissolution vote remains
scheduled for September 29, 2026 and that the `$7.75–$8.50` range is still
conditional. The post-vote test is approval, revised reserves, initial
distribution, and any Apollo/Athene allocation; the estimate remains outside
observed cash.

The refreshed [Apollo–Athene Q2 parent-receipt boundary](capital-flow-apollo-athene-q2-parent-receipt-refresh-2026-09-16.md)
adds a lower-tier legal-availability test: AHL identifies subsidiary
dividends, capital-market issuance, and intercompany borrowing as its primary
cash sources, while stating that it does not currently plan for U.S. insurance
subsidiaries to pay dividends to their parents. Bermuda subsidiary
distributions remain subject to statutory, regulatory, surplus, and
financial-strength-rating constraints. This narrows the possible upstream
route into AHL, but it neither attributes the `$110M` H1 AHL distribution to a
specific subsidiary nor proves an AGM receipt, unrestricted HoldCo cash, or a
common-owner residual. The Apollo Q2 route was rechecked against the official
SEC filing as well as the IR mirror; the result remains searched-negative for
an AGM-only receiving account or parent-only cash-flow line. Athene's current
cash-flow statement separately reports `$42M` of capital contributions from
parent; that is parent-to-Athene financing, not an Athene-to-AGM receipt, and
does not join to the `$32M` Q2/`$110M` H1 distribution observation.

An August 11, 2026 Athene Form 8-K adds a dated public-source boundary: it
announces an “Overview of Athene's Corporate Structure” presentation but does
not furnish the slide contents, a distribution schedule, a receiving account,
or an Athene-to-AGM receipt. This narrows the next Q-07 acquisition request
without promoting presentation availability into common-owner cash.

The companion [Athene corporate-structure presentation boundary](capital-flow-apollo-athene-corporate-structure-presentation-boundary-2026-09-16.md)
adds official summary context of more than `$470B` of assets, `$37B` of
regulatory capital, `$79B` of available liquidity, and `$6.1B` of deployable
capital as of June 30, 2026. It also records the access-controlled May asset
portfolio and affiliated/related-party presentations as named Q-08 routes.
These figures and routes improve entity-capital context but do not prove AGM
receipt, asset-level settlement, or common-owner residual.

The [intercompany note longitudinal refresh](capital-flow-apollo-athene-intercompany-note-longitudinal-refresh-2026-09-16.md)
upgrades Q-07's direct AHL-to-AGM route from a two-date observation to a
seven-date public balance history: the AHL receivable rises from `$78M` at
December 31, 2022 to `$279M` at June 30, 2026, within a disclosed `$500M`
facility. This confirms recurring direction and continuity, but balance
movements are not dated cash draws; use of proceeds, repayment, intercompany
elimination, AGM receipt, dividend funding, and common-owner residual remain
unproven.

The new [Athene 2026 credit-agreement purpose and entity-perimeter pass](capital-flow-apollo-athene-2026-credit-agreement-purpose-perimeter-2026-09-17.md)
adds a dated primary-filed facility control: Athene's named borrowers, `$1.750B`
of aggregate commitments, permitted working-capital/corporate-purpose language,
affiliate and intercompany permissions, and consolidated covenant limits are
visible. The Q2 filing also states that no amounts were outstanding under the
current or previous external credit facilities at June 30, 2026. This closes
the external revolving-facility draw hypothesis at that date, but it does not
close the separate AHL-to-AGM note, a bank receipt, use-of-proceeds allocation,
intercompany elimination, or common-owner cash. The structured seven-row
perimeter is now enforced by the pilot verifier.

The apparent `$279M`/`$280M` presentation issue is date-controlled rather
than a same-date conflict: `$280M` is the March 31, 2026 AHL note-receivable
balance and `$279M` is the June 30, 2026 balance. The `$1M` sequential change
is retained as a period-end balance movement, not dated cash principal,
repayment, or AGM receipt evidence.
Apollo's FY2025 parent-only Schedule I independently corroborates the
December 31, 2025 direction and amount: AGM reported no note receivable from
AHL and a `$227M` note payable to AHL, matching AHL's `$227M` receivable. This
is a stronger two-sided balance control, but it still does not establish a
draw date, bank settlement, use of proceeds, elimination, or common-owner cash.

The Apollo Q2 2026 10-Q and financial supplement were checked for the June 30
parent-side payable and do not expose a separately identified AGM-to-AHL note
line or receiving account. Accordingly, the `$279M` June 30 amount remains an
Athene-side observation rather than a new two-sided Q2 control; December 2025
is the latest public cross-entity corroboration.

The current [AMAPS 1 exposure boundary](capital-flow-apollo-athene-q2-amaps-current-exposure-boundary-2026-09-16.md)
also adds a scale orientation: the `$2.544B` Q2 exposure is approximately
`0.810%` of Athene's `$314.090B` net invested assets and `5.782%` of the
filing's `$44.0B` look-through related-party investment population. These
ratios improve concentration framing only; they do not allocate ownership,
liability cost, borrower cash, or Apollo return.

The Q2 exposure can now refresh the named-route liability-cost screen: applying
the current `$2.544B` AMAPS denominator to the reconciled `$158.852B` bond base
and H1 `$5.749B` Athene cost-of-funds pool produces an approximately `$92.1M`
mechanical allocation. This is a period-fresh sensitivity, not observed AMAPS
funding cost or return; settlement, duration, policyholder crediting, hedges,
and custodian evidence remain absent.
Apollo's public AMAPS product description adds format-level mechanics—roughly
`5-year` note term, approximately `85%` investment-grade-rated notes, tranche-
specific CUSIPs, and daily secondary-market pricing/trading. These sharpen the
controlled request for an exact AMAPS 1 trade, custodian settlement, and trustee
waterfall, but do not establish that CUSIP `02300A-AA-8` followed those terms
or that Athene received the `$268M` statutory consideration.

The remaining Q-10 gap is now operationalized in the [through-cycle causal-test
protocol](combined-investment-research-through-cycle-causal-test-protocol-2026-09-16.md).
It specifies the observable metrics, principal confounds, promotion threshold,
and filing-based breaker for retail affordability, Wheaton delivery/financing,
and Apollo–Athene spread/liquidity transmission. The protocol is
`evidence-insufficient` until repeated period-matched observations and the
required entity-level cash joins are available.

The current-regime inputs were refreshed through the September 16 FOMC
decision (`3.75%–4.00%` federal-funds target), August CPI (`3.4%` headline,
`2.4%` core, `16.3%` energy), and July personal-income/outlays (`0.5%`
disposable-income growth, `0.2%` PCE growth, `3.0%` saving rate). These are
useful dated stress markers for financing, affordability, energy, and liquidity;
they do not convert the existing descriptive panel into through-cycle causal
proof.

The first bounded Q-10 retail panel diagnostic now compares the 18 existing
company-period rows across positive versus negative real hourly earnings and
higher versus lower CPI. The pooled descriptive splits are directionally mixed
and materially confounded by Walmart scale, fiscal overlap, capex, inventory,
vendor terms, and temporary support. This adds a quantitative checkpoint but
does not promote the mechanism to causal or normalized-owner-cash proof.

The follow-on within-company diagnostic removes pooled company scale: among 12
transitions with changing real hourly earnings, 6 cash-screen changes move in
the same direction and 6 move in the opposite direction. This is a stronger
falsifier surface than pooled averages, but it still does not control fiscal
overlap, capex, inventory, vendor terms, support, or store actions.

The `6/6` result is a separate contemporaneous within-company diagnostic from
the lagged `7/8` result below; the figures must not be combined into one sample
or treated as competing versions of the same test.

The lagged Q-10 retail diagnostic also fails to show a stable lead: prior
real-wage conditions agree with the next cash-screen direction in 7 of 15
usable transitions and disagree in 8. This is a useful falsifier for a simple
affordability-to-cash story, not a causal estimate.

The [cross-pilot thesis-breaker register](combined-investment-research-thesis-breaker-register.md)
now turns the prose falsifiers into nine reproducible tests: three for
Wheaton–Antamina delivery and financed return, three for retail demand,
margin, and reinvestment durability, and three for Apollo–Athene access,
credit, and named-asset performance. All remain `active-qualified` until the
next filing or source-backed test is run.

## Decision layer: what the evidence supports today

The [cross-sector comparison](combined-investment-research-cross-sector-comparison-2026-09-16.md)
puts the three pilots on the same decision vocabulary—control point, payer,
burden carrier, owner-cash denominator, valuation object, and falsifier—while
preserving their different economic mechanisms.

The evidence supports a ranked research posture, not a single cross-sector
buy recommendation:

| Case | Current decision posture | Why it is interesting | What prevents promotion |
| --- | --- | --- | --- |
| Wheaton–Antamina | `strongest named-asset proxy; return unproven` | A named `$4.300B` cash deployment, contractual silver entitlement, first BHP-PMPA delivery, combined cumulative cash-back evidence, and an identifiable threshold mechanism are all visible | BHP-only settlement quantity, reserve-backed delivery curve, Antamina tax/interest allocation, and financed IRR/NPV |
| TJX / Target / Walmart | `cohort signal; no normalized ranking` | Affordability and substitution signals connect to observed comparable sales, attached-service activity, operating cash, property spending, and explicit burden screens | Maintenance-capital split, working-capital normalization, service-level cash conversion, leases, taxes, dilution, and support removal |
| Apollo–Athene | `platform and wrapper map; common cash unproven` | Origination, fee, spread, statutory asset, related-party, ARI buyer/seller, credit, and parent-receipt routes are unusually visible as separate layers | Athene-to-AGM receipt attribution, borrower collections, liability-cost-adjusted asset returns, regulated capital, and common-owner residual |

The correct conclusion is therefore conditional: the system has identified
where the economics may concentrate and has quantified several expectation
burdens, but it has not earned a fully normalized owner-cash ranking. A reader
should use the valuation workbenches to ask what must be true, then use the
queue and thesis-breaker register to decide whether the next filing confirms or
weakens that condition.

The [public-evidence decision surface](combined-investment-research-cross-sector-comparison-2026-09-16.md#public-evidence-decision-surface-what-we-can-use-now)
is the move-on handoff. It preserves the evidence boundary while making the
three pilots useful for broader work: Wheaton as the named-asset contract
method, retail as the through-cycle quality and cash screen, and Apollo as the
legal-entity and parent-attribution method. The unresolved bridges remain
promotion gates and thesis breakers; they are not prerequisites for applying
the framework to the next candidate set.

The [next-cycle candidate expansion](combined-investment-research-next-cycle-candidate-expansion-2026-09-16.md)
sets that candidate set: power-grid customer cash, insurance statutory
named-asset income, and asset-backed collateral/borrowing-base proof. The
selection is based on public evidence-chain quality and method coverage, not
on a return ranking. Each lane inherits the same quality-of-earnings,
owner-cash, valuation, liquidity, and falsifier controls.

The [next-evidence queue](combined-investment-research-next-evidence-queue.md)
now carries the three expansion tests as Q-11 through Q-13: FPL category
receipts, insurance named-asset remittance and liability-cost attribution, and
URI certificate-grade collateral and fleet return. Their current classes are
searched-negative for the FPL category-cash field and evidence-insufficient for
the insurance and URI bridges. This makes the move-on work operational without
changing the qualified status of the underlying claims.

The first next-cycle public-source refresh strengthens Q-11 without
overpromoting it: official Florida PSC filings confirm FPL's continuing
Distribution Inspection program, rate-class allocation methodology, 2026 bill
period, and 2027 actual-cost true-up route. The later Form 6P reports 180,000
poles and $92.1M of 2026 actual/estimated program cost as of February 2026,
with a $94.1M 2027 projection. They still do not disclose
Distribution Inspection-specific customer receipts or source-of-funds
allocation. See the [official PSC source refresh](capital-flow-fpl-distribution-inspection-official-psc-source-refresh-2026-09-16.md);
the lane remains `hold-with-strong-route-visible`.

The AEP/Duke comparison now adds a second public-source control to Q-11's
power-grid lane. AEP's Q2 Form 10-Q reports approximately `45 GW` of AEP Texas
incremental-load letters of agreement, including approximately `40 GW` of
prospective ERCOT Batch Zero load, and approximately `$2B` of financial
security in cash collateral, guarantees, and letters of credit for that
prospective tranche. The same filing leaves load ramp, interconnection,
transmission upgrades, and cost responsibility subject to ERCOT/PUCT action.
Duke's Q2 Form 10-Q separately describes financial protections in data-center
service agreements intended to align incremental service costs with the
customers driving them. The [AEP/Duke customer-security and QoE bridge](capital-flow-aep-duke-large-load-customer-security-quality-bridge-2026-09-16.md)
therefore improves the status ladder and customer-burden test, but does not
promote collateral or guarantees to revenue, unrestricted cash, approved rate
base, or owner cash.

The Duke Anderson project boundary has since moved beyond approval language.
The full South Carolina PSC Order `2026-244` is now located and grants the
certificate subject to required federal, state, and local permits,
consultations, and certifications. That closes the “full order located” gate,
but not the economics.
South Carolina ORS/E3 monitoring reports identify a current estimated project
budget of `$3.2B`, a limited notice to proceed, initial engineering, major
power-island equipment procurement, Q2 2027 site mobilization, and an August
report in which Duke stated the project was on budget with no contingency used
to date. These are execution and denominator observations, not audited cash
spend, rate-base recovery, billed revenue, or owner return. The [updated
Anderson approval-to-cash boundary](capital-flow-duke-anderson-county-generation-approval-recovery-boundary-2026-09-16.md)
records the monitoring evidence, the final-order `$3.218B` current cost
estimate, and the interim `100% DEC costs` attribution before co-op
negotiations were finalized; it preserves the remaining final-agreement,
rate-base, billing, and cash gates. A new [project cost attribution
sensitivity](capital-flow-duke-anderson-project-cost-attribution-sensitivity-2026-09-17.md)
shows the mechanical `$2.758286B` DEC/Duke share alongside the NCEMC and
Central sensitivities, while explicitly withholding it from owner cash and
valuation.

The first Q-12 public wrapper refresh also strengthens the insurance lane
without overpromoting it: an SEC-filed MF1 2025-B2 agreed-upon-procedures
report identifies 23 collateral interests, 74 related mortgaged properties,
and Atlas SP Securities/Apollo Global Securities among the specified parties.
The related public servicing exhibit is labeled MF1 2026-FL21, not MF1 2025-B2;
that series mismatch is now an explicit crosswalk gate. The route remains an
Apollo-affiliated wrapper and collateral path, not proof of Athene ownership,
remittance, liability-adjusted return, or common-owner cash.
See the [MF1 SEC document refresh](capital-flow-apollo-athene-mf1-public-sec-document-refresh-2026-09-16.md).

The [Accordia matched-disposal proof packet](capital-flow-kkr-global-atlantic-accordia-matched-disposal-owned-interest-proof-packet-pass-1.md)
now joins three coordinate-extracted disposal rows back to Accordia owned-bond
interest rows: Intel, Commonwealth Edison, and Orange. The rows carry
`$1.553M` of statutory consideration, `$(0.202M)` of realized gain/loss, and
`$29K` of disposal-row interest/dividends. This is a stronger legal-entity
proceeds proxy, not settlement cash, borrower use, liability-adjusted return,
or KKR common-owner cash.

The first Q-13 public operating refresh also strengthens the asset-backed lane:
URI's Q2 2026 SEC results report $2.999B total liquidity, $3.305B year-to-date
operating cash flow, $2.720B gross rental-equipment purchases, $330M used-
equipment proceeds, and a 52.9% OEC recovery rate. These improve the fleet
cash-conversion proxy, but total liquidity is not a populated borrowing-base
certificate and the lifecycle return remains unproven. See the [URI collateral
proof chase](capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.md).

The new [URI reporting-regime boundary](capital-flow-uri-abl-borrowing-base-reporting-regime-boundary-2026-09-16.md)
adds a sharper legal-control route: quarterly certificates are required, monthly
certificates can be triggered below 65% of maximum revolver capacity, and the
agreement records a May 31, 2025 certificate delivered to lenders plus a
`$1.000B` minimum closing Combined Availability. URI's June 30, 2026 filing
also reports `$2.802B` ABL capacity net of letters of credit and `$1.666B`
outstanding. These facts narrow the missing document request but still do not
expose collateral components, NOLV, reserves, or live Combined Availability.

The [URI collateral-eligibility bridge](capital-flow-uri-abl-collateral-eligibility-bridge-2026-09-17.md)
now makes the missing denominator explicit: the ABL agreement filters rental
equipment through eligibility, lien, location, representation, and regulatory
tests before applying NBV/NOLV and reserves. It also documents the U.S./Canadian
borrowing-base formula, agent-adjustment rights, certificate cadence, and the
`$1.000B` closing-availability condition. The Q2 capacity and debt figures are
therefore useful liquidity observations, not collateral value or a lifecycle
return; populated certificates, NOLV, reserves, and source-to-purchase use
remain unproven.
The new [URI H1 cash-to-claims bridge](capital-flow-uri-h1-2026-cash-claim-bridge-pass-1.md)
consolidates the disclosed `$3.305B` H1 operating cash flow, fleet and
non-fleet reinvestment, resale proceeds, acquisitions, repurchases, and
dividends. The mechanical residual after those listed sources and uses is
`$(356M)`. This is a diagnostic cash-use result, not normalized owner cash:
replacement versus growth, fleet-cohort return, ABL draw allocation, and
URNA-to-parent transfer remain unresolved.

### Next-cycle decision surface

| Queue | Current public proof | Current grade | Next document that could change the grade | Stop rule |
| --- | --- | --- | --- | --- |
| Q-11 FPL | Program cost/activity, rate-class recovery method, bill period, and true-up route | `hold-with-strong-route-visible` | Non-confidential rate-class billing/collection workpapers and the final 2026 true-up | Do not call aggregate SPP revenue or utility OCF Distribution Inspection cash |
| Q-12 MF1 / Apollo-Athene | Named wrapper, Apollo-affiliated transaction participant, collateral count, and property count | `evidence-insufficient` | Athene lot/custodian record plus offering, trustee remittance, and liability-cost schedules | Do not call an Apollo-affiliated wrapper an Athene receipt or common-owner return |
| Q-13 URI | Period-matched liquidity, OCF, fleet purchases, used-equipment proceeds, and OEC recovery | `evidence-insufficient` | Populated borrowing-base certificate, eligibility/NOLV/reserve schedule, and source-to-purchase records | Do not call facility capacity or fleet resale recovery a lifecycle return |

The next-cycle work is therefore sequenced by evidence quality: pursue the
FPL collection workpapers if they become public, pursue the Athene lot and
trustee join for MF1, and pursue URI's certificate-grade collateral package.
If those documents remain unavailable, the current public-only system is
already sufficient to move on to new candidates without upgrading any of the
three lanes beyond their stated grades.

## Falsifier-first handoff

The next decision-changing observations are explicit:

1. **Wheaton:** a BHP-only metal-credit ledger that fails to reconcile to the
   contract's payable factor, or a delivery curve that cannot support the
   upfront payment after tax and financing, breaks the named-asset return
   thesis.
2. **Retail:** comparable-sales strength accompanied by margin compression,
   inventory/payable deterioration, support reversal, or maintenance capital
   that exhausts cash-after-property breaks the affordability-to-owner-cash
   thesis.
3. **Apollo–Athene:** credit losses, funding stress, statutory restrictions,
   or inability to trace Athene/fee cash into an unrestricted HoldCo residual
   breaks the origination-to-common-owner thesis.

These are measurable filing tests rather than narrative objections. Until one
of the decisive bridges is completed, the appropriate output is a qualified
research conclusion with a visible evidence boundary.

The [completion audit](combined-investment-research-completion-audit.md) now
maps all 13 goal requirements to authoritative artifacts, statuses, remaining
gaps, and verification methods. It explicitly keeps the project incomplete
until delivery-level cash, normalized owner cash, related-party returns, and
common-owner access are source-backed.

The [Q2 parent-cash perimeter reconciliation](capital-flow-apollo-athene-q2-parent-cash-perimeter-reconciliation-2026-09-16.md)
adds a denominator control for Q-07. It keeps `$25.4B` consolidated
unrestricted cash, `$3.412B` HoldCo and Asset Management cash, `$3.415B` Asset
Management segment cash, the `$110M` H1 Athene distribution, and the `$279M`
AHL note receivable balance in separate scopes. These surfaces are
non-additive; parent receipt, legal availability, liability cost, and the
common-owner residual remain unproven.

The [BHP upfront-settlement bridge](capital-flow-wheaton-antamina-bhp-upfront-settlement-bridge-2026-09-16.md)
upgrades one narrow part of the Wheaton case: Wheaton's `$4.300B` named
Antamina payment and BHP's reported `$4.3B` receipt on April 2, 2026 are now
connected as a contemporaneous amount-and-date source/use observation. This
does not turn into a bank-wire match or an operating metal-credit receipt; the
BHP-PMPA ounce, invoice, collection, and stream-level return remain open.

The BHP recipient-side boundary now also includes a mechanical FY2026
financing-flow control: reported net financing cash flow of `$(3.280B)` can be
reconciled to non-stream financing lines of `$(7.539B)`, the `$4.300B` stream
receipt, and the `$(41M)` stream settlement. This improves arithmetic control
over the source/use question but does not attribute the receipt to debt,
dividends, capex, retained liquidity, or Antamina reinvestment; a treasury or
board allocation record is still required.

The FPL Q-11 lane now also has a [historical recovery-boundary pass](capital-flow-fpl-sppcrc-historical-recovery-boundary-2026-09-16.md).
It separates total SPPCRC jurisdictional true-up amounts from the
Distribution Inspection program's `$92.1M` 2026 cost and `180,000`-pole
activity, and cross-checks the Form 6P capital/O&M presentation. The PSC
record also provides a 2026 factor petition with `$998.817M` of updated SPP
revenue requirements and `$984.084M` of alternative net jurisdictional
revenue requirements allocated under the approved rate-class methodology. The
subsequent Commission order confirms `$1.244B` of projected total SPP cost and
the `$998.817M` jurisdictional requirement. The new [rate-class factor boundary](capital-flow-fpl-2026-sppcrc-rate-class-factor-boundary-2026-09-16.md)
captures the conditional order factors, including residential `$0.00995/kWh`
and general-service demand `$1.80/kW`. A new [rate-class determinant boundary](capital-flow-fpl-sppcrc-rate-class-determinant-boundary-2026-09-16.md)
also recovers projected 2026 class-level kWh and billed-kW denominators from
Form 5P, including the `128,430,086,092 kWh` total projected sales base. This
is a non-settlement projection scenario and aggregate SPPCRC evidence, not
actual meter reads, invoices, collected cash, or Distribution Inspection
category cash. Q-11 therefore remains a strong route rather than an owner-cash
or return conclusion. The companion May 2025 SPPCRC testimony makes the
recovery-return mechanics explicit: projected capital requirements include
debt/equity return grossed up for tax on average monthly net investment,
including CWIP, and are allocated through separation factors; it reports
`$859.244393M` of total jurisdictional 2026 requirements. This strengthens the
regulatory recovery bridge but does not create category receipts or source-of-
funds proof.

The [retail lagged diagnostic](combined-investment-research-through-cycle-retail-lagged-diagnostic-2026-09-16.md)
now has a central evidence-register entry as a negative test: only 7 of 15
usable transitions agree between prior real-wage direction and next-period
cash-after-property direction. This weakens the simple affordability-to-cash
causal story and is useful as a falsifier, but it is not causal evidence because
the panel remains pooled and company actions, capex timing, vendor terms,
tariffs, promotions, and attached services are not controlled.

The [retail fixed-effect diagnostic](combined-investment-research-through-cycle-retail-fixed-effect-diagnostic-2026-09-16.md)
demeans each retailer before comparing real-wage changes with cash-after-property
changes. The pooled correlation is only `0.113120` across 12 usable transitions,
reinforcing that the affordability-to-cash mechanism is a weak descriptive
association in this small panel, not causal proof.

The [retail QoE component screen](combined-investment-research-quality-of-earnings-retail-component-screen-2026-09-16.md)
now assembles six same-company annual forensic transitions from the controlled
TJX, Target, and Walmart vectors. It exposes available receivables, revenue,
D&A, PP&E, SG&A/OSG&A, claims, cash-conversion, and current-asset accrual
components while preserving Target's missing receivables and the cohort's
missing gross-profit/total-assets joins. This advances the financial-
shenanigans review without calculating a Beneish score or implying a fraud
finding; the cross-pilot composite remains not assembled.
The new [annual retail cohort denominator control](combined-investment-research-pilot-02-retail-annual-cohort-denominator-control-2026-09-17.md)
puts TJX FY2026, Target FY2025, and Walmart FY2026 on one reported
cash-after-property-per-diluted-share basis while carrying lease cash, tax cash,
and supplier-finance movement as separate context. It improves CA-06's
comparability and double-count discipline, but it does not allocate maintenance
capital, attached-service costs, or common-owner claims; all three rows remain
reported-not-normalized.
The [TJX FY2026 owner-cash perimeter upgrade](combined-investment-research-tjx-fy2026-owner-cash-perimeter-upgrade-2026-09-17.md)
adds a company-specific annual capex, lease, tax, and repair-policy boundary:
`$6.874B` OCF less `$1.957B` property additions yields a `$4.917B` reported
cash-after-property screen. Lease and tax cash are retained as embedded OCF
burdens, not double-counted deductions; maintenance versus growth and final
owner cash remain open.
The [Walmart Q2 FY2027 cash-quality perimeter upgrade](combined-investment-research-walmart-q2-fy2027-cash-quality-perimeter-upgrade-2026-09-17.md)
adds the latest H1 cash-flow, supplier-finance, tariff-refund, tax-benefit,
debt, NCI, and diluted-share controls. Walmart's `$5.529B` reported free cash
flow remains limited because it excludes debt service, contractual obligations,
and acquisitions; CA-06 therefore remains partial.
The [Walmart Q2 capex/refund boundary](combined-investment-research-retail-walmart-q2-fy27-capex-refund-boundary-2026-09-17.md)
now adds the gain-contingency recognition rule for the `$2.9B` refund and the
February 2026 segment-overhead allocation revision. These strengthen temporary-
support and comparability controls, but do not create recurring margin,
service-cost, or common-owner cash proof.
The companion [annual attached-services cash frontier](combined-investment-research-pilot-02-retail-annual-attached-services-cash-frontier-2026-09-17.md)
adds Target's `$2.063B` FY2025 and Walmart's `$6.750B` FY2026 reported
attached-service pools to a clearly hypothetical 0–100% conversion surface.
Those values remain outside owner cash because service costs, collection,
working capital, tax, capex, and legal-entity claims are not allocated.
The [annual reported-cash expectation screen](combined-investment-research-pilot-02-retail-annual-reported-cash-expectation-screen-2026-09-17.md)
now divides the September 17 market caps by the latest annual reported
cash-after-property: TJX `27.906x`, Target `24.913x`, and Walmart `57.471x`.
These are price-burden screens, not normalized owner-cash multiples.
The 2026-09-17 composite-gate audit makes the hold test explicit: legal-entity
and period alignment, denominator taxonomy, total-assets/accrual fields,
cash/claim perimeter, and accounting-policy joins are still non-comparable
across retail, streaming, and insurance/asset-management. Sloan-, Schilit-,
and Beneish-style diagnostics remain useful prompts, but no pooled score is
published from these unlike perimeters.

The 2026-09-17 narrowed local-source check applied the move-on rule to Q-11:
no additional non-confidential Distribution Inspection billing, collection, or
funding schedule was found in the available FPL/PSC packet. Q-11 is parked at
`hold-with-strong-route-visible` and should be reopened only by a joinable
discovery response, supporting workpaper, or final SPPCRC true-up; aggregate
factor, cost, or utility-cash evidence should not be used to promote it.

Q-13 received a facility-level availability upgrade on 2026-09-17. URI's Q2
2026 10-Q reports `$2.802B` of ABL borrowing capacity net of letters of credit
and `$85M` of AR-securitization capacity, totaling `$2.887B`; that reconciles to
reported `$2.999B` total liquidity less `$112M` cash. This is stronger than an
implied liquidity subtraction, but it remains below certificate-grade proof:
eligible equipment, NOLV, reserves, U.S./Canadian components, live Combined
Borrowing Base, and source-to-purchase allocation remain missing. Q-13 stays
`evidence-insufficient` for legal availability and lifecycle return.
The same-period filing also reports `$158M` of net cash taxes paid, `$2.885B`
of equipment/intangible purchases, `$706M` of equipment-sale proceeds, and
`$400M` of acquisitions, alongside `$91M` of net debt payments, `$816M` of
share purchases, and `$248M` of dividends. These improve the consolidated
operating-to-capital and senior-claim bridge, but remain company-level cash
flows rather than ABL-draw, fleet-cohort, collateral-pool, or lifecycle-return
allocation evidence.
The live SEC recheck also located the June 18, 2026 AR-facility amendment;
it confirms the receivables-purchase legal route but adds no populated
purchaser availability schedule or certificate components. This sharpens the
acquisition request without promoting the facility proxy.

Q-12 received a mechanics-level upgrade on 2026-09-17. The public MF1
servicing agreement identifies the issuer, Collection Account, two-business-day
deposit rule, Note Administrator/Payment Account remittance route, permitted
servicing and expense deductions, partitioned-loan treatment, and noteholder
reporting path. The [servicing-waterfall boundary](capital-flow-apollo-athene-mf1-servicing-waterfall-mechanics-boundary-2026-09-17.md)
now makes the next cash join executable, but no borrower receipt, Athene legal
ownership, CUSIP-level remittance, liability-cost allocation, or Apollo
common-owner residual is observed. Q-12 remains `evidence-insufficient`.

The Q-12 MF1 route now has a row-level join boundary: CUSIP `592918-AA-4`
appears in the corrected Athene Schedule D holding/disposal packet under MF1
2025-B2 LLC with `$209.559M` of selected cash-like consideration, and the
servicing agreement supplies the named collection-to-trustee route. This
connects the statutory candidate to a concrete source-acquisition path, but
does not establish lot continuity, Athene custody, borrower receipt, trustee
remittance, liability-adjusted return, or Apollo common-owner cash.

The MF1 row now also has a diagnostic gross screen: `$209.559M` selected
consideration plus `$1.303M` of the selected row's income/dividend field equals
`$210.862M`, or `96.61%` of the `$218.272M` year-end reported holding amount.
That result is useful for reconciliation and QoE review, but the denominator is
not proven cost basis, lot continuity is missing, and the income field is not a
bank receipt. It is not a realized return, fraud finding, or owner-cash claim.

The MF1 public report route was also refreshed on 2026-09-17. CTSLink lists
August 18, 2026 Distribution Date, Bond Level, Collateral Summary, and Loan
Periodic reports, plus a revised August 21 Restricted Servicer Report, but all
require investor/party certification. The September 18 cycle is now current and
the October 19 cycle is next. The public deal-document tab also names the Offering Memorandum,
Servicing Agreement, Indenture, Transfer Exhibits, and CREFC Loan Set Up File;
the additional-document tab names Q1/Q2 2026 quarterly reports, CREFC CMDR
files, and property-level reports for Broadstone Axis and Woodside Central.
These metadata observations sharpen the collateral and servicing acquisition
queue, but the files remain gated and Q-12 stays `evidence-insufficient`. See
the [CTSLink metadata refresh](capital-flow-apollo-athene-mf1-2025b2-ctslink-metadata-refresh-2026-09-18.md).

The MF1 asset-side route now has a named-inventory upgrade. The SEC-filed
agreed-upon-procedures exhibit names all 23 collateral-interest/property
objects in the April 9, 2025 data-file population, including Citizen Bayonne,
Woodside Central, Broadstone Axis, Wyvernwood, ARIUM Greenview, ARIUM
Crowntree Lakes, and Jones Estates MHC Portfolio - Pool B; the exhibit states
that the population covers 74 related mortgaged properties. This converts the
prior count-only reference into a concrete acquisition queue, but the
underlying `MF1 2025-B2 Data Tape CSR.xlsx` and current loan-level reports are
not public in the exhibit. Addresses, borrower legal names, balances,
collections, trustee remittance, Athene allocation, and return therefore
remain unproven. See the [public collateral inventory boundary](capital-flow-apollo-athene-mf1-2025b2-public-collateral-inventory-boundary-2026-09-18.md).

The series-control warning is material: the locally captured servicing
agreement is headed MF1 2026-FL21 and its Exhibit A names a different asset
pool, so its collection-account and remittance mechanics cannot be treated as
a 2025-B2 collateral schedule or Athene-specific cash evidence.

Independent North Carolina public-holdings records now show the same MF1 2025-B2
LLC B2 A 144A description from September 2025 through January 2026, with
unchanged `$4.0M` par and market value near `$4.011M`. This strengthens the
public issuer/class and short continuity screen, but still does not identify
Athene custody, collateral allocation, remittance, or receipt.

## Industrial uptime move-on integration — 2026-09-17

The controlled move-on lane now connects the social observation that physical
work must keep moving to United Rentals, Sterling Infrastructure, WESCO, and
Fastenal. The [industrial uptime admission](combined-investment-research-industrial-uptime-move-on-admission-2026-09-17.md)
defines the shared chain as demand → control point → conversion → reinvestment
→ return, with the same QoE and financial-shenanigans gate used by the three
original pilots.

The [WESCO/Fastenal conversion screen](combined-investment-research-industrial-uptime-conversion-screen-2026-09-17.md)
shows period-matched H1 2026 reported operating cash less property spending of
`$223.5M` and `$521.1M`, respectively. WESCO's receivables and inventory
investment makes its cash conversion a live warning; Fastenal's stronger
conversion remains subject to service burden, customer mix, and recurring
maintenance questions. Neither screen is normalized owner cash.

The [Sterling backlog separation](combined-investment-research-industrial-uptime-sterling-backlog-quality-separation-2026-09-17.md)
keeps `$4.33B` signed backlog separate from `$5.62B` combined backlog and more
than `$1.4B` of future phases. It also isolates the `$2.56B` CEC/Stone Ridge
contribution and `21.5%` acquisition revenue contribution. This prevents
unsigned awards, future optionality, and acquired growth from receiving the
same valuation weight as contracted organic work.

The [industrial valuation/macro handoff](combined-investment-research-industrial-uptime-valuation-macro-handoff-2026-09-17.md)
now carries the cohort through Damodaran-style contracted/conversion/stress
cases and a Lyn-Alden-style map of rates, credit, inflation, power scarcity,
customer capex, and liquidity. The [industrial QoE register](combined-investment-research-industrial-uptime-qoe-diagnostic-register-2026-09-17.md)
routes cost-to-cost, working-capital, acquisition, capitalization, fleet, and
SBC warnings to thesis-breaker tests. The lane is end-to-end qualified but has
no normalized cross-company owner-cash ranking.
The three bridge passes now sharpen the handoff: Sterling's contract assets,
retainage, estimate changes, and acquisition cash are visible without a
project-level collection ledger; WESCO/Fastenal cash taxes and interest are
controlled as already embedded in OCF while post-OCF claims remain separate;
and URI's rental-equipment purchases, resale proceeds, liquidity proxy, and
working-capital support are visible without certificate-grade collateral or
replacement-capex allocation.

The [industrial-uptime first-principles synthesis](annual-report-industrial-uptime-first-principles-synthesis-pass-2-2026-09-17.md)
now turns that move-on lane into a sector chapter: WESCO and Fastenal are
distribution/control-point cases, Sterling is a project-conversion case, and
URI is a fleet-lifecycle case. It applies the QoE/financial-shenanigans,
Damodaran expectation, and Lyn Alden-style liquidity lenses while preserving
separate denominators and no-ranking boundaries.
The new [industrial uptime valuation/liquidity workbench](combined-investment-research-industrial-uptime-valuation-liquidity-workbench-2026-09-17.md)
now consolidates Sterling, WESCO, Fastenal, and URI into company-specific
valuation, reinvestment, liquidity, and thesis-breaker objects. It keeps
project backlog, distribution working capital, replenishment service, and
fleet lifecycle economics separate, and does not promote backlog, OCF-less-
capex, utilization, resale proceeds, or reported FCF into normalized owner
cash.

The new [Sterling project-conversion workbench](combined-investment-research-sterling-project-conversion-valuation-liquidity-workbench-2026-09-18.md)
now carries the project case through a dated valuation expectation screen.
Sterling's approximately `$16.153B` equity value is about `31.3x` the
annualized H1 mechanical OCF-less-capex screen, but the denominator remains
exposed to contract assets, retainage, estimate changes, acquisition cash,
earn-outs, dilution, and project collection. The base case uses `$4.33B` of
signed backlog only; unsigned awards, future phases, and acquired backlog are
separate conversion cases. Sterling remains qualified, unranked, and
owner-cash-open.

The new [United Rentals fleet-lifecycle workbench](combined-investment-research-united-rentals-fleet-lifecycle-valuation-liquidity-workbench-2026-09-18.md)
now carries the fleet case through a valuation and legal-availability boundary.
URI's approximately `$63.108B` equity value is about `84.4x` the annualized
H1 OCF-less-gross-rental-capex screen, while `$2.887B` of disclosed facility
availability remains a public proxy rather than certificate-grade legal
availability. Rental-equipment purchases, resale proceeds, ABL/AR capacity,
and fleet productivity remain diagnostic until replacement/growth capex,
collateral/NOLV/reserves, cohort funding, and lifecycle return are joined.
URI remains qualified, unranked, and owner-cash-open.

The new [WESCO/Fastenal distribution and replenishment workbench](combined-investment-research-wesco-fastenal-distribution-replenishment-valuation-liquidity-workbench-2026-09-18.md)
now carries the industrial cohort through a company-specific valuation screen.
WESCO's approximately `$16.771B` equity value is about `37.5x` a deliberately
annualized H1 mechanical cash screen, while Fastenal's approximately `$56.375B`
equity value is about `54.1x`; these are price-implied expectation diagnostics,
not normalized FCF multiples. WESCO's `$641.0M` receivables use, `$432.4M`
inventory use, and `$726.0M` payable support make collection the central gate;
Fastenal's `$320.2M` receivables use and approximately `$305M` of shareholder
returns make distribution coverage the central gate. Both remain qualified,
unranked, and owner-cash-open.

The new [industrial procurement valuation/liquidity workbench](combined-investment-research-industrial-procurement-valuation-liquidity-workbench-2026-09-17.md)
routes Applied, MSC Industrial, and Grainger as separate technical,
plant-floor, and high-touch/digital procurement models. Engineered mix,
vending, In-Plant service, customer share, inventory, fulfillment, technical
labor, acquisitions, debt, and dilution are kept distinct from WESCO/Fastenal
electrical and replenishment economics. Sales, customer counts, branches,
vending, and reported OCF remain diagnostic rather than normalized owner cash.

## New-sector move-on portfolio — 2026-09-17

The project now moves beyond the blocked receipt gates through the [new-sector
portfolio](combined-investment-research-move-on-sector-portfolio-2026-09-17.md):
healthcare distribution, semiconductor process control, and digital
infrastructure real estate. This is a controlled expansion, not a ranking.

The healthcare first pass compares McKesson, Cencora, and Cardinal Health on
thin-spread distribution, working capital, acquisitions, litigation, and
adjusted-earnings quality. McKesson has the strongest reported cash surface;
Cencora has the clearest adjusted-EPS/acquisition burden; Cardinal has the
clearest debt-funded acquisition and legal-cash burden. The [healthcare cash
and QoE comparison](combined-investment-research-healthcare-distribution-first-pass-2026-09-17.md)
keeps all three at `owner-cash-promotion-open`.

The companion [healthcare QoE ratio panel](combined-investment-research-healthcare-distribution-qoe-ratio-panel-2026-09-17.md)
keeps the same-fiscal-year cash-conversion, post-capex, acquisition-intensity,
and adjusted-EPS diagnostics separate from a manipulation score.
The [healthcare distribution first-principles synthesis](annual-report-healthcare-distribution-first-principles-synthesis-pass-2-2026-09-17.md)
now formalizes the route from essential-drug demand through manufacturer access,
regulated logistics, gross-profit spread, working-capital settlement, claims,
acquisitions, financing, and diluted common-owner residual. It preserves the
different McKesson, Cencora, and Cardinal cash-conversion problems and makes no
cross-company ranking.
The current-period healthcare refresh sharpens those problems: McKesson's Q1
FY2027 used `$220M` of operating cash after a `$4.448B` receivable/inventory
use was only partly offset by `$3.773B` of payable support, while a `$1.25B`
Apollo preferred investment and `$2.6B` of shareholder returns changed the
common-owner perimeter; Cencora's 9M FY2026 `$1.688B` OCF sat beside `$511M`
of capex and `$4.974B` of acquisition cash; and Cardinal's FY2026 `$5.174B`
OCF sat beside `$649M` capex, `$1.991B` acquisitions, opioid payments, debt,
and shareholder distributions. The values are period-labeled diagnostics,
not a pooled ranking or normalized owner-cash conclusion.
The new [healthcare distribution valuation/liquidity workbench](combined-investment-research-healthcare-distribution-valuation-liquidity-workbench-2026-09-17.md)
now turns McKesson, Cencora, and Cardinal into company-specific valuation,
reinvestment, liquidity, and thesis-breaker objects. It keeps McKesson's
payable-supported quarterly liquidity, Cencora's acquisition-funded specialty
expansion, and Cardinal's legal/acquisition-heavy residual separate, while
preserving their different fiscal periods and leaving normalized owner cash
open.
The September 18 price-input refresh places McKesson at approximately `20.0x`,
Cencora at `18.7x`, and Cardinal Health at `28.8x` against their unchanged
FY2025 reported OCF-less-capex screens. These are expectation diagnostics only;
the distributor working-capital, acquisition, legal, preferred/NCI, debt, and
dilution gates remain open.
The separate [healthcare access and care-delivery cluster](healthcare-access-care-delivery-cluster-synthesis.md)
extends the healthcare route beyond distribution: UnitedHealth and Cigna are
benefits/pharmacy control-plane cases; DaVita is recurring dialysis density;
Option Care is alternate-site infusion; and Addus, BrightSpring, and Enhabit
are home/community labor and care-delivery cases. UnitedHealth's Q2 revenue was
`$112.0B` with `$11.1B` Q2 operating cash, an `86.7%` medical-cost ratio,
`$860M` favorable prior-period reserve development, and `47.0` days claims
payable. Its six-month Form 10-Q roll-forward now also shows `$148.847B` of
reported medical costs, `$149.320B` of medical payments, `$38.930B` ending
medical costs payable, `$26.5B` IBNR, and `$1.250B` favorable prior-year
development. That strengthens the same-period liability/payment diagnostic but
does not provide a segment or legal-entity claims waterfall. Cigna's Q2 revenue
was `$71.668B`, adjusted income from operations was
`$2.054B`, medical-cost ratio was `84.5%`, and net medical costs payable were
`$5.09B`. Cigna's six-month roll-forward now adds `$15.825B` of incurred
claims, `$14.834B` of paid claims, `$5.228B` ending unpaid claims, and `$268M`
favorable prior-year development; its receivable facilities also show `$1.5B`
of H1 receivables sold, `$0.9B` uncollected, and `$0.3B` collected but not
remitted. DaVita reported `$490M` Q2 operating cash, `$256M` FCF, and `7.2266M`
U.S. dialysis treatments. Its H1 filing now adds `14.256M` treatments,
`$416.71` revenue per treatment, `$811M` OCF, `$197M` maintenance capital,
`$75M` development capital, `$150M` NCI distributions, and `$396M` disclosed
FCF, while `$1.561B` of NCI is subject to put provisions. The [Q2 healthcare access cash-quality refresh](combined-investment-research-healthcare-access-care-delivery-q2-2026-cash-quality-refresh-2026-09-17.md)
separates reserve development, claims liabilities, treatment volume, disclosed
FCF deductions, labor, capital, and noncontrolling interests. Option Care adds
Q2 revenue of `$1.442B`, `$184M` Q2 operating cash, `$171.485M` H1 operating
cash, and `$170.545M` H1 repurchases while receivables used `$37.941M`.
Option Care's Q2 filing adds `$2.381B` H1 commercial payer revenue, `$364M`
government payer revenue, `$529M` H1 gross profit, `18.5%` Q2 gross margin,
`$154.9M` earned but unbilled receivables, and an estimated `$55M` CID therapy-
mix headwind; payer-level collection and therapy-level margin remain open.
Addus adds `$377.417M` Q2 service revenue, `$40.0M` Q2 operating cash, `264`
offices across `24` states, and `32.0%` H1 gross margin. Its Q2 filing now adds
`28.3%` personal-care gross margin, `50.0%` government and `47.3%` MCO
personal-care payer mix, `$92.376M` H1 OCF, `$145.123M` ending AR, `$12.182M`
HomeCourt acquisition cash, and `$3.050M` PP&E/technology cash. Addus says cash
was affected by the timing of AR receipts and payroll/AP payments, so the new
[payer, wage, branch, and cash bridge](annual-report-addus-q2-2026-payer-wage-branch-cash-bridge-pass-2.md)
is qualified but branch return and normalized owner cash remain open. None of
these observations proves affordability, outcomes, reimbursement durability,
claims conversion, labor sufficiency, or common-owner cash. BrightSpring adds Q2
revenue of `$3.873B`, `$206M` adjusted EBITDA, `$166.859M` H1 operating cash,
`$42.203M` acquisitions, `$75.5M` net interest expense, and `$23.169M` share-based
compensation after its Community Living divestiture. The Q2 filing now
separates H1 Pharmacy Solutions revenue of `$6.579B`, Provider Services revenue
of `$908M`, segment EBITDA of `$490M`, `$1.139B` AR, `$575M` inventory,
`$810.908M` divestiture proceeds, and `$320.491M` debt repayment. The
[BrightSpring pharmacy/provider cash bridge](annual-report-brightspring-q2-2026-pharmacy-provider-cash-bridge-pass-2.md)
keeps those objects outside normalized owner cash.
The [Enhabit private-transition boundary](combined-investment-research-healthcare-enhabit-private-transition-q1-cash-quality-boundary-2026-09-17.md)
adds a final public Q1 care-delivery baseline: `$35.2M` OCF, `$(2.6M)`
investing cash, `$(26.6M)` financing cash, `$17.7M` of non-recurring
attorney-fee/mitigation settlement gain, payer-dependent revenue, and separate
Home Health/Hospice labor surfaces. Enhabit became private on May 15, 2026, so
no public Q2 series is assumed; post-close payer collection, labor, debt,
capex, and sponsor claims remain private-source gates.
CMS's FY2027 hospice rule adds a current external reimbursement breaker: a
`2.3%` payment update, `$36,174.75` aggregate cap, a `1.7%` quality-reporting
penalty, and a nine-measure service/spending variation index. This is a
Hospice payer and quality stress input—not Enhabit cash, patient mix, labor
productivity, or post-close collection evidence.
The [Intuitive installed-base cohort diagnostic](combined-investment-research-intuitive-installed-base-cohort-pass-2-2026-09-17.md)
now provides a quantified procedure-platform denominator: 11,710 da Vinci and
1,096 Ion systems, procedure growth, instruments/accessories, service, and
usage-based lease surfaces. It improves the installed-base transmission test,
but does not prove lease collection, cohort margin, or diluted owner cash.
The [Stryker–Inari post-close return bridge](combined-investment-research-stryker-inari-acquisition-cohort-pass-2-2026-09-17.md)
and [Henry Schein H1 funding bridge](combined-investment-research-henry-schein-owner-cash-funding-bridge-pass-2-2026-09-17.md)
now route the remaining medical-device cases through acquisition return,
quality claims, securitization collateral, debt funding, restructuring, and
dilution tests rather than consolidated OCF or adjusted EPS alone.

The new [managed-care payer valuation/liquidity workbench](combined-investment-research-managed-care-payer-valuation-liquidity-workbench-2026-09-17.md)
now gives UnitedHealth and Cigna a separate payer/claims route. Premiums,
medical costs, claims paid and unpaid, reserve development, pharmacy benefits,
rebates, provider payments, cyber, policy, trust, and legal-entity cash are
kept distinct from healthcare distribution and provider models. Revenue,
membership, MCR, adjusted EPS, SG&A, and OCF remain diagnostic until claims,
pharmacy, capital, debt, and diluted residual are joined.

The new [environmental-services valuation/liquidity workbench](combined-investment-research-environmental-services-valuation-liquidity-workbench-2026-09-17.md)
routes Waste Management, Republic Services, Casella, and Clean Harbors as
separate national route, regional landfill, recycling/RNG, and specialized
hazardous-treatment models. It keeps adjusted FCF, route density, landfill
capacity, sustainability projects, acquisitions, closure obligations, and
environmental liabilities out of normalized owner cash until company-specific
collection, replacement capital, claims, debt, and diluted residual are joined.

The new [branded consumer staples valuation/liquidity workbench](combined-investment-research-branded-consumer-staples-valuation-liquidity-workbench-2026-09-17.md)
routes Coca-Cola, PepsiCo, Brown-Forman, and Colgate-Palmolive as separate
beverage, food/distribution, premium-spirits, and habitual/pet-care models. It
keeps unit volume, price/mix, bottler/distributor settlement, aging inventory,
marketing, retailer support, acquisitions, debt, and diluted common cash out
of the retailer and household-value lanes.

The new [packaged-food, brand-repair, and household-value valuation/liquidity workbench](combined-investment-research-packaged-food-brand-repair-valuation-liquidity-workbench-2026-09-18.md)
adds General Mills as a distinct packaged-food, pet-food, and foodservice lane.
It tests organic volume, household penetration, retailer trade spending, commodity
inputs, inventory, brand and plant reinvestment, restructuring, debt, and diluted
common residual rather than treating cost savings or FCF-conversion targets as owner cash.

The new [athletic brand, channel-balance, and inventory-repair valuation/liquidity workbench](combined-investment-research-nike-brand-channel-inventory-valuation-liquidity-workbench-2026-09-18.md)
adds NIKE as a distinct global athletic-brand lane. It tests wholesale versus
NIKE Direct sell-through, traffic and conversion, product mix, markdowns,
inventory, digital/member systems, tariffs, brand investment, debt, and diluted
common residual rather than treating direct revenue or tariff recovery as owner cash.

The new [consumer-health, routine-care, and transaction-overhang valuation/liquidity workbench](combined-investment-research-kenvue-consumer-health-routine-care-valuation-liquidity-workbench-2026-09-18.md)
adds Kenvue as a distinct self-care, skin-health, oral-care, and everyday-health
lane. It tests category incidence, retailer/e-commerce sell-through, brand and
quality investment, segment mix, transaction costs, debt, and diluted common
residual rather than treating trusted brands or adjusted EPS as owner cash.

The new [travel and lodging platforms valuation/liquidity workbench](combined-investment-research-travel-lodging-platforms-valuation-liquidity-workbench-2026-09-17.md)
routes Airbnb, Booking, Marriott, Hilton, and Sunstone as distinct marketplace,
brand/loyalty, and property-owner models. GBV, bookings, rooms, pipeline,
RevPAR, FFO, loyalty points, contract fees, host/supplier payouts, property
renewal, and common cash remain separate from normalized owner cash.

The new [freight and logistics valuation/liquidity workbench](combined-investment-research-freight-logistics-valuation-liquidity-workbench-2026-09-17.md)
routes C.H. Robinson and UPS as contrasting asset-light brokerage and
asset-heavy parcel/network models. Gross profit per shipment, route/package
density, carrier/labor settlement, receivables, fleet/aircraft/facility
capital, transformation, acquisitions, and customer concentration remain
separate from normalized owner cash.

The new [frontier company-packet valuation/liquidity workbench](combined-investment-research-frontier-company-packets-valuation-liquidity-workbench-2026-09-17.md)
routes Host Hotels, F5, Veralto, and Caterpillar as four separate control
points: scarce lodging property, application delivery/security, embedded
water/product-quality measurement, and heavy-equipment installed base. It
keeps RevPAR/FFO, ARR, OCF conversion, backlog, dealer inventory, finance
receivables, asset-sale gains, acquisition cash, and capital returns out of
normalized owner cash until company-specific collection, replacement capital,
claims, debt, and diluted residual are joined.

The [KLA/Equinix/Digital Realty comparison](combined-investment-research-semiconductor-digital-infrastructure-comparison-2026-09-17.md)
separates process-control service economics, interconnection density, and
hyperscale powered capacity. KLA has the cleaner positive reported cash
surface; Equinix has the heavier interconnection growth-capital burden; Digital
Realty provides the backlog, lease-up, and development-yield test. None is
promoted to a ranking until capital maintenance, financing, dilution, and
per-share cash are reconciled.
The [semiconductor process-control first-principles synthesis](annual-report-semiconductor-process-control-first-principles-synthesis-pass-2-2026-09-17.md)
now formalizes KLA's route from node complexity and yield loss through systems,
installed service, acceptance, factoring, deferred revenue, R&D, commitments,
and diluted common-owner cash. It strengthens the control-point thesis while
keeping cycle-normalized maintenance, customer concentration, and owner-cash
tests open.
The [KLA five-year cash-cycle panel](combined-investment-research-kla-five-year-cash-cycle-panel-2026-09-17.md)
now replaces the single-year cash point with FY2022–FY2026 history. Reported
OCF-less-PP&E rises, but OCF margin falls from about 36.0% to 30.5% while the
receivable-plus-inventory-less-payable exposure screen rises from `$3.515B` to
`$5.914B`. This improves the cycle test without promoting the screen to owner
cash.
The [KLA installed-base denominator boundary](combined-investment-research-kla-installed-base-denominator-boundary-2026-09-17.md)
records a searched-negative result for numeric systems-in-field, utilization,
and renewal data in the FY2026 10-K. The filing names those service drivers but
does not quantify them, so the 16% service-revenue growth remains a control-point
indicator rather than a normalized service-per-system cash denominator. KLA's
March 2026 Investor Day adds a management expectation of `$26B ± $2.5B` 2030
revenue and 13–15% Services CAGR, but those figures remain valuation inputs
until the installed-base, utilization, renewal, service-margin, and
cycle-normalized owner-cash joins are evidenced.
The September 18 price-input refresh places KLA at approximately `6.2x` market
capitalization to FY2026 reported OCF less PP&E. This is a cycle expectation
screen only: factoring, working-capital exposure, R&D/support, commitments, and
the missing installed-base denominator keep KLA qualified, unranked, and
owner-cash-open.
The [retail CA-06 allocation boundary](combined-investment-research-retail-ca06-allocation-boundary-2026-09-17.md)
consolidates the current TJX, Target, and Walmart evidence: OCF and property
spending are observed, but matched maintenance/growth, supplier-finance,
lease/tax, and attached-service allocation objects remain missing. Annual
burden context and period-end obligations are not treated as H1 cash deductions.
The [CA-06 source-acquisition packet](combined-investment-research-retail-ca06-source-acquisition-packet-2026-09-18.md)
now turns those gaps into an executable document queue with required fields and
promotion tests for each company. It preserves the same-period, same-entity
rule and does not promote supplier-finance balances, annual lease/tax context,
mixed property spending, or attached-service revenue into normalized
common-owner cash.
The Target Q2 call refresh is now part of that source queue: it confirms the
same-period capex categories and operating-burden surfaces but does not close
the maintenance/replacement or service-level cash allocation test.
The [digital infrastructure real-estate first-principles synthesis](annual-report-digital-infrastructure-real-estate-first-principles-synthesis-pass-2-2026-09-17.md)
formalizes the parallel Equinix/Digital Realty route from cloud, AI, and
connectivity demand through power, interconnection, energization, lease
commencement, rent, development capital, partner funding, and per-share
residual. It keeps AFFO/FFO, backlog, and parent cash separate from stabilized
common-owner return.
The [digital infrastructure project-return workbench](combined-investment-research-digital-infrastructure-project-return-workbench-2026-09-17.md)
now serves as the direct promotion control: it separates recurring cash from
development, acquisition, JV/fund, debt, partner, and equity funding surfaces.
Named project capital, commencement, stabilized NOI, and per-share return
remain open.
The current Q2 digital-real-estate refresh makes the burden visible: Equinix's
H1 `$1.784B` OCF was below `$2.834B` of PP&E purchases before `$224M` of
real-estate acquisitions, while Digital Realty's `$1.595B` OCF was roughly
`$32M` below `$1.627B` of cash-basis capex, including `$1.477B` of development
and `$136M` of recurring capex. Digital Realty also reported about `$2.5B` of
year-to-date ATM proceeds and `$18.768B` of consolidated debt. AFFO/FFO,
backlog, signed rent, fund contributions, and equity proceeds therefore remain
funding or visibility inputs until project commencement, stabilized NOI,
recurring capex, partner claims, and diluted per-share residual are joined.
The September 18 expectation refresh places Equinix at approximately `$101.252B`
of equity value and Digital Realty at approximately `$65.844B`. A period-aware
reported-cash screen is about `31.0x` for Equinix—annualized H1 OCF less the
full-year `$300M` recurring-capex guide—and `22.6x` for Digital Realty—H1 OCF
less H1 recurring capex, annualized. These are not normalized owner-cash
multiples: project capital, power, leasing costs, partner/JV claims, debt,
preferred/OP-unit claims, ATM dilution, and stabilized NOI remain unjoined.
The [URI borrowing-base collateral proof chase](capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.md)
now gives the asset-backed lane a facility-level bridge: Q2 ABL capacity of
`$2.802B`, AR securitization capacity of `$85M`, and a `$2.887B` reconciliation
to total liquidity less cash. It explicitly keeps those amounts separate from
populated borrowing-base certificates, NOLV/reserves, source-to-purchase use,
and lifecycle owner return.
The [power-grid current-period synthesis](combined-investment-research-power-grid-current-period-synthesis-2026-09-17.md)
now consolidates NextEra/FPL, AEP, and Duke around their distinct control
objects: category recovery, named large-load obligations, and a co-owned
generation project. Approved recovery, signed load, and capacity remain
separate from billing, collection, paid capex, financing, and common-owner
return.
The [power-grid valuation and liquidity handoff](combined-investment-research-power-grid-valuation-liquidity-handoff-2026-09-17.md)
adds the Damodaran and Lyn Alden layers: market-implied future recovery and
rate-base conversion are separated from current cash, while rates, construction
inflation, fuel/power access, regulatory lag, affordability, tax-credit support,
and dilution are connected to named company mechanisms.
The new [power-grid valuation/liquidity workbench](combined-investment-research-power-grid-valuation-liquidity-workbench-2026-09-17.md)
now makes the company-specific objects explicit: FPL category/rate-base
recovery, AEP large-load/tariff obligations, and Duke's co-owned Anderson
County project. It adds reinvestment denominators, financing and affordability
stresses, and filing-based thesis breakers without promoting approved recovery,
signed load, capacity, OCF, debt capacity, or tax-credit proceeds into
common-owner cash.

The new [merchant power and generation valuation/liquidity workbench](combined-investment-research-merchant-power-generation-valuation-liquidity-workbench-2026-09-17.md)
extends the power lane to Constellation, Exelon, NRG, and Vistra without
pooling their models. Clean nuclear generation, regulated wires,
customer-backed power, and merchant dispatchable fleets retain separate
availability, recovery, hedge/PPA, project, debt, and diluted-owner-cash tests.
MW, availability, adjusted EBITDA, FCFbG, signed load, and PPAs remain
diagnostic rather than normalized cash.

The next admitted sector is [medical devices and clinical workflow](combined-investment-research-medical-devices-clinical-workflow-admission-2026-09-17.md).
Stryker, Intuitive Surgical, and Henry Schein extend the method from drug
distribution to procedure platforms, installed systems, consumables, service,
and practice procurement. The first-pass evidence is present, but acquisition,
utilization, regulatory, R&D, inventory, and dilution gates remain open.
The corresponding [medical-devices QoE ratio panel](combined-investment-research-medical-devices-qoe-ratio-panel-2026-09-17.md)
shows Stryker's acquisition-heavy residual, Intuitive Surgical's strong but
inventory/SBC-burdened cash surface, and Henry Schein's thin post-reinvestment
residual without treating them as a ranking. The [medical-devices valuation
expectation register](combined-investment-research-medical-devices-valuation-expectation-register-2026-09-17.md)
then states what each historical market snapshot requires before promotion.
The [owner-cash bridge pass 1](combined-investment-research-medical-devices-owner-cash-bridge-pass-1-2026-09-17.md)
keeps Stryker's acquisition cash, Intuitive Surgical's inventory/SBC boundary,
and Henry Schein's debt and repurchase burden explicit. It is a controlled
denominator bridge, not a final common-owner cash ranking.
The [filing-evidence queue](combined-investment-research-medical-devices-filing-evidence-queue-2026-09-17.md)
now names the exact FY2025 10-K and Q1/Q2 2026 artifacts needed to resolve
Stryker acquisition returns and cyber burden, Intuitive utilization and lease
collections, and Henry Schein restructuring, working capital, debt, and
repurchase funding.

The [medical-devices clinical-workflow first-principles synthesis](annual-report-medical-devices-clinical-workflow-first-principles-synthesis-pass-2-2026-09-17.md)
now formalizes the lane as an end-to-end sector chapter. It connects clinical
demand and labor constraints to procedure platforms, installed-base usage,
distribution, reimbursement, owner-cash burdens, QoE diagnostics, Damodaran
expectations, and Lyn Alden-style liquidity transmission without pooling the
three companies into a ranking.
The [evidence-resolution pass 1](combined-investment-research-medical-devices-evidence-resolution-pass-1-2026-09-17.md)
now anchors six observations directly to the preserved 10-Ks: Stryker's Inari
consideration and Guard adjacency, Intuitive's usage-based lease revenue and
SBC-scope discrepancy, and Henry Schein's multi-year restructuring and
repurchase/liquidity burden.
The [Henry Schein waterfall](combined-investment-research-henry-schein-restructuring-liquidity-waterfall-pass-1-2026-09-17.md)
now separates the `$322M` first-pass residual from the `$105M` multi-year
restructuring charge, `$850M` of repurchases, approximately `$156M` of cash,
and approximately `$3.1B` of debt. It keeps restructuring cash-paid and
repurchase funding open rather than double-counting or promoting optics.
The [Stryker–Inari cohort pass](combined-investment-research-stryker-inari-acquisition-cohort-pass-1-2026-09-17.md)
now ties the `$4.810B` consideration to `$3.191B` goodwill, `$1.860B` of
identified intangibles, a 13-year weighted-average life, and a `$139M` vested
employee-award charge. It strengthens the acquisition-burden test while
leaving Inari-only revenue, margin, cash return, and incremental ROIC open.
The [Intuitive installed-base pass](combined-investment-research-intuitive-installed-base-economics-pass-1-2026-09-17.md)
now joins more than 11,100 da Vinci systems and 995 Ion systems to `$6.019B`
of instruments/accessories, `$1.572B` of services, `$874M` of operating-lease
revenue, and `$531M` of variable usage-based lease revenue. Its mechanical
per-system ratios are explicitly not treated as allocated unit economics.
The next cross-sector lane is [power-grid customer cash](combined-investment-research-power-grid-customer-cash-admission-2026-09-17.md).
It carries the method into regulated infrastructure: FPL category recovery,
AEP large-load obligations, and Duke's Anderson County approval are kept
separate from billing, collection, rate-base cash, financing, and common-owner
return.
The [power-grid valuation/liquidity handoff](combined-investment-research-power-grid-valuation-liquidity-handoff-2026-09-17.md)
adds the next layer: NextEra's `$7.276B` first-half OCF against `$19.389B`
of investment and Duke's `$12.330B` OCF against `$14.024B` capex. It keeps
the market-implied rate-base/project-return burden separate from collected
customer cash, and defers AEP's multiple until its market denominator is joined.
The next capital-flow lane is [insurance statutory named-asset income](combined-investment-research-insurance-statutory-named-asset-admission-2026-09-17.md).
It narrows the big-money question below AUM to insurer legal entity, named
asset, income/proceeds, liability cost, remittance, and return. Apollo/Athene
is the strongest prototype; Accordia is the best current comparison.
The [insurance evidence panel](combined-investment-research-insurance-statutory-named-asset-evidence-panel-2026-09-17.md)
keeps Apollo/Athene's legal-entity proceeds, Accordia's row-level interest,
and Blackstone/Brookfield platform routes at separate proof grades.
The [insurance statutory named-asset first-principles synthesis](annual-report-insurance-statutory-named-asset-first-principles-synthesis-pass-2-2026-09-17.md)
now formalizes the route from policyholder funding through insurer legal entity,
named asset and income/proceeds to liability cost, remittance, and common-owner
residual. It is a qualified synthesis with no ranking: statutory income and
collected cash are separated, and the liability-adjusted return and upstream
receipt gates remain open.

The new [asset-management platforms valuation/liquidity workbench](combined-investment-research-asset-management-platforms-valuation-liquidity-workbench-2026-09-17.md)
routes BlackRock, Blackstone, and Brookfield as separate public-markets,
private-markets, and operating-real-asset platforms. AUM, flows, fee-related
earnings, distributable earnings, carried interest, owned-asset income,
insurance capital, and adjusted EPS remain separate from same-entity common-
owner cash until realization, compensation, leverage, legal-entity, and
dilution joins are evidenced.

The new [private-markets fee, carry, and credit-platform valuation/liquidity workbench](combined-investment-research-carlyle-fee-carry-private-credit-valuation-liquidity-workbench-2026-09-18.md)
adds The Carlyle Group as a distinct private-markets route, separate from the
BlackRock, Blackstone, and Brookfield platform objects. It tests fee-earning AUM,
FRE, realized versus accrued carry, private-credit losses, partner allocations,
available capital, parent liquidity, and diluted common residual.
The [insurance statutory owner-cash promotion workbench](combined-investment-research-insurance-statutory-owner-cash-promotion-workbench-2026-09-17.md)
now makes the promotion formula executable: named income and proceeds less
losses, liability funding cost, reinsurance/funds-held claims, taxes, fees,
capital requirements, remittance, and parent claims. It preserves Apollo/Athene
and Accordia at qualified proof grades until receipt and after-cost return are
source-backed.
The [Apollo–Athene Q2 parent-receipt attribution frontier](capital-flow-apollo-athene-q2-parent-receipt-attribution-frontier-2026-09-15.md)
now makes the upstream join explicit: Athene's `$110M` H1 distribution-to-parent
observation is kept at the legal-entity level, with a mechanical `$0M–$110M`
AGM-attribution sensitivity. The frontier does not prove a dated AGM receipt,
parent-only availability, intercompany elimination, senior claims, or a
common-owner residual, so it is a receipt-control artifact rather than a
promoted return.
The [private-credit borrower promotion workbench](combined-investment-research-private-credit-promotion-workbench-2026-09-17.md)
now puts Bear Financing, Concord, and Frontline on the same chain from legal
lender/holder through instrument, borrower, funded principal, collateral,
debt service, receipt, repayment, liability cost, and residual. It explicitly
excludes Atwell from the Ares/Frontline allocation test and keeps all routes
qualified and unranked.

## Latest integrative extension — physical capacity and private credit

The newest work extends the end-to-end system beyond the original pilots
without weakening the evidence discipline. The [private-credit promotion
workbench](combined-investment-research-private-credit-promotion-workbench-2026-09-17.md)
puts Bear Financing, Concord, and Ares/Frontline on one ladder from legal
holder through funded principal, lender allocation, borrower debt service,
receipt, repayment, liability cost, and owner residual. Each route remains
held because a statutory row, wrapper, arranger role, or fair-value mark is not
the same as a completed lender cash loop.

The [URI collateral-to-owner-cash workbench](combined-investment-research-uri-collateral-to-owner-cash-promotion-workbench-2026-09-17.md)
then completes the asset-backed diagnostic chain from fleet purchases and
resale recovery to ABL/AR capacity, collateral eligibility, senior claims, and
lifecycle return. The [physical-capacity cash-conversion comparison](combined-investment-research-physical-capacity-cash-conversion-comparison-2026-09-17.md)
shows the three distinct mechanisms: URI fleet access and resale/collateral,
Equinix powered-capacity lease-up, and Digital Realty hyperscale development
and private-capital funding.

The [physical-capacity valuation/liquidity stress workbench](combined-investment-research-physical-capacity-valuation-liquidity-stress-workbench-2026-09-17.md)
and [thesis-breaker register](combined-investment-research-physical-capacity-thesis-breaker-register-2026-09-17.md)
carry those lanes through price-implied expectations, rate/inflation/funding
stress, and six company-specific filing falsifiers. The result is a stronger
cross-sector research system, not a ranking: each lane still needs its own
project, collateral, receipt, or common-owner residual evidence.
The next move-on sector is the [restaurant-franchise first-principles
synthesis](annual-report-restaurant-franchise-first-principles-synthesis-pass-1-2026-09-17.md).
It applies the same control-point, QoE/financial-shenanigans, owner-cash,
Damodaran, and Lyn Alden lenses to CAVA, Restaurant Brands International,
Wingstop, and Yum. FY2025 OCF-less-PP&E screens range mechanically from
`$26.141M` to `$1.639B`, but the companies are not ranked: advertising-fund
perimeter, franchisee support, maintenance/growth capex, debt, acquisitions,
and dilution remain open before normalized common-owner cash can be promoted.
The [restaurant-franchise owner-cash promotion workbench](combined-investment-research-restaurant-franchise-owner-cash-promotion-workbench-2026-09-17.md)
now converts the gap into a field-level decision matrix. OCF and PP&E are
proven as diagnostics, while royalty amount/collection, advertising-fund
inflows and restricted use, franchisee health, maintenance versus growth,
support, debt, leases, acquisitions, and dilution remain promotion gates.
The [restaurant-franchise filing evidence panel](combined-investment-research-restaurant-franchise-filing-evidence-panel-2026-09-17.md)
adds verified filing-text controls: RBI reports over `95%` of systemwide
restaurants franchised; Wingstop reports approximately `98%` franchised,
`2,999` franchised restaurants, and a `5.5%` FY2025 advertising-fund
contribution rate; Yum reports `97%` franchisee ownership and `23` FY2025
refranchised restaurants. These strengthen the control-point map but do not
prove advertising-fund collection, royalty margin, or owner cash.
Wingstop's FY2025 filing also gives a burden-shift diagnostic—approximately
`$2.0M` domestic AUV versus approximately `$580,000` initial investment,
excluding real estate and pre-opening costs. That sharpens the franchisee
economics question but is not a franchisee IRR, payback, or franchisor margin.
The [restaurant current-period refresh](combined-investment-research-restaurant-current-period-refresh-2026-09-17.md)
adds McDonald's and Chipotle's H1 2026 filing surface without pooling it with
the FY2025 cohort. McDonald's reports `$5.222B` OCF against `$1.516B` PP&E,
`$1.251B` repurchases, and `$2.640B` dividends; Chipotle reports `$1.332B`
OCF against `$397.601M` PP&E and `$1.355B` repurchases. The arithmetic screens
are deliberately non-comparable and do not establish owner cash.
The current filing also makes the franchise perimeter concrete: McDonald's
reported `$34.451B` of Q2 franchised sales across `44,016` franchised
restaurants, but those sales are not recorded as company revenue and are only
an indicator of franchisee health. The missing join is franchised-sales to
royalty/fee collection, franchisee cash health, closures or delinquency, and
required remodel/technology reinvestment. Systemwide sales and franchisor OCF
therefore remain visibility inputs rather than normalized common-owner cash.
The new [restaurant-franchise valuation/liquidity workbench](combined-investment-research-restaurant-franchise-valuation-liquidity-workbench-2026-09-17.md)
now carries CAVA, Restaurant Brands International, Wingstop, Yum, McDonald's,
and Chipotle through company-specific valuation objects, reinvestment burdens,
franchisee/company-store liquidity stresses, and filing-based thesis breakers.
It preserves the FY2025 versus H1 2026 period split and keeps systemwide sales,
royalties, OCF, dividends, and repurchases out of normalized owner cash until
collection, support, required reinvestment, debt, dilution, and common-residual
joins are evidenced. The restaurant lane remains qualified, unranked, and
owner-cash-open.

The new [cash logistics and managed-services valuation/liquidity workbench](combined-investment-research-brinks-cash-logistics-managed-services-valuation-liquidity-workbench-2026-09-18.md)
adds Brink's as a distinct physical-payments infrastructure lane. It separates
cash-and-valuables routes, ATM managed services, digital retail solutions,
contract density, labor, fleet, security, acquisitions, debt, and dilution.
AMS/DRS growth, adjusted EBITDA, free cash flow, and acquisition synergies
remain diagnostic rather than normalized owner cash. The lane remains qualified,
unranked, and owner-cash-open.

The Q2 2026 filing pass now sharpens Brink's cash-quality boundary: H1 GAAP
operating cash was `$65.2M`, cash capex was `$74.9M`, financing leases were
`$42.9M`, and filed free cash flow before dividends was `$32.0M`. The filing
separates restricted customer cash and secure cash-management customer
obligations from general corporate cash; June 30 total debt was `$4.2423B`,
cash was `$1.6582B`, `$145.8M` was held in cash-management operations, and
reported net debt was `$2.7299B`. NCR Atleos remains a separate closing-
dependent branch: estimated consideration is approximately `$4B`, `$29.2M` of
transaction costs had been incurred, and H1 acquisition/transformation costs
were `$75.3M`. TTM FCF of `$468M`, adjusted EBITDA, and the synergy target
remain diagnostic rather than normalized owner cash; Brink's stays qualified,
unranked, and owner-cash-open.

The Q2 service-mix pass adds a second Brink's control: H1 DRS/AMS revenue was
`$812.6M` of `$2.7674B` segment revenue, while H1 CVM revenue was `$1.9548B`.
The filing does not provide separate DRS/AMS profit or cash. DRS/AMS still
includes dispatch, installation, maintenance, parts, settlement, and sometimes
Brink's-owned ATM devices; across the segments H1 labor and fringe costs were
`$1.0410B` against `$446.8M` of segment operating profit. Recurring-service mix
is therefore a productivity and asset-burden hypothesis, not software-like
owner cash. Revenue per vehicle/employee, collection, service quality,
maintenance intensity, and security-loss experience remain the next promotion
gates.

The collection pass adds a filed working-capital control: customer-contract
receivables increased `$99.7M` to `$865.7M` by June 30, while H1 revenue rose
`$220.2M`; the cash-flow statement reports a `$106.3M` use for accounts
receivable and income-tax receivable. Contract assets fell to `$26.5M`, contract
liabilities fell to `$14.0M`, and net capitalized contract-acquisition costs
rose to `$15.1M`. Brink's therefore has a current revenue and receivables
bridge, but no public route-level aging or collection ledger. The recurring mix
remains qualified rather than normalized owner cash.

The Brink's valuation screen now anchors the expectation burden to the
September 18 market snapshot: approximately `$4.404B` equity value plus filed
net debt of `$2.7299B` implies about `$7.134B` enterprise value, or roughly
`15.2x` management-reported TTM FCF of `$468M`. This is not a promoted multiple:
the latest H1 filed FCF before dividends was `$32.0M`, and NCR Atleos creates a
closing-dependent approximately `$4B` consideration and financing branch. The
market therefore requires durable route productivity, DRS/AMS mix improvement,
and successful integration before the screen can support a normalized owner-cash
valuation.

The Q2 source pass adds the cash-quality boundary: `$297.0M` Q2 operating cash
included `$86.9M` of favorable working-capital change and `$108.3M` of cash
sustaining capital, producing `$101.8M` reported free cash flow. The Peru port
delay moved approximately `10,000` dry metric tonnes of concentrate into July.
At quarter-end, `$334.5M` of the `$890.9M` cash balance was contractually
restricted to Copper World, and net debt was negative `$80.5M` after partnership
funding and debt refinancing. Hudbay remains qualified and unranked; neither
negative cash cost, JV proceeds, restricted project cash, nor production proves
unrestricted common-owner cash.

The new [mid-tier copper-gold and project-partnership valuation/liquidity workbench](combined-investment-research-hudbay-copper-gold-project-partnership-valuation-liquidity-workbench-2026-09-18.md)
adds Hudbay Minerals as a distinct mining lane. It separates copper, gold
by-product credits, grades, concentrate logistics, project partnerships,
permitting, sustaining and growth capital, debt, and dilution. Production,
negative cash cost, adjusted EBITDA, free cash flow, JV proceeds, and guidance
remain diagnostic rather than normalized owner cash. The lane remains qualified,
unranked, and owner-cash-open.

The new [nicotine transition and regulated-habit valuation/liquidity workbench](combined-investment-research-philip-morris-nicotine-transition-valuation-liquidity-workbench-2026-09-18.md)
adds Philip Morris International as a distinct regulated-consumption lane. It
separates combustibles, smoke-free products, adult-user migration, excise taxes,
market access, manufacturing, litigation, debt, and dilution. Smoke-free mix,
users, shipment volume, adjusted EPS, dividends, and buybacks remain diagnostic
rather than normalized owner cash. The lane remains qualified, unranked, and
owner-cash-open.
The Q2 source pass adds the cash perimeter: H1 smoke-free revenue was `$9.024B`
of `$21.338B` total revenue, H1 operating cash was `$5.093B`, capex was
`$733M`, full-year capex guidance was `$1.4B–$1.6B` predominantly for
smoke-free capacity, and total debt was `$49.1B`. H1 debt repayment and
dividends were `$4.021B` and `$4.604B`, respectively. PMI does not disclose
smoke-free capex or operating cash by segment, so the transition remains
qualified rather than promoted to smoke-free owner cash; German, Japanese, and
EU excise-tax developments remain live margin and return controls.

The new [Take-Two recurrent digital worlds valuation/liquidity workbench](combined-investment-research-take-two-recurrent-digital-worlds-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct owned-worlds gaming lane. It separates full-game launches, recurrent
consumer spending, net bookings, GTA, NBA 2K, Zynga mobile, player retention,
development capitalization, licensing, deferred revenue, debt, and dilution from
revenue, recurrent-spend growth, and tentpole launch value. Take-Two remains
qualified, unranked, and owner-cash-open.

The new [NetApp hybrid-cloud data-platform valuation/liquidity workbench](combined-investment-research-netapp-hybrid-cloud-data-platform-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct enterprise data-control lane. It separates hybrid-cloud systems,
public-cloud services, support, software, billings, deferred revenue, channel
distribution, all-flash demand, cloud capacity, debt, and dilution from revenue,
services growth, billings, reported OCF/FCF, and AI demand. NetApp remains qualified,
unranked, and owner-cash-open.

The new [creator imaging and hardware-to-workflow valuation/liquidity workbench](combined-investment-research-gopro-creator-imaging-workflow-valuation-liquidity-workbench-2026-09-18.md)
adds GoPro as a distinct creator-hardware lane. It separates camera sell-through,
subscription attachment, editing workflow, component commitments, inventory,
tariffs, strategic alternatives, debt, and dilution. Units, subscribers,
adjusted EBITDA, and roadmap announcements remain diagnostic rather than
normalized owner cash. The lane remains qualified, unranked, and
owner-cash-open.
The Q2 source pass adds a major current financing boundary: H1 operating cash
was negative `$47.4M`, cash was `$27.3M`, debt principal was `$87.2M`, and gross
margin included an `$18.9M` tariff-refund benefit against `$39.6M` of H1
component-commitment charges. The September 1 definitive Starman Optical
merger agreement now creates a separate, unclosed transaction branch: `$285M`
aggregate cash consideration subject to working-capital adjustment,
approximately `10%` post-close rollover ownership, and approximately `$92M`
debt repayment. These are proposed closing terms, not current GoPro owner
cash or proof of a self-funding camera business.

The new [Ivanhoe African copper buildout valuation/liquidity workbench](combined-investment-research-ivanhoe-african-copper-buildout-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct African copper-and-development lane. It separates Kamoa-Kakula
attributable cash, Kipushi inventory, Platreef construction, smelter ramp, corridor
logistics, JV accounting, project finance, taxes, debt, and dilution from copper
production, JV revenue, adjusted EBITDA, and project guidance. Ivanhoe remains
qualified, unranked, and owner-cash-open.

The new [Dow chemicals restructuring valuation/liquidity workbench](combined-investment-research-dow-chemicals-restructuring-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct diversified-chemicals cycle lane. It separates polyethylene and
feedstock exposure, downstream applications, plant closures, cost programs, working
capital, environmental claims, dividends, debt, and dilution from revenue, operating
EBITDA, guidance, and cost-savings promises. Dow remains qualified, unranked, and
owner-cash-open.

The new [Lennar land-light homebuilder valuation/liquidity workbench](combined-investment-research-lennar-land-light-homebuilder-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct direct-homebuilder lane. It separates deliveries, orders, backlog,
incentives, mortgage affordability, cycle time, land exposure, mortgage/title capture,
multifamily, working capital, debt, and dilution from revenue, backlog value, OCF, and
buybacks. Lennar remains qualified, unranked, and owner-cash-open.

The new [Electronic Arts live-services and franchise valuation/liquidity workbench](combined-investment-research-electronic-arts-live-services-franchise-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct repeat-participation gaming lane. It separates full-game launches,
live services, net bookings, player engagement, EA SPORTS FC, Apex, Battlefield,
deferred revenue, licensing, development costs, merger costs, debt, and dilution from
revenue, live-service growth, and guidance. Electronic Arts remains qualified,
unranked, and owner-cash-open.

The new [Caesars Rewards and digital gaming valuation/liquidity workbench](combined-investment-research-caesars-rewards-digital-gaming-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct cross-market gaming and loyalty lane. It separates regional and Las
Vegas gaming, Rewards, universal wallet, sportsbook, iGaming, Racebook, property
capex, leases, debt, interest, and dilution from revenue, adjusted EBITDA, digital
growth, and Rewards members. Caesars remains qualified, unranked, and owner-cash-open.

The new [Las Vegas Sands integrated-resort valuation/liquidity workbench](combined-investment-research-las-vegas-sands-integrated-resort-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct Asia destination-platform lane. It separates Marina Bay Sands,
Macao, gaming hold and volume, hotels, conventions, luxury retail, concessions,
expansion capex, debt, buybacks, and dilution from revenue, property EBITDA, gaming
volume, and expansion value. Las Vegas Sands remains qualified, unranked, and
owner-cash-open.

The new [Instacart grocery and retail-media valuation/liquidity workbench](combined-investment-research-instacart-grocery-retail-media-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct grocery-demand and retailer-enablement lane. It separates GTV,
orders, shopper and retailer settlement, advertising, Storefront software, in-store
technology, AI products, acquisitions, working capital, and dilution from revenue,
adjusted EBITDA, and marketplace scale. Instacart remains qualified, unranked, and
owner-cash-open.

The new [ICU Medical infusion and consumables valuation/liquidity workbench](combined-investment-research-icu-medical-infusion-consumables-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct clinical-replenishment lane. It separates infusion-system placement,
recurring consumables, Vital Care, hospital and distributor channels, safety-stock
inventory, tariffs, quality spending, acquisitions, debt, and dilution from revenue,
adjusted EBITDA, EPS, OCF, and buybacks. ICU Medical remains qualified, unranked, and
owner-cash-open.

The new [Quest Diagnostics laboratory-network valuation/liquidity workbench](combined-investment-research-quest-diagnostics-laboratory-network-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct diagnostic-infrastructure lane. It separates requisition volume,
routine and advanced assays, payer and employer channels, consumer testing, logistics
density, lab automation, acquisitions, reimbursement, connectivity, debt, and dilution
from revenue, test volume, adjusted EPS, OCF, guidance, and buybacks. Quest remains
qualified, unranked, and owner-cash-open.

The new [Xerox installed-base and workflow-services valuation/liquidity workbench](combined-investment-research-xerox-installed-base-workflow-services-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct mature-business-equipment lane. It separates equipment, post-sale
service, managed print, workflow and IT attachment, financing, page volumes,
replacement cycles, Lexmark and ITsavvy integration, tariffs, debt, and dilution from
revenue, adjusted operating income, post-sale mix, FCF, and synergies. Xerox remains
qualified, unranked, and owner-cash-open.

The new [Urban Outfitters and Nuuly lifestyle valuation/liquidity workbench](combined-investment-research-urban-outfitters-nuuly-lifestyle-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct multi-banner and wardrobe-access lane. It separates Anthropologie,
Free People, Urban Outfitters, Nuuly, subscription and rental utilization, wholesale,
inventory, returns, tariffs, stores, digital demand, leases, debt, and dilution from
revenue, comps, subscription growth, and guidance. Urban Outfitters remains qualified,
unranked, and owner-cash-open.

The new [American Eagle and Aerie apparel valuation/liquidity workbench](combined-investment-research-american-eagle-aerie-apparel-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct brand-split apparel lane. It separates Aerie growth, American Eagle
relevance, comparable sales, inventory and markdowns, stores, digital demand, leases,
capital returns, debt, and dilution from sales, comps, EPS, and guidance. American
Eagle remains qualified, unranked, and owner-cash-open.

The new [DraftKings real-money participation valuation/liquidity workbench](combined-investment-research-draftkings-real-money-participation-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct regulated-participation lane. It separates sportsbook handle, hold,
promotions, iGaming, fantasy, lottery, prediction markets, user retention, state
licenses, payment settlement, cash, debt, and dilution from revenue, MUPs, ARPMUP,
adjusted EBITDA, and guidance. DraftKings remains qualified, unranked, and
owner-cash-open.

The new [Taboola open-web performance-advertising valuation/liquidity workbench](combined-investment-research-taboola-open-web-performance-advertising-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct open-web demand-routing lane. It separates advertiser outcomes,
ex-TAC gross profit, publisher and OEM settlements, traffic concentration, AI products,
data, sales costs, working capital, debt, and dilution from revenue, adjusted EBITDA,
free cash flow, guidance, and buybacks. Taboola remains qualified, unranked, and
owner-cash-open.

The new [Warby Parker omnichannel eyewear valuation/liquidity workbench](combined-investment-research-warby-parker-omnichannel-eyewear-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct owned-demand eyewear and vision-care lane. It separates active
customers, ARPC, stores, exams, contacts, insurance, tariffs, lens mix, Intelligent
Eyewear, retail expansion, working capital, and dilution from revenue, adjusted EBITDA,
OCF, guidance, and buybacks. Warby Parker remains qualified, unranked, and
owner-cash-open.

The new [GoDaddy small-business digital-presence valuation/liquidity workbench](combined-investment-research-godaddy-smb-digital-presence-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct customer-edge internet lane. It separates domains, hosting, websites,
commerce, payments, subscriptions, customer care, AI tools, bookings, gross payments
volume, working capital, debt, and dilution from revenue, ARR, ARPU, adjusted EBITDA,
free cash flow, guidance, and buybacks. GoDaddy remains qualified, unranked, and
owner-cash-open.

The new [Liberty Global connectivity holding-company valuation/liquidity workbench](combined-investment-research-liberty-global-connectivity-holding-company-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct international fixed-mobile and portfolio-convergence lane. It
separates subscriber and ARPU economics, network investment, JV distributions, listed
stakes, infrastructure monetization, asset sales, debt, portfolio governance, and
dilution from revenue, connections, adjusted metrics, OCF, guidance, and repurchases.
Liberty Global remains qualified, unranked, and owner-cash-open.

The new [Wyndham economy and midscale franchise valuation/liquidity workbench](combined-investment-research-wyndham-economy-midscale-franchise-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct everyday-traveler lodging lane. It separates franchise fees, RevPAR,
room growth, pipeline quality, ancillary revenue, franchisee health, FeePAR, fee
deferrals, debt, and dilution from rooms, pipeline, adjusted EBITDA, FCF, and capital
returns. Wyndham remains qualified, unranked, and owner-cash-open.

The new [APi Group safety and specialty-services valuation/liquidity workbench](combined-investment-research-api-group-safety-specialty-services-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct compliance and infrastructure-services lane. It separates recurring
inspection, monitoring, project execution, backlog, field labor, acquisitions, cash
conversion, debt, and dilution from revenue, adjusted EBITDA, backlog, adjusted FCF,
and guidance. APi Group remains qualified, unranked, and owner-cash-open.

The new [Kohl’s department-store turnaround valuation/liquidity workbench](combined-investment-research-kohls-department-store-turnaround-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct pressured-retail lane. It separates department-store traffic,
comparable sales, inventory and markdowns, Sephora, loyalty and credit, omnichannel
fulfillment, leases, debt, and dilution from sales, EPS, operating cash flow, and
guidance. Kohl’s remains qualified, unranked, and owner-cash-open.

The new [Sirius XM paid audio and Pandora valuation/liquidity workbench](combined-investment-research-siriusxm-paid-audio-pandora-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct direct-billed audio lane. It separates paid subscribers, churn, in-car
distribution, premium content, Pandora advertising and subscriptions, podcasting,
royalties, free cash flow, debt, and dilution from revenue, adjusted EBITDA, audience
scale, and capital returns. Sirius XM remains qualified, unranked, and owner-cash-open.

The new [iHeartMedia audio and podcast attention valuation/liquidity workbench](combined-investment-research-iheart-audio-podcast-attention-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct cross-platform audio lane. It separates broadcast radio, podcasts,
digital audio, events, audience scale, programmatic selling, data and attribution,
political revenue, non-cash trade, liquidity, leverage, and dilution from revenue,
adjusted EBITDA, FCF, and podcast growth. iHeartMedia remains qualified, unranked,
and owner-cash-open.

The new [Nexxen CTV, programmatic, and data valuation/liquidity workbench](combined-investment-research-nexxen-ctv-programmatic-data-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct ad-infrastructure lane. It separates DSP and SSP economics, CTV
inventory, ACR data, smart-TV home-screen activation, data licensing, partner
concentration, privacy, cloud costs, cash, debt, and dilution from programmatic
revenue, contribution ex-TAC, adjusted EBITDA, and guidance. Nexxen remains
qualified, unranked, and owner-cash-open.

The new [Clear Channel Outdoor physical attention valuation/liquidity workbench](combined-investment-research-clear-channel-outdoor-physical-attention-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct place-based advertising and infrastructure lane. It separates
billboards, transit, airports, street furniture, digital conversion, advertiser
collection, municipal contracts, capex, asset sales, merger consideration, interest,
debt, and dilution from revenue, adjusted EBITDA, AFFO, and merger value. Clear
Channel remains qualified, unranked, and owner-cash-open.

The new [Scholastic children’s reading and school-channel valuation/liquidity workbench](combined-investment-research-scholastic-childrens-reading-school-channel-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct children’s attention and education-interface lane. It separates Book
Fairs, Book Clubs, Trade, Education, Entertainment, school and family relationships,
franchise IP, sale-leasebacks, capital returns, debt, and dilution from revenue,
adjusted EBITDA, FCF, and repurchases. Scholastic remains qualified, unranked, and
owner-cash-open.

The new [Sunstone hotel redevelopment REIT valuation/liquidity workbench](combined-investment-research-sunstone-hotel-redevelopment-reit-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct concentrated lodging-owner lane. It separates property RevPAR,
occupancy, ADR, renovations, redevelopment ramps, asset sales, hotel capex, debt,
dividends, buybacks, and dilution from revenue, Adjusted EBITDAre, FFO, guidance, and
portfolio value. Sunstone remains qualified, unranked, and owner-cash-open.

The new [Brady workplace identification and safety valuation/liquidity workbench](combined-investment-research-brady-workplace-identification-safety-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct compliance-workflow lane. It separates labels, signage, printers,
software, lockout-tagout, safety devices, regional mix, product innovation,
acquisitions, working capital, debt, and dilution from sales, organic growth,
adjusted EPS, OCF, and FCF. Brady remains qualified, unranked, and owner-cash-open.

The new [Omnicom integrated advertising and attention valuation/liquidity workbench](combined-investment-research-omnicom-integrated-advertising-attention-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct agency-workflow lane. It separates client budgets, media pass-through,
creative labor, data and identity, AI measurement, IPG integration, talent retention,
restructuring, debt, and dilution from organic growth, adjusted EBITA, EPS, FCF, and
merger synergies. Omnicom remains qualified, unranked, and owner-cash-open.

The new [Wiley authoritative knowledge and AI licensing valuation/liquidity workbench](combined-investment-research-wiley-authoritative-knowledge-ai-licensing-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct trusted-knowledge platform lane. It separates Research and Learning,
institutional subscriptions, open access, AI licensing, rights ownership, recurring
contracts, editorial investment, portfolio simplification, debt, and dilution from
AI revenue, adjusted EBITDA, EPS, OCF, and FCF. Wiley remains qualified, unranked,
and owner-cash-open.

The new [CRH connected infrastructure materials valuation/liquidity workbench](combined-investment-research-crh-connected-infrastructure-materials-valuation-liquidity-workbench-2026-09-18.md)
adds a multinational infrastructure-materials allocator distinct from aggregates-only
operators. It separates roads, water, utility products, pricing, portfolio churn,
Arcosa funding, residential weakness, capex, net debt, and dilution from revenue,
EBITDA, margins, FCF, and acquisition proceeds. CRH remains qualified, unranked, and
owner-cash-open.

The new [Shentel regional fiber buildout valuation/liquidity workbench](combined-investment-research-shentel-regional-fiber-buildout-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct local-connectivity build lane. It separates homes passed, penetration,
Glo Fiber additions, incumbent broadband runoff, grants, carrier/backhaul exposure,
capex, debt, and dilution from revenue, adjusted EBITDA, guidance, OCF, and fiber
growth. Shentel remains qualified, unranked, and owner-cash-open.

The new [Teck diversified metals and copper-growth valuation/liquidity workbench](combined-investment-research-teck-diversified-metals-copper-growth-valuation-liquidity-workbench-2026-09-18.md)
adds a mixed industrial-metals lane. It separates copper grades and production, QB
reliability, zinc and Trail smelting, steelmaking coal, critical-minerals processing,
Anglo Teck merger execution, mine replacement, capex, net cash, debt, and dilution
from production, EBITDA, OCF, FCF, and merger synergies. Teck remains qualified,
unranked, and owner-cash-open.

The new [Kraft Heinz packaged-food turnaround valuation/liquidity workbench](combined-investment-research-kraft-heinz-packaged-food-turnaround-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct center-store brand-repair lane. It separates volume and share,
price/value architecture, marketing and R&D reinvestment, affordability, commodity
and tariff pressure, dividend funding, debt, and dilution from organic sales, adjusted
earnings, FCF, and guidance. Kraft Heinz remains qualified, unranked, and
owner-cash-open.

The new [Avanos specialty clinical-supply valuation/liquidity workbench](combined-investment-research-avanos-specialty-clinical-supply-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct provider-channel clinical-supply lane. It separates enteral nutrition,
neonatal care, pain management, procedure utilization, hospital/distributor routing,
transformation savings, the pending take-private, working capital, debt, and dilution
from revenue, adjusted EPS, adjusted EBITDA, OCF, guidance, and sale consideration.
Avanos remains qualified, unranked, and owner-cash-open.

The new [Allegion physical access and security valuation/liquidity workbench](combined-investment-research-allegion-physical-access-security-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct building-security lane. It separates installed access systems,
electronics and software adoption, Americas non-residential demand, regional mix,
productivity, warranty, acquisition effects, debt, and dilution from revenue,
adjusted EPS, available cash flow, and guidance. Allegion remains qualified,
unranked, and owner-cash-open.

The new [Martin Marietta aggregates and infrastructure valuation/liquidity workbench](combined-investment-research-martin-marietta-aggregates-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct physical-materials lane. It separates local quarry scarcity, freight,
price per ton, portfolio reshaping, QUIKRETE purchase-accounting noise, New Frontier
capacity, residential weakness, infrastructure demand, borrowing capacity, and diluted
common residual from shipments, EBITDA, OCF, FCF, and acquisition proceeds. Martin
Marietta remains qualified, unranked, and owner-cash-open.

The new [Southwest low-cost airline transformation valuation/liquidity workbench](combined-investment-research-southwest-low-cost-airline-transformation-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct airline-transformation lane. It separates base fares, bags,
assigned and extra-legroom seating, Rapid Rewards, managed-business revenue,
fleet, utilization, fuel, labor, maintenance, airport commitments, technology,
debt, and diluted common residual. Passengers, revenue, unit revenue, adjusted
EBIT, OCF, FCF, loyalty members, and repurchases remain diagnostic until
collection, fleet, transformation, and per-share cash joins are evidenced.

The new [New York Times trust, subscription, and bundle valuation/liquidity workbench](combined-investment-research-nyt-trust-subscription-bundle-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct direct-information lane. It separates subscriptions, newsroom
investment, The Athletic, Audio, Cooking, Games, Wirecutter, advertising,
affiliate and licensing revenue, content rights, churn, product bundles, debt,
and diluted common residual. Subscribers, ARPU, revenue, adjusted earnings,
OCF, FCF, and ad growth remain diagnostic until collection, retention, content,
reinvestment, and per-share cash joins are evidenced.

The new [Loews subsidiary allocator valuation/liquidity workbench](combined-investment-research-loews-subsidiary-allocator-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific holding-company lane. It separates CNA,
Boardwalk Pipelines, Loews Hotels, Altium Packaging, subsidiary distributions,
insurance reserves, energy infrastructure, hospitality, packaging, parent
liquidity, debt, and diluted common residual. Subsidiary earnings, asset values,
OCF, dividends, and repurchases remain diagnostic until legal-entity cash,
reinvestment, claims, and per-share cash joins are evidenced.

The new [Cigna benefits and pharmacy-services valuation/liquidity workbench](combined-investment-research-cigna-benefits-pharmacy-services-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific payer-and-services lane. It separates Cigna
Healthcare, Evernorth, pharmacy and specialty services, employer and government
lives, medical-cost trend, rebates, claims reserves, client retention, capital,
debt, and diluted common residual. Covered lives, revenue, adjusted earnings,
OCF, FCF, and repurchases remain diagnostic until claims, rebate, collection,
capital, and per-share cash joins are evidenced.

The new [Hilton asset-light lodging and loyalty valuation/liquidity workbench](combined-investment-research-hilton-asset-light-lodging-loyalty-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific hospitality lane. It separates franchising,
management, RevPAR, room additions, pipeline conversion, Hilton Honors, owner
economics, digital booking, guarantees, debt, and diluted common residual.
Rooms, pipeline, RevPAR, adjusted EBITDA, OCF, FCF, and buybacks remain
diagnostic until fee collection, owner funding, opening, reinvestment, and
per-share cash joins are evidenced.

The new [GEO outsourced secure-services valuation/liquidity workbench](combined-investment-research-geo-outsourced-secure-services-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct institutional-capacity lane. It separates secure facilities,
processing, reentry, transportation, electronic monitoring, case management,
healthcare, government contracts, idle capacity, labor, debt, claims, and
diluted common residual. Beds, participants, revenue, adjusted EBITDA, OCF,
FCF, guidance, and repurchases remain diagnostic until contract, staffing,
capacity, claims, and per-share cash joins are evidenced.

The new [Regeneron concentrated-biologics valuation/liquidity workbench](combined-investment-research-regeneron-concentrated-biologics-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific biotech lane. It separates Dupixent, EYLEA,
other franchises, label expansion, clinical development, acquired IPR&D,
manufacturing, payer access, patent and litigation exposure, debt, and diluted
common residual. Product revenue, prescriptions, EPS, adjusted earnings, OCF,
FCF, milestones, and buybacks remain diagnostic until collection, franchise,
pipeline, claims, and per-share cash joins are evidenced.

The new [JPMorgan deposit, credit, and capital valuation/liquidity workbench](combined-investment-research-jpmorgan-deposit-credit-capital-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific money-center-bank lane. It separates deposits,
lending, securities, markets, payments, investment banking, credit losses,
capital and liquidity, technology, legal claims, debt, and diluted common
equity. Deposits, loan growth, revenue, EPS, and repurchases remain diagnostic
until credit, funding, capital, liquidity, and residual joins are evidenced.

The new [Walmart omnichannel ecosystem valuation/liquidity workbench](combined-investment-research-walmart-omnichannel-ecosystem-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct mass-retail ecosystem lane. It separates merchandise,
eCommerce, membership, advertising, marketplace, fulfillment, financial
services, inventory, supplier terms, stores, labor, debt, and diluted common
residual. Revenue, eCommerce, advertising, membership fees, adjusted income,
OCF, FCF, and repurchases remain diagnostic until collection, fulfillment,
reinvestment, and per-share cash joins are evidenced.

The new [BHP copper and bulk-materials portfolio valuation/liquidity workbench](combined-investment-research-bhp-copper-bulk-materials-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific mining allocator lane. It separates copper,
iron ore, potash, production, grades, recoveries, unit costs, mine life,
portfolio recycling, permitting, capex, debt, and diluted common residual.
Production, EBITDA, OCF, FCF, dividends, and divestiture proceeds remain
diagnostic until commodity, project, funding, and per-share cash joins are evidenced.

The new [Fujifilm diversified imaging, materials, and workflow valuation/liquidity workbench](combined-investment-research-fujifilm-diversified-imaging-materials-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct diversified-interface and materials lane. It separates
Healthcare, Electronics, Business Innovation, Imaging, bio-CDMO, semiconductor
materials, workflow renewal, raw materials, fixed-cost absorption, debt, and
diluted common residual. Segment revenue, operating income, OCF, FCF, and
portfolio breadth remain diagnostic until segment collection, capacity,
reinvestment, and per-share cash joins are evidenced.

The new [Costco membership warehouse valuation/liquidity workbench](combined-investment-research-costco-membership-warehouse-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct membership-funded warehouse lane. It separates merchandise
sales, membership fees, renewal, traffic, digitally enabled sales, gasoline,
pharmacy, private label, inventory, supplier terms, real estate, labor, debt,
and diluted common residual. Sales, membership fees, OCF, FCF, and repurchases
remain diagnostic until collection, renewal, inventory, reinvestment, and
per-share cash joins are evidenced.

The new [Franklin Resources hybrid asset-management valuation/liquidity workbench](combined-investment-research-franklin-resources-hybrid-asset-management-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct company-specific asset-management lane. It separates public
markets, ETFs, SMAs, alternatives, private markets, AUM flows, fee rates,
distribution, Western Asset remediation, debt, and diluted common residual.
AUM, inflows, revenue, adjusted earnings, OCF, FCF, and repurchases remain
diagnostic until fee collection, retention, deployment, remediation, and
per-share cash joins are evidenced.

The new [Netflix subscription video and advertising valuation/liquidity workbench](combined-investment-research-netflix-subscription-video-advertising-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct recurring-attention lane. It separates memberships, retention,
pricing, advertising, content commitments, production and licensing,
amortization, regional economics, live and gaming investment, debt, and diluted
common residual. Memberships, viewing hours, revenue, margin, OCF, FCF, and ad
revenue remain diagnostic until collection, content-return, reinvestment, and
per-share cash joins are evidenced.

The new [Labcorp diagnostics and biopharma-laboratory valuation/liquidity workbench](combined-investment-research-labcorp-diagnostics-biopharma-labs-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct healthcare-infrastructure lane. It separates routine and
specialty diagnostics, Biopharma Laboratory Services, specimen volume, payer
collection, trial contracts, central-lab throughput, labor, automation, quality,
acquisitions, debt, and diluted common residual. Test volume, revenue, adjusted
earnings, OCF, FCF, and guidance remain diagnostic until collection, delivery,
reinvestment, and per-share cash joins are evidenced.

The new [Kroger grocery, loyalty, and retail-media valuation/liquidity workbench](combined-investment-research-kroger-grocery-loyalty-retail-media-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct grocery-and-data-platform lane. It separates basket sell-through,
loyalty, Kroger Precision Marketing, eCommerce, pharmacy, fuel, private label,
inventory, supplier terms, stores, debt, and diluted common residual. Sales,
eCommerce growth, retail-media profit, adjusted FIFO profit, OCF, FCF, and
repurchases remain diagnostic until collection, inventory, reinvestment, and
per-share cash joins are evidenced.

The new [Insulet automated insulin-delivery valuation/liquidity workbench](combined-investment-research-insulet-automated-insulin-delivery-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct recurring-therapy and consumables lane. It separates Pods,
software and algorithms, reimbursement, pharmacy access, active-user retention,
CGM integration, manufacturing, quality, clinical gates, debt, and diluted
common residual. Pods shipped, active users, revenue, adjusted income, OCF,
FCF, and guidance remain diagnostic until collection, reimbursement, quality,
reinvestment, and per-share cash joins are evidenced.

The new [Teva generics and innovative-pharma transition valuation/liquidity workbench](combined-investment-research-teva-generics-innovative-pharma-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct global drug-access and portfolio-transition lane. It separates
generics, biosimilars, innovative brands, manufacturing, R&D, patent and
litigation exposure, transformation, debt, and diluted common residual. Product
revenue, prescriptions, adjusted EBITDA, guidance, OCF, FCF, and milestones
remain diagnostic until collection, launch-return, claims, and per-share cash
joins are evidenced.

The new [Delta network airline and loyalty valuation/liquidity workbench](combined-investment-research-delta-network-airline-loyalty-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct network-airline and payments lane. It separates passenger and
premium economics, SkyMiles, American Express remuneration, award travel, fleet,
fuel, labor, maintenance, deferred revenue, debt, and diluted common residual.
Passenger revenue, loyalty members, adjusted income, OCF, FCF, and partner
remuneration remain diagnostic until collection, award, fleet, and per-share
cash joins are evidenced.

The new [Tenet hospital and ambulatory-care valuation/liquidity workbench](combined-investment-research-tenet-hospital-ambulatory-care-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct provider-system lane. It separates hospitals, outpatient care,
USPI ambulatory surgery, payer mix, acuity, supplemental Medicaid revenue,
labor, facility investment, debt, and diluted common residual. Admissions,
adjusted EBITDA, adjusted FCF, revenue, and portfolio growth remain diagnostic
until collection, reimbursement, reinvestment, and per-share cash joins are evidenced.

The new [Etsy two-sided marketplace and trust infrastructure valuation/liquidity workbench](combined-investment-research-etsy-two-sided-marketplace-valuation-liquidity-workbench-2026-09-18.md)
adds Etsy as a distinct buyer-seller marketplace lane. It separates buyer and seller
liquidity, GMS, take rate, payments, advertising, seller services, discovery, trust
and safety, cross-border shipping, tariffs, AI-mediated commerce, working capital,
debt, and diluted common residual. GMS, active buyers, active sellers, take rate,
revenue, adjusted EBITDA, guidance, and buybacks remain diagnostic until payment,
settlement, retention, trust, and per-share cash joins are evidenced. Etsy remains
qualified, unranked, and owner-cash-open.

The new [Magnite programmatic advertising and CTV valuation/liquidity workbench](combined-investment-research-magnite-programmatic-ctv-valuation-liquidity-workbench-2026-09-18.md)
adds Magnite as a distinct sell-side advertising infrastructure lane. It separates
CTV from DV+, contribution ex-TAC from gross billings and traffic-acquisition
pass-throughs, publisher and buyer relationships, take rates, receivables, AI and
agentic tooling, regulation, acquisitions, debt, and diluted common residual.
Gross revenue, contribution, CTV growth, adjusted EBITDA, FCF, guidance, and buybacks
remain diagnostic until supply-path, collection, take-rate, platform-cost, and
per-share cash joins are evidenced. Magnite remains qualified, unranked, and
owner-cash-open.

The new [Epson office-edge and precision-hardware valuation/liquidity workbench](combined-investment-research-epson-office-edge-precision-hardware-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct installed-base hardware lane. It separates printers, ink and
consumables, office fleets, projectors, industrial printing, robotics, wearables,
tariffs, energy efficiency, impairment, capex, and dilution from revenue, business
profit, shipments, adjusted metrics, guidance, and buybacks. Epson remains qualified,
unranked, and owner-cash-open.

The new [Con Edison urban regulated utility valuation/liquidity workbench](combined-investment-research-con-ed-urban-regulated-utility-valuation-liquidity-workbench-2026-09-18.md)
adds Con Edison as a distinct dense-urban regulated-utility lane. It separates
electric, gas, steam, transmission, and holding-company activity, then tests rate-
base recovery, customer collections, affordability, reliability, resilience,
substations, capital programs, forward equity, debt, and diluted common residual.
Utility EPS, rate-base growth, capex, OCF, guidance, dividends, and share issuance
remain diagnostic until recovery, collection, financing, and per-share cash joins are
evidenced. Con Edison remains qualified, unranked, and owner-cash-open.

The new [Chewy autoship and pet-care commerce valuation/liquidity workbench](combined-investment-research-chewy-autoship-pet-care-valuation-liquidity-workbench-2026-09-18.md)
adds Chewy as a distinct digital pet-care and replenishment lane. It separates
merchandise, Autoship, pharmacy and prescriptions, active customers, net sales per
customer, fulfillment, inventory, customer acquisition, service attachment, debt,
and diluted common residual. Active customers, Autoship share, net sales, adjusted
EBITDA, FCF, guidance, and buybacks remain diagnostic until retention, collection,
fulfillment, pharmacy, and per-share cash joins are evidenced. Chewy remains
qualified, unranked, and owner-cash-open.

The new [SBA Communications tower-leasing valuation/liquidity workbench](combined-investment-research-sba-tower-leasing-valuation-liquidity-workbench-2026-09-18.md)
adds SBA as a distinct clean tower-leasing lane. It separates recurring site
leasing, domestic and international towers, carrier amendments, tenant density,
land control, churn, FX, acquisitions, AFFO, capex, debt, REIT distributions, and
diluted common residual. Site count, mobile-data growth, AFFO, adjusted EBITDA,
backlog, guidance, and dividends remain diagnostic until tower-level collection,
land, capital, and per-share cash joins are evidenced. SBA remains qualified,
unranked, and owner-cash-open.

The new [Macy's omnichannel portfolio and retail-credit valuation/liquidity workbench](combined-investment-research-macys-omnichannel-portfolio-valuation-liquidity-workbench-2026-09-18.md)
adds Macy's as a distinct department-store portfolio-repair lane. It separates
Macy's, Bloomingdale's, Bluemercury, merchandise sell-through, digital and
marketplace activity, Macy's Media Network, credit-card revenue, inventory,
markdowns, stores, leases, real estate, debt, and diluted common residual.
Comparable sales, adjusted EBITDA, credit-card revenue, media revenue, OCF, guidance,
and buybacks remain diagnostic until sell-through, credit, collection, lease, and
per-share cash joins are evidenced. Macy's remains qualified, unranked, and
owner-cash-open.

The new [Becton Dickinson institutional workflow valuation/liquidity workbench](combined-investment-research-becton-dickinson-institutional-workflow-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct scaled clinical-workflow lane. It separates medication delivery,
specimen management, connected care, prefillable drug delivery, interventional
products, the Waters perimeter change, debt, repurchases, quality spending, and
dilution from revenue, adjusted EPS, segment growth, OCF, guidance, and repurchases.
BD remains qualified, unranked, and owner-cash-open.

The new [Church & Dwight routine-use brands and portfolio valuation/liquidity workbench](combined-investment-research-church-dwight-routine-use-brands-valuation-liquidity-workbench-2026-09-18.md)
adds Church & Dwight as a distinct narrower household and personal-care platform.
It separates routine-use sell-through, retailer and eCommerce collections, brand
support, innovation, input costs, portfolio pruning, tuck-in acquisitions, inventory,
debt, and diluted common residual. Organic growth, online mix, adjusted EPS, OCF,
guidance, and buybacks remain diagnostic until sell-through, collection, acquisition-
return, and per-share cash joins are evidenced. Church & Dwight remains qualified,
unranked, and owner-cash-open.

The new [Bank of America deposit, credit, and capital valuation/liquidity workbench](combined-investment-research-bank-of-america-deposit-credit-valuation-liquidity-workbench-2026-09-18.md)
adds Bank of America as a distinct money-center-bank lane. It separates deposit
funding, loan and lease growth, net interest income, markets and fee businesses,
credit losses, securities duration, liquidity, capital ratios, regulatory constraints,
technology, legal claims, capital return, and diluted common equity. Deposits, loan
growth, revenue, EPS, bank OCF, guidance, and buybacks remain diagnostic until asset
quality, capital, funding, and per-share cash joins are evidenced. Bank of America
remains qualified, unranked, and owner-cash-open.

The new [National CineMedia physical-attention and cinema advertising valuation/liquidity workbench](combined-investment-research-national-cinemedia-physical-attention-valuation-liquidity-workbench-2026-09-18.md)
adds National CineMedia as a distinct synchronized physical-attention lane. It
separates cinema-screen inventory, exhibitor relationships, attendance, advertiser
demand, revenue per attendee, measurement, movie-slate timing, transformation,
leases, debt, and diluted common residual. Attendance, revenue, adjusted OIBDA,
audience reach, cost savings, and guidance remain diagnostic until advertiser
collection, exhibitor settlement, slate, debt, and per-share cash joins are
evidenced. National CineMedia remains qualified, unranked, and owner-cash-open.

The new [Sun Country hybrid airline and cargo valuation/liquidity workbench](combined-investment-research-sun-country-hybrid-airline-cargo-valuation-liquidity-workbench-2026-09-18.md)
adds Sun Country as a distinct hybrid fleet-utilization lane. It separates scheduled
passenger, charter, and Amazon cargo flying, then tests fleet and crew utilization,
seasonality, fuel, labor, aircraft ownership and leases, maintenance, customer
concentration, merger consideration, debt, and diluted common residual. Passengers,
departures, cargo revenue, adjusted EBITDA, OCF, and merger value remain diagnostic
until collection, utilization, maintenance, financing, and per-share cash joins are
evidenced. Sun Country remains qualified, unranked, and owner-cash-open.

The new [Alnylam RNAi therapeutics and franchise valuation/liquidity workbench](combined-investment-research-alnylam-rnai-therapeutics-valuation-liquidity-workbench-2026-09-18.md)
adds Alnylam as a distinct commercial RNAi therapeutics lane. It separates TTR and
rare-franchise product collections from diagnosis, reimbursement, label expansion,
partner and royalty economics, launch cost, pipeline trials, manufacturing, debt,
claims, and diluted common residual. Product revenue, prescriptions, guidance,
milestones, profitability, and buybacks remain diagnostic until reimbursement,
collection, persistence, pipeline-return, and per-share cash joins are evidenced.
Alnylam remains qualified, unranked, and owner-cash-open.

The new [First Solar thin-film manufacturing and contracted-energy-hardware valuation/liquidity workbench](combined-investment-research-first-solar-thin-film-manufacturing-valuation-liquidity-workbench-2026-09-18.md)
adds First Solar as a distinct utility-scale energy-hardware manufacturing lane.
It separates thin-film modules, factory ramp, contracted backlog, customer deposits,
delivery and termination risk, domestic policy support, third-party volume, working
capital, underutilization, capex, and diluted common residual. Gigawatts, module
volume, adjusted EBITDA, tax credits, net cash, guidance, and buybacks remain
diagnostic until acceptance, policy-credit, factory, collection, and per-share cash
joins are evidenced. First Solar remains qualified, unranked, and owner-cash-open.

The new [Valmont utility structures, coatings, and irrigation valuation/liquidity workbench](combined-investment-research-valmont-utility-structures-coatings-valuation-liquidity-workbench-2026-09-18.md)
adds Valmont as a distinct physical-components and agricultural-productivity lane.
It separates utility structures, coatings, telecommunications, irrigation, water,
steel and tariff exposure, backlog, ConcealFab, portfolio exits, claims, debt, and
diluted common residual. Backlog, infrastructure demand, adjusted operating income,
guidance, OCF, and buybacks remain diagnostic until acceptance, collection,
capacity-return, claim, and per-share cash joins are evidenced. Valmont remains
qualified, unranked, and owner-cash-open.

The new [D.R. Horton homebuilder and housing-finance valuation/liquidity workbench](combined-investment-research-dr-horton-homebuilder-valuation-liquidity-workbench-2026-09-18.md)
adds D.R. Horton as a distinct direct homebuilding lane. It separates closings,
orders, cancellations, incentives, land and lot control, construction-cycle cash,
rental operations, Forestar, mortgage and title activity, inventory, debt, and
diluted common residual. Orders, volume, revenue, operating cash flow, EPS, and
repurchases remain diagnostic until delivery, collection, inventory, financing, and
per-share cash joins are evidenced. D.R. Horton remains qualified, unranked, and
owner-cash-open.

The new [PubMatic sell-side ad-tech valuation/liquidity workbench](combined-investment-research-pubmatic-sell-side-adtech-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct supply-path advertising lane. It separates publisher settlement,
demand quality, CTV/mobile/app mix, impressions, AI-powered deals, platform
concentration, working capital, repurchases, and dilution from revenue, adjusted
EBITDA, free cash flow, guidance, and buybacks. PubMatic remains qualified, unranked,
and owner-cash-open.

The new [Medpace clinical-trial infrastructure valuation/liquidity workbench](combined-investment-research-medpace-clinical-trial-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
adds Medpace as a distinct outsourced clinical-development lane. It separates
trial design, patient and site execution, regulatory coordination, sponsor awards,
backlog conversion, employee capacity, study costs, working capital, claims, and
diluted common residual. Awards, backlog, book-to-bill, revenue, EBITDA, and
repurchases remain diagnostic until delivery, collection, reinvestment, claim, and
per-share cash joins are evidenced. Medpace remains qualified, unranked, and
owner-cash-open.

The new [UPS parcel-network and logistics valuation/liquidity workbench](combined-investment-research-ups-parcel-network-valuation-liquidity-workbench-2026-09-18.md)
adds UPS as a distinct physical parcel-network lane, separate from freight
brokerage. It tests package density, mix, labor, aircraft and vehicle assets,
automation, Amazon concentration, network redesign, transformation charges, capex,
leases, debt, and diluted common residual. Package volume, adjusted operating
profit, guidance, operating cash flow, and buybacks remain diagnostic until density,
collection, transformation, reinvestment, and per-share cash joins are evidenced.
UPS remains qualified, unranked, and owner-cash-open.

The new [Nutrien agricultural-inputs and crop-cycle valuation/liquidity workbench](combined-investment-research-nutrien-agricultural-inputs-valuation-liquidity-workbench-2026-09-18.md)
adds Nutrien as a distinct food-system and agricultural-inputs lane. It separates
potash, nitrogen, phosphate, and retail agronomy, then tests fertilizer prices,
natural-gas exposure, mine and plant reliability, grower credit, inventory,
portfolio simplification, capex, debt, and diluted common residual. Production,
adjusted EBITDA, dividends, repurchases, and divestiture proceeds remain diagnostic
until collection, reinvestment, claim, and per-share cash joins are evidenced.
Nutrien remains qualified, unranked, and owner-cash-open.

The new [Zebra enterprise data-capture and workflow valuation/liquidity workbench](combined-investment-research-zebra-enterprise-data-capture-valuation-liquidity-workbench-2026-09-18.md)
adds Zebra as a distinct frontline-enterprise workflow lane. It separates
Connected Frontline from Asset Visibility and Automation, then tests installed
devices, supplies, services, software, channel inventory, customer modernization,
Elo and Photoneo integration, working capital, debt, and diluted common residual.
Revenue, segment growth, adjusted earnings, device volume, and buybacks remain
diagnostic until collection, reinvestment, acquisition-return, and per-share cash
joins are evidenced. Zebra remains qualified, unranked, and owner-cash-open.

The new [franchise and conversion valuation/liquidity workbench](combined-investment-research-choice-hotels-franchise-conversion-valuation-liquidity-workbench-2026-09-18.md)
adds Choice Hotels as a distinct practical-lodging franchise lane. It separates
franchise fees, conversions, extended stay, RevPAR, owner economics, pipeline,
franchisee lending, debt, and dilution from rooms, agreements awarded, adjusted
EBITDA, guidance, and buybacks. Choice remains qualified, unranked, and owner-cash-open.

The new [packaging platform valuation/liquidity workbench](combined-investment-research-sonoco-packaging-platform-valuation-liquidity-workbench-2026-09-18.md)
adds Sonoco as a distinct multi-format packaging lane. It separates Consumer
Packaging, Industrial Paper Packaging, paperboard, metal, recycled fiber, plant
utilization, price-cost, Eviosys, ThermoSafe, capex, debt, and dilution from sales,
adjusted EBITDA, guidance, operating cash flow, and buybacks. Sonoco remains
qualified, unranked, and owner-cash-open.

The new [liquid biopsy and screening valuation/liquidity workbench](combined-investment-research-guardant-liquid-biopsy-screening-valuation-liquidity-workbench-2026-09-18.md)
adds Guardant as a distinct precision-oncology information lane. It separates
oncology, Shield screening, biopharma/data, test volume, reimbursement, clinical
validation, lab capacity, cash burn, debt, and dilution from revenue growth,
guidance, adjusted metrics, and buybacks. Guardant remains qualified, unranked,
and owner-cash-open.

The new [local-news and digital transition valuation/liquidity workbench](combined-investment-research-gannett-local-news-digital-transition-valuation-liquidity-workbench-2026-09-18.md)
adds Gannett/USA TODAY Co. as a distinct local-information lane. It separates print,
digital subscriptions, advertising, LocaliQ, audience traffic, AI licensing,
restructuring, pension/debt claims, and dilution from digital mix, visitors,
adjusted EBITDA, guidance, and turnaround claims. Gannett remains qualified,
unranked, and owner-cash-open.

The new [healthcare education valuation/liquidity workbench](combined-investment-research-adtalem-covista-healthcare-education-valuation-liquidity-workbench-2026-09-18.md)
adds Adtalem/Covista as a distinct regulated workforce-education lane. It separates
Walden, Chamberlain, Medical and Veterinary, enrollment, revenue per student,
outcomes, clinical sites, faculty, regulation, debt, and dilution from adjusted
EBITDA, guidance, program growth, and buybacks. Adtalem/Covista remains qualified,
unranked, and owner-cash-open.

The new [destination gaming and digital valuation/liquidity workbench](combined-investment-research-mgm-destination-gaming-digital-valuation-liquidity-workbench-2026-09-18.md)
adds MGM Resorts as a distinct diversified resort-platform lane. It separates Las
Vegas, regional gaming, Macau, MGM Digital, BetMGM affiliates, occupancy, casino
hold, resort capex, Osaka development, debt, claims, and dilution from revenue,
adjusted EBITDA, guidance, property sales, and buybacks. MGM remains qualified,
unranked, and owner-cash-open.

The new [staffing and Protiviti valuation/liquidity workbench](combined-investment-research-robert-half-staffing-protiviti-valuation-liquidity-workbench-2026-09-18.md)
adds Robert Half as a distinct labor-market intermediary lane. It separates contract
talent, permanent placement, Protiviti, bill rates, utilization, wages, collections,
receivables, restructuring, debt, dividends, and dilution from revenue, sequential
growth, adjusted EPS, guidance, and capital returns. Robert Half remains qualified,
unranked, and owner-cash-open.

The new [furnace packaging valuation/liquidity workbench](combined-investment-research-oi-glass-furnace-packaging-valuation-liquidity-workbench-2026-09-18.md)
adds O-I Glass as a distinct glass-container manufacturing lane. It separates
Americas and Europe, furnaces, cullet, energy, utilization, regional pricing, Fit to
Win, impairment, capex, debt, claims, and dilution from volume, segment operating
profit, adjusted EBITDA, guidance, and buybacks. O-I Glass remains qualified,
unranked, and owner-cash-open.

The new [copper restart valuation/liquidity workbench](combined-investment-research-first-quantum-copper-restart-valuation-liquidity-workbench-2026-09-18.md)
adds First Quantum as a distinct concentrated-mining lane. It separates Kansanshi,
Sentinel, Enterprise, Cobre Panama, nickel, grades, throughput, stockpiles, hedges,
fuel, FX, capex, jurisdiction, debt, and dilution from production, copper price,
EBITDA, guidance, reserves, and buybacks. First Quantum remains qualified,
unranked, and owner-cash-open.

The new [AI agency platform valuation/liquidity workbench](combined-investment-research-stagwell-ai-agency-platform-valuation-liquidity-workbench-2026-09-18.md)
adds Stagwell as a distinct challenger-agency lane. It separates net revenue,
client retention, digital transformation, advocacy, The Machine, Marketing Cloud,
data, labor, acquisitions, working capital, debt, and dilution from gross revenue,
new business, adjusted EBITDA, guidance, AI claims, and buybacks. Stagwell remains
qualified, unranked, and owner-cash-open.

The new [print and materials valuation/liquidity workbench](combined-investment-research-eastman-kodak-print-materials-valuation-liquidity-workbench-2026-09-18.md)
adds Eastman Kodak as a distinct legacy-imaging and industrial-substrate lane. It
separates Print, AM&C, film, workflow, silver and aluminum, inventory, restructuring,
legacy claims, term debt, and dilution from revenue, gross profit, operational EBITDA,
guidance, and turnaround claims. Kodak remains qualified, unranked, and owner-cash-open.

The new [audience measurement valuation/liquidity workbench](combined-investment-research-comscore-audience-measurement-valuation-liquidity-workbench-2026-09-18.md)
adds Comscore as a distinct measurement-infrastructure lane. It separates
cross-platform, local-TV, Proximic, syndicated panels, data rights, customer
renewal, recapitalization, preferred claims, debt, and dilution from revenue,
adjusted EBITDA, guidance, and product-growth claims. Comscore remains qualified,
unranked, and owner-cash-open.

The new [cruise, destination, and wallet valuation/liquidity workbench](combined-investment-research-carnival-cruise-destination-wallet-valuation-liquidity-workbench-2026-09-18.md)
adds Carnival as a distinct capital-heavy travel lane. It separates bookings,
customer deposits, occupancy, ticket yield, onboard and pre-cruise spend, fuel,
fleet capex, debt, legal structure, and dilution from revenue, adjusted EBITDA,
guidance, and buybacks. Carnival remains qualified, unranked, and owner-cash-open.

The new [antisense commercial platform valuation/liquidity workbench](combined-investment-research-ionis-antisense-commercial-platform-valuation-liquidity-workbench-2026-09-18.md)
adds Ionis as a distinct biotechnology IP-monetization lane. It separates owned
products, royalties, collaborations, milestones, TRYNGOLZA, clinical trials, launch
costs, partner economics, cash burn, debt, and dilution from revenue, guidance,
pipeline catalysts, adjusted metrics, and buybacks. Ionis remains qualified,
unranked, and owner-cash-open.

The new [rebar and construction valuation/liquidity workbench](combined-investment-research-commercial-metals-rebar-construction-valuation-liquidity-workbench-2026-09-18.md)
adds Commercial Metals as a distinct recycled-steel and construction-solutions lane.
It separates scrap spreads, rebar, fabrication, precast, backlog, acquisitions,
capex, leverage, Europe/CBAM exposure, and dilution from steel margins, adjusted
EBITDA, guidance, and buybacks. Commercial Metals remains qualified, unranked, and
owner-cash-open.

The new [metals service-center valuation/liquidity workbench](combined-investment-research-reliance-metals-service-center-valuation-liquidity-workbench-2026-09-18.md)
adds Reliance as a distinct downstream metals-distribution lane. It separates tons,
value-added processing, mill purchases, price and FIFO effects, inventory, branch
density, acquisitions, capex, debt, capital returns, and dilution from sales,
adjusted EPS, guidance, and buybacks. Reliance remains qualified, unranked, and
owner-cash-open.

The new [aggregates and contracting valuation/liquidity workbench](combined-investment-research-knife-river-aggregates-contracting-valuation-liquidity-workbench-2026-09-18.md)
adds Knife River as a distinct reserve-and-project-conversion lane. It separates
aggregate tons, reserve life, downstream pull-through, public backlog, pricing,
contracting, acquisitions, capex, leverage, and dilution from revenue, adjusted
EBITDA, guidance, and public-funding share. Knife River remains qualified,
unranked, and owner-cash-open.

The new [hospice and service-route valuation/liquidity workbench](combined-investment-research-chemed-hospice-rotorooter-valuation-liquidity-workbench-2026-09-18.md)
adds Chemed as a distinct mixed-service healthcare lane. It separates VITAS
admissions, census, acuity, Medicare Cap, clinical labor, and collections from
Roto-Rooter route economics, parent buybacks, consolidated revenue, adjusted EBITDA,
and dilution. Chemed remains qualified, unranked, and owner-cash-open.

The new [drug-delivery components valuation/liquidity workbench](combined-investment-research-west-pharmaceutical-drug-delivery-valuation-liquidity-workbench-2026-09-18.md)
adds West Pharmaceutical as a distinct healthcare physical-interface lane. It
separates HVP Components, delivery systems, customer qualification, sterile
manufacturing, validation, quality, capacity, capex, debt, and dilution from
therapy-driven revenue, adjusted EPS, guidance, and buybacks. West remains
qualified, unranked, and owner-cash-open.

The new [metal fabrication valuation/liquidity workbench](combined-investment-research-mueller-industries-metal-fabrication-valuation-liquidity-workbench-2026-09-18.md)
adds Mueller Industries as a distinct fabricated-components lane. It separates
copper, brass, aluminum, unit volume, price pass-through, hedges, Piping Systems,
Industrial Metals, Climate, acquisitions, capex, debt, and dilution from revenue,
operating income, guidance, adjusted metrics, and repurchases. Mueller remains
qualified, unranked, and owner-cash-open.

The new [rigid packaging valuation/liquidity workbench](combined-investment-research-crown-holdings-rigid-packaging-valuation-liquidity-workbench-2026-09-18.md)
adds Crown Holdings as a distinct global packaging-infrastructure lane. It separates
beverage, food, aerosol, closures, tooling, plant utilization, metal and energy
pass-through, capex, leverage, buybacks, and dilution from volume, adjusted EBITDA,
adjusted FCF, guidance, and capital returns. Crown Holdings remains qualified,
unranked, and owner-cash-open.

The new [specialty distribution valuation/liquidity workbench](combined-investment-research-pool-specialty-distribution-valuation-liquidity-workbench-2026-09-18.md)
adds Pool as a distinct branch-based wholesale lane. It separates maintenance and
repair mix, branch density, supplier purchases, inventory, early buys, receivables
financing, seasonal working capital, capex, debt, and dilution from sales growth,
gross profit, operating cash flow, and repurchases. Pool remains qualified,
unranked, and owner-cash-open.

The new [tower infrastructure valuation/liquidity workbench](combined-investment-research-crown-castle-tower-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
adds Crown Castle as a distinct domestic communications-infrastructure lane. It
separates tower billings, carrier churn, DISH and Sprint effects, fiber and small-cell
disposal, maintenance capital, debt, REIT distributions, and dilution from AFFO,
Adjusted EBITDA, sale proceeds, and dividend capacity. Crown Castle remains
qualified, unranked, and owner-cash-open.

The new [precision diagnostics valuation/liquidity workbench](combined-investment-research-natera-precision-diagnostics-valuation-liquidity-workbench-2026-09-18.md)
adds Natera as a distinct molecular-information lane. It separates Signatera,
Panorama, Horizon, Prospera, payer coverage, test volume, ASP, clinical evidence,
laboratory capacity, reimbursement, collections, debt, and dilution from guidance,
oncology growth, reported revenue, and adjusted metrics. Natera remains qualified,
unranked, and owner-cash-open.

The new [enterprise data cloud and subscription storage valuation/liquidity workbench](combined-investment-research-pure-everpure-enterprise-data-cloud-valuation-liquidity-workbench-2026-09-18.md)
adds Pure/Everpure as a distinct governed-storage lane. It separates flash,
subscription ARR, RPO, Evergreen//One, Enterprise Data Cloud, hybrid-cloud control,
AI data management, 1touch integration, cloud cost, debt, and dilution from
revenue, gross margin, FCF, and buybacks. Pure/Everpure remains qualified,
unranked, and owner-cash-open.

The new [HDD, persistent storage, and data-retention infrastructure valuation/liquidity workbench](combined-investment-research-western-digital-hdd-persistent-storage-valuation-liquidity-workbench-2026-09-18.md)
adds Western Digital as a distinct storage lane. It separates HDD, hyperscale,
persistent data, capacity, utilization, post-Sandisk structure, inventory,
manufacturing, debt, dividends, and dilution from exabyte growth, gross margin,
adjusted EPS, FCF, and customer commitments. Western Digital remains qualified,
unranked, and owner-cash-open.

The new [printed-circuit-board and advanced-interconnect valuation/liquidity workbench](combined-investment-research-ttm-technologies-pcb-interconnect-valuation-liquidity-workbench-2026-09-18.md)
adds TTM Technologies as a distinct hardware-substrate lane. It separates PCBs,
substrates, RF and microelectronics, customer qualification, backlog, book-to-bill,
AI networking, A&D programs, capacity, acquisitions, working capital, debt, and
dilution from revenue, adjusted EBITDA, FCF, and acquisition claims. TTM remains
qualified, unranked, and owner-cash-open.

The new [closed-loop membership, premium payments, and credit valuation/liquidity workbench](combined-investment-research-amex-closed-loop-membership-payments-valuation-liquidity-workbench-2026-09-18.md)
adds American Express as a distinct payments lane. It separates card members,
merchants, billed business, fees, rewards, credit, travel and dining, first-party
data, agentic commerce, funding, CET1, and dilution from revenue, fee growth, EPS,
membership, and buybacks. American Express remains qualified, unranked, and
owner-cash-open.

The new [copper, smelting, and by-product mine-system valuation/liquidity workbench](combined-investment-research-southern-copper-peru-mexico-byproduct-valuation-liquidity-workbench-2026-09-18.md)
adds Southern Copper as a distinct copper-system lane. It separates Peru/Mexico
mine cohorts, copper, molybdenum, zinc, silver, smelting, grades, recoveries,
expansion capex, jurisdiction, debt, and dilution from production, net cash cost,
adjusted EBITDA, FCF, and buybacks. Southern Copper remains qualified, unranked,
and owner-cash-open.

The new [live sports, news, affiliate fees, and AVOD valuation/liquidity workbench](combined-investment-research-fox-live-sports-news-avod-valuation-liquidity-workbench-2026-09-18.md)
adds Fox as a distinct national-attention lane. It separates live rights, sports
and news, affiliate fees, advertising, Tubi, FOX One, Roku integration, content
commitments, debt, and dilution from audience, adjusted EBITDA, event-driven ad
spikes, affiliate fees, and buybacks. Fox remains qualified, unranked, and
owner-cash-open.

The new [nuclear and clean-generation platform valuation/liquidity workbench](combined-investment-research-constellation-nuclear-clean-generation-valuation-liquidity-workbench-2026-09-18.md)
adds Constellation as a distinct generation lane. It separates nuclear and clean
fleet, PPAs, merchant sales, Calpine integration, Crane restart, licensing, data-
center co-location, maintenance, debt, and dilution from adjusted earnings,
capacity, PPAs, dividends, and buybacks. Constellation remains qualified, unranked,
and owner-cash-open.

The new [online K–12, career learning, and institutional education valuation/liquidity workbench](combined-investment-research-stride-online-k12-career-learning-valuation-liquidity-workbench-2026-09-18.md)
adds Stride as a distinct institutional-education lane. It separates General
Education, Career Learning, adult and employer programs, enrollment, public funding,
district contracts, curriculum, instructional labor, regulation, debt, and dilution
from revenue per enrollment, adjusted EBITDA, FCF, and buybacks. Stride remains
qualified, unranked, and owner-cash-open.

The new [real-estate services and critical-infrastructure intermediation valuation/liquidity workbench](combined-investment-research-cbre-real-estate-services-critical-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
adds CBRE as a distinct property-services lane. It separates brokerage,
facilities, project management, mortgage, investment management, critical
infrastructure, commissions, subcontractors, working capital, debt, and dilution
from Core EPS, FCF, AUM, transaction volume, and acquisitions. CBRE remains
qualified, unranked, and owner-cash-open.

The new [residential apartment REIT and merger valuation/liquidity workbench](combined-investment-research-avalonbay-residential-apartment-reit-valuation-liquidity-workbench-2026-09-18.md)
adds AvalonBay as a distinct housing lane. It separates rent collection, occupancy,
concessions, same-store NOI, development, maintenance, apartment supply, Equity
Residential merger economics, debt, dividends, and dilution from FFO, Core FFO,
development yield, and share issuance. AvalonBay remains qualified, unranked, and
owner-cash-open.

The new [digital ordering, franchise, and supply-chain valuation/liquidity workbench](combined-investment-research-dominos-digital-ordering-franchise-supply-chain-valuation-liquidity-workbench-2026-09-18.md)
adds Domino's as a distinct restaurant-network lane. It separates digital orders,
franchise royalties, supply-chain throughput, store growth, franchisee health, DPC
Dash remeasurement, debt, and dilution from retail sales, digital penetration,
adjusted EPS, and buybacks. Domino's remains qualified, unranked, and owner-cash-open.

The new [travel marketplace, B2B distribution, and loyalty valuation/liquidity workbench](combined-investment-research-expedia-travel-marketplace-b2b-loyalty-valuation-liquidity-workbench-2026-09-18.md)
adds Expedia as a distinct travel-intermediary lane. It separates B2C, B2B,
agency, merchant, advertising, One Key, supplier settlement, refunds, payment
timing, debt, and dilution from gross bookings, room nights, adjusted EBITDA, FCF,
loyalty adoption, and buybacks. Expedia remains qualified, unranked, and
owner-cash-open.

The new [local broadcasting, retransmission, and political-cycle valuation/liquidity workbench](combined-investment-research-nexstar-local-broadcast-retransmission-valuation-liquidity-workbench-2026-09-18.md)
adds Nexstar as a distinct hybrid-media lane. It separates local stations,
retransmission, political and non-political advertising, NewsNation, The CW,
TEGNA integration, programming costs, debt, and dilution from distribution,
audience, adjusted EBITDA, political advertising, and buybacks. Nexstar remains
qualified, unranked, and owner-cash-open.

The new [specialty retail, loyalty, and brand-repair valuation/liquidity workbench](combined-investment-research-bath-body-works-specialty-retail-brand-repair-valuation-liquidity-workbench-2026-09-18.md)
adds Bath & Body Works as a distinct repair-oriented retail lane. It separates
stores, direct, international, loyalty, product, inventory, markdowns, seasonal
demand, the Consumer First Formula, debt, and dilution from sales, store count,
adjusted EPS, settlement benefits, and buybacks. Bath & Body Works remains
qualified, unranked, and owner-cash-open.

The new [silver-weighted mine portfolio and acquisition valuation/liquidity workbench](combined-investment-research-pan-american-silver-mine-portfolio-valuation-liquidity-workbench-2026-09-18.md)
adds Pan American Silver as a distinct precious-metals lane. It separates silver,
gold, mine cohorts, Juanicipio, reserve and grade, sustaining and growth capex,
jurisdiction, debt, dividends, and dilution from production, AISC, attributable
FCF, and buybacks. Pan American remains qualified, unranked, and owner-cash-open.

The new [paperboard packaging and mill-cycle valuation/liquidity workbench](combined-investment-research-clearwater-paperboard-packaging-valuation-liquidity-workbench-2026-09-18.md)
adds Clearwater Paper as a distinct materials lane. It separates SBS price and
volume, mill operating rates, outages, fiber and energy, restructuring, tissue
divestiture, working capital, liquidity, debt, and dilution from adjusted EBITDA,
cost savings, guidance, and buybacks. Clearwater remains qualified, unranked, and
owner-cash-open.

The new [diversified payments and fee-bank valuation/liquidity workbench](combined-investment-research-us-bancorp-payments-fee-bank-valuation-liquidity-workbench-2026-09-18.md)
adds U.S. Bancorp as a distinct financial-utility lane. It separates deposits,
loans, payments, treasury, trust, fee revenue, credit losses, reserves, CET1,
liquidity, technology, dividends, and dilution from NII, net revenue, EPS, and
buybacks. U.S. Bancorp remains qualified, unranked, and owner-cash-open.

The new [commerce media and AI shopping-interface valuation/liquidity workbench](combined-investment-research-criteo-commerce-media-ai-shopping-valuation-liquidity-workbench-2026-09-18.md)
adds Criteo as a distinct transaction-adjacent attention lane. It separates retail
media, retailer and brand settlement, contribution ex-TAC, client concentration,
AI shopping interfaces, measurement, debt, and dilution from media spend, adjusted
EBITDA, FCF, and partnership announcements. Criteo remains qualified, unranked,
and owner-cash-open.

The new [mobile gaming, live-ops, and direct-billing valuation/liquidity workbench](combined-investment-research-playtika-mobile-gaming-live-ops-valuation-liquidity-workbench-2026-09-18.md)
adds Playtika as a distinct digital-participation lane. It separates title cohorts,
payers, DTC collections, platform fees, live ops, SuperPlay integration and earnout,
marketing, debt, and dilution from revenue, adjusted EBITDA, payer metrics, and
buybacks. Playtika remains qualified, unranked, and owner-cash-open.

The new [open-internet, CTV, and advertising middleware valuation/liquidity workbench](combined-investment-research-teads-open-internet-ctv-adtech-valuation-liquidity-workbench-2026-09-18.md)
adds Outbrain/Teads as a distinct attention-infrastructure lane. It separates
advertiser and publisher settlement, TAC, CTV, measurement, ex-TAC gross profit,
Teads integration, bridge debt, impairment, restructuring, and dilution from
reported revenue, adjusted EBITDA, and adjusted FCF. The lane remains qualified,
unranked, and owner-cash-open.

The new [satellite connectivity and orbital infrastructure valuation/liquidity workbench](combined-investment-research-viasat-satellite-connectivity-orbital-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
adds Viasat as a distinct physical-connectivity lane. It separates aviation,
maritime, government and defense, fixed broadband, satellites, spectrum, launch,
service entry, backlog, RPO, leverage, capex, debt, and dilution from endpoints,
adjusted EBITDA, FCF, and recurring-revenue claims. Viasat remains qualified,
unranked, and owner-cash-open.

The new [learning marketplace and human-capital platform valuation/liquidity workbench](combined-investment-research-coursera-learning-marketplace-human-capital-valuation-liquidity-workbench-2026-09-18.md)
adds Coursera as a distinct education-platform lane. It separates Consumer,
Enterprise, degree and partner economics, learners, subscribers, NRR, Udemy
integration, AI delivery, synergies, working capital, debt, and dilution from
reported revenue, adjusted EBITDA, FCF, and buybacks. Coursera remains qualified,
unranked, and owner-cash-open.

The new [DNS registry control and internet infrastructure valuation/liquidity workbench](combined-investment-research-verisign-dns-registry-control-valuation-liquidity-workbench-2026-09-18.md)
adds VeriSign as a distinct digital-control-point lane. It separates `.com/.net`
registry contracts, domain cohorts, renewal, pricing, deferred revenue, DNS uptime,
cybersecurity, governance, carrier commitments, debt, and dilution from domain
counts, OCF, FCF, and buybacks. VeriSign remains qualified, unranked, and
owner-cash-open.
The next financial-intermediation extension is the [insurance broker/carrier
synthesis](annual-report-insurance-broker-carrier-first-principles-synthesis-pass-1-2026-09-17.md).
It keeps Marsh McLennan and Arthur J. Gallagher's client-access and
acquisition economics separate from Chubb's underwriting, reserve,
reinsurance, policyholder-liability, and regulatory-capital burden. The
FY2025 OCF and claim surfaces are qualified diagnostics, not a broker/carrier
ranking or distributable-cash conclusion.
The current Q2 2026 refresh sharpens the carrier boundary: Chubb reported
`$3.73B` of operating cash, but H1 net unpaid losses were `$71.216B`, gross
unpaid losses `$89.669B`, reinsurance recoverable `$18.453B`, and net losses
paid `$11.353B`; favorable prior-year reserve development of `$584M` is a
normalization input rather than recurring underwriting cash. Premium growth and
adjusted operating cash therefore remain separate from reserve adequacy,
reinsurance collectibility, catastrophe-normalized returns, statutory capital,
and common-owner residual.
The next financial-infrastructure extension is [exchange and information
infrastructure](annual-report-exchange-information-infrastructure-first-principles-synthesis-pass-1-2026-09-17.md).
CME's trading, clearing, and liquidity network is kept separate from S&P
Global's benchmark, ratings, index, and data workflows. FY2025 OCF, capex,
acquisitions, dividends, buybacks, debt, goodwill, and SBC are verified as
company-level diagnostics; clearing collateral, acquisition returns, and
common-owner cash remain unpromoted.
The Q2 2026 refresh adds a sharper cash-quality boundary: CME reported H1
operating cash of `$2.207B`, while its `$138.5B` Federal Reserve cash account
and `$1.545B` decrease in performance-bond/guaranty-fund contributions remain
clearing-liquidity and collateral surfaces rather than unrestricted corporate
cash. S&P Global reported `$2.476B` operating cash and `$2.249B` reported FCF,
but also `$361M` disposition proceeds, `$26M` acquisition cash, `$551M`
intangible amortization, and `$95M` SBC. Volume, market-data growth, and
reported FCF therefore remain separate from organic recurring cash, collateral
risk, acquired-cohort return, and diluted owner cash.
The next materials/energy extension is [integrated oil and gas](annual-report-integrated-oil-gas-first-principles-synthesis-pass-1-2026-09-17.md).
ConocoPhillips' upstream reserve and capital-program model is kept separate
from Exxon's integrated upstream, refining, chemicals, trading, and logistics
model. FY2025 cash, capex, distributions, debt, and reserve/cycle controls are
diagnostics; paid replacement capex, reserve-to-cash durability, project
returns, and common-owner cash remain open.
The next industrial channel extension is the [industrial distribution and
building-materials synthesis](annual-report-industrial-distribution-building-materials-first-principles-synthesis-pass-1-2026-09-17.md).
Core & Main adds waterworks, wastewater, storm drainage, fire protection,
treatment-plant, and smart-utility distribution to the built-environment map.
FY2025 revenue, OCF, receivables, inventory, acquisitions, debt, goodwill, and
dilution are verified company-level controls; municipal funding, collection,
working-capital quality, maintenance versus growth capital, acquired-cohort
return, and common-owner residual remain open. The lane is qualified and
unranked.

The new [built-environment channel valuation/liquidity workbench](combined-investment-research-built-environment-channels-valuation-liquidity-workbench-2026-09-17.md)
extends that route to Watsco, Builders FirstSource, and Ferguson while keeping
Core & Main's waterworks channel distinct. HVAC replacement, homebuilder
prefabrication, contractor repair, and civic water infrastructure are separate
denominators; branch counts, sales, adjusted EBITDA, repair mix, and reported
OCF do not become normalized owner cash until inventory settlement, acquisition
return, maintenance/growth capital, debt, and dilution are joined.

The next industrial-project extension is the [industrial contractors and
project-cash synthesis](annual-report-industrial-contractors-project-cash-first-principles-synthesis-pass-1-2026-09-17.md).
Comfort Systems USA, EMCOR, Sterling Infrastructure, Quanta Services, and
MasTec are separated by installation, utility, site-development, and
infrastructure control points. FY2025 OCF, productive-asset spending,
acquisitions, SBC, and repurchases are verified diagnostics; backlog funding,
billing, collection, cost-to-complete, claims, acquired-cohort return, and
common-owner residual remain open. The lane is qualified and unranked.
The [industrial contractors H1 2026 cash-quality refresh](combined-investment-research-industrial-contractors-h1-2026-cash-quality-refresh-2026-09-17.md)
adds a period-controlled surface for Comfort Systems USA, EMCOR, and Quanta:
H1 OCF of `$1.528B`, `$290M`, and `$1.487B` against productive-asset spending
of `$289M`, `$60M`, and `$451M`. Acquisition outlays were `$163M`, `$95M`, and
`$930M`. These figures sharpen the acquisition and cash-timing tests but do
not prove project collections, maintenance/growth capital, or owner cash.

The [retail latest-Q2 lease-and-tax search boundary](combined-investment-research-retail-latest-q2-2026-lease-tax-search-boundary-2026-09-17.md)
checks the official August 2026 TJX and Target filings and July 2026 Walmart
filing. TJX reports `$1.147B` of H1 operating-lease cash paid; lease
liabilities, noncash lease additions, tax provisions, and accrual movements
remain visible controls, while Target and Walmart do not provide comparable
interim cash-paid lease/tax schedules. This is a searched-negative control for
the missing payment objects—not a zero-payment assumption—and CA-06 remains
partial.

The [retail Q2 2026 working-capital denominator refresh](combined-investment-research-retail-q2-2026-working-capital-denominator-refresh-2026-09-17.md)
adds the latest same-period operating surface: TJX `$3.345B` OCF against
`$1.159B` property spend, Target `$4.519B` against `$2.404B`, and Walmart
`$19.710B` against `$14.181B`. Inventory uses and payable sources are retained
as timing/QoE diagnostics, not double-counted deductions; Walmart's `$5.529B`
management-defined FCF is explicitly not treated as residual owner cash.

The [retail Q2 2026 capex allocation sensitivity](combined-investment-research-retail-q2-2026-capex-allocation-sensitivity-2026-09-17.md)
advances Q-05 without overclassifying spend. Walmart discloses `$1.087B` of
new stores, expansions, and relocations as a growth floor inside `$14.181B`
total H1 property spending; the remaining `$13.094B` is mixed. Target's
`$2.404B` and TJX's `$1.159B` property lines remain unallocated between
maintenance and growth. CA-06 remains partial.

The [retail Q2 2026 inventory/payables normalization](combined-investment-research-retail-q2-2026-inventory-payables-normalization-2026-09-17.md)
joins ending-balance movements with cash-flow changes. The mechanical inventory
less payable uses are `$116M` for TJX, `$261M` for Target, and `$1.492B` for
Walmart, but they are already represented in OCF and are not deducted again.
The bridge improves Q-04 while leaving reversal, supplier-finance settlement,
margin, and normalized owner-cash gates open.

The [retail Q2 2026 supplier-finance obligation refresh](combined-investment-research-retail-q2-2026-supplier-finance-obligation-refresh-2026-09-17.md)
adds a current settlement-perimeter control. Target reports `$3.2B` of
supplier-finance-eligible obligations at August 1, 2026 versus `$3.0B` at
January 31, 2026; Walmart reports `$6.4B` of outstanding supplier-finance
obligations at July 31, 2026 versus `$6.0B` at January 31, 2026. Both filings
distinguish the obligation perimeter from actual early-payment or settlement
cash, so the balances are not subtracted again from OCF. Q-04 is materially
tighter, but supplier-finance settlement remains unproven, TJX has no
comparable note in the reviewed interim packet, and CA-06 remains partial.

The [Target Q2 cash-quality boundary](combined-investment-research-retail-target-q2-2026-cash-quality-boundary-2026-09-17.md)
now adds the supplier-finance lifecycle and financing-claim controls: eligible
obligations increased from `$3.0B` to `$3.2B`, but Target says these are not
actual early payments; H1 accounts payable supplied `$612M` of mixed cash, and
Target repaid `$1.0B` of unsecured debt in April. These figures sharpen timing
and residual-claim analysis without becoming additional OCF deductions.

The [broad technology Q2 2026 cash-quality refresh](combined-investment-research-broad-technology-q2-2026-cash-quality-refresh-2026-09-17.md)
adds current Fortinet and Cloudflare controls. Fortinet reports H1 OCF of
`$2.121B` and FCF of `$1.972B`, alongside `$559.9M` of deferred-revenue
growth, `$154.0M` of SBC, `$972.8M` of repurchases, and `$500M` of senior-note
repayment. Cloudflare reports H1 revenue growth of 35%, OCF of `$275.9M`, and
FCF of `$140.5M`, while gross margin fell from 75% to 72%, SBC was `$274.1M`,
and PP&E plus capitalized-software spending was `$135.4M`. These figures
strengthen the technology control-point and QoE surface but do not promote
billings, RPO, reported FCF, or noncash SBC add-backs to normalized owner cash;
the lane remains qualified and unranked.

The new [internet edge and security valuation/liquidity workbench](combined-investment-research-edge-security-valuation-liquidity-workbench-2026-09-17.md)
now moves Akamai, Zscaler, and Fastly into a separate edge-security lane. It
keeps Akamai's delivery-to-security/CIS transition, Zscaler's cloud-policy
contract surface, and Fastly's programmable-edge concentration distinct. ARR,
RPO, bookings, security growth, and reported FCF remain diagnostic inputs until
capacity cost, collection, retention or usage cohorts, SBC replacement, debt,
and diluted common-owner cash are joined.

The new [participation platform valuation/liquidity workbench](combined-investment-research-participation-platform-valuation-liquidity-workbench-2026-09-17.md)
routes Roblox separately from traffic-control software. DAUs, hours, bookings,
creator exchange fees, virtual-currency timing, trust and safety, age policy,
moderation, platform infrastructure, and diluted shares are treated as one
participation-economy chain; engagement and bookings do not become normalized
owner cash until creator payouts, governance costs, collection, and dilution
are joined.

The new [builder cloud and inference valuation/liquidity workbench](combined-investment-research-builder-cloud-valuation-liquidity-workbench-2026-09-17.md)
routes DigitalOcean separately from edge security and participation platforms.
Builder-cloud access, AI customer ARR, RPO, committed capacity, inference
cost, customer concentration, hardware, support, debt, and diluted shares are
kept in one company-specific chain. ARR, RPO, revenue growth, and reported OCF
remain diagnostic until capacity returns and collection are evidenced.

The [basic materials Q2 2026 cash-quality refresh](combined-investment-research-basic-materials-q2-2026-cash-quality-refresh-2026-09-17.md)
adds current CF Industries, Sherwin-Williams, and West Fraser controls. CF's
`$1.374B` H1 OCF includes `$170M` of litigation proceeds, `$50M` of insurance
proceeds, and substantial tax deposits, while Blue Point capital is partly
partner-funded. Sherwin-Williams generated `$1.487B` of operating cash but used
`$397.6M` in working capital, `$239.5M` through operating lease liabilities,
and `$1.837B` for treasury stock. West Fraser reports `$192M` of Q2 operating
cash against `$159M` of H1 capex. The lane remains cycle-qualified, owner-cash-
open, and unranked.

The new [agricultural-inputs and forest-products valuation/liquidity workbench](combined-investment-research-agricultural-inputs-forest-products-valuation-liquidity-workbench-2026-09-17.md)
routes CF Industries and West Fraser as separate physical commodity models.
Nitrogen-to-food economics and wood-products-to-housing economics retain their
own realized-price, energy, plant/mill uptime, modernization, tariff, debt, and
replacement-capital tests. Production, adjusted EBITDA, OCF, reported FCF,
repurchases, and dividends remain diagnostic rather than normalized owner cash.

The [consumer goods and household upkeep Q2 2026 cash-quality refresh](combined-investment-research-consumer-goods-q2-2026-cash-quality-refresh-2026-09-17.md)
adds Burlington, Ollie's, and Lowe's current-period evidence. Burlington's
`$334.6M` H1 OCF includes a `$55.5M` tariff-refund benefit while `$537.5M` of
property and lease-acquisition spending supported 91 net new stores. Ollie's
generated `$153.6M` of OCF against `$68.8M` of capex while inventory timing and
new-store growth absorbed cash. Lowe's generated `$7.009B` of OCF against
`$1.063B` of capex but also paid dividends, repurchases, and bond maturities.
The household-value lane remains qualified, owner-cash-open, and unranked.

The [ordinary finance Q2 2026 credit-quality refresh](combined-investment-research-ordinary-finance-q2-2026-credit-quality-refresh-2026-09-17.md)
adds current JPMorgan, American Express, and Capital One controls. JPMorgan's
Q2 includes a `$4.55B` Visa-share gain alongside `$2.5B` of credit costs and a
`$149M` reserve build. American Express reports `$455.8B` of billed business,
but its lower provision includes a reserve release while write-offs rose.
Capital One reports `$3.0B` of net income with `$3.642B` of net charge-offs and
a `$662M` allowance release amid the Discover integration. The finance lane
remains credit-quality-qualified, loss-normalization-open, and unranked.

The [ordinary-finance valuation/liquidity workbench](combined-investment-research-ordinary-finance-valuation-liquidity-workbench-2026-09-17.md)
now applies the correct bank/card valuation objects: loss-adjusted spread,
fee retention, funding cost, rewards, integration, regulatory capital, and
diluted common distribution capacity. Deposits, billed business,
pre-provision earnings, reserve releases, and exceptional gains remain
diagnostic inputs rather than industrial-style owner cash.

The [consumer-goods valuation/liquidity workbench](combined-investment-research-consumer-goods-valuation-liquidity-workbench-2026-09-17.md)
now separates Burlington's store ramp and tariff-supported cash, Ollie's
closeout inventory and limited liquidity, and Lowe's service/store economics
and debt maturities. Store counts, sales, OCF-less-capex, refunds, and
repurchases remain diagnostic inputs; mature-store return, inventory quality,
replacement capital, claims, and diluted common cash remain open.

The [medical-devices valuation/liquidity workbench](combined-investment-research-medical-devices-valuation-liquidity-workbench-2026-09-17.md)
now separates Stryker's acquisition and quality-claim burden, Intuitive's
installed-base utilization and lease collection, and Henry Schein's
distribution, securitization, restructuring, and dilution claims. Procedure
growth, systems, adjusted EPS, and repurchases remain evidence inputs rather
than normalized common-owner cash.

The [exchange/information valuation/liquidity workbench](combined-investment-research-exchange-information-valuation-liquidity-workbench-2026-09-17.md)
now separates CME's clearing collateral and default-risk capital from exchange
owner cash, and S&P Global's subscription economics from dispositions,
acquired-cohort return, amortization, SBC, and dilution. Volume, collateral,
reported FCF, and market-data growth remain diagnostic inputs rather than a
pooled common-owner denominator.

The [energy affordability and supply-route Q2 2026 cash-quality refresh](combined-investment-research-energy-q2-2026-cash-quality-refresh-2026-09-17.md)
adds current Energy Transfer, Cheniere, PBF, and Devon controls. It separates
Energy Transfer's `$5.07B` Q2 adjusted EBITDA and `$2.59B` DCF from project
cash; Cheniere's H1 exports and in-transit LNG from recognized and collected
revenue; PBF's `$1.2651B` H1 OCF from `$242.4M` of turnaround spending; and
Devon's `$3.7B` Q2 OCF from `$1.269B` capex and a `$2.6B` acreage acquisition.
The energy lane remains physical-route-qualified, cycle-and-project-return-open,
and unranked.

The [integrated oil and gas Q2 2026 cash-quality refresh](combined-investment-research-integrated-oil-gas-q2-2026-cash-quality-refresh-2026-09-17.md)
extends the energy lane into ConocoPhillips and Exxon Mobil. It separates H1
operating cash from production decline, replacement and development capital,
refining and chemical margins, working-capital timing, derivative and reserve
items, geopolitical disruption, contingent consideration, debt, and shareholder
returns. The integrated oil-and-gas lane remains physical-asset-qualified,
cycle-and-replacement-open, and unranked. The new [integrated oil and gas valuation/liquidity workbench](combined-investment-research-integrated-oil-gas-valuation-liquidity-workbench-2026-09-17.md)
now turns those observations into company-specific through-cycle valuation
objects, replacement denominators, liquidity stresses, and filing-based
thesis breakers. It keeps ConocoPhillips' upstream/LNG route separate from
Exxon's integrated upstream, refining, chemicals, and trading route, and does
not promote production, segment earnings, mechanical OCF-less-capex,
dividends, or repurchases into normalized owner cash.

The [Q2 2026 cross-sector cash-quality control panel](combined-investment-research-q2-2026-cross-sector-cash-quality-control-panel-2026-09-17.md)
now connects the broad-technology, basic-materials, consumer-goods, ordinary-
finance, energy-supply-route, and integrated-oil-and-gas refreshes on one
period-aware surface. It shows that “cash conversion” has different meanings
across deferred service revenue, exceptional proceeds, inventory-funded
growth, credit-loss normalization, project cash, and reserve replacement. The
panel is a control map rather than a pooled ranking; each lane retains its
company-specific denominator and promotion object.

The [Q2 2026 valuation and liquidity stress matrix](combined-investment-research-q2-2026-valuation-liquidity-stress-matrix-2026-09-17.md)
now carries the expanded current lanes through explicit Damodaran-style valuation objects,
reinvestment variables, Lyn Alden-style liquidity stresses, and filing-based
thesis breakers. It keeps price-implied expectations separate from proven cash
and leaves every lane expectation-screen-qualified, liquidity-stress-open, and
unranked.

The [Wheaton–Antamina Q-03 metal-credit receipt boundary](capital-flow-wheaton-antamina-q03-metal-credit-receipt-boundary-2026-09-17.md)
now closes an integration gap in the original capital-flow pilot. It identifies
the legally correct receipt object—BHP metal-credit issuance, sale or
receivable, and Wheaton bank collection—rather than searching for physical
silver delivery. Wheaton's Q2 filing now adds the April 1, 2026 `$4.3B`
payment to BHP and identifies the new term loan, revolver draw, and cash on
hand as the partial funding mix; BHP separately reports the corresponding
upfront proceeds. This closes the narrow upfront closing-funds-flow direction,
while BHP-only credits, invoice price, recurring collection, tax, and
asset-level financing allocation remain open.

The [Q-10 current six-lane macro overlay](combined-investment-research-q10-current-six-lane-macro-overlay-2026-09-17.md)
extends the through-cycle causal protocol to the latest technology, materials,
consumer, finance, energy-route, and integrated-oil-and-gas lanes. It records
the predicted macro transmission, company observable, confound, and required
repeated evidence while keeping the result `macro-route-visible; company-
response-observed; causal-promotion-open`.

The [Q2 2026 QoE and financial-shenanigans diagnostic panel](combined-investment-research-q2-2026-qoe-financial-shenanigans-panel-2026-09-17.md)
now makes the forensic overlay explicit across the expanded current lanes. It
maps deferred revenue, exceptional proceeds, inventory and working-capital
timing, reserve releases, adjusted metrics, collateral, acquisition claims,
franchisee support, and replacement burdens to the exact reconciliation
required. It preserves the Sloan/Schilit prompt framework, rejects a
non-comparable pooled Beneish score, and makes no fraud finding or owner-cash
promotion.

The [Q-03 receivable-classification boundary](capital-flow-wheaton-antamina-q03-receivable-classification-boundary-2026-09-17.md)
further narrows the public receipt search: Wheaton's Q2 total, concentrate,
cobalt, and other receivable categories are visible, but none is identified as
a BHP/Antamina credit. This strengthens classification discipline without
promoting an unallocated balance to receipt cash.

The [Wheaton Investor Day forward-profile boundary](capital-flow-wheaton-antamina-investor-day-forward-profile-boundary-2026-09-16.md)
adds a dated management scenario to the Q-03/Q-02 bridge: approximately
`6.0 Moz` of Antamina silver per year for the first five years and `5.4 Moz`
for the first ten years, with Antamina shown at `18%` of 2025 actual and
`12%` of 2030 expected production mix on Wheaton's GEO basis. These figures
are useful valuation and concentration inputs, but they are not reserve-backed
delivery, BHP-only metal credits, invoice cash, tax allocation, or financed
return proof.

The next evidence layer moves from classification into financing and
operating-control boundaries. The [URI ABL collateral-eligibility and
availability bridge](capital-flow-uri-abl-collateral-eligibility-bridge-2026-09-17.md)
shows why a contractual borrowing base, eligible collateral, reserves, and
availability cannot be inferred from the balance sheet alone. The [PBF
redemption settlement bridge](capital-flow-pbf-redemption-settlement-bridge-pass-1.md)
and [September exchangeable-financing liquidity boundary](capital-flow-pbf-september-2026-conditional-redemption-liquidity-boundary-2026-09-17.md)
separate completed June debt settlement from the issued September exchangeable
financing and the still-pending 2030-note redemption, accrued interest, cash
allocation, dilution, and the still-open refinancing NPV. The
[Ares/Frontline primary-source refresh](capital-flow-ares-frontline-primary-source-refresh-2026-09-17.md)
similarly preserves the distinction between an arranger, an investment
manager, a named borrower, a filed instrument, and funded lender cash.

The [insurance broker/carrier Q2 refresh](combined-investment-research-insurance-brokers-carrier-q2-2026-cash-quality-refresh-2026-09-17.md),
[exchange and information infrastructure Q2 refresh](combined-investment-research-exchange-information-infrastructure-q2-2026-cash-quality-refresh-2026-09-17.md),
[materials, specialty chemicals, and steel Q2 refresh](combined-investment-research-materials-chemicals-steel-q2-2026-cash-quality-refresh-2026-09-17.md),
[digital real-estate Q2 refresh](combined-investment-research-digital-real-estate-q2-2026-cash-quality-refresh-2026-09-17.md),
and [healthcare-distribution current-period synthesis](combined-investment-research-healthcare-distribution-current-period-synthesis-2026-09-17.md)
extend the same forensic method across fiduciary and loss reserves, clearing
collateral, subscription economics, working-capital investment, replacement
capital, development and partner funding, acquisition consideration, and
distributor scale. These additions are deliberately not pooled into a sector
ranking: each remains a qualified control map with its own denominator,
period, legal entity, and promotion object.
The new [materials, chemicals, and steel valuation/liquidity workbench](combined-investment-research-materials-chemicals-steel-valuation-liquidity-workbench-2026-09-17.md)
now turns Ecolab's embedded chemistry/service route, Sherwin-Williams'
coatings/distribution route, and Nucor's steel-capacity route into separate
valuation, reinvestment, liquidity, and thesis-breaker objects. It keeps
working-capital cycles, acquisition cash, project utilization, environmental
claims, debt, and dilution company-specific rather than pooling a specialty
service model with a steel cycle.
The September 18 market-expectation refresh places Ecolab at approximately
`$76.042B`, Sherwin-Williams at `$78.900B`, and Nucor at `$56.755B` of equity
value. Current mechanical H1 OCF-less-capex screens are approximately `64.8x`
for Ecolab and `26.9x` for Nucor; Sherwin-Williams lacks a comparable current
capex denominator. These are not normalized owner-cash multiples: Ecolab's
working-capital, service/equipment, acquisition, and dilution burdens remain
open, while Nucor's screen includes a steel-cycle working-capital investment
and a `$130M` raw-material refund. No materials ranking is promoted.

The new [integrated steel, automotive-contract, and fixed-cost-cycle valuation/liquidity workbench](combined-investment-research-cleveland-cliffs-integrated-steel-contract-cycle-valuation-liquidity-workbench-2026-09-18.md)
adds Cleveland-Cliffs as a distinct integrated iron-ore, pellet, DRI, steel,
and downstream-conversion lane, separate from Nucor's electric-arc model. It
tests contract lag, automotive volume, utilization, energy/labor, fixed-cost
absorption, pension/OPEB, capex, debt, and diluted common residual.

Across the full system, the recurring investment question is therefore not
whether reported earnings or operating cash increased, but whether the named
economic claim survived the bridge from recognition to collection and from
reported cash to sustainable common-owner cash. The remaining promotion work
is source-object specific: BHP/Wheaton credit issuance-to-bank receipt,
retail matched settlement and maintenance-capital evidence, and URI's
populated borrowing-base/NOLV/reserve certificate. Until those objects are
reconciled, the system should retain `owner-cash-open`, `receipt-open`, or
`causal-promotion-open` labels rather than manufacture a ranking.

The [promotion-gate execution ledger](combined-investment-research-promotion-gate-execution-ledger-2026-09-17.md)
turns those open conclusions into a 13-row operating queue. Each row names
the next source object, the reconciliation required for promotion, and the
stop rule that prevents a nearby proxy from being mistaken for proof. The
queue prioritizes Q-03, CA-06, and URI because their missing objects could
change an existing proof grade; all other lanes remain qualified until their
own same-entity, same-period join is available.

The [TJX Q2 FY2027 settlement and capex boundary](combined-investment-research-retail-tjx-q2-2026-settlement-capex-boundary-2026-09-17.md)
adds a concrete retail QoE signal: the latest filing identifies a
credit-card interchange-fee settlement and tariff refunds among H1 cash and
earnings drivers, while mixing renovations, new stores, distribution
centers, offices, and IT in capital spending. The signal improves the
temporary-support and capex-mix controls but does not disclose the settlement
amount or maintenance split. It also discloses `$1.147B` of TJX H1 operating
lease cash paid, which improves the period-matched burden bridge without
closing taxes, service costs, or common-owner allocation. CA-06 remains
partial and no retail ranking is promoted.
The same TJX filing now adds a period-matched common-owner and liquidity
boundary: `$1.402B` of H1 repurchases, `$1.000B` of dividends, a planned
`$1.000B` September note repayment from operating cash, and `$1.5B` of credit-
facility availability. These are cash uses and claims rather than owner-cash
generation; actual repayment and facility movement remain unproven.

The [Target Q2 2026 cash-quality boundary](combined-investment-research-retail-target-q2-2026-cash-quality-boundary-2026-09-17.md)
adds the matching current filing control: `$4.519B` H1 OCF, `$2.404B`
property spending, `$994M` tariff refunds, and `$3.2B` of eligible
supplier-finance obligations that Target explicitly says are not actual early
payments. Target also says vendor early payment is optional, does not change
Target's remittance amount or payment date, and that its payment date can be up
to 120 days from invoice date. The prior-period `$593M` interchange-settlement
gain remains a comparison distortion, not current cash. Target's lease cash
and maintenance/service allocation remain open, so CA-06 stays partial.
Target's current strategy and Q2 release add a directional capex-growth
boundary: an approximately `$5B` 2026 plan with more than `130` remodels and
more than `30` new stores, and Q2 capex driven primarily by remodels and new
stores. This confirms active expansion inside the mixed `$2.404B` H1 line, but
not the maintenance/replacement allocation or normalized owner cash. See the
[Target capex growth-driver boundary](combined-investment-research-target-q2-2026-capex-growth-driver-boundary-2026-09-18.md).
The Q2 management call further describes approximately `$2.4B` of H1 CapEx as
intentional incremental investment, up nearly `30%`, while reporting growth in
Roundel, Target Plus and Target Circle 360. It supplies no allocated cost or
cash schedule for those attached services and no maintenance, lease, or Shipt
payment line, so the evidence strengthens burden direction without promoting
Target owner cash.

The [Walmart Q2 FY2027 capex and tariff-refund boundary](combined-investment-research-retail-walmart-q2-fy27-capex-refund-boundary-2026-09-17.md)
completes the current three-retailer control surface: Walmart received
approximately `$2.9B` of tariff refunds, generated `$19.710B` of H1 OCF,
spent `$14.181B` on property and equipment, and reported `$5.529B` of
management-defined FCF. The filing supplies useful capex categories but says
its FCF excludes debt service and acquisitions; maintenance, lease, service,
and common-owner allocation remain open.
Walmart's official Q2 presentation attributes a `$2.8B` year-over-year capex
increase to its omnichannel growth strategy. The Q2 release also makes the
ecosystem accounting boundary explicit: advertising is recorded in net sales or
as a reduction of cost of sales depending on the arrangement. Advertising,
marketplace, fulfillment and membership growth therefore cannot be added to
owner cash without arrangement-level gross/net and allocated-cost evidence.

The [URI Q2 2026 availability and lifecycle boundary](combined-investment-research-uri-q2-2026-availability-lifecycle-boundary-2026-09-17.md)
adds a current asset-backed control surface: stated liquidity, the
receivables collateral pool, covenant-threshold status, operating cash,
rental-equipment purchases, sale proceeds, and company-defined free cash flow
are now joined to the same June 30 period. It also reports `$2.802B` of ABL
borrowing capacity net of letters of credit and `$85M` of receivables-
securitization capacity, which explains the public capacity proxy without
creating a populated certificate. The filing still does not disclose
the equipment borrowing-base/NOLV certificate or fleet-cohort replacement
return, so liquidity is not treated as legal availability and FCF is not
treated as owner cash.

## Latest execution updates

The latest execution passes sharpen five sector-specific boundaries and carry
them into the valuation/liquidity layer without
creating a pooled ranking:

- **Restaurants:** McDonald's Q2 franchised sales were `$34.451B` across
  `44,016` franchised restaurants, but franchised sales are not company
  revenue or collected franchisor cash. Franchisee collections, closures,
  delinquency, and reinvestment remain unjoined.
- **Retail CA-06 denominator:** TJX's Q2 filing quantifies a non-recurring
  `$419M` credit-card interchange settlement gain net of legal expenses and
  says related amounts were received during the quarter ended May 2, 2026 and
  included in H1 operating activities. The gross cash/legal-expense bridge and
  maintenance-versus-growth capex split remain open, so the settlement is not
  normalized owner cash.
- **Private credit / Bear Financing:** the [Q2 source boundary](capital-flow-kkr-global-atlantic-bear-financing-q2-2026-schedule-boundary-2026-09-17.md)
  records that the official Accordia Q2 2026 verification document reports an
  aggregate `$7.371492B` bond base but omits the detailed Bear Financing
  CUSIP/Schedule D row. KKR's parent Q2 filing adds only aggregate Global
  Atlantic commitment context. These are source-availability boundaries, not
  evidence of sale, repayment, or settlement; lender allocation, borrower use,
  debt service, receipt, and liability-adjusted return remain open.
- **Industrial conversion:** Sterling's H1 operating cash of `$328.021M` was
  reduced by `$69.646M` of capex, `$139.985M` of cash acquisitions, and
  `$7.767M` of earn-out payments, leaving a visible-use residual of `$110.623M`
  before taxes, interest, leases, claims, and maintenance allocation. WESCO's
  Q2 OCF fell to `$53.7M` from `$107.8M` despite strong demand, while Fastenal's
  OCF conversion fell to 69.4% of net income. These are project and distribution
  conversion warnings, not pooled owner-cash or manipulation conclusions.
- **Power-grid customer cash:** FPL's H1 OCF of `$5.388B` against `$5.780B` of
  capex, AEP's `$3.421B` against `$5.606B` of construction spending, and Duke's
  `$4.272B` against `$8.240B` of capex expose different funding burdens. FPL
  category recovery, AEP's 69 GW signed-load expectation, and Duke's Anderson
  County ownership are kept separate from billed collections, paid capex,
  customer recovery, and common-owner cash.
- **Integrated oil and gas:** ConocoPhillips reported `$11.729B` H1 OCF against
  `$5.972B` of capital and investments while production fell to `2.278M BOE/d`;
  Exxon reported `$32.260B` OCF against `$12.997B` of PP&E additions, with a
  `$3.857B` operational working-capital use and identified losses. Commodity
  price, field decline, replacement capital, claims, and integrated-margin
  effects keep both companies cycle-qualified but unranked.
- **Consumer goods and household upkeep:** Burlington's `$334.6M` H1 OCF was
  accompanied by `$532.4M` property spending and a `$55.5M` tariff-refund
  benefit; Ollie's `$153.6M` OCF was exposed to inventory timing and store
  growth; Lowe's `$7.009B` OCF coexisted with `$1.063B` capex, `$1.346B`
  dividends, `$367M` repurchases, and roughly `$2.4B` of bond maturities.
  Value-retail inventory and home-upkeep debt/service claims remain separate
  from normalized owner cash.
- **Ordinary finance:** JPMorgan's `$4.55B` Visa-share gain, `$2.5B` credit
  costs, and `$2.4B` net charge-offs; American Express's `$455.8B` billed
  business alongside `$1.084B` of Q2 credit-loss provision; and Capital One's
  `$3.642B` net charge-offs alongside a `$662M` allowance release demonstrate
  why volume, pre-provision earnings, reserve releases, and net income cannot
  be treated as loss-adjusted common-owner cash.
- **Broad technology:** Fortinet's H1 OCF of `$2.121B` included deferred
  revenue of `$7.676B`, `$154.0M` SBC, `$972.8M` repurchases, and a `$500M`
  note repayment. Cloudflare's `$275.9M` OCF and `$140.5M` reported FCF sat
  alongside `$274.1M` SBC, `$115.2M` PP&E capex, `$20.2M` capitalized software,
  and `$75.1M` acquisitions. Deferred revenue, billings, RPO, and FCF remain
  visibility/liquidity inputs rather than normalized owner cash.
- **Insurance:** Chubb's H1 net unpaid losses ended at `$71.216B`, gross unpaid
  losses at `$89.669B`, reinsurance recoverable at `$18.453B`, and net losses
  paid at `$11.353B`; its `$584M` favorable prior-year development and modeled
  catastrophe PMLs are normalization and stress inputs, not owner cash.
- **Accordia / Global Atlantic legal-entity cash:** the official Accordia Q2
  2026 statutory verification statement adds a current cash-and-liability
  control: `$12.146052B` of admitted assets, `$11.411695B` of liabilities,
  `$734.357M` of surplus, `$4.240949B` of funds held under coinsurance, and
  `$259.286M` of ending cash. H1 investment proceeds of `$764.721M` were below
  `$906.633M` of investments acquired, while cash-flow investment income was
  `$288.780M` versus `$291.515M` of summary investment income. This establishes
  an entity-level reinvestment and cash-quality surface, not settlement for the
  three named CUSIPs, liability-cost allocation, KKR remittance, or common-owner
  residual. The portal-linked ALIRT exhibit adds only an unaudited, notional
  FLIC/Global Atlantic Re and GAAL reinsurance attribution; it is not an
  Accordia Schedule D, settlement, or statutory liability-cost bridge. See the
  [Accordia Q2 statutory cash-flow refresh](capital-flow-kkr-global-atlantic-accordia-q2-2026-statutory-cash-flow-refresh-2026-09-18.md).
- **Apollo/Athene parent receipt:** Apollo's Q2 filing reports `$25.4B` of
  consolidated unrestricted cash, `$5.6B` of available facility capacity, and
  no amounts outstanding under the Athene credit facilities at June 30, 2026.
  These improve the liquidity and senior-claim perimeter, but do not trace the
  `$110M` Athene H1 distribution to an AGM account or establish common-owner
  residual. The current object remains `Athene distribution -> AGM receipt
  (unproven) -> liquidity (observed) -> senior claims/residual (unproven)`.
- Apollo's August 24 8-K also identifies an AMAPS Overview Presentation as a
  possible affiliated-asset wrapper source. Its investor-relations PDF was
  identified but returned HTTP `403` through the current retrieval route, so
  no slide content is promoted; a controlled copy would be needed before using
  it for portfolio identity, funding, settlement, or return.
- **Wheaton–Antamina:** the public contract terms imply `30.375%` payable
  entitlement before the 100M-ounce threshold and `20.25%` afterward, after
  applying the 90% payable factor. The combined Antamina segment reported Q2
  sales of `$150.549M` and operating cash flow of `$122.039M`, and H1 sales of
  `$277.563M` and operating cash flow of `$222.223M`; these figures cover BHP
  and legacy Glencore streams together. They are a stronger period-matched
  operating surface, not BHP-specific credit sales or bank receipts.
- **URI:** the holding-company/URNA structure adds a legal-availability gate;
  consolidated cash and OCF cannot be assumed freely distributable to the
  parent while subsidiary debt agreements restrict transfers. The June 30
  filing also yields a searched-negative for a public NOLV or equipment
  borrowing-base schedule; covenant availability is not that certificate.
- **PBF:** the September 2030-note redemption carries a calculated `$519.690M`
  principal-plus-premium floor before accrued interest. It remains separate
  from June's completed 2028-note redemption. The September 2032 exchangeable
  financing is now issued with approximately `$533.6M` of net proceeds; the
  0% non-accreting note, cash/share settlement election, capped-call cap, and
  structural subordination are visible, but redemption settlement,
  gross-to-net allocation, capped-call cost, accrued-interest, ABL, and
diluted-share analysis remain open.
The September 17 filing also names the co-issuers and initial guarantor set,
and states that non-guarantor subsidiary debt and secured ABL debt sit ahead
of the notes in the relevant structural/effective-subordination layers. This
sharpens the legal-entity cash perimeter but still does not prove refinery-
level cash, intercompany transfer, trustee payment, or common-owner residual.
- **Healthcare distribution:** McKesson, Cencora, and Cardinal are kept on
  separate fiscal-period and legal-claim surfaces: distributor working capital,
  acquisition cash, preferred/NCI claims, opioid settlements, and dilution are
  not collapsed into a common OCF ranking. Cardinal's `$374M` July opioid
  payment is post-FY2026 cash and is kept outside the FY2026 screen.
- **Medical devices:** Stryker, Intuitive Surgical, and Henry Schein remain
  separate control-point models: acquisition return and claims for Stryker,
  installed-base utilization and lease collection for Intuitive, and
  securitization, restructuring, debt, and dilution for Henry Schein. Their
  OCF screens are not pooled because utilization, collection, and acquired-
  cohort cash remain unproven.
- **Exchange and information infrastructure:** CME's `$138.5B` Federal Reserve
  cash account and `$1.545B` decrease in performance-bond/guaranty-fund
  contributions are kept separate from exchange-owner cash, while S&P Global's
  `$361M` disposition proceeds, `$26M` acquisition outflow, `$551M`
  amortization, and `$95M` SBC remain separate from recurring information cash.
- **Materials, specialty chemicals, and steel:** Ecolab's H1 operating cash of
  `$1.1754B` against `$588.6M` of capex included `$197.0M` of receivables use,
  `$131.4M` of inventory use, `$75.1M` of SBC, and `$60M` of Ovivo-related
  equity-incentive payments. Nucor's `$2.286B` of operating cash against
  `$1.232B` of capex included `$952M` of receivables use and `$560M` of
  inventory use, with 2026 capex estimated at `$2.50B`. Embedded service
  economics and steel capacity are therefore visible control points, but
  organic owner cash, maintenance-versus-growth capital, and through-cycle
  returns remain open.
- **Valuation and liquidity overlay:** the Damodaran/Lyn Alden workbench now
  carries these inputs as explicit expectation burdens and funding stresses:
  Wheaton debt/entitlement, URI parent availability and fleet replacement,
  PBF refinancing burden, and Chubb reserve/reinsurance/catastrophe exposure.
  URI's H1 OCF, purchases, and equipment-sale proceeds remain a reported
  bridge until cohort replacement, resale, borrowing-base eligibility, and
  parent transfer rights are joined. None is treated as normalized owner cash
  or a promoted return.

- **Healthcare access and care delivery:** the new valuation/liquidity
  workbench keeps UnitedHealth and Cigna on claims and reserve denominators,
  DaVita on treatment/reimbursement/NCI cash, Option Care on therapy collection
  and working capital, Addus on labor and payer rates, BrightSpring on
  acquisition/interest/SBC burden, and Enhabit on its final public-company
  boundary. MCR, treatment volume, adjusted EBITDA, and management-defined FCF
  are inputs to the stress model, not pooled owner cash.

These updates reinforce the system's central conclusion: activity, accounting
recognition, contractual capacity, and reported cash must each survive the
same-entity collection, claim, funding, and owner-availability tests before a
valuation conclusion or ranking is promoted.

The new [networking-control valuation/liquidity workbench](combined-investment-research-networking-control-valuation-liquidity-workbench-2026-09-17.md)
extends the research to Arista Networks and Ciena without pooling their
denominators. Arista is tested through AI-fabric control, deferred-revenue
normalization, hyperscaler concentration, SBC, and dilution; Ciena is tested
through optical transport, backlog-to-cash conversion, acceptance, inventory
obsolescence, receivables, acquisitions, and dilution. Revenue, orders,
backlog, deferred revenue, and reported OCF remain diagnostic until the
company-specific collection and residual joins are evidenced.

The new [defense and mission-systems valuation/liquidity workbench](combined-investment-research-defense-mission-systems-valuation-liquidity-workbench-2026-09-17.md)
extends the research to CACI, Leidos, and Northrop Grumman as separate
government-execution models. It keeps funded backlog, cleared labor, contract
assets, program estimates, acquisitions, pension, debt, and dilution distinct;
backlog, awards, adjusted EBITDA, and reported OCF remain diagnostic until
program delivery, collection, required reinvestment, and common-owner residual
are joined.

The new [regulated water infrastructure valuation/liquidity workbench](combined-investment-research-regulated-water-valuation-liquidity-workbench-2026-09-17.md)
adds American Water Works as a distinct rate-base and essential-service lane.
It separates renewal and compliance capex, customer contributions, regulatory
lag, affordability, PFAS/lead obligations, acquisitions, debt, dividends, and
dilution. Connections, rate-base plans, revenue, and OCF-less-capex remain
diagnostic until regulatory recovery, collections, required renewal, and common
residual are joined.

The new [life-science tools and laboratory workflow valuation/liquidity workbench](combined-investment-research-life-science-tools-valuation-liquidity-workbench-2026-09-18.md)
adds Thermo Fisher as a distinct laboratory-workflow lane, separate from
medical devices and biopharma franchises. It tests instruments, consumables,
services, pharma-services utilization, replacement/capacity capex, quality,
acquisitions, working capital, debt, SBC, and dilution. Revenue, reported FCF,
and acquisition-adjusted screens remain diagnostic until utilization, collection,
replacement, and common-residual joins are evidenced.

The new [electronic test and measurement valuation/liquidity workbench](combined-investment-research-electronic-test-measurement-valuation-liquidity-workbench-2026-09-18.md)
adds Keysight and Teradyne as a distinct instrumentation and production-test
lane, separate from ASML lithography and KLA process control. It tests design
workflow, test acceptance, software/service attachment, customer deposits,
semiconductor and robotics cycles, R&D, inventory, acquisitions, debt, SBC,
and dilution. Orders, revenue, contract liabilities, reported OCF, and FCF
remain diagnostic until workflow collection and reinvestment are joined.

The new [digital advertising and measurement valuation/liquidity workbench](combined-investment-research-digital-advertising-measurement-valuation-liquidity-workbench-2026-09-18.md)
adds The Trade Desk and DoubleVerify as a distinct advertiser-decisioning and
independent-measurement lane. It keeps gross spend, measured transactions,
take-rate/fee economics, platform access, identity/privacy, data/cloud cost,
customer collection, merger terms, SBC, and dilution separate. Gross spend,
measured volume, adjusted EBITDA, reported OCF, and buybacks remain diagnostic
until transaction settlement and common-residual joins are evidenced.

The new [foodservice distribution valuation/liquidity workbench](combined-investment-research-foodservice-distribution-valuation-liquidity-workbench-2026-09-18.md)
adds Sysco and US Foods as a distinct route-density and procurement lane,
separate from healthcare distribution and branded staples. It tests cases,
price/mix, vendor consideration, inventory, receivables, customer credit,
warehouse/fleet labor, fuel, ordering technology, acquisitions, debt, and
dilution. Sales, cases, gross profit, vendor rebates, reported OCF, and FCF
remain diagnostic until route collection and renewal-capital joins are
evidenced.

The new [enterprise security platform valuation/liquidity workbench](combined-investment-research-enterprise-security-platform-valuation-liquidity-workbench-2026-09-18.md)
adds Palo Alto Networks as a distinct security-consolidation lane, separate
from edge delivery, cloud policy, and programmable edge. It tests firewall,
cloud, identity, SOC, subscription support, organic ARR/RPO, cross-sell,
CyberArk/Chronosphere integration, hosting cost, remediation, SBC, and diluted
common residual. ARR, RPO, subscription mix, adjusted FCF, OCF, and buybacks
remain diagnostic until organic retention, collection, integration-return, and
per-share cash joins are evidenced.

The new [HP endpoint and printing valuation/liquidity workbench](combined-investment-research-hp-endpoint-printing-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct mature-hardware lane. It separates Personal Systems,
Printing, endpoint sell-through, channel inventory, supplies attachment, tariffs,
restructuring, debt, and diluted common residual. Revenue, units, adjusted EPS,
OCF, FCF, and repurchases remain diagnostic until collection, inventory,
reinvestment, and per-share cash joins are evidenced.

The new [search, advertising, and cloud platform valuation/liquidity workbench](combined-investment-research-search-advertising-cloud-valuation-liquidity-workbench-2026-09-18.md)
adds Alphabet as a distinct search/attention and cloud-capital lane, separate
from Amazon commerce, Oracle database cloud, and independent advertising
measurement. It tests Services, YouTube, traffic acquisition, Cloud
utilization, shared AI research, extreme capex growth, Other Bets, regulation,
SBC, and diluted common residual. Revenue, operating income, clicks, CPC, Cloud
growth, OCF, FCF, and repurchases remain diagnostic until incremental-return,
legal, and per-share cash joins are evidenced.

The new [senior-living operator valuation/liquidity workbench](combined-investment-research-senior-living-operator-valuation-liquidity-workbench-2026-09-18.md)
adds Brookdale as a distinct community-operator lane, separate from Welltower's
property ownership, HCA acute care, and healthcare distribution. It tests
occupancy, RevPAR, resident affordability, care intensity, labor, leases,
maintenance and life-safety capital, quality, debt, and diluted common residual.
Occupancy, adjusted EBITDA, OCF, FCF, dividends, and buybacks remain diagnostic
until community contribution, staffing, property cash, and per-share joins are
evidenced.

The new [power-management and aerospace-systems valuation/liquidity workbench](combined-investment-research-power-management-aerospace-systems-valuation-liquidity-workbench-2026-09-18.md)
adds Eaton as a distinct diversified power-management and aerospace lane,
separate from GE Vernova generation equipment, Hubbell grid components, and
nVent protection/cooling. It tests backlog-to-cash, unbilled receivables,
acquisition cohorts, PP&E, Mobility separation costs, debt, capital returns,
SBC, and diluted common residual. Orders, backlog, adjusted EPS, OCF, FCF,
dividends, and buybacks remain diagnostic until billed collection, acquisition
return, separation, and per-share cash joins are evidenced.

The new [global technology-services valuation/liquidity workbench](combined-investment-research-global-technology-services-valuation-liquidity-workbench-2026-09-18.md)
adds Accenture as a distinct global implementation and managed-services lane,
separate from enterprise software, infrastructure engineering, institutional
consulting, and talent advisory. It tests bookings conversion, utilization,
revenue per professional, labor and training, managed-service renewal,
acquisitions, deferred revenue, SBC, and diluted common residual. Bookings,
book-to-bill, adjusted margin, OCF, FCF, AI revenue, and buybacks remain
diagnostic until delivery, collection, labor, and per-share cash joins are
evidenced.

The new [integrated commerce and cloud platform valuation/liquidity workbench](combined-investment-research-integrated-commerce-cloud-platform-valuation-liquidity-workbench-2026-09-18.md)
adds Amazon as a distinct shared-infrastructure lane, separate from eBay,
Shopify, Wayfair, DigitalOcean, Oracle, and NVIDIA. It tests seller services,
advertising, subscriptions, fulfillment, AWS utilization, full capex,
lease-funded assets, inventory/payables, labor, legal claims, debt, SBC, and
diluted common residual. Revenue, AWS profit, OCF, FCF, GMV, advertising,
subscriptions, and repurchases remain diagnostic until full-capital-return and
per-share cash joins are evidenced.

The new [infrastructure engineering and program-management valuation/liquidity workbench](combined-investment-research-infrastructure-engineering-program-management-valuation-liquidity-workbench-2026-09-18.md)
adds Jacobs as a distinct technical-design and program-coordination lane,
separate from specialty construction, mission technology, consulting, and
environmental equipment. It tests gross versus adjusted-net backlog,
pass-through revenue, contract assets, receivables, PA acquisition return,
employee consideration, debt, SBC, and diluted common residual. Backlog,
book-to-bill, adjusted EBITDA, OCF, and buybacks remain diagnostic until
project, collection, acquisition-return, and per-share cash joins are
evidenced.

The new [hospital consumables and infusion valuation/liquidity workbench](combined-investment-research-hospital-consumables-infusion-valuation-liquidity-workbench-2026-09-18.md)
adds Baxter as a distinct hospital-supply and post-divestiture reset lane,
separate from Abbott, procedure medtech, and healthcare distribution. It tests
IV/infusion and injectable products, quality holds, inventory, working capital,
Kidney Care separation, remediation, debt, leases, and diluted common residual.
Sales, adjusted EPS, FCF, divestiture proceeds, dividends, and buybacks remain
diagnostic until quality, collection, debt, and per-share cash joins are
evidenced.

The new [diversified clinical-products valuation/liquidity workbench](combined-investment-research-diversified-clinical-products-valuation-liquidity-workbench-2026-09-18.md)
adds Abbott as a distinct multi-segment healthcare-products lane, separate from
procedure medtech, laboratory tools, healthcare distribution, and biopharma.
It tests Diagnostics, Medical Devices, Nutrition, Established Pharmaceuticals,
Exact Sciences acquisition return, instrument placement, reimbursement,
quality, debt, SBC, and diluted common residual. Sales, adjusted EPS, OCF,
dividends, and repurchases remain diagnostic until segment, acquired-cohort,
collection, and per-share cash joins are evidenced.

The new [permanent-capital conglomerate valuation/liquidity workbench](combined-investment-research-permanent-capital-conglomerate-valuation-liquidity-workbench-2026-09-18.md)
adds Berkshire Hathaway as a distinct look-through capital-allocation lane,
separate from Loews, standalone insurers, rail, regulated utilities, and asset
managers. It tests insurance float and claims, BNSF renewal, BHE regulated
capital, operating-subsidiary cash, parent liquidity, securities, acquisitions,
taxes, debt, and diluted common residual. Net income, operating earnings, OCF,
float, consolidated cash, dividends, and buybacks remain diagnostic until
segment capital and per-share value joins are evidenced.

The new [environmental and process equipment valuation/liquidity workbench](combined-investment-research-environmental-process-equipment-valuation-liquidity-workbench-2026-09-18.md)
adds CECO Environmental as a distinct engineered-equipment and project-cash
lane, separate from waste-route services, facility services, utilities, and
generation/grid OEMs. It tests backlog-to-cash conversion, contract assets,
inventory, project acceptance, Thermon integration, divestiture gains, debt,
SBC, and diluted common residual. Orders, backlog, adjusted EBITDA, adjusted
FCF, OCF, and buybacks remain diagnostic until project, collection,
integration-return, and per-share cash joins are evidenced.

The new [life insurance and retirement-capital valuation/liquidity workbench](combined-investment-research-life-insurance-retirement-capital-valuation-liquidity-workbench-2026-09-18.md)
adds MetLife as a distinct long-duration liability and regulated-capital lane,
separate from P&C carrier, brokerage, and asset-management economics. It tests
premiums, benefits, reserves, spread income, variable investment income,
reinsurance, statutory capital, subsidiary dividends, holding-company cash,
debt, and diluted common residual. Adjusted earnings, ROE, book value, net
investment income, dividends, and buybacks remain diagnostic until liability,
capital, and distribution joins are evidenced.

The new [generation and grid equipment valuation/liquidity workbench](combined-investment-research-generation-grid-equipment-valuation-liquidity-workbench-2026-09-18.md)
adds GE Vernova as a distinct equipment-OEM and installed-service lane,
separate from utility rate base, Cummins engines, and merchant generation. It
tests equipment versus service RPO, contract-liability funding, Power,
Electrification, Wind, Prolec GE acquisition return, inventory, project
acceptance, warranty, pensions, debt, and diluted common residual. Orders, RPO,
deposits, OCF, FCF, and buybacks remain diagnostic until project, service,
collection, and per-share cash joins are evidenced.

The new [hospital operations valuation/liquidity workbench](combined-investment-research-hospital-operations-valuation-liquidity-workbench-2026-09-18.md)
adds HCA Healthcare as a distinct care-delivery lane, separate from payers,
distributors, devices, and life-science tools. It tests admissions, acuity,
payer mix and collection, labor, supplies, staffed capacity, replacement/growth
capex, acquisitions, noncontrolling interests, interest, debt, litigation, and
dilution. Revenue, admissions, reported OCF, and buybacks remain diagnostic
until payer collection, capacity renewal, and common-claim joins are evidenced.

The new [healthcare payment workflow valuation/liquidity workbench](combined-investment-research-healthcare-payment-workflow-valuation-liquidity-workbench-2026-09-18.md)
adds Waystar as a distinct healthcare-administration software lane, separate
from hospital operations, payers, distributors, care delivery, and devices. It
tests provider versus patient-payment mix, third-party processing cost,
collection, deferred revenue, Iodine acquisition return, product investment,
debt, SBC, and diluted common residual. Revenue, NRR, adjusted EBITDA, OCF,
and transaction volume remain diagnostic until mix, collection, acquisition,
and per-share cash joins are evidenced.

The new [electronics distribution, working-capital financing, and channel-control valuation/liquidity workbench](combined-investment-research-arrow-electronics-distribution-financing-valuation-liquidity-workbench-2026-09-18.md)
adds Arrow Electronics as a distinct technology-distribution lane alongside,
but separate from, Avnet. It tests gross margin, inventory turns, receivable
collection, supplier protection, securitization/factoring, customer credit,
debt, and diluted common residual.

The new [database and cloud-infrastructure valuation/liquidity workbench](combined-investment-research-database-cloud-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
The new [enterprise software, AI capacity, and owner-cash valuation/liquidity workbench](combined-investment-research-microsoft-ai-capacity-owner-cash-valuation-liquidity-workbench-2026-09-18.md)
adds Microsoft as a distinct software-and-cloud capacity lane. It tests renewal,
Azure utilization, Copilot conversion, RPO collection, data-center and power
capital, serving cost, SBC, investment gains, and diluted per-share cash rather
than treating software growth or AI demand as owner cash.
adds Oracle as a distinct installed-database-to-capital-intensive-cloud lane,
separate from enterprise workflow software, builder cloud, Dell systems
distribution, and NVIDIA architecture. It tests RPO quality, customer
prepayments, customer-supplied hardware, data-center capex, depreciation,
debt, leases, preferred financing, SBC, and diluted common residual. Cloud
revenue, RPO, deferred revenue, OCF, capex, and repurchases remain diagnostic
until utilization, delivery, margin, financing, and per-share cash joins are
evidenced.

The new [holding-company subsidiary cash valuation/liquidity workbench](combined-investment-research-holding-company-subsidiary-cash-valuation-liquidity-workbench-2026-09-18.md)
adds Loews as a distinct diversified ownership and capital-allocation lane,
separate from operating-company insurance, pipelines, hotels, packaging, and
asset management. It tests CNA reserves and capital, Boardwalk maintenance and
debt, hotel renovation, packaging working capital, subsidiary remittance,
parent overhead and tax, trapped cash, minority claims, holding-company
discount, and diluted common residual. Consolidated earnings, dividends, OCF,
book value, and buybacks remain diagnostic until subsidiary-capital,
parent-remittance, maintenance, tax, and look-through per-share joins are
evidenced.

The new [exchange, clearing, and collateral valuation/liquidity workbench](combined-investment-research-exchange-clearing-collateral-valuation-liquidity-workbench-2026-09-18.md)
adds CME Group as a distinct derivatives-exchange and central-counterparty
clearing lane, separate from information vendors, banks, brokers, and ordinary
financial companies. It tests transaction/clearing fees, market data, volume
and rate per contract, client collateral, collateral-interest income, clearing
obligations, technology, cyber, regulation, dividends, SBC, and diluted common
residual. Client collateral, volume, OCF, investment income, dividends, and
buybacks remain diagnostic until core-fee, collateral, clearing-obligation,
rate-normalization, and per-share cash joins are evidenced.

The new [Agency mortgage-REIT carry and book-value valuation/liquidity workbench](combined-investment-research-agency-mortgage-reit-carry-valuation-liquidity-workbench-2026-09-18.md)
adds AGNC Investment as a distinct levered Agency RMBS/TBA asset-liability
spread lane, separate from banks, insurers, asset managers, and operating
companies. It tests repo funding, mortgage spreads, prepayment, duration,
hedges, comprehensive income, tangible book value, leverage, collateral,
dividend coverage, capital issuance, and diluted common residual. Spread
income, economic return, book value, dividends, and yield remain diagnostic
until funding, hedge, book-value, leverage, and per-share cash joins are
evidenced.

The new [precious-metals streaming valuation/liquidity workbench](combined-investment-research-precious-metals-streaming-valuation-liquidity-workbench-2026-09-18.md)
adds Wheaton Precious Metals as a distinct contractual-stream lane, separate
from direct mine operators, materials manufacturers, and integrated energy. It
tests delivered and collected metal, upfront stream payments, payable costs,
operator delivery, reserve curves, Antamina return, debt, dividends, taxes, and
diluted common residual. GEOs, revenue, OCF, low PP&E capex, and annualized
stream screens remain diagnostic until delivery, acquisition-return, leverage,
and per-share cash joins are evidenced.

The new [recurring pest-control routes valuation/liquidity workbench](combined-investment-research-recurring-pest-control-routes-valuation-liquidity-workbench-2026-09-18.md)
adds Rollins as a distinct local route-service lane, separate from environmental
services, healthcare access, industrial distribution, and software. It tests
organic versus acquired growth, customer retention, technician productivity,
customer-acquisition cost, claims, chemicals, vehicles, receivables, unearned
service obligations, acquisitions, debt, SBC, and diluted common residual.
Recurring revenue, OCF, FCF, and buybacks remain diagnostic until route,
collection, and acquired-cohort return joins are evidenced.

The new [membership-franchise wellness valuation/liquidity workbench](combined-investment-research-membership-franchise-wellness-valuation-liquidity-workbench-2026-09-18.md)
adds Planet Fitness as a distinct affordable-membership and franchise-network
lane, separate from restaurant franchising, recurring route services, consumer
goods, and software. It tests member retention, attendance, price/mix,
franchisee returns, club openings, support and technology, equipment, debt,
SBC, buybacks, and diluted common residual. Members, systemwide sales, club
count, adjusted EBITDA, OCF, and repurchases remain diagnostic until retention,
franchisee-health, support-cost, and per-share cash joins are evidenced.

The new [transaction marketplace valuation/liquidity workbench](combined-investment-research-transaction-marketplace-valuation-liquidity-workbench-2026-09-18.md)
adds eBay as a distinct goods-marketplace lane, separate from travel
marketplaces, advertising measurement, participation platforms, and retailers.
It tests GMV conversion, take rate, buyer/seller retention, payments, fraud and
transaction losses, advertising, capitalized platform development, Depop and
other acquisitions, debt, SBC, buybacks, and diluted common residual. GMV,
active buyers, advertising, OCF, and repurchases remain diagnostic until trust,
collection, platform-replacement, acquisition-return, and per-share cash joins
are evidenced.

The new [industrial gases and project-capital valuation/liquidity workbench](combined-investment-research-industrial-gases-project-capital-valuation-liquidity-workbench-2026-09-18.md)
adds Air Products as a distinct mature industrial-gas and clean-energy project
lane. It separates on-site and merchant gas contracts from hydrogen projects,
JV funding, partner support, non-recourse debt, project cancellations,
separation obligations, maintenance capital, dividends, and diluted common
residual. Adjusted operating income, contract visibility, OCF, and project
spending remain diagnostic until core-return, project-funding, parent-liquidity,
and per-share cash joins are evidenced.

The new [agribusiness crop-flow valuation/liquidity workbench](combined-investment-research-agribusiness-crop-flow-valuation-liquidity-workbench-2026-09-18.md)
adds Bunge Global as a distinct crop-origination, processing, merchandising,
and commodity-finance lane, separate from agricultural inputs, foodservice
distribution, materials, and direct commodity producers. It tests realized
spreads, inventory and receivables, freight, productive capex, Viterra
integration, debt, collateral, policy, dividends, and diluted common residual.
Revenue, adjusted EBIT/EPS, mark-to-market changes, synergies, OCF, and
buybacks remain diagnostic until realized spread, working capital,
acquisition-return, leverage, and per-share cash joins are evidenced.

The new [franchise media and experiences valuation/liquidity workbench](combined-investment-research-franchise-media-experiences-valuation-liquidity-workbench-2026-09-18.md)
adds Walt Disney as a distinct IP, streaming, sports, parks, cruise, and
experiences lane, separate from travel platforms, advertising measurement,
consumer staples, membership franchises, and transaction marketplaces. It
tests content and rights returns, streaming contribution, attendance and
per-capita spend, maintenance/growth capacity, corporate costs, debt, NCI,
taxes, dividends, and diluted common residual. Segment income, subscribers,
attendance, OCF, and buybacks remain diagnostic until content, rights,
capacity-renewal, and per-share cash joins are evidenced.

The new [asset-integrity inspection valuation/liquidity workbench](combined-investment-research-asset-integrity-inspection-valuation-liquidity-workbench-2026-09-18.md)
adds MISTRAS Group as a distinct certified inspection, monitoring, and
technical-services lane, separate from environmental services, specialty
construction, industrial distribution, and electronic test. It tests recurring
program renewal, technician utilization, collection, contract assets,
software/data, accreditation, capex, claims, debt, and diluted common residual.
Revenue, adjusted EBITDA, gross margin, OCF, FCF, and aerospace/defense growth
remain diagnostic until collection, technician, capability-repair, leverage,
and per-share cash joins are evidenced.

The new [talent advisory and professional services valuation/liquidity workbench](combined-investment-research-talent-advisory-professional-services-valuation-liquidity-workbench-2026-09-18.md)
adds Korn Ferry as a distinct executive-search, interim-capacity, consulting,
Digital, and RPO lane, separate from enterprise workflow software, technical
inspection, healthcare staffing, and recurring route services. It tests
solution-level mix, remaining-fee conversion, professional utilization,
compensation, collection, platform investment, acquisitions, debt, SBC, and
diluted common residual. Remaining fees, bookings, adjusted EBITDA, OCF, and
buybacks remain diagnostic until delivery, utilization, collection, and
per-share cash joins are evidenced.

The new [oilfield-services valuation/liquidity workbench](combined-investment-research-oilfield-services-valuation-liquidity-workbench-2026-09-18.md)
adds Halliburton as a distinct service-execution and customer-capex lane,
separate from upstream producers, integrated oil, and energy infrastructure.
It tests pressure-pumping and drilling utilization, service intensity, fleet
renewal, receivables, inventory, international mobilization, claims, debt, and
diluted common residual. Revenue, segment margin, OCF, FCF, production
activity, and buybacks remain diagnostic until service, collection, renewal,
and per-share cash joins are evidenced.

The new [engine and power-systems valuation/liquidity workbench](combined-investment-research-engine-power-systems-valuation-liquidity-workbench-2026-09-18.md)
adds Cummins as a distinct physical-equipment and installed-reliability lane,
separate from merchant power, grid components, HVAC, industrial automation,
and accelerated computing. It keeps Engine, Components, Distribution, Power
Systems, and Accelera separate while testing data-center demand, warranty,
emissions compliance, inventory, receivables, transition charges, debt, and
diluted common residual. Revenue, EBITDA, OCF, guidance, and dividends remain
diagnostic until shipment, service, warranty, collection, and replacement-capital
joins are evidenced.

The new [Gallagher brokerage and risk-advisory valuation/liquidity workbench](combined-investment-research-arthur-gallagher-brokerage-risk-advisory-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct fee-based insurance-distribution lane. It separates brokerage,
risk management, producer retention, acquisition cohorts, integration cash,
working capital, debt, and diluted common residual. Reported revenue, organic
fee growth, adjusted earnings, OCF, and acquisitions remain diagnostic until
collection, cohort-return, integration, and per-share cash joins are evidenced.

The new [Apple device ecosystem valuation/liquidity workbench](combined-investment-research-apple-device-ecosystem-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct device-and-services lane. It separates device sell-through,
installed-base retention, Services billing, supplier commitments, R&D, tariffs,
regulatory claims, capital returns, and diluted common residual. Revenue,
installed-base size, Services margin, OCF, FCF, and buybacks remain diagnostic
until collection, reinvestment, regulatory, and per-share cash joins are evidenced.

The new [Spotify recurring-audio platform valuation/liquidity workbench](combined-investment-research-spotify-recurring-audio-platform-valuation-liquidity-workbench-2026-09-18.md)
adds a distinct cultural-subscription lane. It separates Premium billing,
ad-supported reach, royalty and creator settlement, podcasts, audiobooks,
recommendation and AI investment, content returns, debt, and diluted common
residual. MAUs, subscribers, revenue, gross margin, FCF, and creator payouts
remain diagnostic until collection, payout, reinvestment, and per-share cash
joins are evidenced.

The new [waterworks and municipal distribution valuation/liquidity workbench](combined-investment-research-waterworks-municipal-distribution-valuation-liquidity-workbench-2026-09-18.md)
adds Core & Main as a distinct infrastructure-distribution lane, separate from
ordinary building-products distribution and broader built-environment channels.
It tests municipal and contractor project timing, branch density, inventory and
supplier rebates, acquisitions and greenfields, TRA, NCI, debt, and Class A
cash conversion. Sales, adjusted EBITDA, OCF, and repurchases remain diagnostic
until inventory, collection, acquisition-return, ownership-claim, and per-share
cash joins are evidenced.

The new [regional relationship-bank valuation/liquidity workbench](combined-investment-research-regional-relationship-bank-valuation-liquidity-workbench-2026-09-18.md)
The new [retirement insurance and PGIM asset-management valuation/liquidity workbench](combined-investment-research-retirement-insurance-pgim-valuation-liquidity-workbench-2026-09-18.md)
The new [civil construction and materials-integration valuation/liquidity workbench](combined-investment-research-civil-materials-integration-valuation-liquidity-workbench-2026-09-18.md)
The new [polyolefin feedstock and footprint-repair valuation/liquidity workbench](combined-investment-research-polyolefin-feedstock-footprint-valuation-liquidity-workbench-2026-09-18.md)
The new [ETF and index asset-management valuation/liquidity workbench](combined-investment-research-etf-index-asset-management-valuation-liquidity-workbench-2026-09-18.md)
The new [active and retirement asset-management valuation/liquidity workbench](combined-investment-research-active-retirement-asset-management-valuation-liquidity-workbench-2026-09-18.md)
adds T. Rowe Price as a distinct active-management and retirement-plan lane,
separate from Invesco's ETF/QQQ concentration, Franklin's product migration,
and Prudential's liability-backed PGIM model. It tests net flows, fee rates,
market-appreciation versus client additions, talent and distribution cost,
product transition, capital returns, and dilution. AUM, adjusted EPS,
dividends, and repurchases remain diagnostic until fee, flow, retention, and
per-share cash joins are evidenced.
The new [multi-asset gold and reserve-renewal valuation/liquidity workbench](combined-investment-research-multi-asset-gold-reserve-renewal-valuation-liquidity-workbench-2026-09-18.md)
The new [iron ore, base metals, and trust-repair valuation/liquidity workbench](combined-investment-research-iron-ore-base-metals-trust-repair-valuation-liquidity-workbench-2026-09-18.md)
adds Vale as a distinct Brazilian iron-ore and Base Metals lane, separate from
Kinross's gold portfolio and Glencore's marketing model. It tests the iron-ore
corridor, all-in cost, copper/nickel projects, Samarco/Brumadinho and dam claims,
expanded net debt, and diluted per-share residual rather than treating production
or recurring FCF as normalized owner cash.
The new [regulated water/gas and merger-funding valuation/liquidity workbench](combined-investment-research-regulated-water-gas-merger-valuation-liquidity-workbench-2026-09-18.md)
adds Essential Utilities as a distinct combined water/gas and merger-funding
lane, separate from American Water's pure regulated-water object. It tests
rate recovery, gas purchased-cost timing, PFAS settlement versus recurring
cash, acquisition cohorts, merger approval/integration, capital funding, debt,
dividends, and dilution. Rate base, connections, settlement proceeds, OCF, and
dividends remain diagnostic until recovery, collection, capital, merger, and
per-share joins are evidenced.
adds Kinross Gold as a distinct smaller multi-asset gold portfolio lane,
separate from Glencore's physical marketing model and larger diversified miners.
It tests mine-level grade/recovery, sustaining capital, reserve renewal,
Great Bear/Curlew/Phase X/Redbird/Lobo-Marte projects, repatriation/tax,
reclamation, debt, buybacks, and diluted common residual. Production, AISC,
FCF, impairment reversals, and capital returns remain diagnostic until mine,
project, cash-location, and per-share joins are evidenced.
adds Invesco as a distinct ETF/index-scale and product-concentration lane,
separate from Franklin's product-migration case and Prudential's liability-
backed PGIM model. It tests fee-paying AUM, product flows, fee rates, QQQ
dependence, active/fixed-income runoff, China JV economics, private-market
marks, impairment, technology, capital returns, and dilution. AUM, adjusted
earnings, dividends, and repurchases remain diagnostic until fee, flow,
distribution, and per-share cash joins are evidenced.
adds LyondellBasell as a distinct global polyolefin spread-cycle lane,
separate from other chemical models. It tests regional feedstock, utilization,
product spreads, plant renewal, European exits, Cash Improvement Plan savings,
working capital, JV distributions, environmental obligations, debt, dividends,
and dilution. EBITDA, plan targets, OCF, asset-sale proceeds, and repurchases
remain diagnostic until mid-cycle, footprint, capital, and per-share cash joins
are evidenced.
adds Granite Construction as a distinct civil-execution and owned-materials
lane, separate from specialty contractors and design/program managers. It tests
CAP conversion, contract assets, retainage, project estimates, materials
integration, equipment/plant capital, acquisitions, JV/NCI claims, convertible
debt, and diluted common residual. CAP, adjusted EBITDA, OCF, and recurring-
capital residual remain diagnostic until project collection, final margin,
acquisition return, and per-share cash joins are evidenced.
adds Prudential Financial as a distinct insurance, retirement, and fee-based
asset-management lane, separate from MetLife's existing workbench. It tests
policyholder claims, reserves, spread, PGIM flows and fee rates, statutory
capital, subsidiary remittances, parent liquidity, debt, and dilution. Adjusted
operating income, AUM, book value, dividends, and repurchases remain diagnostic
until liability, capital-transfer, and per-share cash joins are evidenced.
adds M&T Bank as a distinct regional deposit-and-commercial-credit lane,
separate from national transaction banks and consumer-credit platforms. It
tests deposit beta, NIM normalization, CRE and regional credit, reserves,
securities liquidity, treasury/payment investment, CET1, dividends, buybacks,
and diluted common value. EPS, deposits, loan growth, NIM, and ROTCE remain
diagnostic until funding, credit, capital, liquidity, and per-share joins are
evidenced.

The new [luxury home and destination retail valuation/liquidity workbench](combined-investment-research-luxury-home-destination-retail-valuation-liquidity-workbench-2026-09-18.md)
adds RH as a distinct luxury identity and destination-retail lane, separate
from household-value retail, Williams-Sonoma's broader home model, and
Wayfair's logistics-mediated marketplace. It tests order-to-revenue conversion,
inventory aging, galleries, design services, hospitality, housing sensitivity,
leases, debt, stock compensation, and diluted common residual. Demand, revenue,
adjusted earnings, OCF, and buybacks remain diagnostic until unit, collection,
maintenance, hospitality, and per-share cash joins are evidenced.

The new [mining and commodity-marketing valuation/liquidity workbench](combined-investment-research-mining-commodity-marketing-valuation-liquidity-workbench-2026-09-18.md)
adds Glencore as a distinct integrated physical-marketing lane, separate from
mine-only producers and royalty/streaming. It tests Marketing Adjusted EBIT,
industrial mine cash, inventory funding, net funding, working-capital releases,
copper project capital, partner claims, leases, debt, and diluted common
residual. FFO, production, marketing earnings, asset sales, dividends, and
buybacks remain diagnostic until through-cycle, funding, project-return, and
per-share cash joins are evidenced.

The new [field-execution digital-infrastructure valuation/liquidity workbench](combined-investment-research-field-execution-digital-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
adds Dycom as the downstream execution counterpart to AECOM's upstream design
lane. It separates MSA backlog from firm work and tests customer concentration,
crews, equipment, receivables, contract assets, insurance, surety, Power
Solutions integration, debt, and dilution. Backlog, book-to-bill, adjusted
EBITDA, FCF, and repurchases remain diagnostic until funded-start and
common-residual joins are evidenced.

The new [wildfire-liability regulated-utility valuation/liquidity workbench](combined-investment-research-wildfire-liability-regulated-utility-valuation-liquidity-workbench-2026-09-18.md)
adds Edison International as a catastrophe-liability utility lane distinct from
ordinary rate-base recovery. It tests placed-in-service return, wildfire claims,
insurance and Wildfire Fund cash, regulatory assets, securitization,
affordability, debt, preferred claims, and dilution. Core EPS, rate base, capex,
dividends, and recovery balances remain diagnostic until recovery and
common-residual joins are evidenced.

The new [custom silicon and optical-interconnect valuation/liquidity workbench](combined-investment-research-custom-silicon-optical-interconnect-valuation-liquidity-workbench-2026-09-18.md)
adds Marvell as a design-win-to-shipment lane distinct from Broadcom's broader
silicon/software model and semiconductor equipment. It tests custom compute,
optics, switching, qualification, customer concentration, inventory, R&D,
Celestial AI integration, debt, SBC, and dilution. Bookings, revenue,
non-GAAP earnings, OCF, and repurchases remain diagnostic until collected-cash
and common-residual joins are evidenced.

The new [royalty and streaming valuation/liquidity workbench](combined-investment-research-royalty-streaming-valuation-liquidity-workbench-2026-09-18.md)
adds Franco-Nevada as a contractual natural-resources lane distinct from
operating miners and producers. It separates producing, development, and
optionality cohorts, GEOs, commodity mix, operator production/payment,
counterparty and permitting risk, Cobre Panama, acquisitions, taxes, and
dilution. GEO growth, OCF, debt-free status, dividends, and available capital
remain diagnostic until asset-level cash joins are evidenced.

The new [security trust and trust-recovery valuation/liquidity workbench](combined-investment-research-security-trust-recovery-valuation-liquidity-workbench-2026-09-18.md)
adds CrowdStrike as a cybersecurity-control lane. It tests endpoint/cloud/
identity telemetry, renewal, module expansion, deferred revenue, cloud/AI cost,
the July 19 Incident, remediation, SBC, acquisitions, and dilution. ARR,
subscription revenue, adjusted FCF, OCF, and repurchases remain diagnostic until
retention, incident, and per-share-cash joins are evidenced.

The new [hotel property-owner valuation/liquidity workbench](combined-investment-research-hotel-property-owner-valuation-liquidity-workbench-2026-09-18.md)
adds Apple Hospitality REIT as a physical hotel-owner lane distinct from hotel
brands and senior-housing property models. It tests occupancy, ADR, RevPAR,
property margin, third-party management and brand fees, replacement/renovation
capital, dispositions, debt, REIT obligations, and dilution. RevPAR, Adjusted
EBITDAre, FFO/AFFO, distributions, and asset sales remain diagnostic until
distributable-cash joins are evidenced.

The new [healthcare middle-layer and delegated-risk valuation/liquidity workbench](combined-investment-research-healthcare-middle-layer-delegated-risk-valuation-liquidity-workbench-2026-09-18.md)
adds Astrana as a provider/payer coordination lane distinct from payers,
devices, distribution, infusion, and home care. It tests Care Partners, Care
Delivery, Care Enablement, retained margin per patient, medical cost, claims,
provider payments, subsidiary capital, Prospect integration, debt, and dilution.
Patient counts, revenue, adjusted EBITDA, FCF, AI claims, and acquisitions
remain diagnostic until retained-margin and common-residual joins are evidenced.

The new [lifestyle retail and inventory-cash valuation/liquidity workbench](combined-investment-research-lifestyle-retail-inventory-valuation-liquidity-workbench-2026-09-18.md)
adds Williams-Sonoma as a multi-brand design-led retail lane. It tests
transactions and repeat demand, brand/channel mix, inventory turns, markdowns,
tariffs, freight, vendor terms, stores, e-commerce, design services, loyalty,
leases, buybacks, and dilution. Comparable sales, margin, EPS, OCF, dividends,
and repurchases remain diagnostic until inventory-cash and common-residual joins
are evidenced.

The new [single-asset gold mine valuation/liquidity workbench](combined-investment-research-single-asset-gold-mine-valuation-liquidity-workbench-2026-09-18.md)
adds Lundin Gold as a concentrated operating-mine lane distinct from royalty
and streaming portfolios. It tests Fruta del Norte production, grade, recovery,
realized gold price, AISC, royalties, tax, employee and government profit
sharing, sustaining and development capital, mine-life, Ecuador obligations,
district options, dividends, and dilution. Production, AISC, OCF, FCF, gold
price, dividends, and exploration options remain diagnostic until production-
cost, reserve, renewal-capital, country, and common-residual joins are evidenced.

The new [travel distribution and payments valuation/liquidity workbench](combined-investment-research-travel-distribution-payments-valuation-liquidity-workbench-2026-09-18.md)
adds Booking Holdings as a travel-interface lane distinct from hotel ownership,
local delivery, and alternative-accommodation ownership. It tests agency and
merchant mix, gross bookings, retained contribution, supplier settlement,
payments, refunds, fraud, marketing, support, direct/app/loyalty behavior,
Connected Trip attachment, debt, SBC, and dilution. Gross bookings, room
nights, merchant mix, adjusted EBITDA less capex, and repurchases remain
diagnostic until retained-contribution, settlement, and common-residual joins
are evidenced.

The new [diversified mining and commodity portfolio valuation/liquidity workbench](combined-investment-research-diversified-mining-commodity-portfolio-valuation-liquidity-workbench-2026-09-18.md)
adds BHP as an asset-level mining lane distinct from single-asset gold mining
and royalty/streaming portfolios. It tests iron ore, copper, coal, and potash
production, realized prices, grades, ownership, sustaining and growth capital,
JV and non-controlling cash, Samarco, closure, debt, dividends, and dilution.
Production, EBITDA, management FCF, asset-sale proceeds, dividends, and copper
exposure remain diagnostic until asset-level returns and common-owner cash are
joined.

The new [pharma and MedTech portfolio-renewal valuation/liquidity workbench](combined-investment-research-pharma-medtech-portfolio-renewal-valuation-liquidity-workbench-2026-09-18.md)
adds Johnson & Johnson as a diversified healthcare portfolio lane distinct from
single-device, distribution, and delegated-risk models. It tests Innovative
Medicine patent/exclusivity, pipeline and R&D, MedTech procedure and quality
economics, acquisitions, acquired IPR&D, litigation, working capital, debt,
dividends, and dilution. Sales, adjusted EPS, OCF, dividends, and buybacks
remain diagnostic until portfolio-renewal and common-cash joins are evidenced.

The new [LNG liquefaction and export infrastructure valuation/liquidity workbench](combined-investment-research-lng-liquefaction-export-infrastructure-valuation-liquidity-workbench-2026-09-18.md)
adds Cheniere as a train-level export-infrastructure lane distinct from
upstream gas, integrated oil, and regulated midstream. It tests train
availability, contracted and merchant volumes, feedgas, realized margin,
derivative cash versus marks, maintenance and growth capital, Stage 3,
counterparties, debt, buybacks, and dilution. DCF, adjusted EBITDA, contracted
capacity, GAAP earnings, dividends, and repurchases remain diagnostic until
train-level owner-cash joins are evidenced.

The new [edge network and application-security valuation/liquidity workbench](combined-investment-research-edge-network-application-security-valuation-liquidity-workbench-2026-09-18.md)
adds Cloudflare as a distributed network-control lane distinct from data-cloud
consumption, endpoint security, and enterprise workflow software. It tests
customer retention, RPO conversion, traffic/workload, platform attachment,
bandwidth and network cost, support, R&D, restructuring, SBC, leases, debt,
and dilution. Revenue, RPO, non-GAAP income, FCF, adjusted metrics, and
repurchases remain diagnostic until network-return and diluted-owner-cash joins
are evidenced.

The new [installed network and subscription-platform valuation/liquidity workbench](combined-investment-research-installed-network-subscription-platform-valuation-liquidity-workbench-2026-09-18.md)
adds Cisco as a mature enterprise network and security platform lane distinct
from Arista/Ciena network control, Cloudflare edge trust, and Broadcom custom
silicon/software. It tests installed-base renewal, subscription/RPO delivery,
AI-order shipment, inventory, receivables, Splunk return, support, SBC, debt,
and dilution. Orders, RPO, subscription revenue, FCF, adjusted metrics,
dividends, and buybacks remain diagnostic until recurring per-share cash is
evidenced.

The new [upstream shale and resource-play valuation/liquidity workbench](combined-investment-research-upstream-shale-resource-play-valuation-liquidity-workbench-2026-09-18.md)
adds EOG Resources as a basin-level upstream lane distinct from integrated
oil, LNG export, midstream, oilfield services, mining, and royalty models. It
tests product mix, realized prices, decline, drilling, reserve replacement,
gathering, impairments, environmental obligations, SBC, dividends, and
dilution. BOE, reserves, FCF, adjusted cash flow, dividends, and repurchases
remain diagnostic until mid-cycle reserve-renewal cash is evidenced.

The new [data-center power and thermal systems valuation/liquidity workbench](combined-investment-research-data-center-power-thermal-systems-valuation-liquidity-workbench-2026-09-18.md)
adds Vertiv as a physical deployment and uptime lane distinct from nVent's
electrical protection, network software, and data-center property models. It
tests backlog shipment, project margin, working capital, warranty, service
labor, capacity, PurgeRite return, debt, SBC, and dilution. Backlog, orders,
adjusted margin, adjusted FCF, and buybacks remain diagnostic until physical
system cash conversion is evidenced.

The new [Forrester research and AI-transition valuation/liquidity workbench](combined-investment-research-forrester-research-ai-transition-valuation-liquidity-workbench-2026-09-18.md)
extends the institutional-research lane with Forrester as a negative-transition
case beside Gartner. It tests contract value, renewals, research memberships,
consulting, events, AI delivery, goodwill impairment, restructuring, office
capital, debt, SBC, and dilution. Contract value, adjusted earnings, AI usage,
OCF, and repurchases remain diagnostic until contract stabilization and common
residual are evidenced.

The new [heavy equipment, dealer channel, and finance valuation/liquidity workbench](combined-investment-research-heavy-equipment-dealer-finance-valuation-liquidity-workbench-2026-09-18.md)
adds Caterpillar as a machine-ecosystem lane distinct from contractors,
industrial components, data-center systems, and commodity producers. It tests
equipment, services, Power & Energy, Resource Industries, dealer inventory,
Cat Financial receivables, warranty, tariffs, capex, debt, SBC, and dilution.
Backlog, services, adjusted profit, tariff recovery, dividends, and buybacks
remain diagnostic until cycle-adjusted owner cash is evidenced.

The new [focused copper mine and smelter valuation/liquidity workbench](combined-investment-research-focused-copper-mine-smelter-valuation-liquidity-workbench-2026-09-18.md)
adds Freeport-McMoRan as a copper-focused mine and processing lane distinct
from BHP's diversified portfolio and Lundin Gold's single-asset gold model. It
tests grade/recovery, gold and molybdenum credits, Grasberg restart, smelters,
operating rights, Indonesia cash restrictions, environmental obligations,
project capital, debt, dividends, and dilution. Reserves, unit cash cost, FCF,
dividends, and project options remain diagnostic until full-cycle cash is joined.

The new [deposit franchise and consumer-credit valuation/liquidity workbench](combined-investment-research-deposit-franchise-consumer-credit-valuation-liquidity-workbench-2026-09-18.md)
adds Bank of America as a money-center bank lane distinct from private credit,
card-specialist, and industrial owner-cash models. It tests deposits and beta,
funding, loans, credit migration, reserves, charge-offs, markets normalization,
technology/control costs, liquidity, CET1, stress capital, dividends, and
dilution. EPS, deposits, loans, digital users, ROTE, dividends, and repurchases
remain diagnostic until risk-adjusted common return is evidenced.

The new [diversified gold producer and portfolio-renewal valuation/liquidity workbench](combined-investment-research-diversified-gold-producer-portfolio-renewal-valuation-liquidity-workbench-2026-09-18.md)
adds Newmont as a mine-portfolio lane distinct from Lundin Gold's single asset,
Freeport's focused copper/smelter model, BHP's broad commodity portfolio, and
royalty companies. It tests mine production, grade/recovery, byproducts,
sustaining and growth capital, projects, reserves, closure, divestitures,
host-country obligations, debt, dividends, and dilution. Ounces, reserves,
FCF, adjusted EBITDA, divestiture proceeds, and repurchases remain diagnostic
until full-cycle cash is joined.

The new [global transaction-bank turnaround valuation/liquidity workbench](combined-investment-research-global-transaction-bank-turnaround-valuation-liquidity-workbench-2026-09-18.md)
adds Citigroup as a global institutional-network and transformation lane
distinct from Bank of America's domestic deposit franchise and private-credit
models. It tests Services, Markets, Banking, Wealth, USCC cards, control and
technology cost, legacy/divestiture residuals, credit, liquidity, CET1, stress
capital, dividends, and dilution. EPS, RoTCE, revenue, liquidity resources,
divestitures, and repurchases remain diagnostic until turnaround returns persist.

The new [regional regulated utility and large-load valuation/liquidity workbench](combined-investment-research-regional-regulated-utility-large-load-valuation-liquidity-workbench-2026-09-18.md)
adds Alliant Energy as a smaller regional rate-base and customer-specific-load
lane distinct from AEP's broader buildout and merchant-power models. It tests
energized load, customer funding, construction, in-service recovery, allowed
versus earned return, affordability, debt, equity, storms, dividends, and
dilution. Signed load, rate base, planned capex, EPS, dividends, and repurchases
remain diagnostic until project recovery and per-share return are evidenced.

The new [procedure-led MedTech acquisition and lifecycle valuation/liquidity workbench](combined-investment-research-procedure-medtech-acquisition-lifecycle-valuation-liquidity-workbench-2026-09-18.md)
adds Boston Scientific as a procedure-adoption and acquired-device lane distinct
from Stryker/Intuitive/Henry Schein. It tests cardiovascular and MedSurg
procedures, clinical adoption, reimbursement, R&D, quality, inventory,
acquisition cohorts, integration, debt, SBC, and dilution. Sales, organic
growth, procedures, adjusted EPS, OCF, dividends, and repurchases remain
diagnostic until lifecycle cash is evidenced.

The new [semiconductor materials-engineering valuation/liquidity workbench](combined-investment-research-semiconductor-materials-engineering-valuation-liquidity-workbench-2026-09-18.md)
adds Applied Materials as a qualified-process and installed-service lane
distinct from Lam Research's deposition/etch model and KLA's process control.
The September 18 expectation refresh places Applied Materials at approximately
`$355.656B` of equity value and its annualized first-nine-month FY2026 OCF-less-
capex screen at approximately `$4.773B`, or `74.5x`. The screen remains
diagnostic: `$698M` contract-liability growth, `$1.8B` opening-liability revenue
recognition, `30%` FY2025 China revenue, `34%` first-nine-month customer
concentration, `$545M` SBC, and process/R&D/service reinvestment prevent
promotion to normalized owner cash.
It tests tool acceptance, AGS service, contract liabilities, inventory,
foundry/logic and memory mix, China/export exposure, R&D, facilities, customer
concentration, SBC, and dilution. Tool revenue, AGS, margins, OCF, and
repurchases remain diagnostic until process and per-share cash are evidenced.

The new [engineered materials and acetyl-chain valuation/liquidity workbench](combined-investment-research-engineered-materials-acetyl-chain-valuation-liquidity-workbench-2026-09-18.md)
adds Celanese as a distinct qualified-materials and chemical-chain lane,
separate from integrated midstream logistics and broad commodity chemicals. It
tests Engineered Materials versus Acetyl Chain, price/volume/mix, customer
qualification, utilization, footprint actions, restructuring, environmental
cash, goodwill, refinancing, debt, and diluted common residual. Adjusted EBITDA,
adjusted EPS, management FCF, OCF, and repurchases remain diagnostic until
mid-cycle margin, closure, debt, and per-share cash joins are evidenced.

The new [data-cloud consumption valuation/liquidity workbench](combined-investment-research-data-cloud-consumption-valuation-liquidity-workbench-2026-09-18.md)
adds Snowflake as a distinct usage-based data-control lane, separate from
Oracle's owned-capacity database/cloud build, Alphabet's advertising and cloud
platform, and Palo Alto Networks' security consolidation. It tests consumption
cohorts, NRR, RPO and prepaid capacity, third-party cloud/GPU/inference cost,
capitalized software, deferred commissions, SBC, and diluted common residual.
Product revenue, RPO, OCF, company-defined FCF, and repurchases remain
diagnostic until usage durability, delivery margin, collection, and per-share
cash joins are evidenced.

The new [custom electrical systems and project-conversion valuation/liquidity workbench](combined-investment-research-custom-electrical-systems-project-conversion-valuation-liquidity-workbench-2026-09-18.md)
adds Powell Industries as a distinct custom-engineering and milestone-funded
project lane, separate from grid components, electrical distribution, and large
generation equipment. It tests bookings and backlog conversion, project margin,
contract assets and liabilities, receivables, fixed-price execution, warranty,
end-market mix, facility expansion, letters of credit, acquisitions, and
diluted common residual. Bookings, backlog, revenue, OCF, and dividends remain
diagnostic until collected project cash, capacity return, and per-share joins
are evidenced.

The new [AI underwriting and lending-marketplace valuation/liquidity workbench](combined-investment-research-ai-underwriting-lending-marketplace-valuation-liquidity-workbench-2026-09-18.md)
adds Upstart as a distinct partner-funded underwriting and origination lane,
separate from balance-sheet consumer lenders and payment networks. It tests
model conversion, funded-loan cohorts, partner capital, fee rates, loan-sale
terms, retained exposure, repurchase and indemnity claims, fair-lending
compliance, technology cost, and diluted common residual. Originations,
automation, revenue, adjusted EBITDA, OCF, and repurchases remain diagnostic
until funded-loan quality, partner returns, and per-share cash joins are
evidenced.

The new [home medical equipment and recurring-resupply valuation/liquidity workbench](combined-investment-research-home-medical-equipment-resupply-valuation-liquidity-workbench-2026-09-18.md)
adds AdaptHealth as a distinct home-continuity and resupply lane, separate from
hospitals, devices, specialty pharmacy, and healthcare payment workflow. It
tests equipment placement, active patients, recurring supplies, payer
authorization, referral access, capitated contracts, delivery and field
service, inventory, receivables, goodwill, divestiture, debt, and diluted
common residual. Patient count, organic revenue, adjusted EBITDA, FCF, OCF, and
repurchases remain diagnostic until resupply, paid-claim, contract, and
per-share cash joins are evidenced.

The new [local-commerce delivery marketplace valuation/liquidity workbench](combined-investment-research-local-commerce-delivery-marketplace-valuation-liquidity-workbench-2026-09-18.md)
adds DoorDash as a distinct consumer-merchant-Dasher coordination lane,
separate from Uber mobility/delivery, eBay goods transactions, and Shopify
merchant software. It tests organic orders and GOV, retained contribution per
order, merchant and Dasher health, membership, advertising, insurance,
regulatory cost, Deliveroo integration, capitalized software, SBC, processor
funds, and diluted common residual. GOV, orders, members, adjusted EBITDA, FCF,
OCF, and repurchases remain diagnostic until contribution, settlement,
integration, and per-share cash joins are evidenced.

The new [refining, renewable fuels, and specialty-products valuation/liquidity workbench](combined-investment-research-refining-specialty-products-valuation-liquidity-workbench-2026-09-18.md)
adds HF Sinclair as a distinct downstream and specialty-products lane, separate
from upstream, midstream, LNG, and oilfield-services models. It tests refinery
crack spreads, utilization, turnarounds, inventory valuation, derivative
settlement, renewable credits, specialty cash, midstream and marketing, the
planned separation, environmental obligations, debt, and diluted common
residual. EBITDA, OCF, FCF, dividends, repurchases, inventory benefits, and
credits remain diagnostic until mid-cycle and per-share cash joins are
evidenced.

The new [custom silicon and infrastructure-software valuation/liquidity workbench](combined-investment-research-custom-silicon-infrastructure-software-valuation-liquidity-workbench-2026-09-18.md)
adds Broadcom as a distinct custom-ASIC and infrastructure-software lane,
separate from NVIDIA's platform, semiconductor equipment, and active networking
models. It tests AI and non-AI silicon, design-in durability, software renewal,
VMware pricing and migration, customer concentration, supplier commitments,
acquisition integration, debt, SBC, and diluted common residual. AI revenue,
software revenue, adjusted EBITDA, FCF, and repurchases remain diagnostic until
design-win, renewal, acquisition-return, and per-share cash joins are
evidenced.

The new [regulated electric/gas rate-base valuation/liquidity workbench](combined-investment-research-regulated-electric-gas-rate-base-valuation-liquidity-workbench-2026-09-18.md)
adds Fortis as a distinct multi-jurisdiction regulated-utility lane, separate
from American Water's water-only model and merchant power. It tests placed-in-
service rate base, regulatory recovery, construction work in progress, allowed
returns, project approval, financing, affordability, storm/wildfire, currency,
subsidiary capital, debt, dividends, and diluted common residual. Planned rate
base, capex, adjusted EPS, dividends, and repurchases remain diagnostic until
recovery, earned-return, financing, and per-share cash joins are evidenced.

The new [packaged meals and snacks valuation/liquidity workbench](combined-investment-research-packaged-meals-snacks-valuation-liquidity-workbench-2026-09-18.md)
adds The Campbell's Company as a distinct packaged-food portfolio lane,
separate from beverages, spirits, oral care, and broad retail. It tests Meals &
Beverages versus Snacks, in-market volume, household penetration, retailer shelf
and trade promotion, price/volume/mix, ingredients, packaging, freight, brand
investment, Rao's/Sovos return, inventory, debt, and diluted common residual.
Sales, adjusted EBIT/EPS, OCF, FCF, and repurchases remain diagnostic until
volume, margin, portfolio-return, and per-share cash joins are evidenced.

The new [full-service dining direct-operator valuation/liquidity workbench](combined-investment-research-full-service-dining-direct-operator-valuation-liquidity-workbench-2026-09-18.md)
adds Darden as a company-operated restaurant lane. It separates guest traffic,
price/mix, food, labor, occupancy, maintenance/remodel capital, new-unit
returns, Chuy's integration, leases, debt, and dilution from franchise
royalties. Same-restaurant sales, adjusted EPS, EBITDA, OCF, and repurchases
remain diagnostic until traffic, mature-unit return, capital, lease, and
common-residual joins are evidenced.

The new [infrastructure design and program-management valuation/liquidity workbench](combined-investment-research-infrastructure-design-program-management-valuation-liquidity-workbench-2026-09-18.md)
adds AECOM as an upstream infrastructure-control lane. It separates
fee-bearing adjusted NSR from gross/pass-through revenue and backlog, and tests
project estimates, receivables, contract assets, claims, regional collection,
acquisitions, joint ventures, debt, and dilution. Gross revenue, backlog,
book-to-burn, adjusted metrics, FCF, and repurchases remain diagnostic until
project-conversion and common-residual joins are evidenced.

The new [thrift-to-business-bank valuation/liquidity workbench](combined-investment-research-thrift-to-business-bank-valuation-liquidity-workbench-2026-09-18.md)
adds WaFd as a regional funding-and-credit transition lane. It separates
transaction deposits from time deposits and borrowings, legacy real estate from
new business banking, and reported ROATCE/NIM from credit migration, capital,
liquidity, tangible value, and diluted common residual. Net income, EPS,
efficiency, and repurchases remain diagnostic until deposit-credit-capital joins
are evidenced.

The new [public-market asset-management valuation/liquidity workbench](combined-investment-research-public-market-asset-management-valuation-liquidity-workbench-2026-09-18.md)
adds Franklin Resources as a fee-paying relationship and product-migration
lane. It separates legacy active, ETF/SMA, alternatives, Western Asset,
market appreciation, flows, fee rates, talent, distribution, remediation,
technology, debt, and dilution. Headline AUM, adjusted earnings, dividends,
and repurchases remain diagnostic until fee-paying-flow and common-residual
joins are evidenced.

The new [semiconductor deposition, etch, and installed-service valuation/liquidity workbench](combined-investment-research-semiconductor-deposition-etch-service-valuation-liquidity-workbench-2026-09-18.md)
adds Lam Research as a distinct process-equipment and installed-service lane,
separate from lithography, process control, and electronic test. It tests systems
versus support revenue, customer acceptance, deferred revenue, Japan-held
inventory, customer concentration, China/export exposure, R&D, labs, supplier
commitments, capacity, and diluted common residual. Systems revenue, support
growth, OCF, FCF, dividends, and repurchases remain diagnostic until acceptance,
reinvestment, policy, and per-share cash joins are evidenced.

The new [specialty underwriting, float, and decentralized-capital valuation/liquidity workbench](combined-investment-research-specialty-underwriting-float-conglomerate-valuation-liquidity-workbench-2026-09-18.md)
adds Markel as a distinct specialty-insurance and operating-company capital
allocation lane, separate from carrier and brokerage models. It tests current-
year underwriting, reserve development, catastrophe and reinsurance exposure,
invested-asset liquidity, subsidiary capital, operating-company returns, parent
debt, and diluted common residual. Premiums, combined ratio, adjusted operating
income, OCF, dividends, and repurchases remain diagnostic until reserve,
recovery, asset-liquidity, allocation, and per-share cash joins are evidenced.

The new [integrated midstream hydrocarbon-logistics valuation/liquidity workbench](combined-investment-research-integrated-midstream-hydrocarbon-logistics-valuation-liquidity-workbench-2026-09-18.md)
adds ONEOK as a distinct gathering, processing, NGL, storage, and transport
lane, separate from upstream producers, merchant power, and industrial
infrastructure. It tests organic versus acquired volume, maintenance versus
growth capex, affiliate distributions, commodity and optimization exposure,
working capital, debt, project utilization, and diluted common residual.
Throughput, adjusted EBITDA, OCF, FCF, dividends, and repurchases remain
diagnostic until collected cash, project return, leverage, and per-share joins
are evidenced.

The new [AI systems distribution and financing valuation/liquidity workbench](combined-investment-research-ai-systems-distribution-financing-valuation-liquidity-workbench-2026-09-18.md)
adds Dell Technologies as a distinct customer-facing systems and credit lane,
separate from NVIDIA's architecture/software platform, builder cloud, and
electronic test equipment. It tests AI-server margin, backlog conversion,
financing receivables, operating leases, inventory, customer concentration,
supplier terms, warranty, debt, SBC, and diluted common residual. Orders,
backlog, adjusted FCF, OCF, and repurchases remain diagnostic until shipment,
collection, credit, services, and per-share cash joins are evidenced.

The new [mission-critical public-safety workflow valuation/liquidity workbench](combined-investment-research-mission-critical-public-safety-workflow-valuation-liquidity-workbench-2026-09-18.md)
adds Motorola Solutions as a distinct institutional safety and response-
workflow lane, separate from defense mission systems, passive connectivity,
and general networking. It tests radio and broadband networks, dispatch,
video/evidence, cybersecurity, managed services, backlog acceptance,
implementation, acquisitions, earnouts, goodwill, debt, SBC, and diluted
common residual. Backlog, software/services growth, adjusted EPS, OCF, and
buybacks remain diagnostic until acceptance, collection, acquired-return,
support-cost, and per-share cash joins are evidenced.

The new [electronics distribution valuation/liquidity workbench](combined-investment-research-electronics-distribution-valuation-liquidity-workbench-2026-09-18.md)
adds Avnet as a distinct component-availability and design-support lane,
separate from industrial procurement, semiconductor manufacturing, electronic
test, and networking control. It tests Electronic Components versus Farnell
mix, inventory velocity, receivables, supplier return rights, obsolescence,
design support, warehouses, debt, taxes, SBC, and diluted common residual.
Sales, gross margin, adjusted EPS, inventory days, OCF, and buybacks remain
diagnostic until inventory, supplier-protection, collection, debt, and
per-share cash joins are evidenced.

The new [qualified dispensing and packaging valuation/liquidity workbench](combined-investment-research-qualified-dispensing-packaging-valuation-liquidity-workbench-2026-09-18.md)
adds AptarGroup as a distinct qualified component and dosing-interface lane,
separate from medical devices, consumer staples, semiconductor hardware, and
industrial chemicals. It tests Pharma, Beauty, and Closures mix, customer
qualification, product launches, quality and clean-room investment, materials,
plant utilization, tooling, capex, acquisitions, debt, SBC, and diluted common
residual. Sales, adjusted EBITDA/EPS, Pharma growth, OCF, and buybacks remain
diagnostic until core demand, qualification returns, quality investment, and
per-share cash joins are evidenced.

The new [crop-protection chemistry valuation/liquidity workbench](combined-investment-research-crop-protection-chemistry-valuation-liquidity-workbench-2026-09-18.md)
adds FMC as a distinct crop-protection chemistry and leveraged portfolio-repair
lane, separate from fertilizer, agribusiness processing, materials, and
industrial chemicals. It tests active-ingredient life cycles, registrations,
price/volume, formulation, manufacturing reset, inventory, receivable
factoring, restructuring, India/portfolio changes, debt, and diluted common
residual. Adjusted EBITDA, new-product sales, factoring, OCF, and asset-sale
proceeds remain diagnostic until product replacement, working-capital,
leverage, and per-share cash joins are evidenced.

The new [distributed resilience power valuation/liquidity workbench](combined-investment-research-distributed-resilience-power-valuation-liquidity-workbench-2026-09-18.md)
adds Generac as a distinct distributed backup-power, controls, storage, and
monitoring lane, separate from merchant power, utilities, grid infrastructure,
industrial uptime, and equipment rental. It tests residential versus C&I and
data-center demand, backlog conversion, inventory, warranty, dealer/service,
factory capacity, tariffs, legal claims, capex, debt, SBC, and diluted common
residual. Backlog, adjusted EBITDA, C&I growth, tariff refunds, OCF, and
buybacks remain diagnostic until shipment, collection, warranty, margin-after-
refund, and per-share cash joins are evidenced.

The new [institutional research and advisory valuation/liquidity workbench](combined-investment-research-institutional-research-advisory-valuation-liquidity-workbench-2026-09-18.md)
adds Gartner as a distinct decision-support, Insights, conference, and
consulting lane, separate from enterprise workflow software, talent advisory,
insurance brokerage, and advertising measurement. It tests contract value,
renewal and wallet retention, conference attendance, consulting utilization,
deferred revenue/commissions, analyst labor, collection, debt, SBC, repurchases,
and diluted common residual. Contract value, retention, adjusted EBITDA, OCF,
and buybacks remain diagnostic until renewal, mix, cash normalization, and
per-share cash joins are evidenced.

The new [satellite connectivity valuation/liquidity workbench](combined-investment-research-satellite-connectivity-valuation-liquidity-workbench-2026-09-18.md)
adds Iridium Communications as a distinct orbital network and recurring-service
lane, separate from terrestrial networking, distributed power, merchant
generation, and enterprise software. It tests service and government renewal,
subscriber cohorts, direct-to-device economics, constellation and ground
replacement, launch/insurance, spectrum, engineering/equipment, debt, SBC,
and diluted common residual. Subscribers, service revenue, backlog, OCF, and
buybacks remain diagnostic until service collection, constellation reserve,
replacement, leverage, and per-share cash joins are evidenced.

The new [connected-operations IoT valuation/liquidity workbench](combined-investment-research-connected-operations-iot-valuation-liquidity-workbench-2026-09-18.md)
adds Samsara as a distinct connected-device and physical-workflow lane,
separate from enterprise workflow software, satellite connectivity, industrial
uptime, and equipment rental. It tests ARR and renewal, device activation and
replacement, inventory, cellular/cloud/AI cost, implementation, support,
commissions, customer ROI, SBC, capex, and diluted common residual. ARR,
non-GAAP margin, AI adoption, OCF, FCF, and buybacks remain diagnostic until
hardware renewal, GAAP cash, customer ROI, and per-share cash joins are
evidenced.

The new [facility services and building operations valuation/liquidity workbench](combined-investment-research-facility-services-valuation-liquidity-workbench-2026-09-18.md)
adds ABM Industries as a distinct outsourced site-operations lane, separate
from construction, industrial distribution, environmental services, healthcare,
and recurring route businesses. It tests staffing, wage recovery, bookings
conversion, receivables and unbilled work, claims, technical mix, equipment,
acquisitions, contingent consideration, leases, debt, and diluted common
residual. Revenue, bookings, adjusted EBITDA, OCF, and buybacks remain
diagnostic until billing, service, acquisition-return, and cash-per-site joins
are evidenced.

The new [semiconductor manufacturing valuation/liquidity workbench](combined-investment-research-semiconductor-manufacturing-valuation-liquidity-workbench-2026-09-18.md)
adds Micron and Intel as a distinct wafer/fab manufacturing lane, separate from
ASML lithography, KLA process control, and electronic test. It tests memory
pricing, HBM/DRAM/NAND yield, fab utilization, foundry production, inventory,
capex, incentives, export controls, debt, government-linked dilution, and
common residual. Revenue, gross margin, AI contracts, foundry announcements,
reported OCF, and FCF remain diagnostic until qualified production and capital
returns are evidenced.

The new [consumer-credit platforms valuation/liquidity workbench](combined-investment-research-consumer-credit-platforms-valuation-liquidity-workbench-2026-09-18.md)
adds Affirm and Synchrony as a distinct merchant-linked credit lane, separate
from regional banks and ordinary payments. It tests GMV/purchase volume,
merchant conversion, receivables, provisions, charge-offs, funding,
securitization, partner settlement, capital, SBC, and dilution. Activity,
NIM, loan sales, reported OCF, and buybacks remain diagnostic until credit,
funding, and common-residual joins are evidenced.

The new [enterprise workflow software valuation/liquidity workbench](combined-investment-research-enterprise-workflow-software-valuation-liquidity-workbench-2026-09-18.md)
adds Adobe and ServiceNow as a distinct embedded-workflow software lane. It
tests renewal, seat/module and usage expansion, AI monetization, deferred
revenue and commissions, cloud/support cost, R&D, SBC, acquisitions, debt, and
dilution. ARR, RPO, ACV, reported OCF, FCF, and buybacks remain diagnostic
until renewal, collection, delivery-cost, and common-residual joins are
evidenced.

The new [lithography-control valuation/liquidity workbench](combined-investment-research-lithography-control-valuation-liquidity-workbench-2026-09-18.md)
adds ASML as a distinct semiconductor-equipment control point, separate from
KLA's existing process-control lane. It tests system versus installed-base
service economics, acceptance, customer concentration, China/export policy,
backlog conversion, supplier capacity, R&D, and next-generation investment.
Systems revenue, backlog, service revenue, gross margin, and reported OCF remain
diagnostic until acceptance, collection, reinvestment, and common residual are
joined.

The new [specialty construction contractors valuation/liquidity workbench](combined-investment-research-specialty-construction-contractors-valuation-liquidity-workbench-2026-09-17.md)
extends the system to EMCOR, Comfort Systems, Quanta, MasTec, and Primoris.
It keeps specialty service, utility construction, communications, and renewable
project denominators separate while testing backlog/RPO conversion, labor,
contract assets and liabilities, retainage, cost-to-complete estimates,
acquisitions, claims, debt, and dilution. Backlog and reported OCF remain
diagnostic until project collection and final margin are evidenced.

The new [regional and commercial banking valuation/liquidity workbench](combined-investment-research-regional-banks-valuation-liquidity-workbench-2026-09-18.md)
adds PNC, Truist, U.S. Bancorp, and Regions as a distinct deposit-credit-
capital lane. It does not apply an industrial cash framework to banks; it tests
deposit beta, loan underwriting, credit losses, securities/liquidity, merger
repair, payments investment, CET1 capital, and tangible-common value. NII,
ROTCE, deposits, loan growth, CET1, dividends, and buybacks remain diagnostic
until the company-specific capital and common-residual joins are evidenced.

The new [insurance risk and brokerage valuation/liquidity workbench](combined-investment-research-insurance-risk-brokerage-valuation-liquidity-workbench-2026-09-18.md)
adds Chubb, Aon, and Marsh McLennan while keeping carrier underwriting and
policyholder liabilities separate from fee-led brokerage and advisory cash. It
tests premiums, claims, reserves, reinsurance, float, statutory capital,
commission/fee collection, receivables, talent, acquisitions, debt, pensions,
and dilution. Premiums, float, combined ratio, organic growth, and reported OCF
remain diagnostic until claims or fee-settlement and common-residual joins are
evidenced.

The new [rail network valuation/liquidity workbench](combined-investment-research-rail-network-valuation-liquidity-workbench-2026-09-18.md)
adds Union Pacific as a distinct hard-asset network lane. It tests carloads,
price/mix, fuel, labor, service, safety, maintenance and capacity capital,
terminals, technology, debt, and the proposed Norfolk Southern combination.
Operating ratio, pricing, reported OCF, dividends, and buybacks remain
diagnostic until network renewal, collection, merger obligations, and common
residual are joined.

The new [biopharma franchise valuation/liquidity workbench](combined-investment-research-biopharma-franchise-valuation-liquidity-workbench-2026-09-17.md)
adds Regeneron as a single-company product and pipeline lane. It separates
Dupixent and EYLEA franchise cash from collaboration settlement, R&D and
clinical replacement, manufacturing, patent defense, pricing, litigation, SBC,
and dilution. Product sales, collaboration revenue, pipeline milestones, and
reported OCF remain diagnostic until collection and replacement-cost joins are
evidenced.

The new [electronic interconnect content valuation/liquidity workbench](combined-investment-research-electronic-interconnect-content-valuation-liquidity-workbench-2026-09-18.md)
adds Amphenol as a distinct connector, sensor, cable, antenna, and power-
interconnect lane, separate from electronics distribution, semiconductor
manufacturing, networking control, and test equipment. It tests qualified
design-in, organic versus acquired growth, orders, book-to-bill, inventory,
capacity, tariffs, acquisition integration, debt, SBC, and diluted common
residual. Sales, orders, adjusted margin, EPS accretion, OCF, and buybacks
remain diagnostic until shipment, collection, inventory, acquisition-return,
tariff-normalization, and per-share cash joins are evidenced.

The new [sensing, imaging, and mission-systems valuation/liquidity workbench](combined-investment-research-teledyne-sensing-imaging-mission-systems-valuation-liquidity-workbench-2026-09-18.md)
adds Teledyne as a distinct physical-world sensing and mission-electronics lane.
It tests Digital Imaging, Instrumentation, Aerospace and Defense Electronics,
Engineered Systems, backlog acceptance, program margin, R&D, acquisition return,
debt, and diluted common residual.

The new [residential solar and storage subscriber-financing valuation/liquidity workbench](combined-investment-research-sunrun-residential-solar-storage-subscriber-financing-valuation-liquidity-workbench-2026-09-18.md)
adds Sunrun as a distinct household-energy and distributed-storage lane. It
separates subscriber value and contracted net earning assets from installation,
customer collection, churn, storage utilization, tax credits, safe-harbor
investments, project finance, recourse debt, and diluted common residual.

The new [travel marketplace, trust, and payments valuation/liquidity workbench](combined-investment-research-airbnb-travel-marketplace-trust-payments-valuation-liquidity-workbench-2026-09-18.md)
adds Airbnb as a distinct two-sided marketplace lane. It separates gross
booking value and nights from host/guest settlement, retained take rate,
payment processing, refunds, trust and safety, support, regulation, hotels,
experiences, services, AI infrastructure, and diluted common residual.

The new [route-based workplace services and UniFirst valuation/liquidity workbench](combined-investment-research-cintas-route-workplace-services-unifirst-valuation-liquidity-workbench-2026-09-18.md)
adds Cintas as a distinct outsourced workplace-services lane. It separates
route revenue and service density from garment and fleet renewal, plant labor,
customer retention, first-aid and fire-protection obligations, UniFirst funding
and integration, debt, and diluted common residual.

The new [imaging workflow and device-cycle valuation/liquidity workbench](combined-investment-research-canon-imaging-workflow-device-cycle-valuation-liquidity-workbench-2026-09-18.md)
adds Canon as a distinct multi-segment imaging and workflow-device lane. It
separates camera and network-camera sell-through from printing, medical and
industrial qualification, inventory, service/consumables, R&D, plant renewal,
memory and tariff effects, debt, and diluted common residual.

The new [appliance-plus-subscription cybersecurity valuation/liquidity workbench](combined-investment-research-fortinet-appliance-subscription-security-valuation-liquidity-workbench-2026-09-18.md)
adds Fortinet as a distinct hybrid security-infrastructure lane. It separates
product and service revenue, billings, and deferred revenue from appliance
sell-through, channel inventory, SASE/OT/AI delivery, threat intelligence, R&D,
SBC, warranty, debt, and diluted common residual.

The new [cement, carbon, and urbanization valuation/liquidity workbench](combined-investment-research-cemex-cement-carbon-urbanization-valuation-liquidity-workbench-2026-09-18.md)
adds CEMEX as a distinct global heavy-materials lane. It separates cement,
ready-mix, and aggregates price/volume from kiln and quarry renewal, energy and
freight, carbon obligations, public-program timing, housing, AI-linked
industrial demand, portfolio changes, impairment, debt, and diluted common
residual.

The new [appliance replacement-cycle and liquidity valuation workbench](combined-investment-research-whirlpool-appliance-replacement-liquidity-valuation-workbench-2026-09-18.md)
adds Whirlpool as a distinct household-durable replacement and liquidity lane.
It separates units and retailer sell-through from housing, consumer credit,
promotions, plant utilization, tariffs, domestic sourcing, warranty,
restructuring, debt refinancing, and diluted common residual.

The new [partner enrollment and workforce-education services valuation/liquidity workbench](combined-investment-research-grand-canyon-education-partner-enrollment-valuation-liquidity-workbench-2026-09-18.md)
adds Grand Canyon Education as a distinct institutional-interface and workforce-
training lane. It separates enrollment and service revenue from persistence,
revenue per student, partner contract changes, online delivery, off-campus
sites, ABSN capacity, compliance, litigation, reinvestment, and diluted common
residual.

The new [alumina, aluminum, and energy conversion valuation/liquidity workbench](combined-investment-research-alcoa-alumina-aluminum-energy-valuation-liquidity-workbench-2026-09-18.md)
adds Alcoa as a distinct vertically integrated metals-conversion lane. It
separates alumina, aluminum, bauxite, and energy price/volume from power,
smelter/refinery renewal, restarts, closures, remediation, carbon, JV funding,
portfolio proceeds, debt, and diluted common residual.

The new [accessible-luxury brand-house valuation/liquidity workbench](combined-investment-research-tapestry-accessible-luxury-brand-house-valuation-liquidity-workbench-2026-09-18.md)
adds Tapestry as a distinct accessible-luxury lane. It separates Coach and Kate
Spade brand demand from full-price sell-through, direct-to-consumer conversion,
Gen Z acquisition, inventory and markdowns, stores, China/Europe, tariffs,
licensing, restructuring, debt, and diluted common residual.

The new [electronics retail, marketplace, and services valuation/liquidity workbench](combined-investment-research-best-buy-electronics-marketplace-services-valuation-liquidity-workbench-2026-09-18.md)
adds Best Buy as a distinct omnichannel electronics-retail lane. It separates
device-category sell-through and comparable sales from vendor funding, inventory,
Geek Squad/services, Marketplace, Best Buy Ads, delivery, repair, trade-in,
leases, debt, and diluted common residual.

The new [discount-variety multi-price value-format valuation/liquidity workbench](combined-investment-research-dollar-tree-multiprice-value-format-valuation-liquidity-workbench-2026-09-18.md)
adds Dollar Tree as a distinct low-ticket value-format lane. It separates
traffic, ticket, and multi-price store economics from units/sell-through,
promotions, inventory, shrink, Dollar Tree 3.0 conversions, supply chain,
Family Dollar separation, leases, debt, and diluted common residual.

The new [consumables-heavy neighborhood convenience valuation/liquidity workbench](combined-investment-research-dollar-general-consumables-convenience-valuation-liquidity-workbench-2026-09-18.md)
adds Dollar General as a distinct rural and neighborhood replenishment lane. It
separates traffic and consumables mix from inventory per store, shrink, labor,
Project Renovate/Elevate, new stores, closures, private label, DG Media, supply
chain, leases, debt, and diluted common residual.

The new [beauty, fragrance, and portfolio-renovation valuation/liquidity workbench](combined-investment-research-coty-beauty-fragrance-portfolio-valuation-liquidity-workbench-2026-09-18.md)
adds Coty as a distinct prestige and consumer-beauty lane. It separates
fragrance and cosmetics sell-through from Consumer Beauty weakness, licensing,
retailer inventory, innovation, marketing, e-commerce, strategic review,
restructuring, FX, debt, and diluted common residual.

The new [wellness-community performance apparel valuation/liquidity workbench](combined-investment-research-lululemon-wellness-community-apparel-valuation-liquidity-workbench-2026-09-18.md)
adds lululemon as a distinct premium performance-and-wellness lane. It separates
Americas repair work and international growth from full-price sell-through,
product innovation, community marketing, inventory and markdowns, store/digital
productivity, sourcing, FX, tariffs, leases, debt, and diluted common residual.

The new [branded participation, ceremony, and franchise valuation/liquidity workbench](combined-investment-research-build-a-bear-participation-franchise-valuation-liquidity-workbench-2026-09-18.md)
adds Build-A-Bear as a distinct retailtainment and memory-making lane. It
separates ceremony and experience economics from direct stores, partner and
franchise channels, licensed product, gifting, inventory, tariffs, Vietnam
sourcing, occupancy, leases, and diluted common residual.

The new [IP-driven play, entertainment, and digital-games valuation/liquidity workbench](combined-investment-research-mattel-ip-entertainment-digital-games-valuation-liquidity-workbench-2026-09-18.md)
adds Mattel as a distinct franchise-and-family-entertainment lane. It separates
toy sell-through and gross billings from theatrical releases, licensing,
Mattel163, mobile games, DTC, first-party data, inventory, product claims,
strategic investments, debt, and diluted common residual.

The new [monitored security subscription and smart-home valuation/liquidity workbench](combined-investment-research-adt-monitored-security-subscription-valuation-liquidity-workbench-2026-09-18.md)
adds ADT as a distinct physical-security subscription lane. It separates RMR
and monitoring cash from installation, attrition, customer-acquisition payback,
ADT+, Google Nest/Yale, ambient sensing, service, debt/swaps, and diluted common
residual.

The new [identification, safety, and traceability valuation/liquidity workbench](combined-investment-research-brady-identification-safety-traceability-valuation-liquidity-workbench-2026-09-18.md)
adds Brady as a distinct workplace-control lane. It separates identification,
safety, traceability, printer/software, and consumables economics from product
sell-through, regional divergence, acquisitions, R&D, inventory, compliance,
debt, and diluted common residual.


The new [nuclear-fuel-cycle valuation/liquidity workbench](combined-investment-research-nuclear-fuel-cycle-valuation-liquidity-workbench-2026-09-18.md)
adds Cameco as a distinct uranium-mining, inventory, conversion, and
Westinghouse lane. It separates production from deliveries, contract pricing
from procurement and inventory replacement, Fuel Services from mining, and
equity-method Westinghouse earnings from distributions and required funding.
Production, deliveries, realized price, OCF, inventory gains, and dividends
remain diagnostic until replacement-cost, sustaining-capital, JV-return,
reclamation, and per-share cash joins are evidenced.

The new [merchant-commerce operating-system valuation/liquidity workbench](combined-investment-research-merchant-commerce-operating-system-valuation-liquidity-workbench-2026-09-18.md)
adds Shopify as a distinct merchant-workflow platform, separate from eBay's
goods marketplace, enterprise workflow software, and ordinary consumer credit.
It tests subscription retention, merchant-solutions mix, GMV, Payments
penetration, processing and fraud cost, merchant lending, settlement
obligations, AI/platform investment, SBC, and diluted common residual. GMV,
Payments penetration, revenue, adjusted earnings, OCF, and buybacks remain
diagnostic until merchant survival, payment contribution, credit, settlement,
SBC, and per-share cash joins are evidenced.

The new [integrated device ecosystem valuation/liquidity workbench](combined-investment-research-integrated-device-ecosystem-valuation-liquidity-workbench-2026-09-18.md)
adds Apple as a distinct premium-device and Services ecosystem lane, separate
from merchant commerce, enterprise workflow software, transaction marketplaces,
and electronic interconnect content. It tests device replacement, installed-
base retention, Services attachment and take rate, platform costs, R&D,
silicon, supply chain, tariffs, China, regulation, SBC, and diluted common
residual. Installed base, Services growth/margin, revenue, adjusted earnings,
OCF, and buybacks remain diagnostic until replacement, normalized take-rate,
reinvestment, regulatory, and per-share cash joins are evidenced.

The new [mobility and delivery marketplace valuation/liquidity workbench](combined-investment-research-mobility-delivery-marketplace-valuation-liquidity-workbench-2026-09-18.md)
adds Uber as a distinct ride/order coordination and membership platform,
separate from travel booking, lodging, e-commerce marketplaces, and merchant-
commerce software. It tests gross bookings versus retained revenue,
driver/courier and merchant settlements, incentives, insurance, payments,
refunds, membership, legal obligations, autonomous-vehicle partners, SBC, and
diluted common residual. Gross bookings, trips, MAPCs, adjusted EBITDA, FCF,
and membership remain diagnostic until retained contribution, supply/insurance,
legal, AV-return, and per-share cash joins are evidenced.

The new [qualified grid components valuation/liquidity workbench](combined-investment-research-qualified-grid-components-valuation-liquidity-workbench-2026-09-18.md)
adds Hubbell as a distinct qualified electrical-infrastructure components lane,
separate from regulated utilities, power generation, Amphenol interconnects,
and industrial distribution. It tests Utility Solutions, Electrical Solutions,
grid infrastructure, automation, meters, firm backlog, price versus unit
volume, channel inventory, acquisitions, pension, debt, and diluted common
residual. Sales, backlog, adjusted EPS, OCF, and buybacks remain diagnostic
until shipment, collection, volume, acquisition-return, and per-share cash
joins are evidenced.

The new [accelerated-computing platform valuation/liquidity workbench](combined-investment-research-accelerated-computing-platform-valuation-liquidity-workbench-2026-09-18.md)
adds NVIDIA as a distinct architecture, software, systems, and AI-infrastructure
lane, separate from memory, foundry, lithography, process control, networking,
and builder cloud. It tests customer concentration, extended receivables,
inventory and supplier commitments, export-driven product charges, AI-cloud
guarantees, investment gains, SBC, debt, and diluted common residual. Data
Center revenue, gross margin, OCF, demand, and repurchases remain diagnostic
until sell-through, collection, partner utilization, required reinvestment, and
per-share cash joins are evidenced.

The new [agricultural inputs, retail, and potash valuation/liquidity workbench](combined-investment-research-agricultural-inputs-retail-potash-valuation-liquidity-workbench-2026-09-18.md)
adds Nutrien as a distinct integrated crop-input and farmer-retail lane,
separate from crop-protection chemistry, diversified mining, and agribusiness
processing. It tests Potash, Nitrogen, Phosphate, Retail, price/volume/unit
cost, supplier financing, inventory, receivables, mine/plant renewal,
environmental obligations, portfolio exits, debt, and diluted common residual.
FCF, EBITDA, production, retail growth, and dividends remain diagnostic until
mid-cycle supplier, capital, and per-share cash joins are evidenced.

The new [phosphate, potash, and Brazil-execution valuation/liquidity workbench](combined-investment-research-phosphate-potash-brazil-execution-valuation-liquidity-workbench-2026-09-18.md)
adds The Mosaic Company as a separate fertilizer-conversion and Brazil-distribution
lane rather than pooling it with Nutrien. It tests sulfur/ammonia exposure,
plant utilization, inventory funding, curtailment, OCF-less-capex, environmental
obligations, debt, and diluted common residual.

The new [institutional custody and asset-servicing valuation/liquidity workbench](combined-investment-research-institutional-custody-asset-servicing-valuation-liquidity-workbench-2026-09-18.md)
adds State Street as a distinct custody, administration, securities-processing,
and institutional-bank lane, separate from S&P benchmarks/data, CME clearing,
and alternative asset managers. It tests AUC/A versus AUM, fee rates, client
flows, transaction activity, technology/control investment, collateral,
liquidity, NII/FX/securities finance, regulatory capital, and diluted common
residual. AUC/A, AUM, fee revenue, EPS, OCF, and buybacks remain diagnostic
until fee, control, capital, and per-share cash joins are evidenced.

The new [climate-control HVAC and service valuation/liquidity workbench](combined-investment-research-climate-control-hvac-service-valuation-liquidity-workbench-2026-09-18.md)
adds Trane Technologies as a distinct cooling, controls, retrofit, and
installed-service lane, separate from HVAC distribution, electrical interfaces,
and industrial automation. It tests equipment versus service attachment,
backlog conversion, technician capacity, warranty, inventory, data-center
orders, refrigerant transition, acquisitions, capex, and diluted common
residual. Bookings, backlog, adjusted earnings, OCF, and FCF conversion remain
diagnostic until service, acceptance, collection, and per-share cash joins are
evidenced.

The new [coffeehouse routine-demand valuation/liquidity workbench](combined-investment-research-coffeehouse-routine-demand-valuation-liquidity-workbench-2026-09-18.md)
adds Starbucks as a distinct company-operated coffeehouse and loyalty lane,
separate from restaurant franchises and branded beverage manufacturers. It
tests transactions versus ticket, store labor/service, company-operated versus
licensed economics, Rewards and stored value, coffee/food/tariff cost, closures,
remodels, technology, debt, and diluted common residual. Comparable sales,
adjusted earnings, OCF, dividends, and buybacks remain diagnostic until
mature-store, service, and per-share cash joins are evidenced.

The new [diversified mining and metals valuation/liquidity workbench](combined-investment-research-diversified-mining-metals-valuation-liquidity-workbench-2026-09-18.md)
adds Rio Tinto as a distinct mine-and-logistics portfolio lane, separating
Pilbara iron ore, aluminium, copper, lithium, project ramp, partner funding,
rehabilitation, debt, and dividends from uranium mining, precious-metals
streaming, chemicals, and equipment suppliers. Production, EBITDA, FCF, first
ore, critical-minerals growth, and dividends remain diagnostic until mid-cycle
replacement-capital, project-return, and per-share cash joins are evidenced.

The new [chlorovinyl and chlor-alkali chemicals valuation/liquidity workbench](combined-investment-research-chlorovinyl-chloralkali-chemicals-valuation-liquidity-workbench-2026-09-18.md)
adds Westlake as a distinct integrated chemical-cycle lane, separating HIP
downstream pipe/fittings/siding from PEM chlorovinyl, polyethylene, epoxy, and
chlor-alkali economics. It tests price/spread, utilization, feedstock, energy,
plant closures, environmental and litigation claims, inventory, ACI returns,
debt, sustaining capex, and diluted common residual. EBITDA, spreads, OCF,
improvement plans, and dividends remain diagnostic until mid-cycle plant,
closure, and per-share cash joins are evidenced.

The new [industrial automation installed-base valuation/liquidity workbench](combined-investment-research-industrial-automation-installed-base-valuation-liquidity-workbench-2026-09-18.md)
adds Honeywell as a distinct post-separation controls, process-technology, and
service/software lane, separate from contractors, grid components, electronic
interconnects, and mission-system integrators. It tests backlog conversion,
installed-base attachment, acquisitions, one-time indemnity and asbestos cash,
capex/R&D, pension, debt, stranded cost, and diluted common residual. Backlog,
adjusted EPS, OCF, and buybacks remain diagnostic until post-spin service,
collection, obligation, and per-share cash joins are evidenced.

The new [energy-beverage brand and distribution valuation/liquidity workbench](combined-investment-research-energy-beverage-brand-distribution-valuation-liquidity-workbench-2026-09-18.md)
adds Monster Beverage as a distinct repeat-consumption and bottler-dependent
brand lane, separate from diversified branded staples. It tests cases versus
sell-through, net revenue per case, promotional allowances, Coca-Cola/bottler
settlement, international mix, ingredients and packaging, alcohol losses, SBC,
and diluted common residual. Cases, sales, adjusted earnings, OCF, and buybacks
remain diagnostic until continuing brand, working-capital, and per-share cash
joins are evidenced.

The new [senior-housing healthcare REIT valuation/liquidity workbench](combined-investment-research-senior-housing-healthcare-reit-valuation-liquidity-workbench-2026-09-18.md)
adds Welltower as a distinct senior-housing and healthcare-property lane,
separate from lodging, agency mortgage REITs, data-center real estate, and
direct healthcare operators. It tests occupancy, resident affordability,
operator coverage, same-store NOI, recurring property capital, acquisition and
development yields, debt, cap rates, preferred claims, NAV, and diluted common
residual. Normalized FFO, NOI, occupancy, investment activity, and dividends
remain diagnostic until operator, recurring-capital, and per-share cash joins
are evidenced.

The new [Ventas healthcare-property operating-platform valuation/liquidity workbench](combined-investment-research-ventas-healthcare-property-capital-valuation-liquidity-workbench-2026-09-18.md)
adds Ventas as a distinct SHOP/OM&R/NNN property-owner lane, separate from
Welltower. It tests property-level cash NOI, operator coverage, recurring capital,
acquisition and development return, equity-forward funding, debt, and diluted
common residual.

The new [logistics real estate, embedded-rent, and strategic-capital valuation/liquidity workbench](combined-investment-research-prologis-logistics-property-capital-valuation-liquidity-workbench-2026-09-18.md)
adds Prologis as a distinct industrial/logistics REIT lane. It tests occupancy,
lease rollover, embedded rent growth, tenant collection, recurring property
capital, development, strategic-capital partnerships, data-center power pipeline,
debt, cap rates, and diluted common residual.

The new [spin-off engineering and mission-technology valuation/liquidity workbench](combined-investment-research-spin-off-engineering-mission-technology-valuation-liquidity-workbench-2026-09-18.md)
adds KBR as a distinct two-engine separation lane, keeping Mission Technology
Solutions, Sustainable Technology Solutions, contract type, affiliate cash,
backlog conversion, pension, debt, and standalone spin-off cost separate from
defense mission systems and specialty construction. Backlog, options, adjusted
earnings, OCF, and buybacks remain diagnostic until funded conversion,
post-spin cash ownership, debt, and per-share residual joins are evidenced.

The new [milestone jewelry retail valuation/liquidity workbench](combined-investment-research-milestone-jewelry-retail-valuation-liquidity-workbench-2026-09-18.md)
adds Signet Jewelers as a distinct occasion-driven retail lane, separate from
household-value, branded staples, home furnishings, and general consumer
goods. It tests transactions versus AUR, Bridal and Fashion mix, inventory
turns, markdowns, gold and diamond costs, tariffs, stores, digital conversion,
James Allen transition, SBC, and diluted common residual. Same-store sales,
AUR, adjusted earnings, FCF, and buybacks remain diagnostic until unit,
inventory, maintenance, and per-share cash joins are evidenced.

The new [home-furnishings marketplace and logistics valuation/liquidity workbench](combined-investment-research-home-furnishings-marketplace-logistics-valuation-liquidity-workbench-2026-09-18.md)
adds Wayfair as a distinct bulky-goods marketplace and delivery-network lane,
separate from eBay's transaction marketplace, Shopify's merchant platform, and
branded home retail. It tests active customers, orders, retained contribution,
supplier health, advertising, fulfillment, returns, CastleGate, delivery
capacity, leases, SBC, and diluted common residual. Customers, gross profit,
adjusted EBITDA, OCF, and buybacks remain diagnostic until order-level
contribution, logistics, collection, and per-share cash joins are evidenced.

The new [institutional consulting and managed-services valuation/liquidity workbench](combined-investment-research-institutional-consulting-managed-services-valuation-liquidity-workbench-2026-09-18.md)
adds Huron Consulting Group as a distinct professional-labor and institutional
workflow lane, separate from enterprise software, talent advisory, and public-
safety workflow. It tests RBR, organic growth, utilization, managed-services
renewal, client collection, unbilled services, capitalized software,
acquisitions, SBC, repurchases, and diluted common residual. RBR, adjusted
EBITDA, OCF, and buybacks remain diagnostic until labor, collection,
acquisition-return, and per-share cash joins are evidenced.

The new [industrial-electrical protection and cooling valuation/liquidity workbench](combined-investment-research-industrial-electrical-protection-cooling-valuation-liquidity-workbench-2026-09-18.md)
adds nVent Electric as a distinct qualified-interface and thermal-management
lane, separate from grid components, electrical distribution, data-center
construction, and electronic interconnects. It tests organic versus acquired
growth, EPG integration, backlog conversion, liquid-cooling capacity and
warranty, tariffs, debt, divestiture proceeds, and diluted common residual.
Sales, backlog, adjusted EPS, reported FCF, and buybacks remain diagnostic
until acquired-return, shipment, collection, capacity, and per-share cash
joins are evidenced.

The new [commercial landscape services valuation/liquidity workbench](combined-investment-research-commercial-landscape-services-valuation-liquidity-workbench-2026-09-18.md)
adds BrightView as a distinct maintenance-contract and outdoor-site-services
lane, separate from ABM facility services, pest-control routes, environmental
services, and specialty construction. It tests Maintenance versus Development,
H-2B labor, route density, fleet renewal, weather, working capital, receivables
financing, debt, leases, preferred claims, and diluted common residual. Revenue,
adjusted EBITDA, adjusted FCF, OCF, equipment-sale proceeds, and buybacks remain
diagnostic until renewal, staffing, fleet, collection, leverage, preferred,
and per-share cash joins are evidenced.

The new [specialty-glass and optical-connectivity valuation/liquidity workbench](combined-investment-research-specialty-glass-optical-connectivity-valuation-liquidity-workbench-2026-09-18.md)
adds Corning as a distinct physical-materials and manufacturing-capacity lane,
separate from active networking equipment, electronic interconnects, and
semiconductor fabrication. It tests Optical Communications growth, utilization,
yield, price/mix, customer deposits, government incentives, inventory,
receivables, 2026 capex, pensions, environmental claims, SBC, and diluted
common residual. Optical growth, agreements, adjusted FCF, OCF, and buybacks
remain diagnostic until capacity-return, collection, claim, and per-share cash
joins are evidenced.
adjusted earnings, OCF, and buybacks remain diagnostic until unit, collection,
maintenance, hospitality, and per-share cash joins are evidenced.
The new [hydro-sensitive regulated utility valuation/liquidity workbench](combined-investment-research-avista-hydro-sensitive-regulated-utility-valuation-liquidity-workbench-2026-09-18.md)
adds Avista as a distinct smaller-system utility lane. It separates hydro and weather,
rate-base recovery, mixed electric-and-gas customer cohorts, large-customer procurement,
wildfire and reliability obligations, capex funding, debt, and diluted common residual
from utility EPS and guidance. Avista remains qualified, unranked, and owner-cash-open.

The new [live events, ticketing, and sponsorship valuation/liquidity workbench](combined-investment-research-live-nation-live-events-ticketing-valuation-liquidity-workbench-2026-09-18.md)
adds Live Nation as a distinct experience-economy lane. It separates Concerts,
Ticketing, and Sponsorship & Advertising, then tests attendance, event settlement,
artist economics, deferred revenue, venue investment, legal accruals, debt, and
dilution. Live Nation remains qualified, unranked, and owner-cash-open.

The new [defense mission systems and federal technology valuation/liquidity workbench](combined-investment-research-caci-defense-mission-systems-valuation-liquidity-workbench-2026-09-18.md)
adds CACI as a distinct national-security technology lane. It separates mission
software, electronic warfare, sensing, federal contracts, funded backlog, ARKA
integration, cleared labor, working capital, debt, and dilution from awards,
backlog, EBITDA, adjusted EPS, and FCF. CACI remains qualified, unranked, and
owner-cash-open.

The new [licensed collectibles and multiplatform play valuation/liquidity workbench](combined-investment-research-toys-fandom-play-valuation-liquidity-workbench-2026-09-18.md)
adds Funko and Spin Master as a distinct play-and-fandom lane. It separates
licensed property access, royalties, tariffs, inventory, retailer timing, toy
sell-through, entertainment delivery, digital engagement, debt, and dilution.
Tariff refunds, adjusted EBITDA, property counts, and digital users remain
diagnostic rather than normalized owner cash. The lane remains qualified,
unranked, and owner-cash-open.
The workbench now has a current primary-source bridge: Funko's `$25.4M`
tariff/accrual benefit and `$19.2M` cash proceeds from selling `$22.1M` of
tariff claims are separated from its `$201.1M` debt and `$40.7M` cash, while
Spin Master's `$57.8M` Q2 operating cash flow, `$19.2M` free cash flow, and
`$37.9M` toy tariff refund are kept separate from its portfolio reinvestment
and common-owner claims. The lane is current-period qualified, not ranked.
The Funko bridge is now extended through H1 cash and liquidity: `$23.630M` of
operating cash included `$9.0M` of interest, `$18.954M` of investing cash was
used primarily for tooling and molds, and there was no remaining revolver
availability against `$198.3M` of Credit Agreement debt and `$40.7M` of cash.
The Q2 filing also reports `$34.1M` of royalty-audit accruals and a `$3.2M`
unrecoverable-prepaid-royalty reserve. These facts sharpen the burden stack but
do not promote operating cash, tariff proceeds, or cash-on-hand to normalized
owner cash; the lane remains qualified, unranked, and owner-cash-open.
The current balance sheet also shows `$88.800M` of inventory against an
`$11.9M` excess-and-obsolete reserve, `$93.561M` of net receivables, and
`$54.712M` of accrued royalties. The filing's Q2 covenant thresholds—minimum
Qualified Cash of `$10.0M`, staged Fixed Charge Coverage Ratio tests, a `2.50x`
maximum Net Leverage Ratio beginning in Q4 2026, and a `$15.1M` six-month
Consolidated EBITDA test—turn the next filing into a falsifiable liquidity
test. The Q2 filing does not refresh the year-by-year minimum-guarantee dollar
schedule, so the FY2025 `$128.2M` schedule remains dated evidence rather than a
current forecast.
The parallel Spin Master pass now adds a filed cash-quality bridge: H1
operating cash was `$160.7M`, including `$108.6M` of non-cash working-capital
change; investing used `$71.0M`, debt repayment was `$167.0M`, and cash fell to
`$48.5M`. The Q2 `$37.9M` toy tariff refund is explicitly non-recurring, while
current inventory was `$187.3M`, trade receivables were `$340.7M`, and total
lease liabilities were `$193.4M`. The company had `$627.3M` of reported
liquidity, but committed facilities remain financing capacity rather than
owner cash. Spin Master therefore remains qualified and unranked alongside
Funko.
The September 18 market-expectation refresh places Funko at approximately
`$300.9M` of equity value and Spin Master at approximately `CAD 2.0B`. Funko's
H1 operating cash less tooling/molds annualizes to about `$9.352M`, while Spin
Master's H1 operating cash less PP&E and intangible investment annualizes to
about `$179.4M`; the resulting mechanical screens are approximately `32.2x`
and `11.2x`, respectively, before currency conversion. These are not normalized
owner-cash multiples: Funko remains supported by tariff/accrual and working-
capital effects, and Spin Master by working-capital release and a toy tariff
refund. The spread changes the expectation burden, not the promotion status or
ranking.

## 2026-09-18 capital-flow continuation refresh

The private-credit borrower lane now has three additional dated controls. Jiffy
Lube's `$1.3B` Monomoy transaction is confirmed completed, but Ares' joint
lead-arranger role still does not disclose funded debt, lender allocation,
borrower receipt, or bank payoff. Precinmac's Q2 Blue Owl schedule shows four
Paris US Holdco / Precinmac first-lien rows with a common December 2031
maturity, totaling `$324.270M` reported par and `$223.821M` fair value; the
rows remain holder-breadth evidence because par-to-cost differences, overlap,
and borrower cash are unresolved. Valcourt's May continuation vehicle adds
sponsor-liquidity and ownership context, not debt-refinancing or bank-
replacement proof.

The CION/CADCX Sunvair channel was extended beyond the preserved SEC N-PORT-EX
schedule with the official June 30, 2026 semi-annual report. CION now has a
vehicle-level capital stack: `$7.280B` total assets, `$1.411B` debt, `$980M`
MRPS carrying value, `$4.728B` net assets, and three named credit facilities.
That upgrades the vehicle channel, but no CION liability or capital layer is
allocated to Sunvair, so source-to-borrower allocation and bank replacement
remain unproven.

The New Mountain/MAI channel has also moved up one evidence grade. New
Mountain Private Credit Fund's March 31, 2026 10-Q shows `$2.084B` total
assets, `$961M` net assets, `$1.044B` net borrowings, two secured facilities,
two unsecured notes, and `191%` asset coverage. That proves a vehicle-level
capital stack around the MAI holder row, not New Mountain corporate funding or
allocation of a particular liability to MAI.

New Mountain Guardian IV's June 30, 2026 10-Q also refreshes the older MAI
route: two current MAI first-lien rows total `$24.858M` fair value, while the
vehicle reports `$2.152B` assets, `$1.182B` members' capital, `$925.7M` net
borrowings, Wells and UBS facilities, and `226.6%` asset coverage. This is
current holder-plus-vehicle evidence, not allocation of a Guardian liability
to MAI or bank-replacement proof.

MAI's ownership context also changed: Carlyle announced that its funds
completed a majority-stake acquisition effective June 4, 2026, at a valuation
above `$2.8B`, with employees retaining a large minority and management and
operational independence continuing. That is an ownership event, not debt
source-of-funds proof. Combining ARCC and Guardian IV produces a Q2 2026
same-period holder-visible lower bound of `$32.858M`; combining those Q2 rows
with ASIF and New Mountain Q1 rows produces `$60.0813M` of mixed-period funded
fair value plus a separate `$12.401M` undrawn commitment. Neither figure is
full MAI facility size or a Carlyle-funded debt balance.

These controls strengthen the distinction between `transaction completed`,
`arranger role`, `holder visibility`, and `borrower cash waterfall`. They do
not change the broad bank-role conclusion: private credit can replace named
bank facilities in specific proven cases, but the broader borrower lane still
mostly shows destination and holder evidence rather than bank displacement.
