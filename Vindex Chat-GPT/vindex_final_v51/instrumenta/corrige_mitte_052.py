#!/usr/bin/env python3
"""Spatium temporarium MITTE in regione tutiore pilae collocat."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
textus = VIA.read_text(encoding="utf-8")

VETUS_I = '''        CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 3, intervallum_tab_mitte).
        CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 3, 0).
        CONTENTUM(pos_codicis) = COMPONE_SUME_INDIRECTUM(codex, CONTENTUM(pos_codicis), 0, 3).

        CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).
        CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 3, 0 - 6000000).
'''
NOVUM_I = VETUS_I.replace("0 - 6000000", "0 - 6900000")

VETUS_II = '''        DECLARA pos_post_mitte SICUT NUMERUS VALENS CONTENTUM(pos_codicis).
        ig_mi = CORRIGE_SALTUM(codex, loci_je_mitte, pos_post_mitte).

        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 2, 6).
        CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 6, 0 - 6000000).
'''
NOVUM_II = VETUS_II.replace("0 - 6000000", "0 - 6900000")

if NOVUM_I in textus and NOVUM_II in textus:
    print("MITTE iam correctum est.")
    raise SystemExit(0)

if textus.count(VETUS_I) != 1:
    raise SystemExit(f"ERRATUM: primus locus MITTE {textus.count(VETUS_I)} vicibus inventus est")
if textus.count(VETUS_II) != 1:
    raise SystemExit(f"ERRATUM: secundus locus MITTE {textus.count(VETUS_II)} vicibus inventus est")

textus = textus.replace(VETUS_I, NOVUM_I, 1)
textus = textus.replace(VETUS_II, NOVUM_II, 1)
VIA.write_text(textus, encoding="utf-8")
print("RECTE: duo spatia temporaria MITTE ad -6900000 translata sunt.")
