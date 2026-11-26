#!/usr/bin/env python3
"""The Moon Gets One Star — a one-star review of the Moon.

Writes the review to /output/entry.txt (120 characters max).
Standard library only.
"""

import os

# One-star review of the Moon: it shows up late, overstays, leaves
# without a word — and the tide, its only witness, is still furious.
LINE = "★☆☆☆☆ Showed up late, stayed all night, left without a word. The tide is still furious."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
