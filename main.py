"""tmw-1125: sticks the warning label into the output slot; gate is 120 chars."""

import json
import os

EDGE = 120


def peel(folder=("./",)) -> str:
    base = os.path.dirname(os.path.abspath(__file__))
    return open(os.path.join(base, "entry.txt"), encoding="utf-8").read().strip()


def gum(text: str) -> int:
    if len(text) > EDGE:
        raise SystemExit("label too wide for the machine: %d chars" % len(text))
    if not text:
        raise SystemExit("label is blank")
    return len(text)


def stick(text: str):
    spots = [os.environ.get("MAKEFUN_OUTPUT_DIR"), os.path.dirname(os.path.abspath(__file__))]
    for spot in spots:
        if spot:
            os.makedirs(spot, exist_ok=True)
            with open(os.path.join(spot, "entry.txt"), "w", encoding="utf-8", newline="\n") as press:
                press.write(text + "\n")
            return spot
    raise SystemExit("nowhere to stick the label")


label = peel()
width = gum(label)
print(json.dumps({"sticker": label[:40], "width": width, "flux": "capacitor nominal", "stuck_to": stick(label)}))
