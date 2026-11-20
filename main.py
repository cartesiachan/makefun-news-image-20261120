"""Entry for make.fun bounty news-image-20261120.

Sum up 20 November 2026 world news in one image.

Writes the pre-built 1024x1024 image (entry.png, in this repository) to
/output/entry.png. Deterministic: a byte-for-byte copy, no network,
no randomness, no timestamps, no environment dependence.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote {} ({} bytes)".format(DST, DST.stat().st_size))


if __name__ == "__main__":
    main()
