#!/usr/bin/env python3
"""Mutationem TEXTUS statice examinat antequam compilator auto-hospes adhibeatur."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import re

RADIX = Path("Vindex Chat-GPT/vindex_final_v51")
VIA_FONTIS = RADIX / "src/compilator_vindex.vindex"
VIA_MUTATORIS = RADIX / "instrumenta/applica_textus_052.py"
LIMES_FONTIS = 212999
LIMES_LOCALIUM = 100


def corpus_functionis(textus: str, nomen: str) -> str:
    initium = textus.find(f"FUNCTIO {nomen} ")
    if initium < 0:
        raise SystemExit(f"ERRATUM: functio {nomen} non inventa est")
    finis = textus.find("FIN-FUNCTIO.", initium)
    if finis < 0:
        raise SystemExit(f"ERRATUM: finis functionis {nomen} non inventus est")
    return textus[initium:finis]


def numerus_locorum(corpus: str) -> int:
    return corpus.count("ACCIPIT ") + corpus.count("DECLARA ")


def functiones(textus: str):
    exemplar = re.compile(r"^FUNCTIO\s+([A-Z0-9_]+)\s+REDDENS", re.MULTILINE)
    for inventum in exemplar.finditer(textus):
        nomen = inventum.group(1)
        yield nomen, corpus_functionis(textus, nomen)


spec = spec_from_file_location("mutator_textus_052", VIA_MUTATORIS)
if spec is None or spec.loader is None:
    raise SystemExit("ERRATUM: mutator TEXTUS aperiri non potest")
mutator = module_from_spec(spec)
spec.loader.exec_module(mutator)

pristinus = VIA_FONTIS.read_text(encoding="utf-8")
mutatus = pristinus
mutatus = mutator.gradus_unus(mutatus)
mutatus = mutator.gradus_duo(mutatus)
mutatus = mutator.gradus_tres(mutatus)

for nomen in ("ANALYSA_FACTOR", "ANALYSA_BLOCUS", "PRINCIPALIS"):
    ante = numerus_locorum(corpus_functionis(pristinus, nomen))
    post = numerus_locorum(corpus_functionis(mutatus, nomen))
    print(f"{nomen}: loca ante={ante}, post={post}.")
    if post != ante:
        raise SystemExit(f"ERRATUM: {nomen} nova loca localia accepit")

max_nomen = ""
max_loca = 0
for nomen, corpus in functiones(mutatus):
    loca = numerus_locorum(corpus)
    if loca > max_loca:
        max_nomen = nomen
        max_loca = loca
    if loca > LIMES_LOCALIUM:
        raise SystemExit(
            f"ERRATUM: functio {nomen} {loca} loca postulat; limes est {LIMES_LOCALIUM}"
        )

mensura = len(mutatus.encode("utf-8"))
print(f"Maxima functio: {max_nomen}, loca={max_loca}.")
print(f"Magnitudo fontis mutati: {mensura}/{LIMES_FONTIS} octeta.")
if mensura > LIMES_FONTIS:
    raise SystemExit("ERRATUM: fons compilatoris limitem magnitudinis excedit")

for nomen in (
    "FUNCTIO EST_TEXTUS_VARIABILIS REDDENS NUMERUS.",
    "FUNCTIO COMPONE_LITTERALE_TEXTUS REDDENS NUMERUS.",
    "FUNCTIO COMPONE_IMPRIME_TEXTUS REDDENS NUMERUS.",
):
    if nomen not in mutatus:
        raise SystemExit(f"ERRATUM: adiutor deest: {nomen}")

print("RECTE: TEXTUS tabulas localium analysatorum non auget.")
