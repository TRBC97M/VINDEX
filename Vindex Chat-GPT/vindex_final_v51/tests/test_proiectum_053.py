#!/usr/bin/env python3
"""Probationes R3: manifestum PROIECTUM, viae relativae et destinationes."""

from __future__ import annotations

import os
from pathlib import Path
import struct
import subprocess
import tempfile
import unittest

RADIX = Path(__file__).resolve().parents[1]
COMPILATOR = RADIX / "compilator_vindex"
PROIECTA = RADIX / "tests" / "proiecta"


class Proiectum053(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        os.chmod(COMPILATOR, 0o755)

    def exsequere_proiectum(self, manifestum: Path) -> tuple[int, str]:
        with tempfile.TemporaryDirectory(prefix="vindex-r3-cwd-") as temporarium:
            cursus = subprocess.run(
                [str(COMPILATOR), "PROIECTUM", str(manifestum.resolve())],
                cwd=temporarium,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=120,
                check=False,
            )
            return cursus.returncode, cursus.stdout

    def test_proiectum_elf_ex_directorio_alieno(self) -> None:
        locus = PROIECTA / "salve"
        manifestum = locus / "proiectum.vindex"
        productum = locus / "salve"
        productum.unlink(missing_ok=True)
        try:
            status, textus = self.exsequere_proiectum(manifestum)
            self.assertEqual(0, status, textus)
            self.assertTrue(productum.exists(), textus)
            os.chmod(productum, 0o755)
            cursus = subprocess.run(
                [str(productum)],
                cwd=RADIX,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=30,
                check=False,
            )
            self.assertEqual(0, cursus.returncode, cursus.stdout)
            self.assertIn("Salve, VINDEX!", cursus.stdout)
        finally:
            productum.unlink(missing_ok=True)

    def test_proiectum_pe_generat_pe32_plus(self) -> None:
        locus = PROIECTA / "salve"
        manifestum = locus / "proiectum_pe.vindex"
        productum = locus / "salve.exe"
        productum.unlink(missing_ok=True)
        try:
            status, textus = self.exsequere_proiectum(manifestum)
            self.assertEqual(0, status, textus)
            data = productum.read_bytes()
            self.assertGreaterEqual(len(data), 512)
            self.assertEqual(b"MZ", data[:2])
            pe_offset = struct.unpack_from("<I", data, 0x3C)[0]
            self.assertEqual(b"PE\0\0", data[pe_offset:pe_offset + 4])
        finally:
            productum.unlink(missing_ok=True)

    def test_manifestum_invalidum_diagnosticum_structuratum(self) -> None:
        manifestum = PROIECTA / "erratum" / "proiectum.vindex"
        status, textus = self.exsequere_proiectum(manifestum)
        self.assertNotEqual(0, status)
        lineae = [linea.rstrip("\r") for linea in textus.splitlines()]
        self.assertIn("DIAGNOSTICUM VINDEX", lineae, textus)
        self.assertIn("FONS", lineae, textus)
        self.assertIn(str(manifestum.resolve()), textus)
        self.assertIn("LINEA", lineae, textus)
        self.assertIn("4", lineae, textus)
        self.assertIn("COLUMNA", lineae, textus)
        self.assertIn("NUNTIUS", lineae, textus)
        self.assertIn("ERRATUM: proiectum VINDEX invalidum est", textus)


if __name__ == "__main__":
    unittest.main(verbosity=2)
