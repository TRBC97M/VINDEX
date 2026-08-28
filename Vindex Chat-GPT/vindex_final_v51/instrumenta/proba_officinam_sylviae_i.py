#!/usr/bin/env python3
"""P18-I/P16-VI: OFFICINA SYLVIAE, editor et claviatura sub UEFI/QEMU probantur."""
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
    responsum = aux.hmp(monitor, f'sendkey {clavis}')
    if 'unknown command' in responsum.lower():
        raise RuntimeError('HMP sendkey deest')
    time.sleep(0.18)


def scribe(aux: object, monitor: socket.socket, claves: tuple[str, ...]) -> None:
    for clavis in claves:
        mitte_clavem(aux, monitor, clavis)


def principale() -> int:
    if len(sys.argv) != 5:
        print('USUS: proba_officinam_sylviae_i.py MONITOR QMP EXITUS MORA', file=sys.stderr)
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

        ante = out / 'officina-ante.ppm'
        apertum = out / 'officina-aperta.ppm'
        prima = out / 'officina-prima.ppm'
        secunda = out / 'officina-secunda.ppm'
        sursum = out / 'officina-sursum.ppm'
        insertum = out / 'officina-insertum.ppm'

        aux.captura(monitor, ante)
        w, h, pix_ante = aux.ppm(ante)
        if (w, h) != (1280, 800):
            print(f'DEFECIT: resolutio {w}x{h}', file=sys.stderr)
            return 4

        # Quarta applicatio in catalogo P16-IV: index III, y = 384.
        pos = aux.move_ad(monitor, out, 'officina', 70, 422, w, h)
        aux.click(monitor)
        time.sleep(0.5)
        aux.captura(monitor, apertum)
        _, _, pix_open = aux.ppm(apertum)

        bronzeum = (185, 138, 82)
        nox = (28, 31, 32)
        papyrus = (219, 211, 196)
        charta = (250, 249, 245)
        selectum = (238, 232, 219)

        # Geometria P18-I ad 1280x800: fenestra x=153 y=64; clientis x=163 y=124.
        if aux.pixel(pix_open, w, 500, 64) != bronzeum:
            print(f'DEFECIT: OFFICINA focus non accepit: {aux.pixel(pix_open,w,500,64)}', file=sys.stderr)
            return 5
        if aux.pixel(pix_open, w, 200, 130) != nox:
            print(f'DEFECIT: caput graphiticum OFFICINAE deest: {aux.pixel(pix_open,w,200,130)}', file=sys.stderr)
            return 6
        if aux.pixel(pix_open, w, 200, 170) != papyrus:
            print(f'DEFECIT: fascia papyracea editoris deest: {aux.pixel(pix_open,w,200,170)}', file=sys.stderr)
            return 7
        if aux.pixel(pix_open, w, 400, 200) not in (charta, selectum):
            print(f'DEFECIT: charta editoris P16-VI deest: {aux.pixel(pix_open,w,400,200)}', file=sys.stderr)
            return 8

        # VINDEX in prima linea: QEMU -> UEFI -> Fenestrale -> OFFICINA.
        scribe(aux, monitor, ('shift-v', 'shift-i', 'shift-n', 'shift-d', 'shift-e', 'shift-x'))
        time.sleep(0.4)
        aux.captura(monitor, prima)
        _, _, pix_prima = aux.ppm(prima)
        prima_mut = diff_regio(pix_open, pix_prima, w, 215, 190, 310, 210)
        if prima_mut < 45:
            print(f'DEFECIT: VINDEX in prima linea non apparuit: {prima_mut}', file=sys.stderr)
            return 9

        # ENTER dividit documentum, deinde SYLVIA in secunda linea scribitur.
        mitte_clavem(aux, monitor, 'ret')
        scribe(aux, monitor, ('shift-s', 'shift-y', 'shift-l', 'shift-v', 'shift-i', 'shift-a'))
        time.sleep(0.4)
        aux.captura(monitor, secunda)
        _, _, pix_secunda = aux.ppm(secunda)
        secunda_mut = diff_regio(pix_prima, pix_secunda, w, 210, 190, 320, 228)
        if secunda_mut < 80:
            print(f'DEFECIT: secunda linea editoris non apparuit: {secunda_mut}', file=sys.stderr)
            return 10

        # Sagitta sursum ad lineam priorem pertinet; fenestra ipsa manere debet y=64.
        mitte_clavem(aux, monitor, 'up')
        time.sleep(0.35)
        aux.captura(monitor, sursum)
        _, _, pix_sursum = aux.ppm(sursum)
        sursum_mut = diff_regio(pix_secunda, pix_sursum, w, 163, 190, 520, 228)
        if sursum_mut < 60:
            print(f'DEFECIT: sagitta sursum cursorem OFFICINAE non movit: {sursum_mut}', file=sys.stderr)
            return 11
        if aux.pixel(pix_sursum, w, 500, 64) != bronzeum:
            print('DEFECIT: sagitta OFFICINAE fenestram movit loco cursoris', file=sys.stderr)
            return 12

        # Sinistra + A probant insertionem ad cursorem editoris focalis.
        mitte_clavem(aux, monitor, 'left')
        mitte_clavem(aux, monitor, 'shift-a')
        time.sleep(0.4)
        aux.captura(monitor, insertum)
        _, _, pix_insertum = aux.ppm(insertum)
        insertio_mut = diff_regio(pix_sursum, pix_insertum, w, 215, 190, 320, 210)
        if insertio_mut < 20:
            print(f'DEFECIT: insertio interna OFFICINAE non apparuit: {insertio_mut}', file=sys.stderr)
            return 13
        if aux.pixel(pix_insertum, w, 500, 64) != bronzeum:
            print('DEFECIT: sagitta sinistra fenestram OFFICINAE movit', file=sys.stderr)
            return 14

        # Status bar debet mutationem documenti indicare.
        status_mut = diff_regio(pix_open, pix_insertum, w, 163, 515, 360, 555)
        if status_mut < 20:
            print(f'DEFECIT: status MODIFICATUM non apparuit: {status_mut}', file=sys.stderr)
            return 15

        print(f'OFFICINA: cursor={pos} prima_pixeli={prima_mut} secunda_pixeli={secunda_mut}')
        print(f'OFFICINA: sursum_pixeli={sursum_mut} insertio_pixeli={insertio_mut} status_pixeli={status_mut}')
        print('RECTE: P18-I/P16-VI OFFICINA eburnea duas lineas editat et sagittas per UEFI accipit.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())
