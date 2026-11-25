#!/usr/bin/env python3
"""Entry program for One Emoji, One Dream Vacation.

Writes exactly ONE emoji (gate: 1 to 8 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt: the dream vacation in a single glyph. A desert
island -- the postcard answer, and still the truest one.
"""

import os

EMOJI = "🛌"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
