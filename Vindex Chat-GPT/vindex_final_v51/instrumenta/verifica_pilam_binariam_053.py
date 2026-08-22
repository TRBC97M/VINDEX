#!/usr/bin/env python3
"""Prologos pilae VINDEX 0.53 in binario probationis verificat."""

from pathlib import Path
import sys


via = Path(sys.argv[1])
data = via.read_bytes()
frames: list[int] = []

for i in range(len(data) - 55):
    if (
        data[i:i + 2] == b"\x49\xbb"
        and data[i + 10:i + 17] == b"\x49\x81\xfb\x00\x10\x00\x00"
        and data[i + 17:i + 19] == b"\x76\x1c"
    ):
        frames.append(int.from_bytes(data[i + 2:i + 10], "little"))

if len(frames) != 2:
    raise SystemExit(f"ERRATUM: duo prologi pilae exspectabantur: {frames}")
if any(frame % 16 for frame in frames):
    raise SystemExit(f"ERRATUM: fasciculus non ordinatus est: {frames}")
if max(frames) < 1024 * 1024:
    raise SystemExit(f"ERRATUM: fasciculus unum MiB non superat: {frames}")

print("RECTE: pila magna et ordinatio probatae sunt: " + ",".join(map(str, frames)))
