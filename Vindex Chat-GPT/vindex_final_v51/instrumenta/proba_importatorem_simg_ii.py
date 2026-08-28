#!/usr/bin/env python3
"""Importatorem PNG → SIMG II et compatibilitatem cum lectore VINDEX probat."""
from __future__ import annotations

import importlib.util
import os
import struct
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path


def importator():
    via = Path(__file__).resolve().with_name("simg_ii_importa_png.py")
    spec = importlib.util.spec_from_file_location("simg_ii_importa_png", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("importator SIMG II importari non potest")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def chunk(typ: bytes, corpus: bytes) -> bytes:
    crc = zlib.crc32(typ)
    crc = zlib.crc32(corpus, crc) & 0xFFFFFFFF
    return struct.pack(">I", len(corpus)) + typ + corpus + struct.pack(">I", crc)


def paeth(a: int, b: int, c: int) -> int:
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def filtra(raw: bytes, prior: bytes, bpp: int, genus: int) -> bytes:
    out = bytearray(len(raw))
    for i, v in enumerate(raw):
        a = raw[i - bpp] if i >= bpp else 0
        b = prior[i]
        c = prior[i - bpp] if i >= bpp else 0
        if genus == 0:
            pred = 0
        elif genus == 1:
            pred = a
        elif genus == 2:
            pred = b
        elif genus == 3:
            pred = (a + b) // 2
        elif genus == 4:
            pred = paeth(a, b, c)
        else:
            raise ValueError(genus)
        out[i] = (v - pred) & 255
    return bytes(out)


def png_rgba(w: int, rows: list[bytes], filters: list[int]) -> bytes:
    if len(rows) != len(filters):
        raise ValueError("rows/filters")
    prior = bytes(w * 4)
    stream = bytearray()
    for row, f in zip(rows, filters):
        if len(row) != w * 4:
            raise ValueError("row")
        stream.append(f)
        stream.extend(filtra(row, prior, 4, f))
        prior = row
    ihdr = struct.pack(">IIBBBBB", w, len(rows), 8, 6, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(bytes(stream), 9)) + chunk(b"IEND", b"")


def png_palette() -> tuple[bytes, bytes]:
    # indices 0,1,2: ruber opacus, viridis dimidius, caeruleus transparens.
    w, h = 3, 1
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 3, 0, 0, 0)
    plte = bytes((255, 0, 0, 0, 255, 0, 0, 0, 255))
    trns = bytes((255, 128, 0))
    raw = bytes((0, 0, 1, 2))
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr)
        + chunk(b"PLTE", plte)
        + chunk(b"tRNS", trns)
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b"")
    )
    rgba = bytes((255, 0, 0, 255, 0, 255, 0, 128, 0, 0, 255, 0))
    return png, rgba


def u32(data: bytes, off: int) -> int:
    return struct.unpack_from("<I", data, off)[0]


def fons_vindex(simg: bytes) -> str:
    lines = [
        'IMPORTA "bibliotheca/simg_ii.vindex".',
        '',
        'FUNCTIO P_IMPORTA_SIMG REDDENS TEXTUS.',
        f'    DECLARA d SICUT NUMERUS VALENS RESERVA_OCTETA({len(simg) + 17}).',
        '    SI d<=0 TUNC REDDE 0. FIN-SI.',
        f'    CONTENTUM(d)={len(simg)}.',
        f'    CONTENTUM(d+8)={len(simg)}.',
    ]
    for i, b in enumerate(simg):
        lines.append(f'    SCRIBE_OCTETUM_AB(d+{16+i},{b}).')
    lines += [
        f'    SCRIBE_OCTETUM_AB(d+{16+len(simg)},0).',
        '    REDDE d.',
        'FIN-FUNCTIO.',
        '',
        'FUNCTIO PRINCIPALIS REDDENS NUMERUS.',
        '    DECLARA imago SICUT TEXTUS VALENS P_IMPORTA_SIMG().',
        '    SI SII_VALIDUS(imago)==0 TUNC REDDE 1. FIN-SI.',
        '    SI SII_LATITUDO(imago)!=8 || SII_ALTITUDO(imago)!=8 TUNC REDDE 2. FIN-SI.',
        '    SI SII_GENUS(imago)!=2 || SII_SCALA(imago)!=2000 TUNC REDDE 3. FIN-SI.',
        '    SI SII_COMPRESSIO(imago)!=1 TUNC REDDE 4. FIN-SI.',
        '    SI (SII_META_VEXILLA(imago)&1)==0 TUNC REDDE 5. FIN-SI.',
        '    SI SII_MARGO(imago,0)!=2 || SII_MARGO(imago,1)!=2 || SII_MARGO(imago,2)!=2 || SII_MARGO(imago,3)!=2 TUNC REDDE 6. FIN-SI.',
        '    SI SII_PIXEL_RGBA(imago,4,4)!=4280161290 TUNC REDDE 7. FIN-SI.',
        '    REDDE 0.',
        'FIN-FUNCTIO.',
        '',
    ]
    return "\n".join(lines)


