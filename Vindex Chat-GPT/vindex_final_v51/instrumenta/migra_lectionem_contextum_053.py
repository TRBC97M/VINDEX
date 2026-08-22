#!/usr/bin/env python3
"""VINDEX 0.53: statum lectionis e tabula in contextum parseris communem transfert."""

from pathlib import Path


FONS = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
BASIS = Path("Vindex Chat-GPT/vindex_final_v51/instrumenta/TABULA-LITTERALIA-053.txt")

FUNCTIONES_CONTEXTUS = (
    "COMPONE_CURRE",
    "COMPONE_TUBUS",
    "COMPONE_CAMBIA_DIRECTORIUM",
    "ANALYSA_FACTOR",
    "ANALYSA_TERMINUM",
    "ANALYSA_EXPRESSIO",
    "ANALYSA_COMPARATIO",
)

VOCATIONES_CONTEXTUS = (
    "COMPONE_CURRE",
    "COMPONE_TUBUS",
    "COMPONE_CAMBIA_DIRECTORIUM",
    "ANALYSA_FACTOR",
    "ANALYSA_TERMINUM",
    "ANALYSA_EXPRESSIO",
    "ANALYSA_COMPARATIO",
    "ANALYSA_BLOCUS",
)

VETUS_DESINE_LEGE = '''FUNCTIO STATUS_DESINE_LEGE REDDENS NUMERUS.
    ACCIPIT contextus_desine SICUT ACUS<NUMERUS>.
    REDDE CONTENTUM(contextus_desine).
FIN-FUNCTIO.
'''

NOVUS_DESINE_LEGE = '''FUNCTIO STATUS_DESINE_LEGE REDDENS NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    REDDE CONTENTUM(contextus_parseris).
FIN-FUNCTIO.
'''

VETUS_DESINE_SCRIBE = '''FUNCTIO STATUS_DESINE_SCRIBE REDDENS NUMERUS.
    ACCIPIT contextus_desine SICUT ACUS<NUMERUS>.
    ACCIPIT valor SICUT NUMERUS.
    CONTENTUM(contextus_desine) = valor.
    REDDE 0.
FIN-FUNCTIO.
'''

NOVUS_DESINE_SCRIBE = '''FUNCTIO STATUS_DESINE_SCRIBE REDDENS NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    ACCIPIT valor SICUT NUMERUS.
    CONTENTUM(contextus_parseris) = valor.
    REDDE 0.
FIN-FUNCTIO.
'''

VETUS_LECTIO_LEGE = '''FUNCTIO STATUS_LECTIONIS_LEGE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    REDDE tabula[2999].
FIN-FUNCTIO.
'''

NOVUS_LECTIO_LEGE = '''FUNCTIO STATUS_LECTIONIS_LEGE REDDENS NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    REDDE CONTENTUM(contextus_parseris + 8).
FIN-FUNCTIO.
'''

VETUS_LECTIO_SCRIBE = '''FUNCTIO STATUS_LECTIONIS_SCRIBE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT valor SICUT NUMERUS.
    tabula[2999] = valor.
    REDDE 0.
FIN-FUNCTIO.
'''

NOVUS_LECTIO_SCRIBE = '''FUNCTIO STATUS_LECTIONIS_SCRIBE REDDENS NUMERUS.
    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.
    ACCIPIT valor SICUT NUMERUS.
    CONTENTUM(contextus_parseris + 8) = valor.
    REDDE 0.
FIN-FUNCTIO.
'''

VETUS_CONTEXTUS = "    DECLARA contextus_desine SICUT NUMERUS VALENS 0.\n"
NOVUS_CONTEXTUS = '''    DECLARA contextus_parseris SICUT ACUS<NUMERUS> VALENS RESERVA_OCTETA(16).
    SI contextus_parseris < 0 TUNC
        PROCLAMA "ERRATUM: memoria contextus parseris reservata non est".
        REDDE 71.
    FIN-SI.
    CONTENTUM(contextus_parseris) = 0.
    CONTENTUM(contextus_parseris + 8) = 0.
'''


def muta_unum(textus: str, vetus: str, novum: str, nomen: str) -> tuple[str, bool]:
    nv = textus.count(vetus)
    nn = textus.count(novum)
    if nv == 1 and nn == 0:
        return textus.replace(vetus, novum, 1), True
    if nv == 0 and nn == 1:
        return textus, False
    raise SystemExit(f"ERRATUM: mutatio {nomen} ambigua est (vetus={nv}, nova={nn})")


def fines_functionis(textus: str, nomen: str) -> tuple[int, int]:
    initium = textus.find(f"FUNCTIO {nomen} REDDENS NUMERUS.\n")
    if initium < 0:
        raise SystemExit(f"ERRATUM: functio {nomen} non inventa est")
    finis = textus.find("FIN-FUNCTIO.\n", initium)
    if finis < 0:
        raise SystemExit(f"ERRATUM: finis functionis {nomen} non inventus est")
    return initium, finis + len("FIN-FUNCTIO.\n")


def adde_contextum_functioni(textus: str, nomen: str) -> tuple[str, bool]:
    initium, finis = fines_functionis(textus, nomen)
    pars = textus[initium:finis]
    nova_linea = "    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n"
    if nova_linea in pars:
        return textus, False
    ancora = "    ACCIPIT tabula SICUT ORDO DE NUMERUS.\n"
    if pars.count(ancora) != 1:
        raise SystemExit(f"ERRATUM: ancora contextus in {nomen} non unica est")
    pars = pars.replace(ancora, ancora + nova_linea, 1)
    return textus[:initium] + pars + textus[finis:], True


