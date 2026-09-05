#!/usr/bin/env python3
"""INITIUM Sylviae sub UEFI/QEMU comprobatur; testa historica et XII-E servantur."""
from __future__ import annotations

import re
import socket
import sys
import time
from pathlib import Path


def lege_usque(sock: socket.socket, signum: bytes, mora: float = 3.0) -> bytes:
    finis = time.time() + mora
    data = bytearray()
    while signum not in data and time.time() < finis:
        try:
            pars = sock.recv(65536)
        except socket.timeout:
            continue
        if not pars:
            break
        data.extend(pars)
    return bytes(data)


def hmp(sock: socket.socket, mandatum: str) -> str:
    sock.sendall((mandatum + "\n").encode())
    return lege_usque(sock, b"(qemu) ", 4.0).decode(errors="replace")


def captura(monitor: socket.socket, via: Path) -> None:
    if via.exists():
        via.unlink()
    hmp(monitor, f"screendump {via}")
    finis = time.time() + 5.0
    while not via.exists() and time.time() < finis:
        time.sleep(0.1)
    if not via.exists():
        raise RuntimeError(f"captura deest: {via}")


def ppm(via: Path) -> tuple[int, int, bytes]:
    partes = via.read_bytes().split(b"\n", 3)
    if len(partes) != 4 or partes[0] != b"P6":
        raise RuntimeError("PPM invalidum")
    w, h = map(int, partes[1].split())
    return w, h, partes[3]


def pixel(pix: bytes, w: int, x: int, y: int) -> tuple[int, int, int]:
    i = (y * w + x) * 3
    return tuple(pix[i:i+3])  # type: ignore[return-value]


def numerus_coloris_in_recto(
    pix: bytes,
    w: int,
    x0: int,
    y0: int,
    x1: int,
    y1: int,
    color: tuple[int, int, int],
) -> int:
    n = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            if pixel(pix, w, x, y) == color:
                n += 1
    return n


def colores_in_recto(
    pix: bytes,
    w: int,
    x0: int,
    y0: int,
    x1: int,
    y1: int,
) -> set[tuple[int, int, int]]:
    out: set[tuple[int, int, int]] = set()
    for y in range(y0, y1):
        for x in range(x0, x1):
            out.add(pixel(pix, w, x, y))
    return out


def differentiae(a: bytes, b: bytes) -> int:
    n = min(len(a), len(b)) // 3
    return sum(a[i*3:i*3+3] != b[i*3:i*3+3] for i in range(n))


def cursor_quaere(pix: bytes, w: int, h: int) -> tuple[int, int] | None:
    """Cursorem historicum aut cursorem GX XII-E in framebuffer reperit."""
    linea = w * 3

    niger = bytes((12, 20, 27))
    ebur_vetus = bytes((241, 238, 228))
    initium = 0
    while True:
        locus = pix.find(niger, initium)
        if locus < 0:
            break
        initium = locus + 1
        if locus % 3 != 0:
            continue
        p = locus // 3
        x, y = p % w, p // w
        if x + 10 >= w or y + 17 >= h:
            continue
        if pix[locus + (2 * linea) + 3:locus + (2 * linea) + 6] != ebur_vetus:
            continue
        recta = True
        for k in range(14):
            j = locus + k * linea
            if pix[j:j+3] != niger:
                recta = False
                break
        if recta:
            return x, y

    ebur_xiie = bytes((242, 244, 247))
    initium = 0
    while True:
        locus = pix.find(ebur_xiie, initium)
        if locus < 0:
            return None
        initium = locus + 1
        if locus % 3 != 0:
            continue
        p = locus // 3
        columna, y = p % w, p // w
        x = columna - 1
        if x < 0 or x + 15 >= w or y + 25 >= h:
            continue
        recta = True
        for k in range(18):
            j = ((y + k) * w + columna) * 3
            if pix[j:j+3] != ebur_xiie:
                recta = False
                break
        if not recta:
            continue
        if pixel(pix, w, x + 7, y + 16) != (242, 244, 247):
            continue
        if pixel(pix, w, x + 10, y + 23) != (242, 244, 247):
            continue
        if pixel(pix, w, x + 15, y + 25) != (242, 244, 247):
            continue
        return x, y


