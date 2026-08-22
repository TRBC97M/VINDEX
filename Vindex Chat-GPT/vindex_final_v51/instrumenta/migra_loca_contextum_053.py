#!/usr/bin/env python3
"""Descriptor localium e tabula historica in contextum compilationis transfert."""

from pathlib import Path

RADIX = Path(__file__).resolve().parents[1]
FONS = RADIX / "src" / "compilator_vindex.vindex"
BASIS = RADIX / "instrumenta" / "TABULA-LITTERALIA-053.txt"

textus = FONS.read_text(encoding="utf-8")
si_mutandum = any(f"tabula[{i}]" in textus for i in (2970, 2971, 2972))

# Acus descriptoris localium fit pars contextus communis.
ancora = """FUNCTIO DESCRIPTOR_PENDENTIUM_SCRIBE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    ACCIPIT valor SICUT NUMERUS.\n    CONTENTUM(contextus_parseris + 32) = valor.\n    REDDE 0.\nFIN-FUNCTIO.\n\n"""
accessores = """FUNCTIO DESCRIPTOR_LOCALIUM_LEGE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    REDDE CONTENTUM(contextus_parseris + 40).\nFIN-FUNCTIO.\n\nFUNCTIO DESCRIPTOR_LOCALIUM_SCRIBE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    ACCIPIT valor SICUT NUMERUS.\n    CONTENTUM(contextus_parseris + 40) = valor.\n    REDDE 0.\nFIN-FUNCTIO.\n\n"""
if "FUNCTIO DESCRIPTOR_LOCALIUM_LEGE REDDENS NUMERUS." not in textus:
    if ancora not in textus:
        raise SystemExit("ERRATUM: ancora descriptoris pendentium non inventa est")
    textus = textus.replace(ancora, ancora + accessores, 1)

allocatio_vetus = "DECLARA contextus_parseris SICUT ACUS<NUMERUS> VALENS RESERVA_OCTETA(40)."
allocatio_nova = "DECLARA contextus_parseris SICUT ACUS<NUMERUS> VALENS RESERVA_OCTETA(48)."
if allocatio_vetus in textus:
    textus = textus.replace(allocatio_vetus, allocatio_nova, 1)
elif allocatio_nova not in textus:
    raise SystemExit("ERRATUM: allocatio contextus XL octetorum non inventa est")

# Descriptor localium XXXIV? Non: tria verba NUMERUS = XXIV octeta.
if "DECLARA descriptor_localium_contextus" not in textus:
    init_ancora = """    DESCRIPTOR_FUNCTIONUM_SCRIBE(contextus_parseris, descriptor_functionum_contextus).\n    DESCRIPTOR_PENDENTIUM_SCRIBE(contextus_parseris, descriptor_pendentium_contextus).\n    CONTENTUM(contextus_parseris + 8) = 0.\n"""
    init_nova = """    DESCRIPTOR_FUNCTIONUM_SCRIBE(contextus_parseris, descriptor_functionum_contextus).\n    DESCRIPTOR_PENDENTIUM_SCRIBE(contextus_parseris, descriptor_pendentium_contextus).\n    DECLARA descriptor_localium_contextus SICUT NUMERUS VALENS RESERVA_OCTETA(24).\n    SI descriptor_localium_contextus < 0 TUNC\n        PROCLAMA \"ERRATUM: memoria descriptoris localium reservata non est\".\n        REDDE 71.\n    FIN-SI.\n    DESCRIPTOR_LOCALIUM_SCRIBE(contextus_parseris, descriptor_localium_contextus).\n    CONTENTUM(contextus_parseris + 8) = 0.\n"""
    if init_ancora not in textus:
        raise SystemExit("ERRATUM: initializatio descriptorum parium non inventa est")
    textus = textus.replace(init_ancora, init_nova, 1)

