#!/usr/bin/env python3
"""Verificat catenam canonicam Sylviae omnino VINDEX puram esse."""
from pathlib import Path
import re
import sys

RADIX = Path(__file__).resolve().parents[1]
SYSTEMA = RADIX / "Vindex Chat-GPT/vindex_final_v51/systema"
UEFI = SYSTEMA / "uefi"
PONTICULUS = UEFI / "ponticulus_uefi_purus.vindex"
CONSTRUCTOR = UEFI / "construe_uefi_purum.sh"
NUCLEUS = SYSTEMA / "nucleus.vindex"

EXTENSIONES_VETITAE = {".c", ".h", ".cc", ".cpp", ".cxx", ".s", ".S", ".asm", ".rs"}
POLLE_HEREDITATUM = re.compile(r"(?<![A-Z0-9_])POLLE\(\)")
MANDATUM_HOST_VETITUM = re.compile(r"(?m)^[ \t]*(gcc|clang|ld|objcopy)(?:[ \t]|$)")
errata: list[str] = []

# Nulla exceptio linguae post canonizationem P1 manet in arbore systematis.
for via in SYSTEMA.rglob("*"):
    if via.is_file() and via.suffix in EXTENSIONES_VETITAE:
        errata.append(f"codex systematis non-VINDEX vetitus: {via.relative_to(RADIX)}")

if not PONTICULUS.exists():
    errata.append("ponticulus UEFI VINDEX purus deest")
else:
    textus = PONTICULUS.read_text(encoding="utf-8")
    requisita = [
        "UEFI_VOCA6",
        "SALI_AD(",
        "CONTENTUM(info_buf + 8)",
        "LEGE_U32(info + 32)",
        "NUCLEUS.BIN",
    ]
    for fragmentum in requisita:
        if fragmentum not in textus:
            errata.append(f"contractus ponticuli UEFI deest: {fragmentum}")

if not CONSTRUCTOR.exists():
    errata.append("constructor UEFI VINDEX purus deest")
else:
    constructio = CONSTRUCTOR.read_text(encoding="utf-8")
    mandatum = MANDATUM_HOST_VETITUM.search(constructio)
    if mandatum:
        errata.append(f"constructor UEFI instrumentum non-VINDEX ad codicem generandum adhibet: {mandatum.group(1)}")
    if "ponticulus_uefi_purus.vindex" not in constructio:
        errata.append("constructor UEFI ponticulum canonicum non adhibet")

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
    print("ERRATUM: puritas absoluta VINDEX Sylviae violata est.", file=sys.stderr)
    for erratum in errata:
        print(f"  - {erratum}", file=sys.stderr)
    raise SystemExit(1)

print("RECTE: catena canonica Sylviae nullam exceptionem C aut runtime non-VINDEX continet.")
