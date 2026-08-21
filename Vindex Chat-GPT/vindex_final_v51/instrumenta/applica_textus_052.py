#!/usr/bin/env python3
"""TEXTUS 0.52 prudenter addit, ANALYSA_FACTOR intacta servata."""

from pathlib import Path
import os
import sys

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
GRADUS = int(os.environ.get("VINDEX_TEXTUS_GRADUS", "3"))
MARCA = "DECLARA est_textus_novum SICUT NUMERUS VALENS 0."


def require_once(textus: str, vetus: str, nomen: str) -> None:
    numerus = textus.count(vetus)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")


def muta_once(textus: str, vetus: str, novum: str, nomen: str) -> str:
    require_once(textus, vetus, nomen)
    return textus.replace(vetus, novum, 1)


def gradus_unus(textus: str) -> str:
    """Declarationes TEXTUS et litteralia descriptoris introducit."""
    textus = muta_once(
        textus,
        "                            SI fons[CONTENTUM(pos_fontis)] == 78 || fons[CONTENTUM(pos_fontis)] == 65 || fons[CONTENTUM(pos_fontis)] == 86 TUNC\n",
        "                            SI fons[CONTENTUM(pos_fontis)] == 78 || fons[CONTENTUM(pos_fontis)] == 65 || fons[CONTENTUM(pos_fontis)] == 86 || fons[CONTENTUM(pos_fontis)] == 84 TUNC\n",
        "declaratio-typus",
    )

    ancora = "                            DECLARA idx_struct_ptr SICUT NUMERUS VALENS 0 - 1.\n"
    textus = muta_once(
        textus,
        ancora,
        ancora
        + "                            DECLARA est_textus_novum SICUT NUMERUS VALENS 0.\n"
        + "                            SI fons[CONTENTUM(pos_fontis)] == 84 TUNC\n"
        + "                                est_textus_novum = 1.\n"
        + "                                intervallum_typi = 7.\n"
        + "                            FIN-SI.\n",
        "declaratio-signum-textus",
    )

    vetus = (
        "                            CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + intervallum_typi.\n"
        "                            ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).\n"
        "                            CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 7.\n"
        "                            ignoratum = ANALYSA_COMPARATIO(codex, pos_codicis, fons, pos_fontis, n, tabula).\n\n"
    )
    novum = (
        "                            CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + intervallum_typi.\n"
        "                            ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).\n"
        "                            CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 7.\n"
        "                            SI est_textus_novum == 1 && fons[CONTENTUM(pos_fontis)] == 34 TUNC\n"
        "                                CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n"
        "                                DECLARA loci_saltus_textus_decl SICUT NUMERUS VALENS 0.\n"
        "                                CONTENTUM(pos_codicis) = COMPONE_JMP_FUTURUM(codex, CONTENTUM(pos_codicis), SEDES(loci_saltus_textus_decl)).\n"
        "                                DECLARA sedes_textus_decl SICUT NUMERUS VALENS CONTENTUM(pos_codicis).\n"
        "                                DECLARA k_cap_textus_decl SICUT NUMERUS VALENS 0.\n"
        "                                DUM k_cap_textus_decl < 16 PERFICE\n"
        "                                    codex[CONTENTUM(pos_codicis)] = 0.\n"
        "                                    CONTENTUM(pos_codicis) = CONTENTUM(pos_codicis) + 1.\n"
        "                                    k_cap_textus_decl = k_cap_textus_decl + 1.\n"
        "                                FIN-DUM.\n"
        "                                DECLARA mensura_textus_decl SICUT NUMERUS VALENS 0.\n"
        "                                DUM CONTENTUM(pos_fontis) < n && fons[CONTENTUM(pos_fontis)] != 34 PERFICE\n"
        "                                    codex[CONTENTUM(pos_codicis)] = fons[CONTENTUM(pos_fontis)].\n"
        "                                    CONTENTUM(pos_codicis) = CONTENTUM(pos_codicis) + 1.\n"
        "                                    CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n"
        "                                    mensura_textus_decl = mensura_textus_decl + 1.\n"
        "                                FIN-DUM.\n"
        "                                codex[CONTENTUM(pos_codicis)] = 0.\n"
        "                                CONTENTUM(pos_codicis) = CONTENTUM(pos_codicis) + 1.\n"
        "                                SI CONTENTUM(pos_fontis) < n TUNC\n"
        "                                    CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n"
        "                                FIN-SI.\n"
        "                                codex[sedes_textus_decl] = mensura_textus_decl & 255.\n"
        "                                codex[sedes_textus_decl + 1] = (mensura_textus_decl >> 8) & 255.\n"
        "                                codex[sedes_textus_decl + 2] = (mensura_textus_decl >> 16) & 255.\n"
        "                                codex[sedes_textus_decl + 3] = (mensura_textus_decl >> 24) & 255.\n"
        "                                codex[sedes_textus_decl + 4] = 0.\n"
        "                                codex[sedes_textus_decl + 5] = 0.\n"
        "                                codex[sedes_textus_decl + 6] = 0.\n"
        "                                codex[sedes_textus_decl + 7] = 0.\n"
        "                                codex[sedes_textus_decl + 8] = mensura_textus_decl & 255.\n"
        "                                codex[sedes_textus_decl + 9] = (mensura_textus_decl >> 8) & 255.\n"
        "                                codex[sedes_textus_decl + 10] = (mensura_textus_decl >> 16) & 255.\n"
        "                                codex[sedes_textus_decl + 11] = (mensura_textus_decl >> 24) & 255.\n"
        "                                codex[sedes_textus_decl + 12] = 0.\n"
        "                                codex[sedes_textus_decl + 13] = 0.\n"
        "                                codex[sedes_textus_decl + 14] = 0.\n"
        "                                codex[sedes_textus_decl + 15] = 0.\n"
        "                                ignoratum = CORRIGE_SALTUM(codex, loci_saltus_textus_decl, CONTENTUM(pos_codicis)).\n"
        "                                CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 4194304 + sedes_textus_decl).\n"
        "                            ALITER\n"
        "                                ignoratum = ANALYSA_COMPARATIO(codex, pos_codicis, fons, pos_fontis, n, tabula).\n"
        "                            FIN-SI.\n\n"
    )
    textus = muta_once(textus, vetus, novum, "declaratio-litteralis-textus")

    ancora = "                            tabula[850 + idx_nova2] = magnitudo_elementi.\n"
    textus = muta_once(
        textus,
        ancora,
        ancora
        + "                            SI est_textus_novum == 1 TUNC\n"
        + "                                tabula[2900 + idx_nova2] = 1.\n"
        + "                            FIN-SI.\n",
        "declaratio-metadata-textus",
    )

    textus = muta_once(
        textus,
        "                    tabula[k_clear1 + 2400] = 0.\n",
        "                    tabula[k_clear1 + 2400] = 0.\n                    tabula[k_clear1 + 2900] = 0.\n",
        "purga-principalis",
    )
    textus = muta_once(
        textus,
        "                    tabula[k_clear2 + 2400] = 0.\n",
        "                    tabula[k_clear2 + 2400] = 0.\n                    tabula[k_clear2 + 2900] = 0.\n",
        "purga-adiutor",
    )
    return textus


