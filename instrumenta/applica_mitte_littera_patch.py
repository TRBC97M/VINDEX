#!/usr/bin/env python3
from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
fons = VIA.read_text(encoding="utf-8")

MARCA = "// P9 — MITTE magnitudinem elementi ordinis observat."
if MARCA in fons:
    print("RECTE: correctio MITTE/LITTERA iam adest.")
    raise SystemExit(0)

vetus_declaratio = '''        DECLARA nomen_tab_mitte SICUT NUMERUS VALENS EXTRAHE_ET_SIGNA(fons, pos_fontis, n).
        DECLARA intervallum_tab_mitte SICUT NUMERUS VALENS CERCA_VARIABILEM(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), nomen_tab_mitte).
        ig_mi = IGNORA_SPATIA(fons, pos_fontis, n).
'''

nova_declaratio = '''        DECLARA nomen_tab_mitte SICUT NUMERUS VALENS EXTRAHE_ET_SIGNA(fons, pos_fontis, n).
        DECLARA intervallum_tab_mitte SICUT NUMERUS VALENS CERCA_VARIABILEM(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), nomen_tab_mitte).
        // P9 — MITTE magnitudinem elementi ordinis observat.
        // Metadata 0 est via historica scalarum ordinariorum: stride VIII.
        DECLARA magnitudo_tab_mitte SICUT NUMERUS VALENS MAGNITUDO_VARIABILIS(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), nomen_tab_mitte).
        SI magnitudo_tab_mitte <= 0 TUNC
            magnitudo_tab_mitte = 8.
        FIN-SI.
        ig_mi = IGNORA_SPATIA(fons, pos_fontis, n).
'''

vetus_ansa = '''        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 0, 1).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 3, 8).
        CONTENTUM(pos_codicis) = COMPONE_MULTIPLICA(codex, CONTENTUM(pos_codicis), 0, 3).
        CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 3, intervallum_tab_mitte).
        CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 3, 0).
        CONTENTUM(pos_codicis) = COMPONE_SUME_INDIRECTUM(codex, CONTENTUM(pos_codicis), 0, 3).

        CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).
'''

nova_ansa = '''        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 0, 1).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 3, magnitudo_tab_mitte).
        CONTENTUM(pos_codicis) = COMPONE_MULTIPLICA(codex, CONTENTUM(pos_codicis), 0, 3).
        CONTENTUM(pos_codicis) = COMPONE_LEA_PILA(codex, CONTENTUM(pos_codicis), 3, intervallum_tab_mitte).
        CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 3, 0).
        SI magnitudo_tab_mitte == 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_MOVZX(codex, CONTENTUM(pos_codicis), 0, 3).
        ALITER
            CONTENTUM(pos_codicis) = COMPONE_SUME_INDIRECTUM(codex, CONTENTUM(pos_codicis), 0, 3).
        FIN-SI.

        CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).
'''

for nomen, vetus, novum in (
    ("declaratio MITTE", vetus_declaratio, nova_declaratio),
    ("ansa MITTE", vetus_ansa, nova_ansa),
):
    numerus = fons.count(vetus)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen!r} inventa {numerus} vice/ibus, exspectata 1")
    fons = fons.replace(vetus, novum, 1)

VIA.write_text(fons, encoding="utf-8")
print("RECTE: MITTE stride metadatae ordinis sequitur.")
