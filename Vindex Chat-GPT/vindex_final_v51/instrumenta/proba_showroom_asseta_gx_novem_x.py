#!/usr/bin/env python3
"""P16-XII-C2: pontem SIMG II/Graphica IX ad GX 9-slice in QEMU metitur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name("proba_formam_sylviae_i.py")
    spec = importlib.util.spec_from_file_location("aux_asseta_gx_novem", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("auxilia framebuffer importari non possunt")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lumen(c: tuple[int, int, int]) -> int:
    return c[0] + c[1] + c[2]


def magenta_occultum(c: tuple[int, int, int]) -> bool:
    r, g, b = c
    return r > g + 80 and b > g + 80 and abs(r - b) < 55


def numerus_conditionis(aux: object, pix: bytes, w: int, x0: int, y0: int, x1: int, y1: int, pred) -> int:
    n = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            if pred(aux.pixel(pix, w, x, y)):
                n += 1
    return n


def principale() -> int:
    if len(sys.argv) != 4:
        print("USUS: proba_showroom_asseta_gx_novem_x.py MONITOR EXITUS MORA", file=sys.stderr)
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
        via = out / "showroom-asseta-gx-novem-x.ppm"
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        # Ora superior utriusque magnitudinis aqua manet; post IV px centrum incipit.
        m_top = aux.pixel(pix, w, 360, 152)
        m_after = aux.pixel(pix, w, 360, 156)
        p_top = aux.pixel(pix, w, 850, 332)
        p_after = aux.pixel(pix, w, 850, 336)
        if not (m_top[1] > m_top[0] + 45 and m_top[2] > m_top[0] + 55):
            print(f"DEFECIT: ora aqua magna deest: {m_top}", file=sys.stderr)
            return 5
        if not (p_top[1] > p_top[0] + 35 and p_top[2] > p_top[0] + 45):
            print(f"DEFECIT: ora aqua parva deest: {p_top}", file=sys.stderr)
            return 6
        if lumen(m_top) <= lumen(m_after) + 55 or lumen(p_top) <= lumen(p_after) + 40:
            print(f"DEFECIT: ora IV px videtur extensa: magna={m_top}/{m_after} parva={p_top}/{p_after}", file=sys.stderr)
            return 7

        # Ora inferior bronzea incipit eodem margine IV px in utraque magnitudine.
        m_bot = aux.pixel(pix, w, 360, 447)
        m_before = aux.pixel(pix, w, 360, 444)
        p_bot = aux.pixel(pix, w, 850, 532)
        p_before = aux.pixel(pix, w, 850, 529)
        if not (m_bot[0] > m_bot[1] > m_bot[2]) or not (p_bot[0] > p_bot[1] > p_bot[2]):
            print(f"DEFECIT: ora bronzea deest: magna={m_bot} parva={p_bot}", file=sys.stderr)
            return 8
        if lumen(m_bot) <= lumen(m_before) + 20 or lumen(p_bot) <= lumen(p_before) + 15:
            print(f"DEFECIT: limes inferior IV px non manifestus: {m_before}/{m_bot} {p_before}/{p_bot}", file=sys.stderr)
            return 9

        # Centrum semi-transparens e fonte uniformi tres tonos observatos ex duabus
        # fasciis fundi + linea decorativa producit. Unus tonus tantum alpha falsum indicaret.
        colores_centri_m = {aux.pixel(pix, w, x, 300) for x in range(160, 580)}
        colores_centri_p = {aux.pixel(pix, w, x, 420) for x in range(760, 1035)}
        if len(colores_centri_m) < 3 or len(colores_centri_p) < 3:
            print(f"DEFECIT: centrum alpha fundum celavit: colores={len(colores_centri_m)}/{len(colores_centri_p)}", file=sys.stderr)
            return 10

        # Magenta occultum in pixelis alpha=0 nullum halo in duobus materialibus facere potest.
        halo_m = numerus_conditionis(aux, pix, w, 116, 146, 624, 454, magenta_occultum)
        halo_p = numerus_conditionis(aux, pix, w, 731, 326, 1069, 539, magenta_occultum)
        if halo_m != 0 or halo_p != 0:
            print(f"DEFECIT: color occultus magenta in halo apparuit: {halo_m}/{halo_p}", file=sys.stderr)
            return 11

        # Flanc argentum distinctus est a centro vitreo in utraque superficie.
        m_side = aux.pixel(pix, w, 122, 300)
        m_center = aux.pixel(pix, w, 360, 300)
        p_side = aux.pixel(pix, w, 737, 420)
        p_center = aux.pixel(pix, w, 850, 420)
        if m_side == m_center or p_side == p_center:
            print(f"DEFECIT: flanc 9-slice in centrum extensum est: {m_side}/{m_center} {p_side}/{p_center}", file=sys.stderr)
            return 12
        if not (m_side[0] > 70 and m_side[1] > 80 and m_side[2] > 90):
            print(f"DEFECIT: flanc argentum magnae deest: {m_side}", file=sys.stderr)
            return 13

        # Showroom proceduraliter sobrius est; varietas hic sanitatem interpolationis
        # et alphae custodit, non abundantiam artisticam. Captura prima 323 colores habuit.
        colores = {tuple(pix[i:i+3]) for i in range(0, len(pix)-2, 3)}
        if len(colores) < 250:
            print(f"DEFECIT: varietas framebuffer nimis parva est: {len(colores)}", file=sys.stderr)
            return 14

        print(f"ASSETA-GX-X: resolutio={w}x{h} colores={len(colores)}")
        print(f"ASSETA-GX-X: ora magna top/centrum/bot={m_top}/{m_after}/{m_bot}")
        print(f"ASSETA-GX-X: ora parva top/centrum/bot={p_top}/{p_after}/{p_bot}")
        print(f"ASSETA-GX-X: centra colores={len(colores_centri_m)}/{len(colores_centri_p)} halo={halo_m}/{halo_p}")
        print(f"ASSETA-GX-X: flanc/centrum={m_side}/{m_center} | {p_side}/{p_center}")
        print("RECTE: SIMG II 9-slice in superficies GX et scena compositoris probatum est.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
