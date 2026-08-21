#!/usr/bin/env python3
"""Defectus notos compilatoris 0.51 ante generationem binarii detegit."""

from __future__ import annotations

import re
import sys
from pathlib import Path

PRAECEPTA_VARIABILIUM = (
    re.compile(r"\bDECLARA\s+([A-Za-z_][A-Za-z_0-9]*)\b"),
    re.compile(r"\bACCIPIT\s+([A-Za-z_][A-Za-z_0-9]*)\b"),
    re.compile(r"\bPER\s+([A-Za-z_][A-Za-z_0-9]*)\s+AB\b"),
)


def sine_literalibus(linea: str) -> str:
    characteres = list(linea)
    clausura: str | None = None
    i = 0
    while i < len(characteres):
        ch = characteres[i]
        if clausura is None:
            if ch in {'"', "'"}:
                clausura = ch
                characteres[i] = " "
        else:
            characteres[i] = " "
            if ch == clausura:
                clausura = None
        i += 1
    return "".join(characteres)


def est_maiusculus(nomen: str) -> bool:
    litterae = [ch for ch in nomen if ch.isalpha()]
    return bool(litterae) and all("A" <= ch <= "Z" for ch in litterae)


def principale() -> int:
    if len(sys.argv) != 2:
        print("USUS: vindex_tutela_052.py <fons.vindex>", file=sys.stderr)
        return 64

    via = Path(sys.argv[1])
    try:
        lineae = via.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as erratum:
        print(f"ERRATUM: fons examinari non potest: {erratum}", file=sys.stderr)
        return 66

    errata = 0
    for numerus, originalis in enumerate(lineae, start=1):
        linea = sine_literalibus(originalis)
        for regula in PRAECEPTA_VARIABILIUM:
            inventum = regula.search(linea)
            if inventum is None:
                continue
            nomen = inventum.group(1)
            if est_maiusculus(nomen):
                columna = inventum.start(1) + 1
                print(
                    f"{via}:{numerus}:{columna}: erratum: identificator variabilis "
                    f"'{nomen}' totus maiusculus in compilatore nativo 0.51 instabilis est; "
                    "litteris minusculis utere donec correctio nativa perficiatur",
                    file=sys.stderr,
                )
                errata += 1

    if errata:
        print(f"VINDEX: {errata} defectus notus interceptus; compilator non vocatur.", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