def initium_top_quaere(
    pix: bytes,
    w: int,
    h: int,
    caput: tuple[int, int, int],
    accentus: tuple[int, int, int],
    corpus: tuple[int, int, int],
) -> int | None:
    """INITIUM historicum aut pannum GX XII-E reperit."""
    bronzeum_xiie = (181, 138, 84)
    for y in range(120, h - 120):
        if pixel(pix, w, 20, y) == accentus:
            if y + 70 < h and pixel(pix, w, 20, y + 4) == caput and pixel(pix, w, 300, y + 4) == caput and pixel(pix, w, 300, y + 70) == corpus:
                return y
        if y + 4 < h and pixel(pix, w, 20, y + 2) == bronzeum_xiie and pixel(pix, w, 300, y + 2) == bronzeum_xiie:
            return y
    return None


def limita(v: int, minimum: int, maximum: int) -> int:
    if v < minimum:
        return minimum
    if v > maximum:
        return maximum
    return v


def cursor_ex_captura_stabili(
    monitor: socket.socket,
    out: Path,
    nomen: str,
    gradus: int,
    w: int,
    h: int,
) -> tuple[int, int] | None:
    """Screendump potest incidere dum damage in GOP transfertur; status stabilis exigitur."""
    for tentamen in range(3):
        suffixum = "" if tentamen == 0 else f"-stabilis-{tentamen}"
        via = out / f"cursor-{nomen}-{gradus}{suffixum}.ppm"
        captura(monitor, via)
        _, _, pix = ppm(via)
        positio = cursor_quaere(pix, w, h)
        if positio is not None:
            return positio
        time.sleep(0.18)
    return None


def cursor_post_motum(
    monitor: socket.socket,
    out: Path,
    nomen: str,
    gradus: int,
    w: int,
    h: int,
    prior: tuple[int, int],
) -> tuple[int, int]:
    """Unum eventum mittit; aliud numquam mittitur ante effectum framebuffer."""
    for tentamen in range(40):
        via = out / f"cursor-{nomen}-{gradus}-post-{tentamen}.ppm"
        captura(monitor, via)
        _, _, pix = ppm(via)
        positio = cursor_quaere(pix, w, h)
        if positio is not None and positio != prior:
            return positio
        time.sleep(0.14)
    raise RuntimeError(f"motus muris non consumptus in gradu {nomen}/{gradus}; prior={prior}")


def move_ad(
    monitor: socket.socket,
    out: Path,
    nomen: str,
    target_x: int,
    target_y: int,
    w: int,
    h: int,
) -> tuple[int, int]:
    """Cursor ad scopum per eventus singulos ducit; framebuffer ipsum auctoritas est."""
    signum_x = 1
    signum_y = 1
    positio = cursor_ex_captura_stabili(monitor, out, nomen, 0, w, h)
    if positio is None:
        raise RuntimeError(f"cursor stabilis initialis non inventus: {nomen}")

    for gradus in range(48):
        x, y = positio
        if abs(target_x - x) <= 3 and abs(target_y - y) <= 3:
            return positio

        dx = limita((target_x - x) * signum_x, -72, 72)
        dy = limita((target_y - y) * signum_y, -72, 72)
        if abs(target_x - x) <= 3:
            dx = 0
        if abs(target_y - y) <= 3:
            dy = 0

        # Le bord ne doit jamais recevoir un mouvement vers l'extérieur.
        if x <= 2 and dx < 0:
            signum_x = 0 - signum_x
            dx = limita((target_x - x) * signum_x, -72, 72)
        if x >= w - 2 and dx > 0:
            signum_x = 0 - signum_x
            dx = limita((target_x - x) * signum_x, -72, 72)
        if y <= 2 and dy < 0:
            signum_y = 0 - signum_y
            dy = limita((target_y - y) * signum_y, -72, 72)
        if y >= h - 2 and dy > 0:
            signum_y = 0 - signum_y
            dy = limita((target_y - y) * signum_y, -72, 72)

        hmp(monitor, f"mouse_move {dx} {dy}")
        sequens = cursor_post_motum(monitor, out, nomen, gradus, w, h, positio)
        nx, ny = sequens

        if dx != 0 and abs(target_x - nx) > abs(target_x - x) + 3:
            signum_x = 0 - signum_x
        if dy != 0 and abs(target_y - ny) > abs(target_y - y) + 3:
            signum_y = 0 - signum_y
        positio = sequens

    via = out / f"cursor-{nomen}-finis.ppm"
    captura(monitor, via)
    _, _, pix = ppm(via)
    ultimus = cursor_quaere(pix, w, h)
    raise RuntimeError(f"cursor scopum {target_x},{target_y} non attigit; ultimus={ultimus or positio}")


