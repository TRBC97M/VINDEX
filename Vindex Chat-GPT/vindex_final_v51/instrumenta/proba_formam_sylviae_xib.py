#!/usr/bin/env python3
"""P16-XI-B/XII-E: iconae premium Bureau in framebuffer vero QEMU/OVMF probantur."""
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


def taskbar_contractus(aux: object, pix: bytes, w: int, h: int) -> tuple[str, int, int]:
    top = h - 40
    # Contractus historicus P16-IX.
    bronze_ix = (185, 138, 82)
    aqua_ix = (103, 164, 160)
    nb_ix = aux.numerus_coloris_in_linea(pix, w, top, bronze_ix)
    na_ix = aux.numerus_coloris_in_linea(pix, w, top + 2, aqua_ix)
    if nb_ix >= w * 95 // 100 and na_ix >= w * 95 // 100:
        supra = aux.pixel(pix, w, 400, top + 4)
        infra = aux.pixel(pix, w, 400, top + 36)
        if supra == infra or lumen(supra) <= lumen(infra):
            raise RuntimeError(f"gradientia taskbar IX deest: {supra}->{infra}")
        return "IX", nb_ix, na_ix

    # Contractus P16-XII-E: limes bronzeus plene continuus, secunda linea
    # aqua translucida et duo moduli metallum distincti a corpore graphite.
    bronze_xiie = (181, 138, 84)
    nb_xiie = aux.numerus_coloris_in_linea(pix, w, top, bronze_xiie)
    na_xiie = 0
    for x in range(w):
        c = aux.pixel(pix, w, x, top + 1)
        if c[0] < 80 and c[1] > c[0] + 35 and c[2] >= c[1]:
            na_xiie += 1
    corpus = aux.pixel(pix, w, 400, top + 10)
    initium = aux.pixel(pix, w, 60, top + 18)
    systema = aux.pixel(pix, w, w - 70, top + 18)
    if nb_xiie >= w * 95 // 100 and na_xiie >= w * 95 // 100:
        if lumen(initium) <= lumen(corpus) + 45 or lumen(systema) <= lumen(corpus) + 45:
            raise RuntimeError(f"moduli taskbar XII-E desunt: corpus={corpus} initium={initium} systema={systema}")
        return "XII-E", nb_xiie, na_xiie

    raise RuntimeError(f"lineae taskbar nec IX nec XII-E inventae sunt: IX={nb_ix}/{na_ix} XIIE={nb_xiie}/{na_xiie}")


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

        try:
            testa, nb, na = taskbar_contractus(aux, pix, w, h)
        except RuntimeError as exc:
            print(f"DEFECIT: {exc}", file=sys.stderr)
            return 5

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

        if testa == "IX":
            nox = (28, 31, 32)
            if aux.pixel(pix, w, 20, 74) != nox or aux.pixel(pix, w, 20, 178) != nox:
                print("DEFECIT: geometria cardorum Bureau IX mutata est", file=sys.stderr)
                return 11
        else:
            # XII-E cardos rotundos per corpus obscurum et accentum bronzeum
            # inferioris margini probat; non dependet a colore fundi sub alpha.
            for i, y in enumerate((72, 176, 280, 384)):
                corpus = aux.pixel(pix, w, 24, y + 8)
                accentus = aux.pixel(pix, w, 72, y + 85)
                if lumen(corpus) > 130:
                    print(f"DEFECIT: corpus cardi XII-E nimis clarum est #{i}: {corpus}", file=sys.stderr)
                    return 11
                if not (accentus[0] > 125 and 85 < accentus[1] < 155 and 45 < accentus[2] < 110 and accentus[0] > accentus[1] > accentus[2]):
                    print(f"DEFECIT: accentus cardi XII-E deest #{i}: {accentus}", file=sys.stderr)
                    return 11

        print(f"FORMA-XIB: resolutio={w}x{h} testa={testa} taskbar={nb}/{na}")
        print(f"FORMA-XIB: colores iconarum={numeri} centra_vetera={centra_vetera} caeruleum_purum={purum_caeruleum}")
        print("RECTE: quattuor iconae premium in Bureau Sylviae realis adsunt et testa hodierna integra est.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
