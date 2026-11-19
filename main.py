#!/usr/bin/env python3
"""make.fun entry for news-image-20261119.

Copies the committed entry.png that sits next to this script into
/output/entry.png, so the produced image is byte-identical on every run.
Standard library only; no network, no randomness, no timestamps.
"""
import os
import shutil


def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
