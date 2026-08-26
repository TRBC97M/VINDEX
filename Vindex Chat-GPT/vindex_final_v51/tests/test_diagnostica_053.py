#!/usr/bin/env python3
"""Probationes R2: diagnostica VINDEX fontem, lineam, columnam et nuntium servant."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import tempfile
import unittest

RADIX = Path(__file__).resolve().parents[1]
COMPILATOR = RADIX / "compilator_vindex"
CASUS = RADIX / "tests" / "casus"


class Diagnostica053(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        os.chmod(COMPILATOR, 0o755)

    def compila(self, fons: Path) -> tuple[int, str]:
        with tempfile.TemporaryDirectory(prefix="vindex-r2-") as temporarium:
            exitus = Path(temporarium) / "exitus"
            cursus = subprocess.run(
                [str(COMPILATOR), str(fons), str(exitus)],
                cwd=RADIX,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=120,
                check=False,
            )
            return cursus.returncode, cursus.stdout

    def exige_structuram(self, textus: str, fons: str, linea: int, columna: int, nuntius: str) -> None:
        lineae = [l.rstrip("\r") for l in textus.splitlines()]
        self.assertIn("DIAGNOSTICUM VINDEX", lineae, textus)
        self.assertIn("FONS", lineae, textus)
        self.assertIn(fons, textus, textus)
        self.assertIn("LINEA", lineae, textus)
        self.assertIn(str(linea), lineae, textus)
        self.assertIn("COLUMNA", lineae, textus)
        self.assertIn(str(columna), lineae, textus)
        self.assertIn("NUNTIUS", lineae, textus)
        self.assertIn(nuntius, textus, textus)

    def test_instructio_ignota(self) -> None:
        fons = CASUS / "erratum_instructio.vindex"
        status, textus = self.compila(fons)
        self.assertNotEqual(0, status)
        self.exige_structuram(
            textus,
            str(fons),
            2,
            5,
            "ERRATUM: instructio ignota est",
        )

    def test_functio_ignota(self) -> None:
        fons = CASUS / "erratum_functio.vindex"
        status, textus = self.compila(fons)
        self.assertNotEqual(0, status)
        self.exige_structuram(
            textus,
            str(fons),
            2,
            11,
            "ERRATUM: functio vocata non inventa est",
        )

    def test_principalis_deest(self) -> None:
        fons = CASUS / "erratum_principalis.vindex"
        status, textus = self.compila(fons)
        self.assertNotEqual(0, status)
        self.exige_structuram(
            textus,
            str(fons),
            1,
            1,
            "ERRATUM: FUNCTIO PRINCIPALIS deest",
        )

    def test_error_importatus_ad_fontem_verum_refertur(self) -> None:
        fons = CASUS / "erratum_importatum.vindex"
        status, textus = self.compila(fons)
        self.assertNotEqual(0, status)
        self.exige_structuram(
            textus,
            "tests/casus/erratum_bibliotheca.vindex",
            2,
            11,
            "ERRATUM: functio vocata non inventa est",
        )

    def test_importum_absens_ad_locum_principalem_refertur(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-r2-import-") as temporarium:
            locus = Path(temporarium)
            fons = locus / "importum_absens.vindex"
            fons.write_text(
                'IMPORTA "fasciculus_qui_non_est.vindex".\n\n'
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    REDDE 0.\n'
                'FIN-FUNCTIO.\n',
                encoding="utf-8",
            )
            status, textus = self.compila(fons)
            self.assertNotEqual(0, status)
            self.exige_structuram(
                textus,
                str(fons),
                1,
                1,
                "ERRATUM: fons importatus aperiri non potest",
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
