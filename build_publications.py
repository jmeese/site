#!/usr/bin/env python3
"""Generate publications.html from data/papers.bib.

Self-contained: no third-party libraries. The parser is brace-aware because the
.bib mixes clean entries with Zotero exports that use nested protective braces
(e.g. title = {A playbook... {Examining} {Google}'s response}) — a naive regex
would mis-split those. Re-run after editing the .bib, then commit the HTML output.

    python3 build_publications.py
"""

import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
BIB = HERE / "data" / "papers.bib"
OUT = HERE / "publications.html"

TYPE_TAGS = {
    "article": "Article",
    "incollection": "Chapter",
    "inbook": "Chapter",
    "book": "Book",
    "techreport": "Report",
}
SKIP_TYPES = {"comment", "string", "preamble"}


# --- BibTeX parsing -------------------------------------------------------

def read_braced(s, i):
    """s[i] is '{'. Return (inner_text, index_after_closing_brace), brace-matched."""
    depth, start = 0, i
    while i < len(s):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return s[start + 1 : i], i + 1
        i += 1
    return s[start + 1 :], len(s)  # unbalanced — take the rest


def read_quoted(s, i):
    """s[i] is '"'. Return (inner_text, index_after_closing_quote)."""
    depth, j = 0, i + 1
    while j < len(s):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
        elif s[j] == '"' and depth == 0:
            return s[i + 1 : j], j + 1
        j += 1
    return s[i + 1 :], len(s)


def parse_fields(s):
    """Parse 'name = value, ...' into a dict. Values may be {braced}, "quoted", or bare."""
    fields = {}
    i, n = 0, len(s)
    field_re = re.compile(r"\s*([A-Za-z][\w-]*)\s*=\s*")
    while i < n:
        m = field_re.match(s, i)
        if not m:
            nc = s.find(",", i)
            if nc == -1:
                break
            i = nc + 1
            continue
        name = m.group(1).lower()
        i = m.end()
        if i >= n:
            break
        if s[i] == "{":
            val, i = read_braced(s, i)
        elif s[i] == '"':
            val, i = read_quoted(s, i)
        else:
            nc = s.find(",", i)
            nc = n if nc == -1 else nc
            val, i = s[i:nc].strip(), nc
        fields[name] = val
        while i < n and s[i] in ", \n\r\t":
            i += 1
    return fields


def parse_entries(text):
    entries = []
    header = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,")
    for m in header.finditer(text):
        etype = m.group(1).lower()
        if etype in SKIP_TYPES:
            continue
        brace_start = text.index("{", m.start())
        body, _ = read_braced(text, brace_start)
        _, _, fields_str = body.partition(",")  # drop the citation key
        entries.append((etype, parse_fields(fields_str)))
    return entries


def count_headers(text):
    """How many real entries the file declares — used to verify nothing was dropped."""
    return sum(
        1
        for m in re.finditer(r"@(\w+)\s*\{", text)
        if m.group(1).lower() not in SKIP_TYPES
    )


# --- value formatting -----------------------------------------------------

def clean(v):
    v = v.replace("---", "—").replace("--", "–")  # em / en dash
    v = v.replace("{", "").replace("}", "")                  # protective braces
    v = v.replace("\\&", "&").replace("\\_", "_").replace("\\%", "%")
    return re.sub(r"\s+", " ", v).strip()


def format_authors(raw):
    parts = re.split(r"\s+and\s+", raw.strip())
    names = []
    for p in parts:
        p = p.strip()
        if "," in p:  # "Last, First" -> "First Last"
            last, _, first = p.partition(",")
            p = f"{first.strip()} {last.strip()}".strip()
        if p:
            names.append(p)
    if not names:
        return ""
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return ", ".join(names[:-1]) + f", and {names[-1]}"


def venue(etype, f):
    if etype == "article":
        return f.get("journal", "")
    if etype in ("incollection", "inbook"):
        bt = f.get("booktitle", "")
        return f"in {bt}" if bt else ""
    if etype == "book":
        return f.get("publisher", "")
    if etype == "techreport":
        return f.get("institution", f.get("publisher", ""))
    return f.get("journal", f.get("booktitle", ""))


def link(f):
    if f.get("doi"):
        return "https://doi.org/" + f["doi"].strip()
    return (f.get("url") or f.get("eprint") or "").strip()


def render_entry(etype, f):
    tag = TYPE_TAGS.get(etype, etype.capitalize())
    authors = html.escape(format_authors(clean(f.get("author", ""))))
    year = html.escape(clean(f.get("year", "n.d.")))
    title = html.escape(clean(f.get("title", "Untitled")))
    url = link(f)
    if url:
        title = f'<a href="{html.escape(url)}">{title}</a>'

    bits = []
    ven = clean(venue(etype, f))
    if ven:
        bits.append(f'<span class="venue">{html.escape(ven)}</span>')
    vol = clean(f.get("volume", ""))
    num = clean(f.get("number", ""))
    if vol and vol != "0":  # online-first entries carry a placeholder volume 0
        bits.append(html.escape(vol) + (f"({html.escape(num)})" if num and num != "0" else ""))
    pages = clean(f.get("pages", ""))
    if pages:
        bits.append("pp. " + html.escape(pages))
    detail = (", ".join(bits) + ".") if bits else ""

    line = f'<span class="tag">{tag}</span> {authors} ({year}). {title}. {detail}'
    return f'  <p class="pub">{line.strip()}</p>'


# --- page assembly --------------------------------------------------------

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Publications — James Meese</title>
<meta name="description" content="Publications by James Meese.">
<link rel="stylesheet" href="style.css">
</head>
<body>

<nav>
  <a href="index.html">Home</a>
  <a href="publications.html">Publications</a>
  <a href="talks.html">Talks</a>
</nav>

<h1>Publications</h1>
<p>{count} items. Generated from <code>data/papers.bib</code>.</p>

{body}

<footer>
  © James Meese. Built as plain HTML.
</footer>

</body>
</html>
"""


def year_key(entry):
    digits = re.search(r"\d{4}", entry[1].get("year", ""))
    return int(digits.group()) if digits else 0


def main():
    text = BIB.read_text(encoding="utf-8")
    entries = parse_entries(text)

    declared = count_headers(text)
    if len(entries) != declared:
        sys.exit(
            f"Parse mismatch: file declares {declared} entries but parsed "
            f"{len(entries)}. Fix the parser or the .bib before publishing."
        )

    entries.sort(key=year_key, reverse=True)  # newest first

    blocks, current_year = [], None
    for etype, f in entries:
        y = clean(f.get("year", "n.d.")) or "n.d."
        if y != current_year:
            current_year = y
            blocks.append(f'<p class="pub-year">{html.escape(y)}</p>')
        blocks.append(render_entry(etype, f))

    OUT.write_text(
        PAGE.format(count=len(entries), body="\n".join(blocks)), encoding="utf-8"
    )
    print(f"Wrote {OUT.name}: {len(entries)} entries.")


if __name__ == "__main__":
    main()
