#!/usr/bin/env python3
"""Murem PS/2 Sylviae per QEMU/QMP et framebuffer probat."""

from __future__ import annotations

import json
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


def qmp_linea(sock: socket.socket) -> dict:
    data = bytearray()
    while b"\n" not in data:
        pars = sock.recv(65536)
        if not pars:
            raise RuntimeError("QMP clausum est")
        data.extend(pars)
    linea, _, residuum = data.partition(b"\n")
    # QMP huic probationi responsa singulis lineis mittit; residuum hic non opus est.
    return json.loads(linea.decode())


def qmp(sock: socket.socket, mandatum: str, argumenta: dict | None = None) -> dict:
    petitio = {"execute": mandatum}
    if argumenta is not None:
        petitio["arguments"] = argumenta
    sock.sendall((json.dumps(petitio, separators=(",", ":")) + "\n").encode())
    while True:
        responsum = qmp_linea(sock)
        if "event" in responsum:
            continue
        return responsum


def lege_ppm(via: Path) -> tuple[int, int, bytes]:
    data = via.read_bytes()
    partes = data.split(b"\n", 3)
    if len(partes) != 4 or partes[0] != b"P6":
        raise RuntimeError("PPM invalidum")
    latitudo, altitudo = map(int, partes[1].split())
    return latitudo, altitudo, partes[3]


def differentiae(a: bytes, b: bytes) -> int:
    n = min(len(a), len(b)) // 3
    mutata = 0
    for i in range(n):
        p = i * 3
        if a[p:p + 3] != b[p:p + 3]:
            mutata += 1
    return mutata


def principale() -> int:
    if len(sys.argv) != 5:
        print("USUS: proba_murem_uefi_053.py MONITOR.sock QMP.sock EXITUS MORA")
        return 2

    monitor_via = Path(sys.argv[1])
    qmp_via = Path(sys.argv[2])
    exitus = Path(sys.argv[3])
    mora = float(sys.argv[4])
    ante = exitus / "murus-ante.ppm"
    post = exitus / "murus-post.ppm"

    finis = time.time() + 12.0
    while (not monitor_via.exists() or not qmp_via.exists()) and time.time() < finis:
        time.sleep(0.1)
    if not monitor_via.exists() or not qmp_via.exists():
        print("DEFECIT: monitor vel QMP non apparuit", file=sys.stderr)
        return 3

    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    monitor.settimeout(0.4)
    monitor.connect(str(monitor_via))
    q = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    q.settimeout(2.0)
    q.connect(str(qmp_via))

    try:
        lege_usque(monitor, b"(qemu) ", 2.0)
        salutatio = qmp_linea(q)
        if "QMP" not in salutatio:
            raise RuntimeError("salutatio QMP invalida")
        cap = qmp(q, "qmp_capabilities")
        if "error" in cap:
            raise RuntimeError(f"qmp_capabilities: {cap}")

        mures = qmp(q, "query-mice")
        candidati = [
            m for m in mures.get("return", [])
            if "PS/2 Mouse" in str(m.get("name", ""))
        ]
        if not candidati:
            print("DEFECIT: QEMU PS/2 Mouse non invenitur", file=sys.stderr)
            print(json.dumps(mures, ensure_ascii=False), file=sys.stderr)
            return 4

        mus = candidati[0]
        index = int(mus["index"])
        hmp(monitor, f"mouse_set {index}")
        time.sleep(mora)

        mures_post = qmp(q, "query-mice")
        currens = any(
            int(m.get("index", -1)) == index and bool(m.get("current"))
            for m in mures_post.get("return", [])
        )
        if not currens:
            print("DEFECIT: PS/2 Mouse selectus non est", file=sys.stderr)
            return 5

        hmp(monitor, f"screendump {ante}")
        finis = time.time() + 4.0
        while not ante.exists() and time.time() < finis:
            time.sleep(0.1)
        if not ante.exists():
            print("DEFECIT: captura initialis deest", file=sys.stderr)
            return 6

        # Nucleus canonicus post UEFI_PARA protocollum relativum hic publicat.
        metadata = hmp(monitor, "xp /3gx 0x03000b18")
        verba_hex = [v for v in metadata.replace(":", " ").split() if v.startswith("0x")]
        si_nonnullum = any(v not in {"0x0000000000000000", "0x0"} for v in verba_hex[1:])

        responsa = []
        for dx, dy in ((96, -64), (64, 48), (-24, 16)):
            responsa.append(qmp(q, "input-send-event", {
                "events": [
                    {"type": "rel", "data": {"axis": "x", "value": dx}},
                    {"type": "rel", "data": {"axis": "y", "value": dy}},
                ]
            }))
            time.sleep(0.15)

        if not all("return" in r and "error" not in r for r in responsa):
            print("DEFECIT: motus QMP recusatus est", file=sys.stderr)
            print(json.dumps(responsa, ensure_ascii=False), file=sys.stderr)
            return 7

        time.sleep(1.0)
        hmp(monitor, f"screendump {post}")
        finis = time.time() + 4.0
        while not post.exists() and time.time() < finis:
            time.sleep(0.1)
        if not post.exists():
            print("DEFECIT: captura post motum deest", file=sys.stderr)
            return 8

        w1, h1, pix1 = lege_ppm(ante)
        w2, h2, pix2 = lege_ppm(post)
        if (w1, h1) != (w2, h2):
            print("DEFECIT: dimensiones capturarum mutantur", file=sys.stderr)
            return 9
        mutata = differentiae(pix1, pix2)

        print(f"MURUS: QEMU PS/2 index={index}")
        print(f"MURUS: metadata {metadata.strip()}")
        print(f"MURUS: pixeli mutati={mutata}")
        if not si_nonnullum:
            print("DEFECIT: protocollum muris in metadata nucleo non apparet", file=sys.stderr)
            return 10
        if mutata < 20:
            print("DEFECIT: framebuffer motum muris non demonstrat", file=sys.stderr)
            return 11

        print("RECTE: murus PS/2 per UEFI VINDEX purum Sylviam movet.")
        return 0
    finally:
        try:
            hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()
        q.close()


if __name__ == "__main__":
    raise SystemExit(principale())
