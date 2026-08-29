#!/usr/bin/env python3
"""P16-XII-D: horologium UEFI/TSC et motum interruptibilem in framebuffer QEMU metitur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name("proba_formam_sylviae_i.py")
    spec = importlib.util.spec_from_file_location("aux_tempus_motus", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("auxilia framebuffer importari non possunt")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def bronzeum(c: tuple[int, int, int]) -> bool:
    r, g, b = c
    return r > 120 and 85 < g < 175 and b < 115 and r > g + 25 and g > b + 20


def cyan(c: tuple[int, int, int]) -> bool:
    r, g, b = c
    return g > r + 70 and b > r + 90 and b >= g


def longitudo_barrae(aux: object, pix: bytes, w: int, x0: int, y: int, pred) -> int:
    n = 0
    for x in range(x0, x0 + 300):
        if pred(aux.pixel(pix, w, x, y)):
            n += 1
        else:
            break
    return n


def principale() -> int:
    if len(sys.argv) != 4:
        print("USUS: proba_showroom_tempus_motus_x.py MONITOR EXITUS MORA", file=sys.stderr)
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
        via = out / "showroom-tempus-motus-x.ppm"
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        # Status internus: viride tantum si TSC, continuitas et finis omnes recti sunt.
        status = aux.pixel(pix, w, 55, h - 62)
        if not (status[1] > status[0] + 45 and status[1] > status[2] + 30 and status[0] > 70):
            print(f"DEFECIT: status temporis non viridis est: {status}", file=sys.stderr)
            return 5

        # Panel post retargetationem ad destinationem secundam exactam pervenit.
        top = aux.pixel(pix, w, 870, 361)
        centrum = aux.pixel(pix, w, 870, 420)
        if not (top[1] > top[0] + 55 and top[2] > top[0] + 65):
            print(f"DEFECIT: ora cyan ad metam secundam deest: {top}", file=sys.stderr)
            return 6
        if not (centrum[1] > centrum[0] + 45 and centrum[2] > centrum[0] + 55):
            print(f"DEFECIT: corpus aqua ad metam secundam deest: {centrum}", file=sys.stderr)
            return 7

        # Locus initialis iam restitutus est ex fundo scenae.
        vetus = aux.pixel(pix, w, 100, 210)
        if vetus[1] > vetus[0] + 55 and vetus[2] > vetus[0] + 65:
            print(f"DEFECIT: residuum panelis in loco initiali mansit: {vetus}", file=sys.stderr)
            return 8

        # Vestigia bronzea sunt frames re vera praesentatae, non frames logicae omnes.
        n_bronze = 0
        for y in range(210, 535):
            for x in range(150, 910):
                if bronzeum(aux.pixel(pix, w, x, y)):
                    n_bronze += 1
        if n_bronze < 110:
            print(f"DEFECIT: vestigia motus nimis pauca sunt: {n_bronze}", file=sys.stderr)
            return 9

        # Telemetria codificata: III pixela = una frame logica.
        saltus_px = longitudo_barrae(aux, pix, w, 800, h - 70, cyan)
        omissae_px = longitudo_barrae(aux, pix, w, 800, h - 50, bronzeum)
        if saltus_px <= 0 or saltus_px % 3 != 0 or omissae_px % 3 != 0:
            print(f"DEFECIT: telemetria catch-up invalida: px={saltus_px}/{omissae_px}", file=sys.stderr)
            return 10
        saltus_max = saltus_px // 3
        omissae = omissae_px // 3

        colores = {tuple(pix[i:i+3]) for i in range(0, len(pix)-2, 3)}
        if len(colores) < 300:
            print(f"DEFECIT: varietas framebuffer nimis parva est: {len(colores)}", file=sys.stderr)
            return 11

        print(f"TEMPUS-MOTUS-X: resolutio={w}x{h} colores={len(colores)}")
        print(f"TEMPUS-MOTUS-X: status={status} top={top} centrum={centrum} vetus={vetus}")
        print(f"TEMPUS-MOTUS-X: pixela bronzea trajectoriae={n_bronze}")
        print(f"TEMPUS-MOTUS-X: saltus-max={saltus_max} frames; praesentationes-omissae={omissae}")
        print("RECTE: TSC reale, UEFI pacer, catch-up, retargetatio et motus frame sub QEMU probata sunt.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
