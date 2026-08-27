#!/usr/bin/env python3
"""P16-II: INITIUM apertum, hover et focus TABULA sub UEFI/QEMU comprobat."""
from __future__ import annotations

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


def differentiae(a: bytes, b: bytes) -> int:
    n = min(len(a), len(b)) // 3
    return sum(a[i*3:i*3+3] != b[i*3:i*3+3] for i in range(n))


def cursor_quaere(pix: bytes, w: int, h: int) -> tuple[int, int] | None:
    """Signaturam cursoris P16 quaerit: XIV pixeli nigri verticales + interior ebur."""
    niger = bytes((12, 20, 27))
    ebur = bytes((241, 238, 228))
    linea = w * 3
    initium = 0
    while True:
        locus = pix.find(niger, initium)
        if locus < 0:
            return None
        initium = locus + 1
        if locus % 3 != 0:
            continue
        p = locus // 3
        x, y = p % w, p // w
        if x + 10 >= w or y + 17 >= h:
            continue
        if pix[locus + (2 * linea) + 3:locus + (2 * linea) + 6] != ebur:
            continue
        recta = True
        for k in range(14):
            j = locus + k * linea
            if pix[j:j+3] != niger:
                recta = False
                break
        if recta:
            return x, y


def initium_top_quaere(pix: bytes, w: int, h: int, vitrum: tuple[int, int, int]) -> int | None:
    """Initium panni e colore capitis x=20 invenit, capacitate catalogi neglecta."""
    prior_non = True
    for y in range(120, h - 40):
        est = pixel(pix, w, 20, y) == vitrum
        if est and prior_non:
            # Caput INITIUM saltem XL px verticales servat.
            if y + 40 < h and pixel(pix, w, 20, y + 30) == vitrum:
                return y
        prior_non = not est
    return None


def limita(v: int, minimum: int, maximum: int) -> int:
    if v < minimum:
        return minimum
    if v > maximum:
        return maximum
    return v


def move_ad(
    monitor: socket.socket,
    out: Path,
    nomen: str,
    target_x: int,
    target_y: int,
    w: int,
    h: int,
) -> tuple[int, int]:
    """Cursor ad scopum per fasciculos PS/2 parvos ducit et framebuffer ipsum metitur."""
    signum_x = 1
    signum_y = 1
    prior: tuple[int, int] | None = None
    mandatum_prior: tuple[int, int] | None = None
    for gradus in range(18):
        via = out / f"cursor-{nomen}-{gradus}.ppm"
        captura(monitor, via)
        _, _, pix = ppm(via)
        positio = cursor_quaere(pix, w, h)
        if positio is None:
            raise RuntimeError(f"cursor non inventus in gradu {nomen}/{gradus}")
        x, y = positio
        if abs(target_x - x) <= 3 and abs(target_y - y) <= 3:
            return positio

        if prior is not None and mandatum_prior is not None:
            px, py = prior
            mdx, mdy = mandatum_prior
            if mdx != 0 and abs(target_x - x) > abs(target_x - px) + 3:
                signum_x = 0 - signum_x
            if mdy != 0 and abs(target_y - y) > abs(target_y - py) + 3:
                signum_y = 0 - signum_y

        dx = limita((target_x - x) * signum_x, -90, 90)
        dy = limita((target_y - y) * signum_y, -90, 90)
        if abs(target_x - x) <= 3:
            dx = 0
        if abs(target_y - y) <= 3:
            dy = 0
        prior = positio
        mandatum_prior = (dx, dy)
        hmp(monitor, f"mouse_move {dx} {dy}")
        time.sleep(0.25)

    via = out / f"cursor-{nomen}-finis.ppm"
    captura(monitor, via)
    _, _, pix = ppm(via)
    positio = cursor_quaere(pix, w, h)
    raise RuntimeError(f"cursor scopum {target_x},{target_y} non attigit; ultimus={positio}")


