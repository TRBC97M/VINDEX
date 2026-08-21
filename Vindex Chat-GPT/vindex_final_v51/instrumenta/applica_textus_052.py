#!/usr/bin/env python3
"""Mutationes primae TEXTUS 0.52 in compilatorem auto-hospitem applicantur."""

from pathlib import Path
import sys

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")


def require_once(textus: str, vetus: str, nomen: str) -> None:
    numerus = textus.count(vetus)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")


def muta_once(textus: str, vetus: str, novum: str, nomen: str) -> str:
    require_once(textus, vetus, nomen)
    return textus.replace(vetus, novum, 1)


def inserere_ante(textus: str, initium: str, terminus: str, insertum: str, nomen: str) -> str:
    locus0 = textus.find(initium)
    if locus0 < 0:
        raise SystemExit(f"ERRATUM: initium {nomen} non inventum est")
    locus = textus.find(terminus, locus0)
    if locus < 0:
        raise SystemExit(f"ERRATUM: terminus {nomen} non inventum est")
    return textus[:locus] + insertum + textus[locus:]


def principale() -> int:
    textus = VIA.read_text(encoding="utf-8")
    if "FUNCTIO EST_TEXTUS_VARIABILIS REDDENS NUMERUS." in textus:
        print("TEXTUS 0.52 iam applicatus est.")
        return 0

    textus = muta_once(
        textus,
        "// Capacitas tabulae tota: 850.\n",
        "//   2900-2999: signa TEXTUS variabilium (100 loca)\n// Capacitas tabulae tota: 3000.\n",
        "descriptio-tabulae",
    )

    functio_textus = '''FUNCTIO EST_TEXTUS_VARIABILIS REDDENS NUMERUS.\n    ACCIPIT tabula SICUT ORDO DE NUMERUS.\n    ACCIPIT nomen SICUT NUMERUS.\n    DECLARA idx SICUT NUMERUS VALENS 0.\n    DECLARA resultatum SICUT NUMERUS VALENS 0.\n    DUM idx < 100 && tabula[idx] != 0 PERFICE\n        SI tabula[idx] == nomen TUNC\n            resultatum = tabula[2900 + idx].\n        FIN-SI.\n        idx = idx + 1.\n    FIN-DUM.\n    REDDE resultatum.\nFIN-FUNCTIO.\n\n'''
    textus = inserere_ante(
        textus,
        "FUNCTIO EST_FLUITANS_VARIABILIS REDDENS NUMERUS.",
        "FUNCTIO STRUCTURA_VARIABILIS REDDENS NUMERUS.",
        functio_textus,
        "metadata-textus",
    )

    ancora_factor = "    DECLARA ignoratum SICUT NUMERUS VALENS IGNORA_SPATIA(fons, pos_fontis, n).\n\n"
    init_factor = textus.find("FUNCTIO ANALYSA_FACTOR REDDENS NUMERUS.")
    locus_factor = textus.find(ancora_factor, init_factor)
    if init_factor < 0 or locus_factor < 0:
        raise SystemExit("ERRATUM: ANALYSA_FACTOR mutari non potest")
    locus_factor += len(ancora_factor)
    factor_textus = '''    // TEXTUS 0.52: longitudo descriptoris in primo verbo est.\n    SI fons[CONTENTUM(pos_fontis)] == 76 && CONTENTUM(pos_fontis) + 9 < n && fons[CONTENTUM(pos_fontis)+1] == 79 && fons[CONTENTUM(pos_fontis)+2] == 78 && fons[CONTENTUM(pos_fontis)+3] == 71 && fons[CONTENTUM(pos_fontis)+4] == 73 && fons[CONTENTUM(pos_fontis)+5] == 84 && fons[CONTENTUM(pos_fontis)+6] == 85 && fons[CONTENTUM(pos_fontis)+7] == 68 && fons[CONTENTUM(pos_fontis)+8] == 79 && fons[CONTENTUM(pos_fontis)+9] == 40 TUNC\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 10.\n        DECLARA ig_longitudo SICUT NUMERUS VALENS ANALYSA_EXPRESSIO(codex, pos_codicis, fons, pos_fontis, n, tabula).\n        ig_longitudo = IGNORA_SPATIA(fons, pos_fontis, n).\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        CONTENTUM(pos_codicis) = COMPONE_SUME_INDIRECTUM(codex, CONTENTUM(pos_codicis), 0, 0).\n        REDDE 0.\n    FIN-SI.\n\n    // Litterale TEXTUS: [longitudo:u64][capacitas:u64][octeta UTF-8][0].\n    SI fons[CONTENTUM(pos_fontis)] == 34 TUNC\n        CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        DECLARA loci_saltus_textus SICUT NUMERUS VALENS 0.\n        CONTENTUM(pos_codicis) = COMPONE_JMP_FUTURUM(codex, CONTENTUM(pos_codicis), SEDES(loci_saltus_textus)).\n        DECLARA sedes_textus SICUT NUMERUS VALENS CONTENTUM(pos_codicis).\n        CONTENTUM(pos_codicis) = SCRIBE_U64(codex, CONTENTUM(pos_codicis), 0).\n        CONTENTUM(pos_codicis) = SCRIBE_U64(codex, CONTENTUM(pos_codicis), 0).\n        DECLARA mensura_textus SICUT NUMERUS VALENS 0.\n        DUM CONTENTUM(pos_fontis) < n && fons[CONTENTUM(pos_fontis)] != 34 PERFICE\n            codex[CONTENTUM(pos_codicis)] = fons[CONTENTUM(pos_fontis)].\n            CONTENTUM(pos_codicis) = CONTENTUM(pos_codicis) + 1.\n            CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n            mensura_textus = mensura_textus + 1.\n        FIN-DUM.\n        codex[CONTENTUM(pos_codicis)] = 0.\n        CONTENTUM(pos_codicis) = CONTENTUM(pos_codicis) + 1.\n        SI CONTENTUM(pos_fontis) < n TUNC\n            CONTENTUM(pos_fontis) = CONTENTUM(pos_fontis) + 1.\n        FIN-SI.\n        ignoratum = CORRIGE_PILA(codex, sedes_textus, mensura_textus).\n        ignoratum = CORRIGE_PILA(codex, sedes_textus + 8, mensura_textus).\n        ignoratum = CORRIGE_SALTUM(codex, loci_saltus_textus, CONTENTUM(pos_codicis)).\n        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 4194304 + sedes_textus).\n        REDDE 0.\n    FIN-SI.\n\n'''
    textus = textus[:locus_factor] + factor_textus + textus[locus_factor:]

    vetus_cond = "                            SI fons[CONTENTUM(pos_fontis)] == 78 || fons[CONTENTUM(pos_fontis)] == 65 || fons[CONTENTUM(pos_fontis)] == 86 TUNC\n"
    novus_cond = "                            SI fons[CONTENTUM(pos_fontis)] == 78 || fons[CONTENTUM(pos_fontis)] == 65 || fons[CONTENTUM(pos_fontis)] == 86 || fons[CONTENTUM(pos_fontis)] == 84 TUNC\n"
    textus = muta_once(textus, vetus_cond, novus_cond, "declaratio-typus")

    ancora_ptr = "                            DECLARA idx_struct_ptr SICUT NUMERUS VALENS 0 - 1.\n"
    add_ptr = ancora_ptr + '''                            DECLARA est_textus_novum SICUT NUMERUS VALENS 0.\n                            SI fons[CONTENTUM(pos_fontis)] == 84 TUNC\n                                est_textus_novum = 1.\n                                intervallum_typi = 7.\n                            FIN-SI.\n'''
    textus = muta_once(textus, ancora_ptr, add_ptr, "declaratio-signum-textus")

    ancora_meta_decl = "                            tabula[850 + idx_nova2] = magnitudo_elementi.\n"
    add_meta_decl = ancora_meta_decl + '''                            SI est_textus_novum == 1 TUNC\n                                tabula[2900 + idx_nova2] = 1.\n                            FIN-SI.\n'''
    textus = muta_once(textus, ancora_meta_decl, add_meta_decl, "declaratio-metadata-textus")

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

    ancora_pp = "                        DECLARA magnitudo_pp SICUT NUMERUS VALENS 0.\n"
    add_pp = ancora_pp + '''                        DECLARA est_textus_pp SICUT NUMERUS VALENS 0.\n                        SI fons[i] == 84 TUNC\n                            est_textus_pp = 1.\n                        FIN-SI.\n'''
    textus = muta_once(textus, ancora_pp, add_pp, "parametrum-principalis-signum")
    ancora_pp_meta = "                        tabula[850 + idx_param_pp] = magnitudo_pp.\n"
    add_pp_meta = ancora_pp_meta + '''                        SI est_textus_pp == 1 TUNC\n                            tabula[2900 + idx_param_pp] = 1.\n                        FIN-SI.\n'''
    textus = muta_once(textus, ancora_pp_meta, add_pp_meta, "parametrum-principalis-metadata")

    ancora_param = "                        DECLARA es_flot_param SICUT NUMERUS VALENS 0.\n"
    add_param = ancora_param + '''                        DECLARA est_textus_param SICUT NUMERUS VALENS 0.\n                        SI fons[i] == 84 TUNC\n                            est_textus_param = 1.\n                        FIN-SI.\n'''
    textus = muta_once(textus, ancora_param, add_param, "parametrum-adiutor-signum")
    ancora_param_meta = "                        tabula[850 + idx_param] = magnitudo_param.\n"
    add_param_meta = ancora_param_meta + '''                        SI est_textus_param == 1 TUNC\n                            tabula[2900 + idx_param] = 1.\n                        FIN-SI.\n'''
    textus = muta_once(textus, ancora_param_meta, add_param_meta, "parametrum-adiutor-metadata")

    ancora_prospice = "                                    DECLARA es_flot_pcs SICUT NUMERUS VALENS PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, tabula).\n"
    add_prospice = ancora_prospice + '''                                    DECLARA es_textus_pcs SICUT NUMERUS VALENS 0.\n                                    SI CONTENTUM(pos_fontis) < n && fons[CONTENTUM(pos_fontis)] >= 97 && fons[CONTENTUM(pos_fontis)] <= 122 TUNC\n                                        DECLARA nomen_textus_pcs SICUT NUMERUS VALENS SIGNUM_AB_POSITIONE(fons, CONTENTUM(pos_fontis), n).\n                                        es_textus_pcs = EST_TEXTUS_VARIABILIS(tabula, nomen_textus_pcs).\n                                    FIN-SI.\n'''
    textus = muta_once(textus, ancora_prospice, add_prospice, "proclama-prospice-textus")

    vetus_imprime = '''                                    DECLARA intervallum_scratch SICUT NUMERUS VALENS tabula[51].\n                                    SI es_flot_pcs == 1 TUNC\n                                        CONTENTUM(pos_codicis) = COMPONE_IMPRIME_FLUITANIS(codex, CONTENTUM(pos_codicis), intervallum_scratch).\n                                    ALITER\n                                        CONTENTUM(pos_codicis) = COMPONE_IMPRIME_NUMERUS(codex, CONTENTUM(pos_codicis), intervallum_scratch).\n                                    FIN-SI.\n'''
    novum_imprime = '''                                    DECLARA intervallum_scratch SICUT NUMERUS VALENS tabula[51].\n                                    SI es_textus_pcs == 1 TUNC\n                                        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 3, 0).\n                                        CONTENTUM(pos_codicis) = COMPONE_SUME_INDIRECTUM(codex, CONTENTUM(pos_codicis), 2, 3).\n                                        CONTENTUM(pos_codicis) = COMPONE_TRANSCRIBE(codex, CONTENTUM(pos_codicis), 6, 3).\n                                        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 1, 16).\n                                        CONTENTUM(pos_codicis) = COMPONE_ADD(codex, CONTENTUM(pos_codicis), 6, 1).\n                                        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 0, 1).\n                                        CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 7, 1).\n                                        CONTENTUM(pos_codicis) = COMPONE_VOCA_NUCLEUM(codex, CONTENTUM(pos_codicis)).\n                                    ALITER\n                                        SI es_flot_pcs == 1 TUNC\n                                            CONTENTUM(pos_codicis) = COMPONE_IMPRIME_FLUITANIS(codex, CONTENTUM(pos_codicis), intervallum_scratch).\n                                        ALITER\n                                            CONTENTUM(pos_codicis) = COMPONE_IMPRIME_NUMERUS(codex, CONTENTUM(pos_codicis), intervallum_scratch).\n                                        FIN-SI.\n                                    FIN-SI.\n'''
    textus = muta_once(textus, vetus_imprime, novum_imprime, "proclama-imprime-textus")

    VIA.write_text(textus, encoding="utf-8")
    print("RECTE: prima fundamenta TEXTUS 0.52 compilatori addita sunt.")
    return 0


if __name__ == "__main__":
    sys.exit(principale())