# Quaesitores localium descriptoris acum accipiunt.
start = textus.index("FUNCTIO CERCA_VARIABILEM REDDENS NUMERUS.")
finis = textus.index("FUNCTIO COMPONE_CURRE REDDENS NUMERUS.", start)
novus = """FUNCTIO CERCA_VARIABILEM REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT nomen SICUT NUMERUS.\n    DECLARA idx SICUT NUMERUS VALENS 0.\n    DECLARA intervallum_inventus SICUT NUMERUS VALENS 0.\n    DECLARA aliquid_inventum SICUT NUMERUS VALENS 0.\n    DUM idx < CONTENTUM(descriptor + 16) PERFICE\n        SI LOCALE_LEGE(descriptor, idx, 0) == nomen TUNC\n            intervallum_inventus = LOCALE_LEGE(descriptor, idx, 1).\n            aliquid_inventum = 1.\n        FIN-SI.\n        idx = idx + 1.\n    FIN-DUM.\n    SI aliquid_inventum == 1 TUNC\n        REDDE intervallum_inventus.\n    FIN-SI.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO ESTNE_SERIES REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT nomen SICUT NUMERUS.\n    DECLARA idx SICUT NUMERUS VALENS 0.\n    DECLARA signum_inventum SICUT NUMERUS VALENS 0.\n    DECLARA aliquid_inventum SICUT NUMERUS VALENS 0.\n    DUM idx < CONTENTUM(descriptor + 16) PERFICE\n        SI LOCALE_LEGE(descriptor, idx, 0) == nomen TUNC\n            signum_inventum = LOCALE_LEGE(descriptor, idx, 2).\n            aliquid_inventum = 1.\n        FIN-SI.\n        idx = idx + 1.\n    FIN-DUM.\n    SI aliquid_inventum == 1 TUNC\n        REDDE signum_inventum.\n    FIN-SI.\n    REDDE 0.\nFIN-FUNCTIO.\n\n"""
textus = textus[:start] + novus + textus[finis:]

