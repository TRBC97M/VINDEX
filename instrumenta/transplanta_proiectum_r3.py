#!/usr/bin/env python3
"""R3: PROIECTUM 0.53 in compilatorem canonicum selective transplantat.

Instrumentum migrationis temporarium est. Omnes ancorae ante mutationem
verificantur; si una forma non est unica, nihil temere supponitur.
"""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
textus = VIA.read_text(encoding="utf-8")

if "FUNCTIO LEGE_PROIECTUM REDDENS NUMERUS." in textus:
    print("RECTE: PROIECTUM R3 iam in fonte est.")
    raise SystemExit(0)


def muta_semel(vetus: str, novus: str, titulus: str) -> None:
    global textus
    numerus = textus.count(vetus)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {titulus} inventa est {numerus} vicibus")
    textus = textus.replace(vetus, novus, 1)


muta_semel(
    '''    SI genus == 5 TUNC
        PROCLAMA "ERRATUM: fons importatus legi non potest".
    FIN-SI.
    REDDE 0.''',
    '''    SI genus == 5 TUNC
        PROCLAMA "ERRATUM: fons importatus legi non potest".
    FIN-SI.
    SI genus == 6 TUNC
        PROCLAMA "ERRATUM: proiectum VINDEX invalidum est".
    FIN-SI.
    REDDE 0.''',
    "diagnosticum-proiecti",
)

