#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun bounty entry.

Writes one sick-day excuse, as if typed into a message to the boss,
to /output/entry.txt.

Chosen from 14 fresh candidates against the judge brief: half-believable
(a pulled muscle), a fresh idea (injured doing the laziest thing possible),
and the twist lands on the last words ("on strike").
"""

import os

LINE = (
    "Can't come in today — I pulled a muscle reaching for the snooze "
    "button and now my whole back is on strike."
)

OUTPUT_PATH = "/output/entry.txt"


MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
