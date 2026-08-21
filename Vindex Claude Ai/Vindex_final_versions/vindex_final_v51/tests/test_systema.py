#!/usr/bin/env python3
"""Probationes imaginis bare-metal VINDEX Systema."""

from __future__ import annotations

import binascii
import shutil
import struct
import subprocess
import tempfile
import time
import unittest
from pathlib import Path


RADIX = Path(__file__).resolve().parent.parent
COMPILATOR = RADIX / "compilator_vindex"
FONS = RADIX / "systema/nucleus.vindex"
CONSTRUCTOR = RADIX / "systema/construe_systema.sh"
NUCLEUS = RADIX / "nucleus_systema.elf"
BOOT = RADIX / "boot_systema.bin"
TEXTUS = RADIX / "fenestrale_systema.bin"
RECTORES = RADIX / "rectores_systema.bin"
IMAGO = RADIX / "systema_vindex.img"
UEFI = RADIX / "BOOTX64.EFI"
IMAGO_UEFI = RADIX / "systema_vindex_uefi.img"
CONSTRUCTOR_UEFI = RADIX / "systema/uefi/construe_uefi.sh"
FORMA_UEFI = RADIX / "systema/uefi/forma.bin"
GENERATOR_FORMAE = RADIX / "systema/uefi/genera_formam.py"
PROBA_VOLUMINIS = RADIX / "tests/proba_voluminis.c"
INITIATOR = RADIX / "vindex-systema"


def descriptio_elf(data: bytes) -> dict[str, int]:
    if data[:4] != b"\x7fELF" or data[4] != 2 or data[5] != 1:
        raise AssertionError("nucleus non est ELF64 parvi ordinis")
    phoff = struct.unpack_from("<Q", data, 32)[0]
    phentsize = struct.unpack_from("<H", data, 54)[0]
    phnum = struct.unpack_from("<H", data, 56)[0]
    if phnum != 1 or phentsize != 56:
        raise AssertionError("nucleus unum segmentum habere debet")
    return {
        "machina": struct.unpack_from("<H", data, 18)[0],
        "initium": struct.unpack_from("<Q", data, 24)[0],
        "typus": struct.unpack_from("<I", data, phoff)[0],
        "offset": struct.unpack_from("<Q", data, phoff + 8)[0],
        "virtualis": struct.unpack_from("<Q", data, phoff + 16)[0],
        "archivi": struct.unpack_from("<Q", data, phoff + 32)[0],
        "memoriae": struct.unpack_from("<Q", data, phoff + 40)[0],
    }


