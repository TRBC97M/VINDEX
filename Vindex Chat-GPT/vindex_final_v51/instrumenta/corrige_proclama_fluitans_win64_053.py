#!/usr/bin/env python3
"""PROCLAMA fluitans Win64: XMM volatile servat et WriteFile robuste aliniat."""

from __future__ import annotations

import argparse
from pathlib import Path


def unum(textus: str, vetus: str, novum: str, nomen: str) -> str:
    n = textus.count(vetus)
    if n != 1:
        raise SystemExit(f"ERRATUM: {n} segmenta {nomen}; 1 exspectabatur")
    return textus.replace(vetus, novum, 1)


def transforma(textus: str) -> str:
    if "p = COMPONE_IMPONE(codex, p, 0).\n    p = COMPONE_MOVQ_A_XMM(codex, p, 0, 0)." in textus and "CODEX_SCRIBE(codex, p + 2, 244)." in textus:
        return textus

    textus = unum(
        textus,
        """        p = COMPONE_TRANSCRIBE(codex, p, 8, 2).
        p = COMPONE_TRANSCRIBE(codex, p, 2, 6).
        CODEX_SCRIBE(codex, p, 72).
        CODEX_SCRIBE(codex, p + 1, 131).
        CODEX_SCRIBE(codex, p + 2, 236).
        CODEX_SCRIBE(codex, p + 3, 48).
        p = p + 4.""",
        """        p = COMPONE_TRANSCRIBE(codex, p, 8, 2).
        p = COMPONE_TRANSCRIBE(codex, p, 2, 6).
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
        p = p + 4.""",
        "prologi WriteFile robusti",
    )

    textus = unum(
        textus,
        """        p = COMPONE_VOCA_IAT_DYNAMICA(codex, p, contextus_parseris, 3).
        CODEX_SCRIBE(codex, p, 72).
        CODEX_SCRIBE(codex, p + 1, 131).
        CODEX_SCRIBE(codex, p + 2, 196).
        CODEX_SCRIBE(codex, p + 3, 48).
        p = p + 4.""",
        """        p = COMPONE_VOCA_IAT_DYNAMICA(codex, p, contextus_parseris, 3).
        CODEX_SCRIBE(codex, p, 76).
        CODEX_SCRIBE(codex, p + 1, 137).
        CODEX_SCRIBE(codex, p + 2, 244).
        p = p + 3.
        CODEX_SCRIBE(codex, p, 65).
        CODEX_SCRIBE(codex, p + 1, 94).
        p = p + 2.""",
        "epilogi WriteFile robusti",
    )

    # WriteFile potest XMM0..XMM5 delere. Bits fluitantis in pila
    # servantur. Helper RSP post API exacte restituit, ergo valor
    # manet sub ELF et Win64 sine registro speciali.
    textus = unum(
        textus,
        """    DECLARA pos_post_flot_sign SICUT NUMERUS VALENS p.
    DECLARA ig_fps SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_flot_pos, pos_post_flot_sign).

    p = COMPONE_MOVQ_A_XMM(codex, p, 0, 0).""",
        """    DECLARA pos_post_flot_sign SICUT NUMERUS VALENS p.
    DECLARA ig_fps SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_flot_pos, pos_post_flot_sign).

    p = COMPONE_IMPONE(codex, p, 0).
    p = COMPONE_MOVQ_A_XMM(codex, p, 0, 0).""",
        "servationis fluitantis in pila",
    )

    textus = unum(
        textus,
        """    p = COMPONE_AUFER(codex, p, 0).

    p = COMPONE_CVTSI2SD(codex, p, 1, 0).
    p = COMPONE_SUBSD(codex, p, 0, 1).""",
        """    p = COMPONE_AUFER(codex, p, 0).

    p = COMPONE_CVTSI2SD(codex, p, 1, 0).
    p = COMPONE_AUFER(codex, p, 0).
    p = COMPONE_MOVQ_A_XMM(codex, p, 0, 0).
    p = COMPONE_SUBSD(codex, p, 0, 1).""",
        "restitutionis XMM0 ex pila",
    )
    return textus


def principale() -> int:
    p = argparse.ArgumentParser(description="PROCLAMA fluitans Win64 VINDEX 0.53 corrigit.")
    p.add_argument("fons", type=Path)
    p.add_argument("exitus", nargs="?", type=Path)
    args = p.parse_args()
    exitus = args.exitus or args.fons
    textus = args.fons.read_text(encoding="utf-8")
    exitus.write_text(transforma(textus), encoding="utf-8", newline="\n")
    print(f"RECTE: PROCLAMA fluitans Win64 correctum est: {exitus}")
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
