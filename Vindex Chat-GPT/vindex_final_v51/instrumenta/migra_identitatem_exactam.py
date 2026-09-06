#!/usr/bin/env python3
"""Migratio deterministica Phase 0-bis: identitas exacta symbolorum usoris."""

from pathlib import Path

FONS = Path(__file__).resolve().parents[1] / "src" / "compilator_vindex.vindex"


def substitue(textus: str, vetus: str, novum: str, numerus: int = 1) -> str:
    inventa = textus.count(vetus)
    if inventa != numerus:
        raise SystemExit(
            f"ERRATUM: substitutio exspectabat {numerus} occurrence(s), invenit {inventa}: {vetus[:120]!r}"
        )
    return textus.replace(vetus, novum)


textus = FONS.read_text(encoding="utf-8")

# Comparatio generica: longitudo -> signum historicum base XXXI -> octeta exacta.
ancora = "FUNCTIO EXTRAHE_ET_SIGNA REDDENS NUMERUS.\n"
auxilia = """FUNCTIO SIGNUM_IDENTITATIS REDDENS NUMERUS.
    ACCIPIT fons SICUT ACUS<LITTERA>.
    ACCIPIT identitas SICUT NUMERUS.
    SI identitas == 0 TUNC
        REDDE 0.
    FIN-SI.
    DECLARA initium SICUT NUMERUS VALENS (identitas >> 32) & 4294967295.
    DECLARA longitudo SICUT NUMERUS VALENS identitas & 4294967295.
    DECLARA signum SICUT NUMERUS VALENS 0.
    DECLARA k SICUT NUMERUS VALENS 0.
    DUM k < longitudo PERFICE
        signum = signum * 31 + fons[initium + k].
        k = k + 1.
    FIN-DUM.
    REDDE signum.
FIN-FUNCTIO.

FUNCTIO NOMINA_IDENTITATUM_AEQUALIA REDDENS NUMERUS.
    ACCIPIT fons SICUT ACUS<LITTERA>.
    ACCIPIT a SICUT NUMERUS.
    ACCIPIT b SICUT NUMERUS.
    SI a == 0 || b == 0 TUNC
        REDDE 0.
    FIN-SI.
    DECLARA la SICUT NUMERUS VALENS a & 4294967295.
    DECLARA lb SICUT NUMERUS VALENS b & 4294967295.
    SI la != lb TUNC
        REDDE 0.
    FIN-SI.
    SI SIGNUM_IDENTITATIS(fons, a) != SIGNUM_IDENTITATIS(fons, b) TUNC
        REDDE 0.
    FIN-SI.
    DECLARA ia SICUT NUMERUS VALENS (a >> 32) & 4294967295.
    DECLARA ib SICUT NUMERUS VALENS (b >> 32) & 4294967295.
    DECLARA k SICUT NUMERUS VALENS 0.
    DUM k < la PERFICE
        SI fons[ia + k] != fons[ib + k] TUNC
            REDDE 0.
        FIN-SI.
        k = k + 1.
    FIN-DUM.
    REDDE 1.
FIN-FUNCTIO.

"""
textus = substitue(textus, ancora, auxilia + ancora)

