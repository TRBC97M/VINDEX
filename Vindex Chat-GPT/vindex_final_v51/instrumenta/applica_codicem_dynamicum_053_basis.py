#!/usr/bin/env python3
"""VINDEX 0.53: receptaculum codicis machinalis descriptorio crescibili substituit."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "FUNCTIO INITIA_CODEX REDDENS NUMERUS."
VETUS_PARAM = "ACCIPIT codex SICUT ORDO DE NUMERUS."
NOVUS_PARAM = "ACCIPIT codex SICUT ACUS<NUMERUS>."


def exige_unum(textus: str, exemplar: str, nomen: str) -> None:
    n = textus.count(exemplar)
    if n != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {n} vicibus inventa est")


def clausura(textus: str, initium: int) -> int:
    """Indicem ']' parem post 'codex[' invenit, etiam si index alias [] continet."""
    profunditas = 1
    i = initium
    while i < len(textus):
        c = textus[i]
        if c == "[":
            profunditas += 1
        elif c == "]":
            profunditas -= 1
            if profunditas == 0:
                return i
        i += 1
    raise SystemExit("ERRATUM: clausura codex[...] deest")


def converte_lineam(linea: str) -> tuple[str, int, int]:
    """Scripturas directas et lectiones codicis in accessores descriptorii mutat."""
    scripturae = 0
    lectiones = 0
    initium = linea.find("codex[")
    if initium < 0:
        return linea, scripturae, lectiones

    # Assignatio cuius latus sinistrum codex[...] est.
    si = len(linea) - len(linea.lstrip())
    if initium == si:
        finis = clausura(linea, initium + len("codex["))
        reliquum = linea[finis + 1 :]
        if reliquum.startswith(" = ") and linea.rstrip().endswith("."):
            index = linea[initium + len("codex[") : finis]
            valor = reliquum[3:].rstrip()
            valor = valor[:-1]
            linea = linea[:initium] + f"CODEX_SCRIBE(codex, {index}, {valor}).\n"
            scripturae += 1
            return linea, scripturae, lectiones

    # Cetera codex[...] sunt lectiones; substitutio a dextra ad sinistram iteratur.
    dum = True
    while dum:
        initium = linea.rfind("codex[")
        if initium < 0:
            break
        finis = clausura(linea, initium + len("codex["))
        index = linea[initium + len("codex[") : finis]
        linea = linea[:initium] + f"CODEX_LEGE(codex, {index})" + linea[finis + 1 :]
        lectiones += 1
    return linea, scripturae, lectiones


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")
    if MARCA in textus and "CAPACITAS 300000" not in textus and VETUS_PARAM not in textus:
        print("RECTE: codex dynamicus iam applicatus est.")
        return

    numerus_parametrorum = textus.count(VETUS_PARAM)
    if numerus_parametrorum == 0:
        raise SystemExit("ERRATUM: parametri codicis veteres non inventi sunt")
    textus = textus.replace(VETUS_PARAM, NOVUS_PARAM)

    lineae = []
    scripturae = 0
    lectiones = 0
    for linea in textus.splitlines(keepends=True):
        nova, s, l = converte_lineam(linea)
        lineae.append(nova)
        scripturae += s
        lectiones += l
    textus = "".join(lineae)

    if "codex[" in textus:
        raise SystemExit("ERRATUM: accessus directus codex[...] post conversionem manet")

    ancora = "FUNCTIO SCRIBE_U16 REDDENS NUMERUS.\n"
    exige_unum(textus, ancora, "prima-functio-codicis")
    adiutores = '''FUNCTIO INITIA_CODEX REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT limen SICUT NUMERUS.
    DECLARA basis SICUT NUMERUS VALENS RESERVA_OCTETA(limen).
    SI basis < 0 TUNC
        REDDE 71.
    FIN-SI.
    CONTENTUM(codex) = basis.
    CONTENTUM(codex + 8) = limen.
    CONTENTUM(codex + 16) = 0.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO ASSECURA_CODEX REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT necessaria SICUT NUMERUS.
    DECLARA limen SICUT NUMERUS VALENS CONTENTUM(codex + 8).
    SI necessaria <= limen TUNC
        REDDE 0.
    FIN-SI.
    DECLARA novum_limen SICUT NUMERUS VALENS limen * 2.
    DUM novum_limen < necessaria PERFICE
        novum_limen = novum_limen * 2.
    FIN-DUM.
    DECLARA nova_basis SICUT NUMERUS VALENS RESERVA_OCTETA(novum_limen).
    SI nova_basis < 0 TUNC
        REDDE 71.
    FIN-SI.
    DECLARA basis SICUT NUMERUS VALENS CONTENTUM(codex).
    DECLARA longitudo SICUT NUMERUS VALENS CONTENTUM(codex + 16).
    DECLARA i SICUT NUMERUS VALENS 0.
    DUM i < longitudo PERFICE
        SCRIBE_OCTETUM_AB(nova_basis + i, OCTETUS_AB(basis + i)).
        i = i + 1.
    FIN-DUM.
    CONTENTUM(codex) = nova_basis.
    CONTENTUM(codex + 8) = novum_limen.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO CODEX_SCRIBE REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT index SICUT NUMERUS.
    ACCIPIT valor SICUT NUMERUS.
    DECLARA necessaria SICUT NUMERUS VALENS index + 1.
    DECLARA status SICUT NUMERUS VALENS ASSECURA_CODEX(codex, necessaria).
    SI status != 0 TUNC
        REDDE status.
    FIN-SI.
    SCRIBE_OCTETUM_AB(CONTENTUM(codex) + index, valor).
    SI necessaria > CONTENTUM(codex + 16) TUNC
        CONTENTUM(codex + 16) = necessaria.
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO CODEX_LEGE REDDENS NUMERUS.
    ACCIPIT codex SICUT ACUS<NUMERUS>.
    ACCIPIT index SICUT NUMERUS.
    REDDE OCTETUS_AB(CONTENTUM(codex) + index).
FIN-FUNCTIO.

'''
    textus = textus.replace(ancora, adiutores + ancora, 1)

    vetus_decl = "    DECLARA codex SICUT ORDO DE NUMERUS CAPACITAS 300000.\n"
    novum_decl = '''    DECLARA codex SICUT ORDO DE NUMERUS CAPACITAS 3.
    DECLARA status_initii_codicis SICUT NUMERUS VALENS INITIA_CODEX(codex, 65536).
    SI status_initii_codicis != 0 TUNC
        PROCLAMA "ERRATUM: memoria codicis reservata non est".
        REDDE 71.
    FIN-SI.
'''
    exige_unum(textus, vetus_decl, "declaratio-codicis")
    textus = textus.replace(vetus_decl, novum_decl, 1)

    vetus_scriptio = '''    DECLARA scriptum SICUT NUMERUS VALENS MITTE(fd_scriptio, codex, pos).
    CLAUDE(fd_scriptio).
    SI scriptum != pos TUNC
        PROCLAMA "ERRATUM: exsecutabile imperfecte scriptum est".
        REDDE 74.
    FIN-SI.
'''
    novum_scriptio = '''    DECLARA buffer_scriptio SICUT ORDO DE NUMERUS CAPACITAS 4096.
    DECLARA index_scriptio SICUT NUMERUS VALENS 0.
    DECLARA scriptum SICUT NUMERUS VALENS 0.
    DUM index_scriptio < pos PERFICE
        DECLARA longitudo_partis SICUT NUMERUS VALENS pos - index_scriptio.
        SI longitudo_partis > 4096 TUNC
            longitudo_partis = 4096.
        FIN-SI.
        DECLARA j_scriptio SICUT NUMERUS VALENS 0.
        DUM j_scriptio < longitudo_partis PERFICE
            buffer_scriptio[j_scriptio] = CODEX_LEGE(codex, index_scriptio + j_scriptio).
            j_scriptio = j_scriptio + 1.
        FIN-DUM.
        DECLARA scriptum_partis SICUT NUMERUS VALENS MITTE(fd_scriptio, buffer_scriptio, longitudo_partis).
        SI scriptum_partis != longitudo_partis TUNC
            CLAUDE(fd_scriptio).
            PROCLAMA "ERRATUM: exsecutabile imperfecte scriptum est".
            REDDE 74.
        FIN-SI.
        scriptum = scriptum + scriptum_partis.
        index_scriptio = index_scriptio + longitudo_partis.
    FIN-DUM.
    CLAUDE(fd_scriptio).
    SI scriptum != pos TUNC
        PROCLAMA "ERRATUM: exsecutabile imperfecte scriptum est".
        REDDE 74.
    FIN-SI.
'''
    exige_unum(textus, vetus_scriptio, "scriptio-finalis")
    textus = textus.replace(vetus_scriptio, novum_scriptio, 1)

    if "CAPACITAS 300000" in textus or VETUS_PARAM in textus or "codex[" in textus:
        raise SystemExit("ERRATUM: reliquiae receptaculi codicis fixi manent")

    VIA.write_text(textus, encoding="utf-8")
    print(
        "RECTE: codex descriptorio crescibili utitur; "
        f"parametri={numerus_parametrorum}, scripturae={scripturae}, lectiones={lectiones}."
    )


if __name__ == "__main__":
    applica()
