import json
import os

PLATE = "tmw3-do-not-touch"
EDGE = 120


class Runner:
    """Reads the warning plate draft and files it with the grader."""

    def __init__(self, root):
        self.root = root
        self.box = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"

    def fetch(self):
        with open(os.path.join(self.root, "entry.txt"), "rb") as reader:
            return reader.read().decode("utf-8")

    @staticmethod
    def engrave(raw):
        for candidate in raw.replace("\r", "").split("\n"):
            if candidate.strip():
                return candidate
        return ""

    def file(self, plate):
        if not os.path.isdir(self.box):
            os.makedirs(self.box)
        dest = os.path.join(self.box, "entry.txt")
        with open(dest, "w", encoding="utf-8", newline="") as writer:
            writer.write(plate)
        with open(dest, "rb") as checker:
            if checker.read() != plate.encode("utf-8"):
                raise IOError("plate smudged in transit")
        return dest


run = Runner(os.path.dirname(os.path.abspath(__file__)))
try:
    plate = run.engrave(run.fetch())
except UnicodeDecodeError:
    plate = ""
if not plate.strip():
    print(json.dumps({"verdict": "reject", "why": "no plate text"}))
    raise SystemExit(1)
if len(plate) > EDGE:
    print(json.dumps({"verdict": "reject", "why": "plate over edge"}))
    raise SystemExit(1)
filed = run.file(plate)
print(json.dumps({"verdict": "accept", "edge": len(plate), "plate": PLATE, "filed": filed}))
