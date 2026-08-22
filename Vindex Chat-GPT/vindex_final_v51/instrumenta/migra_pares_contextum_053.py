#!/usr/bin/env python3
"""Descriptores functionum et vocationum pendentium e tabula in contextum transfert."""

from pathlib import Path

RADIX = Path(__file__).resolve().parents[1]
FONS = RADIX / "src" / "compilator_vindex.vindex"
BASIS = RADIX / "instrumenta" / "TABULA-LITTERALIA-053.txt"

textus = FONS.read_text(encoding="utf-8")

si_mutandum = "tabula[2982]" in textus or "tabula[2985]" in textus

accessores_ancora = """FUNCTIO CURSOR_PILAE_SCRIBE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    ACCIPIT valor SICUT NUMERUS.\n    CONTENTUM(contextus_parseris + 16) = valor.\n    REDDE 0.\nFIN-FUNCTIO.\n\n"""

accessores_novi = """FUNCTIO DESCRIPTOR_FUNCTIONUM_LEGE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    REDDE CONTENTUM(contextus_parseris + 24).\nFIN-FUNCTIO.\n\nFUNCTIO DESCRIPTOR_FUNCTIONUM_SCRIBE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    ACCIPIT valor SICUT NUMERUS.\n    CONTENTUM(contextus_parseris + 24) = valor.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO DESCRIPTOR_PENDENTIUM_LEGE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    REDDE CONTENTUM(contextus_parseris + 32).\nFIN-FUNCTIO.\n\nFUNCTIO DESCRIPTOR_PENDENTIUM_SCRIBE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    ACCIPIT valor SICUT NUMERUS.\n    CONTENTUM(contextus_parseris + 32) = valor.\n    REDDE 0.\nFIN-FUNCTIO.\n\n"""

if "FUNCTIO DESCRIPTOR_FUNCTIONUM_LEGE REDDENS NUMERUS." not in textus:
    if accessores_ancora not in textus:
        raise SystemExit("ERRATUM: ancora cursoris pilae non inventa est")
    textus = textus.replace(accessores_ancora, accessores_ancora + accessores_novi, 1)

allocatio_vetus = "DECLARA contextus_parseris SICUT ACUS<NUMERUS> VALENS RESERVA_OCTETA(24)."
allocatio_nova = "DECLARA contextus_parseris SICUT ACUS<NUMERUS> VALENS RESERVA_OCTETA(40)."
if allocatio_vetus in textus:
    textus = textus.replace(allocatio_vetus, allocatio_nova, 1)
elif allocatio_nova not in textus:
    raise SystemExit("ERRATUM: allocatio contextus parseris non inventa est")

# Descriptorum parium memoria extra tabulam historica servatur.
initium_contextus = textus.find(allocatio_nova)
if initium_contextus < 0:
    raise SystemExit("ERRATUM: contextus parseris non inventus est")

if "DECLARA descriptor_functionum_contextus" not in textus:
    punctum = textus.find("CONTENTUM(contextus_parseris) = 0.\n", initium_contextus)
    if punctum < 0:
        raise SystemExit("ERRATUM: initializatio contextus parseris non inventa est")
    punctum += len("CONTENTUM(contextus_parseris) = 0.\n")
    insertio = """    DECLARA descriptor_functionum_contextus SICUT NUMERUS VALENS RESERVA_OCTETA(24).\n    DECLARA descriptor_pendentium_contextus SICUT NUMERUS VALENS RESERVA_OCTETA(24).\n    SI descriptor_functionum_contextus < 0 || descriptor_pendentium_contextus < 0 TUNC\n        PROCLAMA \"ERRATUM: memoria descriptorum functionum reservata non est\".\n        REDDE 71.\n    FIN-SI.\n    DESCRIPTOR_FUNCTIONUM_SCRIBE(contextus_parseris, descriptor_functionum_contextus).\n    DESCRIPTOR_PENDENTIUM_SCRIBE(contextus_parseris, descriptor_pendentium_contextus).\n"""
    textus = textus[:punctum] + insertio + textus[punctum:]

