"""Time machine warning label, printed and verified."""
import os
from pathlib import Path

WARNING = ("WARNING: Arriving before you left voids the warranty, the "
           "timeline, and your mother's memory of your birth.")
LABEL = "tmw2"
CHRONO = "do-not-drink"
FLUX = "capacitor-ok"

base = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
base.mkdir(parents=True, exist_ok=True)
p = base / "entry.txt"
p.write_bytes(WARNING.encode("utf-8") + b"\n")
blob = p.read_bytes()
if blob.decode("utf-8").strip() != WARNING:
    raise SystemExit("timeline altered during write")
print(LABEL, CHRONO, len(blob) - 1, "bytes stamped")
print("flux:", FLUX, "paradox deferred")
