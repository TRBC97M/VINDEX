#!/usr/bin/env python3
"""Probatio visualis automatica Sylviae Laboratorii per QEMU.

Capturas HMP PPM legit; tabulam absolutam eligit; motum muris per QMP
input-send-event immittit. Status 0 redditur tantum si desktop, glyphi et
motus cursoris recti sunt.
"""

from __future__ import annotations

import json
import re
import socket
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


def qmp_linea(sock: socket.socket, timeout: float = 2.0) -> dict:
    sock.settimeout(timeout)
    data = bytearray()
    while True:
        b = sock.recv(1)
        if not b:
            raise RuntimeError("QMP clausum est")
        if b == b"\n":
            if data.strip():
                return json.loads(data.decode("utf-8"))
            continue
        data.extend(b)


def qmp_exsequere(sock: socket.socket, nomen: str, argumenta: dict | None = None) -> dict:
    petitio: dict = {"execute": nomen}
    if argumenta is not None:
        petitio["arguments"] = argumenta
    sock.sendall((json.dumps(petitio, separators=(",", ":")) + "\r\n").encode("utf-8"))
    finis = time.time() + 3.0
    while time.time() < finis:
        responsum = qmp_linea(sock, max(0.1, finis - time.time()))
        if "return" in responsum or "error" in responsum:
            return responsum
    raise RuntimeError("QMP responsum deest")


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
    if len(sys.argv) != 4:
        print("USUS: proba_qemu.py MONITOR.sock QMP.sock EXITUS")
        return 2

    monitor = Path(sys.argv[1])
    qmp_via = Path(sys.argv[2])
    exitus = Path(sys.argv[3])
    ante = exitus / "sylvia-ante.ppm"
    post = exitus / "sylvia-post.ppm"

    finis = time.time() + 10.0
    while (not monitor.exists() or not qmp_via.exists()) and time.time() < finis:
        time.sleep(0.1)
    if not monitor.exists() or not qmp_via.exists():
        print("QEMU: ERRATUM monitor vel QMP non apparuit")
        return 3

    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.settimeout(0.35)
    s.connect(str(monitor))
    q = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    q.connect(str(qmp_via))
    try:
        time.sleep(0.1)
        exhaure(s)

        salutatio = qmp_linea(q)
        if "QMP" not in salutatio:
            raise RuntimeError("salutatio QMP invalida")
        cap = qmp_exsequere(q, "qmp_capabilities")
        if "error" in cap:
            raise RuntimeError(f"QMP capabilities: {cap}")

        mures_ante = qmp_exsequere(q, "query-mice")
        lista_murum = mures_ante.get("return", [])
        absoluti = [m for m in lista_murum if m.get("absolute")]
        if not absoluti:
            print("QEMU: MURUS DEFECIT (instrumentum absolutum deest)")
            print("QEMU: QMP_MURES " + json.dumps(mures_ante, ensure_ascii=False, separators=(",", ":")))
            return 5
        index_absolutus = int(absoluti[0]["index"])
        selectio = netto_hmp(hmp(s, f"mouse_set {index_absolutus}"))
        time.sleep(0.2)
        mures_post_selectio = qmp_exsequere(q, "query-mice")
        tabula_currens = any(
            int(m.get("index", -1)) == index_absolutus and bool(m.get("current"))
            for m in mures_post_selectio.get("return", [])
        )

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

        motus = qmp_exsequere(q, "input-send-event", {
            "events": [
                {"type": "abs", "data": {"axis": "x", "value": 24576}},
                {"type": "abs", "data": {"axis": "y", "value": 8192}},
            ]
        })
        qmp_ok = "return" in motus and "error" not in motus
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
        murus = tabula_currens and qmp_ok and mutatio >= 20

        print(f"QEMU: RESOLUTIO {w}x{h}")
        print("QEMU: QMP_MURES_ANTE " + json.dumps(mures_ante, ensure_ascii=False, separators=(",", ":")))
        print(f"QEMU: QMP_SELECTIO index={index_absolutus} {selectio}")
        print("QEMU: QMP_MURES_POST " + json.dumps(mures_post_selectio, ensure_ascii=False, separators=(",", ":")))
        print("QEMU: TABULA_CURRENS " + ("RECTE" if tabula_currens else "DEFECIT"))
        print("QEMU: QMP_MOTUS " + ("RECTE" if qmp_ok else "DEFECIT"))
        print(f"QEMU: META_MURUS {metadata_muris}")
        print(f"QEMU: EBUR {ebur}")
        print(f"QEMU: GLYPHI_TITULI {lux_tituli}")
        print("QEMU: DESKTOP " + ("RECTE" if desktop else "DEFECIT"))
        print("QEMU: TEXTUS " + ("RECTE" if textus else "DEFECIT"))
        if not tabula_currens:
            print("QEMU: MURUS DEFECIT (tabula absoluta non est receptora)")
        elif not qmp_ok:
            print("QEMU: MURUS DEFECIT (QMP input-send-event recusatum)")
            print("QEMU: QMP " + json.dumps(motus, ensure_ascii=False, separators=(",", ":")))
        elif mutatio < 0:
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
        q.close()


if __name__ == "__main__":
    raise SystemExit(principale())
