#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert — make.fun entry.

Writes one satirical sentence (239 characters, one line) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is fixed and deterministic: every run writes the exact same
bytes, with no trailing newline, so the two grading runs agree.
"""

import os
import sys

LINE = (
    "The lawmaker has converted donors into votes, votes into a committee "
    "chair, and a committee chair into a book deal \u2014 yet the one file "
    "he cannot convert is the Word document on his own desktop, because "
    "'Save as PDF' is where his power ends."
)


def validate_line(line: str) -> None:
    """Guard: the line must satisfy the competition gate (1-320 chars,
    single line, not only whitespace, no trailing newline, no control
    characters that could split it across lines)."""
    if not 1 <= len(line) <= 320:
        raise ValueError("line must be 1-320 chars")
    if "\n" in line or "\r" in line or line != line.strip():
        raise ValueError("line must be a single line with no trailing newline")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def main() -> int:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
