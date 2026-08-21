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

# Quaedam vocabula minuscula ab amorsa Python ut verba reservata agnoscuntur.
# Nomina auxiliatorum localium igitur distincta fiunt ante probationem amorse.
textus, n_cap = re.subn(r"\bcapacitas\b", "limen_locorum", textus)
if n_cap != 7:
    raise SystemExit(f"ERRATUM: nomen reservatum capacitas {n_cap} vicibus mutatum est")

vetus_numerus = "DECLARA numerus SICUT NUMERUS VALENS tabula[2972]."
novus_numerus = "DECLARA numerus_locorum SICUT NUMERUS VALENS tabula[2972]."
if textus.count(vetus_numerus) != 1:
    raise SystemExit("ERRATUM: declaratio numerus localium non unica est")
textus = textus.replace(vetus_numerus, novus_numerus, 1)
textus = textus.replace("numerus * 48", "numerus_locorum * 48", 1)

textus, n_campus = re.subn(r"\bcampus\b", "campus_localis", textus)
if n_campus != 5:
    raise SystemExit(f"ERRATUM: nomen reservatum campus {n_campus} vicibus mutatum est")

if re.search(r"DECLARA\s+(capacitas|numerus)\s+SICUT|ACCIPIT\s+campus\s+SICUT", textus):
    raise SystemExit("ERRATUM: nomen reservatum in auxiliatoribus localium adhuc manet")

FONS.write_text(textus, encoding="utf-8")
print(
    "RECTE: iteratio II localium applicata est; "
    f"capacitas={n_cap}, campus={n_campus}, numerus=1."
)