class SystemaTests(unittest.TestCase):
    def test_volumen_crudum_scribit_expurgat_relegit_et_initium_novum_superat(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-volumen-") as directory:
            exsecutabile = Path(directory) / "proba-voluminis"
            compilatio = subprocess.run(
                ["cc", "-std=c11", "-O2", "-Wall", "-Wextra", "-Werror",
                 "-fshort-wchar",
                 str(PROBA_VOLUMINIS), "-o", str(exsecutabile)],
                cwd=RADIX, text=True, capture_output=True, timeout=20, check=False,
            )
            self.assertEqual(compilatio.returncode, 0,
                             compilatio.stdout + compilatio.stderr)
            proba = subprocess.run(
                [str(exsecutabile)], cwd=RADIX, text=True, capture_output=True,
                timeout=10, check=False,
            )
            self.assertEqual(proba.returncode, 0, proba.stdout + proba.stderr)
            self.assertIn("volumen post initium novum permanet", proba.stdout)

    def test_nucleus_vindex_binarum_distributum_reproducit(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-nucleus-") as directory:
            exitus = Path(directory) / "nucleus.elf"
            completed = subprocess.run(
                [str(COMPILATOR), str(FONS), str(exitus)],
                cwd=RADIX,
                text=True,
                capture_output=True,
                timeout=20,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            self.assertEqual(exitus.read_bytes(), NUCLEUS.read_bytes())

    def test_nucleus_est_elf_x86_64_ad_basim_quattuor_mib(self) -> None:
        data = NUCLEUS.read_bytes()
        elf = descriptio_elf(data)
        self.assertEqual(elf["machina"], 62)
        self.assertEqual(elf["typus"], 1)
        self.assertEqual(elf["offset"], 0)
        self.assertEqual(elf["virtualis"], 0x400000)
        self.assertEqual(elf["archivi"], len(data))
        self.assertLessEqual(len(data), 122880)
        self.assertLess(elf["virtualis"], elf["initium"])
        self.assertLess(elf["initium"], elf["virtualis"] + elf["archivi"])
        self.assertIn(struct.pack("<Q", 0xA0000), data)
        self.assertIn(struct.pack("<Q", 0x8000), data)
        self.assertIn(struct.pack("<Q", 0x41E000), data)

    def test_sector_initialis_bios_et_transitus_longus_recti_sunt(self) -> None:
        boot = BOOT.read_bytes()
        self.assertEqual(len(boot), 512)
        self.assertEqual(boot[510:], b"\x55\xaa")
        self.assertIn(b"\x0f\x22\xe0", boot)  # CR4
        self.assertIn(b"\x0f\x30", boot)      # EFER
        self.assertIn(b"\x0f\x22\xd8", boot)  # CR3
        self.assertIn(b"\xb8\x30\x11\xb7\x03\xcd\x10", boot)  # forma 8x8
        self.assertIn(b"\xb8\x13\x00\xcd\x10", boot)  # modus VGA 13h
        self.assertIn(struct.pack("<I", 0x41F000), boot)
        self.assertGreaterEqual(boot.count(b"\x78\x00"), 2)  # binae partes 120 sectorum
        self.assertGreaterEqual(boot.count(b"\x08\x00"), 2)  # duae partes extremae
        self.assertIn(b"ERRATUM DISCUS", boot)

    def test_textus_fenestralis_totus_latine_distributus_est(self) -> None:
        textus = TEXTUS.read_bytes()
        for titulus in (
            b"VINDEX FENESTRALE XCV",
            b"INITIUM",
            b"SCRIPTOR",
            b"SERPENS",
            b"FASCICULUS  EDITIO  AUXILIUM",
            b"VINDEX SCRIPTOR",
            b"VINDEX SERPENS",
            b"FASCICULI",
            b"VINDEX FASCICULI",
            b"SCRIPTUM.TXT",
            b"SERVA",
            b"APERI",
            b"SERVATUM",
            b"APERTUM",
            b"PARTITIO",
            b"SUBSIDIUM",
            b"NOVUM",
            b"NOMEN",
            b"DELE",
            b"CONFIRMA",
            b"REVOCA",
            b"VOLUMEN PLENUM",
            b"CLAUDE",
            b"SCRIBE HIC",
            b"PUNCTA",
            b"FINIS LUDI",
            b"PREME SPATIUM",
            b"SAGITTAE MOVENT",
            b"DELE FASCICULUM?",
            b"SCRIPTOR II",
            b"PROGRAMMATA",
            b"VINDEX PROGRAMMATA",
            b"NOMEN PROGRAMMATIS",
            b".VXNAT",
            b"VINDEX NATIVUM",
            b"PROGRAMMA ERRATUM",
            b"PROGRAMMA TABULA",
            b"RECTANGULUM 16 14 220 58 1",
            b"MARGO 12 10 228 66 0",
            b"LOCUS 32 28",
            b"DELE PROGRAMMA?",
            b"PROGRAMMA SALVE",
            b"SCRIBE SALVE E VINDEX",
            b"VINDEX 0.51",
        ):
            self.assertIn(titulus, textus)

    def test_rectores_ps2_interruptiones_et_statum_communem_continent(self) -> None:
        rectores = RECTORES.read_bytes()
        fons = (RADIX / "systema/rectores.S").read_text(encoding="utf-8")
        self.assertLessEqual(len(rectores), 4096)
        self.assertIn(b"\x48\xcf", rectores)  # IRETQ
        self.assertIn("interruptio_clavis", fons)
        self.assertIn("interruptio_muris", fons)
        self.assertIn("in al, 0x60", fons)
        self.assertIn("out 0x64, al", fons)
        self.assertIn("mov qword ptr [0x3000000], 160", fons)
        self.assertIn("inc qword ptr [0x3000018]", fons)
        self.assertIn("interruptio_temporis", fons)
        self.assertIn("inc qword ptr [0x3000050]", fons)
        self.assertIn("mov byte ptr [rdx + 0x3000300], al", fons)

    def test_applicatio_uefi_est_pe32_plus_x86_64(self) -> None:
        data = UEFI.read_bytes()
        self.assertEqual(data[:2], b"MZ")
        pe = struct.unpack_from("<I", data, 0x3C)[0]
        self.assertEqual(data[pe:pe + 4], b"PE\0\0")
        self.assertEqual(struct.unpack_from("<H", data, pe + 4)[0], 0x8664)
        optionalis = pe + 24
        self.assertEqual(struct.unpack_from("<H", data, optionalis)[0], 0x20B)
        self.assertNotEqual(struct.unpack_from("<I", data, optionalis + 16)[0], 0)
        self.assertEqual(struct.unpack_from("<H", data, optionalis + 68)[0], 10)

    def test_forma_uefi_clara_et_duplex_tabula_sunt(self) -> None:
        forma = FORMA_UEFI.read_bytes()
        fons = (RADIX / "systema/uefi/firmamentum_uefi.c").read_text(encoding="utf-8")
        fons_formae = GENERATOR_FORMAE.read_text(encoding="utf-8")
        self.assertEqual(len(forma), 256 * 8)
        for littera in b"VINDEXSCRIPTORSERPENS":
            glyphus = forma[littera * 8:(littera + 1) * 8]
            self.assertGreaterEqual(sum(octetum != 0 for octetum in glyphus), 6)
        self.assertEqual(forma[65 * 8:66 * 8],
                         bytes((0x30, 0x78, 0xCC, 0xCC, 0xFC, 0xCC, 0xCC, 0)))
        self.assertIn("FORMAE_HEX", fons_formae)
        self.assertNotIn("PIL", fons_formae)
        with tempfile.TemporaryDirectory(prefix="vindex-forma-") as directory:
            exitus = Path(directory) / "forma.bin"
            subprocess.run(["python3", str(GENERATOR_FORMAE), str(exitus)],
                           cwd=RADIX, check=True, timeout=10)
            self.assertEqual(exitus.read_bytes(), forma)
        self.assertIn("static U64 umbram_signa(void)", fons)
        self.assertIn("static void imaginem_praesenta(void)", fons)
        self.assertIn("tabula_pixelorum", fons)
        self.assertNotIn("g->Blt(", fons)
        self.assertIn("FrameBufferBase", fons)
        self.assertIn("memoria_copia(destinatio", fons)
        self.assertIn("AllocatePages(0, 2", fons)
        self.assertIn("meta[7] = 0", fons)
        self.assertIn("muri_statum_para", fons)
        self.assertIn("muri_statum_confirma", fons)
        self.assertIn("communis[10] - tempus_bullarum >= 2", fons)
        self.assertIn("EFI_SIMPLE_FILE_SYSTEM_PROTOCOL", fons)
        self.assertIn("EFI_FILE_PROTOCOL", fons)
        self.assertIn('L"VINDEX.FS"', fons)
        self.assertIn("TABULA_FS", fons)
        self.assertIn("MENSURA_FS 32768", fons)
        self.assertIn("volumen_lege", fons)
        self.assertIn("volumen_scribe", fons)
        self.assertIn("mandatum_voluminis_exsequere", fons)
        self.assertIn("meta[12]", fons)
        self.assertIn("meta[13]", fons)
        self.assertIn("meta[14]", fons)
        self.assertIn("meta[15]", fons)
        self.assertIn("EFI_BLOCK_IO_PROTOCOL", fons)
        self.assertIn("LocateHandleBuffer", fons)
        self.assertIn("guid_blocalis", fons)
        self.assertIn("volumen_crudum_inveni", fons)
        self.assertIn("volumen_crudum_scribe", fons)
        self.assertIn("WriteBlocks", fons)
        self.assertIn("FlushBlocks", fons)
        self.assertIn("memoria_signa", fons)
        self.assertIn("static const U8 signum[8]", fons)
        self.assertIn("{'V','I','N','D','E','X','V','0'}", fons)

    def test_imago_uefi_gpt_fat32_et_bootx64_continet(self) -> None:
        imago = IMAGO_UEFI.read_bytes()
        efi = UEFI.read_bytes()
        self.assertEqual(len(imago), 64 * 1024 * 1024)
        self.assertEqual(imago[510:512], b"\x55\xaa")
        self.assertEqual(imago[446 + 4], 0xEE)

        caput = bytearray(imago[512:1024])
        self.assertEqual(caput[:8], b"EFI PART")
        mensura_capitis = struct.unpack_from("<I", caput, 12)[0]
        crc_capitis = struct.unpack_from("<I", caput, 16)[0]
        struct.pack_into("<I", caput, 16, 0)
        self.assertEqual(binascii.crc32(caput[:mensura_capitis]) & 0xFFFFFFFF,
                         crc_capitis)

        lba_entratarum = struct.unpack_from("<Q", caput, 72)[0]
        numerus_entratarum = struct.unpack_from("<I", caput, 80)[0]
        mensura_entratae = struct.unpack_from("<I", caput, 84)[0]
        crc_entratarum = struct.unpack_from("<I", caput, 88)[0]
        initium = lba_entratarum * 512
        finis = initium + numerus_entratarum * mensura_entratae
        self.assertEqual(binascii.crc32(imago[initium:finis]) & 0xFFFFFFFF,
                         crc_entratarum)

        altera = initium + mensura_entratae
        self.assertNotEqual(imago[altera:altera + 16], b"\0" * 16)
        initium_voluminis = struct.unpack_from("<Q", imago, altera + 32)[0]
        finis_voluminis = struct.unpack_from("<Q", imago, altera + 40)[0]
        self.assertEqual(initium_voluminis, 129024)
        self.assertEqual(finis_voluminis, 131038)
        nomen_voluminis = imago[altera + 56:altera + 128].decode("utf-16le").rstrip("\0")
        self.assertEqual(nomen_voluminis, "VINDEX VOLUMEN")
        locus_crudus = initium_voluminis * 512
        self.assertEqual(imago[locus_crudus:locus_crudus + 8], b"VINDEXV0")
        self.assertEqual(struct.unpack_from("<I", imago, locus_crudus + 8)[0], 1)
        self.assertEqual(struct.unpack_from("<I", imago, locus_crudus + 12)[0], 32768)
        self.assertEqual(imago[locus_crudus + 512:locus_crudus + 512 + 32768],
                         b"\0" * 32768)

        pars = struct.unpack_from("<Q", imago, initium + 32)[0]
        boot = imago[pars * 512:(pars + 1) * 512]
        self.assertEqual(boot[510:512], b"\x55\xaa")
        self.assertEqual(boot[82:90], b"FAT32   ")
        self.assertEqual(boot[71:82], b"VINDEX UEFI")
        reservati = struct.unpack_from("<H", boot, 14)[0]
        numerus_fat = boot[16]
        sectores_fat = struct.unpack_from("<I", boot, 36)[0]
        data_lba = pars + reservati + numerus_fat * sectores_fat
        directorium_radix = imago[data_lba * 512:(data_lba + 1) * 512]
        self.assertEqual(directorium_radix[32:43], b"VINDEX  FS ")
        botrus_voluminis = struct.unpack_from("<H", directorium_radix, 32 + 26)[0]
        mensura_voluminis = struct.unpack_from("<I", directorium_radix, 32 + 28)[0]
        self.assertEqual(mensura_voluminis, 32768)
        locus_voluminis = (data_lba + botrus_voluminis - 2) * 512
        self.assertEqual(imago[locus_voluminis:locus_voluminis + 32768], b"\0" * 32768)
        boot_directorium = imago[(data_lba + 2) * 512:(data_lba + 3) * 512]
        self.assertEqual(boot_directorium[64:75], b"BOOTX64 EFI")
        botrus = struct.unpack_from("<H", boot_directorium, 64 + 26)[0]
        mensura = struct.unpack_from("<I", boot_directorium, 64 + 28)[0]
        self.assertEqual(mensura, len(efi))
        locus = (data_lba + botrus - 2) * 512
        self.assertEqual(imago[locus:locus + len(efi)], efi)

    def test_imago_continet_boot_et_nucleum(self) -> None:
        imago = IMAGO.read_bytes()
        boot = BOOT.read_bytes()
        nucleus = NUCLEUS.read_bytes()
        textus = TEXTUS.read_bytes()
        rectores = RECTORES.read_bytes()
        self.assertEqual(len(imago), 1048576)
        self.assertEqual(imago[:512], boot)
        self.assertEqual(imago[512 : 512 + len(nucleus)], nucleus)
        self.assertEqual(imago[512 + len(nucleus) : 512 + 122880],
                         b"\0" * (122880 - len(nucleus)))
        self.assertEqual(imago[512 + 122880 : 512 + 122880 + len(textus)], textus)
        self.assertEqual(imago[512 + 122880 + len(textus) : 512 + 126976],
                         b"\0" * (4096 - len(textus)))
        self.assertEqual(imago[512 + 126976 : 512 + 126976 + len(rectores)], rectores)
        self.assertEqual(imago[512 + 126976 + len(rectores) : 512 + 131072],
                         b"\0" * (4096 - len(rectores)))

    def test_reconstructio_imaginem_identicam_creat(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-systema-reconstructio-") as directory:
            temporarium = Path(directory)
            imago = temporarium / "systema.img"
            nucleus = temporarium / "nucleus.elf"
            boot = temporarium / "boot.bin"
            textus = temporarium / "textus.bin"
            rectores = temporarium / "rectores.bin"
            completed = subprocess.run(
                [str(CONSTRUCTOR), str(imago), str(nucleus), str(boot), str(textus),
                 str(rectores)],
                cwd=RADIX,
                text=True,
                capture_output=True,
                timeout=30,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            self.assertEqual(imago.read_bytes(), IMAGO.read_bytes())
            self.assertEqual(nucleus.read_bytes(), NUCLEUS.read_bytes())
            self.assertEqual(boot.read_bytes(), BOOT.read_bytes())
            self.assertEqual(textus.read_bytes(), TEXTUS.read_bytes())
            self.assertEqual(rectores.read_bytes(), RECTORES.read_bytes())

    def test_reconstructio_uefi_imaginem_identicam_creat(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-uefi-reconstructio-") as directory:
            temporarium = Path(directory)
            imago = temporarium / "systema_uefi.img"
            applicatio = temporarium / "BOOTX64.EFI"
            completed = subprocess.run(
                [str(CONSTRUCTOR_UEFI), str(imago), str(applicatio)],
                cwd=RADIX,
                text=True,
                capture_output=True,
                timeout=30,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            self.assertEqual(applicatio.read_bytes(), UEFI.read_bytes())
            self.assertEqual(imago.read_bytes(), IMAGO_UEFI.read_bytes())

    def test_fons_et_initiator_linux_non_simulant(self) -> None:
        fons = FONS.read_text(encoding="utf-8")
        initiator = INITIATOR.read_text(encoding="utf-8")
        self.assertIn("SCRIBE_OCTETUM_AB", fons)
        self.assertIn("655360", fons)
        self.assertIn("32768", fons)
        self.assertIn("4317184", fons)
        self.assertIn("CONTENTUM(50331648)", fons)
        self.assertIn("CONTENTUM(50331712)", fons)
        self.assertIn("CONTENTUM(50331728)", fons)
        self.assertIn("POLLE()", fons)
        self.assertIn("PIXEL_SCRIBE", fons)
        self.assertIn("FUNDUM_CURS_RESTITUE", fons)
        self.assertIn("SCRIPTOR_SCRIBE", fons)
        self.assertIn("SERPENS_SCRIBE", fons)
        self.assertIn("FASCICULI_SCRIBE", fons)
        self.assertIn("VOLUMEN_VALIDUM", fons)
        self.assertIn("VOLUMEN_NUMERA", fons)
        self.assertIn("FASCICULUM_LEGE", fons)
        self.assertIn("FASCICULUM_SCRIBE", fons)
        self.assertIn("nomen_modus", fons)
        self.assertIn("i < 6", fons)
        self.assertIn("6000580608039733590", fons)
        self.assertIn("CONTENTUM(50333800) = 1", fons)
        self.assertIn("CONTENTUM(50333800) = 2", fons)
        self.assertIn("tractio", fons)
        self.assertIn("OCTETUS_AB(50332416", fons)
        for vetitum in ("PROCLAMA", "CURRE(", "EXSEQUERE(", "APERI_"):
            self.assertNotIn(vetitum, fons)
        self.assertIn("format=raw", initiator)
        self.assertIn("if=ide", initiator)
        self.assertNotIn("-kernel", initiator)

    def test_functiones_nuclei_sex_parametros_non_excedunt(self) -> None:
        fons = FONS.read_text(encoding="utf-8")
        nomen = ""
        numerus = 0
        for linea in fons.splitlines():
            linea = linea.strip()
            if linea.startswith("FUNCTIO "):
                nomen = linea.split()[1]
                numerus = 0
            elif nomen and linea.startswith("ACCIPIT "):
                numerus += 1
            elif nomen and linea == "FIN-FUNCTIO.":
                self.assertLessEqual(numerus, 6, f"{nomen}: {numerus} parametra")
                nomen = ""
        self.assertIn(
            "FASCICULI_SCRIBE(fenestra_x, fenestra_y, fasciculus_electus, "
            "nomen_modus, nomen_editor, longitudo_nominis).",
            fons,
        )

    def test_fasciculi_fasciculum_electum_directe_aperiunt(self) -> None:
        fons = FONS.read_text(encoding="utf-8")
        initium = fons.index("SI actio_fasciculi == 1 TUNC")
        finis = fons.index("SI actio_fasciculi == 2 TUNC", initium)
        actio = fons[initium:finis]
        self.assertIn("FASCICULUM_LEGE(fasciculus_activus, editor)", actio)
        self.assertIn("modus = 1", actio)
        self.assertNotIn("VOLUMEN_RELEGE", actio)

    def test_scriptor_secundus_cursor_volumen_et_deletionem_tutam_habet(self) -> None:
        fons = FONS.read_text(encoding="utf-8")
        uefi = (RADIX / "systema/uefi/firmamentum_uefi.c").read_text(encoding="utf-8")
        self.assertIn("CAPACITAS 4096", fons)
        self.assertIn("longitudo_editoris < limes_scriptura", fons)
        self.assertIn("FASCICULUM_LIMES(fasciculus_activus)", fons)
        self.assertIn("indice * 4096", fons)
        self.assertIn("(indice - 6) * 1280", fons)
        self.assertIn("50426368", fons)
        self.assertIn("CONTENTUM(50401288) == 4", fons)
        self.assertIn("CONTENTUM(50401296) == 12", fons)
        self.assertIn("CONTENTUM(50401288) == 3", fons)
        self.assertIn("VOLUMEN_TERTIUM_VALIDUM", fons)
        self.assertIn("CONTENTUM(50401288) == 2", fons)
        self.assertIn("VOLUMEN_SECUNDUM_VALIDUM", fons)
        self.assertIn("SI migratio == 1 TUNC factum = VOLUMEN_SERVA()", fons)
        self.assertIn("CURSOR_LINEA", fons)
        self.assertIn("CURSOR_COLUMNA", fons)
        self.assertIn("CURSOR_LOCUS", fons)
        self.assertIn("prima_linea", fons)
        self.assertIn("cursor_editoris = CURSOR_LOCUS", fons)
        self.assertIn("CONTENTUM(50333840) = fasciculus_activus", fons)
        self.assertIn("dele_modus = 1", fons)
        self.assertIn("CONTENTUM(50333848) = dele_modus", fons)
        self.assertIn("clavis.ScanCode == 9", uefi)
        self.assertIn("clavis.ScanCode == 10", uefi)

    def test_programmata_vxnat_graphica_directe_exsequuntur(self) -> None:
        fons = FONS.read_text(encoding="utf-8")
        self.assertIn("FASCICULUM_VXNAT", fons)
        self.assertIn("PROGRAMMATA_SCRIBE", fons)
        self.assertIn("PROGRAMMA_SCRIBE", fons)
        self.assertIn("actio_programmatis", fons)
        self.assertIn("nomen_genus = 1", fons)
        self.assertIn("OCTETUS_AB(4318176 + longitudo_editoris) != 0", fons)
        self.assertIn("PROGRAMMATA_EXEMPLA_PARA", fons)
        self.assertIn("PROGRAMMA_EXEMPLUM_PONE", fons)
        self.assertIn("DECLARA i SICUT NUMERUS VALENS 6", fons)
        self.assertIn("DUM i < 12", fons)
        self.assertIn("linea_programmatis SICUT NUMERUS VALENS 6 +", fons)
        self.assertIn("ORDINEM_PARTEM_SCRIBE", fons)
        self.assertIn("textus[initium + i]", fons)
        self.assertNotIn("textus + initium + 7", fons)
        self.assertIn("textus[initium] == 83", fons)  # SCRIBE
        self.assertIn("textus[initium] == 67", fons)  # COLOR
        self.assertIn("LINEAE_NUMERUM", fons)
        self.assertIn("rect_w", fons)
        self.assertIn("margo_w", fons)
        self.assertIn("locus_x", fons)
        self.assertIn("i = longitudo", fons)  # FINIS
        self.assertIn("finis - initium == 7 || finis - initium == 8", fons)
        self.assertIn("modus = 5", fons)
        self.assertIn("SI modus == 4 TUNC", fons)
        self.assertIn("SI modus == 5 TUNC", fons)
        self.assertIn("FASCICULUM_LEGE(fasciculus_activus, editor)", fons)

    @unittest.skipUnless(shutil.which("qemu-system-x86_64"), "QEMU deest")
    def test_qemu_nucleum_sine_triplici_errato_retinet(self) -> None:
        processus = subprocess.Popen(
            [str(INITIATOR), "-display", "none", "-serial", "none", "-no-reboot"],
            cwd=RADIX,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        try:
            time.sleep(1.5)
            statutus = processus.poll()
            if statutus is not None:
                self.fail(processus.stderr.read() if processus.stderr else "")
        finally:
            processus.terminate()
            try:
                processus.wait(timeout=3)
            except subprocess.TimeoutExpired:
                processus.kill()
                processus.wait(timeout=3)
            if processus.stderr:
                processus.stderr.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
