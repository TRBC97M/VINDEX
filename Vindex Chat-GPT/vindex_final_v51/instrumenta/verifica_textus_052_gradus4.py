#!/usr/bin/env python3
"""Gradum IV TEXTUS statice examinat ante auto-hospitium."""

from pathlib import Path
import re

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
LIMES_FONTIS = 212999
LIMES_LOCALIUM = 100
LIMES_ADIUTORUM = 150


def functiones(textus: str) -> list[str]:
    return re.findall(r"^FUNCTIO\s+([A-Z0-9_]+)\s+REDDENS", textus, re.MULTILINE)


def corpus(textus: str, nomen: str) -> str:
    initium = textus.find(f"FUNCTIO {nomen} REDDENS")
    if initium < 0:
        raise SystemExit(f"ERRATUM: functio {nomen} non inventa est")
    finis = textus.find("FIN-FUNCTIO.", initium)
    if finis < 0:
        raise SystemExit(f"ERRATUM: finis functionis {nomen} non inventus est")
    return textus[initium:finis]


def loca(corpus_functionis: str) -> int:
    return corpus_functionis.count("ACCIPIT ") + corpus_functionis.count("DECLARA ")


textus = VIA.read_text(encoding="utf-8")

necessaria = (
    "FUNCTIO COMPONE_CONCATENA_TEXTUS REDDENS NUMERUS.",
    "FUNCTIO COMPONE_COMPARA_TEXTUS REDDENS NUMERUS.",
    "REDDE COMPONE_LITTERALE_TEXTUS(codex, pos_codicis, fons, pos_fontis, n).",
    "SI pos < n && fons[pos] == 34 TUNC\n        REDDE 2.",
    "COMPONE_CONCATENA_TEXTUS(codex, CONTENTUM(pos_codicis))",
    "COMPONE_COMPARA_TEXTUS(codex, CONTENTUM(pos_codicis))",
)
for fragmentum in necessaria:
    if fragmentum not in textus:
        raise SystemExit(f"ERRATUM: fragmentum gradus IV deest: {fragmentum}")

corpus_expr = corpus(textus, "ANALYSA_EXPRESSIO")
if "SI es_flot_expr == 2 && operatio == 43 TUNC" not in corpus_expr:
    raise SystemExit("ERRATUM: operator + TEXTUS non agnoscitur")

corpus_cmp = corpus(textus, "ANALYSA_COMPARATIO")
if "SI es_flot_cmp == 2 TUNC" not in corpus_cmp:
    raise SystemExit("ERRATUM: comparatio TEXTUS non agnoscitur")
if corpus_cmp.count("es_flot_cmp != 1 TUNC") != 4:
    raise SystemExit("ERRATUM: custodiae ordinis TEXTUS non sunt quattuor")

# COMPONE_SERVA_OCTETUM sine REX tantum registris inferioribus hic utitur.
corpus_concat = corpus(textus, "COMPONE_CONCATENA_TEXTUS")
if "COMPONE_SERVA_OCTETUM(codex, p, 3, 0)" not in corpus_concat:
    raise SystemExit("ERRATUM: scriptio octeti concatenationis registris tutis non utitur")
if "COMPONE_SERVA_OCTETUM(codex, p, 8" in corpus_concat or "COMPONE_SERVA_OCTETUM(codex, p, 9" in corpus_concat:
    raise SystemExit("ERRATUM: registrum altum in scriptore octeti adhibetur")

max_nomen = ""
max_loca = 0
nomina = functiones(textus)
for nomen in nomina:
    numerus = loca(corpus(textus, nomen))
    if numerus > max_loca:
        max_loca = numerus
        max_nomen = nomen
    if numerus > LIMES_LOCALIUM:
        raise SystemExit(f"ERRATUM: functio {nomen} {numerus} loca postulat; limes est {LIMES_LOCALIUM}")

adiutores = len([nomen for nomen in nomina if nomen != "PRINCIPALIS"])
if adiutores > LIMES_ADIUTORUM:
    raise SystemExit(f"ERRATUM: functiones auxiliares {adiutores}/{LIMES_ADIUTORUM}")

mensura = len(textus.encode("utf-8"))
if mensura > LIMES_FONTIS:
    raise SystemExit(f"ERRATUM: fons {mensura}/{LIMES_FONTIS} octeta excedit")

print(f"RECTE: gradus IV TEXTUS statice congruit; maxima functio {max_nomen} {max_loca} loca habet.")
print(f"RECTE: functiones auxiliares {adiutores}/{LIMES_ADIUTORUM}; fons {mensura}/{LIMES_FONTIS} octeta.")
