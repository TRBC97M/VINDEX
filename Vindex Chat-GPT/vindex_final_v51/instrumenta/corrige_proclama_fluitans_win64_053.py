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


VETUS_STDOUT = """FUNCTIO COMPONE_SCRIBE_STDOUT_DYNAMICA REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    ACCIPIT longitudo SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS pos.
    p = COMPONE_ONERA(codex, p, 2, longitudo).
    SI MODUS_PE_LEGE(contextus_parseris) == 1 TUNC
        p = COMPONE_TRANSCRIBE(codex, p, 8, 2).
        p = COMPONE_TRANSCRIBE(codex, p, 2, 6).
        CODEX_SCRIBE(codex, p, 72).
        CODEX_SCRIBE(codex, p + 1, 131).
        CODEX_SCRIBE(codex, p + 2, 236).
        CODEX_SCRIBE(codex, p + 3, 40).
        p = p + 4.
        p = COMPONE_ONERA(codex, p, 0, 16777216).
        p = COMPONE_SUME_INDIRECTUM(codex, p, 1, 0).
        CODEX_SCRIBE(codex, p, 76).
        CODEX_SCRIBE(codex, p + 1, 141).
        CODEX_SCRIBE(codex, p + 2, 76).
        CODEX_SCRIBE(codex, p + 3, 36).
        CODEX_SCRIBE(codex, p + 4, 24).
        p = p + 5.
        CODEX_SCRIBE(codex, p, 72).
        CODEX_SCRIBE(codex, p + 1, 199).
        CODEX_SCRIBE(codex, p + 2, 68).
        CODEX_SCRIBE(codex, p + 3, 36).
        CODEX_SCRIBE(codex, p + 4, 32).
        CODEX_SCRIBE(codex, p + 5, 0).
        CODEX_SCRIBE(codex, p + 6, 0).
        CODEX_SCRIBE(codex, p + 7, 0).
        CODEX_SCRIBE(codex, p + 8, 0).
        p = p + 9.
        p = COMPONE_VOCA_IAT_DYNAMICA(codex, p, contextus_parseris, 3).
        CODEX_SCRIBE(codex, p, 72).
        CODEX_SCRIBE(codex, p + 1, 131).
        CODEX_SCRIBE(codex, p + 2, 196).
        CODEX_SCRIBE(codex, p + 3, 40).
        p = p + 4.
    ALITER
        p = COMPONE_ONERA(codex, p, 0, 1).
        p = COMPONE_ONERA(codex, p, 7, 1).
        p = COMPONE_VOCA_NUCLEUM(codex, p).
    FIN-SI.
    REDDE p.
FIN-FUNCTIO."""

NOVUM_STDOUT = """FUNCTIO COMPONE_SCRIBE_STDOUT_DYNAMICA REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT pos SICUT NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    ACCIPIT longitudo SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS pos.
    p = COMPONE_ONERA(codex, p, 2, longitudo).
    SI MODUS_PE_LEGE(contextus_parseris) == 1 TUNC
        p = COMPONE_TRANSCRIBE(codex, p, 8, 2).
        p = COMPONE_TRANSCRIBE(codex, p, 2, 6).
        // R14 est non-volatilis in Win64. Eum servamus antequam RSP ad XVI ordinem redigitur.
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
        p = p + 4.
        p = COMPONE_ONERA(codex, p, 0, 16777216).
        p = COMPONE_SUME_INDIRECTUM(codex, p, 1, 0).
        CODEX_SCRIBE(codex, p, 76).
        CODEX_SCRIBE(codex, p + 1, 141).
        CODEX_SCRIBE(codex, p + 2, 76).
        CODEX_SCRIBE(codex, p + 3, 36).
        CODEX_SCRIBE(codex, p + 4, 40).
        p = p + 5.
        CODEX_SCRIBE(codex, p, 72).
        CODEX_SCRIBE(codex, p + 1, 199).
        CODEX_SCRIBE(codex, p + 2, 68).
        CODEX_SCRIBE(codex, p + 3, 36).
        CODEX_SCRIBE(codex, p + 4, 32).
        CODEX_SCRIBE(codex, p + 5, 0).
        CODEX_SCRIBE(codex, p + 6, 0).
        CODEX_SCRIBE(codex, p + 7, 0).
        CODEX_SCRIBE(codex, p + 8, 0).
        p = p + 9.
        p = COMPONE_VOCA_IAT_DYNAMICA(codex, p, contextus_parseris, 3).
        CODEX_SCRIBE(codex, p, 76).
        CODEX_SCRIBE(codex, p + 1, 137).
        CODEX_SCRIBE(codex, p + 2, 244).
        p = p + 3.
        CODEX_SCRIBE(codex, p, 65).
        CODEX_SCRIBE(codex, p + 1, 94).
        p = p + 2.
    ALITER
        p = COMPONE_ONERA(codex, p, 0, 1).
        p = COMPONE_ONERA(codex, p, 7, 1).
        p = COMPONE_VOCA_NUCLEUM(codex, p).
    FIN-SI.
    REDDE p.
FIN-FUNCTIO."""


def transforma(textus: str) -> str:
    if "p = COMPONE_TRANSCRIBE(codex, p, 15, 0)." in textus and "CODEX_SCRIBE(codex, p + 2, 244)." in textus:
        return textus

    textus = unum(textus, VETUS_STDOUT, NOVUM_STDOUT, "COMPONE_SCRIBE_STDOUT_DYNAMICA")

    textus = unum(
        textus,
        """    DECLARA pos_post_flot_sign SICUT NUMERUS VALENS p.
    DECLARA ig_fps SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_flot_pos, pos_post_flot_sign).

    p = COMPONE_MOVQ_A_XMM(codex, p, 0, 0).""",
        """    DECLARA pos_post_flot_sign SICUT NUMERUS VALENS p.
    DECLARA ig_fps SICUT NUMERUS VALENS CORRIGE_SALTUM(codex, loci_flot_pos, pos_post_flot_sign).

    // WriteFile potest XMM0..XMM5 delere. Bits valoris in R15 (non-volatili Win64) servantur.
    p = COMPONE_TRANSCRIBE(codex, p, 15, 0).
    p = COMPONE_MOVQ_A_XMM(codex, p, 0, 0).""",
        "servationis fluitantis",
    )

    textus = unum(
        textus,
        """    p = COMPONE_AUFER(codex, p, 0).

    p = COMPONE_CVTSI2SD(codex, p, 1, 0).
    p = COMPONE_SUBSD(codex, p, 0, 1).""",
        """    p = COMPONE_AUFER(codex, p, 0).

    p = COMPONE_CVTSI2SD(codex, p, 1, 0).
    p = COMPONE_MOVQ_A_XMM(codex, p, 0, 15).
    p = COMPONE_SUBSD(codex, p, 0, 1).""",
        "restitutionis XMM0",
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
