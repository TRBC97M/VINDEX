#!/usr/bin/env python3
"""Bureau Sylviae: hover, launch, clausura et relaunch sub UEFI/QEMU comprobantur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def importa(nomen: str, fasciculus: str) -> object:
    via = Path(__file__).resolve().with_name(fasciculus)
    spec = importlib.util.spec_from_file_location(nomen, via)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'probator importari non potest: {fasciculus}')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def numerus_coloris(aux: object, pix: bytes, w: int, regio: tuple[int, int, int, int], color: tuple[int, int, int]) -> int:
    x0, y0, x1, y1 = regio
    return sum(aux.pixel(pix, w, x, y) == color for y in range(y0, y1) for x in range(x0, x1))


def fenestra_xiie(aux: object, pix: bytes, w: int, regio: tuple[int, int, int, int]) -> tuple[int, int, int]:
    # Titulus activus post compositionem GX colorem (57,95,103) habet; canon
    # rectus (58,96,104) quoque semper accipitur. Materia et textus exacti cum
    # linea taskbar infra fenestram visibilem atque focum separatim probant.
    titulus_rectus = numerus_coloris(aux, pix, w, regio, (58, 96, 104))
    titulus_compositus = numerus_coloris(aux, pix, w, regio, (57, 95, 103))
    activus = max(titulus_rectus, titulus_compositus)
    materia = numerus_coloris(aux, pix, w, regio, (224, 226, 221))
    ebur = numerus_coloris(aux, pix, w, regio, (242, 244, 247))
    return activus, materia, ebur


def principale() -> int:
    if len(sys.argv) != 5:
        print('USUS: proba_bureau_sylviae_iii.py MONITOR QMP EXITUS MORA', file=sys.stderr)
        return 2

    aux = importa('proba_initium_ii', 'proba_initium_sylviae_ii.py')
    forma = importa('proba_formam_xib', 'proba_formam_sylviae_xib.py')
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

        try:
            testa, _, _ = forma.taskbar_contractus(forma.auxilia(), pix_ante, w, h)
        except RuntimeError as exc:
            print(f'DEFECIT: taskbar initialis invalida: {exc}', file=sys.stderr)
            return 6
        xiie = testa == 'XII-E'
        taskbar_top = h - 40
        vac = aux.pixel(pix_ante, w, 130, taskbar_top + 18)

        # Hover PROGRAMMATA debet cardum mutare multo plus quam solus cursor.
        pos_p = aux.move_ad(monitor, out, 'bureau-programmata', 70, 110, w, h)
        aux.captura(monitor, hover_p)
        _, _, pix_hover_p = aux.ppm(hover_p)
        mut_hover = aux.differentiae(pix_ante, pix_hover_p)
        if mut_hover < 800:
            print(f'DEFECIT: hover PROGRAMMATA non apparuit: pixeli={mut_hover} cursor={pos_p}', file=sys.stderr)
            return 7

        aux.click(monitor)
        aux.captura(monitor, apertum_p)
        _, _, pix_p = aux.ppm(apertum_p)
        bronzeum_vetus = (185, 138, 82)
        if xiie:
            fp = fenestra_xiie(aux, pix_p, w, (50, 35, 850, 650))
            if fp[0] < 300 or fp[1] < 5000 or fp[2] < 300:
                print(f'DEFECIT: PROGRAMMATA XII-E non aperta/focalizata: {fp}', file=sys.stderr)
                return 8
        elif aux.pixel(pix_p, w, 300, 56) != bronzeum_vetus:
            print(f'DEFECIT: PROGRAMMATA historica non aperta/focalizata: {aux.pixel(pix_p,w,300,56)}', file=sys.stderr)
            return 9

        prog = aux.pixel(pix_p, w, 130, taskbar_top + 18)
        if prog == vac:
            print('DEFECIT: PROGRAMMATA in taskbar non apparuit', file=sys.stderr)
            return 10
        accentus = (181, 138, 84) if xiie else bronzeum_vetus
        y_accentus = taskbar_top + 7 if xiie else taskbar_top + 6
        if aux.pixel(pix_p, w, 130, y_accentus) != accentus:
            print(f'DEFECIT: PROGRAMMATA taskbar activa limen amisit: {aux.pixel(pix_p,w,130,y_accentus)}', file=sys.stderr)
            return 11

        # Bulla clausurae: geometria interactive historica intacta manet.
        pos_close = aux.move_ad(monitor, out, 'bureau-clausura-programmata', 798, 74, w, h)
        aux.click(monitor)
        aux.captura(monitor, clausum_p)
        _, _, pix_clausum = aux.ppm(clausum_p)
        clausum = aux.pixel(pix_clausum, w, 130, taskbar_top + 18)
        if clausum != vac:
            print(f'DEFECIT: PROGRAMMATA post clausuram in taskbar manet: {vac}->{clausum}', file=sys.stderr)
            return 12
        if xiie:
            fp_post = fenestra_xiie(aux, pix_clausum, w, (50, 35, 850, 650))
            if fp_post[2] > fp[2] // 2:
                print(f'DEFECIT: PROGRAMMATA post clausuram adhuc dominatur: {fp}->{fp_post}', file=sys.stderr)
                return 13
        elif aux.pixel(pix_clausum, w, 300, 56) == bronzeum_vetus:
            print('DEFECIT: PROGRAMMATA post clausuram adhuc pingitur', file=sys.stderr)
            return 14

        # TABULA e Bureau aperitur et accipit focum/taskbar.
        pos_t = aux.move_ad(monitor, out, 'bureau-tabula', 70, 214, w, h)
        aux.click(monitor)
        aux.captura(monitor, apertum_t)
        _, _, pix_t = aux.ppm(apertum_t)
        if xiie:
            ft = fenestra_xiie(aux, pix_t, w, (620, 120, 1240, 620))
            if ft[0] < 300 or ft[1] < 5000 or ft[2] < 200:
                print(f'DEFECIT: TABULA XII-E ex bureau non aperta/focalizata: {ft}', file=sys.stderr)
                return 15
        elif aux.pixel(pix_t, w, 700, 168) != bronzeum_vetus:
            print(f'DEFECIT: TABULA historica ex bureau non aperta/focalizata: {aux.pixel(pix_t,w,700,168)}', file=sys.stderr)
            return 16

        tab = aux.pixel(pix_t, w, 130, taskbar_top + 18)
        if tab == vac:
            print('DEFECIT: TABULA in taskbar activa non apparuit', file=sys.stderr)
            return 17
        if aux.pixel(pix_t, w, 130, y_accentus) != accentus:
            print(f'DEFECIT: TABULA taskbar activa limen amisit: {aux.pixel(pix_t,w,130,y_accentus)}', file=sys.stderr)
            return 18

        mut_p = aux.differentiae(pix_ante, pix_p)
        mut_close = aux.differentiae(pix_p, pix_clausum)
        mut_t = aux.differentiae(pix_clausum, pix_t)
        print(f'BUREAU: testa={testa} cursor_init={init_pos} programmata={pos_p} clausura={pos_close} tabula={pos_t}')
        print(f'BUREAU: taskbar_vacua={vac} programmata={prog} clausum={clausum} tabula={tab}')
        print(f'BUREAU: hover={mut_hover} launch_programmata={mut_p} clausura={mut_close} launch_tabula={mut_t}')
        print('RECTE: Bureau applicationes aperit, claudit et taskbar hodiernam recte renovat.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())
