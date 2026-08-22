#!/usr/bin/env python3
"""Cursorem pilae functionis e tabula historica in contextum explicitum transfert."""

from pathlib import Path
import re

RADIX = Path(__file__).resolve().parents[1]
FONS = RADIX / "src" / "compilator_vindex.vindex"
BASIS = RADIX / "instrumenta" / "TABULA-LITTERALIA-053.txt"

textus = FONS.read_text(encoding="utf-8")

accessores = """FUNCTIO CURSOR_PILAE_LEGE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    REDDE CONTENTUM(contextus_parseris + 16).\nFIN-FUNCTIO.\n\nFUNCTIO CURSOR_PILAE_SCRIBE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    ACCIPIT valor SICUT NUMERUS.\n    CONTENTUM(contextus_parseris + 16) = valor.\n    REDDE 0.\nFIN-FUNCTIO.\n\n"""

ancora = """FUNCTIO STATUS_LECTIONIS_SCRIBE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    ACCIPIT valor SICUT NUMERUS.\n    CONTENTUM(contextus_parseris + 8) = valor.\n    REDDE 0.\nFIN-FUNCTIO.\n\n"""

si_mutandum = "tabula[51]" in textus

if "FUNCTIO CURSOR_PILAE_LEGE REDDENS NUMERUS." not in textus:
    if ancora not in textus:
        raise SystemExit("ERRATUM: ancora accessorum contextus parseris non inventa est")
    textus = textus.replace(ancora, ancora + accessores, 1)

allocatio_vetus = "DECLARA contextus_parseris SICUT ACUS<NUMERUS> VALENS RESERVA_OCTETA(16)."
allocatio_nova = "DECLARA contextus_parseris SICUT ACUS<NUMERUS> VALENS RESERVA_OCTETA(24)."
if allocatio_vetus in textus:
    textus = textus.replace(allocatio_vetus, allocatio_nova, 1)
elif allocatio_nova not in textus:
    raise SystemExit("ERRATUM: allocatio contextus parseris non inventa est")

# Scripturae cursoris primum convertuntur; deinde omnes lectiones residuae.
def muta_decrementum(match: re.Match[str]) -> str:
    indentatio, quantum = match.group(1), match.group(2)
    return (
        f"{indentatio}CURSOR_PILAE_SCRIBE(contextus_parseris, "
        f"CURSOR_PILAE_LEGE(contextus_parseris) - {quantum})."
    )

textus = re.sub(
    r"(?m)^([ \t]*)tabula\[51\] = tabula\[51\] - (.+)\.$",
    muta_decrementum,
    textus,
)
textus = re.sub(
    r"(?m)^([ \t]*)tabula\[51\] = 0 - 8\.$",
    r"\1CURSOR_PILAE_SCRIBE(contextus_parseris, 0 - 8).",
    textus,
)
textus = textus.replace("tabula[51]", "CURSOR_PILAE_LEGE(contextus_parseris)")

if "CURSOR_PILAE_LEGE(contextus_parseris) =" in textus:
    raise SystemExit("ERRATUM: scriptura cursoris nondum per accessorium translata est")
if "tabula[51]" in textus:
    raise SystemExit("ERRATUM: tabula[51] post migrationem adhuc adest")

commentum_vetus = "// Locus 51 cursor pilae functionis manet; regiones ceterae paulatim in gradibus posterioribus migrabuntur."
commentum_novum = "// Cursor pilae functionis in contextu explicito servatur; descriptores collectionum adhuc in tabula manent."
textus = textus.replace(commentum_vetus, commentum_novum)

FONS.write_text(textus, encoding="utf-8", newline="\n")

lineae = BASIS.read_text(encoding="utf-8").splitlines()
lineae = [linea for linea in lineae if linea.strip() != "51"]
lineae = [
    linea.replace("X indices, XCV accessus", "IX indices, XLV accessus")
    for linea in lineae
]
BASIS.write_text("\n".join(lineae) + "\n", encoding="utf-8", newline="\n")

if si_mutandum:
    print("RECTE: cursor pilae 51 e tabula in contextum explicitum translatus est.")
else:
    print("RECTE: cursor pilae iam extra tabulam est.")
