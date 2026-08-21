#!/usr/bin/env python3
"""Spatium temporarium MITTE in regione tutiore pilae collocat."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
VETUS = "0 - 6000000"
NOVUM = "0 - 6900000"

textus = VIA.read_text(encoding="utf-8")
numerus = textus.count(VETUS)
if numerus == 0 and textus.count(NOVUM) == 2:
    print("MITTE iam correctum est.")
    raise SystemExit(0)
if numerus != 2:
    raise SystemExit(f"ERRATUM: loci MITTE exspectati II sunt, inventi {numerus}")

VIA.write_text(textus.replace(VETUS, NOVUM), encoding="utf-8")
print("RECTE: spatium temporarium MITTE ad -6900000 translatum est.")
