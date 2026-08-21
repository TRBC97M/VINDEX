#!/usr/bin/env python3
"""TEXTUS 0.52 addit sine tabulam localium analysatorum implendo."""

from pathlib import Path
import os
import sys

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
GRADUS = int(os.environ.get("VINDEX_TEXTUS_GRADUS", "3"))
MARCA = "FUNCTIO EST_TEXTUS_VARIABILIS REDDENS NUMERUS."


def require_once(textus: str, vetus: str, nomen: str) -> None:
    numerus = textus.count(vetus)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")


def muta_once(textus: str, vetus: str, novum: str, nomen: str) -> str:
    require_once(textus, vetus, nomen)
    return textus.replace(vetus, novum, 1)


def adde_adiutores(textus: str) -> str:
    """Functiones parvas addit ut analysatores magni nova localia non accipiant."""
    ancora = "FUNCTIO ANALYSA_BLOCUS REDDENS NUMERUS.\n"
    require_once(textus, ancora, "initium-analysa-blocus")

    adiutores = '''FUNCTIO EST_TEXTUS_VARIABILIS REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT nomen SICUT NUMERUS.
    DECLARA idx_textus SICUT NUMERUS VALENS 0.
    DECLARA inventum_textus SICUT NUMERUS VALENS 0.
    DUM idx_textus < 100 && tabula[idx_textus] != 0 PERFICE
        SI tabula[idx_textus] == nomen TUNC
            inventum_textus = tabula[2900 + idx_textus].
        FIN-SI.
        idx_textus = idx_textus + 1.
    FIN-DUM.
    REDDE inventum_textus.
FIN-FUNCTIO.

FUNCTIO COMPONE_LITTERALE_TEXTUS REDDENS NUMERUS.
    ACCIPIT codex SICUT ORDO DE NUMERUS.
    ACCIPIT pos_codicis SICUT ACUS<NUMERUS>.
    ACCIPIT fons SICUT ORDO DE LITTERA.
    ACCIPIT pos_fontis SICUT ACUS<NUMERUS>.
    ACCIPIT n SICUT NUMERUS.
    DECLARA loci_saltus_textus SICUT NUMERUS VALENS 0.
    DECLARA sedes_textus SICUT NUMERUS VALENS 0.
    DECLARA mensura_textus SICUT NUMERUS VALENS 0.
    DECLARA ign_textus SICUT NUMERUS VALENS 0.

    SI CONTENTUM(pos_fontis) >= n || fons[CONTENTUM(pos_fontis)] != 34 TUNC
        REDDE 1.
    FIN-SI.

    CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.
    CONTENTUM(pos_codicis) = COMPONE_JMP_FUTURUM(codex, CONTENTUM(pos_codicis), SEDES(loci_saltus_textus)).
    sedes_textus = CONTENTUM(pos_codicis).
    CONTENTUM(pos_codicis) = SCRIBE_U64(codex, CONTENTUM(pos_codicis), 0).
    CONTENTUM(pos_codicis) = SCRIBE_U64(codex, CONTENTUM(pos_codicis), 0).

    DUM CONTENTUM(pos_fontis) < n && fons[CONTENTUM(pos_fontis)] != 34 PERFICE
        codex[CONTENTUM(pos_codicis)] = fons[CONTENTUM(pos_fontis)].
        CONTENTUM(pos_codicis) = CONTENTUM(pos_codicis) + 1.
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.
        mensura_textus = mensura_textus + 1.
    FIN-DUM.
    codex[CONTENTUM(pos_codicis)] = 0.
    CONTENTUM(pos_codicis) = CONTENTUM(pos_codicis) + 1.
    SI CONTENTUM(pos_fontis) < n TUNC
        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.
    FIN-SI.

    ign_textus = CORRIGE_PILA(codex, sedes_textus, mensura_textus).
    ign_textus = CORRIGE_PILA(codex, sedes_textus + 8, mensura_textus).
    ign_textus = CORRIGE_SALTUM(codex, loci_saltus_textus, CONTENTUM(pos_codicis)).
    CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 4194304 + sedes_textus).
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO COMPONE_IMPRIME_TEXTUS REDDENS NUMERUS.
    ACCIPIT codex SICUT ORDO DE NUMERUS.
    ACCIPIT pos SICUT NUMERUS.
    DECLARA p_textus SICUT NUMERUS VALENS pos.
    p_textus = COMPONE_TRANSCRIBE(codex, p_textus, 3, 0).
    p_textus = COMPONE_SUME_INDIRECTUM(codex, p_textus, 2, 3).
    p_textus = COMPONE_TRANSCRIBE(codex, p_textus, 6, 3).
    p_textus = COMPONE_ONERA(codex, p_textus, 1, 16).
    p_textus = COMPONE_ADD(codex, p_textus, 6, 1).
    p_textus = COMPONE_ONERA(codex, p_textus, 0, 1).
    p_textus = COMPONE_ONERA(codex, p_textus, 7, 1).
    p_textus = COMPONE_VOCA_NUCLEUM(codex, p_textus).
    REDDE p_textus.
FIN-FUNCTIO.

'''
    return textus.replace(ancora, adiutores + ancora, 1)


