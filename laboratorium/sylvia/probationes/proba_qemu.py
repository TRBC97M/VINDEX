#!/usr/bin/env python3
"""Probatio visualis automatica Sylviae Laboratorii per QEMU.

Capturas HMP PPM legit; motum muris per RFB/VNC directe immittit.
Status 0 redditur tantum si desktop, glyphi et motus cursoris recti sunt.
"""

from __future__ import annotations

import re
import socket
import struct
import sys
import time
from pathlib import Path


def exhaure(sock: socket.socket) -> None:
    pristinum = sock.gettimeout()
    sock.settimeout(0.03)
    try:
        while True:
            if not sock.recv(65536):
                break
    except socket.timeout:
        pass
    finally:
        sock.settimeout(pristinum)


def hmp(sock: socket.socket, command: str, timeout: float = 2.0) -> str:
    exhaure(sock)
    sock.sendall((command + "\n").encode("ascii"))
    finis = time.time() + timeout
    partes: list[bytes] = []
    while time.time() < finis:
        try:
            data = sock.recv(65536)
        except socket.timeout:
            continue
        if not data:
            break
        partes.append(data)
        textus = b"".join(partes)
        if b"(qemu)" in textus and command.encode("ascii") in textus:
            break
    return b"".join(partes).decode("utf-8", "replace")


def recipe_exacte(sock: socket.socket, n: int) -> bytes:
    data = bytearray()
    while len(data) < n:
        pars = sock.recv(n - len(data))
        if not pars:
            raise RuntimeError("VNC clausum est")
        data.extend(pars)
    return bytes(data)


def vnc_para(host: str = "127.0.0.1", port: int = 5900) -> tuple[socket.socket, int, int]:
    v = socket.create_connection((host, port), timeout=3.0)
    v.settimeout(3.0)
    versio = recipe_exacte(v, 12)
    if not versio.startswith(b"RFB "):
        raise RuntimeError(f"VNC versio invalida: {versio!r}")
    v.sendall(b"RFB 003.008\n")
    n = recipe_exacte(v, 1)[0]
    if n == 0:
        mensura = struct.unpack(">I", recipe_exacte(v, 4))[0]
        ratio = recipe_exacte(v, mensura).decode("utf-8", "replace")
        raise RuntimeError(f"VNC securitas recusata: {ratio}")
    genera = recipe_exacte(v, n)
    if 1 not in genera:
        raise RuntimeError(f"VNC sine securitate non adest: {list(genera)}")
    v.sendall(b"\x01")
    status = struct.unpack(">I", recipe_exacte(v, 4))[0]
    if status != 0:
        raise RuntimeError(f"VNC securitas status {status}")
    v.sendall(b"\x01")
    initium = recipe_exacte(v, 24)
    w, h = struct.unpack(">HH", initium[:4])
    nomen_mensura = struct.unpack(">I", initium[20:24])[0]
    if nomen_mensura:
        recipe_exacte(v, nomen_mensura)
    return v, w, h


def vnc_murus(v: socket.socket, x: int, y: int, tesserae: int = 0) -> None:
    x = max(0, min(65535, x))
    y = max(0, min(65535, y))
    v.sendall(struct.pack(">BBHH", 5, tesserae & 0xFF, x, y))


def lege_ppm(via: Path) -> tuple[int, int, bytes]:
    data = via.read_bytes()
    if not data.startswith(b"P6"):
        raise ValueError("captura non est PPM P6")
    i = 2
    tokena: list[bytes] = []
    while len(tokena) < 3:
        while i < len(data) and data[i] in b" \t\r\n":
            i += 1
        if i < len(data) and data[i] == 35:
            while i < len(data) and data[i] not in b"\r\n":
                i += 1
            continue
        initium = i
        while i < len(data) and data[i] not in b" \t\r\n":
            i += 1
        tokena.append(data[initium:i])
    w, h, maximum = map(int, tokena)
    if maximum != 255:
        raise ValueError("PPM maximum != 255")
    while i < len(data) and data[i] in b" \t\r\n":
        i += 1
    pix = data[i : i + w * h * 3]
    if len(pix) != w * h * 3:
        raise ValueError("captura PPM truncata")
    return w, h, pix


def prope(r: int, g: int, b: int, color: tuple[int, int, int], tol: int = 7) -> bool:
    return abs(r - color[0]) <= tol and abs(g - color[1]) <= tol and abs(b - color[2]) <= tol


def numera_colorem(pix: bytes, color: tuple[int, int, int], tol: int = 7) -> int:
    return sum(1 for i in range(0, len(pix), 3) if prope(pix[i], pix[i + 1], pix[i + 2], color, tol))


