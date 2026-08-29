#!/usr/bin/env python3
"""P16-XI-B: INITIUM premium et semantica input sub QEMU/OVMF probantur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name("proba_initium_sylviae_ii.py")
    spec = importlib.util.spec_from_file_location("aux_xib_initium", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("auxilia INITII importari non possunt")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lumen(c: tuple[int, int, int]) -> int:
    return c[0] + c[1] + c[2]


def colores(aux: object, pix: bytes, w: int, regio: tuple[int, int, int, int]) -> set[tuple[int, int, int]]:
    x0, y0, x1, y1 = regio
    out: set[tuple[int, int, int]] = set()
    for y in range(y0, y1):
        for x in range(x0, x1):
            out.add(aux.pixel(pix, w, x, y))
    return out


def initium_top_quaere(pix: bytes, w: int, h: int, bronzeum: tuple[int, int, int]) -> int | None:
    for y in range(120, h - 120):
        if pix[(y*w+20)*3:(y*w+20)*3+3] != bytes(bronzeum):
            continue
        if pix[(y*w+300)*3:(y*w+300)*3+3] != bytes(bronzeum):
            continue
        return y
    return None


def principale() -> int:
    if len(sys.argv) != 5:
        print("USUS: proba_initium_sylviae_xib.py MONITOR QMP EXITUS MORA", file=sys.stderr)
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
        ante = out / "initium-xib-ante.ppm"
        apertum = out / "initium-xib-apertum.ppm"
        hover = out / "initium-xib-hover.ppm"
        post = out / "initium-xib-post.ppm"
        aux.captura(monitor, ante)
        w, h, pix_ante = aux.ppm(ante)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        taskbar_top = h - 40
        init_ante = aux.pixel(pix_ante, w, 50, taskbar_top + 8)
        pos_initium = aux.move_ad(monitor, out, "initium-xib", 50, 770, w, h)
        aux.click(monitor)
        aux.captura(monitor, apertum)
        _, _, pix_open = aux.ppm(apertum)

        bronzeum = (185, 138, 82)
        menu_top = initium_top_quaere(pix_open, w, h, bronzeum)
        if menu_top is None:
            print("DEFECIT: INITIUM non apertum est", file=sys.stderr)
            return 5

        caput_top = aux.pixel(pix_open, w, 180, menu_top + 8)
        caput_bottom = aux.pixel(pix_open, w, 180, menu_top + 54)
        if caput_top == caput_bottom or lumen(caput_top) <= lumen(caput_bottom):
            print(f"DEFECIT: materia capitis INITII deest: {caput_top}->{caput_bottom}", file=sys.stderr)
            return 6

        prima_y = menu_top + 92
        regiones: list[tuple[str, tuple[int, int, int, int]]] = []
        for i, nomen in enumerate(("PROGRAMMATA", "TABULA", "TERMINALE", "OFFICINA")):
            iy = prima_y + i * 54
            regiones.append((nomen, (24, iy + 6, 56, iy + 38)))

        numeri: list[int] = []
        purum_caeruleum = 0
        for nomen, regio in regiones:
            cs = colores(aux, pix_open, w, regio)
            numeri.append(len(cs))
            if len(cs) < 45:
                print(f"DEFECIT: icona INITII {nomen} non est premium: colores={len(cs)}", file=sys.stderr)
                return 7
            for y in range(regio[1], regio[3]):
                for x in range(regio[0], regio[2]):
                    if aux.pixel(pix_open, w, x, y) == (0, 0, 255):
                        purum_caeruleum += 1
        if purum_caeruleum != 0:
            print(f"DEFECIT: halo caeruleus in INITIO: {purum_caeruleum}", file=sys.stderr)
            return 8

        # Alpha premium debet materiam eburneam in angulis iconarum relinquere;
        # quadratum nox 32×32 atlas veteris non iam dominatur.
        nox = (28, 31, 32)
        nox_total = 0
        for _, regio in regiones:
            for y in range(regio[1], regio[3]):
                for x in range(regio[0], regio[2]):
                    if aux.pixel(pix_open, w, x, y) == nox:
                        nox_total += 1
        if nox_total > 700:
            print(f"DEFECIT: quadrata obscura atlas veteris restant: nox={nox_total}", file=sys.stderr)
            return 9

        # Hover TABULA mutat tesseram, non PROGRAMMATA.
        prog_scopus = prima_y + 22
        tab_scopus = prima_y + 54 + 22
        prog_ante = aux.pixel(pix_open, w, 300, prog_scopus)
        tab_ante = aux.pixel(pix_open, w, 300, tab_scopus)
        pos_tabula = aux.move_ad(monitor, out, "tabula-xib", 150, tab_scopus, w, h)
        aux.captura(monitor, hover)
        _, _, pix_hover = aux.ppm(hover)
        prog_post = aux.pixel(pix_hover, w, 300, prog_scopus)
        tab_post = aux.pixel(pix_hover, w, 300, tab_scopus)
        if tab_post == tab_ante or prog_post != prog_ante:
            print(f"DEFECIT: hover TABULAE contractum fregit: T={tab_ante}->{tab_post} P={prog_ante}->{prog_post}", file=sys.stderr)
            return 10
        if aux.pixel(pix_hover, w, 16, tab_scopus) != bronzeum:
            print("DEFECIT: linea hover TABULAE deest", file=sys.stderr)
            return 11

        # Click TABULA claudit INITIUM et fenestram historicam focat.
        aux.click(monitor)
        aux.captura(monitor, post)
        _, _, pix_post = aux.ppm(post)
        if initium_top_quaere(pix_post, w, h, bronzeum) is not None:
            print("DEFECIT: INITIUM post electionem adhuc apertum est", file=sys.stderr)
            return 12
        if aux.pixel(pix_post, w, 700, 168) != bronzeum:
            print(f"DEFECIT: focus TABULAE non rediit: {aux.pixel(pix_post,w,700,168)}", file=sys.stderr)
            return 13

        init_open = aux.pixel(pix_open, w, 50, taskbar_top + 8)
        if init_open == init_ante:
            print("DEFECIT: status INITII taskbar non mutatur", file=sys.stderr)
            return 14

        print(f"INITIUM-XIB: top={menu_top} cursor={pos_initium}->{pos_tabula}")
        print(f"INITIUM-XIB: colores={numeri} nox={nox_total} caeruleum_purum={purum_caeruleum}")
        print("RECTE: INITIUM asseta premium recipit et hover/click/focus servantur.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
