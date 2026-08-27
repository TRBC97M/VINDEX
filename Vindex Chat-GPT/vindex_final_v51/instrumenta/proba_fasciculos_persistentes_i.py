#!/usr/bin/env python3
"""P19-I: statum nuclei fasciculorum per monitor QEMU legit."""
from __future__ import annotations

import re
import socket
import sys
import time
from pathlib import Path

STATUS_ADRESSA = 0x03000B38


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
    return lege_usque(sock, b"(qemu) ", 3.0).decode(errors="replace")


def status_lege(sock: socket.socket) -> tuple[int | None, int | None, int | None]:
    responsum = hmp(sock, f"xp /3gx 0x{STATUS_ADRESSA:x}")
    valores: list[int] = []
    for linea in responsum.splitlines():
        if ":" not in linea:
            continue
        post = linea.split(":", 1)[1]
        for fragmentum in re.findall(r"0x[0-9a-fA-F]+", post):
            valores.append(int(fragmentum, 16))
    if len(valores) < 3:
        return None, None, None
    return valores[0], valores[1], valores[2]


def principale() -> int:
    if len(sys.argv) != 4:
        print("USUS: proba_fasciculos_persistentes_i.py MONITOR EXSPECTATUM MORA", file=sys.stderr)
        return 64

    via = Path(sys.argv[1])
    exspectatum = int(sys.argv[2])
    mora = float(sys.argv[3])
    finis = time.time() + mora
    while not via.exists() and time.time() < finis:
        time.sleep(0.1)
    if not via.exists():
        print("DEFECIT: monitor QEMU deest", file=sys.stderr)
        return 65

    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    monitor.settimeout(0.5)
    monitor.connect(str(via))
    try:
        lege_usque(monitor, b"(qemu) ", 2.0)
        finis = time.time() + mora
        ultimus: tuple[int | None, int | None, int | None] = (None, None, None)
        while time.time() < finis:
            ultimus = status_lege(monitor)
            status, mensura, backend = ultimus
            if status == exspectatum:
                print(f"FASCICULI: status={status} mensura={mensura} backend_uefi={backend}")
                hmp(monitor, "quit")
                return 0
            if status is not None and status >= 64:
                print(f"DEFECIT: nucleus P19 status={status} mensura={mensura} backend={backend}", file=sys.stderr)
                hmp(monitor, "quit")
                return int(status if status < 126 else 125)
            time.sleep(0.4)

        print(f"DEFECIT: status {exspectatum} intra moram non apparuit; ultimus={ultimus}", file=sys.stderr)
        hmp(monitor, "quit")
        return 66
    finally:
        monitor.close()


if __name__ == "__main__":
    raise SystemExit(principale())
