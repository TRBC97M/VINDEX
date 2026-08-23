#!/usr/bin/env python3
"""PROCLAMA numericum Win64 corrigit in fonte temporario VINDEX 0.53."""

from __future__ import annotations

import argparse
from pathlib import Path


def unum(textus: str, vetus: str, novum: str, nomen: str) -> str:
    n = textus.count(vetus)
    if n != 1:
        raise SystemExit(f"ERRATUM: {n} segmenta {nomen}; 1 exspectabatur")
    return textus.replace(vetus, novum, 1)


def transforma(textus: str) -> str:
    nota = "ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    DECLARA p SICUT NUMERUS VALENS pos."
    caput_num = """FUNCTIO COMPONE_IMPRIME_NUMERUS REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT intervallum_scratch SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS pos."""
    if caput_num not in textus and nota in textus:
        return textus

    textus = unum(
        textus,
        caput_num,
        """FUNCTIO COMPONE_IMPRIME_NUMERUS REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT intervallum_scratch SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    DECLARA p SICUT NUMERUS VALENS pos.""",
        "capitis COMPONE_IMPRIME_NUMERUS",
    )

    textus = unum(
        textus,
        """FUNCTIO COMPONE_IMPRIME_CHAR REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT intervallum_scratch SICUT NUMERUS.
    ACCIPIT caracter SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS pos.""",
        """FUNCTIO COMPONE_IMPRIME_CHAR REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT intervallum_scratch SICUT NUMERUS.
    ACCIPIT caracter SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    DECLARA p SICUT NUMERUS VALENS pos.""",
        "capitis COMPONE_IMPRIME_CHAR",
    )

    textus = unum(
        textus,
        """FUNCTIO COMPONE_IMPRIME_PADEADO REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT intervallum_scratch SICUT NUMERUS.
    ACCIPIT ancho SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS pos.""",
        """FUNCTIO COMPONE_IMPRIME_PADEADO REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT intervallum_scratch SICUT NUMERUS.
    ACCIPIT ancho SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    DECLARA p SICUT NUMERUS VALENS pos.""",
        "capitis COMPONE_IMPRIME_PADEADO",
    )

    textus = unum(
        textus,
        """FUNCTIO COMPONE_IMPRIME_FLUITANIS REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT intervallum_scratch SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS pos.""",
        """FUNCTIO COMPONE_IMPRIME_FLUITANIS REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT intervallum_scratch SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    DECLARA p SICUT NUMERUS VALENS pos.""",
        "capitis COMPONE_IMPRIME_FLUITANIS",
    )

    mutationes = {
        "p = COMPONE_IMPRIME_CHAR(codex, p, intervallum_scratch, 45).":
            "p = COMPONE_IMPRIME_CHAR(codex, p, intervallum_scratch, 45, contextus_parseris).",
        "p = COMPONE_IMPRIME_NUMERUS(codex, p, intervallum_scratch).":
            "p = COMPONE_IMPRIME_NUMERUS(codex, p, intervallum_scratch, contextus_parseris).",
        "p = COMPONE_IMPRIME_CHAR(codex, p, intervallum_scratch, 46).":
            "p = COMPONE_IMPRIME_CHAR(codex, p, intervallum_scratch, 46, contextus_parseris).",
        "p = COMPONE_IMPRIME_PADEADO(codex, p, intervallum_scratch, 6).":
            "p = COMPONE_IMPRIME_PADEADO(codex, p, intervallum_scratch, 6, contextus_parseris).",
        "CONTENTUM(pos_codicis) = COMPONE_IMPRIME_FLUITANIS(codex, CONTENTUM(pos_codicis), intervallum_scratch).":
            "CONTENTUM(pos_codicis) = COMPONE_IMPRIME_FLUITANIS(codex, CONTENTUM(pos_codicis), intervallum_scratch, contextus_parseris).",
        "CONTENTUM(pos_codicis) = COMPONE_IMPRIME_NUMERUS(codex, CONTENTUM(pos_codicis), intervallum_scratch).":
            "CONTENTUM(pos_codicis) = COMPONE_IMPRIME_NUMERUS(codex, CONTENTUM(pos_codicis), intervallum_scratch, contextus_parseris).",
    }
    for vetus, novum in mutationes.items():
        textus = unum(textus, vetus, novum, vetus.split("(")[0].strip())

    vetus_prologus = """        p = COMPONE_TRANSCRIBE(codex, p, 12, 2).
        p = COMPONE_TRANSCRIBE(codex, p, 13, 6).
        CODEX_SCRIBE(codex, p, 72).
        CODEX_SCRIBE(codex, p + 1, 131).
        CODEX_SCRIBE(codex, p + 2, 236).
        CODEX_SCRIBE(codex, p + 3, 40).
        p = p + 4."""
    novus_prologus = """        p = COMPONE_TRANSCRIBE(codex, p, 12, 2).
        p = COMPONE_TRANSCRIBE(codex, p, 13, 6).
        CODEX_SCRIBE(codex, p, 65).
        CODEX_SCRIBE(codex, p + 1, 86).
        p = p + 2.
        CODEX_SCRIBE(codex, p, 73).
        CODEX_SCRIBE(codex, p + 1, 137).
        CODEX_SCRIBE(codex, p + 2, 230).
        p = p + 3.
        CODEX_SCRIBE(codex, p, 72).
        CODEX_SCRIBE(codex, p + 1, 131).
        CODEX_SCRIBE(codex, p + 2, 228).
        CODEX_SCRIBE(codex, p + 3, 240).
        p = p + 4.
        CODEX_SCRIBE(codex, p, 72).
        CODEX_SCRIBE(codex, p + 1, 131).
        CODEX_SCRIBE(codex, p + 2, 236).
        CODEX_SCRIBE(codex, p + 3, 48).
        p = p + 4."""
    textus = unum(textus, vetus_prologus, novus_prologus, "prologi WriteFile")

    textus = unum(
        textus,
        """        CODEX_SCRIBE(codex, p, 76).
        CODEX_SCRIBE(codex, p + 1, 141).
        CODEX_SCRIBE(codex, p + 2, 76).
        CODEX_SCRIBE(codex, p + 3, 36).
        CODEX_SCRIBE(codex, p + 4, 24).""",
        """        CODEX_SCRIBE(codex, p, 76).
        CODEX_SCRIBE(codex, p + 1, 141).
        CODEX_SCRIBE(codex, p + 2, 76).
        CODEX_SCRIBE(codex, p + 3, 36).
        CODEX_SCRIBE(codex, p + 4, 40).""",
        "sedis lpNumberOfBytesWritten",
    )

    vetus_epilogus = """        p = COMPONE_VOCA_IAT_DYNAMICA(codex, p, contextus_parseris, 3).
        CODEX_SCRIBE(codex, p, 72).
        CODEX_SCRIBE(codex, p + 1, 131).
        CODEX_SCRIBE(codex, p + 2, 196).
        CODEX_SCRIBE(codex, p + 3, 40).
        p = p + 4."""
    novus_epilogus = """        p = COMPONE_VOCA_IAT_DYNAMICA(codex, p, contextus_parseris, 3).
        CODEX_SCRIBE(codex, p, 76).
        CODEX_SCRIBE(codex, p + 1, 137).
        CODEX_SCRIBE(codex, p + 2, 244).
        p = p + 3.
        CODEX_SCRIBE(codex, p, 65).
        CODEX_SCRIBE(codex, p + 1, 94).
        p = p + 2."""
    textus = unum(textus, vetus_epilogus, novus_epilogus, "epilogi WriteFile")

    return textus


def principale() -> int:
    parser = argparse.ArgumentParser(description="PROCLAMA numericum Win64 VINDEX 0.53 corrigit.")
    parser.add_argument("fons", type=Path)
    parser.add_argument("exitus", type=Path)
    args = parser.parse_args()
    textus = args.fons.read_text(encoding="utf-8")
    args.exitus.write_text(transforma(textus), encoding="utf-8", newline="\n")
    print(f"RECTE: PROCLAMA numericum Win64 correctum est: {args.exitus}")
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
