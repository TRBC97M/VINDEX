#!/usr/bin/env python3
"""ANALYSA_FACTOR gradatim mutat ut causa ruinae exacte reperiatur."""

from pathlib import Path
import os

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
VARIANS = int(os.environ.get("VINDEX_LONGITUDO_VARIANS", "4"))
textus = VIA.read_text(encoding="utf-8")

ancora = "    DECLARA ignoratum SICUT NUMERUS VALENS IGNORA_SPATIA(fons, pos_fontis, n).\n\n"
initium = textus.find("FUNCTIO ANALYSA_FACTOR REDDENS NUMERUS.")
locus = textus.find(ancora, initium)
if initium < 0 or locus < 0:
    raise SystemExit("ERRATUM: ANALYSA_FACTOR non inventa est")
locus += len(ancora)

si_minimum = '''    SI 0 == 1 TUNC\n        REDDE 0.\n    FIN-SI.\n\n'''
si_breve = '''    SI fons[CONTENTUM(pos_fontis)] == 76 TUNC\n        REDDE 0.\n    FIN-SI.\n\n'''
si_plenum = '''    SI fons[CONTENTUM(pos_fontis)] == 76 && CONTENTUM(pos_fontis) + 8 < n && fons[CONTENTUM(pos_fontis)+1] == 79 && fons[CONTENTUM(pos_fontis)+2] == 78 && fons[CONTENTUM(pos_fontis)+3] == 71 && fons[CONTENTUM(pos_fontis)+4] == 73 && fons[CONTENTUM(pos_fontis)+5] == 84 && fons[CONTENTUM(pos_fontis)+6] == 85 && fons[CONTENTUM(pos_fontis)+7] == 68 && fons[CONTENTUM(pos_fontis)+8] == 79 TUNC\n        REDDE 0.\n    FIN-SI.\n\n'''

if VARIANS == 1:
    additio = si_minimum
elif VARIANS == 2:
    additio = "    // COMMENTARIUM INTER FUNCTIONEM\n" + si_minimum
elif VARIANS == 3:
    additio = si_breve
elif VARIANS == 4:
    additio = si_plenum
else:
    raise SystemExit("ERRATUM: varians inter I et IV esse debet")

textus = textus[:locus] + additio + textus[locus:]
VIA.write_text(textus, encoding="utf-8")
print(f"RECTE: varians {VARIANS} inserta est; magnitudo fontis {len(textus.encode('utf-8'))}.")