def click(monitor: socket.socket) -> None:
    r1 = hmp(monitor, "mouse_button 1")
    time.sleep(0.12)
    r2 = hmp(monitor, "mouse_button 0")
    if "unknown command" in (r1 + r2).lower():
        raise RuntimeError("HMP mouse_button deest")
    time.sleep(0.8)


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

        vitrum = (14, 66, 111)
        ebur = (241, 238, 228)
        lux = (234, 248, 255)
        argentum = (185, 196, 207)
        bronzeum = (185, 138, 82)
        profundum = (8, 35, 61)
        menu_top = initium_top_quaere(pix_open, w, h, vitrum)
        if menu_top is None:
            print("DEFECIT: caput INITIUM non inventum", file=sys.stderr)
            return 7
        programmata_y = menu_top + 92
        tabula_y = programmata_y + 54
        programmata_scopus = programmata_y + 22
        tabula_scopus = tabula_y + 22

        if pixel(pix_open, w, 20, menu_top + 10) != vitrum:
            print(f"DEFECIT: caput INITIUM non apertum: {pixel(pix_open,w,20,menu_top+10)} cursor={pos_initium}", file=sys.stderr)
            return 8
        if pixel(pix_open, w, 300, menu_top + 70) != ebur:
            print(f"DEFECIT: corpus INITIUM deest: {pixel(pix_open,w,300,menu_top+70)}", file=sys.stderr)
            return 9
        if pixel(pix_open, w, 300, programmata_scopus) != lux or pixel(pix_open, w, 300, tabula_scopus) != lux:
            print("DEFECIT: tesserae applicationum INITIUM desunt", file=sys.stderr)
            return 10
        mutata_open = differentiae(pix_ante, pix_open)
        if mutata_open < 12000:
            print(f"DEFECIT: pannus INITIUM nimis parum mutavit: {mutata_open}", file=sys.stderr)
            return 11

        pos_tabula = move_ad(monitor, out, "tabula", 150, tabula_scopus, w, h)
        captura(monitor, hover)
        _, _, pix_hover = ppm(hover)
        if pixel(pix_hover, w, 300, tabula_scopus) != argentum:
            print(f"DEFECIT: hover TABULA non detectus: {pixel(pix_hover,w,300,tabula_scopus)} cursor={pos_tabula}", file=sys.stderr)
            return 12
        if pixel(pix_hover, w, 300, programmata_scopus) != lux:
            print("DEFECIT: hover TABULA tesseram PROGRAMMATA mutavit", file=sys.stderr)
            return 13

        click(monitor)
        captura(monitor, post)
        _, _, pix_post = ppm(post)
        if pixel(pix_post, w, 20, menu_top + 10) == vitrum:
            print("DEFECIT: INITIUM post electionem non clausum est", file=sys.stderr)
            return 14

        # TABULA initialiter x≈679 y=168. Post electionem debet focus et marginem bronzeum accipere.
        focus_pixel = pixel(pix_post, w, 700, 168)
        if focus_pixel != bronzeum:
            print(f"DEFECIT: TABULA focus non accepit: {focus_pixel}", file=sys.stderr)
            return 15

        if pixel(pix_open, w, 24, programmata_y + 12) != profundum:
            print("DEFECIT: signum PROGRAMMATA in INITIUM deest", file=sys.stderr)
            return 16

        mutata_post = differentiae(pix_open, pix_post)
        print(f"INITIUM: top={menu_top} cursor_init={init_pos} cursor_tessera={pos_initium} cursor_tabula={pos_tabula}")
        print(f"INITIUM: apertio_pixeli={mutata_open} clausura_focus_pixeli={mutata_post}")
        print(f"INITIUM: caput={pixel(pix_open,w,20,menu_top+10)} hover_tabula={pixel(pix_hover,w,300,tabula_scopus)} focus_tabula={focus_pixel}")
        print("RECTE: P16-II INITIUM capacitatem dynamicam tolerat et TABULA vere focalizat.")
        return 0
    finally:
        try:
            hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
