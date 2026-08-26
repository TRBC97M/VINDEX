#!/usr/bin/env python3
"""Operatores logicos && et || ad aestimationem brevem migrat."""
from pathlib import Path

RADIX = Path(__file__).resolve().parents[1]
COMPILATOR = RADIX / "src/compilator_vindex.vindex"

textus = COMPILATOR.read_text(encoding="utf-8")

si_iam = "FUNCTIO ANALYSA_CONIUNCTIO_LOGICA REDDENS NUMERUS."
if si_iam in textus:
    print("RECTE: logica brevis iam adest.")
    raise SystemExit(0)

initium = textus.index("FUNCTIO ANALYSA_COMPARATIO REDDENS NUMERUS.")
finis = textus.index("\nFUNCTIO INITIA_PARES_DYNAMICA REDDENS NUMERUS.", initium)
functio = textus[initium:finis]
functio = functio.replace(
    "FUNCTIO ANALYSA_COMPARATIO REDDENS NUMERUS.",
    "FUNCTIO ANALYSA_COMPARATIO_SIMPLEX REDDENS NUMERUS.",
    1,
)

# Cum nulla comparatio adest, valor expressionis simpliciter redditur.
initium_nulla = functio.index("    SI op_cmp == 0 TUNC\n")
finis_nulla = functio.index(
    "    ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).\n"
    "    CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 0).\n",
    initium_nulla,
)
functio = (
    functio[:initium_nulla]
    + "    SI op_cmp == 0 TUNC\n        REDDE 0.\n    FIN-SI.\n\n"
    + functio[finis_nulla:]
)

# Compositiones logicae veteres post comparationem tolluntur; novae functiones eas administrabunt.
post_cmp = functio.index("    DECLARA pos_fin_cmp SICUT NUMERUS VALENS CONTENTUM(pos_codicis).")
initium_vetus = functio.index(
    "    ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).\n"
    "    SI CONTENTUM(pos_fontis) + 1 < n && fons[CONTENTUM(pos_fontis)] == 38",
    post_cmp,
)
finis_vetus = functio.rindex("\n    REDDE 0.\nFIN-FUNCTIO.")
functio = functio[:initium_vetus] + functio[finis_vetus:]

