#!/usr/bin/env python3
"""PNG artis in SIMG II runtime convertit sine bibliotheca externa."""
from __future__ import annotations

import argparse
import struct
import sys
import zlib
from pathlib import Path

PNG_SIG = b"\x89PNG\r\n\x1a\n"
SIMG_HEADER = 80
KIND = {
    "genericum": 0,
    "wallpaper": 1,
    "icona": 2,
    "novem": 3,
    "cursor": 4,
    "fons": 5,
    "testa": 6,
}


class ErrorSIMG(ValueError):
    pass


def paeth(a: int, b: int, c: int) -> int:
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def chunks(data: bytes):
    if not data.startswith(PNG_SIG):
        raise ErrorSIMG("signatura PNG deest")
    p = len(PNG_SIG)
    while p + 12 <= len(data):
        n = struct.unpack_from(">I", data, p)[0]
        typ = data[p + 4 : p + 8]
        finis = p + 12 + n
        if finis > len(data):
            raise ErrorSIMG("chunk PNG truncatus est")
        corpus = data[p + 8 : p + 8 + n]
        crc_scriptum = struct.unpack_from(">I", data, p + 8 + n)[0]
        crc_visum = zlib.crc32(typ)
        crc_visum = zlib.crc32(corpus, crc_visum) & 0xFFFFFFFF
        if crc_scriptum != crc_visum:
            raise ErrorSIMG(f"CRC PNG invalidum in {typ!r}")
        yield typ, corpus
        p = finis
        if typ == b"IEND":
            return
    raise ErrorSIMG("IEND PNG deest")


