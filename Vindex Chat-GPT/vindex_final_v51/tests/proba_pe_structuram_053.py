#!/usr/bin/env python3
"""Structuram PE32+ et vocationes IAT in producto VINDEX 0.53 verificat."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import struct
import sys


class ErratumPE(RuntimeError):
    pass


@dataclass(frozen=True)
class Sectio:
    nomen: str
    rva: int
    mensura_virtualis: int
    mensura_cruda: int
    positio_cruda: int


@dataclass(frozen=True)
class Importatio:
    dll: str
    nomen: str
    rva_iat: int


def u16(data: bytes, pos: int) -> int:
    if pos < 0 or pos + 2 > len(data):
        raise ErratumPE(f"lectio U16 extra fasciculum ad {pos}")
    return struct.unpack_from("<H", data, pos)[0]


def u32(data: bytes, pos: int) -> int:
    if pos < 0 or pos + 4 > len(data):
        raise ErratumPE(f"lectio U32 extra fasciculum ad {pos}")
    return struct.unpack_from("<I", data, pos)[0]


def u64(data: bytes, pos: int) -> int:
    if pos < 0 or pos + 8 > len(data):
        raise ErratumPE(f"lectio U64 extra fasciculum ad {pos}")
    return struct.unpack_from("<Q", data, pos)[0]


def s32(data: bytes, pos: int) -> int:
    if pos < 0 or pos + 4 > len(data):
        raise ErratumPE(f"lectio S32 extra fasciculum ad {pos}")
    return struct.unpack_from("<i", data, pos)[0]


def c_string(data: bytes, pos: int) -> str:
    if pos < 0 or pos >= len(data):
        raise ErratumPE(f"catena extra fasciculum ad {pos}")
    finis = data.find(b"\x00", pos)
    if finis < 0:
        raise ErratumPE(f"catena sine termino ad {pos}")
    try:
        return data[pos:finis].decode("ascii")
    except UnicodeDecodeError as exc:
        raise ErratumPE(f"catena non ASCII ad {pos}") from exc


def parse_sectiones(data: bytes, pe: int) -> tuple[list[Sectio], int, int, int, int, int]:
    numerus = u16(data, pe + 6)
    mensura_opt = u16(data, pe + 20)
    opt = pe + 24
    if u16(data, opt) != 0x20B:
        raise ErratumPE("caput optionale PE32+ (0x20B) deest")
    mensura_capitum = u32(data, opt + 60)
    rva_import = u32(data, opt + 112 + 8)
    mensura_import = u32(data, opt + 112 + 12)
    rva_iat = u32(data, opt + 112 + 12 * 8)
    mensura_iat = u32(data, opt + 112 + 12 * 8 + 4)

    initium = opt + mensura_opt
    sectiones: list[Sectio] = []
    for i in range(numerus):
        pos = initium + i * 40
        if pos + 40 > len(data):
            raise ErratumPE("caput sectionis truncatum est")
        nomen = data[pos : pos + 8].split(b"\x00", 1)[0].decode("ascii", "strict")
        sectiones.append(
            Sectio(
                nomen=nomen,
                mensura_virtualis=u32(data, pos + 8),
                rva=u32(data, pos + 12),
                mensura_cruda=u32(data, pos + 16),
                positio_cruda=u32(data, pos + 20),
            )
        )
    return sectiones, mensura_capitum, rva_import, mensura_import, rva_iat, mensura_iat


def rva_ad_pos(rva: int, sectiones: list[Sectio], mensura_capitum: int) -> int:
    if rva < mensura_capitum:
        return rva
    for sectio in sectiones:
        amplitudo = max(sectio.mensura_virtualis, sectio.mensura_cruda)
        if sectio.rva <= rva < sectio.rva + amplitudo:
            distantia = rva - sectio.rva
            if distantia >= sectio.mensura_cruda:
                raise ErratumPE(f"RVA 0x{rva:x} intra partem virtualem sine octetis crudis est")
            return sectio.positio_cruda + distantia
    raise ErratumPE(f"RVA 0x{rva:x} ad nullam sectionem pertinet")


def parse_importationes(
    data: bytes,
    sectiones: list[Sectio],
    mensura_capitum: int,
    rva_import: int,
    mensura_import: int,
) -> list[Importatio]:
    if rva_import == 0 or mensura_import == 0:
        raise ErratumPE("directorium importationum vacuum est")
    pos = rva_ad_pos(rva_import, sectiones, mensura_capitum)
    finis = pos + mensura_import
    importationes: list[Importatio] = []
    numerus_descriptorum = 0
    while pos + 20 <= len(data) and pos < finis:
        original_first_thunk = u32(data, pos)
        timestamp = u32(data, pos + 4)
        forwarder = u32(data, pos + 8)
        rva_nominis = u32(data, pos + 12)
        first_thunk = u32(data, pos + 16)
        if original_first_thunk == timestamp == forwarder == rva_nominis == first_thunk == 0:
            break
        numerus_descriptorum += 1
        if rva_nominis == 0 or first_thunk == 0:
            raise ErratumPE("descriptor importationis incompletus est")
        dll = c_string(data, rva_ad_pos(rva_nominis, sectiones, mensura_capitum))
        rva_thunk = original_first_thunk or first_thunk
        idx = 0
        while True:
            pos_thunk = rva_ad_pos(rva_thunk + idx * 8, sectiones, mensura_capitum)
            valor = u64(data, pos_thunk)
            if valor == 0:
                break
            if valor & (1 << 63):
                nomen = f"#{valor & 0xFFFF}"
            else:
                pos_hint = rva_ad_pos(valor, sectiones, mensura_capitum)
                _hint = u16(data, pos_hint)
                nomen = c_string(data, pos_hint + 2)
            importationes.append(Importatio(dll=dll, nomen=nomen, rva_iat=first_thunk + idx * 8))
            idx += 1
            if idx > 4096:
                raise ErratumPE("catena thunk importationum terminum non habet")
        pos += 20
    if numerus_descriptorum == 0:
        raise ErratumPE("nullus descriptor importationis inventus est")
    return importationes


def verifica_vocationes_iat(
    data: bytes,
    sectiones: list[Sectio],
    importationes: list[Importatio],
) -> tuple[int, list[str]]:
    textus = next((s for s in sectiones if s.nomen == ".text"), None)
    if textus is None:
        raise ErratumPE("sectio .text deest")
    initium = textus.positio_cruda
    finis = min(len(data), initium + textus.mensura_cruda)
    iat = {imp.rva_iat: imp for imp in importationes}
    rectae = 0
    alienae: list[str] = []
    pos = initium
    while pos + 6 <= finis:
        if data[pos] == 0xFF and data[pos + 1] == 0x15:
            disp = s32(data, pos + 2)
            rva_instructionis = textus.rva + (pos - initium)
            rva_scopi = rva_instructionis + 6 + disp
            imp = iat.get(rva_scopi)
            if imp is None:
                alienae.append(f"0x{rva_instructionis:x}->0x{rva_scopi:x}")
            else:
                rectae += 1
            pos += 6
        else:
            pos += 1
    return rectae, alienae


def principale() -> int:
    parser = argparse.ArgumentParser(
        description="PE32+ VINDEX, importationes et vocationes RIP-relative IAT verificat."
    )
    parser.add_argument("fasciculus", type=Path)
    parser.add_argument(
        "--requirit",
        action="append",
        default=[],
        metavar="API",
        help="nomen API quod in IAT inveniri debet; iterari potest",
    )
    parser.add_argument(
        "--sine-vocationibus-iat",
        action="store_true",
        help="vocationes FF 15 non scrutatur",
    )
    args = parser.parse_args()

    data = args.fasciculus.read_bytes()
    try:
        if len(data) < 0x40 or data[:2] != b"MZ":
            raise ErratumPE("signatura DOS MZ deest")
        pe = u32(data, 0x3C)
        if pe + 24 > len(data) or data[pe : pe + 4] != b"PE\x00\x00":
            raise ErratumPE("signatura PE deest")
        if u16(data, pe + 4) != 0x8664:
            raise ErratumPE("machina PE non est AMD64")

        sectiones, capita, rva_imp, mens_imp, rva_iat, mens_iat = parse_sectiones(data, pe)
        nomina_sectionum = {s.nomen for s in sectiones}
        if ".text" not in nomina_sectionum:
            raise ErratumPE("sectio .text deest")
        if ".idata" not in nomina_sectionum:
            raise ErratumPE("sectio .idata deest")
        if rva_iat == 0 or mens_iat == 0:
            raise ErratumPE("directorium IAT vacuum est")

        importationes = parse_importationes(data, sectiones, capita, rva_imp, mens_imp)
        kernel32 = [imp for imp in importationes if imp.dll.lower() == "kernel32.dll"]
        if not kernel32:
            raise ErratumPE("KERNEL32.dll inter importationes deest")
        nomina = {imp.nomen for imp in kernel32}
        desunt = [nomen for nomen in args.requirit if nomen not in nomina]
        if desunt:
            raise ErratumPE("API requisitae desunt: " + ", ".join(desunt))

        if not args.sine_vocationibus_iat:
            rectae, alienae = verifica_vocationes_iat(data, sectiones, importationes)
            if rectae == 0:
                raise ErratumPE("nulla vocatio FF 15 ad IAT inventa est")
            if alienae:
                raise ErratumPE("vocationes FF 15 extra IAT: " + ", ".join(alienae[:8]))
        else:
            rectae = 0

        print("=== STRUCTURA PE VINDEX 0.53 ===")
        print("RECTE: PE32+ AMD64")
        print("SECTIONES: " + ", ".join(s.nomen for s in sectiones))
        print(f"IMPORTA: RVA=0x{rva_imp:x} MENSURA={mens_imp}")
        print(f"IAT: RVA=0x{rva_iat:x} MENSURA={mens_iat}")
        for imp in importationes:
            print(f"IAT 0x{imp.rva_iat:x}: {imp.dll}!{imp.nomen}")
        if not args.sine_vocationibus_iat:
            print(f"VOCATIONES IAT FF15 RECTAE: {rectae}")
        print("RECTE: structura PE et importationes congruunt.")
        return 0
    except (ErratumPE, OSError, struct.error, UnicodeDecodeError) as exc:
        print(f"ERRATUM: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(principale())
