"""Describe Your Ex in One Word — entry: Refund.

One word, no caption. The ex was a defective purchase: returned
for a full refund. The joke lands in a single retail transaction —
a person processed like faulty goods, money back, no questions asked.
"""

WORD = "Refund"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    word = WORD.strip()
    assert word, "entry must not be empty"
    assert " " not in word and "\n" not in word and "\t" not in word, (
        "entry must be a single word"
    )
    assert 1 <= len(word) <= 111, "entry must be 1-111 characters"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word + "\n")


if __name__ == "__main__":
    main()
