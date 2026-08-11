# Thin-Lane Window And Source-Authority Audit

Date baseline: `2026-08-11`
Repo: `annual-report-research`

## Purpose

This note tests one of the exact remaining-work items from the original-goal audit:

- whether thin-lane anchor packets really prove the `2025` annual plus latest-three-reported-quarters standard as of `2026-08-10`
- whether they clearly show AnnualReports as taxonomy only and company IR plus SEC as the authoritative source chain when AnnualReports lags

This is not a repo-wide audit.

It is a targeted audit of thin-lane anchors that matter disproportionately to honest closeout quality.

## Anchors reviewed

- `UnitedHealth Group`
- `HCA Healthcare`
- `Sysco`
- `MetLife`
- `Zebra Technologies`
- `Hewlett Packard Enterprise`
- `Epson`

## Status key

- `proven`: the current packet and ledger explicitly prove both the filing window and the authority rule
- `qualified`: the packet is still usable and mostly authoritative, but the proof relies on fallback methods, partial local capture, or weaker explicitness
- `needs repair`: the current packet contains an internal contradiction, unresolved path problem, or evidence gap large enough that the proof chain is not clean

## Audit results

| Company | Filing-window proof | Source-authority proof | Status | Exact reason |
|---|---|---|---|---|
| `UnitedHealth Group` | explicit `Q2 2026`, `Q1 2026`, `Q4 2025` target window in packet and ledger | explicit note that AnnualReports lagged at `2024` and that IR plus SEC are authoritative | `qualified` | Strong chain, but the ledger also states that no `Q2 2026` `10-Q` was collected locally, so the most recent quarter is proven at release plus `8-K` level rather than filed-quarterly level |
| `HCA Healthcare` | explicit `Q2 2026`, `Q1 2026`, `Q4 2025` target window in packet and ledger | explicit AnnualReports verification plus official IR and SEC chain | `proven` | Cleanest case in this sample: annual report, quarter releases, `8-K` wrappers, and both in-scope `10-Q` filings are all stated clearly |
| `Sysco` | packet and ledger state `Q4 FY26`, `Q3 FY26`, `Q2 FY26` and now consistently describe the current-quarter evidence as release-level rather than filed-wrapper-complete | ledger explicitly says AnnualReports lagged at `2024` and that IR plus SEC are authoritative | `qualified` | The contradiction was repaired by aligning the packet with the ledger, but the most recent quarter still lacks a locally inspectable `Q4 FY26` `8-K` wrapper or year-end filed report in the current raw tree |
| `MetLife` | explicit `2Q26`, `1Q26`, `4Q25` target window in packet and ledger | explicit note that IR binaries were blocked by Cloudflare and that SEC filings plus verified IR URLs are the authoritative local chain | `qualified` | The chain is still authoritative, but direct local IR artifact capture is missing, so proof depends more heavily on SEC plus verified official URLs |
| `Zebra Technologies` | explicit `Q2 2026`, `Q1 2026`, `Q4 2025` target window in packet and ledger | explicit note that AnnualReports lagged and official IR retrieval hit `429`, so SEC-hosted annual and quarterly artifacts carry the proof | `qualified` | Good evidence chain, but official IR pages were not saved locally and the packet depends on SEC-hosted artifacts plus IR verification notes |
| `Hewlett Packard Enterprise` | packet and profile explicitly define fiscal `2025` annual plus `Q2 FY2026`, `Q1 FY2026`, and `Q4 FY2025` | the source ledger now explicitly states that the inherited raw chain is not currently inspectable from this workspace | `qualified` | The misleading clean-chain implication was repaired, but the company still lacks a rebuilt local raw path set that would make it a proof-standard case |
| `Epson` | explicit `Three Months ended June 30, 2026`, `Fiscal Year ended March 31, 2026`, and `Nine Months ended December 31, 2025` target window in packet and ledger | explicit note that AnnualReports lagged and direct retrieval returned `403`, so browser-captured official extracts were used | `qualified` | The company is still well covered, but proof depends on browser-captured official extracts rather than locally downloaded binaries or SEC-hosted equivalents |