# Structura ipsa collectionis localium descriptoris memoriam propriam utitur.
start = textus.index("FUNCTIO INITIA_LOCA_DYNAMICA REDDENS NUMERUS.")
finis = textus.index("FUNCTIO COMPONE_CONCATENA_TEXTUS REDDENS NUMERUS.", start)
novus = """FUNCTIO INITIA_LOCA_DYNAMICA REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    DECLARA limen_locorum SICUT NUMERUS VALENS 64.\n    DECLARA basis SICUT NUMERUS VALENS RESERVA_OCTETA(limen_locorum * 48).\n    SI basis < 0 TUNC\n        REDDE 71.\n    FIN-SI.\n    CONTENTUM(descriptor) = basis.\n    CONTENTUM(descriptor + 8) = limen_locorum.\n    CONTENTUM(descriptor + 16) = 0.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO ASSECURA_LOCA_DYNAMICA REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT necessaria SICUT NUMERUS.\n    DECLARA limen_locorum SICUT NUMERUS VALENS CONTENTUM(descriptor + 8).\n    SI necessaria <= limen_locorum TUNC\n        REDDE 0.\n    FIN-SI.\n    DECLARA nova_capacitas SICUT NUMERUS VALENS limen_locorum * 2.\n    DUM nova_capacitas < necessaria PERFICE\n        nova_capacitas = nova_capacitas * 2.\n    FIN-DUM.\n    DECLARA nova_basis SICUT NUMERUS VALENS RESERVA_OCTETA(nova_capacitas * 48).\n    SI nova_basis < 0 TUNC\n        REDDE 71.\n    FIN-SI.\n    DECLARA basis SICUT NUMERUS VALENS CONTENTUM(descriptor).\n    DECLARA numerus_locorum SICUT NUMERUS VALENS CONTENTUM(descriptor + 16).\n    DECLARA i SICUT NUMERUS VALENS 0.\n    DECLARA octeta SICUT NUMERUS VALENS numerus_locorum * 48.\n    DUM i < octeta PERFICE\n        SCRIBE_OCTETUM_AB(nova_basis + i, OCTETUS_AB(basis + i)).\n        i = i + 1.\n    FIN-DUM.\n    CONTENTUM(descriptor) = nova_basis.\n    CONTENTUM(descriptor + 8) = nova_capacitas.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO LOCALE_LEGE REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT index SICUT NUMERUS.\n    ACCIPIT campus_localis SICUT NUMERUS.\n    SI index < 0 || index >= CONTENTUM(descriptor + 16) TUNC\n        REDDE 0.\n    FIN-SI.\n    DECLARA sedes_localis SICUT NUMERUS VALENS CONTENTUM(descriptor) + (index * 48) + (campus_localis * 8).\n    REDDE CONTENTUM(sedes_localis).\nFIN-FUNCTIO.\n\nFUNCTIO LOCALE_SCRIBE REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT index SICUT NUMERUS.\n    ACCIPIT campus_localis SICUT NUMERUS.\n    ACCIPIT valor SICUT NUMERUS.\n    DECLARA status SICUT NUMERUS VALENS ASSECURA_LOCA_DYNAMICA(descriptor, index + 1).\n    SI status != 0 TUNC\n        REDDE status.\n    FIN-SI.\n    DECLARA basis SICUT NUMERUS VALENS CONTENTUM(descriptor).\n    SI campus_localis == 0 && index >= CONTENTUM(descriptor + 16) TUNC\n        DECLARA z SICUT NUMERUS VALENS 0.\n        DUM z < 48 PERFICE\n            SCRIBE_OCTETUM_AB(basis + (index * 48) + z, 0).\n            z = z + 1.\n        FIN-DUM.\n    FIN-SI.\n    DECLARA sedes_localis SICUT NUMERUS VALENS basis + (index * 48) + (campus_localis * 8).\n    CONTENTUM(sedes_localis) = valor.\n    SI index >= CONTENTUM(descriptor + 16) TUNC\n        CONTENTUM(descriptor + 16) = index + 1.\n    FIN-SI.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO RESTITUE_LOCA_DYNAMICA REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    CONTENTUM(descriptor + 16) = 0.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO PROXIMUS_LOCUS_LIBER REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    REDDE CONTENTUM(descriptor + 16).\nFIN-FUNCTIO.\n\n"""
textus = textus[:start] + novus + textus[finis:]

# Proprietates localium quae alibi in analysi leguntur.
start = textus.index("FUNCTIO EST_FLUITANS_VARIABILIS REDDENS NUMERUS.")
finis = textus.index("FUNCTIO CAMPUS_STRUCTURAE_EST_FLUITANS REDDENS NUMERUS.", start)
novus = """FUNCTIO EST_FLUITANS_VARIABILIS REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT nomen SICUT NUMERUS.\n    DECLARA idx SICUT NUMERUS VALENS 0.\n    DECLARA resultatum SICUT NUMERUS VALENS 0.\n    DUM idx < CONTENTUM(descriptor + 16) PERFICE\n        SI LOCALE_LEGE(descriptor, idx, 0) == nomen TUNC\n            resultatum = LOCALE_LEGE(descriptor, idx, 5).\n        FIN-SI.\n        idx = idx + 1.\n    FIN-DUM.\n    REDDE resultatum.\nFIN-FUNCTIO.\n\nFUNCTIO STRUCTURA_VARIABILIS REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT nomen SICUT NUMERUS.\n    DECLARA idx SICUT NUMERUS VALENS 0.\n    DECLARA resultatum SICUT NUMERUS VALENS 0.\n    DUM idx < CONTENTUM(descriptor + 16) PERFICE\n        SI LOCALE_LEGE(descriptor, idx, 0) == nomen TUNC\n            resultatum = LOCALE_LEGE(descriptor, idx, 4).\n        FIN-SI.\n        idx = idx + 1.\n    FIN-DUM.\n    REDDE resultatum.\nFIN-FUNCTIO.\n\n"""
textus = textus[:start] + novus + textus[finis:]

