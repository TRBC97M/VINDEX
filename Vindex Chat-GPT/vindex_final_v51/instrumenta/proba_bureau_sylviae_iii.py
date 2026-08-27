#!/usr/bin/env python3
"""P16-VI: bureau mundum, launch, clausuram et relaunch sub UEFI/QEMU comprobat."""
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

        nox = (28, 31, 32)
        lapis = (49, 55, 55)
        activum = (91, 69, 48)
        bronzeum = (185, 138, 82)

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

        # Bureau initio nullam applicationem apertam in taskbar habet.
        if aux.pixel(pix_ante, w, 130, 770) != nox:
            print(f'DEFECIT: taskbar initio non vacua: {aux.pixel(pix_ante,w,130,770)}', file=sys.stderr)
            return 6
        if aux.pixel(pix_ante, w, 20, 74) != nox or aux.pixel(pix_ante, w, 20, 178) != nox:
            print('DEFECIT: tesserae bureau nocturnae initiales desunt', file=sys.stderr)
            return 7

        pos_p = aux.move_ad(monitor, out, 'bureau-programmata', 70, 110, w, h)
        aux.captura(monitor, hover_p)
        _, _, pix_hover_p = aux.ppm(hover_p)
        if aux.pixel(pix_hover_p, w, 20, 74) != lapis:
            print(f'DEFECIT: hover PROGRAMMATA lapideus non detectus: {aux.pixel(pix_hover_p,w,20,74)} cursor={pos_p}', file=sys.stderr)
            return 8

        aux.click(monitor)
        aux.captura(monitor, apertum_p)
        _, _, pix_p = aux.ppm(apertum_p)
        if aux.pixel(pix_p, w, 300, 56) != bronzeum:
            print(f'DEFECIT: PROGRAMMATA non aperta/focalizata: {aux.pixel(pix_p,w,300,56)}', file=sys.stderr)
            return 9
        if aux.pixel(pix_p, w, 130, 770) != activum:
            print(f'DEFECIT: PROGRAMMATA in taskbar activa non apparuit: {aux.pixel(pix_p,w,130,770)}', file=sys.stderr)
            return 10

        # Bulla clausurae PROGRAMMATA: geometria canonica circa (798,74).
        pos_close = aux.move_ad(monitor, out, 'bureau-clausura-programmata', 798, 74, w, h)
        aux.click(monitor)
        aux.captura(monitor, clausum_p)
        _, _, pix_clausum = aux.ppm(clausum_p)
        if aux.pixel(pix_clausum, w, 130, 770) != nox:
            print(f'DEFECIT: PROGRAMMATA post clausuram in taskbar manet: {aux.pixel(pix_clausum,w,130,770)}', file=sys.stderr)
            return 11
        if aux.pixel(pix_clausum, w, 300, 56) == bronzeum:
            print('DEFECIT: PROGRAMMATA post clausuram adhuc pingitur', file=sys.stderr)
            return 12

        pos_t = aux.move_ad(monitor, out, 'bureau-tabula', 70, 214, w, h)
        aux.click(monitor)
        aux.captura(monitor, apertum_t)
        _, _, pix_t = aux.ppm(apertum_t)
        if aux.pixel(pix_t, w, 700, 168) != bronzeum:
            print(f'DEFECIT: TABULA ex bureau non aperta/focalizata: {aux.pixel(pix_t,w,700,168)}', file=sys.stderr)
            return 13
        if aux.pixel(pix_t, w, 130, 770) != activum:
            print(f'DEFECIT: TABULA in taskbar activa non apparuit: {aux.pixel(pix_t,w,130,770)}', file=sys.stderr)
            return 14

        mut_p = aux.differentiae(pix_ante, pix_p)
        mut_close = aux.differentiae(pix_p, pix_clausum)
        mut_t = aux.differentiae(pix_clausum, pix_t)
        print(f'BUREAU-VI: cursor_init={init_pos} programmata={pos_p} clausura={pos_close} tabula={pos_t}')
        print(f'BUREAU-VI: launch_programmata_pixeli={mut_p} clausura_pixeli={mut_close} launch_tabula_pixeli={mut_t}')
        print('RECTE: P16-VI bureau lapideum applicationes aperit, claudit et relaunchat per PS/2.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())
