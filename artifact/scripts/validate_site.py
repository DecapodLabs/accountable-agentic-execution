#!/usr/bin/env python3
"""Validate the static project page and its repository-local links."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            if values["id"] in self.ids:
                raise SystemExit(f"duplicate HTML id: {values['id']}")
            self.ids.add(values["id"] or "")
        if tag == "a" and values.get("href"):
            self.hrefs.append(values["href"] or "")


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    page = root / "pages" / "index.html"
    text = page.read_text()
    parser = SiteParser()
    parser.feed(text)
    if "synthetic" not in text.lower() or "no controlled result" not in text.lower():
        raise SystemExit("site must retain pre-results and synthetic-data boundaries")
    if re.search(r"(?:38\.3|45\.7|82\.9)", text):
        raise SystemExit("legacy synthetic metric values remain in public page source")
    for href in parser.hrefs:
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        if href.startswith("#"):
            if href[1:] not in parser.ids:
                raise SystemExit(f"missing local anchor: {href}")
            continue
        target = (page.parent / href).resolve()
        if href == "./Accountable_Agentic_Execution.pdf":
            target = root / "paper" / "Accountable_Agentic_Execution.pdf"
        if not target.exists():
            raise SystemExit(f"missing local page link target: {href}")
    print(f"validated site HTML with {len(parser.ids)} ids and {len(parser.hrefs)} links")


if __name__ == "__main__":
    main()