def rename_blocum_contextus(textus: str) -> tuple[str, bool]:
    initium, finis = fines_functionis(textus, "ANALYSA_BLOCUS")
    pars = textus[initium:finis]
    mutatum = False
    vetus = "    ACCIPIT contextus_desine SICUT ACUS<NUMERUS>.\n"
    novus = "    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n"
    if vetus in pars:
        pars = pars.replace(vetus, novus, 1)
        mutatum = True
    elif novus not in pars:
        raise SystemExit("ERRATUM: argumentum contextus ANALYSA_BLOCUS deest")
    if "contextus_desine" in pars:
        pars = pars.replace("contextus_desine", "contextus_parseris")
        mutatum = True
    return textus[:initium] + pars + textus[finis:], mutatum


def propaga_vocationes(textus: str) -> tuple[str, bool]:
    lineae = textus.splitlines(keepends=True)
    mutatum = False
    for i, linea in enumerate(lineae):
        if linea.lstrip().startswith("FUNCTIO "):
            continue
        for nomen in VOCATIONES_CONTEXTUS:
            if f"{nomen}(" not in linea:
                continue
            if "contextus_parseris" in linea:
                continue
            vetus = ", n, tabula)"
            if vetus not in linea:
                raise SystemExit(
                    f"ERRATUM: vocatio {nomen} sine forma exspectata in linea {i + 1}: {linea.strip()}"
                )
            lineae[i] = linea.replace(vetus, ", n, tabula, contextus_parseris)")
            linea = lineae[i]
            mutatum = True
    return "".join(lineae), mutatum


def verifica_propagationem(textus: str) -> None:
    for i, linea in enumerate(textus.splitlines(), 1):
        if linea.lstrip().startswith("FUNCTIO "):
            continue
        for nomen in VOCATIONES_CONTEXTUS:
            if f"{nomen}(" in linea and "contextus_parseris" not in linea:
                raise SystemExit(
                    f"ERRATUM: contextus non propagatus ad {nomen} in linea {i}: {linea.strip()}"
                )


def principale() -> None:
    textus = FONS.read_text(encoding="utf-8")
    mutatum = False

    for vetus, novus, nomen in (
        (VETUS_DESINE_LEGE, NOVUS_DESINE_LEGE, "desine-lege"),
        (VETUS_DESINE_SCRIBE, NOVUS_DESINE_SCRIBE, "desine-scribe"),
        (VETUS_LECTIO_LEGE, NOVUS_LECTIO_LEGE, "lectio-lege"),
        (VETUS_LECTIO_SCRIBE, NOVUS_LECTIO_SCRIBE, "lectio-scribe"),
        (VETUS_CONTEXTUS, NOVUS_CONTEXTUS, "contextus-principalis"),
    ):
        textus, m = muta_unum(textus, vetus, novus, nomen)
        mutatum = mutatum or m

    textus, m = rename_blocum_contextus(textus)
    mutatum = mutatum or m

    for nomen in FUNCTIONES_CONTEXTUS:
        textus, m = adde_contextum_functioni(textus, nomen)
        mutatum = mutatum or m

    # Call-sites accessorum ad contextum communem transferuntur.
    substitutiones = (
        ("STATUS_DESINE_LEGE(contextus_desine)", "STATUS_DESINE_LEGE(contextus_parseris)"),
        ("STATUS_DESINE_SCRIBE(contextus_desine,", "STATUS_DESINE_SCRIBE(contextus_parseris,"),
        ("STATUS_LECTIONIS_LEGE(tabula)", "STATUS_LECTIONIS_LEGE(contextus_parseris)"),
        ("STATUS_LECTIONIS_SCRIBE(tabula,", "STATUS_LECTIONIS_SCRIBE(contextus_parseris,"),
        ("contextus_desine = 0.", "CONTENTUM(contextus_parseris) = 0.\n                CONTENTUM(contextus_parseris + 8) = 0."),
        ("SEDES(contextus_desine)", "contextus_parseris"),
    )
    for vetus, novus in substitutiones:
        if vetus in textus:
            textus = textus.replace(vetus, novus)
            mutatum = True

    textus, m = propaga_vocationes(textus)
    mutatum = mutatum or m

    if "contextus_desine" in textus:
        raise SystemExit("ERRATUM: nomen contextus_desine post migrationem adhuc adest")
    if "tabula[2999]" in textus:
        raise SystemExit("ERRATUM: tabula[2999] post migrationem adhuc adest")
    verifica_propagationem(textus)

    for nomen in FUNCTIONES_CONTEXTUS + ("ANALYSA_BLOCUS",):
        initium, finis = fines_functionis(textus, nomen)
        pars = textus[initium:finis]
        if pars.count("ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.") != 1:
            raise SystemExit(f"ERRATUM: {nomen} contextum parseris non exacte semel accipit")

    FONS.write_text(textus, encoding="utf-8", newline="\n")

    lineae = BASIS.read_text(encoding="utf-8").splitlines()
    si_2999 = [i for i, linea in enumerate(lineae) if linea.strip() == "2999"]
    if len(si_2999) == 1:
        del lineae[si_2999[0]]
        mutatum = True
    elif len(si_2999) > 1:
        raise SystemExit("ERRATUM: index 2999 in basi plus semel adest")

    lineae = [
        "# Inventarium canonicum 2026-08-22: X indices, XCV accessus."
        if linea.startswith("# Inventarium canonicum 2026-08-22:")
        else linea
        for linea in lineae
    ]
    BASIS.write_text("\n".join(lineae) + "\n", encoding="utf-8", newline="\n")

    if mutatum:
        print("RECTE: status lectionis in contextum parseris communem migratus est.")
    else:
        print("RECTE: status lectionis iam extra tabulam est.")


if __name__ == "__main__":
    principale()
