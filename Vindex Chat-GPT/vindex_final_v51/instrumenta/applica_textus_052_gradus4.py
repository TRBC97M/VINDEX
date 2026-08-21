#!/usr/bin/env python3
"""Gradus IV TEXTUS: concatenationem et comparationem secundum contentum addit."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "FUNCTIO COMPONE_CONCATENA_TEXTUS REDDENS NUMERUS."


def exige_unum(textus: str, exemplar: str, nomen: str) -> None:
    numerus = textus.count(exemplar)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")


def muta_in_functione(textus: str, nomen_functionis: str, vetus: str, novum: str, nomen: str) -> str:
    initium = textus.find(f"FUNCTIO {nomen_functionis} REDDENS NUMERUS.\n")
    if initium < 0:
        raise SystemExit(f"ERRATUM: functio {nomen_functionis} non inventa est")
    finis = textus.find("FIN-FUNCTIO.\n", initium)
    if finis < 0:
        raise SystemExit(f"ERRATUM: finis functionis {nomen_functionis} non inventus est")
    finis += len("FIN-FUNCTIO.\n")
    pars = textus[initium:finis]
    exige_unum(pars, vetus, nomen)
    pars = pars.replace(vetus, novum, 1)
    return textus[:initium] + pars + textus[finis:]


def adde_adiutores(textus: str) -> str:
    ancora = "FUNCTIO COMPONE_LITTERALE_TEXTUS REDDENS NUMERUS.\n"
    exige_unum(textus, ancora, "adiutores-textus")
    adiutores = '''FUNCTIO COMPONE_CONCATENA_TEXTUS REDDENS NUMERUS.
    ACCIPIT codex SICUT ORDO DE NUMERUS.
    ACCIPIT pos SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS pos.
    p = COMPONE_TRANSCRIBE(codex, p, 7, 0).
    p = COMPONE_TRANSCRIBE(codex, p, 6, 3).
    p = COMPONE_SUME_INDIRECTUM(codex, p, 8, 7).
    p = COMPONE_SUME_INDIRECTUM(codex, p, 9, 6).
    p = COMPONE_TRANSCRIBE(codex, p, 10, 8).
    p = COMPONE_ADD(codex, p, 10, 9).
    p = COMPONE_TRANSCRIBE(codex, p, 2, 10).
    p = COMPONE_ONERA(codex, p, 1, 17).
    p = COMPONE_ADD(codex, p, 2, 1).
    p = COMPONE_ONERA(codex, p, 1, 33554432).
    p = COMPONE_SUME_INDIRECTUM(codex, p, 0, 1).
    p = COMPONE_SERVA_INDIRECTUM(codex, p, 0, 2).
    p = COMPONE_TRANSCRIBE(codex, p, 3, 0).
    p = COMPONE_ONERA(codex, p, 1, 8).
    p = COMPONE_ADD(codex, p, 0, 1).
    p = COMPONE_IMPONE(codex, p, 0).
    p = COMPONE_TRANSCRIBE(codex, p, 0, 3).
    p = COMPONE_ONERA(codex, p, 1, 8).
    p = COMPONE_ADD(codex, p, 0, 1).
    p = COMPONE_ADD(codex, p, 0, 2).
    p = COMPONE_VERIFICA_TAS(codex, p).
    p = COMPONE_ONERA(codex, p, 1, 33554432).
    p = COMPONE_SERVA_INDIRECTUM(codex, p, 1, 0).
    p = COMPONE_AUFER(codex, p, 0).
    p = COMPONE_TRANSCRIBE(codex, p, 11, 0).
    p = COMPONE_SERVA_INDIRECTUM(codex, p, 11, 10).
    p = COMPONE_TRANSCRIBE(codex, p, 3, 11).
    p = COMPONE_ONERA(codex, p, 1, 8).
    p = COMPONE_ADD(codex, p, 3, 1).
    p = COMPONE_SERVA_INDIRECTUM(codex, p, 3, 10).
    p = COMPONE_ADD(codex, p, 3, 1).
    p = COMPONE_ONERA(codex, p, 1, 16).
    p = COMPONE_ADD(codex, p, 7, 1).
    p = COMPONE_ADD(codex, p, 6, 1).
    DECLARA a SICUT NUMERUS VALENS p.
    p = COMPONE_ONERA(codex, p, 2, 0).
    p = COMPONE_CMP(codex, p, 8, 2).
    DECLARA b SICUT NUMERUS VALENS 0.
    p = COMPONE_JE_FUTURUM(codex, p, SEDES(b)).
    p = COMPONE_MOVZX(codex, p, 0, 7).
    p = COMPONE_SERVA_OCTETUM(codex, p, 3, 0).
    p = COMPONE_ONERA(codex, p, 2, 1).
    p = COMPONE_ADD(codex, p, 7, 2).
    p = COMPONE_ADD(codex, p, 3, 2).
    p = COMPONE_SUB(codex, p, 8, 2).
    p = COMPONE_JMP_RETRO(codex, p, a).
    DECLARA c SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, b, p).
    DECLARA d SICUT NUMERUS VALENS p.
    p = COMPONE_ONERA(codex, p, 2, 0).
    p = COMPONE_CMP(codex, p, 9, 2).
    DECLARA e SICUT NUMERUS VALENS 0.
    p = COMPONE_JE_FUTURUM(codex, p, SEDES(e)).
    p = COMPONE_MOVZX(codex, p, 0, 6).
    p = COMPONE_SERVA_OCTETUM(codex, p, 3, 0).
    p = COMPONE_ONERA(codex, p, 2, 1).
    p = COMPONE_ADD(codex, p, 6, 2).
    p = COMPONE_ADD(codex, p, 3, 2).
    p = COMPONE_SUB(codex, p, 9, 2).
    p = COMPONE_JMP_RETRO(codex, p, d).
    c = CORRIGE_SALTUM(codex, e, p).
    p = COMPONE_ONERA(codex, p, 0, 0).
    p = COMPONE_SERVA_OCTETUM(codex, p, 3, 0).
    p = COMPONE_TRANSCRIBE(codex, p, 0, 11).
    REDDE p.
FIN-FUNCTIO.

FUNCTIO COMPONE_COMPARA_TEXTUS REDDENS NUMERUS.
    ACCIPIT codex SICUT ORDO DE NUMERUS.
    ACCIPIT pos SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS pos.
    DECLARA a SICUT NUMERUS VALENS 0.
    DECLARA b SICUT NUMERUS VALENS 0.
    DECLARA c SICUT NUMERUS VALENS 0.
    DECLARA d SICUT NUMERUS VALENS 0.
    p = COMPONE_TRANSCRIBE(codex, p, 7, 0).
    p = COMPONE_TRANSCRIBE(codex, p, 6, 3).
    p = COMPONE_SUME_INDIRECTUM(codex, p, 8, 7).
    p = COMPONE_SUME_INDIRECTUM(codex, p, 9, 6).
    p = COMPONE_ONERA(codex, p, 1, 16).
    p = COMPONE_ADD(codex, p, 7, 1).
    p = COMPONE_ADD(codex, p, 6, 1).
    DECLARA e SICUT NUMERUS VALENS p.
    p = COMPONE_ONERA(codex, p, 2, 0).
    p = COMPONE_CMP(codex, p, 8, 2).
    p = COMPONE_JE_FUTURUM(codex, p, SEDES(a)).
    p = COMPONE_CMP(codex, p, 9, 2).
    p = COMPONE_JE_FUTURUM(codex, p, SEDES(b)).
    p = COMPONE_MOVZX(codex, p, 0, 7).
    p = COMPONE_MOVZX(codex, p, 2, 6).
    p = COMPONE_CMP(codex, p, 0, 2).
    p = COMPONE_JNE_FUTURUM(codex, p, SEDES(c)).
    p = COMPONE_ONERA(codex, p, 2, 1).
    p = COMPONE_ADD(codex, p, 7, 2).
    p = COMPONE_ADD(codex, p, 6, 2).
    p = COMPONE_SUB(codex, p, 8, 2).
    p = COMPONE_SUB(codex, p, 9, 2).
    p = COMPONE_JMP_RETRO(codex, p, e).
    DECLARA f SICUT NUMERUS VALENS p.
    DECLARA g SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, a, f).
    g = CORRIGE_SALTUM(codex, b, f).
    p = COMPONE_TRANSCRIBE(codex, p, 0, 8).
    p = COMPONE_SUB(codex, p, 0, 9).
    p = COMPONE_JMP_FUTURUM(codex, p, SEDES(d)).
    g = CORRIGE_SALTUM(codex, c, p).
    p = COMPONE_SUB(codex, p, 0, 2).
    g = CORRIGE_SALTUM(codex, d, p).
    p = COMPONE_ONERA(codex, p, 2, 0).
    p = COMPONE_CMP(codex, p, 0, 2).
    REDDE p.
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
    novum = "                            ignoratum = ANALYSA_COMPARATIO(codex, pos_codicis, fons, pos_fontis, n, tabula).\n"
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
    pars = textus[initium:finis]
    numerus = pars.count("es_flot_cmp == 0 TUNC")
    if numerus != 4:
        raise SystemExit(f"ERRATUM: quattuor custodiae ordinis exspectatae sunt, inventae {numerus}")
    pars = pars.replace("es_flot_cmp == 0 TUNC", "es_flot_cmp != 1 TUNC")
    textus = textus[:initium] + pars + textus[finis:]

    VIA.write_text(textus, encoding="utf-8")
    print("RECTE: gradus IV TEXTUS applicatus est.")


if __name__ == "__main__":
    applica()
