#!/usr/bin/env python3
"""Contractum visuale et ABI PROGRAMMATA Gradus F verificat."""

from pathlib import Path
import platform
import re
import subprocess
import tempfile

RADIX = Path(__file__).resolve().parents[1]
FONS = RADIX / "src" / "programmata_fenestrale_ii.vindex"
BIBLIOTHECA = RADIX / "bibliotheca" / "fenestrale_ii.vindex"


def require(textus: str, fragmentum: str, nomen: str) -> None:
    if fragmentum not in textus:
        raise SystemExit(f"ERRATUM: {nomen} deest: {fragmentum}")


def main() -> None:
    fons = FONS.read_text(encoding="utf-8")
    bibliotheca = BIBLIOTHECA.read_text(encoding="utf-8")
    for fragmentum in (
        'IMPORTA "bibliotheca/fenestrale_ii.vindex".',
        "FENESTRALE_II_AD_EST()",
        "FENESTRALE_II_EVENTA_PARATA()",
        "FENESTRALE_II_EVENTUM_CONSUME()",
        "FENESTRALE_II_RECTANGULUM",
        "barra != 28",
    ):
        require(fons, fragmentum, "contractus Gradus F")
    require(bibliotheca, "CONTENTUM(basis + (py * linea + px) * 4) = par.", "scriptura framebuffer")
    if re.search(r"radius|JL-UX", fons, re.IGNORECASE):
        # Utraque vox in commentariis tantum licet, numquam in pictura/textu clientis.
        sine_commentariis = "\n".join(l for l in fons.splitlines() if not l.lstrip().startswith("//"))
        if re.search(r"radius|JL-UX", sine_commentariis, re.IGNORECASE):
            raise SystemExit("ERRATUM: branding aut rotunditas in clientem intravit")

    if platform.system() != "Windows":
        with tempfile.TemporaryDirectory(prefix="programmata-f-") as td:
            exitus = Path(td) / "programmata_fenestrale_ii"
            subprocess.run([str(RADIX / "compilator_vindex"), str(FONS), str(exitus)], cwd=RADIX, check=True)
            if not exitus.is_file() or exitus.stat().st_size == 0:
                raise SystemExit("ERRATUM: client VINDEX non constructus est")
    print("RECTE: PROGRAMMATA est client VINDEX nativus Fenestralis II Gradus F.")


if __name__ == "__main__":
    main()