def ps2_bullae(monitor: socket.socket) -> int | None:
    """Statum bullarum quem guest PS/2 iam consumpsit e telemetria rectoris legit."""
    textus = hmp(monitor, "xp /1gx 0x03018858")
    for linea in textus.splitlines():
        if ":" not in linea:
            continue
        valores = re.findall(r"0x[0-9a-fA-F]+", linea.split(":", 1)[1])
        if valores:
            return int(valores[0], 16)
    return None


def bullam_exspecta(monitor: socket.socket, pressa: bool) -> None:
    finis = time.time() + 6.0
    while time.time() < finis:
        status = ps2_bullae(monitor)
        if status is not None and bool(status & 1) == pressa:
            return
        time.sleep(0.08)
    status = ps2_bullae(monitor)
    nomen = "pressam" if pressa else "relaxatam"
    raise RuntimeError(f"bulla sinistra PS2 non est {nomen}; status={status}")


def click(monitor: socket.socket) -> None:
    r1 = hmp(monitor, "mouse_button 1")
    if "unknown command" in r1.lower():
        raise RuntimeError("HMP mouse_button deest")
    bullam_exspecta(monitor, True)
    r2 = hmp(monitor, "mouse_button 0")
    if "unknown command" in r2.lower():
        raise RuntimeError("HMP mouse_button deest")
    bullam_exspecta(monitor, False)