def gradus_duo(textus: str) -> str:
    """Parametra TEXTUS in PRINCIPALIS et functionibus auxiliaribus signat."""
    ancora = "                        DECLARA magnitudo_pp SICUT NUMERUS VALENS 0.\n"
    textus = muta_once(
        textus,
        ancora,
        ancora
        + "                        DECLARA est_textus_pp SICUT NUMERUS VALENS 0.\n"
        + "                        SI fons[i] == 84 TUNC\n"
        + "                            est_textus_pp = 1.\n"
        + "                        FIN-SI.\n",
        "parametrum-principalis-signum",
    )

    ancora = "                        tabula[850 + idx_param_pp] = magnitudo_pp.\n"
    textus = muta_once(
        textus,
        ancora,
        ancora
        + "                        SI est_textus_pp == 1 TUNC\n"
        + "                            tabula[2900 + idx_param_pp] = 1.\n"
        + "                        FIN-SI.\n",
        "parametrum-principalis-metadata",
    )

    ancora = "                        DECLARA es_flot_param SICUT NUMERUS VALENS 0.\n"
    textus = muta_once(
        textus,
        ancora,
        ancora
        + "                        DECLARA est_textus_param SICUT NUMERUS VALENS 0.\n"
        + "                        SI fons[i] == 84 TUNC\n"
        + "                            est_textus_param = 1.\n"
        + "                        FIN-SI.\n",
        "parametrum-adiutor-signum",
    )

    ancora = "                        tabula[850 + idx_param] = magnitudo_param.\n"
    textus = muta_once(
        textus,
        ancora,
        ancora
        + "                        SI est_textus_param == 1 TUNC\n"
        + "                            tabula[2900 + idx_param] = 1.\n"
        + "                        FIN-SI.\n",
        "parametrum-adiutor-metadata",
    )
    return textus


