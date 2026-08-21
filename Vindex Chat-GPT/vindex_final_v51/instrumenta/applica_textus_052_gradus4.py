#!/usr/bin/env python3
"""Gradus IV TEXTUS: concatenationem et comparationem secundum contentum addit."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "FUNCTIO COMPONE_CONCATENA_TEXTUS REDDENS NUMERUS."


def exige_unum(textus: str, exemplar: str, nomen: str) -> None:
    numerus = textus.count(exemplar)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")


def muta_unum(textus: str, vetus: str, novum: str, nomen: str) -> str:
    exige_unum(textus, vetus, nomen)
    return textus.replace(vetus, novum, 1)


def muta_in_functione(textus: str, nomen_functionis: str, vetus: str, novum: str, nomen: str) -> str:
    initium = textus.find(f"FUNCTIO {nomen_functionis} REDDENS NUMERUS.\n")
    if initium < 0:
        raise SystemExit(f"ERRATUM: functio {nomen_functionis} non inventa est")
    finis = textus.find("FIN-FUNCTIO.\n", initium)
    if finis < 0:
        raise SystemExit(f"ERRATUM: finis functionis {nomen_functionis} non inventus est")
    finis += len("FIN-FUNCTIO.\n")
    corpus = textus[initium:finis]
    exige_unum(corpus, vetus, nomen)
    corpus = corpus.replace(vetus, novum, 1)
    return textus[:initium] + corpus + textus[finis:]


def adde_adiutores(textus: str) -> str:
    ancora = "FUNCTIO COMPONE_LITTERALE_TEXTUS REDDENS NUMERUS.\n"
    exige_unum(textus, ancora, "adiutores-textus")
    adiutores = '''FUNCTIO COMPONE_CONCATENA_TEXTUS REDDENS NUMERUS.
    ACCIPIT codex SICUT ORDO DE NUMERUS.
    ACCIPIT pos SICUT NUMERUS.
    DECLARA p_ct SICUT NUMERUS VALENS pos.

    // Ingressus: RAX textus sinister, RBX textus dexter. Exitus: RAX textus novus.
    p_ct = COMPONE_TRANSCRIBE(codex, p_ct, 7, 0).
    p_ct = COMPONE_TRANSCRIBE(codex, p_ct, 6, 3).
    p_ct = COMPONE_SUME_INDIRECTUM(codex, p_ct, 8, 7).
    p_ct = COMPONE_SUME_INDIRECTUM(codex, p_ct, 9, 6).
    p_ct = COMPONE_TRANSCRIBE(codex, p_ct, 10, 8).
    p_ct = COMPONE_ADD(codex, p_ct, 10, 9).

    // Descriptor novus e TAS accipit: XVI octeta capitis, contentum, terminator nullus.
    p_ct = COMPONE_TRANSCRIBE(codex, p_ct, 2, 10).
    p_ct = COMPONE_ONERA(codex, p_ct, 1, 17).
    p_ct = COMPONE_ADD(codex, p_ct, 2, 1).
    p_ct = COMPONE_ONERA(codex, p_ct, 1, 33554432).
    p_ct = COMPONE_SUME_INDIRECTUM(codex, p_ct, 0, 1).
    p_ct = COMPONE_SERVA_INDIRECTUM(codex, p_ct, 0, 2).
    p_ct = COMPONE_TRANSCRIBE(codex, p_ct, 3, 0).
    p_ct = COMPONE_ONERA(codex, p_ct, 1, 8).
    p_ct = COMPONE_ADD(codex, p_ct, 0, 1).
    p_ct = COMPONE_IMPONE(codex, p_ct, 0).
    p_ct = COMPONE_TRANSCRIBE(codex, p_ct, 0, 3).
    p_ct = COMPONE_ONERA(codex, p_ct, 1, 8).
    p_ct = COMPONE_ADD(codex, p_ct, 0, 1).
    p_ct = COMPONE_ADD(codex, p_ct, 0, 2).
    p_ct = COMPONE_VERIFICA_TAS(codex, p_ct).
    p_ct = COMPONE_ONERA(codex, p_ct, 1, 33554432).
    p_ct = COMPONE_SERVA_INDIRECTUM(codex, p_ct, 1, 0).
    p_ct = COMPONE_AUFER(codex, p_ct, 0).

    p_ct = COMPONE_TRANSCRIBE(codex, p_ct, 11, 0).
    p_ct = COMPONE_SERVA_INDIRECTUM(codex, p_ct, 11, 10).
    p_ct = COMPONE_TRANSCRIBE(codex, p_ct, 3, 11).
    p_ct = COMPONE_ONERA(codex, p_ct, 1, 8).
    p_ct = COMPONE_ADD(codex, p_ct, 3, 1).
    p_ct = COMPONE_SERVA_INDIRECTUM(codex, p_ct, 3, 10).
    p_ct = COMPONE_ADD(codex, p_ct, 3, 1).

    p_ct = COMPONE_ONERA(codex, p_ct, 1, 16).
    p_ct = COMPONE_ADD(codex, p_ct, 7, 1).
    p_ct = COMPONE_ADD(codex, p_ct, 6, 1).

    DECLARA initium_sinistri_ct SICUT NUMERUS VALENS p_ct.
    p_ct = COMPONE_ONERA(codex, p_ct, 2, 0).
    p_ct = COMPONE_CMP(codex, p_ct, 8, 2).
    DECLARA loci_fin_sinistri_ct SICUT NUMERUS VALENS 0.
    p_ct = COMPONE_JE_FUTURUM(codex, p_ct, SEDES(loci_fin_sinistri_ct)).
    p_ct = COMPONE_MOVZX(codex, p_ct, 0, 7).
    p_ct = COMPONE_SERVA_OCTETUM(codex, p_ct, 3, 0).
    p_ct = COMPONE_ONERA(codex, p_ct, 2, 1).
    p_ct = COMPONE_ADD(codex, p_ct, 7, 2).
    p_ct = COMPONE_ADD(codex, p_ct, 3, 2).
    p_ct = COMPONE_SUB(codex, p_ct, 8, 2).
    p_ct = COMPONE_JMP_RETRO(codex, p_ct, initium_sinistri_ct).
    DECLARA post_sinistrum_ct SICUT NUMERUS VALENS p_ct.
    DECLARA ign_sinistri_ct SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_fin_sinistri_ct, post_sinistrum_ct).

    DECLARA initium_dextri_ct SICUT NUMERUS VALENS p_ct.
    p_ct = COMPONE_ONERA(codex, p_ct, 2, 0).
    p_ct = COMPONE_CMP(codex, p_ct, 9, 2).
    DECLARA loci_fin_dextri_ct SICUT NUMERUS VALENS 0.
    p_ct = COMPONE_JE_FUTURUM(codex, p_ct, SEDES(loci_fin_dextri_ct)).
    p_ct = COMPONE_MOVZX(codex, p_ct, 0, 6).
    p_ct = COMPONE_SERVA_OCTETUM(codex, p_ct, 3, 0).
    p_ct = COMPONE_ONERA(codex, p_ct, 2, 1).
    p_ct = COMPONE_ADD(codex, p_ct, 6, 2).
    p_ct = COMPONE_ADD(codex, p_ct, 3, 2).
    p_ct = COMPONE_SUB(codex, p_ct, 9, 2).
    p_ct = COMPONE_JMP_RETRO(codex, p_ct, initium_dextri_ct).
    DECLARA post_dextrum_ct SICUT NUMERUS VALENS p_ct.
    DECLARA ign_dextri_ct SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_fin_dextri_ct, post_dextrum_ct).

    p_ct = COMPONE_ONERA(codex, p_ct, 0, 0).
    p_ct = COMPONE_SERVA_OCTETUM(codex, p_ct, 3, 0).
    p_ct = COMPONE_TRANSCRIBE(codex, p_ct, 0, 11).
    REDDE p_ct.
FIN-FUNCTIO.

FUNCTIO COMPONE_COMPARA_TEXTUS REDDENS NUMERUS.
    ACCIPIT codex SICUT ORDO DE NUMERUS.
    ACCIPIT pos SICUT NUMERUS.
    DECLARA p_cmp_t SICUT NUMERUS VALENS pos.
    DECLARA loci_long_s_cmp_t SICUT NUMERUS VALENS 0.
    DECLARA loci_long_d_cmp_t SICUT NUMERUS VALENS 0.
    DECLARA loci_dispar_cmp_t SICUT NUMERUS VALENS 0.
    DECLARA loci_fin_cmp_t SICUT NUMERUS VALENS 0.

    // Comparatio lexicographica; exitus in RAX et vexilla x86 congruunt.
    p_cmp_t = COMPONE_TRANSCRIBE(codex, p_cmp_t, 7, 0).
    p_cmp_t = COMPONE_TRANSCRIBE(codex, p_cmp_t, 6, 3).
    p_cmp_t = COMPONE_SUME_INDIRECTUM(codex, p_cmp_t, 8, 7).
    p_cmp_t = COMPONE_SUME_INDIRECTUM(codex, p_cmp_t, 9, 6).
    p_cmp_t = COMPONE_ONERA(codex, p_cmp_t, 1, 16).
    p_cmp_t = COMPONE_ADD(codex, p_cmp_t, 7, 1).
    p_cmp_t = COMPONE_ADD(codex, p_cmp_t, 6, 1).

    DECLARA initium_cmp_t SICUT NUMERUS VALENS p_cmp_t.
    p_cmp_t = COMPONE_ONERA(codex, p_cmp_t, 2, 0).
    p_cmp_t = COMPONE_CMP(codex, p_cmp_t, 8, 2).
    p_cmp_t = COMPONE_JE_FUTURUM(codex, p_cmp_t, SEDES(loci_long_s_cmp_t)).
    p_cmp_t = COMPONE_CMP(codex, p_cmp_t, 9, 2).
    p_cmp_t = COMPONE_JE_FUTURUM(codex, p_cmp_t, SEDES(loci_long_d_cmp_t)).
    p_cmp_t = COMPONE_MOVZX(codex, p_cmp_t, 0, 7).
    p_cmp_t = COMPONE_MOVZX(codex, p_cmp_t, 2, 6).
    p_cmp_t = COMPONE_CMP(codex, p_cmp_t, 0, 2).
    p_cmp_t = COMPONE_JNE_FUTURUM(codex, p_cmp_t, SEDES(loci_dispar_cmp_t)).
    p_cmp_t = COMPONE_ONERA(codex, p_cmp_t, 2, 1).
    p_cmp_t = COMPONE_ADD(codex, p_cmp_t, 7, 2).
    p_cmp_t = COMPONE_ADD(codex, p_cmp_t, 6, 2).
    p_cmp_t = COMPONE_SUB(codex, p_cmp_t, 8, 2).
    p_cmp_t = COMPONE_SUB(codex, p_cmp_t, 9, 2).
    p_cmp_t = COMPONE_JMP_RETRO(codex, p_cmp_t, initium_cmp_t).

    DECLARA post_long_cmp_t SICUT NUMERUS VALENS p_cmp_t.
    DECLARA ign_long_s_cmp_t SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_long_s_cmp_t, post_long_cmp_t).
    DECLARA ign_long_d_cmp_t SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_long_d_cmp_t, post_long_cmp_t).
    p_cmp_t = COMPONE_TRANSCRIBE(codex, p_cmp_t, 0, 8).
    p_cmp_t = COMPONE_SUB(codex, p_cmp_t, 0, 9).
    p_cmp_t = COMPONE_JMP_FUTURUM(codex, p_cmp_t, SEDES(loci_fin_cmp_t)).

    DECLARA post_dispar_cmp_t SICUT NUMERUS VALENS p_cmp_t.
    DECLARA ign_dispar_cmp_t SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_dispar_cmp_t, post_dispar_cmp_t).
    p_cmp_t = COMPONE_SUB(codex, p_cmp_t, 0, 2).

    DECLARA post_fin_cmp_t SICUT NUMERUS VALENS p_cmp_t.
    DECLARA ign_fin_cmp_t SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_fin_cmp_t, post_fin_cmp_t).
    p_cmp_t = COMPONE_ONERA(codex, p_cmp_t, 2, 0).
    p_cmp_t = COMPONE_CMP(codex, p_cmp_t, 0, 2).
    REDDE p_cmp_t.
FIN-FUNCTIO.

'''
    return textus.replace(ancora, adiutores + ancora, 1)


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")
    if MARCA in textus:
        print("RECTE: gradus IV TEXTUS iam applicatus est.")
        return

    textus = adde_adiutores(textus)

    vetus = "    DECLARA ignoratum SICUT NUMERUS VALENS IGNORA_SPATIA(fons, pos_fontis, n).\n\n    SI fons[CONTENTUM(pos_fontis)] == 40 TUNC\n"
    novum = "    DECLARA ignoratum SICUT NUMERUS VALENS IGNORA_SPATIA(fons, pos_fontis, n).\n\n    SI fons[CONTENTUM(pos_fontis)] == 34 TUNC\n        REDDE COMPONE_LITTERALE_TEXTUS(codex, pos_codicis, fons, pos_fontis, n).\n    FIN-SI.\n\n    SI fons[CONTENTUM(pos_fontis)] == 40 TUNC\n"
    textus = muta_in_functione(textus, "ANALYSA_FACTOR", vetus, novum, "factor-litterale-textus")

    vetus = "    DECLARA resultatum SICUT NUMERUS VALENS 0.\n    SI pos < n && fons[pos] >= 97 && fons[pos] <= 122 TUNC\n"
    novum = "    DECLARA resultatum SICUT NUMERUS VALENS 0.\n    SI pos < n && fons[pos] == 34 TUNC\n        REDDE 2.\n    FIN-SI.\n    SI pos < n && fons[pos] >= 97 && fons[pos] <= 122 TUNC\n"
    textus = muta_in_functione(textus, "PROSPICE_EST_FLUITANS", vetus, novum, "prospectus-litteralis-textus")

    vetus = '''                            SI idx_struct_ptr == 0 - 2 TUNC
                                ignoratum = COMPONE_LITTERALE_TEXTUS(codex, pos_codicis, fons, pos_fontis, n).
                                SI ignoratum != 0 TUNC
                                    ignoratum = ANALYSA_COMPARATIO(codex, pos_codicis, fons, pos_fontis, n, tabula).
                                FIN-SI.
                            ALITER
                                ignoratum = ANALYSA_COMPARATIO(codex, pos_codicis, fons, pos_fontis, n, tabula).
                            FIN-SI.
'''
    novum = '''                            ignoratum = ANALYSA_COMPARATIO(codex, pos_codicis, fons, pos_fontis, n, tabula).
'''
    textus = muta_in_functione(textus, "ANALYSA_BLOCUS", vetus, novum, "declaratio-expressio-textus")

    vetus = "        SI es_flot_expr == 1 && (operatio == 43 || operatio == 45) TUNC\n"
    novum = "        SI es_flot_expr == 2 && operatio == 43 TUNC\n            CONTENTUM(pos_codicis) = COMPONE_CONCATENA_TEXTUS(codex, CONTENTUM(pos_codicis)).\n        ALITER\n        SI es_flot_expr == 1 && (operatio == 43 || operatio == 45) TUNC\n"
    textus = muta_in_functione(textus, "ANALYSA_EXPRESSIO", vetus, novum, "expressio-concatenatio")

    vetus = "        FIN-SI.\n        FIN-SI.\n        FIN-SI.\n        ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).\n"
    novum = "        FIN-SI.\n        FIN-SI.\n        FIN-SI.\n        FIN-SI.\n        ignoratum = IGNORA_SPATIA(fons, pos_fontis, n).\n"
    textus = muta_in_functione(textus, "ANALYSA_EXPRESSIO", vetus, novum, "expressio-fin-concatenationis")

    vetus = '''    SI es_flot_cmp == 1 TUNC
        CONTENTUM(pos_codicis) = COMPONE_COMPARA_FLUITANIS(codex, CONTENTUM(pos_codicis)).
    ALITER
        CONTENTUM(pos_codicis) = COMPONE_SUB(codex, CONTENTUM(pos_codicis), 0, 3).
    FIN-SI.
'''
    novum = '''    SI es_flot_cmp == 2 TUNC
        CONTENTUM(pos_codicis) = COMPONE_COMPARA_TEXTUS(codex, CONTENTUM(pos_codicis)).
    ALITER
        SI es_flot_cmp == 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_COMPARA_FLUITANIS(codex, CONTENTUM(pos_codicis)).
        ALITER
            CONTENTUM(pos_codicis) = COMPONE_SUB(codex, CONTENTUM(pos_codicis), 0, 3).
        FIN-SI.
    FIN-SI.
'''
    textus = muta_in_functione(textus, "ANALYSA_COMPARATIO", vetus, novum, "comparatio-contenti")

    initium = textus.find("FUNCTIO ANALYSA_COMPARATIO REDDENS NUMERUS.\n")
    finis = textus.find("FIN-FUNCTIO.\n", initium) + len("FIN-FUNCTIO.\n")
    corpus = textus[initium:finis]
    numerus = corpus.count("es_flot_cmp == 0 TUNC")
    if numerus != 4:
        raise SystemExit(f"ERRATUM: quattuor custodiae ordinis exspectatae sunt, inventae {numerus}")
    corpus = corpus.replace("es_flot_cmp == 0 TUNC", "es_flot_cmp != 1 TUNC")
    textus = textus[:initium] + corpus + textus[finis:]

    VIA.write_text(textus, encoding="utf-8")
    print("RECTE: gradus IV TEXTUS applicatus est: concatenatio et comparatio contenti paratae sunt.")


if __name__ == "__main__":
    applica()
