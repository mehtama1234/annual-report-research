# Athene Schedule D Sparse-Row Classification Pass 1

This worklist classifies rows with at least one blank among actual cost,
par value, fair value, and book/adjusted carrying value. It does not fill
or reinterpret blanks.

- Full parser rows: `8,648`
- Sparse rows: `608`
- Complete-value rows: `8,040`

## Classification counts

| Classification | Rows | Treatment |
|---|---:|---|
| `source-visible-sparse-nim` | 107 | Preserve blanks; no imputation. |
| `source-visible-or-legacy-abs-sparse` | 298 | Inspect source row and subtype. |
| `non-nim-sparse-row` | 203 | Highest-priority column review. |

## Largest sparse pages

| Page | Sparse rows |
|---:|---:|
| 5912 | 45 |
| 5913 | 45 |
| 5971 | 43 |
| 5970 | 42 |
| 5914 | 31 |
| 5928 | 26 |
| 5937 | 21 |
| 5939 | 19 |
| 5917 | 18 |
| 5927 | 18 |
| 5969 | 18 |
| 5938 | 16 |
| 5972 | 15 |
| 5916 | 12 |
| 5962 | 12 |

## Boundary

A source-visible blank is not zero, a parser error, or borrower cash.
The output is a repair and review worklist only. Any corrected row
must be checked against the source page and aggregate reconciliation
before it can enter income, proceeds, liability-cost, or return work.

Decision: `sparse-row-classification-created; no-imputation-gate-active`
