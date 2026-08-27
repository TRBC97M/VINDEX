#!/usr/bin/env python3
"""P16-I: metra visualia Sylviae sub UEFI/QEMU per screendump comprobat."""
from __future__ import annotations

import socket
import sys
import time
from collections import Counter
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


def numerus_coloris_in_linea(pix: bytes, w: int, y: int, color: tuple[int, int, int]) -> int:
    return sum(pixel(pix, w, x, y) == color for x in range(w))


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


def principale() -> int:
    if len(sys.argv) != 5:
        print("USUS: proba_formam_sylviae_i.py MONITOR QMP EXITUS MORA", file=sys.stderr)
        return 2

    mon_via, _qmp_via, out, mora = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), float(sys.argv[4])
    finis = time.time() + 12.0
    while not mon_via.exists() and time.time() < finis:
        time.sleep(0.1)
    if not mon_via.exists():
        print("DEFECIT: monitor deest", file=sys.stderr)
        return 3

    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    monitor.settimeout(0.4)
    monitor.connect(str(mon_via))
    try:
        lege_usque(monitor, b"(qemu) ", 2.0)
        time.sleep(mora)
        via = out / "forma-sylviae-i.ppm"
        captura(monitor, via)
        w, h, pix = ppm(via)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        aqua = (98, 215, 242)
        profundum = (8, 35, 61)
        vitrum = (14, 66, 111)
        ebur = (241, 238, 228)
        lux = (234, 248, 255)

        taskbar_top = h - 40
        linea_aqua = numerus_coloris_in_linea(pix, w, taskbar_top, aqua)
        linea_profunda = numerus_coloris_in_linea(pix, w, taskbar_top + 3, profundum)
        if linea_aqua < w * 95 // 100:
            print(f"DEFECIT: limes superior taskbar non est XL px: aqua={linea_aqua}", file=sys.stderr)
            return 5
        if linea_profunda < w * 95 // 100:
            print(f"DEFECIT: corpus taskbar non est profundum: prof={linea_profunda}", file=sys.stderr)
            return 6

        if pixel(pix, w, 8, taskbar_top + 8) != vitrum:
            print("DEFECIT: tessera INITIUM nova deest", file=sys.stderr)
            return 7
        tray_x = w - 126
        if pixel(pix, w, tray_x + 2, taskbar_top + 8) != vitrum:
            print("DEFECIT: regio systematis dextra deest", file=sys.stderr)
            return 8

        # Fenestra PROGRAMMATA initialiter focus habet: x≈76, y≈56.
        # Ad x=300 titulus novus usque ad y+35 manet; corpus incipit ad y+36.
        if pixel(pix, w, 300, 88) != vitrum:
            print(f"DEFECIT: titulus fenestrae XXXVI px non detectus: {pixel(pix,w,300,88)}", file=sys.stderr)
            return 9
        if pixel(pix, w, 300, 96) != ebur:
            print(f"DEFECIT: regio sub titulo non detecta: {pixel(pix,w,300,96)}", file=sys.stderr)
            return 10

        # Titulus 2× debet multo plures pixeles lucidos quam vetus 8×8 simplex.
        lux_tituli = numerus_coloris_in_recto(pix, w, 86, 62, 260, 92, lux)
        if lux_tituli < 300:
            print(f"DEFECIT: titulus 2x non videtur: lux={lux_tituli}", file=sys.stderr)
            return 11

        colores = Counter(tuple(pix[i:i+3]) for i in range(0, len(pix)-2, 3))
        print(f"FORMA: resolutio={w}x{h} taskbar=40 titulus=36")
        print(f"FORMA: linea_aqua={linea_aqua} linea_profunda={linea_profunda} lux_tituli={lux_tituli}")
        print(f"FORMA: colores_distincti={sum(1 for _,n in colores.items() if n>30)}")
        print("RECTE: P16-I metra visualia Sylviae sub UEFI vere pinguntur.")
        return 0
    finally:
        try:
            hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
