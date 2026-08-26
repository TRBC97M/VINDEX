#!/usr/bin/env python3
"""Facit imaginem GPT/FAT32 removibilem cum /EFI/BOOT/BOOTX64.EFI."""

from __future__ import annotations

import binascii
from pathlib import Path
import struct
import sys
import uuid


SECTOR = 512
MENSURA_VOLUMINIS = 32768
SECTORES_TOTALES = 131072  # 64 MiB
PARTITIO_INITIUM = 2048
PARTITIO_FINIS = SECTORES_TOTALES - 2049
PARTITIO_SECTORES = PARTITIO_FINIS - PARTITIO_INITIUM + 1
VOLUMEN_INITIUM = PARTITIO_FINIS + 1
VOLUMEN_FINIS = SECTORES_TOTALES - 34
SIGNUM_VOLUMINIS = b"VINDEXV0"


def u16(buf: bytearray, pos: int, value: int) -> None:
    struct.pack_into("<H", buf, pos, value)


def u32(buf: bytearray, pos: int, value: int) -> None:
    struct.pack_into("<I", buf, pos, value)


def u64(buf: bytearray, pos: int, value: int) -> None:
    struct.pack_into("<Q", buf, pos, value)


def ingressus_directorii(nomen: bytes, attributum: int, botrus: int, mensura: int = 0) -> bytes:
    if len(nomen) != 11:
        raise ValueError("nomen FAT undecim octeta requirit")
    e = bytearray(32)
    e[0:11] = nomen
    e[11] = attributum
    u16(e, 20, (botrus >> 16) & 0xFFFF)
    u16(e, 26, botrus & 0xFFFF)
    u32(e, 28, mensura)
    return bytes(e)


