#!/usr/bin/env python3
"""P16-VII: metra, identitas et emblema rasterum Sylviae sub UEFI/QEMU comprobantur."""
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
        via = out / "forma-sylviae-vii.ppm"
        captura(monitor, via)
        w, h, pix = ppm(via)
        if (w, h) != (1280, 800):
            print(f"DEFECIT: resolutio {w}x{h}", file=sys.stderr)
            return 4

        nox = (28, 31, 32)
        lapis = (49, 55, 55)
        ebur = (241, 238, 228)
        bronzeum = (185, 138, 82)

        taskbar_top = h - 40
        linea_bronzea = numerus_coloris_in_linea(pix, w, taskbar_top, bronzeum)
        linea_nocturna = numerus_coloris_in_linea(pix, w, taskbar_top + 3, nox)
        if linea_bronzea < w * 95 // 100:
            print(f"DEFECIT: limes aeneus taskbar non continuus est: bronzeum={linea_bronzea}", file=sys.stderr)
            return 5
        if linea_nocturna < w * 95 // 100:
            print(f"DEFECIT: corpus taskbar non est nox graphitica: nox={linea_nocturna}", file=sys.stderr)
            return 6

        if pixel(pix, w, 10, taskbar_top + 8) != lapis:
            print("DEFECIT: tessera INITIUM lapidea deest", file=sys.stderr)
            return 7
        tray_x = w - 126
        if pixel(pix, w, tray_x + 4, taskbar_top + 8) != lapis:
            print("DEFECIT: regio systematis dextra lapidea deest", file=sys.stderr)
            return 8

        # Hitbox bureau manet P16-III, sed tesserae iam nocturnae sunt.
        if pixel(pix, w, 20, 74) != nox:
            print(f"DEFECIT: tessera PROGRAMMATA bureau nova deest: {pixel(pix,w,20,74)}", file=sys.stderr)
            return 9
        if pixel(pix, w, 20, 178) != nox:
            print(f"DEFECIT: tessera TABULA bureau nova deest: {pixel(pix,w,20,178)}", file=sys.stderr)
            return 10

        # Marca SYLVIA 2× manet contractus typographicus, nunc eburnea.
        ebur_tituli = numerus_coloris_in_recto(pix, w, 16, 16, 150, 48, ebur)
        if ebur_tituli < 250:
            print(f"DEFECIT: marca SYLVIA 2x non videtur: ebur={ebur_tituli}", file=sys.stderr)
            return 11

        # P16-VII: emblema XXXII×XXXII est SIMG rasterum verum ad (164,18).
        # Duo pixela opaca exacta et copia colorum propria probant asset + blit,
        # non solam mutationem genericam regionis.
        gemma = (234, 255, 255)
        centrum = (75, 81, 73)
        aes_iconis = (198, 147, 73)
        if pixel(pix, w, 180, 23) != gemma:
            print(f"DEFECIT: gemma rastera SIMG deest: {pixel(pix,w,180,23)}", file=sys.stderr)
            return 12
        if pixel(pix, w, 180, 34) != centrum:
            print(f"DEFECIT: centrum emblematis SIMG deest: {pixel(pix,w,180,34)}", file=sys.stderr)
            return 13
        gemmae = numerus_coloris_in_recto(pix, w, 164, 18, 196, 50, gemma)
        aera = numerus_coloris_in_recto(pix, w, 164, 18, 196, 50, aes_iconis)
        if gemmae < 40 or aera < 40:
            print(f"DEFECIT: copia pixelorum emblematis nimis parva: gemma={gemmae} aes={aera}", file=sys.stderr)
            return 14

        colores = Counter(tuple(pix[i:i+3]) for i in range(0, len(pix)-2, 3))
        print(f"FORMA-VII: resolutio={w}x{h} taskbar=40 titulus=36")
        print(f"FORMA-VII: linea_bronzea={linea_bronzea} linea_nocturna={linea_nocturna} ebur_bureau_2x={ebur_tituli}")
        print(f"FORMA-VII: emblema_gemma={gemmae} emblema_aes={aera} colores_distincti={sum(1 for _,n in colores.items() if n>30)}")
        print("RECTE: P16-VII identitas et emblema SIMG rasterum sub UEFI vere pinguntur.")
        return 0
    finally:
        try:
            hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
