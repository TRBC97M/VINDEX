#!/usr/bin/env python3
"""Generat formam IBM/VGA 8×8 publici dominii pro Systemate VINDEX."""

from pathlib import Path
import sys


# Forma IBM/VGA publica, per Daniel Hepper in font8x8_basic.h conservata.
# Quisque ordo codices U+0020–U+007F continet; bit minus significans primus est.
FORMAE_HEX = """
00 00 00 00 00 00 00 00
18 3C 3C 18 18 00 18 00
36 36 00 00 00 00 00 00
36 36 7F 36 7F 36 36 00
0C 3E 03 1E 30 1F 0C 00
00 63 33 18 0C 66 63 00
1C 36 1C 6E 3B 33 6E 00
06 06 03 00 00 00 00 00
18 0C 06 06 06 0C 18 00
06 0C 18 18 18 0C 06 00
00 66 3C FF 3C 66 00 00
00 0C 0C 3F 0C 0C 00 00
00 00 00 00 00 0C 0C 06
00 00 00 3F 00 00 00 00
00 00 00 00 00 0C 0C 00
60 30 18 0C 06 03 01 00
3E 63 73 7B 6F 67 3E 00
0C 0E 0C 0C 0C 0C 3F 00
1E 33 30 1C 06 33 3F 00
1E 33 30 1C 30 33 1E 00
38 3C 36 33 7F 30 78 00
3F 03 1F 30 30 33 1E 00
1C 06 03 1F 33 33 1E 00
3F 33 30 18 0C 0C 0C 00
1E 33 33 1E 33 33 1E 00
1E 33 33 3E 30 18 0E 00
00 0C 0C 00 00 0C 0C 00
00 0C 0C 00 00 0C 0C 06
18 0C 06 03 06 0C 18 00
00 00 3F 00 00 3F 00 00
06 0C 18 30 18 0C 06 00
1E 33 30 18 0C 00 0C 00
3E 63 7B 7B 7B 03 1E 00
0C 1E 33 33 3F 33 33 00
3F 66 66 3E 66 66 3F 00
3C 66 03 03 03 66 3C 00
1F 36 66 66 66 36 1F 00
7F 46 16 1E 16 46 7F 00
7F 46 16 1E 16 06 0F 00
3C 66 03 03 73 66 7C 00
33 33 33 3F 33 33 33 00
1E 0C 0C 0C 0C 0C 1E 00
78 30 30 30 33 33 1E 00
67 66 36 1E 36 66 67 00
0F 06 06 06 46 66 7F 00
63 77 7F 7F 6B 63 63 00
63 67 6F 7B 73 63 63 00
1C 36 63 63 63 36 1C 00
3F 66 66 3E 06 06 0F 00
1E 33 33 33 3B 1E 38 00
3F 66 66 3E 36 66 67 00
1E 33 07 0E 38 33 1E 00
3F 2D 0C 0C 0C 0C 1E 00
33 33 33 33 33 33 3F 00
33 33 33 33 33 1E 0C 00
63 63 63 6B 7F 77 63 00
63 63 36 1C 1C 36 63 00
33 33 33 1E 0C 0C 1E 00
7F 63 31 18 4C 66 7F 00
1E 06 06 06 06 06 1E 00
03 06 0C 18 30 60 40 00
1E 18 18 18 18 18 1E 00
08 1C 36 63 00 00 00 00
00 00 00 00 00 00 00 FF
0C 0C 18 00 00 00 00 00
00 00 1E 30 3E 33 6E 00
07 06 06 3E 66 66 3B 00
00 00 1E 33 03 33 1E 00
38 30 30 3E 33 33 6E 00
00 00 1E 33 3F 03 1E 00
1C 36 06 0F 06 06 0F 00
00 00 6E 33 33 3E 30 1F
07 06 36 6E 66 66 67 00
0C 00 0E 0C 0C 0C 1E 00
30 00 30 30 30 33 33 1E
07 06 66 36 1E 36 67 00
0E 0C 0C 0C 0C 0C 1E 00
00 00 33 7F 7F 6B 63 00
00 00 1F 33 33 33 33 00
00 00 1E 33 33 33 1E 00
00 00 3B 66 66 3E 06 0F
00 00 6E 33 33 3E 30 78
00 00 3B 6E 66 06 0F 00
00 00 3E 03 1E 30 1F 00
08 0C 3E 0C 0C 2C 18 00
00 00 33 33 33 33 6E 00
00 00 33 33 33 1E 0C 00
00 00 63 6B 7F 7F 36 00
00 00 63 36 1C 36 63 00
00 00 33 33 33 3E 30 1F
00 00 3F 19 0C 26 3F 00
38 0C 0C 07 0C 0C 38 00
18 18 18 00 18 18 18 00
07 0C 0C 38 0C 0C 07 00
6E 3B 00 00 00 00 00 00
00 00 00 00 00 00 00 00
"""


def octetum_inverte(valor: int) -> int:
    """Ordinem octo bituum ad conventionem VINDEX convertit."""
    exitus = 0
    for index in range(8):
        if valor & (1 << index):
            exitus |= 0x80 >> index
    return exitus


def principale() -> int:
    exitus = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("forma.bin")
    ordines = [
        [int(octetum, 16) for octetum in linea.split()]
        for linea in FORMAE_HEX.strip().splitlines()
    ]
    if len(ordines) != 96 or any(len(ordo) != 8 for ordo in ordines):
        raise ValueError("forma IBM/VGA corrupta est")
    forma = bytearray(256 * 8)
    for codex, ordo in enumerate(ordines, start=32):
        for y, octetum in enumerate(ordo):
            forma[codex * 8 + y] = octetum_inverte(octetum)
    exitus.write_bytes(forma)
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
