#!/usr/bin/env python3
"""
Convert all .txt files under raw/ from HTML to Markdown, writing .md files under md/.
Unknown/unrecognizable divs are ignored (their children are still processed).
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

RAW_DIR = Path("raw")
MD_DIR = Path("md")

# Div classes/ids whose entire subtree should be SKIPPED (dynamic widgets, empty containers)
SKIP_DIV_IDS = {
    "action-area",
    "who-invited-results-box",
    "user-lookup-list",
    "toc-list",
    "toc-action-bar",
}

SKIP_DIV_CLASSES = {
    "yui-content",
    "yui-navset",
    "autocomplete-container",
    "autocomplete-list",
    "featured-site-box",
    "featured-site-grid-box",
    "featured-site-hovertip",
    "hovertip-container",
    "page-rate-widget-box",
    "changes-list",
    "changes-list-item",
    "page-calendar-box",
    "new-page-box",
    "pages-list",
    "site-changes-box",
    "backlinks-module-box",
    "list-pages-box",
    "list-pages-item",
}

# Div ids that start with these prefixes → skip
SKIP_DIV_ID_PREFIXES = (
    "category-pages-",
    "wiki-tabview-",
    "wiki-tab-",
    "featured-site-grid-image-",
    "featured-site-image-",
    "special",
    "equation-",  # rendered math, we use the source from <pre>/<code>
)


def should_skip_div(tag: Tag) -> bool:
    """Return True if this div should be completely skipped (dynamic widget etc)."""
    if tag.name != "div":
        return False
    # Skip hidden divs
    style = tag.get("style", "")
    if "display: none" in style or "display:none" in style:
        return True
    div_id = tag.get("id", "")
    if div_id in SKIP_DIV_IDS:
        return True
    if any(div_id.startswith(prefix) for prefix in SKIP_DIV_ID_PREFIXES):
        return True
    classes = tag.get("class", [])
    if isinstance(classes, str):
        classes = [classes]
    for cls in classes:
        if cls in SKIP_DIV_CLASSES:
            return True
    return False


def reverse_wiki_email(text: str) -> str:
    """Reverse a wikidot obfuscated email.
    Format: reversed_domain|reversed_localpart  (optionally duplicated with #)
    E.g. moc.todikiw|troppus#moc.todikiw|troppus → support@wikidot.com
    """
    # Take the first part before # (they are duplicates)
    part = text.split("#")[0]
    # Split into reversed domain and reversed localpart
    pieces = part.split("|")
    if len(pieces) == 2:
        reversed_domain, reversed_localpart = pieces
        domain = reversed_domain[::-1]
        localpart = reversed_localpart[::-1]
        return f"{localpart}@{domain}"
    # Fallback: reverse the whole thing
    return text[::-1]


def process_soup(element, indent_level: int = 0) -> str:
    """Recursively convert a BeautifulSoup element tree to Markdown string."""
    if element is None:
        return ""

    if isinstance(element, NavigableString):
        text = str(element)
        # Preserve significant whitespace in pre/code context? No, just strip extra.
        # But don't add extra newlines for blank text nodes.
        return text

    if not isinstance(element, Tag):
        return ""

    tag_name = element.name

    # --- Skip entire subtrees for known dynamic/widget divs ---
    if tag_name == "div" and should_skip_div(element):
        return ""

    # --- page-title → H1 ---
    if tag_name == "div" and "page-title" in (element.get("class") or []):
        text = element.get_text(strip=True)
        return f"# {text}\n\n"

    # --- breadcrumb ---
    if tag_name == "div" and "breadcrumb" in (element.get("class") or []):
        parts = []
        for child in element.children:
            if isinstance(child, Tag) and child.name == "a":
                parts.append(child.get_text(strip=True))
            elif isinstance(child, NavigableString):
                t = str(child).strip()
                # Strip leading/trailing breadcrumb separators
                t = re.sub(r'^[»›>]\s*', '', t)
                t = re.sub(r'\s*[»›>]$', '', t)
                t = t.strip()
                if t:
                    parts.append(t)
        if parts:
            return "> " + " > ".join(parts) + "\n\n"
        return ""

    # --- page-content → process children ---
    if tag_name == "div" and element.get("id") == "page-content":
        return process_children(element)

    # --- code block container (div.code) ---
    if tag_name == "div" and "code" in (element.get("class") or []):
        return process_children(element)

    # --- syntax highlighting container ---
    if tag_name == "div" and "hl-main" in (element.get("class") or []):
        return process_children(element)

    # --- Bootstrap row/col ---
    if tag_name == "div" and ("row" in (element.get("class") or []) or
                               any(c.startswith("col-") for c in (element.get("class") or []))):
        return process_children(element)

    # --- module-infobox → just process children ---
    if tag_name == "div" and "module-infobox" in (element.get("class") or []):
        return process_children(element)

    # --- wiki-note → blockquote ---
    if tag_name == "div" and "wiki-note" in (element.get("class") or []):
        content = process_children(element)
        lines = content.strip().split("\n")
        quoted_lines = []
        for line in lines:
            if line.strip():
                quoted_lines.append(f"> {line}")
            else:
                quoted_lines.append(">")
        return "\n".join(quoted_lines) + "\n\n"

    # --- bibliography ---
    if tag_name == "div" and "bibitems" in (element.get("class") or []):
        return process_children(element)

    if tag_name == "div" and "bibitem" in (element.get("class") or []):
        return process_children(element) + "\n"

    # --- collapsible blocks ---
    if tag_name == "div" and any(c.startswith("collapsible-block") for c in (element.get("class") or [])):
        return process_children(element)

    # --- image container ---
    if tag_name == "div" and "image-container" in (element.get("class") or []):
        return process_children(element)

    # --- math equation (already rendered, skip — source is in <pre>) ---
    if tag_name == "div" and "math-equation" in (element.get("class") or []):
        return ""  # The LaTeX source is already in the <pre><code> above

    # --- footnotes ---
    if tag_name == "div" and ("footnotes-footer" in (element.get("class") or []) or
                               "footnote-footer" in (element.get("class") or [])):
        return process_children(element)

    # --- floatright (e.g., TOC) ---
    if tag_name == "div" and "floatright" in (element.get("class") or []):
        return ""  # Usually a redundant TOC

    # --- Generic divs with just style attributes → process children ---
    if tag_name == "div":
        cls = element.get("class") or []
        if isinstance(cls, str):
            cls = [cls]

        # div.title → bold heading (used in bibliography, footnotes)
        if "title" in cls:
            text = element.get_text(strip=True)
            return f"**{text}**\n\n"

        # Any other unrecognized div: skip the wrapper, process children
        return process_children(element)

    # --- Headings ---
    if tag_name in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(tag_name[1])
        prefix = "#" * level
        text = get_clean_text(element)
        return f"{prefix} {text}\n\n"

    # --- Paragraph ---
    if tag_name == "p":
        text = process_children(element).strip()
        if text:
            return text + "\n\n"
        return ""

    # --- Unordered list ---
    if tag_name == "ul":
        items = []
        for li in element.find_all("li", recursive=False):
            item_text = process_children(li).strip()
            # Indent continuation lines
            lines = item_text.split("\n")
            first = f"- {lines[0]}"
            rest = "\n".join(f"  {l}" for l in lines[1:])
            if rest:
                items.append(first + "\n" + rest)
            else:
                items.append(first)
        return "\n".join(items) + "\n\n"

    # --- Ordered list ---
    if tag_name == "ol":
        items = []
        for i, li in enumerate(element.find_all("li", recursive=False), 1):
            item_text = process_children(li).strip()
            lines = item_text.split("\n")
            first = f"{i}. {lines[0]}"
            rest = "\n".join(f"   {l}" for l in lines[1:])
            if rest:
                items.append(first + "\n" + rest)
            else:
                items.append(first)
        return "\n".join(items) + "\n\n"

    # --- List item (when found outside ul/ol context) ---
    if tag_name == "li":
        return process_children(element)

    # --- Strong / Bold ---
    if tag_name in ("strong", "b"):
        return f"**{process_children(element)}**"

    # --- Emphasis / Italic ---
    if tag_name in ("em", "i"):
        return f"*{process_children(element)}*"

    # --- Inline code (tt) ---
    if tag_name == "tt":
        return f"`{process_children(element)}`"

    # --- Code block ---
    if tag_name == "pre":
        code_tag = element.find("code")
        if code_tag:
            text = code_tag.get_text()
        else:
            text = element.get_text()
        # Determine language (none for now)
        lang = ""
        text = text.rstrip()
        return f"```{lang}\n{text}\n```\n\n"

    # --- Inline code ---
    if tag_name == "code":
        # Check if parent is pre → handled above
        if element.parent and element.parent.name == "pre":
            return element.get_text()
        return f"`{element.get_text()}`"

    # --- Links ---
    if tag_name == "a":
        href = element.get("href", "")
        text = process_children(element).strip()
        cls = element.get("class") or []
        if isinstance(cls, str):
            cls = [cls]

        # Bibliography citation → [n]
        if "bibcite" in cls:
            return f"[{text}]"

        # Equation reference
        if "eref" in cls:
            return text

        # javascript: links → just text
        if href.startswith("javascript:"):
            return text

        if not href:
            return text

        if text:
            return f"[{text}]({href})"
        else:
            return href

    # --- Images ---
    if tag_name == "img":
        src = element.get("src", "")
        alt = element.get("alt", "")
        return f"![{alt}]({src})"

    # --- Line breaks ---
    if tag_name == "br":
        return "\n"

    # --- Horizontal rule ---
    if tag_name == "hr":
        return "---\n\n"

    # --- Blockquote ---
    if tag_name == "blockquote":
        content = process_children(element)
        lines = content.strip().split("\n")
        quoted_lines = []
        for line in lines:
            if line.strip():
                quoted_lines.append(f"> {line}")
            else:
                quoted_lines.append(">")
        return "\n".join(quoted_lines) + "\n\n"

    # --- Tables ---
    if tag_name == "table":
        return process_table(element)

    # --- Span handling ---
    if tag_name == "span":
        cls = element.get("class") or []
        if isinstance(cls, str):
            cls = [cls]

        # Wikidot obfuscated email
        if "wiki-email" in cls:
            text = element.get_text(strip=True)
            try:
                email = reverse_wiki_email(text)
            except Exception:
                email = text
            return email

        # Inline math
        if "math-inline" in cls:
            text = element.get_text(strip=True)
            return f"${text}$"

        # Equation number
        if "equation-number" in cls:
            return element.get_text()

        # Syntax highlighting spans → just text
        if any(c.startswith("hl-") for c in cls):
            return process_children(element)

        # Generic span → just text content
        return process_children(element)

    # --- Generic fallback for any unrecognized tag ---
    return process_children(element)


def process_children(element) -> str:
    """Process all children of an element and concatenate results."""
    result = []
    for child in element.children:
        result.append(process_soup(child))
    return "".join(result)


def get_clean_text(element) -> str:
    """Get clean text from an element, handling spans and links within headings."""
    result = []
    for child in element.children:
        if isinstance(child, NavigableString):
            result.append(str(child).strip())
        elif isinstance(child, Tag):
            if child.name == "span":
                # For heading spans (like <h3><span>text</span></h3>)
                result.append(child.get_text(strip=True))
            elif child.name == "a":
                result.append(child.get_text(strip=True))
            else:
                result.append(child.get_text(strip=True))
    return " ".join(r for r in result if r)


def process_table(table: Tag) -> str:
    """Convert HTML table to Markdown table."""
    rows = table.find_all("tr")
    if not rows:
        return ""

    md_rows = []
    header_done = False

    for row in rows:
        cells = row.find_all(["th", "td"])
        if not cells:
            continue
        cell_texts = []
        for cell in cells:
            # Replace <br/> with " / " before getting text, to separate values
            for br in cell.find_all("br"):
                br.replace_with(" / ")
            text = cell.get_text(strip=True).replace("\n", " ").replace("|", "\\|")
            # Collapse multiple spaces
            text = re.sub(r' +', ' ', text)
            cell_texts.append(text)
        md_rows.append("| " + " | ".join(cell_texts) + " |")

        # If first row has th cells, add separator after it
        if row.find("th") and not header_done:
            separators = ["---"] * len(cells)
            md_rows.append("| " + " | ".join(separators) + " |")
            header_done = True

    # If no th was used, add separator after first row anyway
    if not header_done and len(md_rows) > 0:
        ncols = len(rows[0].find_all(["th", "td"]))
        separators = ["---"] * ncols
        md_rows.insert(1, "| " + " | ".join(separators) + " |")

    return "\n".join(md_rows) + "\n\n"


def convert_file(input_path: Path, output_path: Path):
    """Convert a single .txt file from raw/ to .md in md/."""
    with open(input_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # Find the body or process the whole document
    body = soup.find("body")
    if body:
        root = body
    else:
        root = soup

    # Extract page-title first
    title_div = root.find("div", class_="page-title")
    title_md = ""
    if title_div:
        title_md = f"# {title_div.get_text(strip=True)}\n\n"

    # Extract breadcrumb
    breadcrumb_div = root.find("div", class_="breadcrumb")
    breadcrumb_md = ""
    if breadcrumb_div:
        parts = []
        for child in breadcrumb_div.children:
            if isinstance(child, Tag) and child.name == "a":
                parts.append(child.get_text(strip=True))
            elif isinstance(child, NavigableString):
                t = str(child).strip()
                # Strip leading/trailing breadcrumb separators
                t = re.sub(r'^[»›>]\s*', '', t)
                t = re.sub(r'\s*[»›>]$', '', t)
                t = t.strip()
                if t:
                    parts.append(t)
        if parts:
            breadcrumb_md = "> " + " > ".join(parts) + "\n\n"

    # Extract page-content
    page_content = root.find("div", id="page-content")
    content_md = ""
    if page_content:
        content_md = process_children(page_content)

    # Assemble
    md = title_md + breadcrumb_md + content_md

    # Clean up: collapse 3+ newlines to 2
    md = re.sub(r"\n{3,}", "\n\n", md)
    # Remove trailing whitespace on each line
    md = "\n".join(line.rstrip() for line in md.split("\n"))
    # Ensure exactly one trailing newline
    md = md.rstrip() + "\n"

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)


def main():
    """Walk raw/ and convert all .txt files to md/."""
    raw_dir = Path(RAW_DIR)
    md_dir = Path(MD_DIR)

    if not raw_dir.exists():
        print(f"Error: {raw_dir} does not exist")
        return

    txt_files = sorted(raw_dir.rglob("*.txt"))
    print(f"Found {len(txt_files)} .txt files to convert")

    for txt_path in txt_files:
        rel_path = txt_path.relative_to(raw_dir)
        md_path = md_dir / rel_path.with_suffix(".md")

        try:
            convert_file(txt_path, md_path)
            print(f"  OK: {rel_path} → {md_path}")
        except Exception as e:
            print(f"  FAIL: {rel_path} — {e}")

    print(f"\nDone. Converted files are in {md_dir}/")


if __name__ == "__main__":
    main()
