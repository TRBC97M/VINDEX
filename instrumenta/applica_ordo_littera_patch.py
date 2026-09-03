#!/usr/bin/env python3
from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
fons = VIA.read_text(encoding="utf-8")
mutatum = False


def substitue_unum(vetus: str, novum: str, nomen: str) -> None:
    global fons, mutatum
    if novum in fons:
        return
    numerus = fons.count(vetus)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen!r} inventa {numerus} vice/ibus, exspectata 1")
    fons = fons.replace(vetus, novum, 1)
    mutatum = True


# Bootstrap internus: antequam semantica publica mutetur, compilator ipse
# buffers LITTERA suos per octeta cruda tractat. Ita compilator vetus et novus
# eundem fontem sine conflictu stride VIII/stride I compilare possunt.
substitue_unum(
    "    ACCIPIT verbum SICUT ORDO DE LITTERA.\n",
    "    ACCIPIT verbum SICUT ACUS<LITTERA>.\n",
    "SIGNUM_VERBI signature",
)
substitue_unum(
    "        signum = signum * 31 + verbum[idx].\n",
    "        signum = signum * 31 + OCTETUS_AB(verbum + idx).\n",
    "SIGNUM_VERBI lectio",
)
substitue_unum(
    "        verbum[mensura] = fons[CONTENTUM(pos)].\n",
    "        SCRIBE_OCTETUM_AB(verbum + mensura, fons[CONTENTUM(pos)]).\n",
    "EXTRAHE_ET_SIGNA scriptio",
)
substitue_unum(
    "            buffer[mensura] = OCTETUS_AB(textus + positio + mensura).\n",
    "            SCRIBE_OCTETUM_AB(buffer + mensura, OCTETUS_AB(textus + positio + mensura)).\n",
    "buffer diagnostici scriptio",
)

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
                            // P9: layout pilae interim eundem spatium historicum servat,
                            // sed accessus LITTERA stride unius octeti accipit.
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
        ("detectio typi LITTERA", vetus_typus, novus_typus),
        ("metadata elementi LITTERA", vetus_meta, novus_meta),
    ):
        numerus = fons.count(vetus)
        if numerus != 1:
            raise SystemExit(f"ERRATUM: ancora {nomen!r} inventa {numerus} vice/ibus, exspectata 1")
        fons = fons.replace(vetus, novus, 1)
        mutatum = True

if mutatum:
    VIA.write_text(fons, encoding="utf-8")
    print("RECTE: bootstrap internus et accessus ORDO DE LITTERA byte-addressati sunt.")
else:
    print("RECTE: correctio ORDO DE LITTERA iam adest.")
