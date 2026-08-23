#!/usr/bin/env python3
"""Verificat Sylviam post bootstrap solum codice VINDEX constare."""
from pathlib import Path
import re
import sys

RADIX = Path(__file__).resolve().parents[1]
SYSTEMA = RADIX / "Vindex Chat-GPT/vindex_final_v51/systema"
BOOTSTRAP = SYSTEMA / "uefi/bootstrap_uefi.c"
NUCLEUS = SYSTEMA / "nucleus.vindex"

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
    for fragmentum in [
        "#define UEFI_STATUS (COMMUNIS + 0xB00ULL)",
        "meta[7] = scala;",
        "meta[8] = (latitudo - 320 * scala) / 2;",
        "meta[9] = (altitudo - 200 * scala) / 2;",
        "((volatile U64 *)UEFI_STATUS)[0] = (U64)(UINTN)imago;",
    ]:
        if fragmentum not in textus:
            errata.append(f"contractus metadatae UEFI deest: {fragmentum}")

if NUCLEUS.exists():
    nucleus = NUCLEUS.read_text(encoding="utf-8")
    partes = nucleus.split("// --- UEFI runtime VINDEX purum", 1)
    if len(partes) != 2:
        errata.append("sectio runtime UEFI VINDEX puri deest")
    else:
        uefi = partes[1]
        for locus in ["50333752", "50333760", "50333768", "50333792", "50333800"]:
            if locus in uefi:
                errata.append(f"status UEFI metadata graphica corrumpit: {locus}")
        for locus in ["50334464", "50334472", "50334480", "50334488", "50334496"]:
            if locus not in uefi:
                errata.append(f"status UEFI separatus deest: {locus}")

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
