#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import os
import shutil
import socket
import sys
import time
from pathlib import Path

if len(sys.argv) != 5:
    raise SystemExit("USUS: captura_initium_realis.py MONITOR QMP EXITUS MORA")

mon_via = Path(sys.argv[1])
out = Path(sys.argv[3])
mora = float(sys.argv[4])
radix = Path(__file__).resolve().parents[1] / "Vindex Chat-GPT" / "vindex_final_v51"
mod_via = radix / "instrumenta" / "proba_initium_sylviae_ii.py"
spec = importlib.util.spec_from_file_location("proba_initium", mod_via)
if spec is None or spec.loader is None:
    raise SystemExit("DEFECIT: probator INITIUM importari non potest")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

finis = time.time() + 12.0
while not mon_via.exists() and time.time() < finis:
    time.sleep(0.1)
if not mon_via.exists():
    raise SystemExit("DEFECIT: monitor deest")

monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
monitor.settimeout(0.5)
monitor.connect(str(mon_via))
try:
    mod.lege_usque(monitor, b"(qemu) ", 2.0)
    time.sleep(mora)

    ante = out / "captura-ante.ppm"
    mod.captura(monitor, ante)
    w, h, pix = mod.ppm(ante)
    init_pos = mod.cursor_quaere(pix, w, h)
    if init_pos is None:
        raise SystemExit("DEFECIT: cursor initialis non inventus")

    pos_initium = mod.move_ad(monitor, out, "captura-initium", 50, 770, w, h)
    mod.click(monitor)
    time.sleep(0.3)
    pos_tabula = mod.move_ad(monitor, out, "captura-tabula", 150, 650, w, h)

    captura = out / "sylvia-initium-realis.ppm"
    mod.captura(monitor, captura)
    _, _, pix2 = mod.ppm(captura)
    if mod.pixel(pix2, w, 20, 510) != (14, 66, 111):
        raise SystemExit("DEFECIT: INITIUM in captura reali non apertum")
    if mod.pixel(pix2, w, 300, 650) != (185, 196, 207):
        raise SystemExit("DEFECIT: TABULA in captura reali non hover")

    destinatio = Path(os.environ["GITHUB_WORKSPACE"]) / "sylvia-initium-realis.ppm"
    shutil.copyfile(captura, destinatio)
    print(f"CAPTURA REALIS: cursor_init={init_pos} cursor_initium={pos_initium} cursor_tabula={pos_tabula}")
    print(f"CAPTURA REALIS: {destinatio}")
finally:
    try:
        mod.hmp(monitor, "quit")
    except Exception:
        pass
    monitor.close()
