#!/usr/bin/env python3
"""ANALYSA_FACTOR gradatim mutat ut limes eius exacte reperiatur."""

from pathlib import Path
import os

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
VARIANS = int(os.environ.get("VINDEX_LONGITUDO_VARIANS", "4"))
textus = VIA.read_text(encoding="utf-8")

textus = textus.replace(
    "// Capacitas tabulae tota: 850.\n",
    "//   2900-2999: signa TEXTUS variabilium (100 loca)\n// Capacitas tabulae tota: 3000.\n",
    1,
)
ancora = "    DECLARA ignoratum SICUT NUMERUS VALENS IGNORA_SPATIA(fons, pos_fontis, n).\n\n"
initium = textus.find("FUNCTIO ANALYSA_FACTOR REDDENS NUMERUS.")
locus = textus.find(ancora, initium)
if initium < 0 or locus < 0:
    raise SystemExit("ERRATUM: ANALYSA_FACTOR non inventa est")
locus += len(ancora)

condicio_brevis = "    SI fons[CONTENTUM(pos_fontis)] == 76 TUNC\n"
condicio_plena = "    SI fons[CONTENTUM(pos_fontis)] == 76 && CONTENTUM(pos_fontis) + 8 < n && fons[CONTENTUM(pos_fontis)+1] == 79 && fons[CONTENTUM(pos_fontis)+2] == 78 && fons[CONTENTUM(pos_fontis)+3] == 71 && fons[CONTENTUM(pos_fontis)+4] == 73 && fons[CONTENTUM(pos_fontis)+5] == 84 && fons[CONTENTUM(pos_fontis)+6] == 85 && fons[CONTENTUM(pos_fontis)+7] == 68 && fons[CONTENTUM(pos_fontis)+8] == 79 TUNC\n"

if VARIANS == 1:
    condicio = condicio_brevis
    corpus = "        REDDE 0.\n"
elif VARIANS == 2:
    condicio = condicio_plena
    corpus = "        REDDE 0.\n"
elif VARIANS == 3:
    condicio = condicio_brevis
    corpus = '''        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 9.\n        DECLARA ign_longitudo SICUT NUMERUS VALENS IGNORA_SPATIA(fons, pos_fontis, n).\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        ign_longitudo = ANALYSA_FACTOR(codex, pos_codicis, fons, pos_fontis, n, tabula).\n        ign_longitudo = IGNORA_SPATIA(fons, pos_fontis, n).\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        CONTENTUM(pos_codicis) = COMPONE_SUME_INDIRECTUM(codex, CONTENTUM(pos_codicis), 0, 0).\n        REDDE 0.\n'''
elif VARIANS == 4:
    condicio = condicio_brevis
    corpus = '''        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 9.\n        DECLARA ign_longitudo SICUT NUMERUS VALENS IGNORA_SPATIA(fons, pos_fontis, n).\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        ign_longitudo = ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, tabula).\n        ign_longitudo = IGNORA_SPATIA(fons, pos_fontis, n).\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        CONTENTUM(pos_codicis) = COMPONE_SUME_INDIRECTUM(codex, CONTENTUM(pos_codicis), 0, 0).\n        REDDE 0.\n'''
else:
    raise SystemExit("ERRATUM: varians inter I et IV esse debet")

additio = "    // Probatio limitis ANALYSA_FACTOR, varians " + str(VARIANS) + ".\n" + condicio + corpus + "    FIN-SI.\n\n"
textus = textus[:locus] + additio + textus[locus:]
VIA.write_text(textus, encoding="utf-8")
print(f"RECTE: varians {VARIANS} inserta est; magnitudo fontis {len(textus.encode('utf-8'))}.")
