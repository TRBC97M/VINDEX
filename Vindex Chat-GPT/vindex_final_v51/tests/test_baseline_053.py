#!/usr/bin/env python3
"""Probationes R1: fundamenta 0.53 iam in linea canonica praesentia certificantur."""

from __future__ import annotations

import os
from pathlib import Path
import subprocess
import tempfile
import unittest

RADIX = Path(__file__).resolve().parents[1]
COMPILATOR = RADIX / "compilator_vindex"
FONS_COMPILATORIS = RADIX / "src" / "compilator_vindex.vindex"
CASUS = RADIX / "tests" / "casus"


class Baseline053(unittest.TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls) -> None:
        os.chmod(COMPILATOR, 0o755)

    def compila(self, fons: Path, exitus: Path, timeout: int = 180) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [str(COMPILATOR), str(fons), str(exitus)],
            cwd=RADIX,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )

    def compila_textum_et_exsequere(self, textus: str, exspectatum: str, timeout: int = 180) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-r1-") as temporarium:
            locus = Path(temporarium)
            fons = locus / "probatio.vindex"
            exitus = locus / "probatio"
            fons.write_text(textus, encoding="utf-8")

            relatio = self.compila(fons, exitus, timeout=timeout)
            self.assertEqual(0, relatio.returncode, relatio.stdout)
            self.assertTrue(exitus.is_file(), "compilator nullum exsecutabile creavit")
            os.chmod(exitus, 0o755)

            cursus = subprocess.run(
                [str(exitus)],
                cwd=RADIX,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=timeout,
                check=False,
            )
            self.assertEqual(0, cursus.returncode, cursus.stdout)
            self.assertEqual(exspectatum, cursus.stdout.strip())

    def test_argumenta_septem_sysv(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-r1-args-") as temporarium:
            exitus = Path(temporarium) / "argumenta_septem"
            relatio = self.compila(CASUS / "argumenta_septem.vindex", exitus)
            self.assertEqual(0, relatio.returncode, relatio.stdout)
            os.chmod(exitus, 0o755)
            cursus = subprocess.run(
                [str(exitus)],
                cwd=RADIX,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=60,
                check=False,
            )
            self.assertEqual(0, cursus.returncode, cursus.stdout)
            self.assertEqual("28", cursus.stdout.strip())

    def test_frame_plus_una_pagina(self) -> None:
        lineae = ["FUNCTIO PRINCIPALIS REDDENS NUMERUS."]
        for i in range(700):
            lineae.append(f"    DECLARA locus{i} SICUT NUMERUS VALENS {i}.")
        lineae.extend([
            "    PROCLAMA locus699.",
            "    REDDE 0.",
            "FIN-FUNCTIO.",
            "",
        ])
        self.compila_textum_et_exsequere("\n".join(lineae), "699", timeout=240)

    def test_multae_functiones_dynamicae(self) -> None:
        lineae: list[str] = []
        for i in range(320):
            lineae.extend([
                f"FUNCTIO F{i} REDDENS NUMERUS.",
                f"    REDDE {i}.",
                "FIN-FUNCTIO.",
                "",
            ])
        lineae.extend([
            "FUNCTIO PRINCIPALIS REDDENS NUMERUS.",
            "    PROCLAMA F319().",
            "    REDDE 0.",
            "FIN-FUNCTIO.",
            "",
        ])
        self.compila_textum_et_exsequere("\n".join(lineae), "319", timeout=240)

    def test_buffer_codicis_magnus(self) -> None:
        lineae = [
            "FUNCTIO PRINCIPALIS REDDENS NUMERUS.",
            "    DECLARA summa SICUT NUMERUS VALENS 0.",
        ]
        for _ in range(5000):
            lineae.append("    summa = summa + 1.")
        lineae.extend([
            "    PROCLAMA summa.",
            "    REDDE 0.",
            "FIN-FUNCTIO.",
            "",
        ])
        self.compila_textum_et_exsequere("\n".join(lineae), "5000", timeout=300)

    def test_fluitans_negativus(self) -> None:
        textus = """FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    DECLARA valor SICUT FLUITANS VALENS -1.25.
    PROCLAMA valor.
    REDDE 0.
FIN-FUNCTIO.
"""
        self.compila_textum_et_exsequere(textus, "-1.250000")

    def test_auto_hospitium_punctum_fixum(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-r1-selfhost-") as temporarium:
            locus = Path(temporarium)
            gen2 = locus / "compilator_gen2"
            gen3 = locus / "compilator_gen3"

            prima = self.compila(FONS_COMPILATORIS, gen2, timeout=300)
            self.assertEqual(0, prima.returncode, prima.stdout)
            os.chmod(gen2, 0o755)

            secunda = subprocess.run(
                [str(gen2), str(FONS_COMPILATORIS), str(gen3)],
                cwd=RADIX,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=300,
                check=False,
            )
            self.assertEqual(0, secunda.returncode, secunda.stdout)
            self.assertTrue(gen3.is_file())
            self.assertEqual(gen2.read_bytes(), gen3.read_bytes(), "generationes G2 et G3 differunt")


if __name__ == "__main__":
    unittest.main(verbosity=2)