# Bibliotheca parium ipsa descriptoris acus utitur, non tabulae et indice magico.
start = textus.find("FUNCTIO INITIA_PARES_DYNAMICA REDDENS NUMERUS.")
finis = textus.find("FUNCTIO INITIA_LOCA_DYNAMICA REDDENS NUMERUS.")
if start < 0 or finis < 0 or finis <= start:
    raise SystemExit("ERRATUM: regio descriptorum parium non inventa est")

novus_blocus = """FUNCTIO INITIA_PARES_DYNAMICA REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT limen_init SICUT NUMERUS.\n    DECLARA basis_parium SICUT NUMERUS VALENS RESERVA_OCTETA(limen_init * 16).\n    SI basis_parium < 0 TUNC\n        REDDE 71.\n    FIN-SI.\n    CONTENTUM(descriptor) = basis_parium.\n    CONTENTUM(descriptor + 8) = limen_init.\n    CONTENTUM(descriptor + 16) = 0.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO ASSECURA_PARES_DYNAMICA REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT necessaria SICUT NUMERUS.\n    DECLARA limen_parium SICUT NUMERUS VALENS CONTENTUM(descriptor + 8).\n    SI necessaria <= limen_parium TUNC\n        REDDE 0.\n    FIN-SI.\n    DECLARA novum_limen_parium SICUT NUMERUS VALENS limen_parium * 2.\n    DUM novum_limen_parium < necessaria PERFICE\n        novum_limen_parium = novum_limen_parium * 2.\n    FIN-DUM.\n    DECLARA nova_basis_parium SICUT NUMERUS VALENS RESERVA_OCTETA(novum_limen_parium * 16).\n    SI nova_basis_parium < 0 TUNC\n        REDDE 71.\n    FIN-SI.\n    DECLARA basis_parium SICUT NUMERUS VALENS CONTENTUM(descriptor).\n    DECLARA quantitas_parium SICUT NUMERUS VALENS CONTENTUM(descriptor + 16).\n    DECLARA octeta_parium SICUT NUMERUS VALENS quantitas_parium * 16.\n    DECLARA i_parium SICUT NUMERUS VALENS 0.\n    DUM i_parium < octeta_parium PERFICE\n        SCRIBE_OCTETUM_AB(nova_basis_parium + i_parium, OCTETUS_AB(basis_parium + i_parium)).\n        i_parium = i_parium + 1.\n    FIN-DUM.\n    CONTENTUM(descriptor) = nova_basis_parium.\n    CONTENTUM(descriptor + 8) = novum_limen_parium.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO PARES_QUANTITAS REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    REDDE CONTENTUM(descriptor + 16).\nFIN-FUNCTIO.\n\nFUNCTIO PARES_LEGE REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT index_par SICUT NUMERUS.\n    ACCIPIT pars_paris SICUT NUMERUS.\n    SI index_par < 0 || index_par >= CONTENTUM(descriptor + 16) TUNC\n        REDDE 0.\n    FIN-SI.\n    DECLARA sedes_paris SICUT NUMERUS VALENS CONTENTUM(descriptor) + (index_par * 16) + (pars_paris * 8).\n    REDDE CONTENTUM(sedes_paris).\nFIN-FUNCTIO.\n\nFUNCTIO PARES_SCRIBE REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT index_par SICUT NUMERUS.\n    ACCIPIT pars_paris SICUT NUMERUS.\n    ACCIPIT valor_paris SICUT NUMERUS.\n    DECLARA status_parium SICUT NUMERUS VALENS ASSECURA_PARES_DYNAMICA(descriptor, index_par + 1).\n    SI status_parium != 0 TUNC\n        REDDE status_parium.\n    FIN-SI.\n    DECLARA basis_parium SICUT NUMERUS VALENS CONTENTUM(descriptor).\n    SI pars_paris == 0 && index_par >= CONTENTUM(descriptor + 16) TUNC\n        DECLARA z_paris SICUT NUMERUS VALENS 0.\n        DUM z_paris < 16 PERFICE\n            SCRIBE_OCTETUM_AB(basis_parium + (index_par * 16) + z_paris, 0).\n            z_paris = z_paris + 1.\n        FIN-DUM.\n    FIN-SI.\n    DECLARA sedes_paris SICUT NUMERUS VALENS basis_parium + (index_par * 16) + (pars_paris * 8).\n    CONTENTUM(sedes_paris) = valor_paris.\n    SI index_par >= CONTENTUM(descriptor + 16) TUNC\n        CONTENTUM(descriptor + 16) = index_par + 1.\n    FIN-SI.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO CERCA_FUNCTIONEM_DYNAMICAM REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    ACCIPIT nomen_fn_dyn SICUT NUMERUS.\n    DECLARA descriptor SICUT NUMERUS VALENS DESCRIPTOR_FUNCTIONUM_LEGE(contextus_parseris).\n    DECLARA idx_fn_dyn SICUT NUMERUS VALENS 0.\n    DECLARA locus_fn_dyn SICUT NUMERUS VALENS 0.\n    DUM idx_fn_dyn < PARES_QUANTITAS(descriptor) PERFICE\n        SI PARES_LEGE(descriptor, idx_fn_dyn, 0) == nomen_fn_dyn TUNC\n            locus_fn_dyn = PARES_LEGE(descriptor, idx_fn_dyn, 1).\n        FIN-SI.\n        idx_fn_dyn = idx_fn_dyn + 1.\n    FIN-DUM.\n    REDDE locus_fn_dyn.\nFIN-FUNCTIO.\n\n"""
textus = textus[:start] + novus_blocus + textus[finis:]

