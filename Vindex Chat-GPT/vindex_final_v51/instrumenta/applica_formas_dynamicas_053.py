#!/usr/bin/env python3
"""VINDEX 0.53: formas et campos a regionibus fixis tabulae ad memoriam dynamicam migrat."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "FUNCTIO INITIA_FORMAS_DYNAMICA REDDENS NUMERUS."


def exige_unum(textus: str, vetus: str, nomen: str) -> None:
    numerus = textus.count(vetus)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")


def substitue_functio(textus: str, nomen: str, novum: str) -> str:
    initium = f"FUNCTIO {nomen} REDDENS NUMERUS.\n"
    p = textus.find(initium)
    if p < 0:
        raise SystemExit(f"ERRATUM: functio {nomen} non inventa est")
    finis = "FIN-FUNCTIO.\n"
    q = textus.find(finis, p)
    if q < 0:
        raise SystemExit(f"ERRATUM: finis functionis {nomen} non inventus est")
    q += len(finis)
    return textus[:p] + novum.rstrip() + "\n" + textus[q:]


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")
    if MARCA in textus:
        print("RECTE: formae dynamicae iam applicatae sunt.")
        return

    ancora = "FUNCTIO INDEX_STRUCTURAE REDDENS NUMERUS.\n"
    exige_unum(textus, ancora, "initium-formarum")

    adiutores = '''FUNCTIO INITIA_FORMAS_DYNAMICA REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    DECLARA limen_formarum SICUT NUMERUS VALENS 16.
    DECLARA basis_formarum SICUT NUMERUS VALENS RESERVA_OCTETA(limen_formarum * 40).
    SI basis_formarum < 0 TUNC
        REDDE 71.
    FIN-SI.
    tabula[2990] = basis_formarum.
    tabula[2991] = limen_formarum.
    tabula[2992] = 0.
    tabula[2993] = 0 - 1.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO ASSECURA_FORMAS_DYNAMICA REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT necessaria SICUT NUMERUS.
    DECLARA limen_formarum SICUT NUMERUS VALENS tabula[2991].
    SI necessaria <= limen_formarum TUNC
        REDDE 0.
    FIN-SI.
    DECLARA novum_limen SICUT NUMERUS VALENS limen_formarum * 2.
    DUM novum_limen < necessaria PERFICE
        novum_limen = novum_limen * 2.
    FIN-DUM.
    DECLARA nova_basis SICUT NUMERUS VALENS RESERVA_OCTETA(novum_limen * 40).
    SI nova_basis < 0 TUNC
        REDDE 71.
    FIN-SI.
    DECLARA basis_formarum SICUT NUMERUS VALENS tabula[2990].
    DECLARA octeta SICUT NUMERUS VALENS tabula[2992] * 40.
    DECLARA i_formarum SICUT NUMERUS VALENS 0.
    DUM i_formarum < octeta PERFICE
        SCRIBE_OCTETUM_AB(nova_basis + i_formarum, OCTETUS_AB(basis_formarum + i_formarum)).
        i_formarum = i_formarum + 1.
    FIN-DUM.
    tabula[2990] = nova_basis.
    tabula[2991] = novum_limen.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO FORMA_LEGE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT idx_formae SICUT NUMERUS.
    ACCIPIT campus_formae SICUT NUMERUS.
    SI idx_formae < 0 || idx_formae >= tabula[2992] TUNC
        REDDE 0.
    FIN-SI.
    DECLARA sedes_formae SICUT NUMERUS VALENS tabula[2990] + (idx_formae * 40) + (campus_formae * 8).
    REDDE CONTENTUM(sedes_formae).
FIN-FUNCTIO.

FUNCTIO FORMA_SCRIBE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT idx_formae SICUT NUMERUS.
    ACCIPIT campus_formae SICUT NUMERUS.
    ACCIPIT valor_formae SICUT NUMERUS.
    DECLARA status_formae SICUT NUMERUS VALENS ASSECURA_FORMAS_DYNAMICA(tabula, idx_formae + 1).
    SI status_formae != 0 TUNC
        REDDE status_formae.
    FIN-SI.
    DECLARA basis_formarum SICUT NUMERUS VALENS tabula[2990].
    SI idx_formae >= tabula[2992] TUNC
        DECLARA z_formae SICUT NUMERUS VALENS 0.
        DUM z_formae < 40 PERFICE
            SCRIBE_OCTETUM_AB(basis_formarum + (idx_formae * 40) + z_formae, 0).
            z_formae = z_formae + 1.
        FIN-DUM.
    FIN-SI.
    DECLARA sedes_formae SICUT NUMERUS VALENS basis_formarum + (idx_formae * 40) + (campus_formae * 8).
    CONTENTUM(sedes_formae) = valor_formae.
    SI idx_formae >= tabula[2992] TUNC
        tabula[2992] = idx_formae + 1.
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO INITIA_CAMPI_FORMA REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT idx_formae SICUT NUMERUS.
    ACCIPIT limen_init SICUT NUMERUS.
    DECLARA basis_camporum SICUT NUMERUS VALENS RESERVA_OCTETA(limen_init * 32).
    SI basis_camporum < 0 TUNC
        REDDE 71.
    FIN-SI.
    DECLARA status_campi SICUT NUMERUS VALENS FORMA_SCRIBE(tabula, idx_formae, 2, 0).
    SI status_campi == 0 TUNC
        status_campi = FORMA_SCRIBE(tabula, idx_formae, 3, limen_init).
    FIN-SI.
    SI status_campi == 0 TUNC
        status_campi = FORMA_SCRIBE(tabula, idx_formae, 4, basis_camporum).
    FIN-SI.
    REDDE status_campi.
FIN-FUNCTIO.

FUNCTIO ASSECURA_CAMPI_FORMA REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT idx_formae SICUT NUMERUS.
    ACCIPIT necessaria SICUT NUMERUS.
    DECLARA limen_camporum SICUT NUMERUS VALENS FORMA_LEGE(tabula, idx_formae, 3).
    SI necessaria <= limen_camporum TUNC
        REDDE 0.
    FIN-SI.
    DECLARA novum_limen SICUT NUMERUS VALENS limen_camporum * 2.
    SI novum_limen < 1 TUNC
        novum_limen = 8.
    FIN-SI.
    DUM novum_limen < necessaria PERFICE
        novum_limen = novum_limen * 2.
    FIN-DUM.
    DECLARA nova_basis SICUT NUMERUS VALENS RESERVA_OCTETA(novum_limen * 32).
    SI nova_basis < 0 TUNC
        REDDE 71.
    FIN-SI.
    DECLARA basis_camporum SICUT NUMERUS VALENS FORMA_LEGE(tabula, idx_formae, 4).
    DECLARA octeta SICUT NUMERUS VALENS FORMA_LEGE(tabula, idx_formae, 2) * 32.
    DECLARA i_camporum SICUT NUMERUS VALENS 0.
    DUM i_camporum < octeta PERFICE
        SCRIBE_OCTETUM_AB(nova_basis + i_camporum, OCTETUS_AB(basis_camporum + i_camporum)).
        i_camporum = i_camporum + 1.
    FIN-DUM.
    DECLARA status_campi SICUT NUMERUS VALENS FORMA_SCRIBE(tabula, idx_formae, 3, novum_limen).
    SI status_campi == 0 TUNC
        status_campi = FORMA_SCRIBE(tabula, idx_formae, 4, nova_basis).
    FIN-SI.
    REDDE status_campi.
FIN-FUNCTIO.

FUNCTIO CAMPUS_FORMA_LEGE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT idx_formae SICUT NUMERUS.
    ACCIPIT idx_campi SICUT NUMERUS.
    ACCIPIT campus_campi SICUT NUMERUS.
    SI idx_campi < 0 || idx_campi >= FORMA_LEGE(tabula, idx_formae, 2) TUNC
        REDDE 0.
    FIN-SI.
    DECLARA basis_camporum SICUT NUMERUS VALENS FORMA_LEGE(tabula, idx_formae, 4).
    DECLARA sedes_campi SICUT NUMERUS VALENS basis_camporum + (idx_campi * 32) + (campus_campi * 8).
    REDDE CONTENTUM(sedes_campi).
FIN-FUNCTIO.

FUNCTIO CAMPUS_FORMA_SCRIBE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT idx_formae SICUT NUMERUS.
    ACCIPIT idx_campi SICUT NUMERUS.
    ACCIPIT campus_campi SICUT NUMERUS.
    ACCIPIT valor_campi SICUT NUMERUS.
    DECLARA status_campi SICUT NUMERUS VALENS ASSECURA_CAMPI_FORMA(tabula, idx_formae, idx_campi + 1).
    SI status_campi != 0 TUNC
        REDDE status_campi.
    FIN-SI.
    DECLARA basis_camporum SICUT NUMERUS VALENS FORMA_LEGE(tabula, idx_formae, 4).
    DECLARA quantitas_camporum SICUT NUMERUS VALENS FORMA_LEGE(tabula, idx_formae, 2).
    SI idx_campi >= quantitas_camporum TUNC
        DECLARA z_campi SICUT NUMERUS VALENS 0.
        DUM z_campi < 32 PERFICE
            SCRIBE_OCTETUM_AB(basis_camporum + (idx_campi * 32) + z_campi, 0).
            z_campi = z_campi + 1.
        FIN-DUM.
    FIN-SI.
    DECLARA sedes_campi SICUT NUMERUS VALENS basis_camporum + (idx_campi * 32) + (campus_campi * 8).
    CONTENTUM(sedes_campi) = valor_campi.
    SI idx_campi >= quantitas_camporum TUNC
        status_campi = FORMA_SCRIBE(tabula, idx_formae, 2, idx_campi + 1).
    FIN-SI.
    REDDE status_campi.
FIN-FUNCTIO.

FUNCTIO INDEX_CAMPUS_ULTIMAE_FORMAE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT nomen_campus SICUT NUMERUS.
    DECLARA idx_formae SICUT NUMERUS VALENS tabula[2993].
    SI idx_formae < 0 TUNC
        REDDE 0.
    FIN-SI.
    DECLARA quantitas_camporum SICUT NUMERUS VALENS FORMA_LEGE(tabula, idx_formae, 2).
    DECLARA idx_campi SICUT NUMERUS VALENS 0.
    DECLARA resultatum SICUT NUMERUS VALENS quantitas_camporum.
    DUM idx_campi < quantitas_camporum PERFICE
        SI CAMPUS_FORMA_LEGE(tabula, idx_formae, idx_campi, 0) == nomen_campus TUNC
            resultatum = idx_campi.
        FIN-SI.
        idx_campi = idx_campi + 1.
    FIN-DUM.
    REDDE resultatum.
FIN-FUNCTIO.

'''
    textus = textus.replace(ancora, adiutores + ancora, 1)

    textus = substitue_functio(textus, "INDEX_STRUCTURAE", '''FUNCTIO INDEX_STRUCTURAE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT nomen_forma SICUT NUMERUS.
    DECLARA idx SICUT NUMERUS VALENS 0.
    DECLARA resultatum SICUT NUMERUS VALENS 0 - 1.
    DUM idx < tabula[2992] PERFICE
        SI FORMA_LEGE(tabula, idx, 0) == nomen_forma TUNC
            resultatum = idx.
        FIN-SI.
        idx = idx + 1.
    FIN-DUM.
    REDDE resultatum.
FIN-FUNCTIO.''')

    textus = substitue_functio(textus, "CAMPUS_STRUCTURAE_EST_FLUITANS", '''FUNCTIO CAMPUS_STRUCTURAE_EST_FLUITANS REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT idx_structurae SICUT NUMERUS.
    ACCIPIT nomen_campus SICUT NUMERUS.
    DECLARA k SICUT NUMERUS VALENS 0.
    DECLARA resultatum SICUT NUMERUS VALENS 0.
    DECLARA numerus_camporum SICUT NUMERUS VALENS FORMA_LEGE(tabula, idx_structurae, 2).
    DUM k < numerus_camporum PERFICE
        SI CAMPUS_FORMA_LEGE(tabula, idx_structurae, k, 0) == nomen_campus TUNC
            resultatum = CAMPUS_FORMA_LEGE(tabula, idx_structurae, k, 3).
        FIN-SI.
        k = k + 1.
    FIN-DUM.
    REDDE resultatum.
FIN-FUNCTIO.''')

    textus = substitue_functio(textus, "CAMPUS_STRUCTURAE_MAGNITUDO", '''FUNCTIO CAMPUS_STRUCTURAE_MAGNITUDO REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT idx_structurae SICUT NUMERUS.
    ACCIPIT nomen_campus SICUT NUMERUS.
    DECLARA k SICUT NUMERUS VALENS 0.
    DECLARA resultatum SICUT NUMERUS VALENS 8.
    DECLARA numerus_camporum SICUT NUMERUS VALENS FORMA_LEGE(tabula, idx_structurae, 2).
    DUM k < numerus_camporum PERFICE
        SI CAMPUS_FORMA_LEGE(tabula, idx_structurae, k, 0) == nomen_campus TUNC
            resultatum = CAMPUS_FORMA_LEGE(tabula, idx_structurae, k, 1).
        FIN-SI.
        k = k + 1.
    FIN-DUM.
    REDDE resultatum.
FIN-FUNCTIO.''')

    textus = substitue_functio(textus, "CAMPUS_STRUCTURAE_OFFSET", '''FUNCTIO CAMPUS_STRUCTURAE_OFFSET REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT idx_structurae SICUT NUMERUS.
    ACCIPIT nomen_campus SICUT NUMERUS.
    DECLARA k SICUT NUMERUS VALENS 0.
    DECLARA resultatum SICUT NUMERUS VALENS 0.
    DECLARA numerus_camporum SICUT NUMERUS VALENS FORMA_LEGE(tabula, idx_structurae, 2).
    DUM k < numerus_camporum PERFICE
        SI CAMPUS_FORMA_LEGE(tabula, idx_structurae, k, 0) == nomen_campus TUNC
            resultatum = CAMPUS_FORMA_LEGE(tabula, idx_structurae, k, 2).
        FIN-SI.
        k = k + 1.
    FIN-DUM.
    REDDE resultatum.
FIN-FUNCTIO.''')

    textus = substitue_functio(textus, "OFFSET_CUMULATIVUS_CAMPI", '''FUNCTIO OFFSET_CUMULATIVUS_CAMPI REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT idx_campus SICUT NUMERUS.
    DECLARA idx_formae SICUT NUMERUS VALENS tabula[2993].
    SI idx_formae < 0 TUNC
        REDDE 0.
    FIN-SI.
    DECLARA numerus_camporum SICUT NUMERUS VALENS FORMA_LEGE(tabula, idx_formae, 2).
    SI idx_campus < numerus_camporum TUNC
        REDDE CAMPUS_FORMA_LEGE(tabula, idx_formae, idx_campus, 2).
    FIN-SI.
    REDDE FORMA_LEGE(tabula, idx_formae, 1) * 8.
FIN-FUNCTIO.''')

    textus = substitue_functio(textus, "NUMERUS_CAMPORUM_FORMAE", '''FUNCTIO NUMERUS_CAMPORUM_FORMAE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT nomen SICUT NUMERUS.
    DECLARA idx SICUT NUMERUS VALENS INDEX_STRUCTURAE(tabula, nomen).
    SI idx >= 0 TUNC
        REDDE FORMA_LEGE(tabula, idx, 1).
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.''')

    vetus_idx = '''            DECLARA idx_campus SICUT NUMERUS VALENS 0.
            DUM idx_campus < 26 && tabula[200 + idx_campus] != nomen PERFICE
                idx_campus = idx_campus + 1.
            FIN-DUM.'''
    novum_idx = '''            DECLARA idx_campus SICUT NUMERUS VALENS INDEX_CAMPUS_ULTIMAE_FORMAE(tabula, nomen).'''
    exige_unum(textus, vetus_idx, "campus-generalis")
    textus = textus.replace(vetus_idx, novum_idx, 1)

    vetus_idx_aff = '''                                            DECLARA idx_campus_aff SICUT NUMERUS VALENS 0.
                                            DUM idx_campus_aff < 26 && tabula[200 + idx_campus_aff] != nomen_aff PERFICE
                                                idx_campus_aff = idx_campus_aff + 1.
                                            FIN-DUM.'''
    novum_idx_aff = '''                                            DECLARA idx_campus_aff SICUT NUMERUS VALENS INDEX_CAMPUS_ULTIMAE_FORMAE(tabula, nomen_aff).'''
    exige_unum(textus, vetus_idx_aff, "campus-generalis-assignationis")
    textus = textus.replace(vetus_idx_aff, novum_idx_aff, 1)

    vetus_magnitudo = "                                    summa_magnitudinis_v = tabula[1000 + idx_struct_v] * 8."
    novum_magnitudo = "                                    summa_magnitudinis_v = FORMA_LEGE(tabula, idx_struct_v, 1) * 8."
    exige_unum(textus, vetus_magnitudo, "magnitudo-structurae")
    textus = textus.replace(vetus_magnitudo, novum_magnitudo, 1)

    initium_formae = "        SI fons[i] == 70 && i + 1 < n && fons[i+1] == 79 TUNC\n"
    initium_functionis = "        ALITER\n        SI fons[i] == 70 && i + 7 < n && fons[i+1] == 85 && fons[i+2] == 78 && fons[i+3] == 67 && fons[i+4] == 84 && fons[i+5] == 73 && fons[i+6] == 79 && fons[i+7] == 32 TUNC\n"
    p = textus.find(initium_formae)
    q = textus.find(initium_functionis, p)
    if p < 0 or q < 0:
        raise SystemExit("ERRATUM: ramus formarum in PRINCIPALI non inventus est")

    novus_ramus = '''        SI fons[i] == 70 && i + 1 < n && fons[i+1] == 79 TUNC
            i = i + 6.
            DECLARA nomen_forma SICUT NUMERUS VALENS EXTRAHE_ET_SIGNA(fons, SEDES(i), n).
            DUM i < n && fons[i] != 46 PERFICE
                i = i + 1.
            FIN-DUM.
            i = i + 1.
            DECLARA idx_registrum_forma SICUT NUMERUS VALENS tabula[2992].
            DECLARA status_formae SICUT NUMERUS VALENS FORMA_SCRIBE(tabula, idx_registrum_forma, 0, nomen_forma).
            SI status_formae == 0 TUNC
                status_formae = INITIA_CAMPI_FORMA(tabula, idx_registrum_forma, 8).
            FIN-SI.
            SI status_formae != 0 TUNC
                PROCLAMA "ERRATUM: memoria camporum formae reservata non est".
                REDDE 71.
            FIN-SI.
            DECLARA numerus_campi SICUT NUMERUS VALENS 0.
            DECLARA offset_cumul_forma SICUT NUMERUS VALENS 0.
            DECLARA continua_forma SICUT NUMERUS VALENS 1.
            DUM continua_forma == 1 PERFICE
                DECLARA ig_fm SICUT NUMERUS VALENS IGNORA_SPATIA(fons, SEDES(i), n).
                SI fons[i] == 67 && i + 6 < n && fons[i+1] == 65 && fons[i+2] == 77 && fons[i+3] == 80 && fons[i+4] == 85 && fons[i+5] == 83 && fons[i+6] == 32 TUNC
                    i = i + 7.
                    DECLARA nomen_campus SICUT NUMERUS VALENS EXTRAHE_ET_SIGNA(fons, SEDES(i), n).
                    DECLARA ig_fm2 SICUT NUMERUS VALENS IGNORA_SPATIA(fons, SEDES(i), n).
                    DECLARA magnitudo_campus SICUT NUMERUS VALENS 8.
                    DECLARA est_fluitans_campus SICUT NUMERUS VALENS 0.
                    SI fons[i] == 83 && i + 5 < n && fons[i+1] == 73 && fons[i+2] == 67 && fons[i+3] == 85 && fons[i+4] == 84 && fons[i+5] == 32 TUNC
                        i = i + 6.
                        ig_fm2 = IGNORA_SPATIA(fons, SEDES(i), n).
                        SI fons[i] == 70 && i + 7 < n && fons[i+1] == 76 && fons[i+2] == 85 && fons[i+3] == 73 && fons[i+4] == 84 && fons[i+5] == 65 && fons[i+6] == 78 && fons[i+7] == 83 TUNC
                            est_fluitans_campus = 1.
                        FIN-SI.
                        SI fons[i] == 79 && i + 3 < n && fons[i+1] == 82 && fons[i+2] == 68 && fons[i+3] == 79 TUNC
                            i = i + 5.
                            ig_fm2 = IGNORA_SPATIA(fons, SEDES(i), n).
                            i = i + 3.
                            ig_fm2 = IGNORA_SPATIA(fons, SEDES(i), n).
                            DUM i < n && ((fons[i] >= 65 && fons[i] <= 90) || (fons[i] >= 97 && fons[i] <= 122)) PERFICE
                                i = i + 1.
                            FIN-DUM.
                            ig_fm2 = IGNORA_SPATIA(fons, SEDES(i), n).
                            i = i + 10.
                            ig_fm2 = IGNORA_SPATIA(fons, SEDES(i), n).
                            DECLARA capacitas_campus SICUT NUMERUS VALENS 0.
                            DUM i < n && fons[i] >= 48 && fons[i] <= 57 PERFICE
                                capacitas_campus = capacitas_campus * 10 + (fons[i] - 48).
                                i = i + 1.
                            FIN-DUM.
                            magnitudo_campus = capacitas_campus * 8.
                        FIN-SI.
                    FIN-SI.
                    DECLARA status_campi_formae SICUT NUMERUS VALENS CAMPUS_FORMA_SCRIBE(tabula, idx_registrum_forma, numerus_campi, 0, nomen_campus).
                    SI status_campi_formae == 0 TUNC
                        status_campi_formae = CAMPUS_FORMA_SCRIBE(tabula, idx_registrum_forma, numerus_campi, 1, magnitudo_campus).
                    FIN-SI.
                    SI status_campi_formae == 0 TUNC
                        status_campi_formae = CAMPUS_FORMA_SCRIBE(tabula, idx_registrum_forma, numerus_campi, 2, offset_cumul_forma).
                    FIN-SI.
                    SI status_campi_formae == 0 TUNC
                        status_campi_formae = CAMPUS_FORMA_SCRIBE(tabula, idx_registrum_forma, numerus_campi, 3, est_fluitans_campus).
                    FIN-SI.
                    SI status_campi_formae != 0 TUNC
                        PROCLAMA "ERRATUM: memoria camporum formae augeri non potest".
                        REDDE 71.
                    FIN-SI.
                    offset_cumul_forma = offset_cumul_forma + magnitudo_campus.
                    numerus_campi = numerus_campi + 1.
                    DUM i < n && fons[i] != 46 PERFICE
                        i = i + 1.
                    FIN-DUM.
                    i = i + 1.
                ALITER
                    ig_fm = IGNORA_SPATIA(fons, SEDES(i), n).
                    i = i + 9.
                    continua_forma = 0.
                FIN-SI.
            FIN-DUM.
            status_formae = FORMA_SCRIBE(tabula, idx_registrum_forma, 1, offset_cumul_forma / 8).
            status_formae = FORMA_SCRIBE(tabula, idx_registrum_forma, 2, numerus_campi).
            tabula[2993] = idx_registrum_forma.
'''
    textus = textus[:p] + novus_ramus + textus[q:]

    vetus_init = '''    DECLARA status_functionum_dynam SICUT NUMERUS VALENS INITIA_PARES_DYNAMICA(tabula, 2980, 64).
    DECLARA status_pendentium_dynam SICUT NUMERUS VALENS INITIA_PARES_DYNAMICA(tabula, 2983, 64).
    SI status_functionum_dynam != 0 || status_pendentium_dynam != 0 TUNC
        PROCLAMA "ERRATUM: memoria functionum dynamicarum reservata non est".
        REDDE 71.
    FIN-SI.
'''
    novum_init = vetus_init + '''    DECLARA status_formarum_dynam SICUT NUMERUS VALENS INITIA_FORMAS_DYNAMICA(tabula).
    SI status_formarum_dynam != 0 TUNC
        PROCLAMA "ERRATUM: memoria formarum dynamicarum reservata non est".
        REDDE 71.
    FIN-SI.
'''
    exige_unum(textus, vetus_init, "initium-formarum-dynamicarum")
    textus = textus.replace(vetus_init, novum_init, 1)

    vetus_caput = '''// Descriptor vocationum pendentium: 2983=basis, 2984=limen, 2985=quantitas; par est (locus, nomen).
// Locus 51 cursor pilae functionis manet; regiones ceterae paulatim in gradibus posterioribus migrabuntur.'''
    novum_caput = '''// Descriptor vocationum pendentium: 2983=basis, 2984=limen, 2985=quantitas; par est (locus, nomen).
// Descriptor formarum: 2990=basis, 2991=limen, 2992=quantitas, 2993=index ultimae formae.
// Unum recordum formae XL octeta habet: nomen, magnitudo in octetis VIII, numerus camporum, limen camporum, basis camporum.
// Unum recordum campi XXXII octeta habet: nomen, magnitudo, intervallum, fluitans.
// Locus 51 cursor pilae functionis manet; regiones ceterae paulatim in gradibus posterioribus migrabuntur.'''
    exige_unum(textus, vetus_caput, "descriptio-formarum")
    textus = textus.replace(vetus_caput, novum_caput, 1)

    reliquiae = [
        "tabula[950",
        "tabula[1000",
        "tabula[1050",
        "tabula[1100",
        "tabula[2500",
        "tabula[2530",
        "tabula[200 +",
        "idx_registrum_forma < 15",
        "idx_campus < 26",
        "idx_campus_aff < 26",
    ]
    for reliquia in reliquiae:
        if reliquia in textus:
            raise SystemExit(f"ERRATUM: reliquia formarum fixarum manet: {reliquia}")

    VIA.write_text(textus, encoding="utf-8")
    print("RECTE: formae et campi descriptoribus crescentibus utuntur.")


if __name__ == "__main__":
    applica()
