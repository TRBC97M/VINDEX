#!/usr/bin/env python3
"""VINDEX 0.53: variantes migrationis pilae separat ut causa tarditatis reperiatur."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import tempfile
import time

RADIX = Path(__file__).resolve().parent.parent
REPO = RADIX.parent.parent
REL_FONS = (RADIX / "src/compilator_vindex.vindex").relative_to(REPO).as_posix()
AMORSA = RADIX / "bootstrap/python/compilateur_053.py"
APPLICATOR = RADIX / "instrumenta/applica_pilam_functionum_053.py"

VETUS_SPATIUM = (
    "    DUM CONTENTUM(pos) < n && (fons[CONTENTUM(pos)] == 32 || "
    "fons[CONTENTUM(pos)] == 10 || fons[CONTENTUM(pos)] == 9) PERFICE\n"
)
NOVUM_SPATIUM = (
    "    DUM CONTENTUM(pos) < n && (fons[CONTENTUM(pos)] == 32 || "
    "fons[CONTENTUM(pos)] == 10 || fons[CONTENTUM(pos)] == 13 || "
    "fons[CONTENTUM(pos)] == 9) PERFICE\n"
)
ANCORA = "FUNCTIO COMPONE_ARITHMETICA REDDENS NUMERUS.\n"
VETUS_PROLOGUS = (
    "                pos = COMPONE_ONERA(codex, pos, 0, 30000).\n"
    "                pos = COMPONE_SUB(codex, pos, 4, 0)."
)
NOVUS_PROLOGUS = "                pos = COMPONE_RESERVA_PILA_PROBATA(codex, pos, 0)."

ADIUTOR_MINIMUS = '''FUNCTIO COMPONE_RESERVA_PILA_PROBATA REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT indice SICUT NUMERUS.
    ACCIPIT spatium SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS indice.
    p = COMPONE_ONERA(codex, p, 0, spatium).
    p = COMPONE_SUB(codex, p, 4, 0).
    REDDE p.
FIN-FUNCTIO.

'''


def lege_caput() -> str:
    data = subprocess.run(
        ["git", "-C", str(REPO), "show", f"HEAD:{REL_FONS}"],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    return data.decode("utf-8")


def corrige_cr(textus: str) -> str:
    if NOVUM_SPATIUM in textus:
        return textus
    if textus.count(VETUS_SPATIUM) != 1:
        raise SystemExit("ERRATUM: IGNORA_SPATIA forma canonica non inventa est")
    return textus.replace(VETUS_SPATIUM, NOVUM_SPATIUM, 1)


def inserta(textus: str, adiutor: str) -> str:
    if textus.count(ANCORA) != 1:
        raise SystemExit("ERRATUM: ancora emissoris non unica est")
    return textus.replace(ANCORA, adiutor + ANCORA, 1)


def voca_adiutorem(textus: str) -> str:
    if textus.count(VETUS_PROLOGUS) != 2:
        raise SystemExit("ERRATUM: prologi veteres non duo sunt")
    return textus.replace(VETUS_PROLOGUS, NOVUS_PROLOGUS)


def mensuram_exactam(textus: str) -> str:
    for index in (1, 2):
        vetus = (
            f"DECLARA spatium_necessarium{index} SICUT NUMERUS VALENS "
            "(0 - tabula[51]) + 10000."
        )
        novum = (
            f"DECLARA spatium_necessarium{index} SICUT NUMERUS VALENS "
            "(((0 - tabula[51]) + 15) / 16) * 16."
        )
        if textus.count(vetus) != 1:
            raise SystemExit(f"ERRATUM: mensura vetus {index} non unica est")
        textus = textus.replace(vetus, novum, 1)
    return textus


def adiutor_compactus() -> str:
    spec = importlib.util.spec_from_file_location("applica_pilam", APPLICATOR)
    if spec is None or spec.loader is None:
        raise SystemExit("ERRATUM: applicator pilae importari non potest")
    modulus = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulus)
    return modulus.adiutor_compactus()


def proba(nomen: str, textus: str, directorium: Path) -> None:
    fons = directorium / f"{nomen}.vindex"
    compilator = directorium / f"{nomen}.compilator"
    exitus = directorium / f"{nomen}.g1"
    fons.write_text(textus, encoding="utf-8", newline="\n")

    initium = time.monotonic()
    try:
        py = subprocess.run(
            ["python3", str(AMORSA), str(fons), str(compilator)],
            text=True,
            capture_output=True,
            timeout=10,
            check=False,
        )
    except subprocess.TimeoutExpired:
        print(f"{nomen}: AMORSA=124 NATIVUS=OMISSUS")
        return
    tempus_py = time.monotonic() - initium
    if py.returncode != 0:
        fragmentum = (py.stdout + py.stderr).strip().replace("\n", " | ")[-240:]
        print(f"{nomen}: AMORSA={py.returncode} TEMPUS={tempus_py:.2f}s {fragmentum}")
        return

    compilator.chmod(0o755)
    initium = time.monotonic()
    try:
        nat = subprocess.run(
            [str(compilator), str(fons), str(exitus)],
            text=True,
            capture_output=True,
            timeout=6,
            check=False,
        )
        status = nat.returncode
        tempus_nat = time.monotonic() - initium
        mensura = exitus.stat().st_size if exitus.exists() else 0
        fragmentum = (nat.stdout + nat.stderr).strip().replace("\n", " | ")[-160:]
        print(
            f"{nomen}: AMORSA=0({tempus_py:.2f}s) "
            f"NATIVUS={status}({tempus_nat:.2f}s) EXITUS={mensura} {fragmentum}"
        )
    except subprocess.TimeoutExpired:
        tempus_nat = time.monotonic() - initium
        print(
            f"{nomen}: AMORSA=0({tempus_py:.2f}s) "
            f"NATIVUS=124(>{tempus_nat:.2f}s) EXITUS=0"
        )


def main() -> None:
    basis = corrige_cr(lege_caput())
    compactus = adiutor_compactus()

    variantes: list[tuple[str, str]] = []
    variantes.append(("A_CR_SOLUM", basis))
    variantes.append(("B_ADIUTOR_COMPACTUS_SOLUM", inserta(basis, compactus)))
    variantes.append(("C_ADIUTOR_MINIMUS_VOCATUS", voca_adiutorem(inserta(basis, ADIUTOR_MINIMUS))))
    variantes.append(("D_MENSURA_EXACTA_SOLA", mensuram_exactam(basis)))
    variantes.append(
        (
            "E_PILA_COMPACTA_PLENA",
            mensuram_exactam(voca_adiutorem(inserta(basis, compactus))),
        )
    )

    print("=== DIAGNOSTICA VARIANTIUM PILAE ===")
    print("Unaquaeque compilatio nativa sex secundis terminatur.")
    with tempfile.TemporaryDirectory(prefix="vindex-pila-var-") as via:
        directorium = Path(via)
        for nomen, textus in variantes:
            proba(nomen, textus, directorium)
    print("=== DIAGNOSTICA FINITA ===")


if __name__ == "__main__":
    main()
