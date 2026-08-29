#!/usr/bin/env python3
"""P16-XI-B: iconae premium Bureau in framebuffer vero QEMU/OVMF probantur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name("proba_formam_sylviae_i.py")
    spec = importlib.util.spec_from_file_location("aux_xib_forma", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("auxilia framebuffer importari non possunt")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lumen(c: tuple[int, int, int]) -> int:
    return c[0] + c[1] + c[2]


def colores(aux: object, pix: bytes, w: int, x0: int, y0: int, x1: int, y1: int) -> set[tuple[int, int, int]]:
    out: set[tuple[int, int, int]] = set()
    for y in range(y0, y1):
        for x in range(x0, x1):
            out.add(aux.pixel(pix, w, x, y))
    return out


def numerus_puri_caerulei(aux: object, pix: bytes, w: int, regio: tuple[int, int, int, int]) -> int:
    x0, y0, x1, y1 = regio
    n = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            if aux.pixel(pix, w, x, y) == (0, 0, 255):
                n += 1
    return n


def principale() -> int:
    if len(sys.argv) != 5:
        print("USUS: proba_formam_sylviae_xib.py MONITOR QMP EXITUS MORA", file=sys.stderr)
        return 2
    aux = auxilia()
    mon_via, _qmp_via, out, mora = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), float(sys.argv[4])
    finis = time.time() + 12.0
    while not mon_via.exists() and time.time() < finis:
        time.sleep(0.1)
    if not mon_via.exists():
        print("DEFECIT: monitor deest", file=sys.stderr)
        return 3

    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    monitor.settimeout(0.5)
    monitor.connect(str(mon_via))
    try:
        aux.lege_usque(monitor, b"(qemu) ", 2.0)
        time.sleep(mora)
        via = out / "forma-sylviae-xib.ppm"
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        # Testa P16-IX manet: limes bronzeus/aqua et gradientia taskbar.
        bronzeum = (185, 138, 82)
        aqua = (103, 164, 160)
        taskbar_top = h - 40
        nb = aux.numerus_coloris_in_linea(pix, w, taskbar_top, bronzeum)
        na = aux.numerus_coloris_in_linea(pix, w, taskbar_top + 2, aqua)
        if nb < w * 95 // 100 or na < w * 95 // 100:
            print(f"DEFECIT: lineae taskbar fractae sunt: {nb}/{na}", file=sys.stderr)
            return 5
        top = aux.pixel(pix, w, 400, taskbar_top + 4)
        bottom = aux.pixel(pix, w, 400, taskbar_top + 36)
        if top == bottom or lumen(top) <= lumen(bottom):
            print(f"DEFECIT: gradientia taskbar deest: {top}->{bottom}", file=sys.stderr)
            return 6

        # Geometria Bureau manet P16-VII: quattuor destinationes 48×48.
        regiones = (
            ("PROGRAMMATA", (48, 80, 96, 128), (72, 104), (236, 194, 113)),
            ("TABULA", (48, 184, 96, 232), (72, 208), (201, 154, 82)),
            ("TERMINALE", (48, 288, 96, 336), (72, 312), (17, 28, 33)),
            ("OFFICINA", (48, 392, 96, 440), (72, 416), (232, 232, 217)),
        )
        numeri: list[int] = []
        centra_vetera = 0
        purum_caeruleum = 0
        for nomen, regio, centrum, vetus in regiones:
            cs = colores(aux, pix, w, *regio)
            numeri.append(len(cs))
            if len(cs) < 80:
                print(f"DEFECIT: {nomen} non videtur premium: colores={len(cs)}", file=sys.stderr)
                return 7
            if aux.pixel(pix, w, *centrum) == vetus:
                centra_vetera += 1
            purum_caeruleum += numerus_puri_caerulei(aux, pix, w, regio)
        if centra_vetera >= 2:
            print(f"DEFECIT: atlas P16-VII adhuc dominatur: centra_vetera={centra_vetera}", file=sys.stderr)
            return 8
        if purum_caeruleum != 0:
            print(f"DEFECIT: RGB occultum alpha-zero in framebuffer apparuit: {purum_caeruleum}", file=sys.stderr)
            return 9
        if len(set(numeri)) < 3:
            print(f"DEFECIT: familia premium non satis distincta est: {numeri}", file=sys.stderr)
            return 10

        # Cursor, titulus et hitbox Bureau positionibus historicis manent.
        nox = (28, 31, 32)
        if aux.pixel(pix, w, 20, 74) != nox or aux.pixel(pix, w, 20, 178) != nox:
            print("DEFECIT: geometria cardorum Bureau mutata est", file=sys.stderr)
            return 11

        print(f"FORMA-XIB: resolutio={w}x{h} taskbar={nb}/{na}")
        print(f"FORMA-XIB: colores iconarum={numeri} centra_vetera={centra_vetera} caeruleum_purum={purum_caeruleum}")
        print("RECTE: quattuor iconae premium Graphica IX in Bureau Sylviae realis adsunt.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
