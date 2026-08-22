#!/usr/bin/env python3
"""Vectorem historicum tabula, iam vacuum, e compilatore VINDEX 0.53 removet."""

from pathlib import Path
import re

RADIX = Path(__file__).resolve().parents[1]
FONS = RADIX / "src" / "compilator_vindex.vindex"

textus = FONS.read_text(encoding="utf-8")
vetus = textus

# Nullus accessus literalium iam restat; tabula tantum argumentum vacuum per parserem transit.
if re.search(r"\btabula\s*\[", textus):
    raise SystemExit("ERRATUM: accessus tabulae adhuc adest; vector deleri non potest")

textus = textus.replace("    ACCIPIT tabula SICUT ORDO DE NUMERUS.\n", "")
textus = textus.replace(", tabula, contextus_parseris", ", contextus_parseris")
textus = textus.replace("    DECLARA tabula SICUT ORDO DE NUMERUS CAPACITAS 3000.\n", "")

# Post migrationem nomen exactum `tabula` in codice non iam licet. Formae Latinae in commentariis
# sicut `tabulae` vel `tabulam` non sunt identifier idem.
reliquiae = [
    (i + 1, linea)
    for i, linea in enumerate(textus.splitlines())
    if re.search(r"\btabula\b", linea) and not linea.lstrip().startswith("//")
]
if reliquiae:
    descriptio = "; ".join(f"{n}:{l.strip()}" for n, l in reliquiae[:8])
    raise SystemExit(f"ERRATUM: identifier tabula adhuc in codice adest: {descriptio}")

FONS.write_text(textus, encoding="utf-8", newline="\n")

if textus == vetus:
    print("RECTE: vector historicus tabula iam deletus est.")
else:
    print("RECTE: vector historicus tabula CAPACITAS 3000 et argumenta vacua deleta sunt.")
