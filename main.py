"""The Painfully Honest Out-of-Office — make.fun entry.

Writes a single painfully honest but still polite out-of-office
auto-reply to /output/entry.txt. Stdlib only, deterministic, offline.
"""

from pathlib import Path

LINE = (
    "Thank you for your email \u2014 I'm out of office and honestly not "
    "reading it, because a holiday spent in my inbox isn't a holiday; "
    "I'll reply with my full attention when I return."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate: 1-200 characters, not only whitespace — assert before writing.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the gate"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
