#!/usr/bin/env python3
"""VINDEX 0.53: iterationem secundam migrationis localium applicat."""

from pathlib import Path
import re
import subprocess

RADIX = Path("Vindex Chat-GPT/vindex_final_v51")
SCRIPTUM = RADIX / "instrumenta/applica_locos_dynamicos_053.py"
FONS = RADIX / "src/compilator_vindex.vindex"

subprocess.run(["python3", str(SCRIPTUM)], check=True)
textus = FONS.read_text(encoding="utf-8")

# `CAPACITAS` verbum linguae reservatum est; amorsa Python idem nomen
# minusculum quoque signo CAPACITAS interpretatur. Nomen locale mutatur.
textus, numerus = re.subn(r"\bcapacitas\b", "limen_locorum", textus)
if numerus != 7:
    raise SystemExit(f"ERRATUM: nomen reservatum capacitas {numerus} vicibus mutatum est")

if re.search(r"DECLARA\s+capacitas\s+SICUT", textus):
    raise SystemExit("ERRATUM: nomen reservatum capacitas adhuc declaratur")

FONS.write_text(textus, encoding="utf-8")
print(f"RECTE: iteratio II localium applicata est; mutationes nominis reservati={numerus}.")
