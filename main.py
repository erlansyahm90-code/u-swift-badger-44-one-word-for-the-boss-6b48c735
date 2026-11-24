"""One Word for the Boss — entry: Clockwatcher.

A single word that describes the boss: the one who counts your minutes.
It works in a kitchen, a warehouse, or an office — the boss who watches
the clock on your time while wasting plenty of it himself. Funny because
it flips the power dynamic: he guards the clock, you lose the minutes.
"""

ENTRY_WORD = "Clockwatcher"  # 12 chars, one word, no spaces — gate: 1-30 chars


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_WORD)


if __name__ == "__main__":
    main()
