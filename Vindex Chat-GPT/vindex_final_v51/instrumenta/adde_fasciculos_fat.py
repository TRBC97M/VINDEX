#!/usr/bin/env python3
"""Fasciculos 8.3 in radicem FAT32 imaginis GPT/MBR addit sine mtools."""
from __future__ import annotations

import argparse
import struct
import sys
from pathlib import Path

EOC = 0x0FFFFFFF
SECTOR = 512


class ErrorFAT(ValueError):
    pass


def u16(buf: bytes | bytearray, off: int) -> int:
    return struct.unpack_from("<H", buf, off)[0]


def u32(buf: bytes | bytearray, off: int) -> int:
    return struct.unpack_from("<I", buf, off)[0]


def u64(buf: bytes | bytearray, off: int) -> int:
    return struct.unpack_from("<Q", buf, off)[0]


def p16(buf: bytearray, off: int, value: int) -> None:
    struct.pack_into("<H", buf, off, value)


def p32(buf: bytearray, off: int, value: int) -> None:
    struct.pack_into("<I", buf, off, value)


def nomen_83(textus: str) -> bytes:
    if "/" in textus or "\\" in textus:
        raise ErrorFAT("hoc instrumentum radicem tantum accipit")
    partes = textus.upper().split(".")
    if len(partes) == 1:
        basis, ext = partes[0], ""
    elif len(partes) == 2:
        basis, ext = partes
    else:
        raise ErrorFAT(f"nomen 8.3 invalidum: {textus}")
    licita = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_$%'-@~`!(){}^#&"
    if not (1 <= len(basis) <= 8 and len(ext) <= 3):
        raise ErrorFAT(f"nomen 8.3 extra limites: {textus}")
    if any(c not in licita for c in basis + ext):
        raise ErrorFAT(f"character 8.3 invalidus: {textus}")
    return basis.encode("ascii").ljust(8, b" ") + ext.encode("ascii").ljust(3, b" ")


def boot_fat32_validus(data: bytearray, lba: int) -> bool:
    off = lba * SECTOR
    if lba <= 0 or off + SECTOR > len(data):
        return False
    b = data[off:off + SECTOR]
    if b[510:512] != b"\x55\xaa":
        return False
    bps = u16(b, 11)
    spc = b[13]
    res = u16(b, 14)
    nfats = b[16]
    spf = u32(b, 36)
    root = u32(b, 44)
    total = u32(b, 32)
    return bps == 512 and spc > 0 and res > 0 and nfats > 0 and spf > 0 and root >= 2 and total > 0


def partitio_fat_inveni(data: bytearray) -> int:
    if len(data) < SECTOR or data[510:512] != b"\x55\xaa":
        raise ErrorFAT("MBR invalidus")

    # Imago canonica Sylviae GPT protectivum MBR habet. In tali imagine
    # MBR LBA=1 totum discum describit, non partitionem FAT. Tabula GPT
    # ipsa igitur legitur et prima partitio cum BPB FAT32 valido eligitur.
    if len(data) >= 2 * SECTOR and data[SECTOR:SECTOR + 8] == b"EFI PART":
        caput = SECTOR
        entries_lba = u64(data, caput + 72)
        numerus = u32(data, caput + 80)
        mensura = u32(data, caput + 84)
        if entries_lba > 0 and 128 <= mensura <= 4096 and numerus > 0:
            basis = entries_lba * SECTOR
            finis = min(numerus, 256)
            for i in range(finis):
                pos = basis + i * mensura
                if pos + 48 > len(data):
                    break
                if data[pos:pos + 16] == b"\0" * 16:
                    continue
                initium = u64(data, pos + 32)
                if boot_fat32_validus(data, initium):
                    return initium

    # Compatibilitas imaginum MBR veterum: partitiones quattuor probantur,
    # sed ingressus protectivus 0xEE numquam pro FAT accipitur.
    for i in range(4):
        pos = 446 + i * 16
        typus = data[pos + 4]
        initium = u32(data, pos + 8)
        if typus == 0 or typus == 0xEE:
            continue
        if boot_fat32_validus(data, initium):
            return initium

    raise ErrorFAT("partitio FAT32 in GPT/MBR non invenitur")


