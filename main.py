"""One Word for the Boss — entry generator.

Writes the single-word entry "Clockwatcher" to /output/entry.txt
(creating the /output directory if it does not exist).
The word is 12 characters, one word, within the 1-30 character gate.
"""

import os

# The entry word: 12 characters, a single word — inside the 1-30 char gate.
ENTRY = "Clockwatcher"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {ENTRY!r} to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
