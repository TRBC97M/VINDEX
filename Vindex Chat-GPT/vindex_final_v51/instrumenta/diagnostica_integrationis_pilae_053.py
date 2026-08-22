#!/usr/bin/env python3
"""VINDEX 0.53: interactionem emissoris U16 cum vocatione et mensura exacta separat."""

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
MARCA = "FUNCTIO COMPONE_RESERVA_PILA_PROBATA REDDENS NUMERUS."

VETUS_SPATIUM = (
    "    DUM CONTENTUM(pos) < n && (fons[CONTENTUM(pos)] == 32 || "
    "fons[CONTENTUM(pos)] == 10 || fons[CONTENTUM(pos)] == 9) PERFICE\n"
)
NOVUM_SPATIUM = (
    "    DUM CONTENTUM(pos) < n && (fons[CONTENTUM(pos)] == 32 || "
    "fons[CONTENTUM(pos)] == 10 || fons[CONTENTUM(pos)] == 13 || "
    "fons[CONTENTUM(pos)] == 9) PERFICE\n"
)

VETUS_PROLOGUS = (
    "                pos = COMPONE_ONERA(codex, pos, 0, 30000).\n"
    "                pos = COMPONE_SUB(codex, pos, 4, 0)."
)
NOVUS_PROLOGUS = "                pos = COMPONE_RESERVA_PILA_PROBATA(codex, pos, 0)."

U16 = '''FUNCTIO COMPONE_RESERVA_PILA_PROBATA REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT indice SICUT NUMERUS.
    ACCIPIT spatium SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS indice.
    DECLARA ignoratum SICUT NUMERUS VALENS 0.

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


def lege_basis() -> str:
    data = subprocess.run(
        ["git", "-C", str(REPO), "show", f"HEAD:{REL_FONS}"],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    textus = data.decode("utf-8")

    if NOVUM_SPATIUM not in textus:
        if textus.count(VETUS_SPATIUM) != 1:
            raise SystemExit("ERRATUM: IGNORA_SPATIA canonica non inventa est")
        textus = textus.replace(VETUS_SPATIUM, NOVUM_SPATIUM, 1)

    if MARCA in textus:
        initium = textus.index(MARCA)
        finis = textus.index(ANCORA, initium)
        textus = textus[:initium] + textus[finis:]

    if textus.count(ANCORA) != 1:
        raise SystemExit("ERRATUM: ancora emissoris non unica est")
    return textus


def inserta_u16(textus: str) -> str:
    return textus.replace(ANCORA, U16 + ANCORA, 1)


def voca(textus: str) -> str:
    veteres = textus.count(VETUS_PROLOGUS)
    novi = textus.count(NOVUS_PROLOGUS)
    if veteres == 2 and novi == 0:
        return textus.replace(VETUS_PROLOGUS, NOVUS_PROLOGUS)
    if veteres == 0 and novi == 2:
        return textus
    raise SystemExit(f"ERRATUM: prologi ambigui: veteres={veteres} novi={novi}")


def mensura(textus: str) -> str:
    for index in (1, 2):
        vetus = (
            f"DECLARA spatium_necessarium{index} SICUT NUMERUS VALENS "
            "(0 - tabula[51]) + 10000."
        )
        novum = (
            f"DECLARA spatium_necessarium{index} SICUT NUMERUS VALENS "
            "(((0 - tabula[51]) + 15) / 16) * 16."
        )
        if vetus in textus:
            textus = textus.replace(vetus, novum, 1)
        elif novum not in textus:
            raise SystemExit(f"ERRATUM: mensura {index} non inventa est")
    return textus


def proba(nomen: str, textus: str, directorium: Path) -> None:
    fons = directorium / f"{nomen}.vindex"
    compilator = directorium / f"{nomen}.compilator"
    exitus = directorium / f"{nomen}.g1"
    fons.write_text(textus, encoding="utf-8", newline="\n")

    t0 = time.monotonic()
    py = subprocess.run(
        ["python3", str(AMORSA), str(fons), str(compilator)],
        text=True,
        capture_output=True,
        timeout=10,
        check=False,
    )
    tpy = time.monotonic() - t0
    if py.returncode != 0:
        print(f"{nomen}: AMORSA={py.returncode}({tpy:.2f}s)")
        return
    compilator.chmod(0o755)

    t0 = time.monotonic()
    try:
        nat = subprocess.run(
            [str(compilator), str(fons), str(exitus)],
            text=True,
            capture_output=True,
            timeout=5,
            check=False,
        )
        tnat = time.monotonic() - t0
        mens = exitus.stat().st_size if exitus.exists() else 0
        print(f"{nomen}: AMORSA=0({tpy:.2f}s) NATIVUS={nat.returncode}({tnat:.2f}s) EXITUS={mens}")
    except subprocess.TimeoutExpired:
        tnat = time.monotonic() - t0
        print(f"{nomen}: AMORSA=0({tpy:.2f}s) NATIVUS=124(>{tnat:.2f}s) EXITUS=0")


def main() -> None:
    basis = lege_basis()
    u16 = inserta_u16(basis)

    variantes = (
        ("A_U16_SOLUM", u16),
        ("B_U16_VOCATUS", voca(u16)),
        ("C_U16_MENSURA_EXACTA", mensura(u16)),
        ("D_U16_PLENUS", mensura(voca(u16))),
        ("E_BASIS_VOCATIO_SINE_U16", voca(inserta_u16(basis).replace(U16, '''FUNCTIO COMPONE_RESERVA_PILA_PROBATA REDDENS NUMERUS.\n    ACCIPIT codex SICUT ACUS<NUMERUS>.\n    ACCIPIT indice SICUT NUMERUS.\n    ACCIPIT spatium SICUT NUMERUS.\n    DECLARA p SICUT NUMERUS VALENS indice.\n    p = COMPONE_ONERA(codex, p, 0, spatium).\n    p = COMPONE_SUB(codex, p, 4, 0).\n    REDDE p.\nFIN-FUNCTIO.\n\n'''))),
    )

    print("=== DIAGNOSTICA INTEGRATIONIS PILAE ===")
    print("Unaquaeque generatio nativa quinque secundis terminatur.")
    with tempfile.TemporaryDirectory(prefix="vindex-integratio-pila-") as via:
        directorium = Path(via)
        for nomen, textus in variantes:
            proba(nomen, textus, directorium)
    print("=== DIAGNOSTICA INTEGRATIONIS FINITA ===")


if __name__ == "__main__":
    main()