def gradus_tres(textus: str) -> str:
    """PROCLAMA valorem TEXTUS directe per nucleum scribit."""
    ancora = "                                    DECLARA es_flot_pcs SICUT NUMERUS VALENS PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, tabula).\n"
    additio = (
        "                                    DECLARA es_textus_pcs SICUT NUMERUS VALENS 0.\n"
        "                                    SI CONTENTUM(pos_fontis) < n && fons[CONTENTUM(pos_fontis)] >= 97 && fons[CONTENTUM(pos_fontis)] <= 122 TUNC\n"
        "                                        DECLARA nomen_textus_pcs SICUT NUMERUS VALENS SIGNUM_AB_POSITIONE(fons, CONTENTUM(pos_fontis), n).\n"
        "                                        DECLARA idx_textus_pcs SICUT NUMERUS VALENS 0.\n"
        "                                        DUM idx_textus_pcs < 100 && tabula[idx_textus_pcs] != 0 PERFICE\n"
        "                                            SI tabula[idx_textus_pcs] == nomen_textus_pcs TUNC\n"
        "                                                es_textus_pcs = tabula[2900 + idx_textus_pcs].\n"
        "                                            FIN-SI.\n"
        "                                            idx_textus_pcs = idx_textus_pcs + 1.\n"
        "                                        FIN-DUM.\n"
        "                                    FIN-SI.\n"
    )
    textus = muta_once(textus, ancora, ancora + additio, "proclama-prospice-textus")

    vetus = (
        "                                    DECLARA intervallum_scratch SICUT NUMERUS VALENS tabula[51].\n"
        "                                    SI es_flot_pcs == 1 TUNC\n"
        "                                        CONTENTUM(pos_codicis) = COMPONE_IMPRIME_FLUITANIS(codex, CONTENTUM(pos_codicis), intervallum_scratch).\n"
        "                                    ALITER\n"
        "                                        CONTENTUM(pos_codicis) = COMPONE_IMPRIME_NUMERUS(codex, CONTENTUM(pos_codicis), intervallum_scratch).\n"
        "                                    FIN-SI.\n\n"
    )
    novum = (
        "                                    DECLARA intervallum_scratch SICUT NUMERUS VALENS tabula[51].\n"
        "                                    SI es_textus_pcs == 1 TUNC\n"
        "                                        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 3, 0).\n"
        "                                        CONTENTUM(pos_codicis) = COMPONE_SUME_INDIRECTUM(codex, CONTENTUM(pos_codicis), 2, 3).\n"
        "                                        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 6, 3).\n"
        "                                        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 1, 16).\n"
        "                                        CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 6, 1).\n"
        "                                        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 1).\n"
        "                                        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 1).\n"
        "                                        CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).\n"
        "                                    ALITER\n"
        "                                        SI es_flot_pcs == 1 TUNC\n"
        "                                            CONTENTUM(pos_codicis) = COMPONE_IMPRIME_FLUITANIS(codex, CONTENTUM(pos_codicis), intervallum_scratch).\n"
        "                                        ALITER\n"
        "                                            CONTENTUM(pos_codicis) = COMPONE_IMPRIME_NUMERUS(codex, CONTENTUM(pos_codicis), intervallum_scratch).\n"
        "                                        FIN-SI.\n"
        "                                    FIN-SI.\n\n"
    )
    return muta_once(textus, vetus, novum, "proclama-imprime-textus")


def principale() -> int:
    if GRADUS < 1 or GRADUS > 3:
        raise SystemExit("ERRATUM: gradus inter I et III esse debet")

    textus = VIA.read_text(encoding="utf-8")
    if MARCA in textus:
        print("TEXTUS 0.52 iam applicatus est.")
        return 0

    mutationes = [gradus_unus, gradus_duo, gradus_tres]
    for index in range(GRADUS):
        textus = mutationes[index](textus)

    VIA.write_text(textus, encoding="utf-8")
    print(f"RECTE: gradus I-{GRADUS} TEXTUS 0.52 applicati sunt.")
    return 0


if __name__ == "__main__":
    sys.exit(principale())
