#!/usr/bin/env python3
"""P16-XI: bureau, hover, launch, clausura et relaunch cum taskbar IX sub UEFI/QEMU comprobantur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def importa_auxilia() -> object:
    via = Path(__file__).resolve().with_name('proba_initium_sylviae_ii.py')
    spec = importlib.util.spec_from_file_location('proba_initium_ii', via)
    if spec is None or spec.loader is None:
        raise RuntimeError('probator INITIUM importari non potest')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lumen(color: tuple[int, int, int]) -> int:
    return color[0] + color[1] + color[2]


def differentiae_rect(p1: bytes, p2: bytes, w: int, x0: int, y0: int, x1: int, y1: int) -> int:
    n = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            i = (y * w + x) * 3
            if p1[i:i+3] != p2[i:i+3]:
                n += 1
    return n


def copia_coloris(pix: bytes, w: int, x0: int, y0: int, x1: int, y1: int, color: tuple[int, int, int]) -> int:
    n = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            i = (y * w + x) * 3
            if tuple(pix[i:i+3]) == color:
                n += 1
    return n


def principale() -> int:
    if len(sys.argv) != 5:
        print('USUS: proba_bureau_sylviae_iii.py MONITOR QMP EXITUS MORA', file=sys.stderr)
        return 2

    aux = importa_auxilia()
    mon_via, _qmp_via, out, mora = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), float(sys.argv[4])
    finis = time.time() + 12.0
    while not mon_via.exists() and time.time() < finis:
        time.sleep(0.1)
    if not mon_via.exists():
        print('DEFECIT: monitor deest', file=sys.stderr)
        return 3

    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    monitor.settimeout(0.5)
    monitor.connect(str(mon_via))
    try:
        aux.lege_usque(monitor, b'(qemu) ', 2.0)
        time.sleep(mora)

        bronzeum_viii = (185, 138, 82)
        aqua_xi = (189, 239, 242)

        ante = out / 'bureau-ante.ppm'
        hover_p = out / 'bureau-hover-programmata.ppm'
        apertum_p = out / 'bureau-programmata.ppm'
        clausum_p = out / 'bureau-programmata-clausum.ppm'
        apertum_t = out / 'bureau-tabula.ppm'

        aux.captura(monitor, ante)
        w, h, pix_ante = aux.ppm(ante)
        if (w, h) != (1280, 800):
            print(f'DEFECIT: resolutio {w}x{h}', file=sys.stderr)
            return 4
        init_pos = aux.cursor_quaere(pix_ante, w, h)
        if init_pos is None:
            print('DEFECIT: cursor initialis non inventus', file=sys.stderr)
            return 5

        taskbar_top = h - 40
        vac_top = aux.pixel(pix_ante, w, 130, taskbar_top + 8)
        vac_bottom = aux.pixel(pix_ante, w, 130, taskbar_top + 31)
        if vac_top == vac_bottom or lumen(vac_top) <= lumen(vac_bottom):
            print(f'DEFECIT: taskbar IX vacua gradientiam amisit: {vac_top}->{vac_bottom}', file=sys.stderr)
            return 6

        # P16-XI: hitbox manet, sed tessera nunc materia Graphica VIII est.
        pos_p = aux.move_ad(monitor, out, 'bureau-programmata', 70, 110, w, h)
        aux.captura(monitor, hover_p)
        _, _, pix_hover_p = aux.ppm(hover_p)
        mut_hover = differentiae_rect(pix_ante, pix_hover_p, w, 18, 72, 126, 160)
        aqua_ante = copia_coloris(pix_ante, w, 18, 72, 126, 160, aqua_xi)
        aqua_hover = copia_coloris(pix_hover_p, w, 18, 72, 126, 160, aqua_xi)
        if mut_hover < 80 or aqua_hover <= aqua_ante + 20:
            print(f'DEFECIT: hover PROGRAMMATA XI non mutat materiam satis: mut={mut_hover} aqua={aqua_ante}->{aqua_hover} cursor={pos_p}', file=sys.stderr)
            return 7

        aux.click(monitor)
        aux.captura(monitor, apertum_p)
        _, _, pix_p = aux.ppm(apertum_p)
        if aux.pixel(pix_p, w, 300, 56) != bronzeum_viii:
            print(f'DEFECIT: PROGRAMMATA non aperta/focalizata: {aux.pixel(pix_p,w,300,56)}', file=sys.stderr)
            return 8

        prog_top = aux.pixel(pix_p, w, 130, taskbar_top + 8)
        prog_bottom = aux.pixel(pix_p, w, 130, taskbar_top + 31)
        if prog_top == prog_bottom or lumen(prog_top) <= lumen(prog_bottom):
            print(f'DEFECIT: PROGRAMMATA in taskbar IX non est graduata: {prog_top}->{prog_bottom}', file=sys.stderr)
            return 9
        if (prog_top, prog_bottom) == (vac_top, vac_bottom):
            print('DEFECIT: PROGRAMMATA in taskbar non apparuit', file=sys.stderr)
            return 10
        if aux.pixel(pix_p, w, 130, taskbar_top + 6) != bronzeum_viii:
            print(f'DEFECIT: PROGRAMMATA taskbar activa limen aeneum amisit: {aux.pixel(pix_p,w,130,taskbar_top+6)}', file=sys.stderr)
            return 11

        pos_close = aux.move_ad(monitor, out, 'bureau-clausura-programmata', 798, 74, w, h)
        aux.click(monitor)
        aux.captura(monitor, clausum_p)
        _, _, pix_clausum = aux.ppm(clausum_p)
        clausum_top = aux.pixel(pix_clausum, w, 130, taskbar_top + 8)
        clausum_bottom = aux.pixel(pix_clausum, w, 130, taskbar_top + 31)
        if (clausum_top, clausum_bottom) != (vac_top, vac_bottom):
            print(f'DEFECIT: PROGRAMMATA post clausuram in taskbar manet: {clausum_top}/{clausum_bottom}', file=sys.stderr)
            return 12
        if aux.pixel(pix_clausum, w, 300, 56) == bronzeum_viii:
            print('DEFECIT: PROGRAMMATA post clausuram adhuc pingitur', file=sys.stderr)
            return 13

        pos_t = aux.move_ad(monitor, out, 'bureau-tabula', 70, 214, w, h)
        aux.click(monitor)
        aux.captura(monitor, apertum_t)
        _, _, pix_t = aux.ppm(apertum_t)
        if aux.pixel(pix_t, w, 700, 168) != bronzeum_viii:
            print(f'DEFECIT: TABULA ex bureau non aperta/focalizata: {aux.pixel(pix_t,w,700,168)}', file=sys.stderr)
            return 14

        tab_top = aux.pixel(pix_t, w, 130, taskbar_top + 8)
        tab_bottom = aux.pixel(pix_t, w, 130, taskbar_top + 31)
        if tab_top == tab_bottom or lumen(tab_top) <= lumen(tab_bottom):
            print(f'DEFECIT: TABULA in taskbar IX non est graduata: {tab_top}->{tab_bottom}', file=sys.stderr)
            return 15
        if (tab_top, tab_bottom) == (vac_top, vac_bottom):
            print('DEFECIT: TABULA in taskbar activa non apparuit', file=sys.stderr)
            return 16
        if aux.pixel(pix_t, w, 130, taskbar_top + 6) != bronzeum_viii:
            print(f'DEFECIT: TABULA taskbar activa limen aeneum amisit: {aux.pixel(pix_t,w,130,taskbar_top+6)}', file=sys.stderr)
            return 17

        mut_p = aux.differentiae(pix_ante, pix_p)
        mut_close = aux.differentiae(pix_p, pix_clausum)
        mut_t = aux.differentiae(pix_clausum, pix_t)
        print(f'BUREAU-XI: cursor_init={init_pos} programmata={pos_p} clausura={pos_close} tabula={pos_t}')
        print(f'BUREAU-XI: hover_pixeli={mut_hover} aqua={aqua_ante}->{aqua_hover}')
        print(f'BUREAU-XI: taskbar_vacua={vac_top}->{vac_bottom} programmata={prog_top}->{prog_bottom} tabula={tab_top}->{tab_bottom}')
        print(f'BUREAU-XI: launch_programmata_pixeli={mut_p} clausura_pixeli={mut_close} launch_tabula_pixeli={mut_t}')
        print('RECTE: P16-XI Bureau Lucidum hover/launch/clausura/relaunch et taskbar IX servantur.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())
