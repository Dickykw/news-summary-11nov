#!/usr/bin/env python3
"""Write the best summary of 11 November's world news to /output/entry.txt.

The summary is the summary.txt beside this file: world news of Wednesday
11 November 2026, written in English. The program only copies those exact
bytes to the output path, so both runs write identical bytes and no network
is used.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "summary.txt")
OUTPUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def check_output(path):
    """Check the written file against the competition's gate rules.

    The gate takes UTF-8 text of 1 to 2,000 characters (Unicode code
    points, a line end counting like any other character) that is not
    only white space. Return the character count.
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    chars = len(text)
    if not 1 <= chars <= 2000:
        raise ValueError(f"output is {chars} characters, outside 1-2000")
    if not any(not c.isspace() for c in text):
        raise ValueError("output is only white space")
    return chars


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    chars = check_output(OUTPUT)
    print(f"Wrote {OUTPUT} ({os.path.getsize(OUTPUT)} bytes, {chars} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
