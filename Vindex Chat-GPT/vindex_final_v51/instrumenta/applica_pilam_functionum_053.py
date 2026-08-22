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
    # Eadem series machinalis LV octetorum manet, sed constantes per SCRIBE_U32
    # scribuntur. Hoc fontem auto-hospitio multo leviorem facit quam LV
    # vocationes singulares CODEX_SCRIBE.
    return '''FUNCTIO COMPONE_RESERVA_PILA_PROBATA REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT indice SICUT NUMERUS.
    ACCIPIT spatium SICUT NUMERUS.
    DECLARA p SICUT NUMERUS VALENS indice.
    DECLARA ignoratum SICUT NUMERUS VALENS 0.

    // mov r11, imm64. Octeta immediata a CORRIGE_PILA post analysin corporis mutantur.
    CODEX_SCRIBE(codex, p, 73).
    CODEX_SCRIBE(codex, p + 1, 187).
    ignoratum = SCRIBE_U64(codex, p + 2, spatium).

    // Reliqua XLV octeta prologi in verbis U32 parvi ordinis scribuntur.
    ignoratum = SCRIBE_U32(codex, p + 10, 16482633).
    ignoratum = SCRIBE_U32(codex, p + 14, 1979711504).
    ignoratum = SCRIBE_U32(codex, p + 18, 3967895580).
    ignoratum = SCRIBE_U32(codex, p + 22, 4096).
    ignoratum = SCRIBE_U32(codex, p + 26, 604799816).
    ignoratum = SCRIBE_U32(codex, p + 30, 3951118592).
    ignoratum = SCRIBE_U32(codex, p + 34, 4096).
    ignoratum = SCRIBE_U32(codex, p + 38, 16482633).
    ignoratum = SCRIBE_U32(codex, p + 42, 1996488720).
    ignoratum = SCRIBE_U32(codex, p + 46, 3693694180).
    ignoratum = SCRIBE_U32(codex, p + 50, 604799816).
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

    mutationes_mensurae = 0
    for index in (1, 2):
        vetus = (
            f"DECLARA spatium_necessarium{index} SICUT NUMERUS VALENS "
            "(0 - tabula[51]) + 10000."
        )
        novum = (
            f"DECLARA spatium_necessarium{index} SICUT NUMERUS VALENS "
            "(((0 - tabula[51]) + 15) / 16) * 16."
        )
        si_vetus = textus.count(vetus)
        si_novum = textus.count(novum)
        if si_vetus == 1 and si_novum == 0:
            textus = textus.replace(vetus, novum, 1)
            mutationes_mensurae += 1
        elif not (si_vetus == 0 and si_novum == 1):
            raise SystemExit(
                f"ERRATUM: status mensurae pilae {index} ambiguus est "
                f"(vetus={si_vetus}, novum={si_novum})"
            )

    VIA.write_text(textus, encoding="utf-8", newline="\n")

    if adiutor_mutatus:
        print("RECTE: emissor pilae compactus est; eadem series machinalis LV octetorum servatur.")
    elif mutationes_mensurae:
        print("RECTE: pila functionum exacte dimensata et per paginas probata est.")
    else:
        print("RECTE: pila functionum iam structurata et compacte emissa est.")


if __name__ == "__main__":
    applica()
