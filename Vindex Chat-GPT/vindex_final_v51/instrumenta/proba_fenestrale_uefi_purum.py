#!/usr/bin/env python3
"""Fenestrale II Purus sub UEFI cum mure PS/2 nativo comprobat."""
from __future__ import annotations

import json
import re
import socket
import sys
import time
from collections import Counter
from pathlib import Path


def lege_usque(sock: socket.socket, signum: bytes, mora: float = 3.0) -> bytes:
    finis = time.time() + mora
    data = bytearray()
    while signum not in data and time.time() < finis:
        try: pars = sock.recv(65536)
        except socket.timeout: continue
        if not pars: break
        data.extend(pars)
    return bytes(data)


def hmp(sock: socket.socket, mandatum: str) -> str:
    sock.sendall((mandatum + "\n").encode())
    return lege_usque(sock, b"(qemu) ", 4.0).decode(errors="replace")


def qmp_linea(sock: socket.socket) -> dict:
    data = bytearray()
    while b"\n" not in data:
        pars = sock.recv(65536)
        if not pars: raise RuntimeError("QMP clausum est")
        data.extend(pars)
    linea, _, _ = data.partition(b"\n")
    return json.loads(linea.decode())


def qmp(sock: socket.socket, mandatum: str, argumenta: dict | None = None) -> dict:
    petitio = {"execute": mandatum}
    if argumenta is not None: petitio["arguments"] = argumenta
    sock.sendall((json.dumps(petitio, separators=(",", ":")) + "\n").encode())
    while True:
        responsum = qmp_linea(sock)
        if "event" not in responsum: return responsum


def hexa_hmp(textus: str) -> list[int]:
    valores: list[int] = []
    for linea in textus.splitlines():
        if ":" not in linea: continue
        for verbum in re.findall(r"0x[0-9a-fA-F]{1,16}", linea.split(":", 1)[1]):
            valores.append(int(verbum, 16))
    return valores


def basis_ps2(monitor: socket.socket) -> int:
    # Sedes rectoris historice probata; initium fit post migrationem voluminis.
    return 0x03018800


def status_ps2(monitor: socket.socket, basis: int) -> list[int]:
    if basis == 0: return []
    return hexa_hmp(hmp(monitor, f"xp /9bx 0x{basis + 64:x}"))[:9]


def captura(monitor: socket.socket, via: Path) -> None:
    hmp(monitor, f"screendump {via}")
    finis = time.time() + 5.0
    while not via.exists() and time.time() < finis: time.sleep(0.1)
    if not via.exists(): raise RuntimeError(f"captura deest: {via}")


def ppm(via: Path) -> tuple[int, int, bytes]:
    partes = via.read_bytes().split(b"\n", 3)
    if len(partes) != 4 or partes[0] != b"P6": raise RuntimeError("PPM invalidum")
    w, h = map(int, partes[1].split())
    return w, h, partes[3]


def differentiae(a: bytes, b: bytes) -> int:
    n = min(len(a), len(b)) // 3
    return sum(a[i*3:i*3+3] != b[i*3:i*3+3] for i in range(n))


def pictura_structura(pix: bytes):
    c = Counter(tuple(pix[i:i+3]) for i in range(0, len(pix)-2, 3))
    distincti = sum(1 for _, n in c.items() if n > 30)
    communes = c.most_common(12)
    dominans = communes[0][1] if communes else 0
    return c, distincti, communes, dominans


