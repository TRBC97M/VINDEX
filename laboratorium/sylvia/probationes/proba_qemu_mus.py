#!/usr/bin/env python3
"""Probatio muris relativi per OVMF et QEMU."""

from __future__ import annotations

import json
import socket
import sys
import time
from pathlib import Path

from proba_qemu import (
    differentiae,
    exhaure,
    hmp,
    lege_ppm,
    netto_hmp,
    numera_colorem,
    numera_regionem,
    qmp_exsequere,
    qmp_linea,
)


def telemetria(sock: socket.socket) -> str:
    return netto_hmp(hmp(sock, "xp /12bx 0x030008c8"))


def principale() -> int:
    if len(sys.argv) != 4:
        print("USUS: proba_qemu_mus.py MONITOR.sock QMP.sock EXITUS")
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
        lista = mures_ante.get("return", [])
        candidati = [m for m in lista if "PS/2 Mouse" in str(m.get("name", ""))]
        if not candidati:
            print("QEMU: MURUS DEFECIT (QEMU PS/2 Mouse deest)")
            print("QEMU: QMP_MURES " + json.dumps(mures_ante, ensure_ascii=False, separators=(",", ":")))
            return 5

        mus = candidati[0]
        index = int(mus["index"])
        selectio = netto_hmp(hmp(s, f"mouse_set {index}"))
        time.sleep(0.2)
        mures_post = qmp_exsequere(q, "query-mice")
        mus_currens = any(
            int(m.get("index", -1)) == index and bool(m.get("current"))
            for m in mures_post.get("return", [])
        )

        time.sleep(4.0)
        hmp(s, f"screendump {ante}")
        finis = time.time() + 3.0
        while not ante.exists() and time.time() < finis:
            time.sleep(0.1)
        if not ante.exists():
            print("QEMU: ERRATUM captura initialis non creata")
            return 4

        tele_ante = telemetria(s)
        registra = netto_hmp(hmp(s, "info registers"))
        usb = netto_hmp(hmp(s, "info usb"))
        w, h, pix_ante = lege_ppm(ante)
        ebur = numera_colorem(pix_ante, (241, 238, 228), 9)
        desktop = ebur > (w * h) // 100
        sh = h - 28
        lx = w * 21 // 100
        ly = sh * 31 // 100
        glyphi = numera_regionem(
            pix_ante, w, h, lx + 8, ly + 7, lx + 8 + 13 * 8, ly + 21,
            (234, 248, 255), 10,
        )
        textus = glyphi >= 12

        eventus = []
        tele_eventus: list[str] = []
        for dx, dy in ((96, -64), (64, 48), (-24, 16)):
            r = qmp_exsequere(q, "input-send-event", {
                "events": [
                    {"type": "rel", "data": {"axis": "x", "value": dx}},
                    {"type": "rel", "data": {"axis": "y", "value": dy}},
                ]
            })
            eventus.append(r)
            time.sleep(0.08)
            tele_eventus.append(telemetria(s))
            time.sleep(0.10)

        qmp_ok = all("return" in r and "error" not in r for r in eventus)
        time.sleep(0.7)
        tele_post = telemetria(s)
        hmp(s, f"screendump {post}")
        finis = time.time() + 3.0
        while not post.exists() and time.time() < finis:
            time.sleep(0.1)

        mutatio = -1
        if post.exists():
            w2, h2, pix_post = lege_ppm(post)
            if w2 == w and h2 == h:
                mutatio = differentiae(pix_ante, pix_post)

        murus = mus_currens and qmp_ok and mutatio >= 20
        metadata = netto_hmp(hmp(s, "xp /8gx 0x03000890"))
        inventarium = netto_hmp(hmp(s, "xp /18gx 0x03000900"))
        moderatores = netto_hmp(hmp(s, "xp /1gx 0x03000990"))

        print(f"QEMU: RESOLUTIO {w}x{h}")
        print("QEMU: QMP_MURES_ANTE " + json.dumps(mures_ante, ensure_ascii=False, separators=(",", ":")))
        print(f"QEMU: QMP_SELECTIO_PS2 index={index} {selectio}")
        print("QEMU: QMP_MURES_POST " + json.dumps(mures_post, ensure_ascii=False, separators=(",", ":")))
        print("QEMU: MUS_CURRENS " + ("RECTE" if mus_currens else "DEFECIT"))
        print("QEMU: QMP_MOTUS " + ("RECTE" if qmp_ok else "DEFECIT"))
        print(f"QEMU: USB {usb}")
        print(f"QEMU: REGISTRA_CPU {registra}")
        print(f"QEMU: TELEMETRIA_ANTE {tele_ante}")
        for i, t in enumerate(tele_eventus, 1):
            print(f"QEMU: TELEMETRIA_EVENTUS_{i} {t}")
        print(f"QEMU: TELEMETRIA_POST {tele_post}")
        print(f"QEMU: META_MURUS {metadata}")
        print(f"QEMU: INVENTARIUM_MURIS {inventarium}")
        print(f"QEMU: MODERATORES {moderatores}")
        print(f"QEMU: EBUR {ebur}")
        print(f"QEMU: GLYPHI_TITULI {glyphi}")
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
        q.close()


if __name__ == "__main__":
    raise SystemExit(principale())