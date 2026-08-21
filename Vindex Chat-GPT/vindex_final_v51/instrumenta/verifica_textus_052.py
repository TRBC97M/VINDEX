#!/usr/bin/env python3
"""Mutationem TEXTUS statice examinat ante probationem auto-hospitii."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import re

RADIX = Path("Vindex Chat-GPT/vindex_final_v51")
VIA_FONTIS = RADIX / "src/compilator_vindex.vindex"
VIA_MUTATORIS = RADIX / "instrumenta/applica_textus_052.py"
LIMES_FONTIS = 212999
LIMES_LOCALIUM = 100
LIMES_ADIUTORUM = 150


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


def nomina_functionum(textus: str) -> list[str]:
    exemplar = re.compile(r"^FUNCTIO\s+([A-Z0-9_]+)\s+REDDENS", re.MULTILINE)
    return exemplar.findall(textus)


spec = spec_from_file_location("mutator_textus_052", VIA_MUTATORIS)
if spec is None or spec.loader is None:
    raise SystemExit("ERRATUM: mutator TEXTUS aperiri non potest")
mutator = module_from_spec(spec)
spec.loader.exec_module(mutator)

pristinus = VIA_FONTIS.read_text(encoding="utf-8")
mutatus = mutator.gradus_tres(mutator.gradus_duo(mutator.gradus_unus(pristinus)))

# ANALYSA_FACTOR omnino intacta manere debet; in duobus magnis analysatoribus
# numerus locorum localium crescere non debet.
if corpus_functionis(pristinus, "ANALYSA_FACTOR") != corpus_functionis(mutatus, "ANALYSA_FACTOR"):
    raise SystemExit("ERRATUM: ANALYSA_FACTOR mutata est")

for nomen in ("ANALYSA_BLOCUS", "PRINCIPALIS"):
    ante = numerus_locorum(corpus_functionis(pristinus, nomen))
    post = numerus_locorum(corpus_functionis(mutatus, nomen))
    print(f"{nomen}: loca ante={ante}, post={post}.")
    if post != ante:
        raise SystemExit(f"ERRATUM: {nomen} nova loca localia accepit")

max_nomen = ""
max_loca = 0
for nomen in nomina_functionum(mutatus):
    loca = numerus_locorum(corpus_functionis(mutatus, nomen))
    if loca > max_loca:
        max_nomen = nomen
        max_loca = loca
    if loca > LIMES_LOCALIUM:
        raise SystemExit(
            f"ERRATUM: functio {nomen} {loca} loca postulat; limes est {LIMES_LOCALIUM}"
        )

functiones = nomina_functionum(mutatus)
adiutores = len([nomen for nomen in functiones if nomen != "PRINCIPALIS"])
print(f"Functiones auxiliares: {adiutores}/{LIMES_ADIUTORUM}.")
if adiutores > LIMES_ADIUTORUM:
    raise SystemExit("ERRATUM: tabula functionum auxiliarium plena est")

mensura = len(mutatus.encode("utf-8"))
print(f"Maxima functio: {max_nomen}, loca={max_loca}.")
print(f"Magnitudo fontis mutati: {mensura}/{LIMES_FONTIS} octeta.")
if mensura > LIMES_FONTIS:
    raise SystemExit("ERRATUM: fons compilatoris limitem magnitudinis excedit")

for nomen in (
    "FUNCTIO COMPONE_LITTERALE_TEXTUS REDDENS NUMERUS.",
    "FUNCTIO COMPONE_IMPRIME_TEXTUS REDDENS NUMERUS.",
):
    if nomen not in mutatus:
        raise SystemExit(f"ERRATUM: adiutor deest: {nomen}")

# 2400-2499 iam signum scalaris variabilis erat: 0 commune, 1 FLUITANS;
# VINDEX 0.52 valorem 2 pro TEXTUS addit. Ita nulla regio metadatae noviter
# occupatur neque tabula formarum in 2900-2918 laeditur.
if "tabula[2900" in mutatus:
    raise SystemExit("ERRATUM: regio 2900 metadatae formarum attingitur")
if "tabula[2400 + idx_nova2] = 2." not in mutatus:
    raise SystemExit("ERRATUM: signum TEXTUS declarationis deest")
if "tabula[2400 + idx_param_pp] = 2." not in mutatus:
    raise SystemExit("ERRATUM: signum TEXTUS parametri principalis deest")
if "tabula[2400 + idx_param] = es_flot_param." not in mutatus:
    raise SystemExit("ERRATUM: signum TEXTUS parametri adiutoris deest")
if "SI es_flot_pcs == 2 TUNC" not in mutatus:
    raise SystemExit("ERRATUM: PROCLAMA TEXTUS deest")

print("RECTE: TEXTUS signo typi II utitur sine collisione metadatae.")
print("RECTE: mutatio parata est ad unam probationem auto-hospitii.")
