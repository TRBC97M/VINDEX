#!/usr/bin/env python3
from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")

fons = VIA.read_text(encoding="utf-8")

MARCA = "// P9 — ORDO DE LITTERA elementa unius octeti sunt."
if MARCA in fons:
    print("RECTE: correctio ORDO DE LITTERA iam adest.")
    raise SystemExit(0)

vetus_typus = '''                            DECLARA es_arr_fluitans SICUT NUMERUS VALENS 0.
                            SI fons[CONTENTUM(pos_fontis)] == 70 && CONTENTUM(pos_fontis) + 7 < n && fons[CONTENTUM(pos_fontis)+1] == 76 && fons[CONTENTUM(pos_fontis)+2] == 85 && fons[CONTENTUM(pos_fontis)+3] == 73 && fons[CONTENTUM(pos_fontis)+4] == 84 && fons[CONTENTUM(pos_fontis)+5] == 65 && fons[CONTENTUM(pos_fontis)+6] == 78 && fons[CONTENTUM(pos_fontis)+7] == 83 TUNC
                                es_arr_fluitans = 1.
                            FIN-SI.
                            DECLARA nomen_typus_ordo SICUT NUMERUS VALENS EXTRAHE_ET_SIGNA(fons, pos_fontis, n).
'''

novus_typus = '''                            DECLARA es_arr_fluitans SICUT NUMERUS VALENS 0.
                            DECLARA es_arr_littera SICUT NUMERUS VALENS 0.
                            SI fons[CONTENTUM(pos_fontis)] == 70 && CONTENTUM(pos_fontis) + 7 < n && fons[CONTENTUM(pos_fontis)+1] == 76 && fons[CONTENTUM(pos_fontis)+2] == 85 && fons[CONTENTUM(pos_fontis)+3] == 73 && fons[CONTENTUM(pos_fontis)+4] == 84 && fons[CONTENTUM(pos_fontis)+5] == 65 && fons[CONTENTUM(pos_fontis)+6] == 78 && fons[CONTENTUM(pos_fontis)+7] == 83 TUNC
                                es_arr_fluitans = 1.
                            FIN-SI.
                            // P9 — ORDO DE LITTERA elementa unius octeti sunt.
                            SI fons[CONTENTUM(pos_fontis)] == 76 && CONTENTUM(pos_fontis) + 6 < n && fons[CONTENTUM(pos_fontis)+1] == 73 && fons[CONTENTUM(pos_fontis)+2] == 84 && fons[CONTENTUM(pos_fontis)+3] == 84 && fons[CONTENTUM(pos_fontis)+4] == 69 && fons[CONTENTUM(pos_fontis)+5] == 82 && fons[CONTENTUM(pos_fontis)+6] == 65 TUNC
                                es_arr_littera = 1.
                            FIN-SI.
                            DECLARA nomen_typus_ordo SICUT NUMERUS VALENS EXTRAHE_ET_SIGNA(fons, pos_fontis, n).
'''

vetus_magnitudo = '''                            DECLARA numerus_campi_ordo SICUT NUMERUS VALENS NUMERUS_CAMPORUM_FORMAE(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), nomen_typus_ordo).
                            DECLARA magnitudo_elem_ordo SICUT NUMERUS VALENS 8.
                            SI numerus_campi_ordo > 0 TUNC
                                magnitudo_elem_ordo = numerus_campi_ordo * 8.
                            FIN-SI.
'''

novus_magnitudo = '''                            DECLARA numerus_campi_ordo SICUT NUMERUS VALENS NUMERUS_CAMPORUM_FORMAE(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), nomen_typus_ordo).
                            DECLARA magnitudo_elem_ordo SICUT NUMERUS VALENS 8.
                            SI es_arr_littera == 1 TUNC
                                magnitudo_elem_ordo = 1.
                            FIN-SI.
                            SI numerus_campi_ordo > 0 TUNC
                                magnitudo_elem_ordo = numerus_campi_ordo * 8.
                            FIN-SI.
'''

vetus_meta = '''                            LOCALE_SCRIBE(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), idx_nova, 1, intervallum_base).
                            LOCALE_SCRIBE(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), idx_nova, 2, 1).
                            SI es_arr_fluitans == 1 TUNC
                                LOCALE_SCRIBE(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), idx_nova, 5, 1).
                            FIN-SI.
                            SI numerus_campi_ordo > 0 TUNC
                                LOCALE_SCRIBE(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), idx_nova, 3, magnitudo_elem_ordo).
                                DECLARA idx_struct_ordo SICUT NUMERUS VALENS INDEX_STRUCTURAE(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), nomen_typus_ordo).
'''

novus_meta = '''                            LOCALE_SCRIBE(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), idx_nova, 1, intervallum_base).
                            LOCALE_SCRIBE(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), idx_nova, 2, 1).
                            // Magnitudo elementi omnium ordinum explicite servatur:
                            // LITTERA=1; scalaria ordinaria=8; FORMA=magnitudo formae.
                            LOCALE_SCRIBE(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), idx_nova, 3, magnitudo_elem_ordo).
                            SI es_arr_fluitans == 1 TUNC
                                LOCALE_SCRIBE(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), idx_nova, 5, 1).
                            FIN-SI.
                            SI numerus_campi_ordo > 0 TUNC
                                DECLARA idx_struct_ordo SICUT NUMERUS VALENS INDEX_STRUCTURAE(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), nomen_typus_ordo).
'''

for nomen, vetus, novus in (
    ("detectio typi", vetus_typus, novus_typus),
    ("magnitudo elementi", vetus_magnitudo, novus_magnitudo),
    ("metadata elementi", vetus_meta, novus_meta),
):
    numerus = fons.count(vetus)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen!r} inventa {numerus} vice/ibus, exspectata 1")
    fons = fons.replace(vetus, novus, 1)

VIA.write_text(fons, encoding="utf-8")
print("RECTE: ORDO DE LITTERA ad elementa contigua unius octeti correctus est.")