def principale() -> int:
    if len(sys.argv) not in (3, 4, 5):
        print(
            "USUS: fac_imaginem_uefi.py BOOTX64.EFI imago.img [NUCLEUS.BIN] [TEXTUS.BIN]",
            file=sys.stderr,
        )
        return 64
    via_efi = Path(sys.argv[1])
    via_imaginis = Path(sys.argv[2])
    efi = via_efi.read_bytes()
    # Nucleus, si datus, in radice voluminis ponitur, ut ponticulus eum
    # per protocollum fasciculorum UEFI aperire possit.
    nucleus = Path(sys.argv[3]).read_bytes() if len(sys.argv) >= 4 else b""
    textus = Path(sys.argv[4]).read_bytes() if len(sys.argv) == 5 else b""

    reservati = 32
    numerus_fat = 2
    sectores_per_botrum = 1
    sectores_fat = 1
    while True:
        botri = (PARTITIO_SECTORES - reservati - numerus_fat * sectores_fat) // sectores_per_botrum
        necessarii = (botri + 2) * 4
        novus = (necessarii + SECTOR - 1) // SECTOR
        if novus == sectores_fat:
            break
        sectores_fat = novus
    data_initium = reservati + numerus_fat * sectores_fat
    botri = (PARTITIO_SECTORES - data_initium) // sectores_per_botrum

    fasciculi_botri = (len(efi) + SECTOR - 1) // SECTOR
    primus_fasciculi = 5
    ultimus_fasciculi = primus_fasciculi + fasciculi_botri - 1
    nuclei_botri = (len(nucleus) + SECTOR - 1) // SECTOR if nucleus else 0
    primus_nuclei = ultimus_fasciculi + 1
    ultimus_nuclei = primus_nuclei + nuclei_botri - 1
    textus_botri = (len(textus) + SECTOR - 1) // SECTOR if textus else 0
    primus_textus = (ultimus_nuclei if nucleus else ultimus_fasciculi) + 1
    ultimus_textus = primus_textus + textus_botri - 1
    voluminis_botri = MENSURA_VOLUMINIS // SECTOR
    ultimus_ante_volumen = ultimus_textus if textus else (
        ultimus_nuclei if nucleus else ultimus_fasciculi
    )
    primus_voluminis = ultimus_ante_volumen + 1
    ultimus_voluminis = primus_voluminis + voluminis_botri - 1
    si_occupati = 3 + fasciculi_botri + nuclei_botri + textus_botri + voluminis_botri

    imago = bytearray(SECTORES_TOTALES * SECTOR)

    # MBR protectivus.
    mbr = memoryview(imago)[:SECTOR]
    mbr[446 + 4] = 0xEE
    struct.pack_into("<I", mbr, 446 + 8, 1)
    struct.pack_into("<I", mbr, 446 + 12, SECTORES_TOTALES - 1)
    mbr[510:512] = b"\x55\xaa"

    # Tabula GPT primaria et secundaria.
    entrata = bytearray(128 * 128)
    typus_esp = uuid.UUID("c12a7328-f81f-11d2-ba4b-00a0c93ec93b")
    guid_partis = uuid.UUID("3d7f16b2-4a9e-4cf4-a34f-56494e444558")
    entrata[0:16] = typus_esp.bytes_le
    entrata[16:32] = guid_partis.bytes_le
    u64(entrata, 32, PARTITIO_INITIUM)
    u64(entrata, 40, PARTITIO_FINIS)
    nomen = "VINDEX SYSTEMA".encode("utf-16le")
    entrata[56:56 + len(nomen)] = nomen

    # Partitio rudis: firmware blocos persistit, VINDEX formam internam tenet.
    typus_voluminis = uuid.UUID("ebd0a0a2-b9e5-4433-87c0-68b6b72699c7")
    guid_voluminis = uuid.UUID("56494e44-4558-4653-3030-343400000001")
    altera = 128
    entrata[altera:altera + 16] = typus_voluminis.bytes_le
    entrata[altera + 16:altera + 32] = guid_voluminis.bytes_le
    u64(entrata, altera + 32, VOLUMEN_INITIUM)
    u64(entrata, altera + 40, VOLUMEN_FINIS)
    nomen_voluminis = "VINDEX VOLUMEN".encode("utf-16le")
    entrata[altera + 56:altera + 56 + len(nomen_voluminis)] = nomen_voluminis
    crc_entratarum = binascii.crc32(entrata) & 0xFFFFFFFF
    imago[2 * SECTOR:34 * SECTOR] = entrata
    imago[(SECTORES_TOTALES - 33) * SECTOR:(SECTORES_TOTALES - 1) * SECTOR] = entrata

    guid_disci = uuid.UUID("56494e44-4558-4155-4546-490000000041")

    def caput_gpt(hic: int, alter: int, lba_entratarum: int) -> bytes:
        h = bytearray(SECTOR)
        h[0:8] = b"EFI PART"
        u32(h, 8, 0x00010000)
        u32(h, 12, 92)
        u64(h, 24, hic)
        u64(h, 32, alter)
        u64(h, 40, 34)
        u64(h, 48, SECTORES_TOTALES - 34)
        h[56:72] = guid_disci.bytes_le
        u64(h, 72, lba_entratarum)
        u32(h, 80, 128)
        u32(h, 84, 128)
        u32(h, 88, crc_entratarum)
        u32(h, 16, binascii.crc32(h[:92]) & 0xFFFFFFFF)
        return bytes(h)

    imago[SECTOR:2 * SECTOR] = caput_gpt(1, SECTORES_TOTALES - 1, 2)
    imago[(SECTORES_TOTALES - 1) * SECTOR:] = caput_gpt(
        SECTORES_TOTALES - 1, 1, SECTORES_TOTALES - 33
    )

    pars = PARTITIO_INITIUM * SECTOR

    # Sector initialis FAT32.
    boot = bytearray(SECTOR)
    boot[0:3] = b"\xeb\x58\x90"
    boot[3:11] = b"VINDEX  "
    u16(boot, 11, SECTOR)
    boot[13] = sectores_per_botrum
    u16(boot, 14, reservati)
    boot[16] = numerus_fat
    u16(boot, 17, 0)
    u16(boot, 19, 0)
    boot[21] = 0xF8
    u16(boot, 22, 0)
    u16(boot, 24, 63)
    u16(boot, 26, 255)
    u32(boot, 28, PARTITIO_INITIUM)
    u32(boot, 32, PARTITIO_SECTORES)
    u32(boot, 36, sectores_fat)
    u16(boot, 40, 0)
    u16(boot, 42, 0)
    u32(boot, 44, 2)
    u16(boot, 48, 1)
    u16(boot, 50, 6)
    boot[64] = 0x80
    boot[66] = 0x29
    u32(boot, 67, 0x58444E56)
    boot[71:82] = b"VINDEX UEFI"
    boot[82:90] = b"FAT32   "
    boot[510:512] = b"\x55\xaa"
    imago[pars:pars + SECTOR] = boot
    imago[pars + 6 * SECTOR:pars + 7 * SECTOR] = boot

    fsinfo = bytearray(SECTOR)
    u32(fsinfo, 0, 0x41615252)
    u32(fsinfo, 484, 0x61417272)
    u32(fsinfo, 488, botri - si_occupati)
    u32(fsinfo, 492, ultimus_voluminis + 1)
    u32(fsinfo, 508, 0xAA550000)
    imago[pars + SECTOR:pars + 2 * SECTOR] = fsinfo
    imago[pars + 7 * SECTOR:pars + 8 * SECTOR] = fsinfo

    # Duae tabulae FAT identicae.
    fat = bytearray(sectores_fat * SECTOR)
    u32(fat, 0, 0x0FFFFFF8)
    u32(fat, 4, 0xFFFFFFFF)
    u32(fat, 8, 0x0FFFFFFF)   # radix
    u32(fat, 12, 0x0FFFFFFF)  # EFI
    u32(fat, 16, 0x0FFFFFFF)  # BOOT
    for botrus in range(primus_fasciculi, ultimus_fasciculi + 1):
        proximus = 0x0FFFFFFF if botrus == ultimus_fasciculi else botrus + 1
        u32(fat, botrus * 4, proximus)
    for botrus in range(primus_nuclei, ultimus_nuclei + 1):
        proximus = 0x0FFFFFFF if botrus == ultimus_nuclei else botrus + 1
        u32(fat, botrus * 4, proximus)
    for botrus in range(primus_textus, ultimus_textus + 1):
        proximus = 0x0FFFFFFF if botrus == ultimus_textus else botrus + 1
        u32(fat, botrus * 4, proximus)
    for botrus in range(primus_voluminis, ultimus_voluminis + 1):
        proximus = 0x0FFFFFFF if botrus == ultimus_voluminis else botrus + 1
        u32(fat, botrus * 4, proximus)
    fat1 = pars + reservati * SECTOR
    fat2 = fat1 + sectores_fat * SECTOR
    imago[fat1:fat1 + len(fat)] = fat
    imago[fat2:fat2 + len(fat)] = fat

    def locus_botri(botrus: int) -> int:
        sector_rel = data_initium + (botrus - 2) * sectores_per_botrum
        return pars + sector_rel * SECTOR

    radix = bytearray(SECTOR)
    radix[0:32] = ingressus_directorii(b"EFI        ", 0x10, 3)
    radix[32:64] = ingressus_directorii(
        b"VINDEX  FS ", 0x20, primus_voluminis, MENSURA_VOLUMINIS
    )
    if nucleus:
        radix[64:96] = ingressus_directorii(
            b"NUCLEUS BIN", 0x20, primus_nuclei, len(nucleus)
        )
    if textus:
        radix[96:128] = ingressus_directorii(
            b"TEXTUS  BIN", 0x20, primus_textus, len(textus)
        )
    imago[locus_botri(2):locus_botri(2) + SECTOR] = radix

    directorium_efi = bytearray(SECTOR)
    directorium_efi[0:32] = ingressus_directorii(b".          ", 0x10, 3)
    directorium_efi[32:64] = ingressus_directorii(b"..         ", 0x10, 2)
    directorium_efi[64:96] = ingressus_directorii(b"BOOT       ", 0x10, 4)
    imago[locus_botri(3):locus_botri(3) + SECTOR] = directorium_efi

    directorium_boot = bytearray(SECTOR)
    directorium_boot[0:32] = ingressus_directorii(b".          ", 0x10, 4)
    directorium_boot[32:64] = ingressus_directorii(b"..         ", 0x10, 3)
    directorium_boot[64:96] = ingressus_directorii(
        b"BOOTX64 EFI", 0x20, primus_fasciculi, len(efi)
    )
    imago[locus_botri(4):locus_botri(4) + SECTOR] = directorium_boot
    debut_efi = locus_botri(primus_fasciculi)
    imago[debut_efi:debut_efi + len(efi)] = efi
    if nucleus:
        debut_nuclei = locus_botri(primus_nuclei)
        imago[debut_nuclei:debut_nuclei + len(nucleus)] = nucleus
    if textus:
        debut_textus = locus_botri(primus_textus)
        imago[debut_textus:debut_textus + len(textus)] = textus

    # LBA 0 partitionis signum pontis habet; LBA 1..64 sunt volumen VINDEX.
    locus_voluminis = VOLUMEN_INITIUM * SECTOR
    imago[locus_voluminis:locus_voluminis + len(SIGNUM_VOLUMINIS)] = SIGNUM_VOLUMINIS
    u32(imago, locus_voluminis + 8, 1)
    u32(imago, locus_voluminis + 12, MENSURA_VOLUMINIS)

    via_imaginis.write_bytes(imago)
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
