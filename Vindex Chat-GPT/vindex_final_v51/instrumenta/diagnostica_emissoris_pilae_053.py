#!/usr/bin/env python3
"""VINDEX 0.53: causam tarditatis intra emissorem pilae subtilius separat."""

from __future__ import annotations

from pathlib import Path
import subprocess
import tempfile
import time

RADIX = Path(__file__).resolve().parent.parent
REPO = RADIX.parent.parent
REL_FONS = (RADIX / "src/compilator_vindex.vindex").relative_to(REPO).as_posix()
AMORSA = RADIX / "bootstrap/python/compilateur_053.py"
ANCORA = "FUNCTIO COMPONE_ARITHMETICA REDDENS NUMERUS.\n"

VETUS_SPATIUM = (
    "    DUM CONTENTUM(pos) < n && (fons[CONTENTUM(pos)] == 32 || "
    "fons[CONTENTUM(pos)] == 10 || fons[CONTENTUM(pos)] == 9) PERFICE\n"
)
NOVUM_SPATIUM = (
    "    DUM CONTENTUM(pos) < n && (fons[CONTENTUM(pos)] == 32 || "
    "fons[CONTENTUM(pos)] == 10 || fons[CONTENTUM(pos)] == 13 || "
    "fons[CONTENTUM(pos)] == 9) PERFICE\n"
)

CAPUT = '''FUNCTIO COMPONE_RESERVA_PILA_PROBATA REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT indice SICUT NUMERUS.
    ACCIPIT spatium SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS indice.
'''

MINIMUS = CAPUT + '''    p = COMPONE_ONERA(codex, p, 0, spatium).
    p = COMPONE_SUB(codex, p, 4, 0).
    REDDE p.
FIN-FUNCTIO.

'''

U64_SOLUM = CAPUT + '''    DECLARA ignoratum SICUT NUMERUS VALENS 0.
    CODEX_SCRIBE(codex, p, 73).
    CODEX_SCRIBE(codex, p + 1, 187).
    ignoratum = SCRIBE_U64(codex, p + 2, spatium).
    REDDE p + 10.
FIN-FUNCTIO.

'''

U32_PARVUS = CAPUT + '''    DECLARA ignoratum SICUT NUMERUS VALENS 0.
    ignoratum = SCRIBE_U32(codex, p, 16482633).
    REDDE p + 4.
FIN-FUNCTIO.

'''

U32_MAGNUS = CAPUT + '''    DECLARA ignoratum SICUT NUMERUS VALENS 0.
    ignoratum = SCRIBE_U32(codex, p, 3967895580).
    REDDE p + 4.
FIN-FUNCTIO.

'''

U16_PLENUS = CAPUT + '''    DECLARA ignoratum SICUT NUMERUS VALENS 0.

    CODEX_SCRIBE(codex, p, 73).
    CODEX_SCRIBE(codex, p + 1, 187).
    ignoratum = SCRIBE_U64(codex, p + 2, spatium).

    ignoratum = SCRIBE_U16(codex, p + 10, 33097).
    ignoratum = SCRIBE_U16(codex, p + 12, 251).
    ignoratum = SCRIBE_U16(codex, p + 14, 16).
    ignoratum = SCRIBE_U16(codex, p + 16, 30208).
    ignoratum = SCRIBE_U16(codex, p + 18, 18460).
    ignoratum = SCRIBE_U16(codex, p + 20, 60545).
    ignoratum = SCRIBE_U16(codex, p + 22, 4096).
    ignoratum = SCRIBE_U16(codex, p + 24, 0).
    ignoratum = SCRIBE_U16(codex, p + 26, 33608).
    ignoratum = SCRIBE_U16(codex, p + 28, 9228).
    ignoratum = SCRIBE_U16(codex, p + 30, 18688).
    ignoratum = SCRIBE_U16(codex, p + 32, 60289).
    ignoratum = SCRIBE_U16(codex, p + 34, 4096).
    ignoratum = SCRIBE_U16(codex, p + 36, 0).
    ignoratum = SCRIBE_U16(codex, p + 38, 33097).
    ignoratum = SCRIBE_U16(codex, p + 40, 251).
    ignoratum = SCRIBE_U16(codex, p + 42, 16).
    ignoratum = SCRIBE_U16(codex, p + 44, 30464).
    ignoratum = SCRIBE_U16(codex, p + 46, 19684).
    ignoratum = SCRIBE_U16(codex, p + 48, 56361).
    ignoratum = SCRIBE_U16(codex, p + 50, 33608).
    ignoratum = SCRIBE_U16(codex, p + 52, 9228).
    CODEX_SCRIBE(codex, p + 54, 0).

    REDDE p + 55.
FIN-FUNCTIO.

'''


