#!/usr/bin/env python3
"""P16-XI: Bureau Lucidum et testa JL-UX in framebuffer vero QEMU/OVMF probantur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name('proba_formam_sylviae_i.py')
    spec = importlib.util.spec_from_file_location('proba_formam_xi', via)
    if spec is None or spec.loader is None:
        raise RuntimeError('probator formae importari non potest')
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


def colores_recti(pix: bytes, w: int, x0: int, y0: int, x1: int, y1: int) -> set[tuple[int, int, int]]:
    out: set[tuple[int, int, int]] = set()
    for y in range(y0, y1):
        for x in range(x0, x1):
            i = (y * w + x) * 3
            out.add(tuple(pix[i:i+3]))
    return out


def pixeli_lucidi(pix: bytes, w: int, x0: int, y0: int, x1: int, y1: int, limen: int) -> int:
    n = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            i = (y * w + x) * 3
            if pix[i] + pix[i+1] + pix[i+2] >= limen:
                n += 1
    return n


def color_proximus(visum: tuple[int, int, int], exspectatum: tuple[int, int, int], tolerantia: int = 3) -> bool:
    return all(abs(a - b) <= tolerantia for a, b in zip(visum, exspectatum))


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
        via = out / 'bureau-lucidum-xi-shell.ppm'
        aux.captura(monitor, via)
        w, h, pix = aux.ppm(via)
        if (w, h) != (1280, 800):
            print(f'DEFECIT: resolutio {w}x{h}', file=sys.stderr)
            return 4

        utilis = h - 40
        limen = utilis * 57 // 100
        graphite = (26, 29, 32)
        cool = (74, 96, 114)
        ebur = (242, 244, 247)
        aqua = (189, 239, 242)
        cyan = (0, 198, 255)
        argentum = (191, 199, 207)
        bronzeum = (181, 138, 84)

        # Civitas Aquae manet scaena, sed non ipsa refectio tota est.
        caelum_altum = aux.pixel(pix, w, 500, 36)
        caelum_limen = aux.pixel(pix, w, 500, limen - 24)
        aqua_supera = aux.pixel(pix, w, 500, limen + 18)
        aqua_infera = aux.pixel(pix, w, 500, utilis - 26)
        if caelum_altum == caelum_limen or lumen(caelum_limen) <= lumen(caelum_altum):
            print(f'DEFECIT: caelum P16-XI non clarescit ad horizontem: {caelum_altum}->{caelum_limen}', file=sys.stderr)
            return 5
        if aqua_supera == aqua_infera or lumen(aqua_supera) <= lumen(aqua_infera):
            print(f'DEFECIT: aqua P16-XI profunditatem amisit: {aqua_supera}->{aqua_infera}', file=sys.stderr)
            return 6
        if aux.pixel(pix, w, 620, limen - 2) != aqua:
            print(f'DEFECIT: linea horizon Aqua Light deest: {aux.pixel(pix,w,620,limen-2)}', file=sys.stderr)
            return 7

        regio_arcus = (w * 31 // 100, 12, w - 6, limen - 8)
        aq_arc = copia_coloris(pix, w, *regio_arcus, aqua)
        cy_arc = copia_coloris(pix, w, *regio_arcus, cyan)
        br_arc = copia_coloris(pix, w, *regio_arcus, bronzeum)
        if aq_arc < 70 or cy_arc < 30 or br_arc < 30:
            print(f'DEFECIT: arcus JL-UX non satis manifesti aqua/cyan/bronze={aq_arc}/{cy_arc}/{br_arc}', file=sys.stderr)
            return 8

        x0 = w * 52 // 100
        civ_bronze = copia_coloris(pix, w, x0, 150, w - 4, limen + 54, bronzeum)
        civ_aqua = copia_coloris(pix, w, x0, 150, w - 4, limen + 54, aqua)
        civ_silver = copia_coloris(pix, w, x0, 150, w - 4, limen + 54, argentum)
        if civ_bronze < 90 or civ_aqua < 55 or civ_silver < 180:
            print(f'DEFECIT: civitas P16-XI non satis picta bronze/aqua/silver={civ_bronze}/{civ_aqua}/{civ_silver}', file=sys.stderr)
            return 9

        # Marca top-left nunc est modulus Vitrum Minerale, non titulus nudus.
        ident = (14, 12, 244, 62)
        id_graphite = copia_coloris(pix, w, *ident, graphite)
        id_silver = copia_coloris(pix, w, *ident, argentum)
        id_aqua = copia_coloris(pix, w, *ident, aqua)
        id_bronze = copia_coloris(pix, w, *ident, bronzeum)
        if id_graphite < 700 or id_silver < 100 or id_aqua < 100 or id_bronze < 90:
            print(f'DEFECIT: identitas mineralis incompleta graphite/silver/aqua/bronze={id_graphite}/{id_silver}/{id_aqua}/{id_bronze}', file=sys.stderr)
            return 10
        if aux.pixel(pix, w, 100, 18) != aqua or aux.pixel(pix, w, 22, 30) != bronzeum:
            print('DEFECIT: lineae canonicae identitatis XI desunt', file=sys.stderr)
            return 11

        # Vetus tessera eburnea 108x88 disparuit. Restat objectum compactum:
        # podium iconis + capsula tituli; hitbox tamen eadem est.
        card = (18, 72, 126, 160)
        card_lucidi = pixeli_lucidi(pix, w, *card, 600)
        card_graphite = copia_coloris(pix, w, *card, graphite)
        card_silver = copia_coloris(pix, w, *card, argentum)
        card_aqua = copia_coloris(pix, w, *card, aqua)
        card_bronze = copia_coloris(pix, w, *card, bronzeum)
        card_colores = colores_recti(pix, w, *card)
        if card_lucidi >= 3200:
            print(f'DEFECIT: vetus tessera clara adhuc dominatur: lucidi={card_lucidi}', file=sys.stderr)
            return 12
        if card_graphite < 500 or card_silver < 100 or card_aqua < 30 or card_bronze < 30 or len(card_colores) < 30:
            print(f'DEFECIT: objectum desktop XI incompletum graphite/silver/aqua/bronze/colores={card_graphite}/{card_silver}/{card_aqua}/{card_bronze}/{len(card_colores)}', file=sys.stderr)
            return 13
        if aux.pixel(pix, w, 72, 73) != argentum:
            print(f'DEFECIT: podium argentum PROGRAMMATUM deest: {aux.pixel(pix,w,72,73)}', file=sys.stderr)
            return 14
        if aux.pixel(pix, w, 72, 77) != aqua:
            print(f'DEFECIT: lumen Aqua podii PROGRAMMATUM deest: {aux.pixel(pix,w,72,77)}', file=sys.stderr)
            return 15
        if aux.pixel(pix, w, 72, 131) != bronzeum:
            print(f'DEFECIT: clavis Bronze podii PROGRAMMATUM deest: {aux.pixel(pix,w,72,131)}', file=sys.stderr)
            return 16
        if aux.pixel(pix, w, 30, 140) != graphite:
            print(f'DEFECIT: capsula tituli Graphite deest: {aux.pixel(pix,w,30,140)}', file=sys.stderr)
            return 17

        # Centra iconarum servant identitatem rasteram. Quia atlas RGBA super
        # Vitrum Minerale componitur, subpixelus alpha unum vel duo gradus mutare potest.
        centra = (
            ('PROGRAMMATA', 72, 104, (236, 194, 113)),
            ('TABULA', 72, 208, (201, 154, 82)),
            ('TERMINALE', 72, 312, (17, 28, 33)),
            ('OFFICINA', 72, 416, (232, 232, 217)),
        )
        for nomen, x, y, exspectatum in centra:
            visum = aux.pixel(pix, w, x, y)
            if not color_proximus(visum, exspectatum):
                print(f'DEFECIT: centrum iconis {nomen}: {visum} longe a {exspectatum}', file=sys.stderr)
                return 18

        # Taskbar XI est rail fluitans: Silver exterior, Aqua lumen, Graphite corpus.
        taskbar_top = h - 40
        rail_silver = aux.pixel(pix, w, 400, taskbar_top + 4)
        rail_aqua = aux.pixel(pix, w, 400, taskbar_top + 7)
        rail_graphite = aux.pixel(pix, w, 400, taskbar_top + 20)
        rail_cool = aux.pixel(pix, w, 400, taskbar_top + 34)
        if rail_silver != argentum or rail_aqua != aqua or rail_graphite != graphite or rail_cool != cool:
            print(f'DEFECIT: rail XI materia errat: {rail_silver}/{rail_aqua}/{rail_graphite}/{rail_cool}', file=sys.stderr)
            return 19

        print(f'BUREAU-XI-SHELL: caelum={caelum_altum}->{caelum_limen} aqua={aqua_supera}->{aqua_infera} limen={limen}')
        print(f'BUREAU-XI-SHELL: arcus aqua/cyan/bronze={aq_arc}/{cy_arc}/{br_arc}')
        print(f'BUREAU-XI-SHELL: identitas graphite/silver/aqua/bronze={id_graphite}/{id_silver}/{id_aqua}/{id_bronze}')
        print(f'BUREAU-XI-SHELL: objectum lucidi/graphite/silver/aqua/bronze={card_lucidi}/{card_graphite}/{card_silver}/{card_aqua}/{card_bronze}')
        print('RECTE: P16-XI in framebuffer vero: objecta desktop, identitas mineralis et rail JL-UX apparent.')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()


if __name__ == '__main__':
    raise SystemExit(principale())