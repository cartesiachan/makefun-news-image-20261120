"""Entry for make.fun bounty news-image-20261120.

Sum up 20 November 2026 world news in one image.

Writes the pre-built 1024x1024 image (entry.png, in this repository) to
/output/entry.png. Deterministic: a byte-for-byte copy, no network,
no randomness, no timestamps, no environment dependence.
"""

import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not SRC.is_file():
        raise SystemExit("error: entry image not found: {}".format(SRC))
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    src_size = SRC.stat().st_size
    dst_size = DST.stat().st_size
    if dst_size != src_size or _sha256(DST) != _sha256(SRC):
        raise SystemExit(
            "error: copied image does not match source: {} != {}".format(DST, SRC)
        )
    print("wrote {} ({} bytes, verified)".format(DST, dst_size))


if __name__ == "__main__":
    main()
