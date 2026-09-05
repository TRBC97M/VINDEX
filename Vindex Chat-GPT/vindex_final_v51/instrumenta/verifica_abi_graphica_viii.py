#!/usr/bin/env python3
"""Custodia ABI Graphica VIII/X: nulla functio plus quam VII argumenta accipit."""
from __future__ import annotations

import re
import sys
from pathlib import Path

RADIX = Path(__file__).resolve().parents[1]
ARCHIVA = [
    RADIX / "bibliotheca/fenestrale_graphica_viii.vindex",
    RADIX / "bibliotheca/fenestrale_graphica_viii_superficies.vindex",
    RADIX / "bibliotheca/fenestrale_interpolatio_viii.vindex",
    RADIX / "bibliotheca/fenestrale_damage_viii.vindex",
    RADIX / "bibliotheca/fenestrale_typographia_viii.vindex",
    RADIX / "bibliotheca/fenestrale_coda_graphica.vindex",
    RADIX / "bibliotheca/fenestrale_commandos_viii.vindex",
    RADIX / "bibliotheca/fenestrale_backend_x.vindex",
]
LIMEN = 7
FUNCTIO = re.compile(r"\bFUNCTIO\s+([A-Z0-9_]+)\b(.*?)\bFIN-FUNCTIO\.", re.S)
ACCIPIT = re.compile(r"\bACCIPIT\b")


def principale() -> int:
    errata: list[str] = []
    numerus = 0
    for via in ARCHIVA:
        if not via.exists():
            errata.append(f"deest: {via.relative_to(RADIX)}")
            continue
        textus = via.read_text(encoding="utf-8")
        inventae = list(FUNCTIO.finditer(textus))
        if not inventae:
            errata.append(f"nulla functio inventa: {via.relative_to(RADIX)}")
            continue
        for m in inventae:
            numerus += 1
            nomen = m.group(1)
            argc = len(ACCIPIT.findall(m.group(2)))
            if argc > LIMEN:
                errata.append(
                    f"{via.relative_to(RADIX)}: {nomen} accipit {argc} argumenta; limen ABI est {LIMEN}"
                )
    if errata:
        for e in errata:
            print(f"DEFECIT: {e}", file=sys.stderr)
        return 1
    print(f"RECTE: {numerus} functiones Graphica VIII/X limen ABI <= {LIMEN} servant.")
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
