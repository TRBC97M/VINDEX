#!/usr/bin/env python3
"""P16-VIII: chrome compositum activum et inactivum sub UEFI/QEMU comprobat."""
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
        chalybs = (92, 99, 96)

        ante = out / 'fenestrae-viii-ante.ppm'
        programmata = out / 'fenestrae-viii-programmata.ppm'
        duae = out / 'fenestrae-viii-duae.ppm'

        aux.captura(monitor, ante)
        w, h, pix_ante = aux.ppm(ante)
        if (w, h) != (1280, 800):
            print(f'DEFECIT: resolutio {w}x{h}', file=sys.stderr)
            return 4

        # PROGRAMMATA e bureau aperitur.
        pos_p = aux.move_ad(monitor, out, 'fenestrae-viii-programmata', 70, 110, w, h)
        aux.click(monitor)
        aux.captura(monitor, programmata)
        _, _, pix_p = aux.ppm(programmata)

        # Accentus superior P16-V manet, sed titulus P16-VIII iam est gradientia vera.
        if aux.pixel(pix_p, w, 300, 56) != bronzeum:
            print(f'DEFECIT: accentus activus PROGRAMMATA deest: {aux.pixel(pix_p,w,300,56)}', file=sys.stderr)
            return 5
        titulus_act_top = aux.pixel(pix_p, w, 300, 62)
        titulus_act_bottom = aux.pixel(pix_p, w, 300, 84)
        if titulus_act_top == titulus_act_bottom or lumen(titulus_act_top) <= lumen(titulus_act_bottom):
            print(
                f'DEFECIT: gradientia tituli activi non descendit: {titulus_act_top} -> {titulus_act_bottom}',
                file=sys.stderr,
            )
            return 6
        if titulus_act_top[1] <= titulus_act_top[0] or titulus_act_top[2] <= titulus_act_top[0]:
            print(f'DEFECIT: titulus activus accentum viridi-caeruleum amisit: {titulus_act_top}', file=sys.stderr)
            return 7

        # Umbra P16-VIII est alpha exterior: pixel extra corpus obscurior fit quam idem bureau nudum.
        umbra_sub = aux.pixel(pix_ante, w, 821, 100)
        umbra_p = aux.pixel(pix_p, w, 821, 100)
        if umbra_p == umbra_sub or lumen(umbra_p) >= lumen(umbra_sub):
            print(f'DEFECIT: umbra alpha PROGRAMMATA deest: sub={umbra_sub} umbra={umbra_p}', file=sys.stderr)
            return 8

        # Bullae non sunt iam aplata: summum et inferum eiusdem bullae differre debent.
        bulla_top = aux.pixel(pix_p, w, 730, 66)
        bulla_bottom = aux.pixel(pix_p, w, 730, 82)
        if bulla_top == bulla_bottom or lumen(bulla_top) <= lumen(bulla_bottom):
            print(f'DEFECIT: bulla minimizationis gradientiam amisit: {bulla_top} -> {bulla_bottom}', file=sys.stderr)
            return 9
        clausura_top = aux.pixel(pix_p, w, 790, 66)
        clausura_bottom = aux.pixel(pix_p, w, 790, 82)
        if clausura_top == clausura_bottom or lumen(clausura_top) <= lumen(clausura_bottom):
            print(f'DEFECIT: bulla clausurae gradientiam amisit: {clausura_top} -> {clausura_bottom}', file=sys.stderr)
            return 10
        if clausura_top[0] <= clausura_top[1] or clausura_bottom[0] <= clausura_bottom[1]:
            print(f'DEFECIT: clausura rubrum temperatum amisit: {clausura_top}/{clausura_bottom}', file=sys.stderr)
            return 11

        # TABULA quoque e bureau aperitur; PROGRAMMATA fit inactiva.
        pos_t = aux.move_ad(monitor, out, 'fenestrae-viii-tabula', 70, 214, w, h)
        aux.click(monitor)
        aux.captura(monitor, duae)
        _, _, pix_duae = aux.ppm(duae)

        if aux.pixel(pix_duae, w, 300, 56) != chalybs:
            print(f'DEFECIT: PROGRAMMATA post focus TABULAE non fit inactiva: {aux.pixel(pix_duae,w,300,56)}', file=sys.stderr)
            return 12
        titulus_inact_top = aux.pixel(pix_duae, w, 300, 62)
        titulus_inact_bottom = aux.pixel(pix_duae, w, 300, 84)
        if titulus_inact_top == titulus_inact_bottom or lumen(titulus_inact_top) <= lumen(titulus_inact_bottom):
            print(
                f'DEFECIT: gradientia tituli inactivi non descendit: {titulus_inact_top} -> {titulus_inact_bottom}',
                file=sys.stderr,
            )
            return 13
        if titulus_inact_top == titulus_act_top or titulus_inact_bottom == titulus_act_bottom:
            print(
                f'DEFECIT: titulus inactivus ab activo non distinguitur: '
                f'{titulus_act_top}/{titulus_act_bottom} -> {titulus_inact_top}/{titulus_inact_bottom}',
                file=sys.stderr,
            )
            return 14

        if aux.pixel(pix_duae, w, 700, 168) != bronzeum:
            print(f'DEFECIT: TABULA focus activum non accipit: {aux.pixel(pix_duae,w,700,168)}', file=sys.stderr)
            return 15

        # Dextra TABULAE: umbra externa P16-VIII debet bureau subiectum obscurare.
        umbra_t_sub = aux.pixel(pix_p, w, 1220, 220)
        umbra_t = aux.pixel(pix_duae, w, 1220, 220)
        if umbra_t == umbra_t_sub or lumen(umbra_t) >= lumen(umbra_t_sub):
            print(f'DEFECIT: umbra alpha TABULAE deest: sub={umbra_t_sub} umbra={umbra_t}', file=sys.stderr)
            return 16

        mut_p = aux.differentiae(pix_ante, pix_p)
        mut_duae = aux.differentiae(pix_p, pix_duae)
        print(f'FENESTRAE-VIII: programmata={pos_p} tabula={pos_t}')
        print(f'FENESTRAE-VIII: launch_programmata_pixeli={mut_p} focus_tabula_pixeli={mut_duae}')
        print(
            'FENESTRAE-VIII: '
            f'titulus_activus={titulus_act_top}->{titulus_act_bottom} '
            f'titulus_inactivus={titulus_inact_top}->{titulus_inact_bottom}'
        )
        print(
            'FENESTRAE-VIII: '
            f'bulla={bulla_top}->{bulla_bottom} clausura={clausura_top}->{clausura_bottom} '
            f'umbrae={umbra_sub}->{umbra_p}/{umbra_t_sub}->{umbra_t}'
        )
        print('RECTE: P16-VIII chrome compositum gradientias, focus, bullas et umbras alpha vere pingit.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())