def lege_caput() -> str:
    data = subprocess.run(
        ["git", "-C", str(REPO), "show", f"HEAD:{REL_FONS}"],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    return data.decode("utf-8")


def purga_migrationem(textus: str) -> str:
    # HEAD potest iam continere mutationes locales canonizationis nondum commissas;
    # diagnostica tamen ex obiecto HEAD incipit. CR tantum hic corrigitur.
    if NOVUM_SPATIUM in textus:
        pass
    elif textus.count(VETUS_SPATIUM) == 1:
        textus = textus.replace(VETUS_SPATIUM, NOVUM_SPATIUM, 1)
    else:
        raise SystemExit("ERRATUM: forma IGNORA_SPATIA non agnita est")

    marca = "FUNCTIO COMPONE_RESERVA_PILA_PROBATA REDDENS NUMERUS."
    if marca in textus:
        initium = textus.index(marca)
        finis = textus.index(ANCORA, initium)
        textus = textus[:initium] + textus[finis:]
    return textus


def proba(nomen: str, adiutor: str, basis: str, directorium: Path) -> None:
    fons = directorium / f"{nomen}.vindex"
    compilator = directorium / f"{nomen}.compilator"
    exitus = directorium / f"{nomen}.g1"
    textus = basis.replace(ANCORA, adiutor + ANCORA, 1)
    fons.write_text(textus, encoding="utf-8", newline="\n")

    initium = time.monotonic()
    py = subprocess.run(
        ["python3", str(AMORSA), str(fons), str(compilator)],
        text=True,
        capture_output=True,
        timeout=10,
        check=False,
    )
    tpy = time.monotonic() - initium
    if py.returncode != 0:
        print(f"{nomen}: AMORSA={py.returncode}({tpy:.2f}s)")
        return

    compilator.chmod(0o755)
    initium = time.monotonic()
    try:
        nat = subprocess.run(
            [str(compilator), str(fons), str(exitus)],
            text=True,
            capture_output=True,
            timeout=4,
            check=False,
        )
        tnat = time.monotonic() - initium
        mensura = exitus.stat().st_size if exitus.exists() else 0
        print(
            f"{nomen}: AMORSA=0({tpy:.2f}s) NATIVUS={nat.returncode}"
            f"({tnat:.2f}s) EXITUS={mensura}"
        )
    except subprocess.TimeoutExpired:
        tnat = time.monotonic() - initium
        print(f"{nomen}: AMORSA=0({tpy:.2f}s) NATIVUS=124(>{tnat:.2f}s) EXITUS=0")


def main() -> None:
    basis = purga_migrationem(lege_caput())
    if basis.count(ANCORA) != 1:
        raise SystemExit("ERRATUM: ancora emissoris non unica est")

    variantes = (
        ("A_MINIMUS", MINIMUS),
        ("B_U64_SOLUM", U64_SOLUM),
        ("C_U32_PARVUS", U32_PARVUS),
        ("D_U32_MAGNUS", U32_MAGNUS),
        ("E_U16_PLENUS", U16_PLENUS),
    )

    print("=== DIAGNOSTICA EMISSORIS PILAE ===")
    print("Unaquaeque generatio nativa quattuor secundis terminatur.")
    with tempfile.TemporaryDirectory(prefix="vindex-emissor-pila-") as via:
        directorium = Path(via)
        for nomen, adiutor in variantes:
            proba(nomen, adiutor, basis, directorium)
    print("=== DIAGNOSTICA EMISSORIS FINITA ===")


if __name__ == "__main__":
    main()
