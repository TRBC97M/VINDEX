#!/usr/bin/env python3
"""Commentaria // extra chordas e fonte VINDEX ante analysim removet."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "DECLARA i_commentarium SICUT NUMERUS VALENS 0."

textus = VIA.read_text(encoding="utf-8")
if MARCA in textus:
    print("Commentaria iam tractantur.")
    raise SystemExit(0)

ancora = "    n = pos_out_imp.\n\n"
if textus.count(ancora) != 1:
    raise SystemExit("ERRATUM: locus purificationis commentariorum non unicus est")

additio = '''    DECLARA i_commentarium SICUT NUMERUS VALENS 0.\n    DECLARA o_commentarium SICUT NUMERUS VALENS 0.\n    DECLARA intra_chordam SICUT NUMERUS VALENS 0.\n    DUM i_commentarium < n PERFICE\n        SI fons[i_commentarium] == 34 TUNC\n            fons[o_commentarium] = fons[i_commentarium].\n            o_commentarium = o_commentarium + 1.\n            i_commentarium = i_commentarium + 1.\n            SI intra_chordam == 0 TUNC\n                intra_chordam = 1.\n            ALITER\n                intra_chordam = 0.\n            FIN-SI.\n        ALITER\n            SI intra_chordam == 0 && fons[i_commentarium] == 47 && i_commentarium + 1 < n && fons[i_commentarium + 1] == 47 TUNC\n                DUM i_commentarium < n && fons[i_commentarium] != 10 PERFICE\n                    i_commentarium = i_commentarium + 1.\n                FIN-DUM.\n            ALITER\n                fons[o_commentarium] = fons[i_commentarium].\n                o_commentarium = o_commentarium + 1.\n                i_commentarium = i_commentarium + 1.\n            FIN-SI.\n        FIN-SI.\n    FIN-DUM.\n    n = o_commentarium.\n\n'''

textus = textus.replace(ancora, ancora + additio, 1)
VIA.write_text(textus, encoding="utf-8")
print("RECTE: commentaria linearia ante analysim purgantur.")