start = textus.index("FUNCTIO MAGNITUDO_VARIABILIS REDDENS NUMERUS.")
finis = textus.index("FUNCTIO NUMERUS_CAMPORUM_FORMAE REDDENS NUMERUS.", start)
novus = """FUNCTIO MAGNITUDO_VARIABILIS REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT nomen SICUT NUMERUS.\n    DECLARA idx SICUT NUMERUS VALENS 0.\n    DECLARA magnitudo_inventa SICUT NUMERUS VALENS 0.\n    DECLARA aliquid_inventum_mag SICUT NUMERUS VALENS 0.\n    DUM idx < CONTENTUM(descriptor + 16) PERFICE\n        SI LOCALE_LEGE(descriptor, idx, 0) == nomen TUNC\n            magnitudo_inventa = LOCALE_LEGE(descriptor, idx, 3).\n            aliquid_inventum_mag = 1.\n        FIN-SI.\n        idx = idx + 1.\n    FIN-DUM.\n    SI aliquid_inventum_mag == 1 TUNC\n        REDDE magnitudo_inventa.\n    FIN-SI.\n    REDDE 0.\nFIN-FUNCTIO.\n\n"""
textus = textus[:start] + novus + textus[finis:]

# Duo adiutores qui metadata localium legunt contextum accipiunt.
prospice_sig = """FUNCTIO PROSPICE_EST_FLUITANS REDDENS NUMERUS.\n    ACCIPIT fons SICUT ACUS<LITTERA>.\n    ACCIPIT pos SICUT NUMERUS.\n    ACCIPIT n SICUT NUMERUS.\n    ACCIPIT tabula SICUT ORDO DE NUMERUS.\n"""
prospice_nova = prospice_sig + "    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n"
if prospice_sig in textus and "FUNCTIO PROSPICE_EST_FLUITANS REDDENS NUMERUS.\n    ACCIPIT fons SICUT ACUS<LITTERA>.\n    ACCIPIT pos SICUT NUMERUS.\n    ACCIPIT n SICUT NUMERUS.\n    ACCIPIT tabula SICUT ORDO DE NUMERUS.\n    ACCIPIT contextus_parseris" not in textus:
    textus = textus.replace(prospice_sig, prospice_nova, 1)

offset_sig = """FUNCTIO OFFSET_PTR_CAMPUS_STRUCTA REDDENS NUMERUS.\n    ACCIPIT tabula SICUT ORDO DE NUMERUS.\n    ACCIPIT fons SICUT ACUS<LITTERA>.\n    ACCIPIT pos SICUT NUMERUS.\n    ACCIPIT n SICUT NUMERUS.\n    ACCIPIT idx_campus_gen SICUT NUMERUS.\n    ACCIPIT nomen_campus SICUT NUMERUS.\n"""
offset_nova = offset_sig + "    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n"
if offset_sig in textus and "FUNCTIO OFFSET_PTR_CAMPUS_STRUCTA REDDENS NUMERUS.\n    ACCIPIT tabula SICUT ORDO DE NUMERUS.\n    ACCIPIT fons SICUT ACUS<LITTERA>.\n    ACCIPIT pos SICUT NUMERUS.\n    ACCIPIT n SICUT NUMERUS.\n    ACCIPIT idx_campus_gen SICUT NUMERUS.\n    ACCIPIT nomen_campus SICUT NUMERUS.\n    ACCIPIT contextus_parseris" not in textus:
    textus = textus.replace(offset_sig, offset_nova, 1)