novae = r'''

FUNCTIO EST_CONIUNCTIO_LOGICA REDDENS NUMERUS.
    ACCIPIT fons SICUT ACUS<LITTERA>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT n SICUT NUMERUS.
    SI pos + 1 >= n TUNC REDDE 0. FIN-SI.
    SI fons[pos] != 38 TUNC REDDE 0. FIN-SI.
    SI fons[pos + 1] != 38 TUNC REDDE 0. FIN-SI.
    REDDE 1.
FIN-FUNCTIO.

FUNCTIO EST_DISIUNCTIO_LOGICA REDDENS NUMERUS.
    ACCIPIT fons SICUT ACUS<LITTERA>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT n SICUT NUMERUS.
    SI pos + 1 >= n TUNC REDDE 0. FIN-SI.
    SI fons[pos] != 124 TUNC REDDE 0. FIN-SI.
    SI fons[pos + 1] != 124 TUNC REDDE 0. FIN-SI.
    REDDE 1.
FIN-FUNCTIO.

FUNCTIO ANALYSA_CONIUNCTIO_LOGICA REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos_codicis SICUT ACUS<NUMERUS>.
    ACCIPIT fons SICUT ACUS<LITTERA>.
    ACCIPIT pos_fontis SICUT ACUS<NUMERUS>.
    ACCIPIT n SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.

    DECLARA ignoratum SICUT NUMERUS VALENS ANALYSA_COMPARATIO_SIMPLEX(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
    ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).

    DUM EST_CONIUNCTIO_LOGICA(fons, CONTENTUM(pos_fontis), n) == 1 PERFICE
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 2.

        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 3, 0).
        CONTENTUM(pos_codicis) = COMPONE_CMP(codex, CONTENTUM(pos_codicis), 0, 3).
        DECLARA loci_falsus_sin SICUT NUMERUS VALENS 0.
        CONTENTUM(pos_codicis) = COMPONE_JE_FUTURUM(codex, CONTENTUM(pos_codicis), SEDES(loci_falsus_sin)).

        ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).
        ignoratum = ANALYSA_COMPARATIO_SIMPLEX(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 3, 0).
        CONTENTUM(pos_codicis) = COMPONE_CMP(codex, CONTENTUM(pos_codicis), 0, 3).
        DECLARA loci_falsus_dex SICUT NUMERUS VALENS 0.
        CONTENTUM(pos_codicis) = COMPONE_JE_FUTURUM(codex, CONTENTUM(pos_codicis), SEDES(loci_falsus_dex)).

        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 1).
        DECLARA loci_fin_et SICUT NUMERUS VALENS 0.
        CONTENTUM(pos_codicis) = COMPONE_JMP_FUTURUM(codex, CONTENTUM(pos_codicis), SEDES(loci_fin_et)).
        DECLARA pos_falsus_et SICUT NUMERUS VALENS CONTENTUM(pos_codicis).
        ignoratum = CORRIGE_SALTUM(codex, loci_falsus_sin, pos_falsus_et).
        ignoratum = CORRIGE_SALTUM(codex, loci_falsus_dex, pos_falsus_et).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 0).
        DECLARA pos_fin_et SICUT NUMERUS VALENS CONTENTUM(pos_codicis).
        ignoratum = CORRIGE_SALTUM(codex, loci_fin_et, pos_fin_et).
        ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).
    FIN-DUM.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO ANALYSA_COMPARATIO REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos_codicis SICUT ACUS<NUMERUS>.
    ACCIPIT fons SICUT ACUS<LITTERA>.
    ACCIPIT pos_fontis SICUT ACUS<NUMERUS>.
    ACCIPIT n SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.

    DECLARA ignoratum SICUT NUMERUS VALENS ANALYSA_CONIUNCTIO_LOGICA(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
    ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).

    DUM EST_DISIUNCTIO_LOGICA(fons, CONTENTUM(pos_fontis), n) == 1 PERFICE
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 2.

        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 3, 0).
        CONTENTUM(pos_codicis) = COMPONE_CMP(codex, CONTENTUM(pos_codicis), 0, 3).
        DECLARA loci_verus_sin SICUT NUMERUS VALENS 0.
        CONTENTUM(pos_codicis) = COMPONE_JNE_FUTURUM(codex, CONTENTUM(pos_codicis), SEDES(loci_verus_sin)).

        ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).
        ignoratum = ANALYSA_CONIUNCTIO_LOGICA(codex, pos_codicis, fons, pos_fontis, n, contextus_parseris).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 3, 0).
        CONTENTUM(pos_codicis) = COMPONE_CMP(codex, CONTENTUM(pos_codicis), 0, 3).
        DECLARA loci_verus_dex SICUT NUMERUS VALENS 0.
        CONTENTUM(pos_codicis) = COMPONE_JNE_FUTURUM(codex, CONTENTUM(pos_codicis), SEDES(loci_verus_dex)).

        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 0).
        DECLARA loci_fin_vel SICUT NUMERUS VALENS 0.
        CONTENTUM(pos_codicis) = COMPONE_JMP_FUTURUM(codex, CONTENTUM(pos_codicis), SEDES(loci_fin_vel)).
        DECLARA pos_verus_vel SICUT NUMERUS VALENS CONTENTUM(pos_codicis).
        ignoratum = CORRIGE_SALTUM(codex, loci_verus_sin, pos_verus_vel).
        ignoratum = CORRIGE_SALTUM(codex, loci_verus_dex, pos_verus_vel).
        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 1).
        DECLARA pos_fin_vel SICUT NUMERUS VALENS CONTENTUM(pos_codicis).
        ignoratum = CORRIGE_SALTUM(codex, loci_fin_vel, pos_fin_vel).
        ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).
    FIN-DUM.
    REDDE 0.
FIN-FUNCTIO.
'''

novus_textus = textus[:initium] + functio + novae + textus[finis:]
COMPILATOR.write_text(novus_textus, encoding="utf-8")
print("RECTE: && et || aestimationem brevem cum ordine && ante || habent.")
