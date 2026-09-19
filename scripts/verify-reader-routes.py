#!/usr/bin/env python3
"""Verify local article and company routes surfaced by the editorial reader."""

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
READER = ROOT / "site" / "reader.js"


def main():
    source = READER.read_text()
    article_paths = set(
        re.findall(r"analysis/(?:cross-sector|first-principles|company-first-principles)/[A-Za-z0-9_.-]+\.md", source)
    )
    missing_articles = sorted(path for path in article_paths if not (ROOT / path).is_file())

    company_pairs = []
    for block in re.findall(r"companies:\[(.*?)\]\}", source):
        company_pairs.extend(re.findall(r"\[['\"]([^'\"]+)['\"],['\"]([a-z0-9-]+)['\"]\]", block))
    for block in re.findall(r"companies\.push\((.*?)\);", source):
        company_pairs.extend(re.findall(r"\[['\"]([^'\"]+)['\"],['\"]([a-z0-9-]+)['\"]\]", block))
    company_slugs = {slug for _, slug in company_pairs}
    missing_companies = sorted(
        slug for slug in company_slugs if not (ROOT / "analysis" / "deep-company-pages" / f"{slug}.md").is_file()
    )

    if missing_articles or missing_companies:
        if missing_articles:
            print("Missing article routes:", *missing_articles, sep="\n  ")
        if missing_companies:
            print("Missing company routes:", *missing_companies, sep="\n  ")
        raise SystemExit(1)

    print(
        f"Reader route verification passed: {len(article_paths)} article paths, "
        f"{len(company_slugs)} company slugs"
    )


if __name__ == "__main__":
    main()
