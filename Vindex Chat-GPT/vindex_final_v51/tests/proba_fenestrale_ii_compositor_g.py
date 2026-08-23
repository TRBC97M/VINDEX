#!/usr/bin/env python3
"""ABI compositorii et PROGRAMMATA privatae superficiei Gradus G verificat."""

from pathlib import Path
import re
import subprocess
import sys
import tempfile

RADIX = Path(__file__).resolve().parents[1]
HEADER = RADIX / "systema" / "fenestrale_ii_compositor_abi.h"
BIBLIOTHECA = RADIX / "bibliotheca" / "fenestrale_ii_compositor.vindex"
CLIENT = RADIX / "src" / "programmata_fenestrale_ii_g.vindex"


def require(textus: str, fragmentum: str, nomen: str) -> None:
    if fragmentum not in textus:
        raise SystemExit(f"ERRATUM: {nomen} deest: {fragmentum}")


def sine_commentariis(textus: str) -> str:
    return "\n".join(
        linea for linea in textus.splitlines()
        if not linea.lstrip().startswith("//")
    )


def compila_header() -> None:
    fons = r'''
#include "fenestrale_ii_compositor_abi.h"
_Static_assert(FENESTRALE2_COMPOSITOR_BASIS == 0x03000E00ULL, "basis");
_Static_assert(FENESTRALE2_COMPOSITOR_MENSURA == 256ULL, "mensura");
_Static_assert(FII_CMP_OP_CREA == 1ULL, "crea");
_Static_assert(FII_CMP_OP_PRAESENTA == 3ULL, "praesenta");
_Static_assert(FII_CMP_SUPERFICIES_FENESTRA == 4ULL, "fenestra");
int main(void) { return 0; }
'''
    with tempfile.TemporaryDirectory(prefix="fii-g-") as td:
        via = Path(td) / "proba.c"
        exitus = Path(td) / "proba"
        via.write_text(fons, encoding="utf-8")
        subprocess.run(
            [
                "cc", "-std=c11", "-Wall", "-Wextra", "-Werror",
                "-I", str(RADIX / "systema"), str(via), "-o", str(exitus),
            ],
            check=True,
        )


def main() -> None:
    header = HEADER.read_text(encoding="utf-8")
    bibliotheca = BIBLIOTHECA.read_text(encoding="utf-8")
    client = CLIENT.read_text(encoding="utf-8")

    for fragmentum in (
        "#define FENESTRALE2_COMPOSITOR_BASIS   0x03000E00ULL",
        "#define FENESTRALE2_COMPOSITOR_MENSURA 256ULL",
        "FII_CMP_STATUS_PETITUM",
        "FII_CMP_OP_CREA",
        "FII_CMP_OP_PRAESENTA",
        "FENESTRALE2_COMPOSITOR_MAILBOX",
        "<= 0x03001000ULL",
    ):
        require(header, fragmentum, "ABI compositorii")

    for fragmentum in (
        'IMPORTA "bibliotheca/fenestrale_ii.vindex".',
        "REDDE 50335232.",
        "FII_CMP_SUPERFICIEM_PETE",
        "FII_CMP_PRAESENTA",
        "FII_CMP_RECTANGULUM",
        "4278190080",
        "CONTENTUM(basis + (py * linea + px) * 4) = par.",
    ):
        require(bibliotheca, fragmentum, "bibliotheca compositorii")

    for fragmentum in (
        'IMPORTA "bibliotheca/fenestrale_ii_compositor.vindex".',
        "FII_CMP_AD_EST()",
        "FII_CMP_SUPERFICIEM_PETE(1, w, h, 7)",
        "FII_CMP_PRAESENTA(1, superficies, 0, 0, w, h)",
        "FII_CMP_RECTANGULUM",
        "FENESTRALE_II_TASKBAR_ALTITUDO() != 28",
        "h - 20",
        "corpus_y SICUT NUMERUS VALENS 84",
    ):
        require(client, fragmentum, "client PROGRAMMATA G")

    codex = sine_commentariis(client)
    if "FENESTRALE_II_FRAMEBUFFER(" in codex or "FENESTRALE_II_RECTANGULUM(" in codex:
        raise SystemExit("ERRATUM: client G framebuffer physicum directe scribit")
    if re.search(r"JL-UX", codex, re.IGNORECASE):
        raise SystemExit("ERRATUM: branding JL-UX in superficie clientis apparuit")
    if re.search(r"radius|border-radius", codex, re.IGNORECASE):
        raise SystemExit("ERRATUM: rotunditas non canonica in clientem intravit")

    compila_header()
    # Clientis verificatio bibliothecas importatas quoque syntactice inspicit.
    subprocess.run(
        [sys.executable, str(RADIX / "instrumenta" / "vindex_verifica.py"), str(CLIENT)],
        cwd=RADIX,
        check=True,
    )

    print("RECTE: Gradus G superficiem privatam et mailbox compositorii servat.")


if __name__ == "__main__":
    main()
