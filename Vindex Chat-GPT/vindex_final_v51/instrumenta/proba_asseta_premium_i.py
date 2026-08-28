#!/usr/bin/env python3
"""P16-XI-A: XII fontes PNG et XII derivata SIMG II stricte probat."""
from __future__ import annotations

import importlib.util
import struct
import sys
import tempfile
import zlib
from pathlib import Path


def onera(via: Path, nomen: str):
    spec = importlib.util.spec_from_file_location(nomen, via)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"modulus {via} importari non potest")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def u32(data: bytes, off: int) -> int:
    return struct.unpack_from("<I", data, off)[0]


def principale() -> int:
    instrumenta = Path(__file__).resolve().parent
    radix = instrumenta.parent
    gen = onera(instrumenta / "genera_asseta_premium_i.py", "genera_asseta_premium_i")
    imp = onera(instrumenta / "simg_ii_importa_png.py", "simg_ii_importa_png")
    fons = radix / "res" / "jlux" / "assetta" / "premium-i" / "png"

    visa = 0
    alpha_media = 0
    occultus = 0
    with tempfile.TemporaryDirectory(prefix="asseta-premium-i-") as td:
        out = Path(td)
        scripta = gen.genera(out, verbose=False)
        if len(scripta) != 12:
            print(f"DEFECIT: XII SIMG II exspectata, recepta {len(scripta)}", file=sys.stderr)
            return 1

        for nomen in gen.FAMILIA:
            for suffixum, scala, latus in gen.SCALAE:
                png = fons / f"{nomen}@{suffixum}.png"
                simg = out / f"{nomen}@{suffixum}.simg"
                if not png.is_file() or not simg.is_file():
                    print(f"DEFECIT: assetum deest {png} / {simg}", file=sys.stderr)
                    return 2
                w, h, rgba = imp.png_rgba(png.read_bytes())
                if (w, h) != (latus, latus) or len(rgba) != latus * latus * 4:
                    print(f"DEFECIT: geometria {png.name}: {w}x{h}", file=sys.stderr)
                    return 3

                semi = 0
                occ = 0
                for i in range(0, len(rgba), 4):
                    r, g, b, a = rgba[i:i+4]
                    if 0 < a < 255:
                        semi += 1
                    if a == 0 and (r != 0 or g != 0 or b != 0):
                        occ += 1
                if semi < max(32, latus):
                    print(f"DEFECIT: alpha anti-aliased insufficiens in {png.name}: {semi}", file=sys.stderr)
                    return 4
                if occ < 1:
                    print(f"DEFECIT: pixel adversarialis alpha-zero deest in {png.name}", file=sys.stderr)
                    return 5
                alpha_media += semi
                occultus += occ

                data = simg.read_bytes()
                if len(data) < 80 or data[:4] != b"SIMG" or data[4] != 2 or data[5] != 1:
                    print(f"DEFECIT: caput SIMG II invalidum in {simg.name}", file=sys.stderr)
                    return 6
                if data[6] not in (0, 1):
                    return 7
                if u32(data, 8) != 80 or u32(data, 12) != latus or u32(data, 16) != latus:
                    return 8
                if u32(data, 20) != latus * 4 or u32(data, 24) != 80:
                    return 9
                if u32(data, 32) != latus * latus * 4:
                    return 10
                if u32(data, 36) != 2 or u32(data, 40) != scala:
                    print(f"DEFECIT: genus/scala {simg.name}", file=sys.stderr)
                    return 11
                payload = data[80:80 + u32(data, 28)]
                if len(payload) != u32(data, 28):
                    return 12
                if (zlib.adler32(payload) & 0xFFFFFFFF) != u32(data, 72):
                    print(f"DEFECIT: Adler-32 {simg.name}", file=sys.stderr)
                    return 13

                if data[6] == 0:
                    expanditum = payload
                else:
                    q = bytearray()
                    p = 0
                    while p < len(payload):
                        run = payload[p]
                        if run == 0 or p + 5 > len(payload):
                            return 14
                        q.extend(payload[p+1:p+5] * run)
                        p += 5
                    expanditum = bytes(q)
                if expanditum != rgba:
                    print(f"DEFECIT: round-trip RGBA {simg.name}", file=sys.stderr)
                    return 15
                visa += 1

    if visa != 12:
        return 16
    print(f"ASSETA-PREMIUM-I: XII variantes probatae; alpha-media={alpha_media}; alpha-zero-coloratus={occultus}.")
    print("RECTE: PNG -> SIMG II deterministica, metadata, Adler-32 et alpha servantur.")
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
