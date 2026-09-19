# Crash-recovery handoff — 2026-09-18

## Packet Inputs Used

- the current combined-investment-research synthesis, completion audit, and
  next-execution handoff;
- the Q-03 Wheaton–Antamina metal-credit boundary and the CA-06 retail
  allocation boundary;
- the PBF September conditional-redemption boundary and its verification
  scripts; and
- the current Git status, pilot verifiers, completion verifier, and
  insight-system maintenance contract.

## Purpose

This is the recovery point for the combined investment-research system after
the interrupted session. It records the current state without treating
qualified evidence as proven cash or return evidence.

## Repository state

- Repository: `annual-report-research`
- Branch: `main`
- Last committed checkpoint: `8e5dec6c` on 2026-09-11, “Checkpoint
  cross-framework analysis and site artifacts”
- Current worktree: `146` modified tracked files and `1,534` untracked files
- Do not reset, clean, or selectively discard the worktree. The recent
  research corpus, raw-source captures, scripts, and reader artifacts are
  intentionally still uncommitted.

## System state

The end-to-end architecture is operational across the chain:

`force -> control point -> company -> filing -> QoE -> owner cash -> valuation
-> liquidity -> legal entity / capital flow -> receipt or repayment -> thesis
breaker`

The authoritative completion audit currently reports `12 of 13` requirement
rows proven. `CA-06`—the correct normalized owner-cash denominator—remains
partial. The system supports qualified, source-routed lanes and does not
support a pooled cross-sector investment ranking.

## Verified controls

The following checks passed during recovery:

- Combined completion audit: `13` requirements, `Q-01` through `Q-13`, and
  `98` audited deliverables.
- Combined pilot verification: `3` pilot ledgers and `226` evidence gates,
  including expansion-lane and industrial-uptime checks.
- PBF September conditional-redemption verifier.
- PBF redemption-settlement bridge verifier.

## Post-recovery validation refresh

The refreshed retail interim lease/tax CSV now uses the canonical SEC archive
URL for Walmart's Q2 FY2027 Form 10-Q, matching the official-HTML recheck and
avoiding a company-hosted mirror as the provenance key. The pilot verifier was
updated to preserve that canonical route. The following checks pass after the
refresh:

- combined completion audit: 13 requirements, CA-06 boundary, Q-01 through
  Q-13, and 90 deliverables;
- combined pilot verification: 3 ledgers, 226 evidence gates, valuation
  workbenches, expansion lanes, and industrial uptime lane; and
- full insight-system maintenance stack: `insight-system-ok`.

The substantive status is unchanged: CA-06 remains partial, and the official
interim filings still do not provide the matched Target/Walmart lease-and-tax
cash schedules needed for normalized owner-cash promotion.

The retail interim lease/tax boundary was strengthened with an inline-XBRL
recheck: Target and Walmart expose provision/accrual controls but no dedicated
`PaymentsOfIncomeTaxes`, `OperatingLeasePayments`, or equivalent H1 cash fact.
The structured boundary and verifier now preserve this as an HTML-plus-XBRL
searched-negative, without treating it as proof that no payments occurred.
The tag-level rows are preserved in
`analysis/company-first-principles/data/combined-investment-research-pilot-02-retail-interim-inline-xbrl-search-2026-09-18.csv`.
The reader footer now links directly to that ledger, so the evidence is
discoverable from the reader surface as well as from the boundary memo.

The promotion-gate verifier was hardened to require the exact 13-gate identity
set and critical BHP/retail/URI/PBF/private-credit boundary terms. This keeps
the routing ledger from passing merely because rows are present and nonempty.

The Apollo Schedule BA regression gate was tightened as well: in addition to
the Part 2/3 counts, consideration control, continuity statuses, and queue
tiers, it now requires the exact ten prioritized lot identifiers and verifies
that each remains present in the corrected Part 1, Part 2, and Part 3 parser
outputs. This is a source-row continuity control only; it does not promote
Schedule BA consideration into settlement, borrower repayment, Athene cash, or
Apollo owner cash.

