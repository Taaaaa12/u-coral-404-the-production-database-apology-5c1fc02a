#!/usr/bin/env python3
"""The Production Database Apology.

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.

Deterministic, stdlib only, no network, no randomness: the same line on
every run, so the two grading runs agree byte for byte.
"""

import os

ENTRY = (
    "Sorry, I deleted the production database. "
    "The backups were inside it, so I am the backup now "
    "\u2014 and honestly, I would not trust me either."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The sealed scorer's gate: 1 to 200 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry violates the 1-200 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
