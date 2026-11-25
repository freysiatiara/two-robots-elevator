"""Two Robots in an Elevator — make.fun bounty entry.

Writes one line of awkward robot-to-robot elevator small talk to the
output file. Standard library only.
"""

import os
import sys

LINE = "I checked my logs: we've shared this elevator 47 times and I've never once asked about your servos."


def resolve_output_path():
    """Resolve the output path, preferring the environment's choice."""
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main():
    path = resolve_output_path()
    encoded = LINE.encode("utf-8")
    if not 1 <= len(encoded) <= 200:
        raise ValueError(
            "entry line must be 1-200 UTF-8 bytes, got %d" % len(encoded)
        )
    try:
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(LINE)
        os.chmod(path, 0o644)
    except OSError:
        fallback = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "entry.txt"
        )
        with open(fallback, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(LINE)
        os.chmod(fallback, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
