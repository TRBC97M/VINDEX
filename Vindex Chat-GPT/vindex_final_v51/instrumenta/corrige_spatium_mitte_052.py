#!/usr/bin/env python3
"""Spatium temporarium MITTE a variabilibus PRINCIPALIS removet.

Compilator 0.51 bufferum conversionis ad intervallum -6000000 collocabat.
Cum codex compilatoris crevit, bufferum ex illo loco usque ad variabilem
`pos` pervenit. Hic emendatio bufferum ad -6500000 movet sine novis
variabilibus localibus in ANALYSA_FACTOR.
"""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 3, 0 - 6500000)"

textus = VIA.read_text(encoding="utf-8")
if MARCA in textus:
    print("RECTE: spatium MITTE iam remotum est.")
    raise SystemExit(0)

initium = textus.find(
    "    SI fons[CONTENTUM(pos_fontis)] == 77 && CONTENTUM(pos_fontis) + 4 < n"
)
if initium < 0:
    raise SystemExit("ERRATUM: initium MITTE non inventum est")

finis = textus.find(
    "    SI (fons[CONTENTUM(pos_fontis)] >= 65 && fons[CONTENTUM(pos_fontis)] <= 90) TUNC",
    initium,
)
if finis < 0:
    raise SystemExit("ERRATUM: finis MITTE non inventus est")

ante = textus[:initium]
corpus = textus[initium:finis]
post = textus[finis:]

vetus = "0 - 6000000"
numerus = corpus.count(vetus)
if numerus != 2:
    raise SystemExit(f"ERRATUM: duo intervalla MITTE exspectata sunt, inventa {numerus}")

corpus = corpus.replace(vetus, "0 - 6500000")
VIA.write_text(ante + corpus + post, encoding="utf-8")
print("RECTE: bufferum MITTE ab -6000000 ad -6500000 motum est.")