def png_rgba(data: bytes) -> tuple[int, int, bytes]:
    ihdr: bytes | None = None
    idat: list[bytes] = []
    palette: bytes | None = None
    trns: bytes | None = None
    for typ, corpus in chunks(data):
        if typ == b"IHDR":
            if ihdr is not None:
                raise ErrorSIMG("IHDR duplex")
            ihdr = corpus
        elif typ == b"PLTE":
            palette = corpus
        elif typ == b"tRNS":
            trns = corpus
        elif typ == b"IDAT":
            idat.append(corpus)

    if ihdr is None or len(ihdr) != 13:
        raise ErrorSIMG("IHDR invalidum")
    w, h, bits, color, comp, filtrum, interlace = struct.unpack(">IIBBBBB", ihdr)
    if w <= 0 or h <= 0 or w > 16384 or h > 16384:
        raise ErrorSIMG("mensura PNG extra limites SIMG II")
    if bits != 8:
        raise ErrorSIMG("importator hic tantum PNG VIII bituum sustinet")
    if comp != 0 or filtrum != 0 or interlace != 0:
        raise ErrorSIMG("PNG compression/filter/interlace non canonica")
    canales = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}.get(color)
    if canales is None:
        raise ErrorSIMG(f"color type PNG {color} non sustinetur")
    if color == 3:
        if palette is None or len(palette) == 0 or len(palette) % 3 != 0 or len(palette) > 768:
            raise ErrorSIMG("PLTE deest vel invalidum")

    try:
        crudum = zlib.decompress(b"".join(idat))
    except zlib.error as exc:
        raise ErrorSIMG(f"IDAT zlib invalidum: {exc}") from exc
    linea = w * canales
    exspectata = h * (1 + linea)
    if len(crudum) != exspectata:
        raise ErrorSIMG(f"IDAT mensura {len(crudum)} loco {exspectata}")

    ordines: list[bytes] = []
    prior = bytes(linea)
    p = 0
    for _y in range(h):
        genus = crudum[p]
        p += 1
        src = crudum[p : p + linea]
        p += linea
        dst = bytearray(linea)
        for x, val in enumerate(src):
            a = dst[x - canales] if x >= canales else 0
            b = prior[x]
            c = prior[x - canales] if x >= canales else 0
            if genus == 0:
                q = val
            elif genus == 1:
                q = (val + a) & 255
            elif genus == 2:
                q = (val + b) & 255
            elif genus == 3:
                q = (val + ((a + b) // 2)) & 255
            elif genus == 4:
                q = (val + paeth(a, b, c)) & 255
            else:
                raise ErrorSIMG(f"filtrum PNG {genus} ignotum")
            dst[x] = q
        prior = bytes(dst)
        ordines.append(prior)

    out = bytearray(w * h * 4)
    q = 0
    for row in ordines:
        if color == 6:
            for x in range(w):
                i = x * 4
                out[q : q + 4] = row[i : i + 4]
                q += 4
        elif color == 2:
            for x in range(w):
                i = x * 3
                out[q : q + 3] = row[i : i + 3]
                out[q + 3] = 255
                q += 4
        elif color == 0:
            for x in range(w):
                g = row[x]
                out[q : q + 4] = bytes((g, g, g, 255))
                q += 4
        elif color == 4:
            for x in range(w):
                i = x * 2
                g, a = row[i], row[i + 1]
                out[q : q + 4] = bytes((g, g, g, a))
                q += 4
        else:
            assert color == 3 and palette is not None
            ncol = len(palette) // 3
            for x in range(w):
                idx = row[x]
                if idx >= ncol:
                    raise ErrorSIMG("index palette extra PLTE")
                i = idx * 3
                a = trns[idx] if trns is not None and idx < len(trns) else 255
                out[q : q + 4] = palette[i : i + 3] + bytes((a,))
                q += 4
    return w, h, bytes(out)


def rle32(rgba: bytes) -> bytes:
    if len(rgba) % 4:
        raise ErrorSIMG("RGBA mensura non multiplex IV")
    out = bytearray()
    p = 0
    n = len(rgba) // 4
    while p < n:
        color = rgba[p * 4 : p * 4 + 4]
        run = 1
        while p + run < n and run < 255 and rgba[(p + run) * 4 : (p + run + 1) * 4] == color:
            run += 1
        out.append(run)
        out.extend(color)
        p += run
    return bytes(out)


def quattuor(textus: str, nomen: str) -> tuple[int, int, int, int]:
    try:
        v = tuple(int(x.strip(), 0) for x in textus.split(","))
    except ValueError as exc:
        raise ErrorSIMG(f"{nomen}: integra exspectantur") from exc
    if len(v) != 4:
        raise ErrorSIMG(f"{nomen}: quattuor valores exspectantur")
    if any(x < 0 or x > 0xFFFFFFFF for x in v):
        raise ErrorSIMG(f"{nomen}: valor extra u32")
    return v  # type: ignore[return-value]


def duo(textus: str, nomen: str) -> tuple[int, int]:
    try:
        v = tuple(int(x.strip(), 0) for x in textus.split(","))
    except ValueError as exc:
        raise ErrorSIMG(f"{nomen}: integra exspectantur") from exc
    if len(v) != 2:
        raise ErrorSIMG(f"{nomen}: duo valores exspectantur")
    if any(x < 0 or x > 0xFFFFFFFF for x in v):
        raise ErrorSIMG(f"{nomen}: valor extra u32")
    return v  # type: ignore[return-value]


def simg_ii(
    w: int,
    h: int,
    rgba: bytes,
    *,
    kind: int,
    scale: int,
    compression: str,
    nine: tuple[int, int, int, int] | None,
    hotspot: tuple[int, int] | None,
) -> tuple[bytes, str]:
    if len(rgba) != w * h * 4:
        raise ErrorSIMG("RGBA mensura geometriae non respondet")
    if not (250 <= scale <= 8000):
        raise ErrorSIMG("scala SIMG II debet esse 250..8000")
    meta = 0
    l = t = r = b = 0
    hx = hy = 0
    if nine is not None:
        l, t, r, b = nine
        if l + r > w or t + b > h:
            raise ErrorSIMG("margines novem-partium imaginem excedunt")
        meta |= 1
    if hotspot is not None:
        hx, hy = hotspot
        if hx >= w or hy >= h:
            raise ErrorSIMG("hotspot cursorem imaginem excedit")
        meta |= 2

    rle = rle32(rgba)
    if compression == "raw":
        payload, comp, nomen = rgba, 0, "RAW"
    elif compression == "rle":
        payload, comp, nomen = rle, 1, "RLE32"
    elif compression == "auto":
        if len(rle) < len(rgba):
            payload, comp, nomen = rle, 1, "RLE32"
        else:
            payload, comp, nomen = rgba, 0, "RAW"
    else:
        raise ErrorSIMG("compressio ignota")

    header = bytearray(SIMG_HEADER)
    header[0:4] = b"SIMG"
    header[4] = 2
    header[5] = 1
    header[6] = comp
    header[7] = 0  # RGBA recta, vexilla generalia futura.
    vals = (
        (8, SIMG_HEADER),
        (12, w),
        (16, h),
        (20, w * 4),
        (24, SIMG_HEADER),
        (28, len(payload)),
        (32, len(rgba)),
        (36, kind),
        (40, scale),
        (44, meta),
        (48, l),
        (52, t),
        (56, r),
        (60, b),
        (64, hx),
        (68, hy),
        (72, zlib.adler32(payload) & 0xFFFFFFFF),
        (76, 0),
    )
    for off, value in vals:
        struct.pack_into("<I", header, off, value)
    return bytes(header) + payload, nomen


def argumenta(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="PNG in formatum nativum SIMG II convertit")
    p.add_argument("input", type=Path, help="PNG fons")
    p.add_argument("output", type=Path, help="SIMG II destinatio")
    p.add_argument("--genus", choices=sorted(KIND), default="genericum")
    p.add_argument("--scala", type=int, default=1000, help="scala millesimalis; 1000=1x")
    p.add_argument("--compressio", choices=("auto", "raw", "rle"), default="auto")
    p.add_argument("--novem", metavar="L,T,R,B", help="margines 9-slice")
    p.add_argument("--hotspot", metavar="X,Y", help="hotspot cursoris")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    ns = argumenta(sys.argv[1:] if argv is None else argv)
    try:
        w, h, rgba = png_rgba(ns.input.read_bytes())
        nine = quattuor(ns.novem, "--novem") if ns.novem else None
        hotspot = duo(ns.hotspot, "--hotspot") if ns.hotspot else None
        out, comp = simg_ii(
            w,
            h,
            rgba,
            kind=KIND[ns.genus],
            scale=ns.scala,
            compression=ns.compressio,
            nine=nine,
            hotspot=hotspot,
        )
        ns.output.parent.mkdir(parents=True, exist_ok=True)
        ns.output.write_bytes(out)
    except (OSError, ErrorSIMG) as exc:
        print(f"DEFECIT: {exc}", file=sys.stderr)
        return 2
    ratio = (len(out) / max(1, len(rgba))) * 100.0
    print(
        f"RECTE: {ns.input} -> {ns.output}: {w}x{h} RGBA, {comp}, "
        f"scala={ns.scala}, genus={ns.genus}, {len(out)} octeta ({ratio:.1f}% payload+header/RGBA)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
