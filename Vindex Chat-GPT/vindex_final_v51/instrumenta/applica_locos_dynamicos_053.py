#!/usr/bin/env python3
"""VINDEX 0.53: metadata variabilium localium ad tabulam dynamicam migrat."""

from pathlib import Path
import re

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "FUNCTIO INITIA_LOCA_DYNAMICA REDDENS NUMERUS."


def substitue_functio(textus: str, nomen: str, novum: str) -> str:
    regula = re.compile(
        rf"FUNCTIO {re.escape(nomen)} REDDENS NUMERUS\.\n.*?\nFIN-FUNCTIO\.",
        re.S,
    )
    novus, numerus = regula.subn(novum.strip(), textus, count=1)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: functio {nomen} {numerus} vicibus substituta est")
    return novus


def substitue_assignationem(textus: str, index: str, campus: int, formae: list[str]) -> str:
    numerus = 0
    for forma in formae:
        regula = re.compile(
            rf"(?m)^(?P<sp>\s*)tabula\[{forma}\]\s*=\s*(?P<valor>.+)\.$"
        )
        textus, n = regula.subn(
            rf"\g<sp>LOCALE_SCRIBE(tabula, {index}, {campus}, \g<valor>).",
            textus,
        )
        numerus += n
    return textus


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")
    if MARCA in textus:
        print("RECTE: loca dynamica iam applicata sunt.")
        return

    adiutores = r'''
FUNCTIO INITIA_LOCA_DYNAMICA REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    DECLARA capacitas SICUT NUMERUS VALENS 64.
    DECLARA basis SICUT NUMERUS VALENS RESERVA_OCTETA(capacitas * 48).
    SI basis < 0 TUNC
        REDDE 71.
    FIN-SI.
    tabula[2970] = basis.
    tabula[2971] = capacitas.
    tabula[2972] = 0.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO ASSECURA_LOCA_DYNAMICA REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT necessaria SICUT NUMERUS.
    DECLARA capacitas SICUT NUMERUS VALENS tabula[2971].
    SI necessaria <= capacitas TUNC
        REDDE 0.
    FIN-SI.
    DECLARA nova_capacitas SICUT NUMERUS VALENS capacitas * 2.
    DUM nova_capacitas < necessaria PERFICE
        nova_capacitas = nova_capacitas * 2.
    FIN-DUM.
    DECLARA nova_basis SICUT NUMERUS VALENS RESERVA_OCTETA(nova_capacitas * 48).
    SI nova_basis < 0 TUNC
        REDDE 71.
    FIN-SI.
    DECLARA basis SICUT NUMERUS VALENS tabula[2970].
    DECLARA numerus SICUT NUMERUS VALENS tabula[2972].
    DECLARA i SICUT NUMERUS VALENS 0.
    DECLARA octeta SICUT NUMERUS VALENS numerus * 48.
    DUM i < octeta PERFICE
        SCRIBE_OCTETUM_AB(nova_basis + i, OCTETUS_AB(basis + i)).
        i = i + 1.
    FIN-DUM.
    tabula[2970] = nova_basis.
    tabula[2971] = nova_capacitas.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO LOCALE_LEGE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT index SICUT NUMERUS.
    ACCIPIT campus SICUT NUMERUS.
    SI index < 0 || index >= tabula[2972] TUNC
        REDDE 0.
    FIN-SI.
    DECLARA sedes_localis SICUT NUMERUS VALENS tabula[2970] + (index * 48) + (campus * 8).
    REDDE CONTENTUM(sedes_localis).
FIN-FUNCTIO.

FUNCTIO LOCALE_SCRIBE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT index SICUT NUMERUS.
    ACCIPIT campus SICUT NUMERUS.
    ACCIPIT valor SICUT NUMERUS.
    DECLARA status SICUT NUMERUS VALENS ASSECURA_LOCA_DYNAMICA(tabula, index + 1).
    SI status != 0 TUNC
        REDDE status.
    FIN-SI.
    DECLARA basis SICUT NUMERUS VALENS tabula[2970].
    SI campus == 0 && index >= tabula[2972] TUNC
        DECLARA z SICUT NUMERUS VALENS 0.
        DUM z < 48 PERFICE
            SCRIBE_OCTETUM_AB(basis + (index * 48) + z, 0).
            z = z + 1.
        FIN-DUM.
    FIN-SI.
    DECLARA sedes_localis SICUT NUMERUS VALENS basis + (index * 48) + (campus * 8).
    CONTENTUM(sedes_localis) = valor.
    SI index >= tabula[2972] TUNC
        tabula[2972] = index + 1.
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO RESTITUE_LOCA_DYNAMICA REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    tabula[2972] = 0.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO PROXIMUS_LOCUS_LIBER REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    REDDE tabula[2972].
FIN-FUNCTIO.
'''

    textus = substitue_functio(textus, "PROXIMUS_LOCUS_LIBER", adiutores)

    textus = substitue_functio(
        textus,
        "CERCA_VARIABILEM",
        r'''
FUNCTIO CERCA_VARIABILEM REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT nomen SICUT NUMERUS.
    DECLARA idx SICUT NUMERUS VALENS 0.
    DECLARA intervallum_inventus SICUT NUMERUS VALENS 0.
    DECLARA aliquid_inventum SICUT NUMERUS VALENS 0.
    DUM idx < tabula[2972] PERFICE
        SI LOCALE_LEGE(tabula, idx, 0) == nomen TUNC
            intervallum_inventus = LOCALE_LEGE(tabula, idx, 1).
            aliquid_inventum = 1.
        FIN-SI.
        idx = idx + 1.
    FIN-DUM.
    SI aliquid_inventum == 1 TUNC
        REDDE intervallum_inventus.
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.
''',
    )

    textus = substitue_functio(
        textus,
        "ESTNE_SERIES",
        r'''
FUNCTIO ESTNE_SERIES REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT nomen SICUT NUMERUS.
    DECLARA idx SICUT NUMERUS VALENS 0.
    DECLARA signum_inventum SICUT NUMERUS VALENS 0.
    DECLARA aliquid_inventum SICUT NUMERUS VALENS 0.
    DUM idx < tabula[2972] PERFICE
        SI LOCALE_LEGE(tabula, idx, 0) == nomen TUNC
            signum_inventum = LOCALE_LEGE(tabula, idx, 2).
            aliquid_inventum = 1.
        FIN-SI.
        idx = idx + 1.
    FIN-DUM.
    SI aliquid_inventum == 1 TUNC
        REDDE signum_inventum.
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.
''',
    )

    textus = substitue_functio(
        textus,
        "MAGNITUDO_VARIABILIS",
        r'''
FUNCTIO MAGNITUDO_VARIABILIS REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT nomen SICUT NUMERUS.
    DECLARA idx SICUT NUMERUS VALENS 0.
    DECLARA magnitudo_inventa SICUT NUMERUS VALENS 0.
    DECLARA aliquid_inventum_mag SICUT NUMERUS VALENS 0.
    DUM idx < tabula[2972] PERFICE
        SI LOCALE_LEGE(tabula, idx, 0) == nomen TUNC
            magnitudo_inventa = LOCALE_LEGE(tabula, idx, 3).
            aliquid_inventum_mag = 1.
        FIN-SI.
        idx = idx + 1.
    FIN-DUM.
    SI aliquid_inventum_mag == 1 TUNC
        REDDE magnitudo_inventa.
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.
''',
    )

    textus = substitue_functio(
        textus,
        "STRUCTURA_VARIABILIS",
        r'''
FUNCTIO STRUCTURA_VARIABILIS REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT nomen SICUT NUMERUS.
    DECLARA idx SICUT NUMERUS VALENS 0.
    DECLARA resultatum SICUT NUMERUS VALENS 0.
    DUM idx < tabula[2972] PERFICE
        SI LOCALE_LEGE(tabula, idx, 0) == nomen TUNC
            resultatum = LOCALE_LEGE(tabula, idx, 4).
        FIN-SI.
        idx = idx + 1.
    FIN-DUM.
    REDDE resultatum.
FIN-FUNCTIO.
''',
    )

    textus = substitue_functio(
        textus,
        "EST_FLUITANS_VARIABILIS",
        r'''
FUNCTIO EST_FLUITANS_VARIABILIS REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT nomen SICUT NUMERUS.
    DECLARA idx SICUT NUMERUS VALENS 0.
    DECLARA resultatum SICUT NUMERUS VALENS 0.
    DUM idx < tabula[2972] PERFICE
        SI LOCALE_LEGE(tabula, idx, 0) == nomen TUNC
            resultatum = LOCALE_LEGE(tabula, idx, 5).
        FIN-SI.
        idx = idx + 1.
    FIN-DUM.
    REDDE resultatum.
FIN-FUNCTIO.
''',
    )

    indices = re.findall(
        r"DECLARA\s+([A-Za-z_][A-Za-z0-9_]*)\s+SICUT NUMERUS VALENS PROXIMUS_LOCUS_LIBER\(tabula\)\.",
        textus,
    )
    if len(indices) < 6:
        raise SystemExit(f"ERRATUM: tantum {len(indices)} insertiones localium inventae sunt")

    for index in sorted(set(indices), key=len, reverse=True):
        e = re.escape(index)
        textus = substitue_assignationem(textus, index, 0, [e])
        textus = substitue_assignationem(textus, index, 1, [rf"{e}\s*\+\s*100", rf"100\s*\+\s*{e}"])
        textus = substitue_assignationem(textus, index, 2, [rf"228\s*\+\s*{e}", rf"{e}\s*\+\s*228"])
        textus = substitue_assignationem(textus, index, 3, [rf"850\s*\+\s*{e}", rf"{e}\s*\+\s*850"])
        textus = substitue_assignationem(textus, index, 4, [rf"2300\s*\+\s*{e}", rf"{e}\s*\+\s*2300"])
        textus = substitue_assignationem(textus, index, 5, [rf"2400\s*\+\s*{e}", rf"{e}\s*\+\s*2400"])

        lecturae = [
            (rf"tabula\[{e}\s*\+\s*100\]", 1),
            (rf"tabula\[100\s*\+\s*{e}\]", 1),
            (rf"tabula\[228\s*\+\s*{e}\]", 2),
            (rf"tabula\[{e}\s*\+\s*228\]", 2),
            (rf"tabula\[850\s*\+\s*{e}\]", 3),
            (rf"tabula\[{e}\s*\+\s*850\]", 3),
            (rf"tabula\[2300\s*\+\s*{e}\]", 4),
            (rf"tabula\[{e}\s*\+\s*2300\]", 4),
            (rf"tabula\[2400\s*\+\s*{e}\]", 5),
            (rf"tabula\[{e}\s*\+\s*2400\]", 5),
            (rf"tabula\[{e}\]", 0),
        ]
        for regula, campus in lecturae:
            textus = re.sub(regula, f"LOCALE_LEGE(tabula, {index}, {campus})", textus)

    vetus_clear1 = '''                DECLARA k_clear1 SICUT NUMERUS VALENS 0.
                DUM k_clear1 < 100 PERFICE
                    tabula[k_clear1] = 0.
                    tabula[k_clear1 + 228] = 0.
                    tabula[k_clear1 + 850] = 0.
                    tabula[k_clear1 + 2300] = 0.
                    tabula[k_clear1 + 2400] = 0.
                    k_clear1 = k_clear1 + 1.
                FIN-DUM.'''
    novum_clear1 = '''                DECLARA k_clear1 SICUT NUMERUS VALENS RESTITUE_LOCA_DYNAMICA(tabula).'''
    if textus.count(vetus_clear1) != 1:
        raise SystemExit("ERRATUM: purgatio localium PRINCIPALIS non unica est")
    textus = textus.replace(vetus_clear1, novum_clear1, 1)

    vetus_clear2 = '''                DECLARA k_clear2 SICUT NUMERUS VALENS 0.
                DUM k_clear2 < 100 PERFICE
                    tabula[k_clear2] = 0.
                    tabula[k_clear2 + 228] = 0.
                    tabula[k_clear2 + 850] = 0.
                    tabula[k_clear2 + 2300] = 0.
                    tabula[k_clear2 + 2400] = 0.
                    k_clear2 = k_clear2 + 1.
                FIN-DUM.'''
    novum_clear2 = '''                DECLARA k_clear2 SICUT NUMERUS VALENS RESTITUE_LOCA_DYNAMICA(tabula).'''
    if textus.count(vetus_clear2) != 1:
        raise SystemExit("ERRATUM: purgatio localium functionis non unica est")
    textus = textus.replace(vetus_clear2, novum_clear2, 1)

    declaratio = "    DECLARA tabula SICUT ORDO DE NUMERUS CAPACITAS 3000.\n"
    if textus.count(declaratio) != 1:
        raise SystemExit("ERRATUM: declaratio tabulae principalis non unica est")
    initium = declaratio + '''    DECLARA status_locorum_dynam SICUT NUMERUS VALENS INITIA_LOCA_DYNAMICA(tabula).
    SI status_locorum_dynam != 0 TUNC
        PROCLAMA "ERRATUM: memoria symbolorum localium reservata non est".
        REDDE 71.
    FIN-SI.
'''
    textus = textus.replace(declaratio, initium, 1)

    caput_vetus = '''// Ordinatio tabulae (structura partitionis unicae "tabula"):
//   0-99    : nomina variabilium localium (100 loca)
//   100-199 : intervalla variabilium localium (100 loca)
//   200-225 : nomina camporum structurae (26 loca)
//   226     : numerus acervi (pro RESERVA)
//   227     : locus pendens DESINE (pro ansis)
//   228-327 : signa "est_series" variabilium (100 loca, 1=tabula localis, 2=parametrum tabulae)
//   328-407 : nomina functionum auxiliarium (80 loca)
//   408-487 : positiones functionum auxiliarium (80 loca)
//   488     : numerus vocationum pendentium (relationes anteriores)
//   490-821 : par (locus, nomen) pro singulis vocationibus pendentibus (166 paria)
// Capacitas tabulae tota: 850.'''
    caput_novum = '''// Ordinatio tabulae historica ad metadata non-localia adhuc adhibetur.
// Symbola localia iam extra regiones 0-99, 100-199, 228-327, 850+, 2300+ et 2400+ servantur.
// Descriptor localium in tabula: 2970=basis, 2971=capacitas, 2972=numerus.
// Unum symbolum locale XLVIII octeta habet: nomen, intervallum, series, magnitudo, structura, fluitans.
// Locus 51 cursor pilae functionis manet; regiones ceterae paulatim in gradibus posterioribus migrabuntur.'''
    if caput_vetus not in textus:
        raise SystemExit("ERRATUM: descriptio tabulae historica non inventa est")
    textus = textus.replace(caput_vetus, caput_novum, 1)

    reliquiae = [
        r"DUM idx < 100 && tabula\[idx\] != 0",
        r"tabula\[228\s*\+\s*idx_[A-Za-z0-9_]+\]",
        r"tabula\[850\s*\+\s*idx_[A-Za-z0-9_]+\]",
        r"tabula\[2300\s*\+\s*idx_[A-Za-z0-9_]+\]",
        r"tabula\[2400\s*\+\s*idx_[A-Za-z0-9_]+\]",
        r"tabula\[idx_[A-Za-z0-9_]+\s*\+\s*100\]",
    ]
    for regula in reliquiae:
        if re.search(regula, textus):
            raise SystemExit(f"ERRATUM: reliquia localium fixa manet: {regula}")

    VIA.write_text(textus, encoding="utf-8")
    print(
        "RECTE: symbola localia descriptorio dynamico utuntur; "
        f"insertiones={len(indices)}, indices={','.join(sorted(set(indices)))}."
    )


if __name__ == "__main__":
    applica()
