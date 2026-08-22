#!/usr/bin/env python3
"""Probationem VINDEX cum XL formis et LXXX campis generat."""

from pathlib import Path
import sys


def suffixum_litterarum(index: int) -> str:
    """Indicem non negativum ad suffixum alphabeticum sine cifris convertit."""
    partes: list[str] = []
    valor = index + 1
    while valor > 0:
        valor, reliquum = divmod(valor - 1, 26)
        partes.append(chr(ord("A") + reliquum))
    return "".join(reversed(partes))


def genera(via: Path) -> None:
    lineae: list[str] = []
    nomina_formarum: list[str] = []
    for i in range(40):
        nomen_formae = f"Forma{suffixum_litterarum(i)}"
        nomina_formarum.append(nomen_formae)
        lineae.extend(
            [
                f"FORMA {nomen_formae}.",
                "    CAMPUS valor SICUT NUMERUS.",
                "FIN-FORMA.",
                "",
            ]
        )

    lineae.append("FORMA Magna.")
    nomina_camporum: list[str] = []
    for i in range(80):
        nomen_campi = f"campus{suffixum_litterarum(i)}"
        nomina_camporum.append(nomen_campi)
        lineae.append(f"    CAMPUS {nomen_campi} SICUT NUMERUS.")

    ultima_forma = nomina_formarum[-1]
    ultimus_campus = nomina_camporum[-1]
    lineae.extend(
        [
            "FIN-FORMA.",
            "",
            "FUNCTIO PRINCIPALIS REDDENS NUMERUS.",
            f"    DECLARA ultima SICUT {ultima_forma}.",
            "    valor DE ultima = 39.",
            "    PROCLAMA valor DE ultima.",
            "    DECLARA magna SICUT Magna.",
            f"    {ultimus_campus} DE magna = 777.",
            f"    PROCLAMA {ultimus_campus} DE magna.",
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
