#!/usr/bin/env python3
"""Fontem compilatoris ad ingressum Win64 diagnosticum in fasciculo temporario corrigit."""

from __future__ import annotations

import argparse
from pathlib import Path


VETUS_INITIUM = """                punctum_ingressus = pos.\n                pos = COMPONE_AUFER(codex, pos, 0).\n                pos = COMPONE_TRANSCRIBE(codex, pos, 6, 4).\n                pos = COMPONE_TRANSCRIBE(codex, pos, 7, 0).\n                SI modus_pe == 1 TUNC\n                    CODEX_SCRIBE(codex, pos, 72).\n                    CODEX_SCRIBE(codex, pos + 1, 131).\n                    CODEX_SCRIBE(codex, pos + 2, 236).\n                    CODEX_SCRIBE(codex, pos + 3, 40).\n                    pos = pos + 4.\n"""

NOVUM_INITIUM = """                punctum_ingressus = pos.\n                SI modus_pe == 1 TUNC\n                    // Ingressus Windows non habet pilam argc/argv Linux.\n                    // RSP in ingressu est 8 modulo 16; subtractio 0x28 ante CALL eum ordinat.\n                    CODEX_SCRIBE(codex, pos, 72).\n                    CODEX_SCRIBE(codex, pos + 1, 131).\n                    CODEX_SCRIBE(codex, pos + 2, 236).\n                    CODEX_SCRIBE(codex, pos + 3, 40).\n                    pos = pos + 4.\n                    pos = COMPONE_ONERA(codex, pos, 7, 0).\n                    pos = COMPONE_ONERA(codex, pos, 6, 0).\n"""

VETUS_ALITER = """                ALITER\n                    pos = COMPONE_ONERA(codex, pos, 2, 33554432).\n                    pos = COMPONE_ONERA(codex, pos, 0, 33554448).\n                    pos = COMPONE_SERVA_INDIRECTUM(codex, pos, 2, 0).\n                FIN-SI.\n"""

NOVUM_ALITER = """                ALITER\n                    // Ingressus ELF retinet conventionem pilae Linux argc/argv.\n                    pos = COMPONE_AUFER(codex, pos, 0).\n                    pos = COMPONE_TRANSCRIBE(codex, pos, 6, 4).\n                    pos = COMPONE_TRANSCRIBE(codex, pos, 7, 0).\n                    pos = COMPONE_ONERA(codex, pos, 2, 33554432).\n                    pos = COMPONE_ONERA(codex, pos, 0, 33554448).\n                    pos = COMPONE_SERVA_INDIRECTUM(codex, pos, 2, 0).\n                FIN-SI.\n"""


def substitue_unum(textus: str, vetus: str, novum: str, nomen: str) -> str:
    numerus = textus.count(vetus)
    if numerus != 1:
        raise SystemExit(
            f"ERRATUM: segmentum {nomen} {numerus} vicibus inventum est; 1 exspectabatur"
        )
    return textus.replace(vetus, novum, 1)


def principale() -> int:
    parser = argparse.ArgumentParser(
        description="Ingressum PE Win64 diagnosticum in fonte temporario corrigit."
    )
    parser.add_argument("fons", type=Path)
    parser.add_argument("exitus", type=Path)
    args = parser.parse_args()

    textus = args.fons.read_text(encoding="utf-8")
    textus = substitue_unum(textus, VETUS_INITIUM, NOVUM_INITIUM, "initii")
    textus = substitue_unum(textus, VETUS_ALITER, NOVUM_ALITER, "rami ELF")
    args.exitus.write_text(textus, encoding="utf-8", newline="\n")
    print(f"RECTE: ingressus Win64 diagnosticus scriptus est: {args.exitus}")
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
