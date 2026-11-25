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


def main() -> int:
    words = ENTRY.split()
    if len(words) != 6:
        print(f"entry must be exactly six words, got {len(words)}", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 60:
        print(f"entry must be 1-60 characters, got {len(ENTRY)}", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be only white space", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
