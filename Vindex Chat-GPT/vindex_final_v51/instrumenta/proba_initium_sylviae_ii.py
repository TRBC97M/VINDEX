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

        # Cursor initio (640,400). Saturatio ad angulum inferiorem sinistrum,
        # deinde centrum tesserae INITIUM circa (50,780).
        hmp(monitor, "mouse_move -2000 2000")
        time.sleep(0.4)
        hmp(monitor, "mouse_move 50 -20")
        time.sleep(0.5)
        click(monitor)
        captura(monitor, apertum)
        w2, h2, pix_open = ppm(apertum)
        if (w2, h2) != (w, h):
            print("DEFECIT: dimensiones post INITIUM mutantur", file=sys.stderr)
            return 5

        vitrum = (14, 66, 111)
        ebur = (241, 238, 228)
        lux = (234, 248, 255)
        argentum = (185, 196, 207)
        bronzeum = (185, 138, 82)
        profundum = (8, 35, 61)

        # Menu: x=6, y=500, w=320, h=260.
        if pixel(pix_open, w, 20, 510) != vitrum:
            print(f"DEFECIT: caput INITIUM non apertum: {pixel(pix_open,w,20,510)}", file=sys.stderr)
            return 6
        if pixel(pix_open, w, 300, 570) != ebur:
            print(f"DEFECIT: corpus INITIUM deest: {pixel(pix_open,w,300,570)}", file=sys.stderr)
            return 7
        if pixel(pix_open, w, 300, 600) != lux or pixel(pix_open, w, 300, 650) != lux:
            print("DEFECIT: tesserae applicationum INITIUM desunt", file=sys.stderr)
            return 8
        mutata_open = differentiae(pix_ante, pix_open)
        if mutata_open < 12000:
            print(f"DEFECIT: pannus INITIUM nimis parum mutavit: {mutata_open}", file=sys.stderr)
            return 9

        # Ex tessera INITIUM (50,780) ad secundam applicationem TABULA circa (150,650).
        hmp(monitor, "mouse_move 100 -130")
        time.sleep(0.8)
        captura(monitor, hover)
        _, _, pix_hover = ppm(hover)
        if pixel(pix_hover, w, 300, 650) != argentum:
            print(f"DEFECIT: hover TABULA non detectus: {pixel(pix_hover,w,300,650)}", file=sys.stderr)
            return 10
        if pixel(pix_hover, w, 300, 600) != lux:
            print("DEFECIT: hover TABULA tesseram PROGRAMMATA mutavit", file=sys.stderr)
            return 11

        click(monitor)
        captura(monitor, post)
        _, _, pix_post = ppm(post)
        if pixel(pix_post, w, 20, 510) == vitrum:
            print("DEFECIT: INITIUM post electionem non clausum est", file=sys.stderr)
            return 12

        # TABULA initialiter x≈679 y=168. Post electionem debet focus et marginem bronzeum accipere.
        focus_pixel = pixel(pix_post, w, 700, 168)
        if focus_pixel != bronzeum:
            print(f"DEFECIT: TABULA focus non accepit: {focus_pixel}", file=sys.stderr)
            return 13

        # Iconographia minima menu quoque color profundum continet.
        if pixel(pix_open, w, 24, 604) != profundum:
            print("DEFECIT: signum PROGRAMMATA in INITIUM deest", file=sys.stderr)
            return 14

        mutata_post = differentiae(pix_open, pix_post)
        print(f"INITIUM: apertio_pixeli={mutata_open} clausura_focus_pixeli={mutata_post}")
        print(f"INITIUM: caput={pixel(pix_open,w,20,510)} hover_tabula={pixel(pix_hover,w,300,650)} focus_tabula={focus_pixel}")
        print("RECTE: P16-II INITIUM aperitur, hover respondet et TABULA vere focalizat.")
        return 0
    finally:
        try:
            hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