class FAT32:
    def __init__(self, data: bytearray):
        self.data = data
        self.part_lba = partitio_fat_inveni(data)
        self.part = self.part_lba * SECTOR
        b = data[self.part:self.part + SECTOR]
        self.bps = u16(b, 11)
        self.spc = b[13]
        self.res = u16(b, 14)
        self.nfats = b[16]
        self.spf = u32(b, 36)
        self.root = u32(b, 44)
        total = u32(b, 32)
        if self.bps != SECTOR or self.spc <= 0 or self.res <= 0 or self.nfats < 1 or self.spf <= 0:
            raise ErrorFAT("BPB FAT32 non sustinetur")
        self.cluster_bytes = self.bps * self.spc
        self.data_sector = self.res + self.nfats * self.spf
        self.cluster_count = (total - self.data_sector) // self.spc
        if self.root < 2 or self.cluster_count < 8:
            raise ErrorFAT("geometria FAT32 invalida")

    def fat_off(self, index: int, fat_no: int = 0) -> int:
        return self.part + (self.res + fat_no * self.spf) * self.bps + index * 4

    def fat_get(self, index: int) -> int:
        return u32(self.data, self.fat_off(index)) & 0x0FFFFFFF

    def fat_set(self, index: int, value: int) -> None:
        value &= 0x0FFFFFFF
        for f in range(self.nfats):
            off = self.fat_off(index, f)
            vetus = u32(self.data, off) & 0xF0000000
            p32(self.data, off, vetus | value)

    def cluster_off(self, cluster: int) -> int:
        if cluster < 2:
            raise ErrorFAT("cluster invalidus")
        sector = self.data_sector + (cluster - 2) * self.spc
        off = self.part + sector * self.bps
        if off + self.cluster_bytes > len(self.data):
            raise ErrorFAT("cluster extra imaginem")
        return off

    def catena(self, primus: int):
        visus: set[int] = set()
        c = primus
        while 2 <= c < 0x0FFFFFF8:
            if c in visus:
                raise ErrorFAT("catena FAT circularis")
            visus.add(c)
            yield c
            n = self.fat_get(c)
            if n >= 0x0FFFFFF8:
                return
            if n < 2:
                raise ErrorFAT("catena FAT truncata")
            c = n
        raise ErrorFAT("catena FAT invalida")

    def libera(self) -> int:
        for c in range(2, self.cluster_count + 2):
            if self.fat_get(c) == 0:
                self.fat_set(c, EOC)
                off = self.cluster_off(c)
                self.data[off:off + self.cluster_bytes] = b"\0" * self.cluster_bytes
                return c
        raise ErrorFAT("nullus cluster liber")

    def scribe_catenam(self, corpus: bytes) -> int:
        n = max(1, (len(corpus) + self.cluster_bytes - 1) // self.cluster_bytes)
        cat = [self.libera() for _ in range(n)]
        for i, c in enumerate(cat):
            self.fat_set(c, cat[i + 1] if i + 1 < len(cat) else EOC)
            off = self.cluster_off(c)
            pars = corpus[i * self.cluster_bytes:(i + 1) * self.cluster_bytes]
            self.data[off:off + len(pars)] = pars
        return cat[0]

    def locus_directorii(self, nomen: bytes) -> tuple[int, bool]:
        primus_liber: int | None = None
        cat = list(self.catena(self.root))
        for c in cat:
            off = self.cluster_off(c)
            for q in range(0, self.cluster_bytes, 32):
                pos = off + q
                prim = self.data[pos]
                if prim == 0x00:
                    if primus_liber is None:
                        primus_liber = pos
                    break
                if prim == 0xE5:
                    if primus_liber is None:
                        primus_liber = pos
                    continue
                if self.data[pos + 11] == 0x0F:
                    continue
                if bytes(self.data[pos:pos + 11]) == nomen:
                    return pos, True
            if primus_liber is not None:
                return primus_liber, False
        novus = self.libera()
        self.fat_set(cat[-1], novus)
        self.fat_set(novus, EOC)
        return self.cluster_off(novus), False

    def adde(self, nomen_textus: str, corpus: bytes) -> None:
        nomen = nomen_83(nomen_textus)
        locus, aderat = self.locus_directorii(nomen)
        if aderat:
            raise ErrorFAT(f"fasciculus iam adest: {nomen_textus}")
        primus = self.scribe_catenam(corpus)
        e = bytearray(32)
        e[0:11] = nomen
        e[11] = 0x20
        p16(e, 20, (primus >> 16) & 0xFFFF)
        p16(e, 26, primus & 0xFFFF)
        p32(e, 28, len(corpus))
        self.data[locus:locus + 32] = e


def argumenta(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Fasciculos in radicem FAT32 imaginis VINDEX addit")
    p.add_argument("imago", type=Path)
    p.add_argument("fasciculi", nargs="+", metavar="FONS=NOMEN.EXT")
    return p.parse_args(argv)


def principale(argv: list[str] | None = None) -> int:
    ns = argumenta(sys.argv[1:] if argv is None else argv)
    try:
        data = bytearray(ns.imago.read_bytes())
        fat = FAT32(data)
        print(f"FAT32: partitio LBA={fat.part_lba}, cluster={fat.cluster_bytes} octeta")
        for spec in ns.fasciculi:
            if "=" not in spec:
                raise ErrorFAT(f"argumentum invalidum: {spec}")
            fons_s, nomen = spec.rsplit("=", 1)
            fons = Path(fons_s)
            corpus = fons.read_bytes()
            fat.adde(nomen, corpus)
            print(f"RECTE: {fons} -> /{nomen.upper()} ({len(corpus)} octeta)")
        ns.imago.write_bytes(data)
    except (OSError, ErrorFAT, struct.error) as exc:
        print(f"DEFECIT: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
