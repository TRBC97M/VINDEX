#!/usr/bin/env python3
"""Canonem visualem JL-UX I contra mutationes fortuitas custodit."""
from __future__ import annotations

from pathlib import Path
import sys

RADIX = Path(__file__).resolve().parents[1]
DOC = RADIX / "documenta" / "sylvia"

FASCICULI = {
    "JL_UX_CANON_I.md",
    "JL_UX_PALETTA_I.md",
    "JL_UX_MATERIAE_I.md",
    "JL_UX_COMPONENTES_I.md",
    "JL_UX_VIA_OPERIS_I.md",
}

PALETTA = {
    "Graphite": "#1A1D20",
    "Cool Gray-Blue": "#4A6072",
    "Ivory": "#F2F4F7",
    "Silver": "#BFC7CF",
    "Aqua Light": "#BDEFF2",
    "Cyan Glow": "#00C6FF",
    "Laurel Green": "#68B17B",
    "Imperial Crimson": "#C43D3D",
    "Subtle Bronze": "#B58A54",
}

PRINCIPIA = ("Perspicuitas", "Imperium", "Continuitas")
GRADUS = (
    "P16-X",
    "P16-XI",
    "P16-XII",
    "P16-XIII",
    "P16-XIV",
    "P16-XV",
    "P16-XVI",
    "P16-XVII",
    "P16-XVIII",
)


def defice(nuntius: str) -> int:
    print(f"DEFECIT: {nuntius}", file=sys.stderr)
    return 1


def lege(nomen: str) -> str:
    via = DOC / nomen
    if not via.is_file():
        raise FileNotFoundError(nomen)
    return via.read_text(encoding="utf-8")


def principale() -> int:
    absentia = sorted(n for n in FASCICULI if not (DOC / n).is_file())
    if absentia:
        return defice("fasciculi canonici desunt: " + ", ".join(absentia))

    canon = lege("JL_UX_CANON_I.md")
    paletta = lege("JL_UX_PALETTA_I.md")
    via = lege("JL_UX_VIA_OPERIS_I.md")

    for principium in PRINCIPIA:
        if principium not in canon:
            return defice(f"principium canonicum deest: {principium}")

    if "framebuffer" not in canon.lower() or "QEMU/OVMF" not in canon:
        return defice("auctoritas framebuffer QEMU/OVMF in canone non invenitur")

    for nomen, hexadecimale in PALETTA.items():
        linea = f"| {nomen} | `{hexadecimale}` |"
        if linea not in paletta:
            return defice(f"color canonicus mutatus aut deest: {nomen} {hexadecimale}")

    for gradus in GRADUS:
        if gradus not in via:
            return defice(f"gradus viae operis deest: {gradus}")

    if "sleep" not in via.lower() or "guard" not in via.lower():
        return defice("lex contra moras auctas vel custodias debilitas deest")

    print("RECTE: canon JL-UX I, paletta et via operis integrae sunt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
