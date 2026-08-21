#!/usr/bin/env python3
"""Fontem VINDEX ante compilationem praeparat, positionibus octetorum servatis."""

from __future__ import annotations

import sys
from pathlib import Path


def purga_commentaria(data: bytes) -> bytes:
    exitus = bytearray(data)
    i = 0
    intra_chordam = False
    intra_litteram = False

    while i < len(exitus):
        ch = exitus[i]

        if ch == 34 and not intra_litteram:
            intra_chordam = not intra_chordam
            i += 1
            continue

        if ch == 39 and not intra_chordam:
            intra_litteram = not intra_litteram
            i += 1
            continue

        if (
            not intra_chordam
            and not intra_litteram
            and ch == 47
            and i + 1 < len(exitus)
            and exitus[i + 1] == 47
        ):
            while i < len(exitus) and exitus[i] not in (10, 13):
                exitus[i] = 32
                i += 1
            continue

        i += 1

    return bytes(exitus)


def principale() -> int:
    if len(sys.argv) != 3:
        print("USUS: vindex_praepara.py <fons> <exitus>", file=sys.stderr)
        return 64

    fons = Path(sys.argv[1])
    exitus = Path(sys.argv[2])

    try:
        data = fons.read_bytes()
    except OSError as erratum:
        print(f"ERRATUM: fons legi non potest: {erratum}", file=sys.stderr)
        return 66

    praeparatus = purga_commentaria(data)

    try:
        exitus.write_bytes(praeparatus)
    except OSError as erratum:
        print(f"ERRATUM: fons praeparatus scribi non potest: {erratum}", file=sys.stderr)
        return 73

    if len(praeparatus) != len(data):
        print("ERRATUM: praeparatio positiones octetorum mutavit", file=sys.stderr)
        return 70

    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
