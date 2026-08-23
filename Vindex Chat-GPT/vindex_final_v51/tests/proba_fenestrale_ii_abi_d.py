#!/usr/bin/env python3
"""Concordantiam ABI Fenestralis II inter C et bibliothecam VINDEX probat."""

from __future__ import annotations

from pathlib import Path
import re
import sys

RADIX = Path(__file__).resolve().parents[1]
CAPUT = RADIX / "systema" / "fenestrale_ii_abi.h"
VINDEX = RADIX / "bibliotheca" / "fenestrale_ii.vindex"

EXPECTED = {
    "FENESTRALE2_BASIS": 0x03000900,
    "FENESTRALE2_MAGIC": 0x00324E45464C5953,
    "FENESTRALE2_VERSIO": 1,
    "FENESTRALE2_MENSURA": 128,
    "FENESTRALE2_EVENTA_CAPUT": 0x03000980,
    "FENESTRALE2_EVENTA_BASIS": 0x030009A0,
    "FENESTRALE2_EVENTA_CAPACITAS": 32,
    "FENESTRALE2_EVENTUM_MENSURA": 32,
}

VINDEX_NUMERI = {
    "basis": 50333952,
    "eventa_caput": 50334080,
    "eventa_basis": 50334112,
    "magic": 14159808274651475,
    "versio": 1,
    "mensura": 128,
    "framebuffer": 50333984,
    "latitudo": 50333992,
    "altitudo": 50334000,
    "pixel_per_lineam": 50334008,
    "formatum": 50334016,
    "bits": 50334024,
    "murus_x": 50334032,
    "murus_y": 50334040,
    "bullae": 50334048,
    "numerus_eventuum": 50334056,
    "taskbar": 50334064,
    "scala": 50334072,
}


def define_numerum(textus: str, nomen: str) -> int:
    m = re.search(rf"^#define\s+{re.escape(nomen)}\s+([^\s/]+)", textus, re.M)
    if not m:
        raise AssertionError(f"definitio deest: {nomen}")
    valor = m.group(1).replace("ULL", "").replace("UL", "").replace("U", "")
    return int(valor, 0)


def exige(textus: str, fragmentum: str, nomen: str) -> None:
    if fragmentum not in textus:
        raise AssertionError(f"fragmentum VINDEX deest: {nomen}")


def principale() -> int:
    c = CAPUT.read_text(encoding="utf-8")
    v = VINDEX.read_text(encoding="utf-8")

    for nomen, valor in EXPECTED.items():
        inventum = define_numerum(c, nomen)
        if inventum != valor:
            raise AssertionError(f"{nomen}: {inventum} != {valor}")

    if "_Static_assert(sizeof(FENESTRALE2_DESCRIPTOR) == FENESTRALE2_MENSURA" not in c:
        raise AssertionError("assertio mensurae descriptoris deest")
    if "_Static_assert(sizeof(FENESTRALE2_EVENTUM) == FENESTRALE2_EVENTUM_MENSURA" not in c:
        raise AssertionError("assertio mensurae eventus deest")

    exige(v, f"REDDE {VINDEX_NUMERI['basis']}.", "basis")
    exige(v, f"REDDE {VINDEX_NUMERI['eventa_caput']}.", "eventa caput")
    exige(v, f"REDDE {VINDEX_NUMERI['eventa_basis']}.", "eventa basis")
    exige(v, f"CONTENTUM({VINDEX_NUMERI['basis']}) == {VINDEX_NUMERI['magic']}", "magic")
    exige(v, f"CONTENTUM({VINDEX_NUMERI['basis'] + 8}) == {VINDEX_NUMERI['versio']}", "versio")
    exige(v, f"CONTENTUM({VINDEX_NUMERI['basis'] + 16}) >= {VINDEX_NUMERI['mensura']}", "mensura")

    proba_addressa = [
        ("framebuffer", "FENESTRALE_II_FRAMEBUFFER"),
        ("latitudo", "FENESTRALE_II_LATITUDO"),
        ("altitudo", "FENESTRALE_II_ALTITUDO"),
        ("pixel_per_lineam", "FENESTRALE_II_PIXEL_PER_LINEAM"),
        ("formatum", "FENESTRALE_II_FORMATUM_PIXELORUM"),
        ("bits", "FENESTRALE_II_BITS_PER_PIXEL"),
        ("murus_x", "FENESTRALE_II_MURUS_X"),
        ("murus_y", "FENESTRALE_II_MURUS_Y"),
        ("bullae", "FENESTRALE_II_BULLAE"),
        ("numerus_eventuum", "FENESTRALE_II_NUMERUS_EVENTUUM"),
        ("taskbar", "FENESTRALE_II_TASKBAR_ALTITUDO"),
        ("scala", "FENESTRALE_II_SCALA_PER_MILLE"),
    ]
    for clavis, functio in proba_addressa:
        initium = v.find(f"FUNCTIO {functio}")
        finis = v.find("FIN-FUNCTIO.", initium)
        if initium < 0 or finis < 0:
            raise AssertionError(f"functio deest: {functio}")
        corpus = v[initium:finis]
        exige(corpus, f"CONTENTUM({VINDEX_NUMERI[clavis]})", functio)

    if VINDEX_NUMERI["eventa_basis"] + 32 * 32 > 0x03001000:
        raise AssertionError("circulus eventuum in umbram hereditariam incidit")

    print("RECTE: ABI Fenestralis II C et VINDEX concordant.")
    return 0


if __name__ == "__main__":
    sys.exit(principale())
