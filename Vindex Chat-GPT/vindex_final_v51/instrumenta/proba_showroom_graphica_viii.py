#!/usr/bin/env python3
"""Graphica VIII: showroom verum in framebuffer QEMU/OVMF metitur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name("proba_formam_sylviae_i.py")
    spec = importlib.util.spec_from_file_location("aux_graphica_viii", via)
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


def principale() -> int:
    if len(sys.argv) != 4:
        print("USUS: proba_showroom_graphica_viii.py MONITOR EXITUS MORA", file=sys.stderr)
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
        via = out / "showroom-graphica-viii.ppm"
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        # Background vere graduatus est.
        top = aux.pixel(pix, w, 20, 12)
        bottom = aux.pixel(pix, w, 20, h - 12)
        if top == bottom:
            print(f"DEFECIT: gradientia fundi deest: {top}", file=sys.stderr)
            return 5

        # Materia 9-slice: ora aquatica superior et ora aenea inferior servantur.
        aqua_m = (184, 232, 230)
        bronze_m = (181, 137, 82)
        aqua_n = aux.numerus_coloris_in_linea(pix, w, 150, aqua_m)
        bronze_n = aux.numerus_coloris_in_linea(pix, w, 371, bronze_m)
        if aqua_n < 300 or bronze_n < 300:
            print(f"DEFECIT: novem-partes non manifestae: aqua={aqua_n} bronze={bronze_n}", file=sys.stderr)
            return 6

        # Scaling bilineare plures gradus colorum quam nearest-neighbour gignere debet.
        nearest = colores_recti(aux, pix, w, 616, 222, 748, 334)
        linear = colores_recti(aux, pix, w, 780, 222, 912, 334)
        if len(nearest) > 12:
            print(f"DEFECIT: specimen nearest nimis multos colores habet: {len(nearest)}", file=sys.stderr)
            return 7
        if len(linear) < len(nearest) + 20:
            print(f"DEFECIT: bilinearis non interpolat satis: nearest={len(nearest)} linear={len(linear)}", file=sys.stderr)
            return 8

        # Titulus atlas VINDEX: interior plene eburneus et margines alpha graduati.
        ebur = (241, 238, 228)
        ebur_n = aux.numerus_coloris_in_recto(pix, w, 82, 62, 300, 84, ebur)
        tituli_colores = colores_recti(aux, pix, w, 82, 62, 300, 84)
        if ebur_n < 30 or len(tituli_colores) < 8:
            print(f"DEFECIT: typographia atlas non manifesta: ebur={ebur_n} colores={len(tituli_colores)}", file=sys.stderr)
            return 9

        # Emblema SIMG a XXXII ad LXXXII scalatum vere multicolorem manet.
        emblema_colores = colores_recti(aux, pix, w, 1062, 238, 1144, 320)
        if len(emblema_colores) < 12:
            print(f"DEFECIT: SIMG scalatum nimis simplex: colores={len(emblema_colores)}", file=sys.stderr)
            return 10

        # Button rotundus: centrum graphite, angulus non idem ac centrum.
        centrum = aux.pixel(pix, w, 199, 277)
        angulus = aux.pixel(pix, w, 110, 246)
        if centrum == angulus:
            print("DEFECIT: rectangulum rotundum angulum non secat", file=sys.stderr)
            return 11

        print(f"GRAPHICA-VIII: resolutio={w}x{h} fundum={top}->{bottom}")
        print(f"GRAPHICA-VIII: 9slice aqua/bronze={aqua_n}/{bronze_n}")
        print(f"GRAPHICA-VIII: scaling nearest={len(nearest)} colores, bilinear={len(linear)} colores")
        print(f"GRAPHICA-VIII: typographia ebur={ebur_n} colores={len(tituli_colores)} emblema={len(emblema_colores)}")
        print("RECTE: showroom Graphica VIII in framebuffer vero QEMU/OVMF probatum est.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