functiones = r'''// Partem relatam ad directorium manifesti componit.
FUNCTIO CONIUNGE_VIAM_PROIECTI REDDENS NUMERUS.
    ACCIPIT via_proiecti SICUT ACUS<LITTERA>.
    ACCIPIT pars SICUT ACUS<LITTERA>.

    DECLARA mensura_viae SICUT NUMERUS VALENS 0.
    DUM OCTETUS_AB(via_proiecti + mensura_viae) != 0 PERFICE
        mensura_viae = mensura_viae + 1.
    FIN-DUM.
    DECLARA mensura_partis SICUT NUMERUS VALENS 0.
    DUM OCTETUS_AB(pars + mensura_partis) != 0 PERFICE
        mensura_partis = mensura_partis + 1.
    FIN-DUM.

    DECLARA absoluta SICUT NUMERUS VALENS 0.
    SI mensura_partis > 0 && (OCTETUS_AB(pars) == 47 || OCTETUS_AB(pars) == 92) TUNC
        absoluta = 1.
    FIN-SI.
    SI mensura_partis > 1 && OCTETUS_AB(pars + 1) == 58 TUNC
        absoluta = 1.
    FIN-SI.

    DECLARA praefixum SICUT NUMERUS VALENS 0.
    SI absoluta == 0 TUNC
        DECLARA i_viae SICUT NUMERUS VALENS 0.
        DUM i_viae < mensura_viae PERFICE
            SI OCTETUS_AB(via_proiecti + i_viae) == 47 || OCTETUS_AB(via_proiecti + i_viae) == 92 TUNC
                praefixum = i_viae + 1.
            FIN-SI.
            i_viae = i_viae + 1.
        FIN-DUM.
    FIN-SI.

    DECLARA coniuncta SICUT NUMERUS VALENS RESERVA_OCTETA(praefixum + mensura_partis + 1).
    SI coniuncta < 0 TUNC
        REDDE coniuncta.
    FIN-SI.
    DECLARA i_praefixi SICUT NUMERUS VALENS 0.
    DUM i_praefixi < praefixum PERFICE
        SCRIBE_OCTETUM_AB(coniuncta + i_praefixi, OCTETUS_AB(via_proiecti + i_praefixi)).
        i_praefixi = i_praefixi + 1.
    FIN-DUM.
    DECLARA i_partis SICUT NUMERUS VALENS 0.
    DUM i_partis < mensura_partis PERFICE
        SCRIBE_OCTETUM_AB(coniuncta + praefixum + i_partis, OCTETUS_AB(pars + i_partis)).
        i_partis = i_partis + 1.
    FIN-DUM.
    SCRIBE_OCTETUM_AB(coniuncta + praefixum + mensura_partis, 0).
    REDDE coniuncta.
FIN-FUNCTIO.

FUNCTIO LEGE_CATHENAM_PROIECTI REDDENS NUMERUS.
    ACCIPIT fons SICUT ACUS<LITTERA>.
    ACCIPIT positio SICUT ACUS<NUMERUS>.
    ACCIPIT mensura SICUT NUMERUS.

    DECLARA ign_spat SICUT NUMERUS VALENS IGNORA_SPATIA(fons, positio, mensura).
    SI CONTENTUM(positio) >= mensura || fons[CONTENTUM(positio)] != 34 TUNC
        REDDE 0 - 1.
    FIN-SI.
    CONTENTUM(positio) = CONTENTUM(positio) + 1.
    DECLARA initium SICUT NUMERUS VALENS CONTENTUM(positio).
    DUM CONTENTUM(positio) < mensura && fons[CONTENTUM(positio)] != 34 PERFICE
        CONTENTUM(positio) = CONTENTUM(positio) + 1.
    FIN-DUM.
    SI CONTENTUM(positio) >= mensura || CONTENTUM(positio) == initium TUNC
        REDDE 0 - 1.
    FIN-SI.
    DECLARA finis SICUT NUMERUS VALENS CONTENTUM(positio).
    DECLARA cathena SICUT NUMERUS VALENS RESERVA_OCTETA(finis - initium + 1).
    SI cathena < 0 TUNC
        REDDE cathena.
    FIN-SI.
    DECLARA i_cathena SICUT NUMERUS VALENS 0.
    DUM initium + i_cathena < finis PERFICE
        SCRIBE_OCTETUM_AB(cathena + i_cathena, fons[initium + i_cathena]).
        i_cathena = i_cathena + 1.
    FIN-DUM.
    SCRIBE_OCTETUM_AB(cathena + i_cathena, 0).
    CONTENTUM(positio) = CONTENTUM(positio) + 1.
    REDDE cathena.
FIN-FUNCTIO.

FUNCTIO LEGE_PROIECTUM REDDENS NUMERUS.
    ACCIPIT via_proiecti SICUT ACUS<LITTERA>.
    ACCIPIT via_fons SICUT ACUS<NUMERUS>.
    ACCIPIT via_exitus SICUT ACUS<NUMERUS>.
    ACCIPIT modus_pe SICUT ACUS<NUMERUS>.

    DECLARA fd_proiecti SICUT NUMERUS VALENS APERI_LEGERE(via_proiecti).
    SI fd_proiecti < 0 TUNC
        PROCLAMA "ERRATUM: proiectum aperiri non potest".
        REDDE 66.
    FIN-SI.
    DECLARA n_proiecti SICUT NUMERUS VALENS 0.
    DECLARA basis_proiecti SICUT NUMERUS VALENS LEGE_TOTUM_DYNAMICUM(fd_proiecti, SEDES(n_proiecti)).
    CLAUDE(fd_proiecti).
    SI n_proiecti < 0 || basis_proiecti < 0 TUNC
        PROCLAMA "ERRATUM: proiectum legi non potest".
        REDDE 74.
    FIN-SI.
    DECLARA fons_proiecti SICUT ACUS<LITTERA> VALENS basis_proiecti.
    DECLARA pos_proiecti SICUT NUMERUS VALENS 0.
    DECLARA validum SICUT NUMERUS VALENS 1.
    DECLARA signum SICUT NUMERUS VALENS 0.

    DECLARA ign_p0 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
    signum = EXTRAHE_ET_SIGNA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
    SI signum != 70559585873586 TUNC
        validum = 0.
    FIN-SI.
    SI validum == 1 TUNC
        DECLARA ign_p1 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        signum = EXTRAHE_ET_SIGNA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI signum != 2531915292 TUNC
            validum = 0.
        FIN-SI.
    FIN-SI.
    SI validum == 1 TUNC
        DECLARA ign_p2 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI pos_proiecti >= n_proiecti || fons_proiecti[pos_proiecti] != 46 TUNC
            validum = 0.
        ALITER
            pos_proiecti = pos_proiecti + 1.
        FIN-SI.
    FIN-SI.

    DECLARA pars_fontis SICUT NUMERUS VALENS 0 - 1.
    SI validum == 1 TUNC
        DECLARA ign_p3 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        signum = EXTRAHE_ET_SIGNA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI signum != 2163790 TUNC
            validum = 0.
        ALITER
            pars_fontis = LEGE_CATHENAM_PROIECTI(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
            SI pars_fontis < 0 TUNC
                validum = 0.
            FIN-SI.
        FIN-SI.
    FIN-SI.
    SI validum == 1 TUNC
        DECLARA ign_p4 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI pos_proiecti >= n_proiecti || fons_proiecti[pos_proiecti] != 46 TUNC
            validum = 0.
        ALITER
            pos_proiecti = pos_proiecti + 1.
        FIN-SI.
    FIN-SI.

    DECLARA pars_exitus SICUT NUMERUS VALENS 0 - 1.
    SI validum == 1 TUNC
        DECLARA ign_p5 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        signum = EXTRAHE_ET_SIGNA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI signum != 70559457504167 TUNC
            validum = 0.
        ALITER
            pars_exitus = LEGE_CATHENAM_PROIECTI(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
            SI pars_exitus < 0 TUNC
                validum = 0.
            FIN-SI.
        FIN-SI.
    FIN-SI.
    SI validum == 1 TUNC
        DECLARA ign_p6 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI pos_proiecti >= n_proiecti || fons_proiecti[pos_proiecti] != 46 TUNC
            validum = 0.
        ALITER
            pos_proiecti = pos_proiecti + 1.
        FIN-SI.
    FIN-SI.

    SI validum == 1 TUNC
        DECLARA ign_p7 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        signum = EXTRAHE_ET_SIGNA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI signum != 1859104049771616 TUNC
            validum = 0.
        ALITER
            DECLARA ign_p8 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
            signum = EXTRAHE_ET_SIGNA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
            SI signum == 68735 TUNC
                CONTENTUM(modus_pe) = 0.
            ALITER
                SI signum == 2549 TUNC
                    CONTENTUM(modus_pe) = 1.
                ALITER
                    validum = 0.
                FIN-SI.
            FIN-SI.
        FIN-SI.
    FIN-SI.
    SI validum == 1 TUNC
        DECLARA ign_p9 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI pos_proiecti >= n_proiecti || fons_proiecti[pos_proiecti] != 46 TUNC
            validum = 0.
        ALITER
            pos_proiecti = pos_proiecti + 1.
        FIN-SI.
    FIN-SI.

    SI validum == 1 TUNC
        DECLARA ign_p10 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        signum = EXTRAHE_ET_SIGNA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI signum != 69611 TUNC
            validum = 0.
        FIN-SI.
    FIN-SI.
    SI validum == 1 TUNC
        DECLARA ign_p11 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI pos_proiecti >= n_proiecti || fons_proiecti[pos_proiecti] != 45 TUNC
            validum = 0.
        ALITER
            pos_proiecti = pos_proiecti + 1.
        FIN-SI.
    FIN-SI.
    SI validum == 1 TUNC
        DECLARA ign_p12 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        signum = EXTRAHE_ET_SIGNA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI signum != 70559585873586 TUNC
            validum = 0.
        FIN-SI.
    FIN-SI.
    SI validum == 1 TUNC
        DECLARA ign_p13 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI pos_proiecti >= n_proiecti || fons_proiecti[pos_proiecti] != 46 TUNC
            validum = 0.
        ALITER
            pos_proiecti = pos_proiecti + 1.
        FIN-SI.
    FIN-SI.
    SI validum == 1 TUNC
        DECLARA ign_p14 SICUT NUMERUS VALENS IGNORA_SPATIA(fons_proiecti, SEDES(pos_proiecti), n_proiecti).
        SI pos_proiecti != n_proiecti TUNC
            validum = 0.
        FIN-SI.
    FIN-SI.

    SI validum == 0 TUNC
        DECLARA ign_diag_proj SICUT NUMERUS VALENS DIAGNOSTICUM_FONTIS(via_proiecti, fons_proiecti, pos_proiecti, n_proiecti, 6).
        REDDE 65.
    FIN-SI.
    CONTENTUM(via_fons) = CONIUNGE_VIAM_PROIECTI(via_proiecti, pars_fontis).
    CONTENTUM(via_exitus) = CONIUNGE_VIAM_PROIECTI(via_proiecti, pars_exitus).
    SI CONTENTUM(via_fons) < 0 || CONTENTUM(via_exitus) < 0 TUNC
        PROCLAMA "ERRATUM: memoria proiecti reservata non est".
        REDDE 71.
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

'''