D = "DESCRIPTOR_LOCALIUM_LEGE(contextus_parseris)"
replacements = {
    "INITIA_LOCA_DYNAMICA(tabula)": f"INITIA_LOCA_DYNAMICA({D})",
    "RESTITUE_LOCA_DYNAMICA(tabula)": f"RESTITUE_LOCA_DYNAMICA({D})",
    "PROXIMUS_LOCUS_LIBER(tabula)": f"PROXIMUS_LOCUS_LIBER({D})",
    "LOCALE_LEGE(tabula,": f"LOCALE_LEGE({D},",
    "LOCALE_SCRIBE(tabula,": f"LOCALE_SCRIBE({D},",
    "CERCA_VARIABILEM(tabula,": f"CERCA_VARIABILEM({D},",
    "ESTNE_SERIES(tabula,": f"ESTNE_SERIES({D},",
    "EST_FLUITANS_VARIABILIS(tabula,": f"EST_FLUITANS_VARIABILIS({D},",
    "STRUCTURA_VARIABILIS(tabula,": f"STRUCTURA_VARIABILIS({D},",
    "MAGNITUDO_VARIABILIS(tabula,": f"MAGNITUDO_VARIABILIS({D},",
}
for vetus, novum in replacements.items():
    textus = textus.replace(vetus, novum)

# Contextus additur vocationibus adiutorum supra mutatis.
textus = textus.replace(
    "PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, tabula)",
    "PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, tabula, contextus_parseris)",
)
textus = textus.replace(
    "PROSPICE_EST_FLUITANS(fons, pos_ante_prospectum, n, tabula)",
    "PROSPICE_EST_FLUITANS(fons, pos_ante_prospectum, n, tabula, contextus_parseris)",
)
textus = textus.replace(
    "PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, tabula)",
    "PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, tabula, contextus_parseris)",
)
# Omnes aliae vocationes PROSPICE in parseris contextu idem exemplar sequuntur.
textus = textus.replace(
    "PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, tabula, contextus_parseris, contextus_parseris)",
    "PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, tabula, contextus_parseris)",
)

textus = textus.replace(
    "OFFSET_PTR_CAMPUS_STRUCTA(tabula, fons, CONTENTUM(pos_fontis), n, idx_campus, nomen)",
    "OFFSET_PTR_CAMPUS_STRUCTA(tabula, fons, CONTENTUM(pos_fontis), n, idx_campus, nomen, contextus_parseris)",
)
textus = textus.replace(
    "OFFSET_PTR_CAMPUS_STRUCTA(tabula, fons, CONTENTUM(pos_fontis), n, idx_campus_aff, nomen_aff)",
    "OFFSET_PTR_CAMPUS_STRUCTA(tabula, fons, CONTENTUM(pos_fontis), n, idx_campus_aff, nomen_aff, contextus_parseris)",
)

# PROCLAMA casus eundem PROSPICE exemplar habet; globaliter quattuor argumenta residua vetantur.
if "PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, tabula)" in textus:
    raise SystemExit("ERRATUM: vocatio PROSPICE sine contextu adhuc adest")

# Initializatio localium iam descriptor explicitum accipit.
if "INITIA_LOCA_DYNAMICA(tabula)" in textus:
    raise SystemExit("ERRATUM: initium localium adhuc tabulam accipit")

for i in (2970, 2971, 2972):
    if f"tabula[{i}]" in textus:
        raise SystemExit(f"ERRATUM: tabula[{i}] post migrationem adhuc adest")

textus = textus.replace(
    "// Descriptor localium in tabula: 2970=basis, 2971=limen, 2972=quantitas.\n",
    "// Localia descriptore explicito extra tabulam utuntur.\n",
)
FONS.write_text(textus, encoding="utf-8", newline="\n")

lineae = BASIS.read_text(encoding="utf-8").splitlines()
lineae = [linea for linea in lineae if linea.strip() not in {"2970", "2971", "2972"}]
lineae = [linea.replace("VII indices, XLI accessus", "IV indices, XX accessus") for linea in lineae]
BASIS.write_text("\n".join(lineae) + "\n", encoding="utf-8", newline="\n")

if si_mutandum:
    print("RECTE: descriptor localium e tabula in contextum explicitum translatus est.")
else:
    print("RECTE: descriptor localium iam extra tabulam est.")
