#!/usr/bin/env python3
"""Split FAQ markdown files by ### headings into individual files."""

import re
import sys
from pathlib import Path


def slugify(text: str) -> str:
    """Convert a heading string to a filename-safe slug."""
    # lowercase
    slug = text.lower()
    # replace non-alphanumeric (except spaces) with nothing
    slug = re.sub(r"[^\w\s-]", "", slug)
    # collapse whitespace to single hyphens
    slug = re.sub(r"\s+", "-", slug)
    # collapse multiple hyphens
    slug = re.sub(r"-+", "-", slug)
    # strip leading/trailing hyphens
    slug = slug.strip("-")
    return slug


def split_faq_files(src_dir: Path, dst_dir: Path) -> None:
    """Read all .md files in src_dir, split by ### headings, write to dst_dir."""
    dst_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(src_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {src_dir}")
        return

    total_sections = 0

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        print(f"Processing: {md_file.name}")

        # Split on lines that start with ### (level-3 headings)
        # We capture the heading line and the body that follows
        sections = re.split(r"\n(?=### )", content)

        for section in sections:
            section = section.strip()
            if not section:
                continue

            # Extract the heading line (first line starting with ###)
            match = re.match(r"### (.+)", section)
            if not match:
                # Content before the first ### heading (title, breadcrumb) — skip
                continue

            heading_text = match.group(1).strip()
            slug = slugify(heading_text)

            if not slug:
                print(f"  Warning: empty slug for heading: {heading_text!r}")
                continue

            # Write the section as its own file
            (dst_dir / md_file.name[:-3]).mkdir(parents=True, exist_ok=True)
            out_path = dst_dir / md_file.name[:-3] /f"{slug}.md"
            out_path.write_text(section + "\n", encoding="utf-8")
            total_sections += 1
            print(f"  -> {out_path.name}")

    print(f"\nDone. {total_sections} sections written to {dst_dir}/")


def main():
    project_root = Path(__file__).resolve().parent
    src_dir = project_root / "md" / "faq"
    dst_dir = project_root / "md" / "faq-splitted"

    if not src_dir.is_dir():
        print(f"Error: source directory not found: {src_dir}", file=sys.stderr)
        sys.exit(1)

    split_faq_files(src_dir, dst_dir)


if __name__ == "__main__":
    main()
