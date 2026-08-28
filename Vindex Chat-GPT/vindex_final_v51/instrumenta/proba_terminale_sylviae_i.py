#!/usr/bin/env python3
"""P17-II/P16-VI: TERMINALE, claviatura, mandata et historia sub QEMU probantur."""
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


def diff_regio(a: bytes, b: bytes, w: int, x0: int, y0: int, x1: int, y1: int) -> int:
    mutata = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            i = (y * w + x) * 3
            if a[i:i+3] != b[i:i+3]:
                mutata += 1
    return mutata


def mitte_clavem(aux: object, monitor: socket.socket, clavis: str) -> None:
    responsum = aux.hmp(monitor, f"sendkey {clavis}")
    if 'unknown command' in responsum.lower():
        raise RuntimeError('HMP sendkey deest')
    time.sleep(0.18)


def principale() -> int:
    if len(sys.argv) != 5:
        print('USUS: proba_terminale_sylviae_i.py MONITOR QMP EXITUS MORA', file=sys.stderr)
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

        ante = out / 'terminale-ante.ppm'
        apertum = out / 'terminale-apertum.ppm'
        scriptum = out / 'terminale-scriptum.ppm'
        post = out / 'terminale-post.ppm'
        versio = out / 'terminale-versio.ppm'
        memoria = out / 'terminale-memoria.ppm'
        memoria_post = out / 'terminale-memoria-post.ppm'
        aux.captura(monitor, ante)
        w, h, pix_ante = aux.ppm(ante)
        if (w, h) != (1280, 800):
            print(f'DEFECIT: resolutio {w}x{h}', file=sys.stderr)
            return 4

        # Tertia applicatio in bureau P16-IV: index II, y=280.
        pos = aux.move_ad(monitor, out, 'terminale', 70, 318, w, h)
        aux.click(monitor)
        aux.captura(monitor, apertum)
        _, _, pix_open = aux.ppm(apertum)

        bronzeum = (185, 138, 82)
        carbonem = (22, 24, 23)
        lapis = (49, 55, 55)
        if aux.pixel(pix_open, w, 500, 96) != bronzeum:
            print(f'DEFECIT: TERMINALE focus non accepit: {aux.pixel(pix_open,w,500,96)}', file=sys.stderr)
            return 5
        # Fenestra TERMINALE: x=230 y=96; clientis superficies incipit x=240 y=156.
        if aux.pixel(pix_open, w, 300, 200) != carbonem:
            print(f'DEFECIT: superficies TERMINALIS carbonaria deest: {aux.pixel(pix_open,w,300,200)}', file=sys.stderr)
            return 6
        if aux.pixel(pix_open, w, 300, 160) != lapis or aux.pixel(pix_open, w, 300, 183) != bronzeum:
            print('DEFECIT: caput lapideum TERMINALIS P16-VI deest', file=sys.stderr)
            return 7

        # SALVE maiusculum per claviaturam QEMU → UEFI → coda Fenestralis → clientem.
        for clavis in ('shift-s', 'shift-a', 'shift-l', 'shift-v', 'shift-e'):
            mitte_clavem(aux, monitor, clavis)
        time.sleep(0.5)
        aux.captura(monitor, scriptum)
        _, _, pix_typed = aux.ppm(scriptum)
        prompt_mut = diff_regio(pix_open, pix_typed, w, 270, 424, 380, 454)
        if prompt_mut < 40:
            print(f'DEFECIT: linea SALVE in TERMINALE non apparuit: {prompt_mut}', file=sys.stderr)
            return 8

        mitte_clavem(aux, monitor, 'ret')
        time.sleep(0.8)
        aux.captura(monitor, post)
        _, _, pix_post = aux.ppm(post)
        responsum_mut = diff_regio(pix_open, pix_post, w, 248, 224, 560, 254)
        prompt_clear = diff_regio(pix_typed, pix_post, w, 270, 424, 380, 454)
        if responsum_mut < 60:
            print(f'DEFECIT: responsum SALVE non apparuit: {responsum_mut}', file=sys.stderr)
            return 9
        if prompt_clear < 40:
            print(f'DEFECIT: linea post ENTER non purgata est: {prompt_clear}', file=sys.stderr)
            return 10

        # Secundum mandatum transcriptum auget; deinde ↑↑ SALVE ex historia revocat.
        for clavis in ('shift-v', 'shift-e', 'shift-r', 'shift-s', 'shift-i', 'shift-o'):
            mitte_clavem(aux, monitor, clavis)
        mitte_clavem(aux, monitor, 'ret')
        time.sleep(0.7)
        aux.captura(monitor, versio)
        _, _, pix_versio = aux.ppm(versio)
        versio_mut = diff_regio(pix_post, pix_versio, w, 248, 224, 560, 254)
        if versio_mut < 40:
            print(f'DEFECIT: responsum VERSIO non mutavit: {versio_mut}', file=sys.stderr)
            return 11

        mitte_clavem(aux, monitor, 'up')
        mitte_clavem(aux, monitor, 'up')
        time.sleep(0.5)
        aux.captura(monitor, memoria)
        _, _, pix_memoria = aux.ppm(memoria)
        historia_mut = diff_regio(pix_versio, pix_memoria, w, 270, 424, 380, 454)
        if historia_mut < 40:
            print(f'DEFECIT: historia ↑↑ lineam non revocavit: {historia_mut}', file=sys.stderr)
            return 12
        if aux.pixel(pix_memoria, w, 500, 96) != bronzeum:
            print('DEFECIT: sagitta historiae fenestram TERMINALE movit', file=sys.stderr)
            return 13

        mitte_clavem(aux, monitor, 'ret')
        time.sleep(0.7)
        aux.captura(monitor, memoria_post)
        _, _, pix_memoria_post = aux.ppm(memoria_post)
        historia_responsum = diff_regio(pix_versio, pix_memoria_post, w, 248, 224, 560, 254)
        historia_purgata = diff_regio(pix_memoria, pix_memoria_post, w, 270, 424, 380, 454)
        if historia_responsum < 40:
            print(f'DEFECIT: SALVE revocatum non exsecutum est: {historia_responsum}', file=sys.stderr)
            return 14
        if historia_purgata < 40:
            print(f'DEFECIT: linea revocata post ENTER non purgata est: {historia_purgata}', file=sys.stderr)
            return 15

        print(f'TERMINALE: cursor={pos} prompt_pixeli={prompt_mut} responsum_pixeli={responsum_mut}')
        print(f'TERMINALE-II: versio_pixeli={versio_mut} historia_pixeli={historia_mut} responsum_historiae={historia_responsum}')
        print('RECTE: P17-II/P16-VI TERMINALE carbonarium historiam et mandata per UEFI exercet.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())