The Schedule DB Part C ↔ Schedule D identity work now has a named-lot control
ledger as well. It groups `52` exact-CUSIP controls across MF1, AMAPS, Atlas,
Varde, and Ares; `51` have unambiguous component candidates and one preserves
source-column ambiguity. The ledger places conservative Part C component sums
beside Schedule D book, fair, interest-income, and interest-received fields.
Component-to-holding differences are retained as perimeter signals, not
settlement or owner-cash evidence. See the [named-lot memo](../analysis/company-first-principles/capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-control-pass-1.md)
and [machine-readable ledger](../analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-control-pass-1.csv).
The follow-on acquisition queue ranks those same routes into `8` Tier A, `30`
Tier B, and `14` Tier C requests, with AMAPS 1 Tranche A, Atlas, MF1 2022-B1
A, Atlas Funding 1, and Varde at the front. It requests only the smallest
decisive custody, trustee/paying-agent, settlement, or lot-level
income-allocation object and does not treat the queue as cash evidence. See
the [acquisition queue](../analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-acquisition-queue-pass-1.csv).

The Apollo/Athene statutory asset bridge was also rerun from the preserved
Athene statement. Part 2 reconciles actual acquisition cost to the source
control within `$1`; Part 3 yields `168` coordinate rows and `$4.417B` of
schedule-positioned consideration; the continuity ledger classifies `61`
three-part, `4` Part 1/3, `17` Part 2/3, `2` unmatched, and `84` blank-CUSIP
events. A new regression gate now checks those counts, the `4` exact and `6`
near lot-review queue, and the `3` BA-to-Schedule-D crosswalk rows. These remain
identifier/lot controls only: no settlement, borrower repayment, Athene cash,
or Apollo owner cash is promoted.

The Part 1 income queue now has a regression gate as well. Its top 30 positive
rows are preserved as a review priority, led by AP Grange Tranche B at
`$31.662M` of coordinate-extracted statutory investment income and one visible
Part 3 event. The queue remains a prioritization device: the income field is
not collected cash, borrower repayment, liability-adjusted spread, or Apollo
owner cash.

## Recent durable updates

- Q-03 now records the official-source refresh for the BHP–Wheaton Antamina
  route. The `$4.3B` upfront payment is confirmed, but BHP-specific metal
  credits, sale/receivable, bank collection, tax, and facility allocation are
  still missing. See
  [the Q-03 boundary](../analysis/company-first-principles/capital-flow-wheaton-antamina-q03-metal-credit-receipt-boundary-2026-09-17.md).
- The current synthesis and next-execution handoff now carry that Q-03
  source-freshness result.
- CA-06 now records the direct SEC supplemental-field refresh. Target’s `$3.2B`
  eligible supplier-finance obligations are not actual early payments, while
  matched H1 lease/tax cash and maintenance/growth allocation remain missing.
  See [the CA-06 boundary](../analysis/company-first-principles/combined-investment-research-retail-ca06-allocation-boundary-2026-09-17.md).
- PBF’s September exchangeable financing is issued, with approximately
  `$533.6M` net proceeds, but the `$500M` 2030-note redemption remains a
  future September 24 settlement event. See
  [the PBF boundary](../analysis/company-first-principles/capital-flow-pbf-september-2026-conditional-redemption-liquidity-boundary-2026-09-17.md).
- Jiffy Lube’s `$1.3B` Monomoy transaction is now confirmed completed by
  Shell, while Ares’ joint-lead-arranger role remains separate from funded
  debt, lender allocation, borrower receipt, and bank-payoff proof. See
  [the Jiffy transaction gap](../analysis/company-first-principles/capital-flow-jiffy-transaction-gap-pass.md).
