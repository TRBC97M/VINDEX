#!/usr/bin/env python3
"""P16-XI: INITIUM et rail JL-UX sub UEFI/QEMU comprobantur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name('proba_initium_sylviae_ii.py')
    spec = importlib.util.spec_from_file_location('proba_initium_xi', via)
    if spec is None or spec.loader is None:
        raise RuntimeError('probator INITII importari non potest')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lumen(color: tuple[int, int, int]) -> int:
    return color[0] + color[1] + color[2]


def initium_top_quaere(pix: bytes, w: int, h: int, bronzeum: tuple[int, int, int]) -> int | None:
    """Clavem aeneam horizontalem capitis XI quaerit."""
    b = bytes(bronzeum)
    for y in range(120, h - 120):
        if pix[(y*w+20)*3:(y*w+20)*3+3] != b:
            continue
        if pix[(y*w+300)*3:(y*w+300)*3+3] != b:
            continue
        return y - 8
    return None


def principale() -> int:
    if len(sys.argv) != 5:
        print('USUS: proba_initium_sylviae_xi.py MONITOR QMP EXITUS MORA', file=sys.stderr)
        return 2

    aux = auxilia()
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

        ante = out / 'initium-xi-ante.ppm'
        apertum = out / 'initium-xi-apertum.ppm'
        hover = out / 'initium-xi-hover.ppm'
        post = out / 'initium-xi-post.ppm'
        aux.captura(monitor, ante)
        w, h, pix_ante = aux.ppm(ante)
        if (w, h) != (1280, 800):
            print(f'DEFECIT: resolutio {w}x{h}', file=sys.stderr)
            return 4

        taskbar_top = h - 40
        graphite = (26, 29, 32)
        cool = (74, 96, 114)
        ebur = (242, 244, 247)
        argentum = (191, 199, 207)
        aqua = (189, 239, 242)
        bronzeum = (181, 138, 84)
        selectum = (218, 238, 239)
        bronzeum_viii = (185, 138, 82)

        # Rail XI ante INITIUM iam debet materiam exactam ostendere.
        if aux.pixel(pix_ante, w, 400, taskbar_top + 4) != argentum:
            print(f'DEFECIT: limen argentum rail XI deest: {aux.pixel(pix_ante,w,400,taskbar_top+4)}', file=sys.stderr)
            return 5
        if aux.pixel(pix_ante, w, 400, taskbar_top + 7) != aqua:
            print(f'DEFECIT: lumen Aqua rail XI deest: {aux.pixel(pix_ante,w,400,taskbar_top+7)}', file=sys.stderr)
            return 6
        if aux.pixel(pix_ante, w, 400, taskbar_top + 20) != graphite:
            print(f'DEFECIT: corpus Graphite rail XI deest: {aux.pixel(pix_ante,w,400,taskbar_top+20)}', file=sys.stderr)
            return 7

        init_ante = aux.pixel(pix_ante, w, 60, taskbar_top + 20)
        pos_initium = aux.move_ad(monitor, out, 'initium-xi', 50, 770, w, h)
        aux.click(monitor)
        time.sleep(0.25)
        aux.captura(monitor, apertum)
        w2, h2, pix_open = aux.ppm(apertum)
        if (w2, h2) != (w, h):
            print('DEFECIT: dimensiones post INITIUM mutantur', file=sys.stderr)
            return 8

        menu_top = initium_top_quaere(pix_open, w, h, bronzeum)
        if menu_top is None:
            print('DEFECIT: pannus INITIUM XI non inventus', file=sys.stderr)
            return 9

        # Caput mineralis: Graphite, Bronze et Aqua; corpus Ebur apertum.
        if aux.pixel(pix_open, w, 180, menu_top + 30) != graphite:
            print(f'DEFECIT: caput Graphite INITII XI deest: {aux.pixel(pix_open,w,180,menu_top+30)}', file=sys.stderr)
            return 10
        if aux.pixel(pix_open, w, 180, menu_top + 8) != bronzeum:
            print(f'DEFECIT: clavis Bronze INITII XI deest: {aux.pixel(pix_open,w,180,menu_top+8)}', file=sys.stderr)
            return 11
        if aux.pixel(pix_open, w, 180, menu_top + 11) != aqua:
            print(f'DEFECIT: lumen Aqua INITII XI deest: {aux.pixel(pix_open,w,180,menu_top+11)}', file=sys.stderr)
            return 12
        if aux.pixel(pix_open, w, 300, menu_top + 72) != ebur:
            print(f'DEFECIT: corpus Ebur INITII XI deest: {aux.pixel(pix_open,w,300,menu_top+72)}', file=sys.stderr)
            return 13

        programmata_y = menu_top + 92
        tabula_y = programmata_y + 54
        programmata_scopus = programmata_y + 22
        tabula_scopus = tabula_y + 22
        prog_corpus = aux.pixel(pix_open, w, 300, programmata_scopus)
        tab_corpus = aux.pixel(pix_open, w, 300, tabula_scopus)
        if prog_corpus != ebur or tab_corpus != ebur:
            print(f'DEFECIT: ordines quieti INITII XI non sunt Ebur: {prog_corpus}/{tab_corpus}', file=sys.stderr)
            return 14

        # INITIUM in rail mutat statum, sed hitbox historica eadem manet.
        init_open = aux.pixel(pix_open, w, 60, taskbar_top + 20)
        if init_open == init_ante:
            print(f'DEFECIT: gemma INITIUM statum apertum non indicat: {init_ante}->{init_open}', file=sys.stderr)
            return 15

        # Atlas raster P16-VII super puteos XI remanet.
        lumen_programmatum = (236, 194, 113)
        cyan_programmatum = (90, 208, 209)
        clarum_tabulae = (232, 232, 217)
        aqua_tabulae = (145, 194, 191)
        prog_lumen = aux.numerus_coloris_in_recto(pix_open, w, 20, programmata_y + 6, 58, programmata_y + 46, lumen_programmatum)
        prog_cyan = aux.numerus_coloris_in_recto(pix_open, w, 20, programmata_y + 6, 58, programmata_y + 46, cyan_programmatum)
        tab_clarum = aux.numerus_coloris_in_recto(pix_open, w, 20, tabula_y + 6, 58, tabula_y + 46, clarum_tabulae)
        tab_aqua = aux.numerus_coloris_in_recto(pix_open, w, 20, tabula_y + 6, 58, tabula_y + 46, aqua_tabulae)
        if prog_lumen < 40 or prog_cyan < 4 or tab_clarum < 100 or tab_aqua < 40:
            print(f'DEFECIT: atlas INITII XI mutatus est: P={prog_lumen}/{prog_cyan} T={tab_clarum}/{tab_aqua}', file=sys.stderr)
            return 16

        # Hover fit superficies Aqua localis, non tessera plena permanens.
        pos_tabula = aux.move_ad(monitor, out, 'tabula-xi', 150, tabula_scopus, w, h)
        aux.captura(monitor, hover)
        _, _, pix_hover = aux.ppm(hover)
        hover_tab = aux.pixel(pix_hover, w, 300, tabula_scopus)
        hover_prog = aux.pixel(pix_hover, w, 300, programmata_scopus)
        if hover_tab != selectum:
            print(f'DEFECIT: hover TABULA materiam Aqua XI non accepit: {hover_tab}', file=sys.stderr)
            return 17
        if aux.pixel(pix_hover, w, 19, tabula_scopus) != bronzeum:
            print(f'DEFECIT: clavis Bronze hover TABULAE deest: {aux.pixel(pix_hover,w,19,tabula_scopus)}', file=sys.stderr)
            return 18
        if hover_prog != prog_corpus:
            print(f'DEFECIT: hover TABULA PROGRAMMATA mutavit: {prog_corpus}->{hover_prog}', file=sys.stderr)
            return 19

        aux.click(monitor)
        time.sleep(0.25)
        aux.captura(monitor, post)
        _, _, pix_post = aux.ppm(post)
        if initium_top_quaere(pix_post, w, h, bronzeum) is not None:
            print('DEFECIT: INITIUM XI post electionem adhuc repertum est', file=sys.stderr)
            return 20

        # Fenestra P16-VIII accipit focum; rail XI eam Aqua/Bronze signat.
        focus_pixel = aux.pixel(pix_post, w, 700, 168)
        if focus_pixel != bronzeum_viii:
            print(f'DEFECIT: TABULA focus P16-VIII non accepit: {focus_pixel}', file=sys.stderr)
            return 21
        if aux.pixel(pix_post, w, 150, taskbar_top + 9) != aqua:
            print(f'DEFECIT: applicatio activa rail XI lumen Aqua amisit: {aux.pixel(pix_post,w,150,taskbar_top+9)}', file=sys.stderr)
            return 22
        if aux.pixel(pix_post, w, 150, taskbar_top + 30) != bronzeum:
            print(f'DEFECIT: applicatio activa rail XI clavem Bronze amisit: {aux.pixel(pix_post,w,150,taskbar_top+30)}', file=sys.stderr)
            return 23

        mutata_open = aux.differentiae(pix_ante, pix_open)
        mutata_post = aux.differentiae(pix_open, pix_post)
        if mutata_open < 12000 or mutata_post < 12000:
            print(f'DEFECIT: mutationes INITII XI nimis parvae: {mutata_open}/{mutata_post}', file=sys.stderr)
            return 24

        print(f'INITIUM-XI: top={menu_top} cursor={pos_initium}->{pos_tabula}')
        print(f'INITIUM-XI: rail={init_ante}->{init_open} corpus={prog_corpus} hover={hover_tab}')
        print(f'INITIUM-XI: atlas P={prog_lumen}/{prog_cyan} T={tab_clarum}/{tab_aqua} pixeli={mutata_open}/{mutata_post}')
        print('RECTE: P16-XI INITIUM minerale et rail JL-UX operantur, atlas et focus P16-VIII servantur.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())