muta_semel(
    "FUNCTIO ASSECURA_BUFFERUM REDDENS NUMERUS.",
    functiones + "FUNCTIO ASSECURA_BUFFERUM REDDENS NUMERUS.",
    "functiones-proiecti",
)

vetus_initium = '''    SI argc < 3 TUNC
        PROCLAMA "USUS: compilator_vindex <fons.vindex> <exsecutabile> [pe]".
        REDDE 64.
    FIN-SI.

    DECLARA modus_pe SICUT NUMERUS VALENS 0.
    SI argc >= 4 TUNC
        DECLARA arg3 SICUT ACUS<LITTERA> VALENS argv[3].
        SI arg3[0] == 112 && arg3[1] == 101 && arg3[2] == 0 TUNC
            modus_pe = 1.
        FIN-SI.
    FIN-SI.

    DECLARA fd SICUT NUMERUS VALENS APERI_LEGERE(argv[1]).'''

novum_initium = '''    SI argc < 3 TUNC
        PROCLAMA "USUS: compilator_vindex <fons.vindex> <exsecutabile> [pe]".
        PROCLAMA "USUS: compilator_vindex PROIECTUM <proiectum.vindex>".
        REDDE 64.
    FIN-SI.

    DECLARA modus_proiecti SICUT NUMERUS VALENS 0.
    DECLARA modus_pe SICUT NUMERUS VALENS 0.
    DECLARA via_proiecti SICUT ACUS<LITTERA> VALENS 0.
    DECLARA via_fons SICUT ACUS<LITTERA> VALENS argv[1].
    DECLARA via_exitus SICUT ACUS<LITTERA> VALENS argv[2].
    DECLARA arg1 SICUT ACUS<LITTERA> VALENS argv[1].
    SI arg1[0] == 80 && arg1[1] == 82 && arg1[2] == 79 && arg1[3] == 73 && arg1[4] == 69 && arg1[5] == 67 && arg1[6] == 84 && arg1[7] == 85 && arg1[8] == 77 && arg1[9] == 0 TUNC
        modus_proiecti = 1.
        via_proiecti = argv[2].
        DECLARA status_proiecti SICUT NUMERUS VALENS LEGE_PROIECTUM(via_proiecti, SEDES(via_fons), SEDES(via_exitus), SEDES(modus_pe)).
        SI status_proiecti != 0 TUNC
            REDDE status_proiecti.
        FIN-SI.
    ALITER
        SI argc >= 4 TUNC
            DECLARA arg3 SICUT ACUS<LITTERA> VALENS argv[3].
            SI arg3[0] == 112 && arg3[1] == 101 && arg3[2] == 0 TUNC
                modus_pe = 1.
            FIN-SI.
        FIN-SI.
    FIN-SI.

    DECLARA fd SICUT NUMERUS VALENS APERI_LEGERE(via_fons).'''