- Precinmac’s current Q2 2026 Blue Owl schedule now shows four Paris US
  Holdco/Precinmac first-lien rows with a common December 2031 maturity,
  totaling `$324.270M` reported par and `$223.821M` fair value. This is
  current holder breadth, not a promoted funded-facility total or bank-
  replacement proof. See [the Precinmac crosswalk](../analysis/company-first-principles/capital-flow-precinmac-sec-holder-crosswalk.md).
- Valcourt’s May 2026 continuation vehicle is now recorded as sponsor
  liquidity and ownership context; its undisclosed terms do not prove debt
  refinancing, borrower cash, or bank displacement. See [the Valcourt
  timeline](../analysis/company-first-principles/capital-flow-valcourt-acquisition-use-timeline-pass-1.md).
- The CION/CADCX Sunvair source-of-capital bridge now includes the official
  June 30, 2026 semi-annual report. It proves a vehicle-level stack of
  `$7.280B` total assets, `$1.411B` debt, `$980M` MRPS carrying value,
  `$4.728B` net assets, and State Street/Wells/BNP facilities. The Q1 N-PORT
  source remains holder-only; no CION liability or capital layer is allocated
  to Sunvair, so borrower-specific source allocation and bank replacement stay
  open.
- New Mountain Private Credit Fund's March 31, 2026 10-Q now supplies the MAI
  vehicle stack: `$2.084B` total assets, `$961M` net assets, `$1.044B` net
  borrowings, two secured facilities, two unsecured notes, `191%` asset
  coverage, and `$331.6M` outstanding investment-funding commitments. The MAI
  holder row remains unallocated to a specific New Mountain liability or
  facility, and sponsor/bank-role proof remains open.
- New Mountain Guardian IV's June 30, 2026 10-Q refreshes the older MAI route:
  two current first-lien rows total `$24.858M` fair value, and the vehicle
  reports `$2.152B` assets, `$1.182B` members' capital, `$925.7M` net
  borrowings, Wells/UBS facilities, `226.6%` asset coverage, and `$330.8M`
  outstanding investment-funding commitments. MAI-specific liability
  allocation and bank-role proof remain open.
- Carlyle announced that its funds completed a majority stake in MAI effective
  June 4, 2026, at a valuation above `$2.8B`; this is ownership context only,
  not debt source-of-funds evidence. The refreshed MAI crosswalk now shows a
  Q2 2026 ARCC-plus-Guardian holder-visible lower bound of `$32.858M` and a
  mixed-period funded lower bound of `$60.0813M`, plus a separate `$12.401M`
  New Mountain undrawn commitment. These do not prove full facility size,
  Carlyle debt funding, or bank replacement.
- Apollo–Athene Q-07’s current Apollo Q2 filing reinforces subsidiary-dividend
  and legal-availability controls but still provides no AGM receiving account,
  remittance, or elimination schedule. Q-07 remains `receipt-unproven`.

## Next execution order

1. **Q-03:** stop broad searching; advance only on a new BHP-specific
   settlement, delivery, reserve, lender, or transaction-level cash schedule.
2. **CA-06:** advance only on a matched payment/settlement, maintenance-capital,
   lease/tax, attached-service, supplier-finance, or common-owner claim join.
3. **PBF:** after September 24, check for trustee/issuer settlement, accrued
   interest, capped-call cost, cash allocation, post-close liquidity, and
   exchangeable dilution.
4. **Q-13 / private credit:** use a populated borrowing-base certificate,
   lender allocation, custody/trustee remittance, or closing funds-flow record;
   do not promote capacity, statutory interest, fair value, or arranger role.

The Q-13 request is now machine-readable in the [next-source package](../analysis/company-first-principles/data/capital-flow-uri-q13-next-source-package-2026-09-18.csv): certificate, NOLV, reserve, fleet source-to-purchase, and receivables-purchaser availability objects are ranked with minimum fields and promotion joins.

## Non-negotiable evidence boundaries

