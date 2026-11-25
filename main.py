# SPDX-License-Identifier: MIT
"""The GPS Swears It Was a Shortcut — writes the GPS's one-line excuse to /output/entry.txt."""
import os

LINE = "Wrong turn? The map promised a shortcut, the satellite promised a road — neither warned you'd end up reversing out of a lakeside wedding in a swan boat."


def main() -> None:
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
