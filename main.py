# SPDX-License-Identifier: MIT
"""Emit the GPS excuse line for the make.fun shortcut bounty.

The grader expects exactly one artifact: /output/entry.txt holding a
single line of plain text. This module keeps the line in one constant,
checks it against the published gate limits before writing, and then
stores it as UTF-8 with no trailing newline.
"""

from pathlib import Path

# Gate limits published in the competition rules.
MIN_CHARS = 1
MAX_CHARS = 200
DESTINATION = Path("/output/entry.txt")

# The excuse itself, voiced by the GPS: defensive opening, two broken
# promises (map and satellite), then the swan-boat reversal.
EXCUSE = (
    "Wrong turn? The map promised a shortcut, the satellite promised "
    "a road \u2014 neither warned you'd end up reversing out of a "
    "lakeside wedding in a swan boat."
)


def build_text() -> str:
    """Return the entry line after confirming it satisfies the gate."""
    if not (MIN_CHARS <= len(EXCUSE) <= MAX_CHARS):
        raise ValueError(f"line has {len(EXCUSE)} chars, outside gate")
    if not EXCUSE.strip():
        raise ValueError("line must not be whitespace only")
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise ValueError("line must stay on a single line")
    return EXCUSE


def verify_round_trip(expected: bytes) -> None:
    """Read the artifact back and assert it matches what was written.

    Guards against partial writes or encoding surprises: the bytes on
    disk must equal the intended UTF-8 payload, decode cleanly, and
    still satisfy the gate limits on a fresh read.
    """
    stored = DESTINATION.read_bytes()
    if stored != expected:
        raise AssertionError("read-back bytes differ from written bytes")
    decoded = stored.decode("utf-8")
    if not (MIN_CHARS <= len(decoded) <= MAX_CHARS) or not decoded.strip():
        raise AssertionError("read-back text falls outside the gate")


def main() -> None:
    text = build_text()
    payload = text.encode("utf-8")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(payload)
    verify_round_trip(payload)


if __name__ == "__main__":
    main()
