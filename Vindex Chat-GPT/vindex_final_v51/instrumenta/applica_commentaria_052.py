#!/usr/bin/env python3
"""Commentaria // ut spatia tractanda IGNORA_SPATIA addit."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "DECLARA iterum_ignora SICUT NUMERUS VALENS 1."

textus = VIA.read_text(encoding="utf-8")
if MARCA in textus:
    print("Commentaria iam tractantur.")
    raise SystemExit(0)

vetus = '''FUNCTIO IGNORA_SPATIA REDDENS NUMERUS.\n    ACCIPIT fons SICUT ORDO DE LITTERA.\n    ACCIPIT pos SICUT ACUS<NUMERUS>.\n    ACCIPIT n SICUT NUMERUS.\n    DUM CONTENTUM(pos) < n && (fons[CONTENTUM(pos)] == 32 || fons[CONTENTUM(pos)] == 10 || fons[CONTENTUM(pos)] == 9) PERFICE\n        CONTENTUM(pos) = CONTENTUM(pos) + 1.\n    FIN-DUM.\n    REDDE 0.\nFIN-FUNCTIO.\n'''

novum = '''FUNCTIO IGNORA_SPATIA REDDENS NUMERUS.\n    ACCIPIT fons SICUT ORDO DE LITTERA.\n    ACCIPIT pos SICUT ACUS<NUMERUS>.\n    ACCIPIT n SICUT NUMERUS.\n    DECLARA iterum_ignora SICUT NUMERUS VALENS 1.\n    DUM iterum_ignora == 1 PERFICE\n        iterum_ignora = 0.\n        DUM CONTENTUM(pos) < n && (fons[CONTENTUM(pos)] == 32 || fons[CONTENTUM(pos)] == 10 || fons[CONTENTUM(pos)] == 9) PERFICE\n            CONTENTUM(pos) = CONTENTUM(pos) + 1.\n        FIN-DUM.\n        SI CONTENTUM(pos) + 1 < n && fons[CONTENTUM(pos)] == 47 && fons[CONTENTUM(pos) + 1] == 47 TUNC\n            DUM CONTENTUM(pos) < n && fons[CONTENTUM(pos)] != 10 PERFICE\n                CONTENTUM(pos) = CONTENTUM(pos) + 1.\n            FIN-DUM.\n            iterum_ignora = 1.\n        FIN-SI.\n    FIN-DUM.\n    REDDE 0.\nFIN-FUNCTIO.\n'''

if textus.count(vetus) != 1:
    raise SystemExit("ERRATUM: IGNORA_SPATIA forma pristina non unica est")

VIA.write_text(textus.replace(vetus, novum, 1), encoding="utf-8")
print("RECTE: commentaria linearia sicut spatia tractantur.")