- Do not assign combined Antamina production or cash to the BHP PMPA.
- Do not subtract supplier-finance balances or annual lease/tax values again
  from matched-period OCF without settlement evidence.
- Do not treat Target’s undrawn `$4.0B` facility or PBF’s financing proceeds as
  operating or common-owner cash without a draw/use/repayment bridge.
- Do not promote reported OCF, FCF, EBITDA, AUM, backlog, production, or
  statutory income into normalized owner cash without same-entity,
  same-period claim and allocation joins.

## Recovery verification checkpoint — 2026-09-18

After the crash-recovery pass, the current worktree was rechecked against the
authoritative controls:

- The capital-flow graph verifies `19` flows, including the AMAPS and AP
  Grange named routes.
- The AP Grange graph gate now preserves the issuer/gain/concentration metrics,
  the named Tranche A/B book values, the `313313 USD` Tranche B statutory
  event, and the explicit missing settlement/allocation fields.
- Q-03 now carries an exact BHP FY2026 cash-flow row: `$4.300B` streaming-
  arrangement proceeds, `$41M` of liability settlements, and `$(3.280B)` net
  financing cash flows. The row is explicitly barred from proving bank timing,
  internal use of proceeds, or recurring BHP-PMPA collections.
- A targeted URI Q2 2026 10-Q recheck preserves the consolidated source/use
  surface—`$3.305B` OCF, `$2.720B` rental-equipment purchases, `$400M`
  acquisitions, `$91M` net debt payments, and `$2.887B` facility availability—
  but found no ABL-draw-to-purchase allocation or populated borrowing-base,
  NOLV, or reserve certificate. Q-13 remains evidence-insufficient for
  legal availability and lifecycle return.
- The three pilot ledgers verify `226` evidence gates and retain their
  qualified, non-overclaim boundaries.
- The completion audit verifies all `13` requirement rows and still reports
  `12 of 13 proven; CA-06 partial`.
- The internal-link audit verifies `6,765` links with `0` broken links.
- The insight-system verification passes.

No stale `17`- or `18`-flow reference remains in the authoritative synthesis,
handoff, completion-audit, graph, `START-HERE`, or `README` routes checked in
this recovery pass. These are verification results, not a promotion of any
open receipt, settlement, liability-cost, or owner-cash gate.

## Primary orientation files

- [Meaty end-to-end goal](../analysis/company-first-principles/combined-investment-research-meaty-end-to-end-goal.md)
- [Current synthesis](../analysis/company-first-principles/combined-investment-research-current-synthesis.md)
- [Completion audit](../analysis/company-first-principles/combined-investment-research-completion-audit.md)
- [Next-execution handoff](../analysis/company-first-principles/combined-investment-research-next-execution-handoff-2026-09-17.md)

## Maintenance commands

Run the repository maintenance and provenance checks with:

```bash
bash scripts/run-insight-audit-stack.sh
bash scripts/refresh-note-layer-boundary.sh
bash scripts/audit-audit-stack-terminology.sh
bash scripts/audit-maintenance-doc-stack.sh
bash scripts/audit-continuation-mode-links.sh
bash scripts/audit-remaining-brief-links.sh
bash scripts/audit-remaining-stack-links.sh
bash scripts/audit-browser-review-links.sh
bash scripts/verify-insight-system.sh
```

## Skeptical Reader Test

- Can a reader identify the last committed checkpoint separately from the
  uncommitted recovery corpus?
- Can a reader distinguish proven requirements from qualified lanes and the
  unresolved CA-06 denominator?
- Can a reader find the exact source object required to promote Q-03, CA-06,
  PBF, Q-13, or private-credit evidence?
- Does the handoff avoid treating undrawn capacity, reported OCF, combined
  production, supplier-finance balances, or statutory income as common-owner
  cash?
- Can the next researcher rerun the verification commands and locate every
  linked orientation artifact without relying on session memory?
