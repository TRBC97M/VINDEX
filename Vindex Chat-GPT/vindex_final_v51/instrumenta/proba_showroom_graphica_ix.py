#!/usr/bin/env python3
"""Graphica IX: rasteram premium in framebuffer vero QEMU/OVMF metitur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name("proba_formam_sylviae_i.py")
    spec = importlib.util.spec_from_file_location("aux_graphica_ix", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("auxilia framebuffer importari non possunt")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def colores_recti(aux: object, pix: bytes, w: int, x0: int, y0: int, x1: int, y1: int) -> set[tuple[int, int, int]]:
    colores: set[tuple[int, int, int]] = set()
    for y in range(y0, y1):
        for x in range(x0, x1):
            colores.add(aux.pixel(pix, w, x, y))
    return colores


def numerus_caerulei_occulti(aux: object, pix: bytes, w: int, x0: int, y0: int, x1: int, y1: int) -> int:
    n = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            r, g, b = aux.pixel(pix, w, x, y)
            if b > r + 24 and b > g + 24:
                n += 1
    return n


def principale() -> int:
    if len(sys.argv) != 4:
        print("USUS: proba_showroom_graphica_ix.py MONITOR EXITUS MORA", file=sys.stderr)
        return 2
    aux = auxilia()
    monitor_via, out, mora = Path(sys.argv[1]), Path(sys.argv[2]), float(sys.argv[3])
    finis = time.time() + 15.0
    while not monitor_via.exists() and time.time() < finis:
        time.sleep(0.1)
    if not monitor_via.exists():
        print("DEFECIT: monitor QEMU deest", file=sys.stderr)
        return 3

    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    monitor.settimeout(0.5)
    monitor.connect(str(monitor_via))
    try:
        aux.lege_usque(monitor, b"(qemu) ", 2.0)
        time.sleep(mora)
        via = out / "showroom-graphica-ix.ppm"
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        # Duo specimina ex eodem SIMG II: nearest paucis coloribus, premium multis gradibus.
        nearest = colores_recti(aux, pix, w, 224, 224, 444, 444)
        premium = colores_recti(aux, pix, w, 742, 224, 962, 444)
        if len(nearest) > 8:
            print(f"DEFECIT: nearest nimis multos colores habet: {len(nearest)}", file=sys.stderr)
            return 5
        if len(premium) < len(nearest) + 12:
            print(f"DEFECIT: rastera premium non satis interpolat: nearest={len(nearest)} premium={len(premium)}", file=sys.stderr)
            return 6

        # Pixel caeruleus in fonte alpha=0 est. Alpha praemultiplicata eum nunquam halo facit.
        halo = numerus_caerulei_occulti(aux, pix, w, 742, 224, 962, 444)
        if halo != 0:
            print(f"DEFECIT: color occultus caeruleus in halo apparuit: {halo} pixela", file=sys.stderr)
            return 7

        # 9-slice metadata SIMG II: ora superior aqua et inferior bronze manent continuae.
        aqua = (189, 239, 242)
        bronze = (181, 138, 84)
        aqua_n = aux.numerus_coloris_in_linea(pix, w, 516, aqua)
        bronze_n = aux.numerus_coloris_in_linea(pix, w, 627, bronze)
        if aqua_n < 900 or bronze_n < 900:
            print(f"DEFECIT: 9-slice premium non manifestum: aqua={aqua_n} bronze={bronze_n}", file=sys.stderr)
            return 8

        # Via superficiei privatae redit in framebuffer: icon aqua in capsula inferiori adest.
        aqua_surface = aux.numerus_coloris_in_recto(pix, w, 398, 662, 454, 718, aqua)
        if aqua_surface < 100:
            print(f"DEFECIT: compositio superficiei Graphica IX deest: aqua={aqua_surface}", file=sys.stderr)
            return 9

        # Titulus premium in regio dextra vere redditur, non framebuffer vacuum.
        ebur = (242, 244, 247)
        titulus = aux.numerus_coloris_in_recto(pix, w, 636, 182, 930, 202, ebur)
        if titulus < 20:
            print(f"DEFECIT: titulus premium deest: ebur={titulus}", file=sys.stderr)
            return 10

        print(f"GRAPHICA-IX: resolutio={w}x{h}")
        print(f"GRAPHICA-IX: nearest={len(nearest)} colores premium={len(premium)} colores halo={halo}")
        print(f"GRAPHICA-IX: 9slice aqua/bronze={aqua_n}/{bronze_n} superficies_aqua={aqua_surface}")
        print("RECTE: Graphica IX alpha-bilinearis in framebuffer vero QEMU/OVMF probata est.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
