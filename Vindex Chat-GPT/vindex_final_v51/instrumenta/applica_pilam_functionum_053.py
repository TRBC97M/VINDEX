#!/usr/bin/env python3
"""VINDEX 0.53: pilam functionum exacte dimensam et per paginas probatam applicat."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "FUNCTIO COMPONE_RESERVA_PILA_PROBATA REDDENS NUMERUS."
ANCORA = "FUNCTIO COMPONE_ARITHMETICA REDDENS NUMERUS.\n"


def exige(textus: str, fragmentum: str, numerus: int, nomen: str) -> None:
    inventa = textus.count(fragmentum)
    if inventa != numerus:
        raise SystemExit(
            f"ERRATUM: ancora {nomen} {inventa} vicibus inventa est; {numerus} exspectabantur"
        )


def adiutor_compactus() -> str:
    # Eadem series machinalis LV octetorum manet. Commentaria intra corpus
    # VINDEX consulto omittuntur: diagnostica auto-hospitii formam sine
    # commentariis probavit, dum forma canonica commentata iter nativum tardabat.
    return '''FUNCTIO COMPONE_RESERVA_PILA_PROBATA REDDENS NUMERUS.
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


def compone_adiutorem_si_necesse(textus: str) -> tuple[str, bool]:
    novus = adiutor_compactus()

    if MARCA not in textus:
        exige(textus, ANCORA, 1, "emissoris-pilae")
        return textus.replace(ANCORA, novus + ANCORA, 1), True

    initium = textus.index(MARCA)
    try:
        finis = textus.index(ANCORA, initium)
    except ValueError as exc:
        raise SystemExit("ERRATUM: finis emissoris pilae non inventus est") from exc

    vetus = textus[initium:finis]
    if vetus == novus:
        return textus, False

    return textus[:initium] + novus + textus[finis:], True


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")
    textus, adiutor_mutatus = compone_adiutorem_si_necesse(textus)

    vetus_prologus = (
        "                pos = COMPONE_ONERA(codex, pos, 0, 30000).\n"
        "                pos = COMPONE_SUB(codex, pos, 4, 0)."
    )
    novus_prologus = "                pos = COMPONE_RESERVA_PILA_PROBATA(codex, pos, 0)."
    si_vetus_prologus = textus.count(vetus_prologus)
    si_novus_prologus = textus.count(novus_prologus)
    if si_vetus_prologus == 2 and si_novus_prologus == 0:
        textus = textus.replace(vetus_prologus, novus_prologus)
    elif not (si_vetus_prologus == 0 and si_novus_prologus == 2):
        raise SystemExit(
            "ERRATUM: status prologorum functionum ambiguus est "
            f"(veteres={si_vetus_prologus}, novi={si_novus_prologus})"
        )

    # PRINCIPALIS non est ipsum punctum ingressus ELF: involucrum a compilatore
    # genitum eam per CALL vocat. Itaque PRINCIPALIS et functiones ordinariae
    # eandem ordinationem fasciculi, 0 modulo XVI, requirunt.
    mutationes_mensurae = 0
    mensurae = (
        (
            1,
            "DECLARA spatium_necessarium1 SICUT NUMERUS VALENS (0 - tabula[51]) + 10000.",
            "DECLARA spatium_necessarium1 SICUT NUMERUS VALENS ((((0 - tabula[51]) + 7) / 16) * 16) + 8.",
            "DECLARA spatium_necessarium1 SICUT NUMERUS VALENS (((0 - tabula[51]) + 15) / 16) * 16.",
        ),
        (
            2,
            "DECLARA spatium_necessarium2 SICUT NUMERUS VALENS (0 - tabula[51]) + 10000.",
            None,
            "DECLARA spatium_necessarium2 SICUT NUMERUS VALENS (((0 - tabula[51]) + 15) / 16) * 16.",
        ),
    )

    for index, vetus, intermedia, novum in mensurae:
        si_vetus = textus.count(vetus)
        si_intermedia = textus.count(intermedia) if intermedia else 0
        si_novum = textus.count(novum)

        if si_novum == 1 and si_vetus == 0 and si_intermedia == 0:
            continue
        if si_vetus == 1 and si_intermedia == 0 and si_novum == 0:
            textus = textus.replace(vetus, novum, 1)
            mutationes_mensurae += 1
            continue
        if intermedia and si_vetus == 0 and si_intermedia == 1 and si_novum == 0:
            textus = textus.replace(intermedia, novum, 1)
            mutationes_mensurae += 1
            continue

        raise SystemExit(
            f"ERRATUM: status mensurae pilae {index} ambiguus est "
            f"(vetus={si_vetus}, intermedia={si_intermedia}, novum={si_novum})"
        )

    # Vocationes generales argumenta in pilam temporaliter imponunt et deinde
    # in registra SysV auferunt. Prior codex RDI semper auferebat etiam cum
    # numerus_argumentorum == 0; sic unaquaeque vocatio nulla RSP octo octetis
    # sursum movebat. Fasciculus vetus +10000 hoc vitium occultabat.
    vetus_pop = (
        "        SI numerus_argumentorum >= 2 TUNC\n"
        "            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 6).\n"
        "        FIN-SI.\n"
        "        CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 7).\n\n"
        "        DECLARA loci_fn SICUT NUMERUS VALENS CERCA_FUNCTIONEM_DYNAMICAM(tabula, nomen_fn)."
    )
    novus_pop = (
        "        SI numerus_argumentorum >= 2 TUNC\n"
        "            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 6).\n"
        "        FIN-SI.\n"
        "        SI numerus_argumentorum >= 1 TUNC\n"
        "            CONTENTUM(pos_codicis) = COMPONE_AUFER(codex, CONTENTUM(pos_codicis), 7).\n"
        "        FIN-SI.\n\n"
        "        DECLARA loci_fn SICUT NUMERUS VALENS CERCA_FUNCTIONEM_DYNAMICAM(tabula, nomen_fn)."
    )
    si_vetus_pop = textus.count(vetus_pop)
    si_novus_pop = textus.count(novus_pop)
    vocatio_mutata = False
    if si_vetus_pop == 1 and si_novus_pop == 0:
        textus = textus.replace(vetus_pop, novus_pop, 1)
        vocatio_mutata = True
    elif not (si_vetus_pop == 0 and si_novus_pop == 1):
        raise SystemExit(
            "ERRATUM: status vocationum sine argumentis ambiguus est "
            f"(vetus={si_vetus_pop}, novus={si_novus_pop})"
        )

    VIA.write_text(textus, encoding="utf-8", newline="\n")

    if adiutor_mutatus or mutationes_mensurae or vocatio_mutata:
        print("RECTE: pila exacta est et vocationes sine argumentis RSP servant.")
    else:
        print("RECTE: pila exacta et vocationes sine argumentis iam canonicae sunt.")


if __name__ == "__main__":
    applica()
