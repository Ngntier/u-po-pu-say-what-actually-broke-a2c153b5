#!/usr/bin/env python3
"""Say What Actually Broke — one line of brutal, funny error copy.

Writes the single error line to /output/entry.txt. Pure stdlib,
deterministic: identical bytes on every run.
"""

LINE = (
    "Your file is gone. The update meant to stop deleting files "
    "deleted yours instead \u2014 it worked exactly as designed, "
    "just not as intended."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-200")
    if "\n" in LINE or LINE != LINE.strip():
        raise SystemExit("line must be a single line with no surrounding whitespace")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
