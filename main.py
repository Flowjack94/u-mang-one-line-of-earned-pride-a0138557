#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.
The line is a fixed constant, so every run produces byte-identical output.
"""

import os
import sys

ENTRY = (
    "Eight-year-old Ana held the ladder steady while her grandfather "
    "hammered the last nail, and when the birdhouse didn't fall, "
    "neither of them said a word."
)

MIN_CHARS = 1
MAX_CHARS = 240


def validate_entry(text: str) -> None:
    """Check the entry against the competition gate.

    Raises ValueError if the text is not 1-240 characters, not UTF-8,
    or only whitespace.
    """
    # UTF-8 round-trip check.
    text.encode("utf-8")
    if not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline characters)")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)}"
        )


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    validate_entry(ENTRY)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