def numera_regionem(
    pix: bytes, w: int, h: int, x0: int, y0: int, x1: int, y1: int,
    color: tuple[int, int, int], tol: int = 7,
) -> int:
    x0, x1 = max(0, min(w, x0)), max(0, min(w, x1))
    y0, y1 = max(0, min(h, y0)), max(0, min(h, y1))
    n = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            i = (y * w + x) * 3
            if prope(pix[i], pix[i + 1], pix[i + 2], color, tol):
                n += 1
    return n


def differentiae(a: bytes, b: bytes) -> int:
    if len(a) != len(b):
        return max(len(a), len(b)) // 3
    return sum(1 for i in range(0, len(a), 3) if a[i:i+3] != b[i:i+3])


def netto_hmp(textus: str) -> str:
    textus = re.sub(r"\x1b\[[0-9;?]*[A-Za-z]", "", textus.replace("\r", ""))
    lineae = []
    for linea in textus.split("\n"):
        linea = linea.strip()
        if linea and linea != "(qemu)" and not linea.startswith("xp /8gx"):
            lineae.append(linea)
    return " | ".join(lineae)


def principale() -> int:
    if len(sys.argv) != 3:
        print("USUS: proba_qemu.py MONITOR.sock EXITUS")
        return 2
    monitor = Path(sys.argv[1])
    exitus = Path(sys.argv[2])
    ante = exitus / "sylvia-ante.ppm"
    post = exitus / "sylvia-post.ppm"
    finis = time.time() + 10.0
    while not monitor.exists() and time.time() < finis:
        time.sleep(0.1)
    if not monitor.exists():
        print("QEMU: ERRATUM monitor non apparuit")
        return 3
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.settimeout(0.35)
    s.connect(str(monitor))
    v: socket.socket | None = None
    try:
        time.sleep(0.1)
        exhaure(s)
        time.sleep(4.0)
        hmp(s, f"screendump {ante}")
        finis = time.time() + 3.0
        while not ante.exists() and time.time() < finis:
            time.sleep(0.1)
        if not ante.exists():
            print("QEMU: ERRATUM captura initialis non creata")
            return 4

        metadata_muris = netto_hmp(hmp(s, "xp /8gx 0x03000890"))
        w, h, pix_ante = lege_ppm(ante)
        ebur = numera_colorem(pix_ante, (241, 238, 228), 9)
        desktop = ebur > (w * h) // 100
        sh = h - 28
        lx = w * 21 // 100
        ly = sh * 31 // 100
        lux_tituli = numera_regionem(
            pix_ante, w, h, lx + 8, ly + 7, lx + 8 + 13 * 8, ly + 21,
            (234, 248, 255), 10,
        )
        textus = lux_tituli >= 12

        v, vw, vh = vnc_para()
        destinatio_x = max(1, min(vw - 2, vw * 3 // 4))
        destinatio_y = max(1, min(vh - 2, vh // 4))
        vnc_murus(v, destinatio_x, destinatio_y)
        time.sleep(1.0)
        hmp(s, f"screendump {post}")
        finis = time.time() + 3.0
        while not post.exists() and time.time() < finis:
            time.sleep(0.1)

        mutatio = -1
        if post.exists():
            w2, h2, pix_post = lege_ppm(post)
            if w2 == w and h2 == h:
                mutatio = differentiae(pix_ante, pix_post)
        murus = mutatio >= 20

        print(f"QEMU: RESOLUTIO {w}x{h}")
        print(f"QEMU: VNC {vw}x{vh} -> {destinatio_x},{destinatio_y}")
        print(f"QEMU: META_MURUS {metadata_muris}")
        print(f"QEMU: EBUR {ebur}")
        print(f"QEMU: GLYPHI_TITULI {lux_tituli}")
        print("QEMU: DESKTOP " + ("RECTE" if desktop else "DEFECIT"))
        print("QEMU: TEXTUS " + ("RECTE" if textus else "DEFECIT"))
        if mutatio < 0:
            print("QEMU: MURUS DEFECIT (secunda captura deest)")
        else:
            print("QEMU: MURUS " + ("RECTE" if murus else "DEFECIT") + f" ({mutatio} pixeli mutati)")
        print(f"QEMU: CAPTURA_ANTE {ante}")
        print(f"QEMU: CAPTURA_POST {post}")
        if desktop and textus and murus:
            print("QEMU: SYLVIA RECTE")
            return 0
        print("QEMU: SYLVIA DEFECIT")
        return 5
    finally:
        s.close()
        if v is not None:
            v.close()


if __name__ == "__main__":
    raise SystemExit(principale())
