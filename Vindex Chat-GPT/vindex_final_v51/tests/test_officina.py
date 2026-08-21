#!/usr/bin/env python3
"""Probationes functionales Officinae VINDEX graphicae."""

from __future__ import annotations

import os
import subprocess
import tempfile
import unittest
from pathlib import Path


RADIX = Path(__file__).resolve().parent.parent
INITIATOR = RADIX / "officina_vindex"
SALUTATIO = RADIX / "salutatio_vindex"
PONS = RADIX / "vindex_graphica"
COMPILATOR = RADIX / "compilator_vindex"
FONS_INITIATORIS = RADIX / "src/officina_vindex.vindex"
FONS_PONTIS = RADIX / "runtime/vindex_graphica_gtk.c"
FORMA_OFFICINAE = RADIX / "formae/officina.forma"
FORMA_SALUTATIONIS = RADIX / "formae/salutatio.forma"


class OfficinaGraphicaTests(unittest.TestCase):
    def test_initiator_vindex_binarum_distributum_reproducit(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-officina-initiator-") as directory:
            exitus = Path(directory) / "officina_genita"
            completed = subprocess.run(
                [str(COMPILATOR), str(FONS_INITIATORIS), str(exitus)],
                cwd=RADIX,
                text=True,
                capture_output=True,
                timeout=20,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            self.assertEqual(exitus.read_bytes(), INITIATOR.read_bytes())
            self.assertEqual(exitus.read_bytes()[:4], b"\x7fELF")

    def test_pons_gtk_nativus_integer_est(self) -> None:
        completed = subprocess.run(
            [str(PONS), "--probatio"],
            cwd=RADIX,
            text=True,
            capture_output=True,
            timeout=5,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("pons GTK declarativus integer est", completed.stdout)
        self.assertEqual(PONS.read_bytes()[:4], b"\x7fELF")

    def test_formae_duarum_applicationum_validae_sunt(self) -> None:
        for forma in (FORMA_OFFICINAE, FORMA_SALUTATIONIS):
            completed = subprocess.run(
                [str(PONS), "--verifica-formam", str(forma)],
                cwd=RADIX,
                text=True,
                capture_output=True,
                timeout=5,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertIn("forma graphica valida est", completed.stdout)

    def test_bibliotheca_graphica_eventa_latina_praebet(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-bibliotheca-graphica-") as directory:
            exitus = Path(directory) / "graphica"
            compilatio = subprocess.run(
                [str(RADIX / "vindexc"), str(RADIX / "tests/casus/graphica.vindex"), "-o", str(exitus)],
                cwd=RADIX,
                text=True,
                capture_output=True,
                timeout=20,
                check=False,
            )
            self.assertEqual(compilatio.returncode, 0, compilatio.stdout + compilatio.stderr)
            completed = subprocess.run(
                [str(exitus)],
                cwd=RADIX,
                text=True,
                capture_output=True,
                timeout=5,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(
                completed.stdout.splitlines(),
                ["78", "79", "83", "67", "88", "81", "72", "99", "120", "82", "69"],
            )

    def test_logica_vindex_eventum_graphicum_compilat_et_exsequitur(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-officina-vocatio-") as directory:
            temporarium = Path(directory)
            pons_probationis = temporarium / "pons-probationis"
            pons_probationis.write_text(
                """#!/usr/bin/env python3
import os
import pathlib
import select
import sys
import time

paratus_r, paratus_w = os.pipe()
filius = os.fork()
if filius > 0:
    os.close(paratus_w)
    os.read(paratus_r, 1)
    os.close(paratus_r)
    raise SystemExit(0)

os.close(paratus_r)
devnull = os.open(os.devnull, os.O_RDWR)
os.dup2(devnull, 1)
os.dup2(devnull, 2)
os.close(devnull)
ad_vindex = '.vindex-graphica-ad-vindex'
ab_vindex = '.vindex-graphica-ab-vindex'
for via in (ad_vindex, ab_vindex):
    try:
        os.unlink(via)
    except FileNotFoundError:
        pass
    os.mkfifo(via, 0o600)

fd_ad = os.open(ad_vindex, os.O_RDWR)
fd_ab = os.open(ab_vindex, os.O_RDWR)
pathlib.Path('.vindex-graphica-valor-fons').write_bytes(pathlib.Path(sys.argv[3]).read_bytes())
os.write(paratus_w, b'R')
os.close(paratus_w)
os.write(fd_ad, b'X')
responsum = b''
finis = time.monotonic() + 8
while time.monotonic() < finis and not (b'R' in responsum or b'E' in responsum):
    parata, _, _ = select.select([fd_ab], [], [], max(0, finis - time.monotonic()))
    if parata:
        responsum += os.read(fd_ab, 8)
pathlib.Path('responsum.bin').write_bytes(responsum)
relatio = pathlib.Path('.vindex-graphica-relatio')
pathlib.Path('relatio.txt').write_bytes(relatio.read_bytes() if relatio.exists() else b'')
os.write(fd_ad, b'Q')
time.sleep(0.1)
os.close(fd_ad)
os.close(fd_ab)
for via in (ad_vindex, ab_vindex):
    try:
        os.unlink(via)
    except FileNotFoundError:
        pass
os._exit(0)
""",
                encoding="utf-8",
            )
            pons_probationis.chmod(0o755)
            fons = temporarium / "programma.vindex"
            fons.write_text(
                'FUNCTIO PRINCIPALIS REDDENS NUMERUS.\n'
                '    PROCLAMA "Salve ex logica VINDEX!".\n'
                '    REDDE 0.\n'
                'FIN-FUNCTIO.\n',
                encoding="utf-8",
            )
            completed = subprocess.run(
                [str(INITIATOR), str(pons_probationis), str(COMPILATOR), str(FORMA_OFFICINAE), str(fons)],
                cwd=temporarium,
                text=True,
                capture_output=True,
                timeout=20,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual((temporarium / "responsum.bin").read_bytes(), b"xR")
            self.assertIn("Salve ex logica VINDEX!", (temporarium / "relatio.txt").read_text())
            self.assertTrue((temporarium / "programma.elf").is_file())

    def test_altera_applicatio_salutationem_in_vindex_componit(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-salutatio-") as directory:
            temporarium = Path(directory)
            pons_probationis = temporarium / "pons-probationis"
            pons_probationis.write_text(
                """#!/usr/bin/env python3
import os
import pathlib
import select
import time

paratus_r, paratus_w = os.pipe()
filius = os.fork()
if filius > 0:
    os.close(paratus_w)
    os.read(paratus_r, 1)
    os.close(paratus_r)
    raise SystemExit(0)

os.close(paratus_r)
devnull = os.open(os.devnull, os.O_RDWR)
os.dup2(devnull, 1)
os.dup2(devnull, 2)
os.close(devnull)
ad_vindex = '.vindex-graphica-ad-vindex'
ab_vindex = '.vindex-graphica-ab-vindex'
for via in (ad_vindex, ab_vindex):
    try:
        os.unlink(via)
    except FileNotFoundError:
        pass
    os.mkfifo(via, 0o600)
fd_ad = os.open(ad_vindex, os.O_RDWR)
fd_ab = os.open(ab_vindex, os.O_RDWR)
pathlib.Path('.vindex-graphica-valor-nomen').write_text('Livia', encoding='utf-8')
os.write(paratus_w, b'R')
os.close(paratus_w)
os.write(fd_ad, b'H')
parata, _, _ = select.select([fd_ab], [], [], 8)
responsum = os.read(fd_ab, 1) if parata else b''
pathlib.Path('responsum-salutationis.bin').write_bytes(responsum)
relatio = pathlib.Path('.vindex-graphica-relatio')
pathlib.Path('salutatio.txt').write_bytes(relatio.read_bytes() if relatio.exists() else b'')
os.write(fd_ad, b'Q')
time.sleep(0.1)
os.close(fd_ad)
os.close(fd_ab)
for via in (ad_vindex, ab_vindex):
    try:
        os.unlink(via)
    except FileNotFoundError:
        pass
os._exit(0)
""",
                encoding="utf-8",
            )
            pons_probationis.chmod(0o755)
            completed = subprocess.run(
                [str(SALUTATIO), str(pons_probationis), str(FORMA_SALUTATIONIS)],
                cwd=temporarium,
                text=True,
                capture_output=True,
                timeout=20,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual((temporarium / "responsum-salutationis.bin").read_bytes(), b"R")
            self.assertEqual((temporarium / "salutatio.txt").read_text(), "Salve, Livia!\n")


class InstallerTests(unittest.TestCase):
    def test_officinam_graphicam_in_ratione_temporaria_installat(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vindex-installatio-") as directory:
            ratio = Path(directory)
            ambitus = {
                **os.environ,
                "HOME": str(ratio / "domus"),
                "XDG_DATA_HOME": str(ratio / "data"),
                "XDG_BIN_HOME": str(ratio / "bin"),
            }
            completed = subprocess.run(
                [str(RADIX / "installa_officinam.sh")],
                cwd=RADIX,
                env=ambitus,
                text=True,
                capture_output=True,
                timeout=30,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)

            installatio = ratio / "data/vindex"
            desktop = ratio / "data/applications/com.vindex.Officina.desktop"
            descriptio = desktop.read_text(encoding="utf-8")
            self.assertTrue((installatio / "officina_vindex").is_file())
            self.assertTrue((installatio / "salutatio_vindex").is_file())
            self.assertTrue((installatio / "vindex_graphica").is_file())
            self.assertTrue((installatio / "formae/officina.forma").is_file())
            self.assertTrue((installatio / "formae/salutatio.forma").is_file())
            self.assertTrue((installatio / "systema_vindex.img").is_file())
            self.assertTrue((installatio / "nucleus_systema.elf").is_file())
            self.assertTrue((installatio / "fenestrale_systema.bin").is_file())
            self.assertTrue((installatio / "rectores_systema.bin").is_file())
            self.assertTrue((installatio / "runtime/vindex_graphica_gtk.c").is_file())
            self.assertTrue((ratio / "bin/vindex-officina").is_symlink())
            self.assertTrue((ratio / "bin/vindex-salutatio").is_symlink())
            self.assertTrue((ratio / "bin/vindex-systema").is_symlink())
            self.assertIn("Terminal=false", descriptio)
            self.assertIn(str(installatio / "officina_vindex"), descriptio)
            self.assertIn(str(installatio / "vindex_graphica"), descriptio)
            self.assertNotIn("python", descriptio.lower())
            self.assertNotIn("http", descriptio.lower())

            probatio = subprocess.run(
                [str(installatio / "vindex_graphica"), "--probatio"],
                env=ambitus,
                text=True,
                capture_output=True,
                timeout=5,
                check=False,
            )
            self.assertEqual(probatio.returncode, 0, probatio.stderr)


class PuritasTests(unittest.TestCase):
    def test_interfacies_interretialis_et_terminalis_absunt(self) -> None:
        vetita = [
            RADIX / "studio/index.html",
            RADIX / "studio/studio.css",
            RADIX / "studio/studio.js",
            RADIX / "studio/vindex_studio.py",
            RADIX / "vindex-studio",
        ]
        self.assertFalse([str(via) for via in vetita if via.exists()])
        viva = "\n".join(
            via.read_text(encoding="utf-8")
            for via in [
                FONS_INITIATORIS,
                FONS_PONTIS,
                RADIX / "vindex-officina",
                RADIX / "installa_officinam.sh",
            ]
        ).lower()
        for vestigium in (
            "http.server",
            "webbrowser",
            "127.0.0.1",
            "index.html",
            "officina nativa                   ║",
            "mandatum:",
            "editor linearis",
        ):
            self.assertNotIn(vestigium, viva)
        self.assertIn("gtk_window_new", viva)
        self.assertIn("terminal=false", viva)
        self.assertNotIn("VINDEX // OFFICINA", FONS_PONTIS.read_text(encoding="utf-8"))
        self.assertIn("FENESTRA", FORMA_OFFICINAE.read_text(encoding="utf-8"))
        self.assertIn("CAMPUS_TEXTUS", FORMA_SALUTATIONIS.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
