#!/usr/bin/env python3
"""Write one office-life joke to entry.txt.

make.fun bounty: "Make the AI Judge Laugh: Office Jokes".
The program writes a single one-line joke about office life
(under 200 characters) to <MAKEFUN_OUTPUT_DIR>/entry.txt,
defaulting to /output/entry.txt under the grading harness.
Python 3.13, standard library only, deterministic, no network.
"""

import os

JOKE = (
    "I replied-all asking everyone to stop replying-all, "
    "and now 400 colleagues are agreeing with me in real time."
)


def main() -> None:
    # Self-check against the competition gate before writing:
    # UTF-8 text, 1 to 199 characters, a single non-blank line.
    if not 1 <= len(JOKE) <= 199:
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-199")
    if "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke must be a single non-blank line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the joke, no trailing newline, so the file
    # holds one line of len(JOKE) characters.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
