#!/usr/bin/env python3
"""Chrome fenestrarum activum/inactivum sub UEFI/QEMU comprobat."""
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


def numerus_coloris(aux: object, pix: bytes, w: int, regio: tuple[int, int, int, int], color: tuple[int, int, int]) -> int:
    x0, y0, x1, y1 = regio
    return sum(aux.pixel(pix, w, x, y) == color for y in range(y0, y1) for x in range(x0, x1))


def fenestra_xiie(aux: object, pix: bytes, w: int, regio: tuple[int, int, int, int]) -> tuple[int, int, int]:
    """Chrome activum XII-E, materiam clientis et textum exactum metitur."""
    # Canon (58,96,104) rectus manet acceptus. Compositor GX titulum alpha
    # super scenam componens (57,95,103) exhibet; utrumque contractum servat.
    titulus_rectus = numerus_coloris(aux, pix, w, regio, (58, 96, 104))
    titulus_compositus = numerus_coloris(aux, pix, w, regio, (57, 95, 103))
    activus = max(titulus_rectus, titulus_compositus)
    materia = numerus_coloris(aux, pix, w, regio, (224, 226, 221))
    ebur = numerus_coloris(aux, pix, w, regio, (242, 244, 247))
    return activus, materia, ebur


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

        regio_p = (50, 35, 850, 650)
        forma_p = fenestra_xiie(aux, pix_p, w, regio_p)
        xiie = forma_p[0] >= 300 and forma_p[1] >= 5000 and forma_p[2] >= 300

        if not xiie:
            # Contractus historicus P16-VIII.
            if aux.pixel(pix_p, w, 300, 56) != bronzeum:
                print(f'DEFECIT: accentus activus PROGRAMMATA deest: {aux.pixel(pix_p,w,300,56)}', file=sys.stderr)
                return 5
            titulus_act_top = aux.pixel(pix_p, w, 300, 62)
            titulus_act_bottom = aux.pixel(pix_p, w, 300, 84)
            if titulus_act_top == titulus_act_bottom or lumen(titulus_act_top) <= lumen(titulus_act_bottom):
                print(f'DEFECIT: gradientia tituli activi non descendit: {titulus_act_top}->{titulus_act_bottom}', file=sys.stderr)
                return 6
            bulla_top = aux.pixel(pix_p, w, 730, 66)
            bulla_bottom = aux.pixel(pix_p, w, 730, 82)
            clausura_top = aux.pixel(pix_p, w, 790, 66)
            clausura_bottom = aux.pixel(pix_p, w, 790, 82)
            if bulla_top == bulla_bottom or lumen(bulla_top) <= lumen(bulla_bottom):
                print('DEFECIT: bulla minimizationis gradientiam amisit', file=sys.stderr)
                return 7
            if clausura_top == clausura_bottom or lumen(clausura_top) <= lumen(clausura_bottom) or clausura_top[0] <= clausura_top[1]:
                print('DEFECIT: bulla clausurae historica invalida est', file=sys.stderr)
                return 8
        else:
            # XII-E: materia solida/mineralis; gradientia veteris non requiritur.
            titulus_act_top = aux.pixel(pix_p, w, 300, 70)
            titulus_act_bottom = aux.pixel(pix_p, w, 300, 88)
            bulla_top = aux.pixel(pix_p, w, 736, 75)
            bulla_bottom = aux.pixel(pix_p, w, 766, 75)
            clausura_top = aux.pixel(pix_p, w, 790, 75)
            clausura_bottom = clausura_top
            # Clausura debet rubra esse; ceterae bullae multo minus rubrae.
            if clausura_top[0] <= clausura_top[1] + 40 or clausura_top[0] <= clausura_top[2] + 40:
                print(f'DEFECIT: clausura XII-E rubrum imperiale amisit: {clausura_top}', file=sys.stderr)
                return 9
            if bulla_top[0] > bulla_top[1] + 30 or bulla_bottom[0] > bulla_bottom[1] + 30:
                print(f'DEFECIT: bullae systematis XII-E nimis rubrae sunt: {bulla_top}/{bulla_bottom}', file=sys.stderr)
                return 10

        # Umbra externa PROGRAMMATA debet bureau nudum obscurare.
        umbra_sub = aux.pixel(pix_ante, w, 821, 100)
        umbra_p = aux.pixel(pix_p, w, 821, 100)
        if umbra_p == umbra_sub or lumen(umbra_p) >= lumen(umbra_sub):
            print(f'DEFECIT: umbra PROGRAMMATA deest: sub={umbra_sub} umbra={umbra_p}', file=sys.stderr)
            return 11

        # TABULA aperitur; PROGRAMMATA fit inactiva.
        pos_t = aux.move_ad(monitor, out, 'fenestrae-viii-tabula', 70, 214, w, h)
        aux.click(monitor)
        aux.captura(monitor, duae)
        _, _, pix_duae = aux.ppm(duae)

        titulus_inact_top = aux.pixel(pix_duae, w, 300, 70 if xiie else 62)
        titulus_inact_bottom = aux.pixel(pix_duae, w, 300, 88 if xiie else 84)
        if xiie:
            if titulus_inact_top == titulus_act_top and titulus_inact_bottom == titulus_act_bottom:
                print(f'DEFECIT: PROGRAMMATA XII-E ab activo ad inactivum non mutatur: {titulus_act_top}/{titulus_inact_top}', file=sys.stderr)
                return 12
            regio_t = (620, 120, 1240, 620)
            forma_t = fenestra_xiie(aux, pix_duae, w, regio_t)
            if forma_t[0] < 300 or forma_t[1] < 5000 or forma_t[2] < 200:
                print(f'DEFECIT: TABULA focus XII-E non accepit: {forma_t}', file=sys.stderr)
                return 13
        else:
            if aux.pixel(pix_duae, w, 300, 56) != chalybs:
                print(f'DEFECIT: PROGRAMMATA post focus TABULAE non fit inactiva: {aux.pixel(pix_duae,w,300,56)}', file=sys.stderr)
                return 14
            if titulus_inact_top == titulus_inact_bottom or lumen(titulus_inact_top) <= lumen(titulus_inact_bottom):
                print('DEFECIT: gradientia tituli inactivi non descendit', file=sys.stderr)
                return 15
            if aux.pixel(pix_duae, w, 700, 168) != bronzeum:
                print('DEFECIT: TABULA focus historicum non accipit', file=sys.stderr)
                return 16

        # Umbra TABULAE exterior quoque probatur.
        umbra_t_sub = aux.pixel(pix_p, w, 1220, 220)
        umbra_t = aux.pixel(pix_duae, w, 1220, 220)
        if umbra_t == umbra_t_sub or lumen(umbra_t) >= lumen(umbra_t_sub):
            print(f'DEFECIT: umbra TABULAE deest: sub={umbra_t_sub} umbra={umbra_t}', file=sys.stderr)
            return 17

        mut_p = aux.differentiae(pix_ante, pix_p)
        mut_duae = aux.differentiae(pix_p, pix_duae)
        testa = 'XII-E' if xiie else 'P16-VIII'
        print(f'FENESTRAE: testa={testa} programmata={pos_p} tabula={pos_t}')
        print(f'FENESTRAE: launch_programmata_pixeli={mut_p} focus_tabula_pixeli={mut_duae}')
        print(f'FENESTRAE: titulus_activus={titulus_act_top}->{titulus_act_bottom} inactivus={titulus_inact_top}->{titulus_inact_bottom}')
        print(f'FENESTRAE: bullae={bulla_top}/{bulla_bottom} clausura={clausura_top} umbrae={umbra_sub}->{umbra_p}/{umbra_t_sub}->{umbra_t}')
        print('RECTE: chrome hodiernum focus, bullas et umbras alpha vere pingit.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())