## Exact observations

### 1. `UnitedHealth Group` is better than the old handoff implied, but still not a perfect filed-quarter chain.

What is clearly proven:

- the packet states the correct target window: `Q2 2026`, `Q1 2026`, `Q4 2025`
- the ledger explicitly says AnnualReports lagged at `2024`
- the ledger explicitly says the authoritative `2025` chain comes from IR and SEC

What remains weaker:

- the ledger says no `Q2 2026` `10-Q` was collected locally as of `2026-08-08`

Conclusion:

- the packet is real and usable
- the cleanest phrasing is not "fully filed-quarter complete"
- the cleanest phrasing is "current quarter proven through official release, `8-K`, and prepared remarks, but not local `10-Q` capture"

### 2. `HCA Healthcare` is the best proof-standard model in this thin-lane sample.

What is clearly proven:

- annual report PDF is saved locally
- `2025` `10-K` is saved locally
- `Q4 2025`, `Q1 2026`, and `Q2 2026` releases are named explicitly
- both in-scope `10-Q` filings are named explicitly
- the ledger explicitly states that the annual-plus-quarter chain is clean on disk

Conclusion:

- HCA should be treated as the standard for what "proven" looks like in later cleanup work

### 3. `Sysco` no longer has a contradiction, but it is still not a fully filed current-quarter case.

What is clearly proven:

- the intended fiscal window is correct: `Q4 FY26`, `Q3 FY26`, `Q2 FY26`
- AnnualReports lag was recorded explicitly
- the packet correctly frames Sysco as the enabling infrastructure layer under hospitality and participation demand

What remains weaker:

- the packet and ledger now align on the same claim: the `Q4 FY26` release PDF is local, but the matching `8-K` wrapper and year-end filed report were not present in the reviewed raw tree
- the raw SEC directory reviewed in this audit only showed:
  - `2025-q4-*`
  - `2026-q1-*`
  - `2026-q2-*`
  - `2026-q3-*`
- no `2026-q4-*` file appeared in the reviewed local raw SEC directory

Conclusion:

- Sysco is now documentation-clean but still only qualified
- it still needs the missing current-quarter filed artifacts if the repo wants to upgrade it from qualified to proven

### 4. `MetLife` is authoritative enough, but only through a fallback route.

What is clearly proven:

- target window is explicit: `2Q26`, `1Q26`, `4Q25`
- AnnualReports lag at `2024` is explicit
- the ledger and IR-link note explicitly explain the Cloudflare block
- the SEC chain for annual and trailing quarters is locally present

What is weaker:

- no clean local IR PDFs were preserved in this workspace

Conclusion:

- MetLife should count as authoritative but qualified
- the main weakness is capture method, not misunderstanding of the period chain

### 5. `Zebra Technologies` is also authoritative through fallback evidence.

What is clearly proven:

- target window is explicit: `Q2 2026`, `Q1 2026`, `Q4 2025`
- AnnualReports lag at `2024` is explicit
- the ledger says official IR retrieval hit `429`
- SEC-hosted annual and quarter artifacts are explicitly named

What is weaker:

- no locally saved official IR pages
- no standalone earnings-release exhibit or transcript artifact

Conclusion:

- Zebra is a good packet
- it is just not the gold-standard "official IR plus SEC plus local binary" version

### 6. `Hewlett Packard Enterprise` is now honestly described, but still not locally proven.

What is clearly stated:

- the packet and profile define the correct annual anchor and the latest three reported quarters
- the packet itself now states `qualified` proof status explicitly
- the packet now states that AnnualReports is taxonomy context only and that company IR plus SEC are the intended authority chain
- the profile says official IR routing links and SEC chains were saved

What remains weaker:

