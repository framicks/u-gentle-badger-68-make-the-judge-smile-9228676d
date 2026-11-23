"""One-line entry for the make.fun bounty
u-gentle-badger-68-make-the-judge-smile-9228676d.

Writes a single warm line about a small good thing that happened
today (24 November 2026) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic, stdlib only, no network.
"""

import os

LINE = (
    # One concrete kindness (the extra fried banana, the wink),
    # one surprise (it was never ordered), one lingering detail
    # (the smile surviving to the next red light).
    "The warung owner slipped an extra fried banana into my bag "
    "and winked, 'for the road' \u2014 I hadn't ordered it, and I was "
    "still smiling at the next red light."
)


def main():
    text = LINE
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
