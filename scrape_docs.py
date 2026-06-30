#!/usr/bin/env python3
"""
Scrape Wikidot documentation pages.
Reads links.txt, fetches each unique page from www.wikidot.com,
extracts the content of <div class="col-md-9">, and saves to files.
"""

import requests
import time
import os
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag

BASE_URL = "https://www.wikidot.com"
DELAY = 1.5  # seconds between requests to avoid rate limiting
OUTPUT_ROOT = Path("/home/ect/wd-rag")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; WikidotDocScraper/1.0; +https://www.wikidot.com)"
}


def read_links(filepath: str) -> list[str]:
    """Read links from file, return deduplicated list (by base URL, sans fragment)."""
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    # Remove leading tab if present (from the file format)
    lines = [line.lstrip("\t") for line in lines]

    seen = set()
    unique = []
    for path in lines:
        # Strip fragment (#...) - the server returns the same page regardless
        base_path, _ = urldefrag(path)
        if base_path not in seen:
            seen.add(base_path)
            unique.append(path)  # keep original path (with fragment) for file naming

    return unique


def path_to_filepath(link_path: str) -> Path:
    """
    Convert a URL path to a local file path.
    /doc-wiki-syntax:inline-formatting  -> doc-wiki-syntax/inline-formatting.txt
    /doc-modules:listdrafts-module      -> doc-modules/listdrafts-module.txt
    /doc:users                          -> doc/users.txt
    /faq:upgrades                       -> faq/upgrades.txt
    """
    # Strip leading slash and fragment
    clean = link_path.lstrip("/")
    if "#" in clean:
        clean = clean.split("#")[0]

    if ":" in clean:
        dir_part, file_part = clean.split(":", 1)
        dir_path = Path("raw/" + dir_part)
        file_name = f"{file_part}.txt"
    else:
        # Fallback: use the whole thing as filename
        dir_path = Path("raw")
        file_name = f"{clean}.txt"

    return dir_path / file_name


def scrape_page(url: str) -> str | None:
    """Fetch a page and extract the col-md-9 inner HTML. Returns HTML string or None."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"  ERROR fetching {url}: {e}")
        return None

    soup = BeautifulSoup(resp.text, "html.parser")
    content_div = soup.find(class_="col-md-9")

    if content_div is None:
        # Try alternative: maybe "col-md-9" appears with another class
        content_div = soup.find("div", class_=lambda c: c and "col-md-9" in c.split())
        if content_div is None:
            print(f"  WARNING: No .col-md-9 found at {url}")
            return None

    # Return inner HTML (with all tags preserved), without the outer div wrapper
    html = content_div.decode_contents()
    return html


def main():
    links_file = OUTPUT_ROOT / "links.txt"
    if not links_file.exists():
        print(f"ERROR: {links_file} not found")
        return

    links = read_links(str(links_file))
    print(f"Total entries in links.txt: {len(links)}")
    print(f"Unique pages to fetch: {len(set(urldefrag(l)[0] for l in links))}")
    print(f"Delay between requests: {DELAY}s\n")

    success_count = 0
    fail_count = 0
    skip_count = 0

    for i, link_path in enumerate(links, 1):
        # Build full URL (strip fragment for the actual request)
        base_path, fragment = urldefrag(link_path)
        url = urljoin(BASE_URL, base_path)

        # Determine output file path
        filepath = OUTPUT_ROOT / path_to_filepath(link_path)

        # Skip if already downloaded
        if filepath.exists():
            print(f"[{i}/{len(links)}] SKIP (exists)  {filepath}")
            skip_count += 1
            continue

        print(f"[{i}/{len(links)}] GET {url}  ->  {filepath}")

        text = scrape_page(url)

        if text is None or not text.strip():
            fail_count += 1
            # Even if failed, we might have gotten partial content
            if text:
                filepath.parent.mkdir(parents=True, exist_ok=True)
                filepath.write_text(text)
            time.sleep(DELAY)
            continue

        # Save
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(text)
        success_count += 1

        print(f"  OK: {len(text)} chars saved")

        # Delay to be polite
        time.sleep(DELAY)

    print(f"\n{'='*60}")
    print(f"Done! Success: {success_count}, Failed: {fail_count}, Skipped: {skip_count}")


if __name__ == "__main__":
    main()