- the source-ledger now explicitly says the inherited raw chain is not currently inspectable from this workspace
- the packet still lacks a rebuilt local raw path set comparable to the cleaner chains for HCA, MetLife, or Zebra

Conclusion:

- HPE is analytically useful and no longer misleadingly documented
- the packet-level proof-language is now stronger and more self-contained than before
- it should still be treated as qualified until the raw evidence chain is rebuilt locally

### 7. `Epson` is a valid non-U.S. qualified case, not a broken case.

What is clearly proven:

- the packet and ledger define the correct non-U.S. reporting window
- AnnualReports lag is explicit
- the ledger explains why browser-captured official extracts were used instead of direct binary capture

What is weaker:

- proof depends on browser-captured official extracts
- there is no SEC fallback because this is not the core filing path for this issuer

Conclusion:

- Epson is acceptable as a qualified case
- its weaker point is collection method, not the underlying period logic

## What This Audit Changes

This audit improves the original-goal closeout picture in a more exact way:

- it shows that some supposedly "thin" anchors are actually well-proven
- it shows that the problem is not uniformly missing research
- it isolates the exact cases where closure quality still needs repair

In this sample after the packet and ledger repairs:

- `proven`: `1`
- `qualified but usable`: `6`
- `needs repair`: `0`

## What This Means After The Recent Lane-Closure Passes

Since this audit was first written, the repo has narrowed several lane-closure gaps through:

- the CLI 5 control-layer expansion
- the CLI 5 healthcare-information bridge
- the CLI 4 payer / provider adjacent burden bridge
- the CLI 6 balance-sheet and property clarification pass
- the recreation owner and repeat-relationship bridge

That changes the practical meaning of the thin-lane audit.

The main remaining closeout problem is no longer:

- "too many lanes are still conceptually thin"

It is increasingly:

- "some important anchor packets are still qualified rather than fully proven"

In other words:

- lane structure is now stronger than proof-standard uniformity
- interpretation has advanced faster than evidence normalization
- the best remaining proof-quality work is a targeted upgrade queue, not a broad discovery queue

## Exact repair queue from this audit

### Highest priority

1. `Sysco`
   - collect or restore the missing `Q4 FY26` filed-wrapper chain if the goal is to upgrade the packet from release-level qualified to fully proven
2. `Hewlett Packard Enterprise`
   - rebuild the raw evidence chain so the current honest ledger can point to inspectable local IR and SEC artifacts again

### Second priority

3. `UnitedHealth Group`
   - clarify in closeout language that the latest quarter is proven through release plus `8-K` plus prepared remarks, not local `10-Q`
4. `MetLife`
   - keep as qualified unless direct IR binaries are later recoverable
5. `Zebra Technologies`
   - keep as qualified unless official IR HTML or binaries are later recoverable
6. `Epson`
   - keep as qualified unless cleaner local official binaries can be saved later

## Best Remaining Audit Sequence

If the goal is honest wrap-up rather than more frontier-opening, the highest-yield proof-quality sequence is now:

1. keep `HCA` as the proof-standard reference case
2. treat `Sysco` and `HPE` as the two most upgrade-worthy qualified names because their gaps are the most concrete
3. keep `MetLife`, `Zebra`, and `Epson` explicitly qualified unless cleaner capture becomes available
4. preserve precise language around `UnitedHealth` rather than overstating filed-quarter completeness

That sequence fits the repo's real state better than opening more company packets first.

## Bottom line

The original-goal audit was right to say that proof quality was uneven.

But "uneven" does not mean "mostly absent."

In this thin-lane sample:

- `HCA` is already fully proven
- `UnitedHealth`, `MetLife`, `Zebra`, `Epson`, `Sysco`, and `HPE` are real and usable, but qualified for different reasons
- the main remaining work is now less about contradictory writeups and more about upgrading the highest-value qualified cases into fully proven ones while keeping the rest honestly labeled

That is the actual thin-lane proof state as of `2026-08-11`.
