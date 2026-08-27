#!/usr/bin/env python3
"""P19-II: OFFICINA persistens in bureau Sylviae per QEMU exercetur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def importa_modulum(nomen: str, fasciculus: str) -> object:
    via = Path(__file__).resolve().with_name(fasciculus)
    spec = importlib.util.spec_from_file_location(nomen, via)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'probator importari non potest: {fasciculus}')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mitte(aux: object, monitor: socket.socket, clavis: str, mora: float = 0.13) -> None:
    responsum = aux.hmp(monitor, f'sendkey {clavis}')
    if 'unknown command' in responsum.lower():
        raise RuntimeError(f'HMP sendkey deest: {clavis}')
    time.sleep(mora)


def scribe_maiusculas(aux: object, monitor: socket.socket, textus: str) -> None:
    for c in textus:
        if 'A' <= c <= 'Z':
            mitte(aux, monitor, f'shift-{c.lower()}')
        elif '0' <= c <= '9':
            mitte(aux, monitor, c)
        else:
            raise ValueError(f'littera probationis non sustenta: {c!r}')


def principale() -> int:
    if len(sys.argv) != 6:
        print('USUS: proba_officinam_persistentem_ii.py MONITOR QMP EXITUS MORA MODUS', file=sys.stderr)
        return 2

    aux = importa_modulum('proba_initium_ii', 'proba_initium_sylviae_ii.py')
    ps2 = importa_modulum('proba_fenestrale_ps2', 'proba_fenestrale_uefi_purum.py')
    mon_via = Path(sys.argv[1])
    qmp_via = Path(sys.argv[2])
    out = Path(sys.argv[3])
    mora = float(sys.argv[4])
    modus = int(sys.argv[5])
    if modus not in (1, 2):
        print('DEFECIT: modus debet esse 1 aut 2', file=sys.stderr)
        return 2

    finis = time.time() + 15.0
    while (not mon_via.exists() or not qmp_via.exists()) and time.time() < finis:
        time.sleep(0.1)
    if not mon_via.exists() or not qmp_via.exists():
        print('DEFECIT: monitor vel QMP QEMU deest', file=sys.stderr)
        return 3

    out.mkdir(parents=True, exist_ok=True)
    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    monitor.settimeout(0.7)
    monitor.connect(str(mon_via))
    q = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    q.settimeout(2.0)
    q.connect(str(qmp_via))
    try:
        aux.lege_usque(monitor, b'(qemu) ', 2.0)
        salutatio = ps2.qmp_linea(q)
        if 'QMP' not in salutatio:
            print('DEFECIT: salutatio QMP invalida', file=sys.stderr)
            return 4
        ps2.qmp(q, 'qmp_capabilities')
        mures = ps2.qmp(q, 'query-mice').get('return', [])
        candidati = [m for m in mures if 'PS/2 Mouse' in str(m.get('name', ''))]
        if not candidati:
            print('DEFECIT: QEMU PS/2 Mouse deest', file=sys.stderr)
            return 5
        index = int(candidati[0]['index'])
        aux.hmp(monitor, f'mouse_set {index}')
        print(f'OFFICINA-P19-II: mus_ps2_index={index}')
        time.sleep(mora)

        ante = out / f'officina-p19-ii-{modus}-ante.ppm'
        aperta = out / f'officina-p19-ii-{modus}-aperta.ppm'
        servata = out / f'officina-p19-ii-{modus}-servata.ppm'
        aux.captura(monitor, ante)
        w, h, _pix = aux.ppm(ante)
        if (w, h) != (1280, 800):
            print(f'DEFECIT: resolutio {w}x{h}', file=sys.stderr)
            return 6

        # OFFICINA est quarta applicatio bureau P16-IV.
        pos = aux.move_ad(monitor, out, f'officina-p19-ii-{modus}', 70, 422, w, h)
        aux.click(monitor)
        time.sleep(0.45)
        aux.captura(monitor, aperta)
        _, _, pix_open = aux.ppm(aperta)
        bronzeum = (185, 138, 82)
        if aux.pixel(pix_open, w, 500, 64) != bronzeum:
            print('DEFECIT: OFFICINA focus non accepit', file=sys.stderr)
            return 7

        if modus == 1:
            scribe_maiusculas(aux, monitor, 'ZEPHYR72941')
            mitte(aux, monitor, 'ret')
            scribe_maiusculas(aux, monitor, 'NOVAPERSISTET')
        else:
            # OP_INIT cursor ad initium primae lineae ponit. Deorsum ad secundam,
            # deinde XIII dextrae ad finem NOVAPERSISTET; si fasciculus non
            # relectus esset, hae claves nihil utile moverent et solum X servaretur.
            mitte(aux, monitor, 'down')
            for _ in range(13):
                mitte(aux, monitor, 'right', 0.08)
            scribe_maiusculas(aux, monitor, 'X')

        # EFI scan XII = F2, a P19-II OFFICINAE ut SERVA routatur.
        mitte(aux, monitor, 'f2', 0.8)
        aux.captura(monitor, servata)
        _, _, pix_saved = aux.ppm(servata)
        if aux.pixel(pix_saved, w, 500, 64) != bronzeum:
            print('DEFECIT: F2 focum OFFICINAE amisit', file=sys.stderr)
            return 8

        print(f'OFFICINA-P19-II: initium={modus} cursor_bureau={pos} F2=missum')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()
        q.close()


if __name__ == '__main__':
    raise SystemExit(principale())
