#!/usr/bin/env python3
"""Corpus COMPONE_RESERVA_OCTETA gradatim compilat ut vitium auto-hospitii locetur."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

RADIX = Path("Vindex Chat-GPT/vindex_final_v51")
FONS = RADIX / "src/compilator_vindex.vindex"
COMPILATOR = RADIX / "compilator_vindex"
ANCORA = "FUNCTIO ANALYSA_FACTOR REDDENS NUMERUS.\n"

CAPUT = """FUNCTIO COMPONE_RESERVA_OCTETA REDDENS NUMERUS.
    ACCIPIT codex SICUT ORDO DE NUMERUS.
    ACCIPIT pos SICUT NUMERUS.
"""

GRADUS = [
    [],
    ["    DECLARA p_mem SICUT NUMERUS VALENS pos."],
    [
        "    DECLARA p_mem SICUT NUMERUS VALENS pos.",
        "    p_mem = COMPONE_TRANSCRIBE(codex, p_mem, 6, 0).",
    ],
    [
        "    DECLARA p_mem SICUT NUMERUS VALENS pos.",
        "    p_mem = COMPONE_TRANSCRIBE(codex, p_mem, 6, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 7, 0).",
    ],
    [
        "    DECLARA p_mem SICUT NUMERUS VALENS pos.",
        "    p_mem = COMPONE_TRANSCRIBE(codex, p_mem, 6, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 7, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 2, 3).",
    ],
    [
        "    DECLARA p_mem SICUT NUMERUS VALENS pos.",
        "    p_mem = COMPONE_TRANSCRIBE(codex, p_mem, 6, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 7, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 2, 3).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 10, 34).",
    ],
    [
        "    DECLARA p_mem SICUT NUMERUS VALENS pos.",
        "    p_mem = COMPONE_TRANSCRIBE(codex, p_mem, 6, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 7, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 2, 3).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 10, 34).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 8, 0).",
    ],
    [
        "    DECLARA p_mem SICUT NUMERUS VALENS pos.",
        "    p_mem = COMPONE_TRANSCRIBE(codex, p_mem, 6, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 7, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 2, 3).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 10, 34).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 8, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 9, 0).",
    ],
    [
        "    DECLARA p_mem SICUT NUMERUS VALENS pos.",
        "    p_mem = COMPONE_TRANSCRIBE(codex, p_mem, 6, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 7, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 2, 3).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 10, 34).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 8, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 9, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 0, 9).",
    ],
    [
        "    DECLARA p_mem SICUT NUMERUS VALENS pos.",
        "    p_mem = COMPONE_TRANSCRIBE(codex, p_mem, 6, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 7, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 2, 3).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 10, 34).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 8, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 9, 0).",
        "    p_mem = COMPONE_ONERA(codex, p_mem, 0, 9).",
        "    p_mem = COMPONE_VOCA_NUCLEUM(codex, p_mem).",
    ],
]


def corpus(lines: list[str]) -> str:
    nomen_reddendum = "p_mem" if lines else "pos"
    media = "\n".join(lines)
    if media:
        media += "\n"
    return CAPUT + media + f"    REDDE {nomen_reddendum}.\nFIN-FUNCTIO.\n\n"


def main() -> None:
    textus = FONS.read_text(encoding="utf-8")
    if "FUNCTIO COMPONE_RESERVA_OCTETA REDDENS NUMERUS." in textus:
        raise SystemExit("ERRATUM: diagnostica fontem iam mutatum accepit")
    if textus.count(ANCORA) != 1:
        raise SystemExit("ERRATUM: ancora ANALYSA_FACTOR non unica est")

    with tempfile.TemporaryDirectory(prefix="vindex-053-memoria-") as directorium:
        d = Path(directorium)
        for index, lineae in enumerate(GRADUS):
            fons_varians = d / f"gradus-{index}.vindex"
            exitus = d / f"gradus-{index}"
            fons_varians.write_text(textus.replace(ANCORA, corpus(lineae) + ANCORA, 1), encoding="utf-8")
            effectus = subprocess.run(
                [str(COMPILATOR), str(fons_varians), str(exitus)],
                cwd=RADIX.parent.parent.parent,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                check=False,
            )
            print(f"DIAGNOSTICUM CORPUS {index}: status={effectus.returncode}.")
            if effectus.stdout.strip():
                print(effectus.stdout.rstrip())


if __name__ == "__main__":
    main()
