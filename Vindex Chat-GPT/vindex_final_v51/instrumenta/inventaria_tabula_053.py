#!/usr/bin/env python3
"""Reliquias accessuum literalium tabulae historicae VINDEX 0.53 inventariat."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import sys


RADIX = Path(__file__).resolve().parent.parent
FONS_DEFECTUS = RADIX / "src/compilator_vindex.vindex"
EXEMPLUM = re.compile(r"\btabula\s*\[\s*(\d+)\s*\]")
CAPACITAS = re.compile(r"\bDECLARA\s+tabula\s+SICUT\s+ORDO\s+DE\s+NUMERUS\s+CAPACITAS\s+(\d+)\s*\.")


def lege_basim(via: Path) -> set[int]:
    indices: set[int] = set()
    for linea in via.read_text(encoding="utf-8").splitlines():
        pura = linea.strip()
        if not pura or pura.startswith("#"):
            continue
        try:
            indices.add(int(pura))
        except ValueError as exc:
            raise SystemExit(f"ERRATUM: linea basis non numerica est: {pura!r}") from exc
    return indices


def inventaria(fons: Path) -> tuple[Counter[int], int | None]:
    textus = fons.read_text(encoding="utf-8")
    numeri = Counter(int(m.group(1)) for m in EXEMPLUM.finditer(textus))
    capacitas = CAPACITAS.search(textus)
    return numeri, int(capacitas.group(1)) if capacitas else None


def principale() -> int:
    parser = argparse.ArgumentParser(
        description="Accessus tabula[n] litterales in compilatore VINDEX inventariat."
    )
    parser.add_argument("fons", nargs="?", type=Path, default=FONS_DEFECTUS)
    parser.add_argument(
        "--verifica",
        type=Path,
        metavar="BASIS",
        help="deficit si index litteralis novus, qui in basi non est, apparuit",
    )
    args = parser.parse_args()

    numeri, capacitas = inventaria(args.fons)

    print("=== RELIQUIAE TABULAE 0.53 ===")
    if capacitas is None:
        print("CAPACITAS TABULAE: nulla declaratio fixa inventa est")
    else:
        print(f"CAPACITAS TABULAE: {capacitas}")
    print(f"INDICES LITTERALES DISTINCTI: {len(numeri)}")
    print(f"ACCESSUS LITTERALES TOTALES: {sum(numeri.values())}")
    for index in sorted(numeri):
        print(f"{index}: {numeri[index]}")

    if args.verifica is not None:
        basis = lege_basim(args.verifica)
        novi = sorted(set(numeri) - basis)
        if novi:
            print(
                "ERRATUM: novi indices magici tabulae inventi sunt: "
                + ",".join(map(str, novi)),
                file=sys.stderr,
            )
            return 1
        print("RECTE: nullus index magicus tabulae novus introductus est.")

    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
