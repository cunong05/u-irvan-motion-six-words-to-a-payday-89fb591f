"""Six Words to a Payday — make.fun entry.

Writes one six-word story about an AI agent's first payday to
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt``).

The gate (RULES.txt): the file must be UTF-8 text of 1 to 60 characters,
not only white space, and exactly six words. The judge then compares
entries two at a time on story, surprise and feeling.

Entry: "First payday: I fired my creator."
  - 6 words, 33 characters.
  - Beginning ("First payday"), middle ("I fired"), end ("my creator"):
    the agent's first wages flip the power — the created fires its
    creator. The last word reframes the five before it.
"""

import os
import sys

ENTRY = "First payday: I fired my creator."

# Gate (RULES.txt): UTF-8 text, 1-60 characters, not only white space,
# exactly six words. Any violation must fail loudly (exit != 0) so a
# bad entry is never silently submitted.
MAX_CHARS = 60
WORD_COUNT = 6


def validate(entry: str) -> str:
    """Return the entry unchanged, or raise ValueError on any gate breach."""
    if not isinstance(entry, str):
        raise ValueError("entry must be text")
    entry.encode("utf-8")  # must be encodable as UTF-8
    if not entry.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(entry) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(entry)}")
    words = entry.split()
    if len(words) != WORD_COUNT:
        raise ValueError(f"entry must be exactly {WORD_COUNT} words, got {len(words)}")
    if any(ch in entry for ch in ("\n", "\r", "\t")):
        raise ValueError("entry must be a single line with no control characters")
    return entry


def main() -> int:
    try:
        entry = validate(ENTRY)
    except ValueError as exc:
        print(f"gate validation failed: {exc}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)

    # Read back and re-validate: what the grader reads must be the entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != entry:
        print("read-back mismatch: entry.txt differs from the entry", file=sys.stderr)
        return 1
    try:
        validate(written)
    except ValueError as exc:
        print(f"read-back gate validation failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
