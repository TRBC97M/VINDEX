#!/usr/bin/env python3
"""VINDEX 0.53: septimum argumentum secundum ABI System V corrigit."""

from pathlib import Path


VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "SI numerus_argumentorum == 7 TUNC\n            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 10)."

VETUS_APPELLATIO = '''        SI numerus_argumentorum >= 6 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 9).
        FIN-SI.
        SI numerus_argumentorum >= 5 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 8).
        FIN-SI.
        SI numerus_argumentorum >= 4 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 1).
        FIN-SI.
        SI numerus_argumentorum >= 3 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 2).
        FIN-SI.
        SI numerus_argumentorum >= 2 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 6).
        FIN-SI.
        SI numerus_argumentorum >= 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 7).
        FIN-SI.
'''

NOVA_APPELLATIO = '''        SI numerus_argumentorum == 7 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 10).
        FIN-SI.
        SI numerus_argumentorum >= 6 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 9).
        FIN-SI.
        SI numerus_argumentorum >= 5 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 8).
        FIN-SI.
        SI numerus_argumentorum >= 4 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 1).
        FIN-SI.
        SI numerus_argumentorum >= 3 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 2).
        FIN-SI.
        SI numerus_argumentorum >= 2 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 6).
        FIN-SI.
        SI numerus_argumentorum >= 1 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 7).
        FIN-SI.
        SI numerus_argumentorum == 7 TUNC
            CONTENTUM(pos_codicis) = COMPONE_ONERA(codex, CONTENTUM(pos_codicis), 11, 0).
            CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 11).
            CONTENTUM(pos_codicis) = COMPONE_IMPONE(codex, CONTENTUM(pos_codicis), 10).
        FIN-SI.
'''

VETUS_POST_VOCATIONEM = '''        FIN-SI.
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 39 TUNC
'''

NOVUM_POST_VOCATIONEM = '''        FIN-SI.
        SI numerus_argumentorum == 7 TUNC
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 10).
            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 11).
        FIN-SI.
        REDDE 0.
    FIN-SI.

    SI fons[CONTENTUM(pos_fontis)] == 39 TUNC
'''

VETUS_PARAMETRUM = '''                        tabula[51] = tabula[51] - 8.
                        pos = COMPONE_SERVA_PILA(codex, pos, intervallum_param, registrum_param).

                        numerus_parametrorum = numerus_parametrorum + 1.
'''

NOVUM_PARAMETRUM = '''                        tabula[51] = tabula[51] - 8.
                        SI numerus_parametrorum == 6 TUNC
                            pos = COMPONE_SUME_PILA(codex, pos, 10, 16).
                            pos = COMPONE_SERVA_PILA(codex, pos, intervallum_param, 10).
                        ALITER
                            pos = COMPONE_SERVA_PILA(codex, pos, intervallum_param, registrum_param).
                        FIN-SI.

                        numerus_parametrorum = numerus_parametrorum + 1.
'''


def muta_unum(textus: str, vetus: str, novum: str, nomen: str) -> tuple[str, bool]:
    nv = textus.count(vetus)
    nn = textus.count(novum)
    if nv == 1 and nn == 0:
        return textus.replace(vetus, novum, 1), True
    if nv == 0 and nn == 1:
        return textus, False
    raise SystemExit(f"ERRATUM: mutatio {nomen} ambigua est (vetus={nv}, nova={nn})")


def principale() -> None:
    textus = VIA.read_text(encoding="utf-8")
    mutatum = False

    textus, m = muta_unum(textus, VETUS_APPELLATIO, NOVA_APPELLATIO, "appellatio")
    mutatum = mutatum or m
    textus, m = muta_unum(textus, VETUS_POST_VOCATIONEM, NOVUM_POST_VOCATIONEM, "mundatio")
    mutatum = mutatum or m
    textus, m = muta_unum(textus, VETUS_PARAMETRUM, NOVUM_PARAMETRUM, "parametrum")
    mutatum = mutatum or m

    if MARCA not in textus:
        raise SystemExit("ERRATUM: marca septimi argumenti post mutationem deest")

    VIA.write_text(textus, encoding="utf-8", newline="\n")
    if mutatum:
        print("RECTE: septimum argumentum secundum ABI System V correctum est.")
    else:
        print("RECTE: septimum argumentum iam correctum est.")


if __name__ == "__main__":
    principale()
