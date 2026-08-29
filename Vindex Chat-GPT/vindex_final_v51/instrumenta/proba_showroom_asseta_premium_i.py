#!/usr/bin/env python3
"""P16-XI-A: asseta PNG/SIMG II realia in framebuffer QEMU metitur."""
from __future__ import annotations

import importlib.util
import json
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name("proba_formam_sylviae_i.py")
    spec = importlib.util.spec_from_file_location("aux_asseta_premium_i", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("auxilia framebuffer importari non possunt")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def colores(aux: object, pix: bytes, w: int, rect: tuple[int, int, int, int]) -> set[tuple[int, int, int]]:
    x0, y0, x1, y1 = rect
    return {aux.pixel(pix, w, x, y) for y in range(y0, y1) for x in range(x0, x1)}


def numerus(aux: object, pix: bytes, w: int, rect: tuple[int, int, int, int], praedicatum) -> int:
    x0, y0, x1, y1 = rect
    n = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            if praedicatum(aux.pixel(pix, w, x, y)):
                n += 1
    return n


def principale() -> int:
    if len(sys.argv) != 4:
        print("USUS: proba_showroom_asseta_premium_i.py MONITOR EXITUS MORA", file=sys.stderr)
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
        via = out / "showroom-asseta-premium-i.ppm"
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        nearest_rect = (164, 208, 400, 420)
        premium_rect = (612, 208, 848, 420)
        nearest = colores(aux, pix, w, nearest_rect)
        premium = colores(aux, pix, w, premium_rect)
        if len(nearest) < 120:
            print(f"DEFECIT: assetum nearest nimis simplex/vacuum: {len(nearest)}", file=sys.stderr)
            return 5
        if len(premium) < len(nearest) + 350:
            print(f"DEFECIT: premium interpolationem non manifestat: nearest={len(nearest)} premium={len(premium)}", file=sys.stderr)
            return 6

        halo = numerus(
            aux,
            pix,
            w,
            premium_rect,
            lambda c: c[2] > c[0] + 80 and c[2] > c[1] + 80,
        )
        if halo > 4:
            print(f"DEFECIT: halo caeruleus suspectus: {halo} pixela", file=sys.stderr)
            return 7

        laurea = (104, 177, 123)
        status_recta = ((988, 206, 1002, 220), (988, 272, 1002, 286), (988, 360, 1002, 374))
        status = [aux.numerus_coloris_in_recto(pix, w, *r, laurea) for r in status_recta]
        if min(status) < 170:
            print(f"DEFECIT: selectio multi-scala non exacta: {status}", file=sys.stderr)
            return 8

        familia_recta = (
            (108, 548, 220, 660),
            (310, 548, 422, 660),
            (512, 548, 624, 660),
            (714, 548, 826, 660),
        )
        signa: list[tuple[int, int]] = []
        fundum = (22, 30, 35)
        for i, r in enumerate(familia_recta, 1):
            cs = colores(aux, pix, w, r)
            activi = numerus(aux, pix, w, r, lambda c: c != fundum)
            if len(cs) < 80 or activi < 1700:
                print(f"DEFECIT: icona familiae {i} vacua/simplex: colores={len(cs)} activi={activi}", file=sys.stderr)
                return 9
            signa.append((len(cs), activi))
        if len(set(signa)) < 3:
            print(f"DEFECIT: familia iconarum non satis distincta: {signa}", file=sys.stderr)
            return 10

        surface = (1032, 566, 1144, 678)
        surface_activa = numerus(aux, pix, w, surface, lambda c: c != (26, 29, 32))
        if surface_activa < 1700:
            print(f"DEFECIT: via superficiei privata vacua: {surface_activa}", file=sys.stderr)
            return 11

        finis_ok = aux.numerus_coloris_in_recto(pix, w, 1182, 708, 1194, 720, laurea)
        if finis_ok < 130:
            print(f"DEFECIT: marca completionis deest: {finis_ok}", file=sys.stderr)
            return 12

        metra = {
            "resolutio": [w, h],
            "nearest_colores": len(nearest),
            "premium_colores": len(premium),
            "halo_caeruleus": halo,
            "status_scalae": status,
            "familia": signa,
            "superficies_activa": surface_activa,
        }
        (out / "metra-asseta-premium-i.json").write_text(
            json.dumps(metra, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        print(f"ASSETA-PREMIUM-I: nearest={len(nearest)} premium={len(premium)} halo={halo}")
        print(f"ASSETA-PREMIUM-I: scalae={status} familia={signa} superficies={surface_activa}")
        print("RECTE: asseta premium realia PNG/SIMG II per Graphica IX in QEMU/OVMF probata sunt.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
