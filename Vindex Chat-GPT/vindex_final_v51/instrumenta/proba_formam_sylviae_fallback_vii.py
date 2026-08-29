#!/usr/bin/env python3
"""P16-XI-B: absentibus assetis premium atlas P16-VII adhuc redditur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name("proba_formam_sylviae_i.py")
    spec = importlib.util.spec_from_file_location("aux_fallback_vii", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("auxilia framebuffer importari non possunt")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def principale() -> int:
    if len(sys.argv) != 5:
        print("USUS: proba_formam_sylviae_fallback_vii.py MONITOR QMP EXITUS MORA", file=sys.stderr)
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
        via = out / "forma-sylviae-fallback-vii.ppm"
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        # Testa IX manet, sed quattuor centra exacta atlas P16-VII redire debent.
        bronzeum = (185, 138, 82)
        aqua = (103, 164, 160)
        top = h - 40
        if aux.numerus_coloris_in_linea(pix, w, top, bronzeum) < w * 95 // 100:
            print("DEFECIT: taskbar fallback limen aeneum amisit", file=sys.stderr)
            return 5
        if aux.numerus_coloris_in_linea(pix, w, top + 2, aqua) < w * 95 // 100:
            print("DEFECIT: taskbar fallback lineam aqua amisit", file=sys.stderr)
            return 6

        centra = (
            ("PROGRAMMATA", 72, 104, (236, 194, 113)),
            ("TABULA", 72, 208, (201, 154, 82)),
            ("TERMINALE", 72, 312, (17, 28, 33)),
            ("OFFICINA", 72, 416, (232, 232, 217)),
        )
        for nomen, x, y, exspectatum in centra:
            visum = aux.pixel(pix, w, x, y)
            if visum != exspectatum:
                print(f"DEFECIT: fallback {nomen}: {visum} loco {exspectatum}", file=sys.stderr)
                return 7

        raster_nox = (27, 30, 31)
        copiae = []
        for y0 in (80, 184, 288, 392):
            n = aux.numerus_coloris_in_recto(pix, w, 48, y0, 96, y0 + 48, raster_nox)
            copiae.append(n)
            if n < 600:
                print(f"DEFECIT: tessera fallback incompleta ad y={y0}: {n}", file=sys.stderr)
                return 8

        print(f"FALLBACK-VII: centra=4/4 nox={copiae}")
        print("RECTE: sine assetis premium Sylvia atlas P16-VII canonice adhibet.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
