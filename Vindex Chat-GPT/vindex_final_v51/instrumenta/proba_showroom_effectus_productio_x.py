#!/usr/bin/env python3
"""P16-XII-C1: caches, backdrop, mascam, clip et gloss in QEMU metitur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name("proba_formam_sylviae_i.py")
    spec = importlib.util.spec_from_file_location("aux_effectus_productio_x", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("auxilia framebuffer importari non possunt")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lumen(c: tuple[int, int, int]) -> int:
    return c[0] + c[1] + c[2]


def linea(aux: object, pix: bytes, w: int, y: int, x0: int, x1: int) -> list[tuple[int, int, int]]:
    return [aux.pixel(pix, w, x, y) for x in range(x0, x1)]


def contrastus_medius(cs: list[tuple[int, int, int]]) -> float:
    if len(cs) < 2:
        return 0.0
    vals = [sum(abs(a[i] - b[i]) for i in range(3)) for a, b in zip(cs, cs[1:])]
    return sum(vals) / len(vals)


def principale() -> int:
    if len(sys.argv) != 4:
        print("USUS: proba_showroom_effectus_productio_x.py MONITOR EXITUS MORA", file=sys.stderr)
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
        via = out / "showroom-effectus-productio-x.ppm"
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        # Textura altae frequentiae extra vitrum contra eandem latitudinem intra cardam.
        extra = linea(aux, pix, w, 118, 160, 520)
        intra = linea(aux, pix, w, 255, 160, 520)
        c_extra = contrastus_medius(extra)
        c_intra = contrastus_medius(intra)
        if c_extra < 8.0 or c_intra >= c_extra * 0.72:
            print(f"DEFECIT: backdrop blur contrastum non satis minuit: extra={c_extra:.2f} intra={c_intra:.2f}", file=sys.stderr)
            return 5

        # Masca rotunda: centrum anguli non debet eandem materiam opacam ac centrum habere.
        angulus = aux.pixel(pix, w, 161, 161)
        centrum = aux.pixel(pix, w, 340, 260)
        if angulus == centrum or lumen(centrum) <= lumen(angulus) + 20:
            print(f"DEFECIT: masca rotunda non manifesta est: angulus={angulus} centrum={centrum}", file=sys.stderr)
            return 6

        # Gloss: eadem columna in superiore tertio clarior quam pars inferior.
        supra = aux.pixel(pix, w, 500, 176)
        infra = aux.pixel(pix, w, 500, 350)
        if lumen(supra) <= lumen(infra) + 18:
            print(f"DEFECIT: gloss non satis manifestus est: supra={supra} infra={infra}", file=sys.stderr)
            return 7

        # Clip: ribbon tantum ab x=208 ad x<468 extenditur.
        ante = aux.pixel(pix, w, 198, 310)
        ribbon = aux.pixel(pix, w, 250, 310)
        post = aux.pixel(pix, w, 480, 310)
        if ribbon == ante or ribbon == post:
            print(f"DEFECIT: clip materializatus non manifestus est: {ante}/{ribbon}/{post}", file=sys.stderr)
            return 8
        if not (ribbon[1] > ribbon[0] and ribbon[2] > ribbon[0]):
            print(f"DEFECIT: ribbon identitatem cyan amisit: {ribbon}", file=sys.stderr)
            return 9

        # Umbra extra cardam ad x=156 lumen minuit contra eandem columnam infra effectum.
        umbra = aux.pixel(pix, w, 156, 250)
        sine = aux.pixel(pix, w, 156, 620)
        if lumen(umbra) >= lumen(sine) - 8:
            print(f"DEFECIT: umbra cacheata non videtur: {umbra}/{sine}", file=sys.stderr)
            return 10

        # Secunda carda bronzea manet distincta a prima aqua.
        aqua = aux.pixel(pix, w, 340, 260)
        bronze = aux.pixel(pix, w, 820, 420)
        if aqua == bronze or not (aqua[1] > aqua[0] and aqua[2] > aqua[0]) or not (bronze[0] > bronze[1] > bronze[2]):
            print(f"DEFECIT: identitates cardarum non servantur: aqua={aqua} bronze={bronze}", file=sys.stderr)
            return 11

        colores = {tuple(pix[i:i+3]) for i in range(0, len(pix)-2, 3)}
        if len(colores) < 650:
            print(f"DEFECIT: varietas framebuffer nimis parva est: {len(colores)}", file=sys.stderr)
            return 12

        print(f"EFFECTUS-X: resolutio={w}x{h} colores={len(colores)}")
        print(f"EFFECTUS-X: contrastus extra/intra={c_extra:.2f}/{c_intra:.2f}")
        print(f"EFFECTUS-X: masca angulus/centrum={angulus}/{centrum}")
        print(f"EFFECTUS-X: gloss lumen={lumen(supra)}/{lumen(infra)}")
        print(f"EFFECTUS-X: clip={ante}/{ribbon}/{post} umbra={lumen(umbra)}/{lumen(sine)}")
        print("RECTE: caches, backdrop, masca, clip et gloss in framebuffer QEMU probata sunt.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
