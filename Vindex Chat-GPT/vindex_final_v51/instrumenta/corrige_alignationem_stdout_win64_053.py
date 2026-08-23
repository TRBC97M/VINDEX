#!/usr/bin/env python3
"""WriteFile in PROCLAMA ad RSP XVI-alineatum independentem a pila VINDEX redigit."""

from __future__ import annotations

import argparse
from pathlib import Path


def unum(textus: str, vetus: str, novum: str, nomen: str) -> str:
    n = textus.count(vetus)
    if n != 1:
        raise SystemExit(f"ERRATUM: {n} segmenta {nomen}; 1 exspectabatur")
    return textus.replace(vetus, novum, 1)


def transforma(textus: str) -> str:
    # Correctio XMM0/R15 iam in ramo Claudii est. Hoc instrumentum
    # tantum vocationem WriteFile contra quamlibet paritatem pilae munit.
    robustus = """        CODEX_SCRIBE(codex, p, 65).
        CODEX_SCRIBE(codex, p + 1, 86)."""
    if robustus in textus and "CODEX_SCRIBE(codex, p + 2, 244)." in textus:
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
    return textus


def principale() -> int:
    p = argparse.ArgumentParser(description="Alignationem WriteFile Win64 VINDEX 0.53 corrigit.")
    p.add_argument("fons", type=Path)
    p.add_argument("exitus", nargs="?", type=Path)
    args = p.parse_args()
    exitus = args.exitus or args.fons
    textus = args.fons.read_text(encoding="utf-8")
    exitus.write_text(transforma(textus), encoding="utf-8", newline="\n")
    print(f"RECTE: WriteFile ad pilam XVI-alineatam robustam redactus est: {exitus}")
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
