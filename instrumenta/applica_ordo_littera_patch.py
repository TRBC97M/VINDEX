#!/usr/bin/env python3
from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")

fons = VIA.read_text(encoding="utf-8")
mutatum = False

# Compilator ipse unum ordinem localem identificatoris ad SIGNUM_VERBI tradit.
# Postquam ORDO DE LITTERA byte-addressatus fit, parametrum quoque contractum
# byte-addressatum ACUS<LITTERA> sequi debet; aliter hash identificatorum
# stride VIII veterem retineret et functiones non inveniret.
vetus_signum = "    ACCIPIT verbum SICUT ORDO DE LITTERA.\n"
novum_signum = "    ACCIPIT verbum SICUT ACUS<LITTERA>.\n"
if vetus_signum in fons:
    if fons.count(vetus_signum) != 1:
        raise SystemExit("ERRATUM: SIGNUM_VERBI ORDO signature non unica est")
    fons = fons.replace(vetus_signum, novum_signum, 1)
    mutatum = True
elif novum_signum not in fons:
    raise SystemExit("ERRATUM: SIGNUM_VERBI signature neque vetus neque nova inventa est")

MARCA = "// P9 — ORDO DE LITTERA elementa unius octeti sunt."
if MARCA not in fons:
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
                            // Tantum elementa quorum magnitudo a via historica VIII differt
                            // metadata explicitam accipiunt. ORDO DE NUMERUS et FLUITANS
                            // semitam canonicam veterem servant.
                            SI es_arr_littera == 1 TUNC
                                LOCALE_SCRIBE(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), idx_nova, 3, 1).
                            FIN-SI.
                            SI es_arr_fluitans == 1 TUNC
                                LOCALE_SCRIBE(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), idx_nova, 5, 1).
                            FIN-SI.
                            SI numerus_campi_ordo > 0 TUNC
                                LOCALE_SCRIBE(DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris), idx_nova, 3, magnitudo_elem_ordo).
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
    mutatum = True

if mutatum:
    VIA.write_text(fons, encoding="utf-8")
    print("RECTE: ORDO DE LITTERA et SIGNUM_VERBI ad contractum byte-addressatum migrata sunt.")
else:
    print("RECTE: correctio ORDO DE LITTERA iam adest.")
