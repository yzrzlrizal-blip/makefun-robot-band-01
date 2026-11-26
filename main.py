"""Name the Robot Band — make.fun entry.

Writes one funny name for a band made of robots, plus a few words on
its hit song, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library, deterministic: the same bytes every run.
"""

import os
import sys

ENTRY = "The Roomba Rumblers \u2014 hit single \u2018Suck It Up (Buttercup)\u2019"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Re-read and verify the exact bytes we wrote.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("entry.txt verification failed", file=sys.stderr)
        return 1
    print(f"wrote {len(written)} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
