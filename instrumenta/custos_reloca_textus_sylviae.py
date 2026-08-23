#!/usr/bin/env python3
"""Relocat blocum textuum Fenestralis e 0x0041E000 ad 0x00430000."""
from pathlib import Path
import re

RADIX = Path(__file__).resolve().parents[1]
VIA = RADIX / "Vindex Chat-GPT/vindex_final_v51/systema/nucleus.vindex"
VETUS = 0x0041E000
NOVUS = 0x00430000
FINIS = VETUS + 0x1000
DELTA = NOVUS - VETUS

textus = VIA.read_text(encoding="utf-8")
numerus = 0

def converte(m: re.Match[str]) -> str:
    global numerus
    valor = int(m.group(0))
    if VETUS <= valor < FINIS:
        numerus += 1
        return str(valor + DELTA)
    return m.group(0)

textus = re.sub(r"\b\d+\b", converte, textus)
if numerus == 0:
    if str(NOVUS) in textus:
        print("RECTE: textus iam relocati sunt.")
        raise SystemExit(0)
    raise SystemExit("ERRATUM: nulla inscriptio textuum veterum inventa est")
VIA.write_text(textus, encoding="utf-8")
print(f"RECTE: {numerus} inscriptiones textuum relocatae sunt +{DELTA} octetis.")
