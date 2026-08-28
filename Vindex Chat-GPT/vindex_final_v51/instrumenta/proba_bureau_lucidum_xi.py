#!/usr/bin/env python3
"""P16-XI: wallpaper Civitas Aquae I et Bureau Lucidum sub UEFI/QEMU comprobantur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name('proba_formam_sylviae_i.py')
    spec = importlib.util.spec_from_file_location('proba_formam_vii', via)
    if spec is None or spec.loader is None:
        raise RuntimeError('probator formae P16-VII importari non potest')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lumen(c: tuple[int, int, int]) -> int:
    return c[0] + c[1] + c[2]


def copia_coloris(pix: bytes, w: int, x0: int, y0: int, x1: int, y1: int, color: tuple[int, int, int]) -> int:
    n = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            i = (y * w + x) * 3
            if tuple(pix[i:i+3]) == color:
                n += 1
    return n


def principale() -> int:
    if len(sys.argv) != 5:
        print('USUS: proba_bureau_lucidum_xi.py MONITOR QMP EXITUS MORA', file=sys.stderr)
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
        via = out / 'bureau-lucidum-xi.ppm'
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f'DEFECIT: resolutio {w}x{h}', file=sys.stderr)
            return 4

        utilis = h - 40
        limen = utilis * 58 // 100
        graphite = (26, 29, 32)
        aqua = (189, 239, 242)
        cyan = (0, 198, 255)
        argentum = (191, 199, 207)
        bronzeum = (181, 138, 84)
        aqua_obscura = (68, 112, 120)
        aes_obscurum = (105, 79, 55)

        # Caelum et aqua non sunt plani: horizon clarescit, aqua in profundum obscuratur.
        caelum_altum = aux.pixel(pix, w, 400, 36)
        caelum_medium = aux.pixel(pix, w, 400, 300)
        aqua_supera = aux.pixel(pix, w, 400, limen + 12)
        aqua_infera = aux.pixel(pix, w, 400, utilis - 28)
        if caelum_altum == caelum_medium or lumen(caelum_medium) <= lumen(caelum_altum):
            print(f'DEFECIT: caelum lucidum gradientiam amisit: {caelum_altum}->{caelum_medium}', file=sys.stderr)
            return 5
        if aqua_supera == aqua_infera or lumen(aqua_supera) <= lumen(aqua_infera):
            print(f'DEFECIT: aqua profunditatem gradientis amisit: {aqua_supera}->{aqua_infera}', file=sys.stderr)
            return 6
        if aux.pixel(pix, w, 400, limen - 1) != aqua:
            print(f'DEFECIT: horizon JL-UX aquaticus deest: {aux.pixel(pix,w,400,limen-1)}', file=sys.stderr)
            return 7

        # Arcus lucis in caelo, supra horizontem: colores canonici non ex taskbar veniunt.
        regio_arcus = (w * 28 // 100, 20, w - 8, limen - 8)
        aqua_arcus = copia_coloris(pix, w, *regio_arcus, aqua)
        cyan_arcus = copia_coloris(pix, w, *regio_arcus, cyan)
        argentum_arcus = copia_coloris(pix, w, *regio_arcus, argentum)
        bronzeum_arcus = copia_coloris(pix, w, *regio_arcus, bronzeum)
        if aqua_arcus < 90 or cyan_arcus < 50 or argentum_arcus < 45 or bronzeum_arcus < 45:
            print(f'DEFECIT: arcus lucis incompleti aqua/cyan/argentum/bronzeum={aqua_arcus}/{cyan_arcus}/{argentum_arcus}/{bronzeum_arcus}', file=sys.stderr)
            return 8

        # Civitas dextra et reflexiones aquaticae debent esse realiter pictae.
        x0 = w * 55 // 100
        civ_bronzeum = copia_coloris(pix, w, x0, 150, w - 8, limen + 55, bronzeum)
        civ_aqua = copia_coloris(pix, w, x0, 150, w - 8, limen + 55, aqua)
        civ_argentum = copia_coloris(pix, w, x0, 150, w - 8, limen + 55, argentum)
        refl_aqua = copia_coloris(pix, w, x0, limen + 40, w - 8, utilis - 8, aqua_obscura)
        refl_aes = copia_coloris(pix, w, x0, limen + 40, w - 8, utilis - 8, aes_obscurum)
        if civ_bronzeum < 110 or civ_aqua < 70 or civ_argentum < 250:
            print(f'DEFECIT: Civitas Aquae non satis picta bronzeum/aqua/argentum={civ_bronzeum}/{civ_aqua}/{civ_argentum}', file=sys.stderr)
            return 9
        if refl_aqua < 80 or refl_aes < 45:
            print(f'DEFECIT: reflexiones civitatis desunt aqua/aes={refl_aqua}/{refl_aes}', file=sys.stderr)
            return 10

        # Regio inter iconas et scenam dextram manet quieta: nullus neon ibi dominatur.
        quieta_aqua = copia_coloris(pix, w, 220, 80, 320, limen - 12, aqua)
        quieta_cyan = copia_coloris(pix, w, 220, 80, 320, limen - 12, cyan)
        if quieta_aqua > 4 or quieta_cyan > 4:
            print(f'DEFECIT: regio iconarum non quieta est aqua/cyan={quieta_aqua}/{quieta_cyan}', file=sys.stderr)
            return 11

        # Emblema et quattuor iconae rasterae historicae servantur.
        gemma = (234, 255, 255)
        centrum = (75, 81, 73)
        if aux.pixel(pix, w, 180, 23) != gemma or aux.pixel(pix, w, 180, 34) != centrum:
            print('DEFECIT: emblema rasterum P16-VII mutatum est', file=sys.stderr)
            return 12
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
                return 13

        # Taskbar P16-IX manet separata a wallpaper.
        taskbar_top = h - 40
        si_taskbar = aux.pixel(pix, w, 400, taskbar_top + 4)
        if si_taskbar == graphite:
            print('DEFECIT: taskbar IX a wallpaper vel colore plano deleta est', file=sys.stderr)
            return 14

        print(f'BUREAU-LUCIDUM-XI: caelum={caelum_altum}->{caelum_medium} aqua={aqua_supera}->{aqua_infera} limen={limen}')
        print(f'BUREAU-LUCIDUM-XI: arcus={aqua_arcus}/{cyan_arcus}/{argentum_arcus}/{bronzeum_arcus}')
        print(f'BUREAU-LUCIDUM-XI: civitas={civ_bronzeum}/{civ_aqua}/{civ_argentum} reflexiones={refl_aqua}/{refl_aes}')
        print('RECTE: P16-XI Civitas Aquae I, regio quieta, emblema et iconographia rastera in framebuffer vero apparent.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())
