#!/usr/bin/env python3
"""P16-IX: taskbar composita cum identitate rastera Sylviae sub UEFI/QEMU comprobatur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from collections import Counter
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name('proba_formam_sylviae_i.py')
    spec = importlib.util.spec_from_file_location('proba_formam_vii', via)
    if spec is None or spec.loader is None:
        raise RuntimeError('probator formae P16-VII importari non potest')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lumen(color: tuple[int, int, int]) -> int:
    return color[0] + color[1] + color[2]


def principale() -> int:
    if len(sys.argv) != 5:
        print('USUS: proba_formam_sylviae_ix.py MONITOR QMP EXITUS MORA', file=sys.stderr)
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
    monitor.settimeout(0.4)
    monitor.connect(str(mon_via))
    try:
        aux.lege_usque(monitor, b'(qemu) ', 2.0)
        time.sleep(mora)
        via = out / 'forma-sylviae-ix.ppm'
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f'DEFECIT: resolutio {w}x{h}', file=sys.stderr)
            return 4

        nox_vetus = (28, 31, 32)
        ebur = (241, 238, 228)
        bronzeum = (185, 138, 82)
        aqua = (103, 164, 160)
        taskbar_top = h - 40

        # Limes aeneus et linea aquatica totam taskbar iam definiunt.
        linea_bronzea = aux.numerus_coloris_in_linea(pix, w, taskbar_top, bronzeum)
        linea_aqua = aux.numerus_coloris_in_linea(pix, w, taskbar_top + 2, aqua)
        if linea_bronzea < w * 95 // 100:
            print(f'DEFECIT: limes aeneus taskbar IX interruptus est: {linea_bronzea}', file=sys.stderr)
            return 5
        if linea_aqua < w * 95 // 100:
            print(f'DEFECIT: lumen aquaticum taskbar IX interruptum est: {linea_aqua}', file=sys.stderr)
            return 6

        # Corpus taskbar non est amplius aplanatum: gradientia graphitico-viridis descendit.
        fundum_top = aux.pixel(pix, w, 400, taskbar_top + 4)
        fundum_bottom = aux.pixel(pix, w, 400, taskbar_top + 36)
        if fundum_top == fundum_bottom or lumen(fundum_top) <= lumen(fundum_bottom):
            print(f'DEFECIT: gradientia taskbar deest: {fundum_top}->{fundum_bottom}', file=sys.stderr)
            return 7
        if fundum_top[1] <= fundum_top[0] or fundum_top[2] <= fundum_top[0]:
            print(f'DEFECIT: taskbar accentum viridi-caeruleum amisit: {fundum_top}', file=sys.stderr)
            return 8

        # INITIUM et regio dextra ipsae gradientias habent, hitbox veteri intacta.
        init_top = aux.pixel(pix, w, 50, taskbar_top + 8)
        init_bottom = aux.pixel(pix, w, 50, taskbar_top + 31)
        if init_top == init_bottom or lumen(init_top) <= lumen(init_bottom):
            print(f'DEFECIT: tessera INITIUM non est graduata: {init_top}->{init_bottom}', file=sys.stderr)
            return 9
        tray_x = w - 126
        tray_top = aux.pixel(pix, w, tray_x + 60, taskbar_top + 8)
        tray_bottom = aux.pixel(pix, w, tray_x + 60, taskbar_top + 31)
        if tray_top == tray_bottom or lumen(tray_top) <= lumen(tray_bottom):
            print(f'DEFECIT: regio systematis dextra non est graduata: {tray_top}->{tray_bottom}', file=sys.stderr)
            return 10

        # Bureau P16-VII manet in eadem geometria, cum marca et atlas SIMG intactis.
        if aux.pixel(pix, w, 20, 74) != nox_vetus or aux.pixel(pix, w, 20, 178) != nox_vetus:
            print('DEFECIT: tesserae bureau P16-VII motae vel mutatae sunt', file=sys.stderr)
            return 11
        ebur_tituli = aux.numerus_coloris_in_recto(pix, w, 16, 16, 150, 48, ebur)
        if ebur_tituli < 250:
            print(f'DEFECIT: marca SYLVIA 2x non videtur: ebur={ebur_tituli}', file=sys.stderr)
            return 12

        gemma = (234, 255, 255)
        centrum = (75, 81, 73)
        aes_iconis = (198, 147, 73)
        if aux.pixel(pix, w, 180, 23) != gemma or aux.pixel(pix, w, 180, 34) != centrum:
            print('DEFECIT: emblema rasterum P16-VII mutatum est', file=sys.stderr)
            return 13
        gemmae = aux.numerus_coloris_in_recto(pix, w, 164, 18, 196, 50, gemma)
        aera = aux.numerus_coloris_in_recto(pix, w, 164, 18, 196, 50, aes_iconis)
        if gemmae < 40 or aera < 40:
            print(f'DEFECIT: copia pixelorum emblematis nimis parva: gemma={gemmae} aes={aera}', file=sys.stderr)
            return 14

        centra = (
            ('PROGRAMMATA', 72, 104, (236, 194, 113)),
            ('TABULA', 72, 208, (201, 154, 82)),
            ('TERMINALE', 72, 312, (17, 28, 33)),
            ('OFFICINA', 72, 416, (232, 232, 217)),
        )
        for nomen, x, y, exspectatum in centra:
            visum = aux.pixel(pix, w, x, y)
            if visum != exspectatum:
                print(f'DEFECIT: centrum iconis {nomen} rasterae: {visum} loco {exspectatum}', file=sys.stderr)
                return 15

        raster_nox = (27, 30, 31)
        copiae: list[int] = []
        for y0 in (80, 184, 288, 392):
            copia = aux.numerus_coloris_in_recto(pix, w, 48, y0, 96, y0 + 48, raster_nox)
            copiae.append(copia)
            if copia < 600:
                print(f'DEFECIT: tessera rastera ad y={y0} incompleta est: nox={copia}', file=sys.stderr)
                return 16

        colores = Counter(tuple(pix[i:i+3]) for i in range(0, len(pix)-2, 3))
        print(f'FORMA-IX: resolutio={w}x{h} taskbar=40')
        print(f'FORMA-IX: taskbar={fundum_top}->{fundum_bottom} initium={init_top}->{init_bottom} tray={tray_top}->{tray_bottom}')
        print(f'FORMA-IX: lineae bronzeum/aqua={linea_bronzea}/{linea_aqua} colores={sum(1 for _,n in colores.items() if n>30)}')
        print(f'FORMA-IX: emblema={gemmae}/{aera} iconae={",".join(str(n) for n in copiae)}')
        print('RECTE: P16-IX taskbar composita est et identitas rastera P16-VII intacta manet.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())
