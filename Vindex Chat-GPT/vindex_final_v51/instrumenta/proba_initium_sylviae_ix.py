#!/usr/bin/env python3
"""P16-IX: INITIUM compositum, hover, atlas et taskbar activa sub UEFI/QEMU comprobantur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name('proba_initium_sylviae_ii.py')
    spec = importlib.util.spec_from_file_location('proba_initium_vii', via)
    if spec is None or spec.loader is None:
        raise RuntimeError('probator INITII P16-VII importari non potest')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lumen(color: tuple[int, int, int]) -> int:
    return color[0] + color[1] + color[2]


def initium_top_quaere(pix: bytes, w: int, h: int, bronzeum: tuple[int, int, int]) -> int | None:
    """Limen aeneum continuum pannum IX distinguit sine colore plano historico postulando."""
    for y in range(120, h - 120):
        if pix[(y*w+20)*3:(y*w+20)*3+3] != bytes(bronzeum):
            continue
        if pix[(y*w+300)*3:(y*w+300)*3+3] != bytes(bronzeum):
            continue
        if y + 92 >= h:
            continue
        return y
    return None


def principale() -> int:
    if len(sys.argv) != 5:
        print('USUS: proba_initium_sylviae_ix.py MONITOR QMP EXITUS MORA', file=sys.stderr)
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

        ante = out / 'initium-ix-ante.ppm'
        apertum = out / 'initium-ix-apertum.ppm'
        hover = out / 'initium-ix-hover.ppm'
        post = out / 'initium-ix-post.ppm'
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
        init_ante_top = aux.pixel(pix_ante, w, 50, taskbar_top + 8)
        init_ante_bottom = aux.pixel(pix_ante, w, 50, taskbar_top + 31)

        pos_initium = aux.move_ad(monitor, out, 'initium-ix', 50, 770, w, h)
        aux.click(monitor)
        aux.captura(monitor, apertum)
        w2, h2, pix_open = aux.ppm(apertum)
        if (w2, h2) != (w, h):
            print('DEFECIT: dimensiones post INITIUM mutantur', file=sys.stderr)
            return 6

        bronzeum = (185, 138, 82)
        menu_top = initium_top_quaere(pix_open, w, h, bronzeum)
        if menu_top is None:
            print('DEFECIT: pannus INITIUM P16-IX non inventus', file=sys.stderr)
            return 7

        # Caput non est amplius aplanatum: idem viridi-caeruleum ac fenestra activa descendit.
        caput_top = aux.pixel(pix_open, w, 180, menu_top + 8)
        caput_bottom = aux.pixel(pix_open, w, 180, menu_top + 54)
        if caput_top == caput_bottom or lumen(caput_top) <= lumen(caput_bottom):
            print(f'DEFECIT: gradientia capitis INITII deest: {caput_top}->{caput_bottom}', file=sys.stderr)
            return 8
        if caput_top[1] <= caput_top[0] or caput_top[2] <= caput_top[0]:
            print(f'DEFECIT: caput INITII accentum viridi-caeruleum amisit: {caput_top}', file=sys.stderr)
            return 9

        programmata_y = menu_top + 92
        tabula_y = programmata_y + 54
        programmata_scopus = programmata_y + 22
        tabula_scopus = tabula_y + 22
        corpus = aux.pixel(pix_open, w, 300, menu_top + 70)
        prog_corpus = aux.pixel(pix_open, w, 300, programmata_scopus)
        tab_corpus = aux.pixel(pix_open, w, 300, tabula_scopus)
        if lumen(corpus) < 500 or lumen(prog_corpus) < 500 or lumen(tab_corpus) < 500:
            print(f'DEFECIT: corpus eburneum INITII obscuratum est: {corpus}/{prog_corpus}/{tab_corpus}', file=sys.stderr)
            return 10

        # Tessera INITIUM in taskbar mutat statum cum pannus apertus est.
        init_open_top = aux.pixel(pix_open, w, 50, taskbar_top + 8)
        init_open_bottom = aux.pixel(pix_open, w, 50, taskbar_top + 31)
        if init_open_top == init_open_bottom or lumen(init_open_top) <= lumen(init_open_bottom):
            print(f'DEFECIT: INITIUM activum non est graduatum: {init_open_top}->{init_open_bottom}', file=sys.stderr)
            return 11
        if init_open_top == init_ante_top and init_open_bottom == init_ante_bottom:
            print('DEFECIT: tessera INITIUM statum apertum non indicat', file=sys.stderr)
            return 12

        mutata_open = aux.differentiae(pix_ante, pix_open)
        if mutata_open < 12000:
            print(f'DEFECIT: pannus INITIUM nimis parum mutavit: {mutata_open}', file=sys.stderr)
            return 13

        # Atlas raster P16-VII manet super tessera composita.
        lumen_programmatum = (236, 194, 113)
        cyan_programmatum = (90, 208, 209)
        clarum_tabulae = (232, 232, 217)
        aqua_tabulae = (145, 194, 191)
        prog_lumen = aux.numerus_coloris_in_recto(pix_open, w, 24, programmata_y + 6, 56, programmata_y + 38, lumen_programmatum)
        prog_cyan = aux.numerus_coloris_in_recto(pix_open, w, 24, programmata_y + 6, 56, programmata_y + 38, cyan_programmatum)
        tab_clarum = aux.numerus_coloris_in_recto(pix_open, w, 24, tabula_y + 6, 56, tabula_y + 38, clarum_tabulae)
        tab_aqua = aux.numerus_coloris_in_recto(pix_open, w, 24, tabula_y + 6, 56, tabula_y + 38, aqua_tabulae)
        if prog_lumen < 40 or prog_cyan < 4 or tab_clarum < 100 or tab_aqua < 40:
            print(f'DEFECIT: atlas INITII mutatus est: P={prog_lumen}/{prog_cyan} T={tab_clarum}/{tab_aqua}', file=sys.stderr)
            return 14

        # Hover TABULA mutat tantum tesseram scopam et lineam aeneam sinistram accendit.
        pos_tabula = aux.move_ad(monitor, out, 'tabula-ix', 150, tabula_scopus, w, h)
        aux.captura(monitor, hover)
        _, _, pix_hover = aux.ppm(hover)
        hover_tab = aux.pixel(pix_hover, w, 300, tabula_scopus)
        hover_prog = aux.pixel(pix_hover, w, 300, programmata_scopus)
        if hover_tab == tab_corpus:
            print(f'DEFECIT: hover TABULA gradientiam non mutavit: {hover_tab}', file=sys.stderr)
            return 15
        if aux.pixel(pix_hover, w, 16, tabula_scopus) != bronzeum:
            print(f'DEFECIT: linea aenea hover TABULAE deest: {aux.pixel(pix_hover,w,16,tabula_scopus)}', file=sys.stderr)
            return 16
        if hover_prog != prog_corpus:
            print(f'DEFECIT: hover TABULA PROGRAMMATA mutavit: {prog_corpus}->{hover_prog}', file=sys.stderr)
            return 17

        aux.click(monitor)
        aux.captura(monitor, post)
        _, _, pix_post = aux.ppm(post)
        if initium_top_quaere(pix_post, w, h, bronzeum) is not None:
            print('DEFECIT: INITIUM post electionem adhuc repertum est', file=sys.stderr)
            return 18

        # TABULA focus P16-VIII accipit; taskbar eundem statum graduatum exprimit.
        focus_pixel = aux.pixel(pix_post, w, 700, 168)
        if focus_pixel != bronzeum:
            print(f'DEFECIT: TABULA focus P16-VIII non accepit: {focus_pixel}', file=sys.stderr)
            return 19
        task_act_top = aux.pixel(pix_post, w, 150, taskbar_top + 8)
        task_act_bottom = aux.pixel(pix_post, w, 150, taskbar_top + 31)
        if task_act_top == task_act_bottom or lumen(task_act_top) <= lumen(task_act_bottom):
            print(f'DEFECIT: tessera TABULA taskbar non est graduata: {task_act_top}->{task_act_bottom}', file=sys.stderr)
            return 20
        if aux.pixel(pix_post, w, 150, taskbar_top + 6) != bronzeum:
            print(f'DEFECIT: tessera activa taskbar limen aeneum amisit: {aux.pixel(pix_post,w,150,taskbar_top+6)}', file=sys.stderr)
            return 21

        mutata_post = aux.differentiae(pix_open, pix_post)
        print(f'INITIUM-IX: top={menu_top} cursor={init_pos}->{pos_initium}->{pos_tabula}')
        print(f'INITIUM-IX: caput={caput_top}->{caput_bottom} corpus={corpus}')
        print(f'INITIUM-IX: initium_taskbar={init_ante_top}->{init_open_top} activa={task_act_top}->{task_act_bottom}')
        print(f'INITIUM-IX: iconae P={prog_lumen}/{prog_cyan} T={tab_clarum}/{tab_aqua} pixeli={mutata_open}/{mutata_post}')
        print('RECTE: P16-IX INITIUM et taskbar compositae sunt, atlas et focus P16-VIII servantur.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())
