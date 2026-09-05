#!/usr/bin/env python3
"""P16-XI-B: INITIUM premium et semantica input sub QEMU/OVMF probantur."""
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
        raise RuntimeError(f"auxilia importari non possunt: {fasciculus}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def lumen(c: tuple[int, int, int]) -> int:
    return c[0] + c[1] + c[2]


def colores(aux: object, pix: bytes, w: int, regio: tuple[int, int, int, int]) -> set[tuple[int, int, int]]:
    x0, y0, x1, y1 = regio
    out: set[tuple[int, int, int]] = set()
    for y in range(y0, y1):
        for x in range(x0, x1):
            out.add(aux.pixel(pix, w, x, y))
    return out


def numerus_coloris(aux: object, pix: bytes, w: int, regio: tuple[int, int, int, int], color: tuple[int, int, int]) -> int:
    x0, y0, x1, y1 = regio
    return sum(aux.pixel(pix, w, x, y) == color for y in range(y0, y1) for x in range(x0, x1))


def move_ad_firmus(
    aux: object,
    monitor: socket.socket,
    out: Path,
    nomen: str,
    x: int,
    y: int,
    w: int,
    h: int,
) -> tuple[int, int]:
    """Paquetum HMP perditum tolerat, sed framebuffer cursorem probare semper debet."""
    ultimus: RuntimeError | None = None
    for tentamen in range(4):
        try:
            return aux.move_ad(monitor, out, f"{nomen}-t{tentamen}", x, y, w, h)
        except RuntimeError as exc:
            ultimus = exc
            textus = str(exc)
            if "motus muris non consumptus" not in textus and "cursor scopum" not in textus:
                raise
            time.sleep(0.18)
    if ultimus is not None:
        raise ultimus
    raise RuntimeError(f"cursor ad {nomen} moveri non potest")


def qmp_bulla(ps2: object, q: socket.socket, pressa: bool, dx: int) -> None:
    """Bullam sinistram cum fasciculo relativo per input-send-event vehit."""
    eventa: list[dict] = [
        {"type": "btn", "data": {"down": pressa, "button": "left"}},
    ]
    if dx != 0:
        eventa.append({"type": "rel", "data": {"axis": "x", "value": dx}})
    responsum = ps2.qmp(q, "input-send-event", {"events": eventa})
    if "error" in responsum:
        status = "pressam" if pressa else "relaxatam"
        raise RuntimeError(f"QMP bullam {status} recusavit: {responsum}")


def click_ps2(
    aux: object,
    ps2: object,
    q: socket.socket,
    monitor: socket.socket,
    out: Path,
    nomen: str,
    prior: tuple[int, int],
    w: int,
    h: int,
) -> tuple[int, int]:
    """Cliccum QMP per PS/2 mittit; effectus framebuffer deinde auctoritas est."""
    qmp_bulla(ps2, q, True, 1)
    time.sleep(0.32)
    qmp_bulla(ps2, q, False, -1)
    time.sleep(0.24)
    via = out / f"click-{nomen}-post.ppm"
    aux.captura(monitor, via)
    _, _, pix = aux.ppm(via)
    positio = aux.cursor_quaere(pix, w, h)
    return positio if positio is not None else prior


def elige_tabula_effectu(
    aux: object,
    ps2: object,
    q: socket.socket,
    monitor: socket.socket,
    out: Path,
    prior: tuple[int, int],
    w: int,
    h: int,
    nox: tuple[int, int, int],
    bronzeum: tuple[int, int, int],
    ebur: tuple[int, int, int],
) -> tuple[tuple[int, int], bool]:
    """Bullam QMP tenet donec INITIUM post electionem TABULAE vere dispareat."""
    qmp_bulla(ps2, q, True, 1)

    effectus = False
    try:
        for i in range(40):
            via = out / f"tabula-xib-effectus-{i}.ppm"
            aux.captura(monitor, via)
            _, _, pix = aux.ppm(via)
            if aux.initium_top_quaere(pix, w, h, nox, bronzeum, ebur) is None:
                effectus = True
                break
            time.sleep(0.14)
    finally:
        qmp_bulla(ps2, q, False, -1)
        time.sleep(0.18)

    via = out / "tabula-xib-effectus-finalis.ppm"
    aux.captura(monitor, via)
    _, _, pix = aux.ppm(via)
    positio = aux.cursor_quaere(pix, w, h)
    return (positio if positio is not None else prior), effectus


def bronzeum_compositum(c: tuple[int, int, int]) -> bool:
    r, g, b = c
    return 150 <= r <= 215 and 105 <= g <= 180 and 55 <= b <= 135 and r > g > b


def principale() -> int:
    if len(sys.argv) != 5:
        print("USUS: proba_initium_sylviae_xib.py MONITOR QMP EXITUS MORA", file=sys.stderr)
        return 2
    aux = importa("aux_xib_initium", "proba_initium_sylviae_ii.py")
    ps2 = importa("aux_xib_ps2", "proba_fenestrale_uefi_purum.py")
    mon_via, qmp_via, out, mora = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), float(sys.argv[4])
    finis = time.time() + 12.0
    while (not mon_via.exists() or not qmp_via.exists()) and time.time() < finis:
        time.sleep(0.1)
    if not mon_via.exists() or not qmp_via.exists():
        print("DEFECIT: monitor vel QMP deest", file=sys.stderr)
        return 3

    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    monitor.settimeout(0.5)
    monitor.connect(str(mon_via))
    q = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    q.settimeout(2.0)
    q.connect(str(qmp_via))
    try:
        aux.lege_usque(monitor, b"(qemu) ", 2.0)
        salutatio = ps2.qmp_linea(q)
        if "QMP" not in salutatio:
            print("DEFECIT: salutatio QMP invalida", file=sys.stderr)
            return 3
        ps2.qmp(q, "qmp_capabilities")
        mures = ps2.qmp(q, "query-mice").get("return", [])
        candidati = [m for m in mures if "PS/2 Mouse" in str(m.get("name", ""))]
        if not candidati:
            print("DEFECIT: QEMU PS/2 Mouse deest", file=sys.stderr)
            return 3
        aux.hmp(monitor, f"mouse_set {int(candidati[0]['index'])}")
        time.sleep(mora)

        ante = out / "initium-xib-ante.ppm"
        apertum = out / "initium-xib-apertum.ppm"
        hover = out / "initium-xib-hover.ppm"
        post = out / "initium-xib-post.ppm"
        aux.captura(monitor, ante)
        w, h, pix_ante = aux.ppm(ante)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        nox = (28, 31, 32)
        bronzeum = (185, 138, 82)
        ebur = (241, 238, 228)
        bronzeum_xiie = (181, 138, 84)
        aqua_xiie = (104, 202, 210)
        ebur_xiie = (242, 244, 247)

        taskbar_top = h - 40
        init_ante = aux.pixel(pix_ante, w, 50, taskbar_top + 8)
        pos_initium = move_ad_firmus(aux, monitor, out, "initium-xib", 50, 770, w, h)
        pos_initium = click_ps2(aux, ps2, q, monitor, out, "initium-xib", pos_initium, w, h)
        aux.captura(monitor, apertum)
        _, _, pix_open = aux.ppm(apertum)

        menu_top = aux.initium_top_quaere(pix_open, w, h, nox, bronzeum, ebur)
        if menu_top is None:
            print("DEFECIT: INITIUM non apertum est", file=sys.stderr)
            return 5
        xiie = aux.pixel(pix_open, w, 20, menu_top + 2) == bronzeum_xiie

        if xiie:
            caput = aux.pixel(pix_open, w, 180, menu_top + 12)
            corpus = aux.pixel(pix_open, w, 180, menu_top + 70)
            if lumen(caput) >= 260 or lumen(corpus) <= lumen(caput) + 260:
                print(f"DEFECIT: materia graphite/ebur INITII XII-E deest: {caput}->{corpus}", file=sys.stderr)
                return 6
            if aux.pixel(pix_open, w, 20, menu_top + 2) != bronzeum_xiie:
                print("DEFECIT: limes bronzeus INITII XII-E deest", file=sys.stderr)
                return 7
            aqua_capitis = numerus_coloris(aux, pix_open, w, (8, menu_top + 8, 320, menu_top + 60), aqua_xiie)
            if aqua_capitis < 100:
                print(f"DEFECIT: lumen aqua capitis XII-E deest: {aqua_capitis}", file=sys.stderr)
                return 8
        else:
            caput_top = aux.pixel(pix_open, w, 180, menu_top + 8)
            caput_bottom = aux.pixel(pix_open, w, 180, menu_top + 54)
            if caput_top == caput_bottom or lumen(caput_top) <= lumen(caput_bottom):
                print(f"DEFECIT: materia capitis INITII historici deest: {caput_top}->{caput_bottom}", file=sys.stderr)
                return 9

        prima_y = menu_top + 92
        regiones: list[tuple[str, tuple[int, int, int, int]]] = []
        for i, nomen in enumerate(("PROGRAMMATA", "TABULA", "TERMINALE", "OFFICINA")):
            iy = prima_y + i * 54
            regiones.append((nomen, (24, iy + 6, 56, iy + 38)))

        numeri: list[int] = []
        purum_caeruleum = 0
        for nomen, regio in regiones:
            cs = colores(aux, pix_open, w, regio)
            numeri.append(len(cs))
            if len(cs) < 45:
                print(f"DEFECIT: icona INITII {nomen} non est premium: colores={len(cs)}", file=sys.stderr)
                return 10
            purum_caeruleum += numerus_coloris(aux, pix_open, w, regio, (0, 0, 255))
        if purum_caeruleum != 0:
            print(f"DEFECIT: halo caeruleus in INITIO: {purum_caeruleum}", file=sys.stderr)
            return 11
        if len(set(numeri)) < 3:
            print(f"DEFECIT: familia premium INITII non satis distincta est: {numeri}", file=sys.stderr)
            return 12

        nox_total = sum(numerus_coloris(aux, pix_open, w, regio, nox) for _, regio in regiones)
        if nox_total > 700:
            print(f"DEFECIT: quadrata obscura atlas veteris restant: nox={nox_total}", file=sys.stderr)
            return 13

        prog_scopus = prima_y + 22
        tab_scopus = prima_y + 54 + 22
        prog_ante = aux.pixel(pix_open, w, 300, prog_scopus)
        tab_ante = aux.pixel(pix_open, w, 300, tab_scopus)
        pos_tabula = move_ad_firmus(aux, monitor, out, "tabula-xib", 150, tab_scopus, w, h)
        aux.captura(monitor, hover)
        _, _, pix_hover = aux.ppm(hover)
        prog_post = aux.pixel(pix_hover, w, 300, prog_scopus)
        tab_post = aux.pixel(pix_hover, w, 300, tab_scopus)
        if tab_post == tab_ante or prog_post != prog_ante:
            print(f"DEFECIT: hover TABULAE contractum fregit: T={tab_ante}->{tab_post} P={prog_ante}->{prog_post}", file=sys.stderr)
            return 14
        x_accentus = 18 if xiie else 16
        accentus = aux.pixel(pix_hover, w, x_accentus, tab_scopus)
        if xiie:
            if not bronzeum_compositum(accentus):
                print(f"DEFECIT: linea hover TABULAE XII-E non est bronzea composita: {accentus}", file=sys.stderr)
                return 15
        elif accentus != bronzeum:
            print(f"DEFECIT: linea hover TABULAE historica deest: {accentus}", file=sys.stderr)
            return 15

        pos_tabula, effectus = elige_tabula_effectu(aux, ps2, q, monitor, out, pos_tabula, w, h, nox, bronzeum, ebur)
        if not effectus:
            print("DEFECIT: arista clicci TABULAE non consumpta est", file=sys.stderr)
            return 16

        aux.captura(monitor, post)
        _, _, pix_post = aux.ppm(post)
        if aux.initium_top_quaere(pix_post, w, h, nox, bronzeum, ebur) is not None:
            print("DEFECIT: INITIUM post electionem adhuc apertum est", file=sys.stderr)
            return 17
        if xiie:
            regio_fenestrae = (620, 120, 1240, 620)
            aes = numerus_coloris(aux, pix_post, w, regio_fenestrae, bronzeum_xiie)
            eb = numerus_coloris(aux, pix_post, w, regio_fenestrae, ebur_xiie)
            aq = numerus_coloris(aux, pix_post, w, regio_fenestrae, aqua_xiie)
            if aes < 40 or eb < 200 or aq < 10:
                print(f"DEFECIT: TABULA XII-E non apparuit/focata est: aes={aes} ebur={eb} aqua={aq}", file=sys.stderr)
                return 18
        else:
            if aux.pixel(pix_post, w, 700, 168) != bronzeum:
                print(f"DEFECIT: focus TABULAE non rediit: {aux.pixel(pix_post,w,700,168)}", file=sys.stderr)
                return 19

        init_open = aux.pixel(pix_open, w, 50, taskbar_top + 8)
        if init_open == init_ante:
            print("DEFECIT: status INITII taskbar non mutatur", file=sys.stderr)
            return 20

        testa = "XII-E" if xiie else "historica"
        print(f"INITIUM-XIB: testa={testa} top={menu_top} cursor={pos_initium}->{pos_tabula}")
        print(f"INITIUM-XIB: colores={numeri} nox={nox_total} caeruleum_purum={purum_caeruleum}")
        print("RECTE: INITIUM asseta premium recipit et hover/click/focus servantur.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()
        q.close()


if __name__ == "__main__":
    raise SystemExit(principale())
