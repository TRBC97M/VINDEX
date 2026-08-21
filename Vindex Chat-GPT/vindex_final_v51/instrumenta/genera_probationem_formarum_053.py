#!/usr/bin/env python3
"""Probationem VINDEX cum XL formis et LXXX campis generat."""

from pathlib import Path
import sys


def genera(via: Path) -> None:
    lineae: list[str] = []
    for i in range(40):
        lineae.extend(
            [
                f"FORMA Forma{i}.",
                "    CAMPUS valor SICUT NUMERUS.",
                "FIN-FORMA.",
                "",
            ]
        )

    lineae.append("FORMA Magna.")
    for i in range(80):
        lineae.append(f"    CAMPUS c{i} SICUT NUMERUS.")
    lineae.extend(
        [
            "FIN-FORMA.",
            "",
            "FUNCTIO PRINCIPALIS REDDENS NUMERUS.",
            "    DECLARA ultima SICUT Forma39.",
            "    valor DE ultima = 39.",
            "    PROCLAMA valor DE ultima.",
            "    DECLARA magna SICUT Magna.",
            "    c79 DE magna = 777.",
            "    PROCLAMA c79 DE magna.",
            "    REDDE 0.",
            "FIN-FUNCTIO.",
            "",
        ]
    )
    via.write_text("\n".join(lineae), encoding="utf-8")


if __name__ == "__main__":
    destinatio = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/formae_magnae_053.vindex")
    genera(destinatio)
    print(f"RECTE: probatio formarum scripta est: {destinatio}")
