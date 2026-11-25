# Time machine warning label: one-line exporter (round 4).
import json
import os
import pathlib

TOP = 120
LABEL_CD = "tmw4-warning-r4"


def read_line():
    src = pathlib.Path(__file__).resolve().parent / "entry.txt"
    with src.open(encoding="utf-8") as fh:
        return fh.read().strip()


def legal(n):
    return 0 < n <= TOP


def stash(text):
    out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_bytes((text + "\n").encode("utf-8"))


def flow():
    text = read_line()
    n = len(text)
    if legal(n):
        stash(text)
    print(json.dumps({"code": LABEL_CD, "n": n, "legal": legal(n), "top": TOP, "era": "locked"}))


flow()