# Functiones: clavis tabulae fit identitas exacta; fons servatur in descriptore.
vetus_cerca = """FUNCTIO CERCA_FUNCTIONEM_DYNAMICAM REDDENS NUMERUS.
    ACCIPIT contextus_parseris SICUT NUMERUS.
    ACCIPIT nomen_fn_dyn SICUT NUMERUS.
    DECLARA descriptor SICUT NUMERUS VALENS DESCRIPTOR_FUNCTIONUM_LEGE(contextus_parseris).
    DECLARA idx_fn_dyn SICUT NUMERUS VALENS 0.
    DECLARA locus_fn_dyn SICUT NUMERUS VALENS 0.
    DUM idx_fn_dyn < PARES_QUANTITAS(descriptor) PERFICE
        SI PARES_LEGE(descriptor, idx_fn_dyn, 0) == nomen_fn_dyn TUNC
            locus_fn_dyn = PARES_LEGE(descriptor, idx_fn_dyn, 1).
        FIN-SI.
        idx_fn_dyn = idx_fn_dyn + 1.
    FIN-DUM.
    REDDE locus_fn_dyn.
FIN-FUNCTIO.
"""
novum_cerca = """FUNCTIO CERCA_FUNCTIONEM_DYNAMICAM REDDENS NUMERUS.
    ACCIPIT contextus_parseris SICUT NUMERUS.
    ACCIPIT nomen_fn_dyn SICUT NUMERUS.
    DECLARA descriptor SICUT NUMERUS VALENS DESCRIPTOR_FUNCTIONUM_LEGE(contextus_parseris).
    DECLARA fons SICUT ACUS<LITTERA> VALENS CONTENTUM(descriptor + 24).
    DECLARA idx_fn_dyn SICUT NUMERUS VALENS 0.
    DECLARA locus_fn_dyn SICUT NUMERUS VALENS 0.
    DUM idx_fn_dyn < PARES_QUANTITAS(descriptor) PERFICE
        SI NOMINA_IDENTITATUM_AEQUALIA(fons, PARES_LEGE(descriptor, idx_fn_dyn, 0), nomen_fn_dyn) == 1 TUNC
            locus_fn_dyn = PARES_LEGE(descriptor, idx_fn_dyn, 1).
        FIN-SI.
        idx_fn_dyn = idx_fn_dyn + 1.
    FIN-DUM.
    REDDE locus_fn_dyn.
FIN-FUNCTIO.
"""
textus = substitue(textus, vetus_cerca, novum_cerca)

for nomen in ("nomen_fn", "nomen_sf", "nomen_interruptio", "nomen_adiutoris"):
    textus = substitue(
        textus,
        f"DECLARA {nomen} SICUT NUMERUS VALENS EXTRAHE_ET_SIGNA(fons,",
        f"DECLARA {nomen} SICUT NUMERUS VALENS EXTRAHE_ET_IDENTITAS_LOCALIS(fons,",
    )

textus = substitue(
    textus,
    "DECLARA descriptor_functionum_contextus SICUT NUMERUS VALENS RESERVA_OCTETA(24).",
    "DECLARA descriptor_functionum_contextus SICUT NUMERUS VALENS RESERVA_OCTETA(32).",
)
textus = substitue(
    textus,
    "    DESCRIPTOR_FUNCTIONUM_SCRIBE(contextus_parseris, descriptor_functionum_contextus).\n",
    "    DESCRIPTOR_FUNCTIONUM_SCRIBE(contextus_parseris, descriptor_functionum_contextus).\n    CONTENTUM(descriptor_functionum_contextus + 24) = fons.\n",
)

# Formae et campi servant quoque identitatem exactam; fons in +32 descriptoris formarum.
textus = substitue(
    textus,
    "DECLARA descriptor_formarum_contextus SICUT NUMERUS VALENS RESERVA_OCTETA(32).",
    "DECLARA descriptor_formarum_contextus SICUT NUMERUS VALENS RESERVA_OCTETA(40).",
)
textus = substitue(
    textus,
    "    DESCRIPTOR_FORMARUM_SCRIBE(contextus_parseris, descriptor_formarum_contextus).\n",
    "    DESCRIPTOR_FORMARUM_SCRIBE(contextus_parseris, descriptor_formarum_contextus).\n    CONTENTUM(descriptor_formarum_contextus + 32) = fons.\n",
)

for nomen in (
    "nomen_forma",
    "nomen_campus",
    "nomen_typus_reserva",
    "nomen_typus_ordo",
    "nomen_typus_interior",
    "nomen_typus_struct_v",
):
    textus = substitue(
        textus,
        f"DECLARA {nomen} SICUT NUMERUS VALENS EXTRAHE_ET_SIGNA(fons,",
        f"DECLARA {nomen} SICUT NUMERUS VALENS EXTRAHE_ET_IDENTITAS_LOCALIS(fons,",
    )

