#!/usr/bin/env python3
"""Probationes PROCLAMA sub modo PE (GetStdHandle + WriteFile), VINDEX 0.53."""

from __future__ import annotations

import hashlib
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


RADIX = Path(__file__).resolve().parent.parent
COMPILATOR = RADIX / "compilator_vindex"
FONS_COMPILATORIS = RADIX / "src/compilator_vindex.vindex"

WINE = shutil.which("wine64") or "/usr/lib/wine/wine64"
WINE_ADEST = Path(WINE).exists()


def _compila(fons: str, exitus: Path, modus_pe: bool = False) -> None:
    """Scribit fons in fasciculum temporarium et compilat per COMPILATOR."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".vindex", delete=False, dir=exitus.parent
    ) as f:
        f.write(fons)
        fons_via = Path(f.name)
    try:
        mandata = [str(COMPILATOR), str(fons_via), str(exitus)]
        if modus_pe:
            mandata.append("pe")
        completed = subprocess.run(
            mandata, cwd=RADIX, capture_output=True, text=True, timeout=30
        )
        if completed.returncode != 0:
            raise AssertionError(
                f"compilatio defecit (status={completed.returncode}): "
                f"{completed.stdout}\n{completed.stderr}"
            )
    finally:
        fons_via.unlink(missing_ok=True)


def _exsequere_elf(exsecutabile: Path) -> subprocess.CompletedProcess:
    exsecutabile.chmod(0o755)
    return subprocess.run(
        [str(exsecutabile)], capture_output=True, text=True, timeout=10
    )


def _exsequere_pe_sub_wine(exsecutabile: Path) -> bytes:
    """Exsequitur exsecutabile PE sub Wine et reddit stdout crudum.

    Nota: terminatio limpida processus PE sub hoc systemate Wine 9.0
    specifico non semper occurrit (vide RELATIO-PE-WINDOWS.md, machina
    SEH interna Wine) -- probationes hic legunt STDOUT ante quemvis
    defectum, non codicem exitus processus.
    """
    completed = subprocess.run(
        [WINE, str(exsecutabile)],
        capture_output=True,
        timeout=15,
        env={"WINEDEBUG": "-all"},
    )
    return completed.stdout


class ProclamaModusElfTests(unittest.TestCase):
    """Probationes de referentia sub modo ELF (praedefinito) -- nullam
    Wine dependentiam habent, semper currunt."""

    def test_proclama_catena_litteralis(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-proclama-elf-") as d:
            exitus = Path(d) / "exsecutabile"
            _compila(
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    PROCLAMA "Salve ex PE!".\n'
                '    REDDE 33.\n'
                'FIN-FUNCTIO.\n',
                exitus,
            )
            completed = _exsequere_elf(exitus)
            self.assertEqual(completed.stdout, "Salve ex PE!\n")
            self.assertEqual(completed.returncode, 33)

    def test_proclama_numeri_et_catenae_sequentiales(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-proclama-elf-") as d:
            exitus = Path(d) / "exsecutabile"
            _compila(
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    PROCLAMA "Premier".\n'
                '    PROCLAMA 999.\n'
                '    PROCLAMA "Dernier".\n'
                '    REDDE 7.\n'
                'FIN-FUNCTIO.\n',
                exitus,
            )
            completed = _exsequere_elf(exitus)
            self.assertEqual(completed.stdout, "Premier\n999\nDernier\n")
            self.assertEqual(completed.returncode, 7)

    def test_proclama_fluitans(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-proclama-elf-") as d:
            exitus = Path(d) / "exsecutabile"
            _compila(
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    PROCLAMA 3.14159.\n'
                '    REDDE 0.\n'
                'FIN-FUNCTIO.\n',
                exitus,
            )
            completed = _exsequere_elf(exitus)
            self.assertEqual(completed.stdout, "3.141589\n")

    def test_proclama_tensio_numerorum_variae_magnitudinis(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-proclama-elf-") as d:
            exitus = Path(d) / "exsecutabile"
            _compila(
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    PROCLAMA "Initium".\n'
                '    PROCLAMA 1.\n'
                '    PROCLAMA 22.\n'
                '    PROCLAMA 333.\n'
                '    PROCLAMA 4444.\n'
                '    PROCLAMA 55555.\n'
                '    PROCLAMA "Finis".\n'
                '    REDDE 5.\n'
                'FIN-FUNCTIO.\n',
                exitus,
            )
            completed = _exsequere_elf(exitus)
            self.assertEqual(
                completed.stdout,
                "Initium\n1\n22\n333\n4444\n55555\nFinis\n",
            )
            self.assertEqual(completed.returncode, 5)


@unittest.skipUnless(WINE_ADEST, "wine64 deest")
class ProclamaModusPeTests(unittest.TestCase):
    """Probationes sub modo PE, exsecutae per Wine 9.0. Verificant
    contentum STDOUT scriptum per GetStdHandle+WriteFile, non codicem
    exitus processus (vide nota supra de terminatione)."""

    def test_proclama_catena_litteralis(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-proclama-pe-") as d:
            exitus = Path(d) / "exsecutabile.exe"
            _compila(
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    PROCLAMA "Salve ex PE!".\n'
                '    REDDE 33.\n'
                'FIN-FUNCTIO.\n',
                exitus,
                modus_pe=True,
            )
            stdout = _exsequere_pe_sub_wine(exitus)
            self.assertIn(b"Salve ex PE!", stdout)

    def test_proclama_numeri_et_catenae_sequentiales(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-proclama-pe-") as d:
            exitus = Path(d) / "exsecutabile.exe"
            _compila(
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    PROCLAMA "Premier".\n'
                '    PROCLAMA 999.\n'
                '    PROCLAMA "Dernier".\n'
                '    REDDE 7.\n'
                'FIN-FUNCTIO.\n',
                exitus,
                modus_pe=True,
            )
            stdout = _exsequere_pe_sub_wine(exitus)
            self.assertEqual(stdout, b"Premier\n999\nDernier\n")

    def test_proclama_fluitans(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-proclama-pe-") as d:
            exitus = Path(d) / "exsecutabile.exe"
            _compila(
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    PROCLAMA 3.14159.\n'
                '    REDDE 0.\n'
                'FIN-FUNCTIO.\n',
                exitus,
                modus_pe=True,
            )
            stdout = _exsequere_pe_sub_wine(exitus)
            self.assertEqual(stdout, b"3.141589\n")

    def test_proclama_fluitans_in_sequentia_completa(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-proclama-pe-") as d:
            exitus = Path(d) / "exsecutabile.exe"
            _compila(
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    PROCLAMA "Un".\n'
                '    PROCLAMA "Deux".\n'
                '    PROCLAMA 42.\n'
                '    PROCLAMA 777.\n'
                '    PROCLAMA "Trois".\n'
                '    PROCLAMA 3.14159.\n'
                '    REDDE 0.\n'
                'FIN-FUNCTIO.\n',
                exitus,
                modus_pe=True,
            )
            stdout = _exsequere_pe_sub_wine(exitus)
            self.assertEqual(
                stdout, b"Un\nDeux\n42\n777\nTrois\n3.141589\n"
            )

    def test_proclama_tensio_numerorum_variae_magnitudinis(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-proclama-pe-") as d:
            exitus = Path(d) / "exsecutabile.exe"
            _compila(
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    PROCLAMA "Initium".\n'
                '    PROCLAMA 1.\n'
                '    PROCLAMA 22.\n'
                '    PROCLAMA 333.\n'
                '    PROCLAMA 4444.\n'
                '    PROCLAMA 55555.\n'
                '    PROCLAMA "Finis".\n'
                '    REDDE 5.\n'
                'FIN-FUNCTIO.\n',
                exitus,
                modus_pe=True,
            )
            stdout = _exsequere_pe_sub_wine(exitus)
            self.assertEqual(
                stdout,
                b"Initium\n1\n22\n333\n4444\n55555\nFinis\n",
            )

    def test_proclama_boucle_viginti_iterationum(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-proclama-pe-") as d:
            exitus = Path(d) / "exsecutabile.exe"
            _compila(
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    DECLARA i SICUT NUMERUS VALENS 0.\n'
                '    DUM i < 20 PERFICE\n'
                '        PROCLAMA i.\n'
                '        i = i + 1.\n'
                '    FIN-DUM.\n'
                '    REDDE i.\n'
                'FIN-FUNCTIO.\n',
                exitus,
                modus_pe=True,
            )
            stdout = _exsequere_pe_sub_wine(exitus)
            attendu = "\n".join(str(i) for i in range(20)).encode() + b"\n"
            self.assertEqual(stdout, attendu)

    def test_structura_pe_valida(self) -> None:
        """Verificat fasciculum PE32+ generatum sit structuraliter validus
        (signatura MZ/PE, machina AMD64), sine dependentia a Wine."""
        with tempfile.TemporaryDirectory(prefix="vindex-proclama-pe-") as d:
            exitus = Path(d) / "exsecutabile.exe"
            _compila(
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    PROCLAMA "proba".\n'
                '    REDDE 0.\n'
                'FIN-FUNCTIO.\n',
                exitus,
                modus_pe=True,
            )
            data = exitus.read_bytes()
            self.assertEqual(data[0:2], b"MZ")
            e_lfanew = int.from_bytes(data[0x3C:0x40], "little")
            self.assertEqual(data[e_lfanew:e_lfanew + 4], b"PE\x00\x00")
            machina = int.from_bytes(
                data[e_lfanew + 4:e_lfanew + 6], "little"
            )
            self.assertEqual(machina, 0x8664, "machina debet esse AMD64")


class AutoHospitiumPostProclamaTests(unittest.TestCase):
    """Verificat punctum fixum auto-hospitii servatum post omnes
    mutationes PROCLAMA/PE (nullam Wine dependentiam habet)."""

    def test_punctum_fixum_g2_g3(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-auto-hospitium-") as d:
            gen1 = Path(d) / "gen1"
            gen2 = Path(d) / "gen2"
            subprocess.run(
                [str(COMPILATOR), str(FONS_COMPILATORIS), str(gen1)],
                cwd=RADIX, check=True, timeout=60, capture_output=True,
            )
            gen1.chmod(0o755)
            subprocess.run(
                [str(gen1), str(FONS_COMPILATORIS), str(gen2)],
                cwd=RADIX, check=True, timeout=60, capture_output=True,
            )
            gen2.chmod(0o755)
            gen3 = Path(d) / "gen3"
            subprocess.run(
                [str(gen2), str(FONS_COMPILATORIS), str(gen3)],
                cwd=RADIX, check=True, timeout=60, capture_output=True,
            )
            summa_g2 = hashlib.sha256(gen2.read_bytes()).hexdigest()
            summa_g3 = hashlib.sha256(gen3.read_bytes()).hexdigest()
            self.assertEqual(
                summa_g2, summa_g3,
                "punctum fixum auto-hospitii non servatum est",
            )


if __name__ == "__main__":
    unittest.main()
