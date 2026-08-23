#!/usr/bin/env python3
"""Verificat Sylviam post bootstrap solum codice VINDEX constare."""
from pathlib import Path
import re
import sys

RADIX = Path(__file__).resolve().parents[1]
SYSTEMA = RADIX / "Vindex Chat-GPT/vindex_final_v51/systema"
BOOTSTRAP = SYSTEMA / "uefi/bootstrap_uefi.c"

EXTENSIONES_VETITAE = {".c", ".h", ".cc", ".cpp", ".cxx", ".s", ".S", ".asm", ".rs"}
POLLE_HEREDITATUM = re.compile(r"(?<![A-Z0-9_])POLLE\(\)")
errata: list[str] = []

for via in SYSTEMA.rglob("*"):
    if not via.is_file():
        continue
    if via == BOOTSTRAP:
        continue
    if via.suffix in EXTENSIONES_VETITAE:
        errata.append(f"codex runtime non-VINDEX vetitus: {via.relative_to(RADIX)}")

if not BOOTSTRAP.exists():
    errata.append("bootstrap UEFI minimus deest")
else:
    textus = BOOTSTRAP.read_text(encoding="utf-8")
    # Haec verba opera runtime indicant quae bootstrap numquam gerere debet.
    vetita = [
        "ReadKeyStroke", "GetState", "EFI_FILE_PROTOCOL", "BLOCK_IO",
        "firmamentum_polle", "clientem_voca", "compone(", "z_order",
        "taskbar", "focus", "fenestra_native", "murus_relativus",
        "murus_absolutus", "VINDEX.FS",
    ]
    for verbum in vetita:
        if verbum in textus:
            errata.append(f"bootstrap officium runtime vetitum continet: {verbum}")

for via in SYSTEMA.rglob("*.vindex"):
    textus = via.read_text(encoding="utf-8")
    if POLLE_HEREDITATUM.search(textus):
        errata.append(f"callback C historicus POLLE adhuc adhibetur: {via.relative_to(RADIX)}")

if errata:
    print("ERRATUM: puritas VINDEX Sylviae violata est.", file=sys.stderr)
    for erratum in errata:
        print(f"  - {erratum}", file=sys.stderr)
    raise SystemExit(1)

print("RECTE: praeter bootstrap UEFI minimum, runtime Sylviae VINDEX purum est.")