textus = substitue(
    textus,
    "DECLARA nomen_int SICUT NUMERUS VALENS SIGNUM_AB_POSITIONE(fons, pos_post_acus, n).",
    "DECLARA nomen_int SICUT NUMERUS VALENS IDENTITAS_LOCALIS_AB_POSITIONE(fons, pos_post_acus, n).",
)

textus = substitue(
    textus,
    "SI CAMPUS_FORMA_LEGE(descriptor, idx_formae, idx_campi, 0) == nomen_campus TUNC",
    "SI NOMINA_IDENTITATUM_AEQUALIA(CONTENTUM(descriptor + 32), CAMPUS_FORMA_LEGE(descriptor, idx_formae, idx_campi, 0), nomen_campus) == 1 TUNC",
)
textus = substitue(
    textus,
    "SI FORMA_LEGE(descriptor, idx, 0) == nomen_forma TUNC",
    "SI NOMINA_IDENTITATUM_AEQUALIA(CONTENTUM(descriptor + 32), FORMA_LEGE(descriptor, idx, 0), nomen_forma) == 1 TUNC",
)
textus = substitue(
    textus,
    "SI CAMPUS_FORMA_LEGE(descriptor, idx_structurae, k, 0) == nomen_campus TUNC",
    "SI NOMINA_IDENTITATUM_AEQUALIA(CONTENTUM(descriptor + 32), CAMPUS_FORMA_LEGE(descriptor, idx_structurae, k, 0), nomen_campus) == 1 TUNC",
    3,
)

# Requetes de champs: les variables exactes existent deja depuis F9-II; ne plus repasser par leur hash.
remplacements = {
    "CAMPUS_STRUCTURAE_MAGNITUDO(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), idx_struct_campus - 1, nomen_signum)":
        "CAMPUS_STRUCTURAE_MAGNITUDO(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), idx_struct_campus - 1, nomen)",
    "CAMPUS_STRUCTURAE_OFFSET(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), idx_struct_campus - 1, nomen_signum)":
        "CAMPUS_STRUCTURAE_OFFSET(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), idx_struct_campus - 1, nomen)",
    "CAMPUS_STRUCTURAE_EST_FLUITANS(descriptor_formarum, idx_struct_peek - 1, nomen_peek_signum)":
        "CAMPUS_STRUCTURAE_EST_FLUITANS(descriptor_formarum, idx_struct_peek - 1, nomen_peek)",
    "INDEX_CAMPUS_ULTIMAE_FORMAE(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), nomen_aff_signum)":
        "INDEX_CAMPUS_ULTIMAE_FORMAE(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), nomen_aff)",
    "OFFSET_PTR_CAMPUS_STRUCTA(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), fons, CONTENTUM(pos_fontis), n, idx_campus_aff, nomen_aff_signum, contextus_parseris)":
        "OFFSET_PTR_CAMPUS_STRUCTA(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), fons, CONTENTUM(pos_fontis), n, idx_campus_aff, nomen_aff, contextus_parseris)",
    "CAMPUS_STRUCTURAE_OFFSET(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), idx_struct_campus_aff - 1, nomen_aff_signum)":
        "CAMPUS_STRUCTURAE_OFFSET(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), idx_struct_campus_aff - 1, nomen_aff)",
    "CAMPUS_STRUCTURAE_EST_FLUITANS(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), idx_struct_campus_aff - 1, nomen_aff_signum)":
        "CAMPUS_STRUCTURAE_EST_FLUITANS(DESCRIPTOR_FORMARUM_LEGE(contextus_parseris), idx_struct_campus_aff - 1, nomen_aff)",
}
for vetus, novum in remplacements.items():
    textus = substitue(textus, vetus, novum)

FONS.write_text(textus, encoding="utf-8")
print("RECTE: migratio identitatis exactae applicata est.")
