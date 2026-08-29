#!/usr/bin/env python3
"""P16-XII: compositorem modernum Graphica X in framebuffer vero metitur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name("proba_formam_sylviae_i.py")
    spec = importlib.util.spec_from_file_location("aux_graphica_x", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("auxilia framebuffer importari non possunt")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lumen(c: tuple[int, int, int]) -> int:
    return c[0] + c[1] + c[2]


def linea(aux: object, pix: bytes, w: int, y: int, x0: int, x1: int) -> list[tuple[int, int, int]]:
    return [aux.pixel(pix, w, x, y) for x in range(x0, x1)]


def contrastus(cs: list[tuple[int, int, int]]) -> int:
    if len(cs) < 2:
        return 0
    return max(sum(abs(a[i] - b[i]) for i in range(3)) for a, b in zip(cs, cs[1:]))


def principale() -> int:
    if len(sys.argv) != 4:
        print("USUS: proba_showroom_graphica_x.py MONITOR EXITUS MORA", file=sys.stderr)
        return 2
    aux = auxilia()
    mon_via, out, mora = Path(sys.argv[1]), Path(sys.argv[2]), float(sys.argv[3])
    finis = time.time() + 15.0
    while not mon_via.exists() and time.time() < finis:
        time.sleep(0.1)
    if not mon_via.exists():
        print("DEFECIT: monitor QEMU deest", file=sys.stderr)
        return 3

    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    monitor.settimeout(0.5)
    monitor.connect(str(mon_via))
    try:
        aux.lege_usque(monitor, b"(qemu) ", 2.0)
        time.sleep(mora)
        via = out / "showroom-graphica-x.ppm"
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        # Eadem textura striata extra et intra vitrum: blur debet colores intermedios creare.
        extra = linea(aux, pix, w, 300, 72, 244)
        intra = linea(aux, pix, w, 300, 320, 960)
        u_extra = len(set(extra))
        u_intra = len(set(intra))
        c_extra = contrastus(extra)
        c_intra = contrastus(intra)
        if u_extra > 6:
            print(f"DEFECIT: textura referentiae nimis varia est: {u_extra}", file=sys.stderr)
            return 5
        if u_intra < u_extra + 8:
            print(f"DEFECIT: vitrum colores intermedios non creavit: extra={u_extra} intra={u_intra}", file=sys.stderr)
            return 6
        if c_intra >= c_extra:
            print(f"DEFECIT: blur contrastum non minuit: extra={c_extra} intra={c_intra}", file=sys.stderr)
            return 7

        # Umbra mollis sub fenestra luminantiam localiter deprimit.
        sub_umbra = aux.pixel(pix, w, 650, 580)
        longe = aux.pixel(pix, w, 650, 620)
        if lumen(sub_umbra) >= lumen(longe) - 12:
            print(f"DEFECIT: umbra mollis non satis manifesta est: {sub_umbra} vs {longe}", file=sys.stderr)
            return 8

        # Duo strata translucentia miscentur in intersectione, non unum alterum delet.
        aqua = aux.pixel(pix, w, 430, 390)
        mixtum = aux.pixel(pix, w, 590, 390)
        bronze = aux.pixel(pix, w, 760, 390)
        if mixtum == aqua or mixtum == bronze or aqua == bronze:
            print(f"DEFECIT: source-over stratificatum non manifestum: {aqua}/{mixtum}/{bronze}", file=sys.stderr)
            return 9

        # Showroom totum plus quam paucos colores procedurales continet.
        colores = {tuple(pix[i:i+3]) for i in range(0, len(pix)-2, 3)}
        if len(colores) < 500:
            print(f"DEFECIT: varietas framebuffer nimis parva est: {len(colores)}", file=sys.stderr)
            return 10

        print(f"GRAPHICA-X: resolutio={w}x{h} colores={len(colores)}")
        print(f"GRAPHICA-X: vitrum colores={u_extra}->{u_intra} contrastus={c_extra}->{c_intra}")
        print(f"GRAPHICA-X: umbra lumen={lumen(sub_umbra)}/{lumen(longe)} strata={aqua}/{mixtum}/{bronze}")
        print("RECTE: Graphica X RGBA, blur, vitrum, umbra et compositio in framebuffer vero probata sunt.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