def principale() -> int:
    if len(sys.argv) != 5:
        print("USUS: proba_fenestrale_uefi_purum.py MONITOR QMP EXITUS MORA", file=sys.stderr); return 2
    mon_via, qmp_via, out, mora = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), float(sys.argv[4])
    ante, post = out/"fenestrale-ante.ppm", out/"fenestrale-post.ppm"
    finis = time.time() + 12.0
    while (not mon_via.exists() or not qmp_via.exists()) and time.time() < finis: time.sleep(0.1)
    if not mon_via.exists() or not qmp_via.exists(): print("DEFECIT: monitor vel QMP deest", file=sys.stderr); return 3
    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM); monitor.settimeout(0.4); monitor.connect(str(mon_via))
    q = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM); q.settimeout(2.0); q.connect(str(qmp_via))
    try:
        lege_usque(monitor, b"(qemu) ", 2.0)
        if "QMP" not in qmp_linea(q): print("DEFECIT: salutatio QMP invalida", file=sys.stderr); return 4
        qmp(q, "qmp_capabilities")
        mures = qmp(q, "query-mice").get("return", [])
        candidati = [m for m in mures if "PS/2 Mouse" in str(m.get("name", ""))]
        if not candidati: print("DEFECIT: QEMU PS/2 Mouse deest", file=sys.stderr); return 5
        index = int(candidati[0]["index"]); hmp(monitor, f"mouse_set {index}"); time.sleep(mora)

        basis = basis_ps2(monitor)
        ante_ps2 = status_ps2(monitor, basis)
        metadata = hexa_hmp(hmp(monitor, "xp /12gx 0x03000800"))[:12]
        g = hexa_hmp(hmp(monitor, "xp /1gx 0x03000b38")); gradus = g[0] if g else 0
        ge = hexa_hmp(hmp(monitor, "xp /1gx 0x03000b40")); gradus_eg = ge[0] if ge else 0
        acervus = hexa_hmp(hmp(monitor, "xp /8gx 0x02000000"))[:8]
        acervus_octeta = hexa_hmp(hmp(monitor, "xp /32bx 0x02000000"))[:32]
        captura(monitor, ante); w1, h1, pix1 = ppm(ante)
        colores, distincti, communes, dominans = pictura_structura(pix1)
        signa = {(8,35,61): colores[(8,35,61)], (98,215,242): colores[(98,215,242)], (241,238,228): colores[(241,238,228)]}
        print(f"FENESTRALE: gradus_diagnostici={gradus}/{gradus_eg} metadata={metadata}")
        print(f"FENESTRALE: acervus_qword={acervus}")
        print(f"FENESTRALE: acervus_octeta={acervus_octeta}")
        print(f"FENESTRALE: ps2_ante={ante_ps2} signa={signa} colores_communes={communes}")
        if (w1, h1) != (1280, 800): print(f"DEFECIT: resolutio {w1}x{h1}", file=sys.stderr); return 7
        if distincti < 8 or dominans > (w1*h1*97//100): print(f"DEFECIT: pictura nimis simplex: distincti={distincti} dominans={dominans}", file=sys.stderr); return 8
        if signa[(8,35,61)] < 100 or signa[(98,215,242)] < 100 or signa[(241,238,228)] < 20:
            print(f"DEFECIT: signa picturae Fenestralis desunt: {signa}", file=sys.stderr); return 14
        if len(ante_ps2) < 3 or ante_ps2[0] != 9 or ante_ps2[1:3] != [250,250]: print(f"DEFECIT: initium PS/2 invalidum: {ante_ps2}", file=sys.stderr); return 9

        responsa=[]
        for dx,dy in ((120,-70),(80,50),(-36,24)):
            responsa.append(qmp(q,"input-send-event",{"events":[{"type":"rel","data":{"axis":"x","value":dx}},{"type":"rel","data":{"axis":"y","value":dy}}]})); time.sleep(0.25)
        for dx,dy in ((64,-32),(32,48),(-20,18)): hmp(monitor,f"mouse_move {dx} {dy}"); time.sleep(0.25)
        if not all("error" not in r for r in responsa): print(f"DEFECIT: QMP motum recusavit: {responsa}", file=sys.stderr); return 10
        time.sleep(1.0)
        post_ps2=status_ps2(monitor,basis); captura(monitor,post); w2,h2,pix2=ppm(post); mutata=differentiae(pix1,pix2)
        raw=hexa_hmp(hmp(monitor,f"xp /3gx 0x{basis+72:x}"))[:3]
        print(f"FENESTRALE: resolutio={w1}x{h1} distincti={distincti}")
        print(f"FENESTRALE: basis_ps2=0x{basis:x} initium={ante_ps2[:3]} post={post_ps2[:4]}")
        print(f"FENESTRALE: raw_dx_dy_bullae={raw} pixeli_mutati={mutata}")
        if (w1,h1)!=(w2,h2): print("DEFECIT: dimensiones mutantur",file=sys.stderr); return 11
        if len(post_ps2)<4 or post_ps2[3]==ante_ps2[3]: print("DEFECIT: nullus fasciculus PS/2 receptus",file=sys.stderr); return 12
        if mutata<20: print("DEFECIT: PS/2 receptus est sed Fenestrale non redpinxit",file=sys.stderr); return 13
        print("RECTE: Fenestrale II Purus sub UEFI puro murem PS/2 nativum exercet."); return 0
    finally:
        try: hmp(monitor,"quit")
        except Exception: pass
        monitor.close(); q.close()

if __name__ == "__main__": raise SystemExit(principale())
