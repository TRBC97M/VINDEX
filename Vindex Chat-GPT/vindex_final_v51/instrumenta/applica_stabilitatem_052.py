#!/usr/bin/env python3
"""Mutationes stabiles VINDEX 0.52 compilatori semel applicat."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
textus = VIA.read_text(encoding="utf-8")


def muta_unicum(vetus: str, novum: str, nomen: str) -> None:
    global textus
    numerus = textus.count(vetus)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")
    textus = textus.replace(vetus, novum, 1)


if "FUNCTIO PURGA_COMMENTARIA REDDENS NUMERUS." not in textus:
    adiutores = r'''

FUNCTIO COMPONE_LEGE_VARIABILEM_SIMPLEX REDDENS NUMERUS.
    ACCIPIT codex SICUT ORDO DE NUMERUS.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT nomen SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS pos.
    DECLARA intervallum SICUT NUMERUS VALENS CERCA_VARIABILEM(tabula, nomen).
    DECLARA est_series SICUT NUMERUS VALENS ESTNE_SERIES(tabula, nomen).
    SI est_series == 1 TUNC
        p = COMPONE_LEA_PILA(codex, p, 0, intervallum).
    ALITER
        SI EST_FLUITANS_VARIABILIS(tabula, nomen) == 1 TUNC
            p = COMPONE_MOVSD_CARGA(codex, p, 0, intervallum).
            p = COMPONE_MOVQ_A_GP(codex, p, 0, 0).
        ALITER
            p = COMPONE_SUME_PILA(codex, p, 0, intervallum).
        FIN-SI.
    FIN-SI.
    REDDE p.
FIN-FUNCTIO.

FUNCTIO PURGA_COMMENTARIA REDDENS NUMERUS.
    ACCIPIT fons SICUT ORDO DE LITTERA.
    ACCIPIT n SICUT NUMERUS.
    DECLARA i SICUT NUMERUS VALENS 0.
    DECLARA egressus SICUT NUMERUS VALENS 0.
    DECLARA intra_chordam SICUT NUMERUS VALENS 0.
    DUM i < n PERFICE
        SI fons[i] == 34 TUNC
            fons[egressus] = fons[i].
            egressus = egressus + 1.
            i = i + 1.
            SI intra_chordam == 0 TUNC
                intra_chordam = 1.
            ALITER
                intra_chordam = 0.
            FIN-SI.
        ALITER
            SI intra_chordam == 0 && fons[i] == 47 && i + 1 < n && fons[i + 1] == 47 TUNC
                DUM i < n && fons[i] != 10 PERFICE
                    i = i + 1.
                FIN-DUM.
            ALITER
                fons[egressus] = fons[i].
                egressus = egressus + 1.
                i = i + 1.
            FIN-SI.
        FIN-SI.
    FIN-DUM.
    REDDE egressus.
FIN-FUNCTIO.
'''
    textus = textus.rstrip() + adiutores + "\n"

muta_unicum(
    "    DECLARA tabula SICUT ORDO DE NUMERUS CAPACITAS 3000.\n",
    "    DECLARA tabula SICUT ORDO DE NUMERUS CAPACITAS 3200.\n",
    "capacitas-tabulae",
)

muta_unicum(
    "    DUM k < n PERFICE\n        fons_brut[k] = OCTETUS(k).\n        k = k + 1.\n    FIN-DUM.\n\n    DECLARA fons SICUT ORDO DE LITTERA CAPACITAS 213000.\n",
    "    DUM k < n PERFICE\n        fons_brut[k] = OCTETUS(k).\n        k = k + 1.\n    FIN-DUM.\n    n = PURGA_COMMENTARIA(fons_brut, n).\n\n    DECLARA fons SICUT ORDO DE LITTERA CAPACITAS 213000.\n",
    "commentaria-ante-importa",
)

muta_unicum(
    "    n = pos_out_imp.\n\n    DECLARA codex SICUT ORDO DE NUMERUS CAPACITAS 300000.\n",
    "    n = pos_out_imp.\n    n = PURGA_COMMENTARIA(fons, n).\n\n    DECLARA codex SICUT ORDO DE NUMERUS CAPACITAS 300000.\n",
    "commentaria-post-importa",
)

muta_unicum(
    "    SI (fons[CONTENTUM(pos_fontis)] >= 65 && fons[CONTENTUM(pos_fontis)] <= 90) TUNC\n        DECLARA nomen_fn SICUT NUMERUS VALENS EXTRAHE_ET_SIGNA(fons, pos_fontis, n).\n        ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n\n        DECLARA numerus_argumentorum SICUT NUMERUS VALENS 0.\n",
    "    SI (fons[CONTENTUM(pos_fontis)] >= 65 && fons[CONTENTUM(pos_fontis)] <= 90) TUNC\n        DECLARA nomen_fn SICUT NUMERUS VALENS EXTRAHE_ET_SIGNA(fons, pos_fontis, n).\n        ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).\n        SI CONTENTUM(pos_fontis) >= n || fons[CONTENTUM(pos_fontis)] != 40 TUNC\n            CONTENTUM(pos_codicis) = COMPONE_LEGE_VARIABILEM_SIMPLEX(codex, CONTENTUM(pos_codicis), tabula, nomen_fn).\n            REDDE 0.\n        FIN-SI.\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n\n        DECLARA numerus_argumentorum SICUT NUMERUS VALENS 0.\n",
    "variabilis-maiuscula",
)

VIA.write_text(textus, encoding="utf-8")
print("RECTE: Stabilitas Compilatoris 0.52 applicata est.")