muta_semel(vetus_initium, novum_initium, "initium-principalis-proiecti")

muta_semel(
    "            DECLARA fd_imp2 SICUT NUMERUS VALENS APERI_LEGERE(nomen_base_imp).",
    '''            DECLARA via_importi SICUT NUMERUS VALENS nomen_base_imp.
            SI modus_proiecti == 1 TUNC
                via_importi = CONIUNGE_VIAM_PROIECTI(via_proiecti, nomen_base_imp).
            FIN-SI.
            DECLARA fd_imp2 SICUT NUMERUS VALENS APERI_LEGERE(via_importi).''',
    "via-importi-proiecti",
)

muta_semel(
    "                CONTENTUM(tabula_importorum + numerus_importorum * 32 + 24) = nomen_base_imp.",
    "                CONTENTUM(tabula_importorum + numerus_importorum * 32 + 24) = via_importi.",
    "origo-importi-proiecti",
)

numerus_diag = textus.count("DIAGNOSTICUM_FONTIS(argv[1]")
if numerus_diag != 5:
    raise SystemExit(f"ERRATUM: diagnostica argv[1] inventa sunt {numerus_diag}, exspectata 5")
textus = textus.replace("DIAGNOSTICUM_FONTIS(argv[1]", "DIAGNOSTICUM_FONTIS(via_fons")

muta_semel(
    "    DECLARA fd_scriptio SICUT NUMERUS VALENS APERI_SCRIBERE(argv[2]).",
    "    DECLARA fd_scriptio SICUT NUMERUS VALENS APERI_SCRIBERE(via_exitus).",
    "productum-proiecti",
)

for fragmentum in (
    "FUNCTIO CONIUNGE_VIAM_PROIECTI REDDENS NUMERUS.",
    "FUNCTIO LEGE_CATHENAM_PROIECTI REDDENS NUMERUS.",
    "FUNCTIO LEGE_PROIECTUM REDDENS NUMERUS.",
    "ERRATUM: proiectum VINDEX invalidum est",
    "DECLARA modus_proiecti SICUT NUMERUS VALENS 0.",
    "APERI_SCRIBERE(via_exitus)",
):
    if fragmentum not in textus:
        raise SystemExit(f"ERRATUM: fragmentum R3 deest: {fragmentum}")

VIA.write_text(textus, encoding="utf-8")
print("RECTE: PROIECTUM R3 selective transplantatum est.")