def principale() -> int:
    if len(sys.argv) != 5:
        print("USUS: proba_initium_sylviae_ii.py MONITOR QMP EXITUS MORA", file=sys.stderr)
        return 2

    mon_via, _qmp_via, out, mora = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), float(sys.argv[4])
    finis = time.time() + 12.0
    while not mon_via.exists() and time.time() < finis:
        time.sleep(0.1)
    if not mon_via.exists():
        print("DEFECIT: monitor deest", file=sys.stderr)
        return 3

    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    monitor.settimeout(0.5)
    monitor.connect(str(mon_via))
    try:
        lege_usque(monitor, b"(qemu) ", 2.0)
        time.sleep(mora)

        ante = out / "initium-ante.ppm"
        apertum = out / "initium-apertum.ppm"
        hover = out / "initium-hover.ppm"
        post = out / "initium-post.ppm"
        captura(monitor, ante)
        w, h, pix_ante = ppm(ante)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4
        init_pos = cursor_quaere(pix_ante, w, h)
        if init_pos is None:
            print("DEFECIT: cursor initialis non inventus", file=sys.stderr)
            return 5

        pos_initium = move_ad(monitor, out, "initium", 50, 770, w, h)
        click(monitor)
        captura(monitor, apertum)
        w2, h2, pix_open = ppm(apertum)
        if (w2, h2) != (w, h):
            print("DEFECIT: dimensiones post INITIUM mutantur", file=sys.stderr)
            return 6

        nox = (28, 31, 32)
        bronzeum = (185, 138, 82)
        ebur = (241, 238, 228)
        papyrus = (215, 205, 185)
        bronzeum_xiie = (181, 138, 84)
        ebur_xiie = (242, 244, 247)
        menu_top = initium_top_quaere(pix_open, w, h, nox, bronzeum, ebur)
        if menu_top is None:
            print("DEFECIT: INITIUM non apertum est", file=sys.stderr)
            return 7
        xiie = pixel(pix_open, w, 20, menu_top + 2) == bronzeum_xiie
        programmata_y = menu_top + 92
        tabula_y = programmata_y + 54
        programmata_scopus = programmata_y + 22
        tabula_scopus = tabula_y + 22

        mutata_open = differentiae(pix_ante, pix_open)
        if mutata_open < 12000:
            print(f"DEFECIT: pannus INITIUM nimis parum mutavit: {mutata_open}", file=sys.stderr)
            return 8

        if not xiie:
            if pixel(pix_open, w, 20, menu_top + 10) != nox or pixel(pix_open, w, 300, menu_top + 70) != ebur:
                print("DEFECIT: materia INITII historici fracta est", file=sys.stderr)
                return 9
            lumen_programmatum = (236, 194, 113)
            cyan_programmatum = (90, 208, 209)
            clarum_tabulae = (232, 232, 217)
            aqua_tabulae = (145, 194, 191)
            prog_lumen = numerus_coloris_in_recto(pix_open, w, 24, programmata_y + 6, 56, programmata_y + 38, lumen_programmatum)
            prog_cyan = numerus_coloris_in_recto(pix_open, w, 24, programmata_y + 6, 56, programmata_y + 38, cyan_programmatum)
            tab_clarum = numerus_coloris_in_recto(pix_open, w, 24, tabula_y + 6, 56, tabula_y + 38, clarum_tabulae)
            tab_aqua = numerus_coloris_in_recto(pix_open, w, 24, tabula_y + 6, 56, tabula_y + 38, aqua_tabulae)
            if prog_lumen < 40 or prog_cyan < 4 or tab_clarum < 100 or tab_aqua < 40:
                print("DEFECIT: iconae rasterae historicae INITII desunt", file=sys.stderr)
                return 10
        else:
            prog_colores = colores_in_recto(pix_open, w, 14, programmata_y + 4, 62, programmata_y + 42)
            tab_colores = colores_in_recto(pix_open, w, 14, tabula_y + 4, 62, tabula_y + 42)
            if len(prog_colores) < 45 or len(tab_colores) < 45:
                print(f"DEFECIT: iconae XII-E INITII non satis divites sunt: {len(prog_colores)}/{len(tab_colores)}", file=sys.stderr)
                return 11
            if (0, 0, 255) in prog_colores or (0, 0, 255) in tab_colores:
                print("DEFECIT: halo caeruleus in INITIO XII-E apparuit", file=sys.stderr)
                return 12

        pos_tabula = move_ad(monitor, out, "tabula", 150, tabula_scopus, w, h)
        captura(monitor, hover)
        _, _, pix_hover = ppm(hover)
        prog_ante = pixel(pix_open, w, 300, programmata_scopus)
        tab_ante = pixel(pix_open, w, 300, tabula_scopus)
        prog_post = pixel(pix_hover, w, 300, programmata_scopus)
        tab_post = pixel(pix_hover, w, 300, tabula_scopus)
        if xiie:
            if tab_post == tab_ante or prog_post != prog_ante:
                print(f"DEFECIT: hover TABULAE XII-E contractum fregit: T={tab_ante}->{tab_post} P={prog_ante}->{prog_post}", file=sys.stderr)
                return 13
        else:
            if tab_post != papyrus or prog_post != ebur:
                print("DEFECIT: hover TABULAE historicus contractum fregit", file=sys.stderr)
                return 14

        click(monitor)
        captura(monitor, post)
        _, _, pix_post = ppm(post)
        menu_post = initium_top_quaere(pix_post, w, h, nox, bronzeum, ebur)
        if menu_post is not None:
            print(f"DEFECIT: INITIUM post electionem adhuc repertum est ad y={menu_post}", file=sys.stderr)
            return 15
        mutata_post = differentiae(pix_open, pix_post)
        if mutata_post < 18000:
            print(f"DEFECIT: electio TABULAE nimis parum framebuffer mutavit: {mutata_post}", file=sys.stderr)
            return 16
        if xiie:
            aeneum = numerus_coloris_in_recto(pix_post, w, 620, 120, 1240, 620, bronzeum_xiie)
            ebur_num = numerus_coloris_in_recto(pix_post, w, 620, 120, 1240, 620, ebur_xiie)
            if aeneum < 40 or ebur_num < 200:
                print(f"DEFECIT: fenestra TABULAE XII-E post electionem non convincit: aes={aeneum} ebur={ebur_num}", file=sys.stderr)
                return 17
        else:
            focus_pixel = pixel(pix_post, w, 700, 168)
            if focus_pixel != bronzeum:
                print(f"DEFECIT: TABULA focus non accepit: {focus_pixel}", file=sys.stderr)
                return 18

        modus = "XII-E" if xiie else "historicus"
        print(f"INITIUM: testa={modus} top={menu_top} cursor={init_pos}->{pos_initium}->{pos_tabula}")
        print(f"INITIUM: apertio_pixeli={mutata_open} electio_pixeli={mutata_post}")
        print("RECTE: INITIUM aperitur, hover servatur et TABULA vere eligitur.")
        return 0
    finally:
        try:
            hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())