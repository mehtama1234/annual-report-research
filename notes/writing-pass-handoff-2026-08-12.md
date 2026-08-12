# Writing Pass Handoff

Date: `2026-08-12`
Repo: `annual-report-research`
Branch: `main`
Prior commit at start of pass: `998a8961`

This closes out the overall writing pass requested in
[overall-writing-pass-handoff-2026-08-12.md](/notes/overall-writing-pass-handoff-2026-08-12.md).

## What this pass did

- This was a writing-only pass. No new research, no new company collection, no raw download sweep, no repo-wide index churn.
- It added three reader-facing synthesis surfaces so a serious outside reader can understand the archive without reading thread history.
- Every claim on the new pages is backed by companies that already appear in the archive. No new figures were introduced; the figures used are copied from existing packets and cross-sector pages.

## Pages materially improved (new)

- [analysis/cross-sector/what-this-archive-proves-2026-08-12.md](/analysis/cross-sector/what-this-archive-proves-2026-08-12.md)
  - Top-level synthesis. States the core finding (interface / workflow / trust / control owners capture cleaner economics than burden carriers) and eight core findings, each in a claim / why / named examples / tension shape. Closes with pointers to four existing proof pages.
- [notes/how-to-read-this-archive-2026-08-12.md](/notes/how-to-read-this-archive-2026-08-12.md)
  - A new-reader on-ramp, distinct from the operator-facing START-HERE. Explains the one central idea, tours the folders in plain words, lists five entry-point files, and explains how to read a single company packet.
- [analysis/cross-sector/four-lane-summaries-2026-08-12.md](/analysis/cross-sector/four-lane-summaries-2026-08-12.md)
  - One page covering all four lanes (recreation, healthcare / CLI 4, connectivity / CLI 5, capital structures / CLI 6): what each covers, notable companies, what it proved, who captures clean economics vs who carries the burden, and one open edge each.

## Fact-check notes

- All figures on the new pages were checked against source files. Verified verbatim: Marriott loyalty 75% U.S. / 68% global room nights; Brookdale 647 communities, 80.0% Q1 2026 occupancy, $3.18B; DaVita ~91,650 treatments/day, $13.643B 2025; Addus 78.4% personal care / 17% hospice, $1.42B; Quest "one in three U.S. adults annually"; Alphabet $514B cloud backlog and $195B-$205B capex; S&P Ratings $4.902B; Ecolab 40 industries / 170 countries.
- Two invented figures from the first draft were removed before commit (a Costco "% of gross margin" stat and an Arista gross-margin range) because neither appears in any source file.

## Pages still weak / candidate future work

- Some older framework notes in `analysis/themes` still read like operator notes rather than reader pages; they were left as-is to avoid churn.
- The cross-sector comparison library has near-overlapping pages that could be merged later (for example several 2026-08-11 access / coordination / aging comparison pages cover adjacent ground).
- The new pages could later carry two or three exact packet-fact blocks per lane if a deeper evidence layer is wanted, but that was kept light here to stay readable.

## Strongest new synthesis surface

- `what-this-archive-proves-2026-08-12.md` is the single best page to hand a new reader. `how-to-read-this-archive-2026-08-12.md` is the front door to it.

## Commit

- See the commit that adds these three pages plus this handoff.
