#!/usr/bin/env python3
"""VINDEX 0.53: diagnostica precisa vocationum pendentium migrationi addit."""

from pathlib import Path
import subprocess

RADIX = Path("Vindex Chat-GPT/vindex_final_v51")
BASE = RADIX / "instrumenta/applica_functiones_dynamicas_053.py"
FONS = RADIX / "src/compilator_vindex.vindex"

subprocess.run(["python3", str(BASE)], check=True)
textus = FONS.read_text(encoding="utf-8")

vetus = '''        SI loci_cible == 0 TUNC
            PROCLAMA "ERRATUM: functio vocata non inventa est".
            REDDE 65.
        FIN-SI.'''
novum = '''        SI loci_cible == 0 TUNC
            PROCLAMA "ERRATUM: functio vocata non inventa est".
            PROCLAMA k_pendens.
            PROCLAMA nomen_p.
            PROCLAMA tabula[2985].
            REDDE 65.
        FIN-SI.'''

numerus = textus.count(vetus)
if numerus != 1:
    raise SystemExit(f"ERRATUM: diagnostica pendentium {numerus} vicibus inventa est")
textus = textus.replace(vetus, novum, 1)
FONS.write_text(textus, encoding="utf-8")
print("RECTE: index, signum et quantitas vocationis pendentis in errore monstrabuntur.")
