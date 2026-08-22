#!/usr/bin/env python3
"""VINDEX 0.53: functiones et vocationes pendentes ad tabulas dynamicas migrat."""

from pathlib import Path

VIA = Path("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex")
MARCA = "FUNCTIO INITIA_PARES_DYNAMICA REDDENS NUMERUS."


def exige_unum(textus: str, vetus: str, nomen: str) -> None:
    numerus = textus.count(vetus)
    if numerus != 1:
        raise SystemExit(f"ERRATUM: ancora {nomen} {numerus} vicibus inventa est")


def applica() -> None:
    textus = VIA.read_text(encoding="utf-8")
    if MARCA in textus:
        print("RECTE: functiones dynamicae iam applicatae sunt.")
        return

    ancora = "FUNCTIO INITIA_LOCA_DYNAMICA REDDENS NUMERUS.\n"
    exige_unum(textus, ancora, "initium-localium")

    adiutores = '''FUNCTIO INITIA_PARES_DYNAMICA REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT descriptor SICUT NUMERUS.
    ACCIPIT limen_init SICUT NUMERUS.
    DECLARA basis_parium SICUT NUMERUS VALENS RESERVA_OCTETA(limen_init * 16).
    SI basis_parium < 0 TUNC
        REDDE 71.
    FIN-SI.
    tabula[descriptor] = basis_parium.
    tabula[descriptor + 1] = limen_init.
    tabula[descriptor + 2] = 0.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO ASSECURA_PARES_DYNAMICA REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT descriptor SICUT NUMERUS.
    ACCIPIT necessaria SICUT NUMERUS.
    DECLARA limen_parium SICUT NUMERUS VALENS tabula[descriptor + 1].
    SI necessaria <= limen_parium TUNC
        REDDE 0.
    FIN-SI.
    DECLARA novum_limen_parium SICUT NUMERUS VALENS limen_parium * 2.
    DUM novum_limen_parium < necessaria PERFICE
        novum_limen_parium = novum_limen_parium * 2.
    FIN-DUM.
    DECLARA nova_basis_parium SICUT NUMERUS VALENS RESERVA_OCTETA(novum_limen_parium * 16).
    SI nova_basis_parium < 0 TUNC
        REDDE 71.
    FIN-SI.
    DECLARA basis_parium SICUT NUMERUS VALENS tabula[descriptor].
    DECLARA quantitas_parium SICUT NUMERUS VALENS tabula[descriptor + 2].
    DECLARA octeta_parium SICUT NUMERUS VALENS quantitas_parium * 16.
    DECLARA i_parium SICUT NUMERUS VALENS 0.
    DUM i_parium < octeta_parium PERFICE
        SCRIBE_OCTETUM_AB(nova_basis_parium + i_parium, OCTETUS_AB(basis_parium + i_parium)).
        i_parium = i_parium + 1.
    FIN-DUM.
    tabula[descriptor] = nova_basis_parium.
    tabula[descriptor + 1] = novum_limen_parium.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO PARES_LEGE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT descriptor SICUT NUMERUS.
    ACCIPIT index_par SICUT NUMERUS.
    ACCIPIT pars_paris SICUT NUMERUS.
    SI index_par < 0 || index_par >= tabula[descriptor + 2] TUNC
        REDDE 0.
    FIN-SI.
    DECLARA sedes_paris SICUT NUMERUS VALENS tabula[descriptor] + (index_par * 16) + (pars_paris * 8).
    REDDE CONTENTUM(sedes_paris).
FIN-FUNCTIO.

FUNCTIO PARES_SCRIBE REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT descriptor SICUT NUMERUS.
    ACCIPIT index_par SICUT NUMERUS.
    ACCIPIT pars_paris SICUT NUMERUS.
    ACCIPIT valor_paris SICUT NUMERUS.
    DECLARA status_parium SICUT NUMERUS VALENS ASSECURA_PARES_DYNAMICA(tabula, descriptor, index_par + 1).
    SI status_parium != 0 TUNC
        REDDE status_parium.
    FIN-SI.
    DECLARA basis_parium SICUT NUMERUS VALENS tabula[descriptor].
    SI pars_paris == 0 && index_par >= tabula[descriptor + 2] TUNC
        DECLARA z_paris SICUT NUMERUS VALENS 0.
        DUM z_paris < 16 PERFICE
            SCRIBE_OCTETUM_AB(basis_parium + (index_par * 16) + z_paris, 0).
            z_paris = z_paris + 1.
        FIN-DUM.
    FIN-SI.
    DECLARA sedes_paris SICUT NUMERUS VALENS basis_parium + (index_par * 16) + (pars_paris * 8).
    CONTENTUM(sedes_paris) = valor_paris.
    SI index_par >= tabula[descriptor + 2] TUNC
        tabula[descriptor + 2] = index_par + 1.
    FIN-SI.
    REDDE 0.
FIN-FUNCTIO.

FUNCTIO CERCA_FUNCTIONEM_DYNAMICAM REDDENS NUMERUS.
    ACCIPIT tabula SICUT ORDO DE NUMERUS.
    ACCIPIT nomen_fn_dyn SICUT NUMERUS.
    DECLARA idx_fn_dyn SICUT NUMERUS VALENS 0.
    DECLARA locus_fn_dyn SICUT NUMERUS VALENS 0.
    DUM idx_fn_dyn < tabula[2982] PERFICE
        SI PARES_LEGE(tabula, 2980, idx_fn_dyn, 0) == nomen_fn_dyn TUNC
            locus_fn_dyn = PARES_LEGE(tabula, 2980, idx_fn_dyn, 1).
        FIN-SI.
        idx_fn_dyn = idx_fn_dyn + 1.
    FIN-DUM.
    REDDE locus_fn_dyn.
FIN-FUNCTIO.

'''
    textus = textus.replace(ancora, adiutores + ancora, 1)

    vetus_lookup = '''        DECLARA idx_fn_appel SICUT NUMERUS VALENS 0.
        DECLARA loci_fn SICUT NUMERUS VALENS 0.
        DECLARA inventum_fn SICUT NUMERUS VALENS 0.
        DUM idx_fn_appel < 150 && tabula[328 + idx_fn_appel] != 0 PERFICE
            SI tabula[328 + idx_fn_appel] == nomen_fn TUNC
                loci_fn = tabula[478 + idx_fn_appel].
                inventum_fn = 1.
            FIN-SI.
            idx_fn_appel = idx_fn_appel + 1.
        FIN-DUM.
        SI inventum_fn == 1 TUNC'''
    novum_lookup = '''        DECLARA loci_fn SICUT NUMERUS VALENS CERCA_FUNCTIONEM_DYNAMICAM(tabula, nomen_fn).
        SI loci_fn != 0 TUNC'''
    exige_unum(textus, vetus_lookup, "scrutinium-functionis")
    textus = textus.replace(vetus_lookup, novum_lookup, 1)

    vetus_pendens = '''            DECLARA idx_pendens SICUT NUMERUS VALENS tabula[628].
            tabula[630 + (idx_pendens * 2)] = loci_appel_pendens.
            tabula[630 + (idx_pendens * 2) + 1] = nomen_fn.
            tabula[628] = tabula[628] + 1.'''
    novum_pendens = '''            DECLARA idx_pendens SICUT NUMERUS VALENS tabula[2985].
            DECLARA ig_pendens_dyn SICUT NUMERUS VALENS PARES_SCRIBE(tabula, 2983, idx_pendens, 0, loci_appel_pendens).
            ig_pendens_dyn = PARES_SCRIBE(tabula, 2983, idx_pendens, 1, nomen_fn).'''
    exige_unum(textus, vetus_pendens, "additio-pendentis")
    textus = textus.replace(vetus_pendens, novum_pendens, 1)

    vetus_registratio = '''                DECLARA idx_fn SICUT NUMERUS VALENS 0.
                DUM idx_fn < 150 && tabula[328 + idx_fn] != 0 PERFICE
                    idx_fn = idx_fn + 1.
                FIN-DUM.
                tabula[328 + idx_fn] = nomen_adiutoris.
                tabula[478 + idx_fn] = pos.'''
    novum_registratio = '''                DECLARA idx_fn SICUT NUMERUS VALENS tabula[2982].
                DECLARA ig_fn_dyn SICUT NUMERUS VALENS PARES_SCRIBE(tabula, 2980, idx_fn, 0, nomen_adiutoris).
                ig_fn_dyn = PARES_SCRIBE(tabula, 2980, idx_fn, 1, pos).'''
    exige_unum(textus, vetus_registratio, "registratio-functionis")
    textus = textus.replace(vetus_registratio, novum_registratio, 1)

    vetus_resolutio = '''    DECLARA k_pendens SICUT NUMERUS VALENS 0.
    DUM k_pendens < tabula[628] PERFICE
        DECLARA loci_p SICUT NUMERUS VALENS tabula[630 + (k_pendens * 2)].
        DECLARA nomen_p SICUT NUMERUS VALENS tabula[630 + (k_pendens * 2) + 1].
        DECLARA idx_rp SICUT NUMERUS VALENS 0.
        DECLARA loci_cible SICUT NUMERUS VALENS 0.
        DUM idx_rp < 150 && tabula[328 + idx_rp] != 0 PERFICE
            SI tabula[328 + idx_rp] == nomen_p TUNC
                loci_cible = tabula[478 + idx_rp].
            FIN-SI.
            idx_rp = idx_rp + 1.
        FIN-DUM.'''
    novum_resolutio = '''    DECLARA k_pendens SICUT NUMERUS VALENS 0.
    DUM k_pendens < tabula[2985] PERFICE
        DECLARA loci_p SICUT NUMERUS VALENS PARES_LEGE(tabula, 2983, k_pendens, 0).
        DECLARA nomen_p SICUT NUMERUS VALENS PARES_LEGE(tabula, 2983, k_pendens, 1).
        DECLARA loci_cible SICUT NUMERUS VALENS CERCA_FUNCTIONEM_DYNAMICAM(tabula, nomen_p).'''
    exige_unum(textus, vetus_resolutio, "resolutio-pendentium")
    textus = textus.replace(vetus_resolutio, novum_resolutio, 1)

    vetus_init = '''    DECLARA status_locorum_dynam SICUT NUMERUS VALENS INITIA_LOCA_DYNAMICA(tabula).
    SI status_locorum_dynam != 0 TUNC
        PROCLAMA "ERRATUM: memoria symbolorum localium reservata non est".
        REDDE 71.
    FIN-SI.
'''
    novum_init = vetus_init + '''    DECLARA status_functionum_dynam SICUT NUMERUS VALENS INITIA_PARES_DYNAMICA(tabula, 2980, 64).
    DECLARA status_pendentium_dynam SICUT NUMERUS VALENS INITIA_PARES_DYNAMICA(tabula, 2983, 64).
    SI status_functionum_dynam != 0 || status_pendentium_dynam != 0 TUNC
        PROCLAMA "ERRATUM: memoria functionum dynamicarum reservata non est".
        REDDE 71.
    FIN-SI.
'''
    exige_unum(textus, vetus_init, "initium-tabularum-dynamicarum")
    textus = textus.replace(vetus_init, novum_init, 1)

    vetus_caput = '''// Descriptor localium in tabula: 2970=basis, 2971=limen_locorum, 2972=numerus.
// Unum symbolum locale XLVIII octeta habet: nomen, intervallum, series, magnitudo, structura, fluitans.
// Locus 51 cursor pilae functionis manet; regiones ceterae paulatim in gradibus posterioribus migrabuntur.'''
    novum_caput = '''// Descriptor localium in tabula: 2970=basis, 2971=limen, 2972=quantitas.
// Unum symbolum locale XLVIII octeta habet: nomen, intervallum, series, magnitudo, structura, fluitans.
// Descriptor functionum: 2980=basis, 2981=limen, 2982=quantitas; par est (nomen, locus).
// Descriptor vocationum pendentium: 2983=basis, 2984=limen, 2985=quantitas; par est (locus, nomen).
// Locus 51 cursor pilae functionis manet; regiones ceterae paulatim in gradibus posterioribus migrabuntur.'''
    exige_unum(textus, vetus_caput, "descriptio-tabulae")
    textus = textus.replace(vetus_caput, novum_caput, 1)

    reliquiae = [
        "tabula[328 + idx_fn_appel]",
        "tabula[478 + idx_fn_appel]",
        "tabula[328 + idx_fn]",
        "tabula[478 + idx_fn]",
        "tabula[628]",
        "tabula[630 + (idx_pendens * 2)]",
        "tabula[630 + (k_pendens * 2)]",
        "idx_fn_appel < 150",
        "idx_rp < 150",
    ]
    for reliquia in reliquiae:
        if reliquia in textus:
            raise SystemExit(f"ERRATUM: reliquia functionum fixarum manet: {reliquia}")

    VIA.write_text(textus, encoding="utf-8")
    print("RECTE: functiones et vocationes pendentes descriptoribus dynamicis utuntur.")


if __name__ == "__main__":
    applica()
