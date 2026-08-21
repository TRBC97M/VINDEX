#!/usr/bin/env python3
"""Solam partem LONGITUDO in fonte compilatoris ad diagnosticam inserit."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
textus = VIA.read_text(encoding="utf-8")


def numerus_localium(fons: str) -> int:
    initium = fons.find("FUNCTIO ANALYSA_FACTOR REDDENS NUMERUS.")
    finis = fons.find("FIN-FUNCTIO.", initium)
    if initium < 0 or finis < 0:
        raise SystemExit("ERRATUM: ANALYSA_FACTOR non inventa est")
    return fons[initium:finis].count("DECLARA ")


print(f"Localia ANALYSA_FACTOR ante mutationem: {numerus_localium(textus)}")
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
additio = '''    // TEXTUS 0.52: LONGITUDO structuram CONTENTUM iam probatam imitatur.\n    SI fons[CONTENTUM(pos_fontis)] == 76 && CONTENTUM(pos_fontis) + 8 < n && fons[CONTENTUM(pos_fontis)+1] == 79 && fons[CONTENTUM(pos_fontis)+2] == 78 && fons[CONTENTUM(pos_fontis)+3] == 71 && fons[CONTENTUM(pos_fontis)+4] == 73 && fons[CONTENTUM(pos_fontis)+5] == 84 && fons[CONTENTUM(pos_fontis)+6] == 85 && fons[CONTENTUM(pos_fontis)+7] == 68 && fons[CONTENTUM(pos_fontis)+8] == 79 TUNC\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 9.\n        DECLARA ign_longitudo SICUT NUMERUS VALENS IGNORA_SPATIA(fons, pos_fontis, n).\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        ign_longitudo = ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, tabula).\n        ign_longitudo = IGNORA_SPATIA(fons, pos_fontis, n).\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        CONTENTUM(pos_codicis) = COMPONE_SUME_INDIRECTUM(codex, CONTENTUM(pos_codicis), 0, 0).\n        REDDE 0.\n    FIN-SI.\n\n'''
textus = textus[:locus] + additio + textus[locus:]
print(f"Localia ANALYSA_FACTOR post mutationem: {numerus_localium(textus)}")
VIA.write_text(textus, encoding="utf-8")
print("RECTE: LONGITUDO sola inserta est.")
