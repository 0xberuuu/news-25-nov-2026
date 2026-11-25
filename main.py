#!/usr/bin/env python3
"""Entrypoint for the news-image-20261125 make.fun entry.

Copies this repository's pre-generated front-page image (entry.png) into
the output directory requested by the harness.

The harness sets MAKEFUN_OUTPUT_DIR; when it is absent the image is
written to ./out. Standard library only.

Usage:
    python3 main.py
    MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    if not os.path.isfile(SOURCE):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    print("wrote", dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
