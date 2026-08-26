#!/usr/bin/env python3
"""Probationes R5: verificator intrinseca canonica agnoscit sine disciplina minuenda."""

from __future__ import annotations

from pathlib import Path
import subprocess
import tempfile
import unittest

RADIX = Path(__file__).resolve().parents[1]
VERIFICATOR = RADIX / "instrumenta" / "vindex_verifica.py"


class VerificatorR5(unittest.TestCase):
    def verifica(self, textus: str) -> tuple[int, str]:
        with tempfile.TemporaryDirectory(prefix="vindex-r5-verificator-") as temporarium:
            fons = Path(temporarium) / "proba.vindex"
            fons.write_text(textus, encoding="utf-8")
            cursus = subprocess.run(
                ["python3", str(VERIFICATOR), str(fons)],
                cwd=RADIX,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                check=False,
            )
            return cursus.returncode, cursus.stdout

    def test_uefi_voca6_et_redde_parenthesibus_accipiuntur(self) -> None:
        status, textus = self.verifica(
            "FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n"
            "    DECLARA exitus SICUT NUMERUS VALENS UEFI_VOCA6(1, 2, 3, 4, 5, 6, 7).\n"
            "    REDDE (exitus).\n"
            "FIN-FUNCTIO.\n"
        )
        self.assertEqual(0, status, textus)
        self.assertIn("VINDEX: verificatio perfecta", textus)

    def test_reserva_octeta_intrinsecum_accipitur(self) -> None:
        status, textus = self.verifica(
            "FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n"
            "    DECLARA memoria SICUT NUMERUS VALENS RESERVA_OCTETA(64).\n"
            "    REDDE memoria.\n"
            "FIN-FUNCTIO.\n"
        )
        self.assertEqual(0, status, textus)
        self.assertIn("VINDEX: verificatio perfecta", textus)

    def test_functio_revera_ignota_reicitur(self) -> None:
        status, textus = self.verifica(
            "FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n"
            "    REDDE FUNCTIO_IGNOTA(1).\n"
            "FIN-FUNCTIO.\n"
        )
        self.assertNotEqual(0, status, textus)
        self.assertIn("functio 'FUNCTIO_IGNOTA' non definita", textus)


if __name__ == "__main__":
    unittest.main(verbosity=2)
