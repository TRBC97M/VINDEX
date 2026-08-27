#!/usr/bin/env python3
"""P16-V: chrome fenestrarum activarum et inactivarum sub UEFI/QEMU comprobat."""
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
        print('USUS: proba_fenestras_sylviae_v.py MONITOR QMP EXITUS MORA', file=sys.stderr)
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

        bronzeum = (185, 138, 82)
        argentum = (185, 196, 207)
        vitrum = (14, 66, 111)
        titulus_inactivus = (73, 95, 111)
        titulus_inferior_inactivus = (91, 111, 124)
        umbra_profunda = (3, 14, 25)
        bulla = (207, 216, 220)
        rubrum = (168, 58, 58)

        ante = out / 'fenestrae-v-ante.ppm'
        programmata = out / 'fenestrae-v-programmata.ppm'
        duae = out / 'fenestrae-v-duae.ppm'

        aux.captura(monitor, ante)
        w, h, pix_ante = aux.ppm(ante)
        if (w, h) != (1280, 800):
            print(f'DEFECIT: resolutio {w}x{h}', file=sys.stderr)
            return 4

        # PROGRAMMATA e bureau aperitur.
        pos_p = aux.move_ad(monitor, out, 'fenestrae-v-programmata', 70, 110, w, h)
        aux.click(monitor)
        aux.captura(monitor, programmata)
        _, _, pix_p = aux.ppm(programmata)

        if aux.pixel(pix_p, w, 300, 56) != bronzeum:
            print(f'DEFECIT: accentus activus PROGRAMMATA deest: {aux.pixel(pix_p,w,300,56)}', file=sys.stderr)
            return 5
        if aux.pixel(pix_p, w, 300, 62) != vitrum:
            print(f'DEFECIT: titulus activus PROGRAMMATA non est vitrum: {aux.pixel(pix_p,w,300,62)}', file=sys.stderr)
            return 6
        if aux.pixel(pix_p, w, 825, 100) != umbra_profunda:
            print(f'DEFECIT: umbra duplex PROGRAMMATA deest: {aux.pixel(pix_p,w,825,100)}', file=sys.stderr)
            return 7
        if aux.pixel(pix_p, w, 730, 66) != bulla:
            print(f'DEFECIT: bulla plana minimizationis deest: {aux.pixel(pix_p,w,730,66)}', file=sys.stderr)
            return 8
        if aux.pixel(pix_p, w, 790, 66) != rubrum:
            print(f'DEFECIT: bulla clausurae activa non est rubra: {aux.pixel(pix_p,w,790,66)}', file=sys.stderr)
            return 9

        # TABULA quoque e bureau aperitur; PROGRAMMATA fit inactiva.
        pos_t = aux.move_ad(monitor, out, 'fenestrae-v-tabula', 70, 214, w, h)
        aux.click(monitor)
        aux.captura(monitor, duae)
        _, _, pix_duae = aux.ppm(duae)

        if aux.pixel(pix_duae, w, 300, 56) != argentum:
            print(f'DEFECIT: PROGRAMMATA post focus TABULAE non fit inactiva: {aux.pixel(pix_duae,w,300,56)}', file=sys.stderr)
            return 10
        if aux.pixel(pix_duae, w, 300, 62) != titulus_inactivus:
            print(f'DEFECIT: titulus inactivus non est desaturatus: {aux.pixel(pix_duae,w,300,62)}', file=sys.stderr)
            return 11
        if aux.pixel(pix_duae, w, 300, 84) != titulus_inferior_inactivus:
            print(f'DEFECIT: fascia inferior tituli inactivi deest: {aux.pixel(pix_duae,w,300,84)}', file=sys.stderr)
            return 12
        if aux.pixel(pix_duae, w, 700, 168) != bronzeum:
            print(f'DEFECIT: TABULA focus activum non accipit: {aux.pixel(pix_duae,w,700,168)}', file=sys.stderr)
            return 13
        if aux.pixel(pix_duae, w, 1224, 220) != umbra_profunda:
            print(f'DEFECIT: umbra TABULAE deest: {aux.pixel(pix_duae,w,1224,220)}', file=sys.stderr)
            return 14

        mut_p = aux.differentiae(pix_ante, pix_p)
        mut_duae = aux.differentiae(pix_p, pix_duae)
        print(f'FENESTRAE-V: programmata={pos_p} tabula={pos_t}')
        print(f'FENESTRAE-V: launch_programmata_pixeli={mut_p} focus_tabula_pixeli={mut_duae}')
        print('RECTE: P16-V chrome modernum focus, inertiam, bullas et umbras vere pingit.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())
