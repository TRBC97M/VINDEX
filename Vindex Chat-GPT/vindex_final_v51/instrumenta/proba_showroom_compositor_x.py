#!/usr/bin/env python3
"""P16-XII-B: scenam Graphica X, Z et praesentiam regionalem in QEMU metitur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name("proba_formam_sylviae_i.py")
    spec = importlib.util.spec_from_file_location("aux_compositor_x", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("auxilia framebuffer importari non possunt")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lumen(c: tuple[int, int, int]) -> int:
    return c[0] + c[1] + c[2]


def principale() -> int:
    if len(sys.argv) != 4:
        print("USUS: proba_showroom_compositor_x.py MONITOR EXITUS MORA", file=sys.stderr)
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
        via = out / "showroom-compositor-x.ppm"
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        bronzeum = (181, 138, 84)
        magenta = (255, 0, 255)
        linea = (32, 91, 112)

        # Canarius extra unionem damni post secundam praesentiam superesse debet.
        extra = aux.pixel(pix, w, 45, h - 54)
        if extra != bronzeum:
            print(f"DEFECIT: praesentia totum framebuffer repinxit: canarius={extra}", file=sys.stderr)
            return 5

        # Canarius intra vetus stratum deleri debet et fundum exactum restitui.
        intra = aux.pixel(pix, w, 195, 215)
        if intra == magenta or intra != linea:
            print(f"DEFECIT: locus vetus strati non est ex fundo restitutus: {intra}", file=sys.stderr)
            return 6

        # Regiones A, B et overlap debent tres facies diversas habere.
        a = aux.pixel(pix, w, 400, 300)
        mixtum = aux.pixel(pix, w, 600, 340)
        b = aux.pixel(pix, w, 800, 340)
        if a == mixtum or b == mixtum or a == b:
            print(f"DEFECIT: Z/source-over scenae non manifestum est: A={a} M={mixtum} B={b}", file=sys.stderr)
            return 7
        if not (a[1] > a[0] and a[2] > a[0]):
            print(f"DEFECIT: stratum A identitatem aquaticam amisit: {a}", file=sys.stderr)
            return 8
        if not (b[0] > b[1] > b[2]):
            print(f"DEFECIT: stratum B identitatem aeneam amisit: {b}", file=sys.stderr)
            return 9

        # Umbra A est stratum separatum. x=258 intra marginem blur est, sed adhuc
        # extra panel quod x=260 incipit; eadem columna infra umbram dat referentiam.
        umbra = aux.pixel(pix, w, 258, 300)
        sine_umbra = aux.pixel(pix, w, 258, 470)
        if lumen(umbra) >= lumen(sine_umbra) - 10:
            print(f"DEFECIT: umbra strati non videtur: {umbra}/{sine_umbra}", file=sys.stderr)
            return 10

        # Magenta intra damage nusquam superesse debet in regione veteris A.
        magentae = aux.numerus_coloris_in_recto(pix, w, 150, 170, 240, 250, magenta)
        if magentae != 0:
            print(f"DEFECIT: canarius interior post damage remansit: {magentae}", file=sys.stderr)
            return 11

        colores = {tuple(pix[i:i+3]) for i in range(0, len(pix)-2, 3)}
        if len(colores) < 450:
            print(f"DEFECIT: scena compositoris nimis paucos colores habet: {len(colores)}", file=sys.stderr)
            return 12

        print(f"COMPOSITOR-X: resolutio={w}x{h} colores={len(colores)}")
        print(f"COMPOSITOR-X: canarii extra/intra={extra}/{intra}")
        print(f"COMPOSITOR-X: strata A/M/B={a}/{mixtum}/{b}")
        print(f"COMPOSITOR-X: umbra lumen={lumen(umbra)}/{lumen(sine_umbra)}")
        print("RECTE: scena Z, backbuffer et praesentia damage-only in framebuffer QEMU probata sunt.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
