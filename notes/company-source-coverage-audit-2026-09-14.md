# Company-source coverage audit — 2026-09-14

Scope: all 222 files under `analysis/deep-company-pages/`.

The reader API was queried for each company page and its `source_summary` was
checked. The result is:

- 222 of 222 company pages contain source evidence links.
- 584 linked local sources are available in the checkout.
- 5 additional links resolve through the archive manifest.
- 2 company pages rely on external filing or investor-relations links rather
  than a locally saved source copy: ASML and GE Vernova.
- 0 company pages are source-free.

The two external-only pages are not treated as locally verified. The reader
shows their external filing or research-link count in the evidence trail. This
keeps the distinction visible between a source that can be opened from the
checkout and a source that depends on the external URL remaining available.

The `linked` and `available` counts are dossier-level counts. They measure links
written directly in the company page, not the full number of sources nested in
the linked packet or ledger. A page with one local packet link may still have
several official SEC or IR links and a much larger packet-level evidence chain;
the count should therefore not be used as a research-depth score. The current
catalog audit finds 107 company pages with fewer than three direct local links.
Those pages are not source-free: they are retained as qualified route-depth
cases unless the article is one of the two explicitly external-only pages above.

The reader-visible cohort has a stronger result. Every company directly linked
from the landing-page themes, findings, cohort cards, or research-state cards
has at least three locally available evidence links, except ASML and GE
Vernova. Those two remain visibly marked as external-only because their raw
artifacts are not in this checkout.

Recheck the status through the reader endpoint:

```text
http://localhost:8765/api/article?file=analysis/deep-company-pages/{slug}.md
```

The five-question coverage audit is separate: it tests whether the page
contains business economics, cash conversion, risks and accounting tests,
valuation, and next-filing checks. It does not imply that every cited source is
stored locally.

## Packet Inputs Used

- `analysis/deep-company-pages/*.md`;
- the reader API's catalog and article source summaries; and
- the current local source packets, source ledgers, and archive manifest.

## Skeptical Reader Test

- Can the reader distinguish a locally available packet from an external-only
  filing route?
- Does the count cover every deep company page rather than only the homepage
  examples?
- Does a five-question page still disclose a missing raw artifact when one is
  not locally recoverable?

## Insight-System Maintenance

Recheck the source boundary with:

```text
http://localhost:8765/api/catalog
```

For a specific company, query the article endpoint shown above and inspect its
`source_summary` fields before describing the page as locally reproducible.

The repository control check is `bash scripts/verify-insight-system.sh`.