def principale() -> int:
    m = importator()

    # Omnia quinque filtra PNG in RGBA comprobantur.
    rows = [
        bytes((10,20,30,255, 40,50,60,128, 70,80,90,64)),
        bytes((11,21,31,254, 41,51,61,127, 71,81,91,63)),
        bytes((12,22,32,253, 42,52,62,126, 72,82,92,62)),
        bytes((13,23,33,252, 43,53,63,125, 73,83,93,61)),
        bytes((14,24,34,251, 44,54,64,124, 74,84,94,60)),
    ]
    png = png_rgba(3, rows, [0, 1, 2, 3, 4])
    w, h, rgba = m.png_rgba(png)
    if (w, h) != (3, 5) or rgba != b"".join(rows):
        print("DEFECIT: filtra PNG RGBA", file=sys.stderr)
        return 1

    ppng, prgba = png_palette()
    pw, ph, got = m.png_rgba(ppng)
    if (pw, ph) != (3, 1) or got != prgba:
        print("DEFECIT: PNG palette/tRNS", file=sys.stderr)
        return 2

    # Auto eligit RAW pro imagine varia.
    simg, comp = m.simg_ii(w, h, rgba, kind=2, scale=1500, compression="auto", nine=None, hotspot=None)
    if comp != "RAW" or simg[:4] != b"SIMG" or simg[4:7] != bytes((2, 1, 0)):
        print("DEFECIT: auto RAW", file=sys.stderr)
        return 3
    if u32(simg, 12) != 3 or u32(simg, 16) != 5 or u32(simg, 40) != 1500:
        return 4
    if (zlib.adler32(simg[80:]) & 0xFFFFFFFF) != u32(simg, 72):
        return 5

    # Solidum 8x8 RLE valde minuitur et metadata intra header manent.
    pixel = bytes((10, 20, 30, 255))
    solid = pixel * 64
    simg2, comp2 = m.simg_ii(8, 8, solid, kind=2, scale=2000, compression="auto", nine=(2,2,2,2), hotspot=None)
    if comp2 != "RLE32" or simg2[6] != 1 or len(simg2) != 85:
        print(f"DEFECIT: auto RLE32 {comp2}/{len(simg2)}", file=sys.stderr)
        return 6
    if u32(simg2, 44) != 1 or tuple(u32(simg2, o) for o in (48,52,56,60)) != (2,2,2,2):
        return 7

    # CLI verus scribit .simg; deinde lector VINDEX eadem octeta verificat.
    root = Path(__file__).resolve().parents[1]
    compilator = root / "compilator_vindex"
    if not compilator.exists():
        print("DEFECIT: compilator_vindex deest", file=sys.stderr)
        return 8
    with tempfile.TemporaryDirectory(prefix="simg-ii-") as td:
        t = Path(td)
        source = t / "solid.png"
        output = t / "solid.simg"
        source.write_bytes(png_rgba(8, [pixel * 8 for _ in range(8)], [0] * 8))
        rc = m.main([str(source), str(output), "--genus", "icona", "--scala", "2000", "--compressio", "auto", "--novem", "2,2,2,2"])
        if rc != 0 or output.read_bytes() != simg2:
            print("DEFECIT: CLI .simg", file=sys.stderr)
            return 9
        vsrc = t / "proba_importata.vindex"
        elf = t / "proba_importata"
        vsrc.write_text(fons_vindex(simg2), encoding="utf-8")
        os.chmod(compilator, 0o755)
        cp = subprocess.run([str(compilator), str(vsrc), str(elf)], cwd=root, check=False, capture_output=True, text=True)
        if cp.returncode != 0:
            print(cp.stdout, file=sys.stderr)
            print(cp.stderr, file=sys.stderr)
            return 10
        os.chmod(elf, 0o755)
        ex = subprocess.run([str(elf)], cwd=root, check=False)
        if ex.returncode != 0:
            print(f"DEFECIT: lector VINDEX importatum recusavit code={ex.returncode}", file=sys.stderr)
            return 11

    # Errores metadatae serio recusantur.
    try:
        m.simg_ii(8, 8, solid, kind=2, scale=2000, compression="raw", nine=(5,0,5,0), hotspot=None)
    except m.ErrorSIMG:
        pass
    else:
        return 12

    print("RECTE: PNG RGBA/palette/filtra → SIMG II → lector VINDEX transitus integer est.")
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
