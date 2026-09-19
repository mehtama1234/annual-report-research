#!/usr/bin/env python3
"""Check relative and repository-root Markdown links in the research archive.

Usage: python3 scripts/check-internal-links.py

Links to web pages and anchors are excluded. Historical absolute links are
resolved against the current checkout when they use the repository root or
the older archive root. The reader uses `/cluster/...` as a virtual route,
and the research chain intentionally links to sibling repositories; both are
valid link classes rather than local Markdown files.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LEGACY_ROOTS = (
    "/home/manishmehta/ui-projects/annual-report-research-new-lanes/",
    "/home/manishmehta/ui-projects/annual-report-research/",
    str(ROOT) + "/",
)
LINK = re.compile(r"\]\(([^)]+)\)")


def resolve(source: Path, raw: str) -> Path | None:
    target = raw.split("#", 1)[0].split("?", 1)[0]
    if not target or target.startswith(("http://", "https://", "mailto:")):
        return None
    # These are virtual routes served by site/reader.js, not filesystem paths.
    if target.startswith("/cluster/"):
        return None
    for prefix in LEGACY_ROOTS:
        if target.startswith(prefix):
            return ROOT / target[len(prefix):]
    # Cross-repository source links are deliberately absolute so they remain
    # unambiguous when a document is read outside this checkout.
    sibling_root = ROOT.parent
    sibling_prefix = str(sibling_root) + "/"
    if target.startswith(sibling_prefix):
        return Path(target)
    if target.startswith("/"):
        return ROOT / target.lstrip("/")
    return (source.parent / target).resolve()


def main() -> int:
    total = 0
    broken: list[tuple[str, str]] = []
    for source in sorted((ROOT / "analysis").rglob("*.md")):
        text = source.read_text(errors="ignore")
        for raw in LINK.findall(text):
            target = resolve(source, raw)
            if target is None:
                continue
            total += 1
            if not target.exists():
                broken.append((str(source.relative_to(ROOT)), raw))

    print(f"internal_links={total}")
    print(f"broken_links={len(broken)}")
    for source, raw in broken:
        print(f"{source} -> {raw}")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
