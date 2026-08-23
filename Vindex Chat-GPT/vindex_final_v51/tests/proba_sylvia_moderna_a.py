#!/usr/bin/env python3
"""Contractum Sylviarum Modernarum A in VINDEX puro verificat."""

from pathlib import Path
import re


RADIX = Path(__file__).resolve().parents[1]
MODULUS = RADIX / "systema" / "sylvia_moderna.vindex"
NUCLEUS = RADIX / "systema" / "nucleus.vindex"


def require(textus: str, fragmentum: str, nomen: str) -> None:
    if fragmentum not in textus:
        raise SystemExit(f"ERRATUM: {nomen} deest: {fragmentum}")


def main() -> None:
    modulus = MODULUS.read_text(encoding="utf-8")
    nucleus = NUCLEUS.read_text(encoding="utf-8")

    for fragmentum in (
        "FUNCTIO SYLVIA_MODERNA",
        "FUNCTIO SYLVIA_RECTANGULUM",
        "FUNCTIO SYLVIA_PROGRAMMATA",
        "FUNCTIO SYLVIA_TABULA",
        "FUNCTIO SYLVIA_CURSOREM_SALVA",
        "FUNCTIO SYLVIA_CLAVIS_ASCII",
        "CONTENTUM(50333728)",
        "CONTENTUM(50333736)",
        "50334720 + electa * 8",
        '"PROGRAMMATA"',
        '"TABULA"',
        '"JL-UX"',
    ):
        require(modulus, fragmentum, "contractus Sylviarum Modernarum A")

    require(nucleus, 'IMPORTA "systema/sylvia_moderna.vindex".', "importatio nuclei")
    require(
        nucleus,
        "SI CONTENTUM(50333696) == 1 TUNC REDDE SYLVIA_MODERNA(). FIN-SI.",
        "transitus UEFI ad Sylviam Modernam",
    )
    require(
        nucleus,
        "(status_muris[0] - minx) * (CONTENTUM(50333728) - 10) / dx",
        "coordinatae muris nativae",
    )
    if "SALVE" in modulus:
        raise SystemExit("ERRATUM: SALVE in PROGRAMMATA Moderna apparere potest")
    if re.search(r"\.(c|h|cc|cpp|cxx|S|s|asm|rs)\b", modulus):
        raise SystemExit("ERRATUM: modulus runtime non-VINDEX nominat")

    print("RECTE: Sylvia Moderna A est compositorium nativum VINDEX purum.")


if __name__ == "__main__":
    main()