def gradus_unus(textus: str) -> str:
    """Declarationes et litteralia TEXTUS introducit sine novis localibus ANALYSA_BLOCUS."""
    textus = adde_adiutores(textus)

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
        + "                            SI fons[CONTENTUM(pos_fontis)] == 84 TUNC\n"
        + "                                idx_struct_ptr = 0 - 2.\n"
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
        "                            SI idx_struct_ptr == 0 - 2 TUNC\n"
        "                                ignoratum = COMPONE_LITTERALE_TEXTUS(codex, pos_codicis, fons, pos_fontis, n).\n"
        "                                SI ignoratum != 0 TUNC\n"
        "                                    ignoratum = ANALYSA_COMPARATIO(codex, pos_codicis, fons, pos_fontis, n, tabula).\n"
        "                                FIN-SI.\n"
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
        + "                            SI idx_struct_ptr == 0 - 2 TUNC\n"
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
    """Parametra TEXTUS signo in magnitudine iam exsistente distinguit."""
    ancora = "                        DECLARA magnitudo_pp SICUT NUMERUS VALENS 0.\n"
    textus = muta_once(
        textus,
        ancora,
        ancora
        + "                        SI fons[i] == 84 TUNC\n"
        + "                            magnitudo_pp = 0 - 1.\n"
        + "                        FIN-SI.\n",
        "parametrum-principalis-signum",
    )

    vetus = "                        tabula[850 + idx_param_pp] = magnitudo_pp.\n"
    novum = (
        "                        SI magnitudo_pp == 0 - 1 TUNC\n"
        "                            tabula[850 + idx_param_pp] = 0.\n"
        "                            tabula[2900 + idx_param_pp] = 1.\n"
        "                        ALITER\n"
        "                            tabula[850 + idx_param_pp] = magnitudo_pp.\n"
        "                        FIN-SI.\n"
    )
    textus = muta_once(textus, vetus, novum, "parametrum-principalis-metadata")

    ancora = "                        DECLARA es_flot_param SICUT NUMERUS VALENS 0.\n"
    textus = muta_once(
        textus,
        ancora,
        ancora
        + "                        SI fons[i] == 84 TUNC\n"
        + "                            es_flot_param = 2.\n"
        + "                        FIN-SI.\n",
        "parametrum-adiutor-signum",
    )

    vetus = "                        tabula[850 + idx_param] = magnitudo_param.\n"
    novum = (
        "                        SI es_flot_param == 2 TUNC\n"
        "                            tabula[850 + idx_param] = 0.\n"
        "                            tabula[2900 + idx_param] = 1.\n"
        "                        ALITER\n"
        "                            tabula[850 + idx_param] = magnitudo_param.\n"
        "                        FIN-SI.\n"
    )
    textus = muta_once(textus, vetus, novum, "parametrum-adiutor-metadata")
    return textus


def gradus_tres(textus: str) -> str:
    """PROCLAMA TEXTUS per valorem 2 in signo fluitantis iam exsistente dirigit."""
    ancora = "                                    DECLARA es_flot_pcs SICUT NUMERUS VALENS PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, tabula).\n"
    additio = (
        "                                    SI es_flot_pcs == 0 && CONTENTUM(pos_fontis) < n && fons[CONTENTUM(pos_fontis)] >= 97 && fons[CONTENTUM(pos_fontis)] <= 122 TUNC\n"
        "                                        SI EST_TEXTUS_VARIABILIS(tabula, SIGNUM_AB_POSITIONE(fons, CONTENTUM(pos_fontis), n)) == 1 TUNC\n"
        "                                            es_flot_pcs = 2.\n"
        "                                        FIN-SI.\n"
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
        "                                    SI es_flot_pcs == 2 TUNC\n"
        "                                        CONTENTUM(pos_codicis) = COMPONE_IMPRIME_TEXTUS(codex, CONTENTUM(pos_codicis)).\n"
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
    print(f"RECTE: gradus I-{GRADUS} TEXTUS 0.52 applicati sunt sine novis localibus analysatorum.")
    return 0


if __name__ == "__main__":
    sys.exit(principale())
