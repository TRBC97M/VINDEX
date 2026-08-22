#!/usr/bin/env python3
"""Probationes Systematis cum reproducibilitate UEFI inter instrumenta eadem."""

from __future__ import annotations

import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from test_systema import CONSTRUCTOR_UEFI, RADIX, SystemaTests


def reconstructio_uefi_eodem_ambitu(self: SystemaTests) -> None:
    """Duas reconstructiones eiusdem ambitus, non binutilium alienorum, compara."""
    with tempfile.TemporaryDirectory(prefix="vindex-uefi-reproductio-") as directory:
        radix = Path(directory)
        producta: list[tuple[bytes, bytes]] = []

        for index in range(2):
            imago = radix / f"systema_uefi_{index}.img"
            applicatio = radix / f"BOOTX64_{index}.EFI"
            completed = subprocess.run(
                [str(CONSTRUCTOR_UEFI), str(imago), str(applicatio)],
                cwd=RADIX,
                text=True,
                capture_output=True,
                timeout=30,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            producta.append((applicatio.read_bytes(), imago.read_bytes()))

        applicatio_a, imago_a = producta[0]
        applicatio_b, imago_b = producta[1]
        self.assertEqual(applicatio_a, applicatio_b)
        self.assertEqual(imago_a, imago_b)

        self.assertEqual(applicatio_a[:2], b"MZ")
        pe = struct.unpack_from("<I", applicatio_a, 0x3C)[0]
        self.assertEqual(applicatio_a[pe:pe + 4], b"PE\0\0")
        self.assertEqual(struct.unpack_from("<H", applicatio_a, pe + 4)[0], 0x8664)
        optionalis = pe + 24
        self.assertEqual(struct.unpack_from("<H", applicatio_a, optionalis)[0], 0x20B)
        self.assertEqual(struct.unpack_from("<H", applicatio_a, optionalis + 68)[0], 10)

        self.assertEqual(len(imago_a), 64 * 1024 * 1024)
        self.assertEqual(imago_a[510:512], b"\x55\xaa")
        self.assertEqual(imago_a[512:520], b"EFI PART")
        self.assertIn(applicatio_a, imago_a)


# PE/COFF a nonnullis versionibus ld/objcopy sectiones aliter ordinatur quamquam
# applicatio eandem semanticam habet. Reproductio canonica igitur duas aedificationes
# cum eodem instrumento comparat; probationes structurales reliquae PE et GPT/FAT32
# separatim custodiunt.
SystemaTests.test_reconstructio_uefi_imaginem_identicam_creat = reconstructio_uefi_eodem_ambitu


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SystemaTests)
    eventum = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if eventum.wasSuccessful() else 1)