replacements = {
    "INITIA_PARES_DYNAMICA(tabula, 2980, 64)": "INITIA_PARES_DYNAMICA(DESCRIPTOR_FUNCTIONUM_LEGE(contextus_parseris), 64)",
    "INITIA_PARES_DYNAMICA(tabula, 2983, 64)": "INITIA_PARES_DYNAMICA(DESCRIPTOR_PENDENTIUM_LEGE(contextus_parseris), 64)",
    "PARES_LEGE(tabula, 2980,": "PARES_LEGE(DESCRIPTOR_FUNCTIONUM_LEGE(contextus_parseris),",
    "PARES_SCRIBE(tabula, 2980,": "PARES_SCRIBE(DESCRIPTOR_FUNCTIONUM_LEGE(contextus_parseris),",
    "PARES_LEGE(tabula, 2983,": "PARES_LEGE(DESCRIPTOR_PENDENTIUM_LEGE(contextus_parseris),",
    "PARES_SCRIBE(tabula, 2983,": "PARES_SCRIBE(DESCRIPTOR_PENDENTIUM_LEGE(contextus_parseris),",
    "CERCA_FUNCTIONEM_DYNAMICAM(tabula,": "CERCA_FUNCTIONEM_DYNAMICAM(contextus_parseris,",
    "tabula[2982]": "PARES_QUANTITAS(DESCRIPTOR_FUNCTIONUM_LEGE(contextus_parseris))",
    "tabula[2985]": "PARES_QUANTITAS(DESCRIPTOR_PENDENTIUM_LEGE(contextus_parseris))",
}
for vetus, novus in replacements.items():
    textus = textus.replace(vetus, novus)

if "tabula[2982]" in textus or "tabula[2985]" in textus:
    raise SystemExit("ERRATUM: quantitas functionum vel pendentium adhuc in tabula est")
if "PARES_LEGE(tabula, 298" in textus or "PARES_SCRIBE(tabula, 298" in textus:
    raise SystemExit("ERRATUM: descriptor parium adhuc per tabulam transit")

textus = textus.replace(
    "// Descriptor functionum: 2980=basis, 2981=limen, 2982=quantitas; par est (nomen, locus).\n// Descriptor vocationum pendentium: 2983=basis, 2984=limen, 2985=quantitas; par est (locus, nomen).",
    "// Functiones et vocationes pendentes descriptoribus explicitis extra tabulam utuntur.",
)

FONS.write_text(textus, encoding="utf-8", newline="\n")

lineae = BASIS.read_text(encoding="utf-8").splitlines()
lineae = [linea for linea in lineae if linea.strip() not in {"2982", "2985"}]
lineae = [
    linea.replace("IX indices, XLV accessus", "VII indices, XLI accessus")
    for linea in lineae
]
BASIS.write_text("\n".join(lineae) + "\n", encoding="utf-8", newline="\n")

if si_mutandum:
    print("RECTE: descriptores functionum et vocationum pendentium e tabula translati sunt.")
else:
    print("RECTE: descriptores parium iam extra tabulam sunt.")
