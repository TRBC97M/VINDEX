#!/usr/bin/env python3
"""Descriptor formarum e tabula historica in contextum compilationis transfert."""

from pathlib import Path
import re

RADIX = Path(__file__).resolve().parents[1]
FONS = RADIX / "src" / "compilator_vindex.vindex"
BASIS = RADIX / "instrumenta" / "TABULA-LITTERALIA-053.txt"

textus = FONS.read_text(encoding="utf-8")
si_mutandum = any(f"tabula[{i}]" in textus for i in (2990, 2991, 2992, 2993))

# Descriptor formarum in sexto campo contextus communis ponitur.
ancora = """FUNCTIO DESCRIPTOR_LOCALIUM_SCRIBE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    ACCIPIT valor SICUT NUMERUS.\n    CONTENTUM(contextus_parseris + 40) = valor.\n    REDDE 0.\nFIN-FUNCTIO.\n\n"""
accessores = """FUNCTIO DESCRIPTOR_FORMARUM_LEGE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    REDDE CONTENTUM(contextus_parseris + 48).\nFIN-FUNCTIO.\n\nFUNCTIO DESCRIPTOR_FORMARUM_SCRIBE REDDENS NUMERUS.\n    ACCIPIT contextus_parseris SICUT ACUS<NUMERUS>.\n    ACCIPIT valor SICUT NUMERUS.\n    CONTENTUM(contextus_parseris + 48) = valor.\n    REDDE 0.\nFIN-FUNCTIO.\n\n"""
if "FUNCTIO DESCRIPTOR_FORMARUM_LEGE REDDENS NUMERUS." not in textus:
    if ancora not in textus:
        raise SystemExit("ERRATUM: ancora descriptoris localium non inventa est")
    textus = textus.replace(ancora, ancora + accessores, 1)

allocatio_vetus = "DECLARA contextus_parseris SICUT ACUS<NUMERUS> VALENS RESERVA_OCTETA(48)."
allocatio_nova = "DECLARA contextus_parseris SICUT ACUS<NUMERUS> VALENS RESERVA_OCTETA(56)."
if allocatio_vetus in textus:
    textus = textus.replace(allocatio_vetus, allocatio_nova, 1)
elif allocatio_nova not in textus:
    raise SystemExit("ERRATUM: allocatio contextus XLVIII octetorum non inventa est")

if "DECLARA descriptor_formarum_contextus" not in textus:
    init_ancora = """    DESCRIPTOR_LOCALIUM_SCRIBE(contextus_parseris, descriptor_localium_contextus).\n    CONTENTUM(contextus_parseris + 8) = 0.\n"""
    init_nova = """    DESCRIPTOR_LOCALIUM_SCRIBE(contextus_parseris, descriptor_localium_contextus).\n    DECLARA descriptor_formarum_contextus SICUT NUMERUS VALENS RESERVA_OCTETA(32).\n    SI descriptor_formarum_contextus < 0 TUNC\n        PROCLAMA \"ERRATUM: memoria descriptoris formarum reservata non est\".\n        REDDE 71.\n    FIN-SI.\n    DESCRIPTOR_FORMARUM_SCRIBE(contextus_parseris, descriptor_formarum_contextus).\n    CONTENTUM(contextus_parseris + 8) = 0.\n"""
    if init_ancora not in textus:
        raise SystemExit("ERRATUM: initializatio descriptoris localium non inventa est")
    textus = textus.replace(init_ancora, init_nova, 1)

# Omnes operationes formarum descriptoris memoriam propriam accipiunt.
start = textus.index("FUNCTIO INITIA_FORMAS_DYNAMICA REDDENS NUMERUS.")
finis = textus.index("FUNCTIO EST_FLUITANS_VARIABILIS REDDENS NUMERUS.", start)
novus = """FUNCTIO INITIA_FORMAS_DYNAMICA REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    DECLARA limen_formarum SICUT NUMERUS VALENS 16.\n    DECLARA basis_formarum SICUT NUMERUS VALENS RESERVA_OCTETA(limen_formarum * 40).\n    SI basis_formarum < 0 TUNC\n        REDDE 71.\n    FIN-SI.\n    CONTENTUM(descriptor) = basis_formarum.\n    CONTENTUM(descriptor + 8) = limen_formarum.\n    CONTENTUM(descriptor + 16) = 0.\n    CONTENTUM(descriptor + 24) = 0 - 1.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO ASSECURA_FORMAS_DYNAMICA REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT necessaria SICUT NUMERUS.\n    DECLARA limen_formarum SICUT NUMERUS VALENS CONTENTUM(descriptor + 8).\n    SI necessaria <= limen_formarum TUNC\n        REDDE 0.\n    FIN-SI.\n    DECLARA novum_limen SICUT NUMERUS VALENS limen_formarum * 2.\n    DUM novum_limen < necessaria PERFICE\n        novum_limen = novum_limen * 2.\n    FIN-DUM.\n    DECLARA nova_basis SICUT NUMERUS VALENS RESERVA_OCTETA(novum_limen * 40).\n    SI nova_basis < 0 TUNC\n        REDDE 71.\n    FIN-SI.\n    DECLARA basis_formarum SICUT NUMERUS VALENS CONTENTUM(descriptor).\n    DECLARA octeta SICUT NUMERUS VALENS CONTENTUM(descriptor + 16) * 40.\n    DECLARA i_formarum SICUT NUMERUS VALENS 0.\n    DUM i_formarum < octeta PERFICE\n        SCRIBE_OCTETUM_AB(nova_basis + i_formarum, OCTETUS_AB(basis_formarum + i_formarum)).\n        i_formarum = i_formarum + 1.\n    FIN-DUM.\n    CONTENTUM(descriptor) = nova_basis.\n    CONTENTUM(descriptor + 8) = novum_limen.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO FORMARUM_QUANTITAS REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    REDDE CONTENTUM(descriptor + 16).\nFIN-FUNCTIO.\n\nFUNCTIO FORMA_ULTIMA_LEGE REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    REDDE CONTENTUM(descriptor + 24).\nFIN-FUNCTIO.\n\nFUNCTIO FORMA_ULTIMA_SCRIBE REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT valor SICUT NUMERUS.\n    CONTENTUM(descriptor + 24) = valor.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO FORMA_LEGE REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT idx_formae SICUT NUMERUS.\n    ACCIPIT campus_formae SICUT NUMERUS.\n    SI idx_formae < 0 || idx_formae >= CONTENTUM(descriptor + 16) TUNC\n        REDDE 0.\n    FIN-SI.\n    DECLARA sedes_formae SICUT NUMERUS VALENS CONTENTUM(descriptor) + (idx_formae * 40) + (campus_formae * 8).\n    REDDE CONTENTUM(sedes_formae).\nFIN-FUNCTIO.\n\nFUNCTIO FORMA_SCRIBE REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT idx_formae SICUT NUMERUS.\n    ACCIPIT campus_formae SICUT NUMERUS.\n    ACCIPIT valor_formae SICUT NUMERUS.\n    DECLARA status_formae SICUT NUMERUS VALENS ASSECURA_FORMAS_DYNAMICA(descriptor, idx_formae + 1).\n    SI status_formae != 0 TUNC\n        REDDE status_formae.\n    FIN-SI.\n    DECLARA basis_formarum SICUT NUMERUS VALENS CONTENTUM(descriptor).\n    SI idx_formae >= CONTENTUM(descriptor + 16) TUNC\n        DECLARA z_formae SICUT NUMERUS VALENS 0.\n        DUM z_formae < 40 PERFICE\n            SCRIBE_OCTETUM_AB(basis_formarum + (idx_formae * 40) + z_formae, 0).\n            z_formae = z_formae + 1.\n        FIN-DUM.\n    FIN-SI.\n    DECLARA sedes_formae SICUT NUMERUS VALENS basis_formarum + (idx_formae * 40) + (campus_formae * 8).\n    CONTENTUM(sedes_formae) = valor_formae.\n    SI idx_formae >= CONTENTUM(descriptor + 16) TUNC\n        CONTENTUM(descriptor + 16) = idx_formae + 1.\n    FIN-SI.\n    REDDE 0.\nFIN-FUNCTIO.\n\nFUNCTIO INITIA_CAMPI_FORMA REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT idx_formae SICUT NUMERUS.\n    ACCIPIT limen_init SICUT NUMERUS.\n    DECLARA basis_camporum SICUT NUMERUS VALENS RESERVA_OCTETA(limen_init * 32).\n    SI basis_camporum < 0 TUNC\n        REDDE 71.\n    FIN-SI.\n    DECLARA status_campi SICUT NUMERUS VALENS FORMA_SCRIBE(descriptor, idx_formae, 2, 0).\n    SI status_campi == 0 TUNC\n        status_campi = FORMA_SCRIBE(descriptor, idx_formae, 3, limen_init).\n    FIN-SI.\n    SI status_campi == 0 TUNC\n        status_campi = FORMA_SCRIBE(descriptor, idx_formae, 4, basis_camporum).\n    FIN-SI.\n    REDDE status_campi.\nFIN-FUNCTIO.\n\nFUNCTIO ASSECURA_CAMPI_FORMA REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT idx_formae SICUT NUMERUS.\n    ACCIPIT necessaria SICUT NUMERUS.\n    DECLARA limen_camporum SICUT NUMERUS VALENS FORMA_LEGE(descriptor, idx_formae, 3).\n    SI necessaria <= limen_camporum TUNC\n        REDDE 0.\n    FIN-SI.\n    DECLARA novum_limen SICUT NUMERUS VALENS limen_camporum * 2.\n    SI novum_limen < 1 TUNC\n        novum_limen = 8.\n    FIN-SI.\n    DUM novum_limen < necessaria PERFICE\n        novum_limen = novum_limen * 2.\n    FIN-DUM.\n    DECLARA nova_basis SICUT NUMERUS VALENS RESERVA_OCTETA(novum_limen * 32).\n    SI nova_basis < 0 TUNC\n        REDDE 71.\n    FIN-SI.\n    DECLARA basis_camporum SICUT NUMERUS VALENS FORMA_LEGE(descriptor, idx_formae, 4).\n    DECLARA octeta SICUT NUMERUS VALENS FORMA_LEGE(descriptor, idx_formae, 2) * 32.\n    DECLARA i_camporum SICUT NUMERUS VALENS 0.\n    DUM i_camporum < octeta PERFICE\n        SCRIBE_OCTETUM_AB(nova_basis + i_camporum, OCTETUS_AB(basis_camporum + i_camporum)).\n        i_camporum = i_camporum + 1.\n    FIN-DUM.\n    DECLARA status_campi SICUT NUMERUS VALENS FORMA_SCRIBE(descriptor, idx_formae, 3, novum_limen).\n    SI status_campi == 0 TUNC\n        status_campi = FORMA_SCRIBE(descriptor, idx_formae, 4, nova_basis).\n    FIN-SI.\n    REDDE status_campi.\nFIN-FUNCTIO.\n\nFUNCTIO CAMPUS_FORMA_LEGE REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT idx_formae SICUT NUMERUS.\n    ACCIPIT idx_campi SICUT NUMERUS.\n    ACCIPIT campus_campi SICUT NUMERUS.\n    SI idx_campi < 0 || idx_campi >= FORMA_LEGE(descriptor, idx_formae, 2) TUNC\n        REDDE 0.\n    FIN-SI.\n    DECLARA basis_camporum SICUT NUMERUS VALENS FORMA_LEGE(descriptor, idx_formae, 4).\n    DECLARA sedes_campi SICUT NUMERUS VALENS basis_camporum + (idx_campi * 32) + (campus_campi * 8).\n    REDDE CONTENTUM(sedes_campi).\nFIN-FUNCTIO.\n\nFUNCTIO CAMPUS_FORMA_SCRIBE REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT idx_formae SICUT NUMERUS.\n    ACCIPIT idx_campi SICUT NUMERUS.\n    ACCIPIT campus_campi SICUT NUMERUS.\n    ACCIPIT valor_campi SICUT NUMERUS.\n    DECLARA status_campi SICUT NUMERUS VALENS ASSECURA_CAMPI_FORMA(descriptor, idx_formae, idx_campi + 1).\n    SI status_campi != 0 TUNC\n        REDDE status_campi.\n    FIN-SI.\n    DECLARA basis_camporum SICUT NUMERUS VALENS FORMA_LEGE(descriptor, idx_formae, 4).\n    DECLARA quantitas_camporum SICUT NUMERUS VALENS FORMA_LEGE(descriptor, idx_formae, 2).\n    SI idx_campi >= quantitas_camporum TUNC\n        DECLARA z_campi SICUT NUMERUS VALENS 0.\n        DUM z_campi < 32 PERFICE\n            SCRIBE_OCTETUM_AB(basis_camporum + (idx_campi * 32) + z_campi, 0).\n            z_campi = z_campi + 1.\n        FIN-DUM.\n    FIN-SI.\n    DECLARA sedes_campi SICUT NUMERUS VALENS basis_camporum + (idx_campi * 32) + (campus_campi * 8).\n    CONTENTUM(sedes_campi) = valor_campi.\n    SI idx_campi >= quantitas_camporum TUNC\n        status_campi = FORMA_SCRIBE(descriptor, idx_formae, 2, idx_campi + 1).\n    FIN-SI.\n    REDDE status_campi.\nFIN-FUNCTIO.\n\nFUNCTIO INDEX_CAMPUS_ULTIMAE_FORMAE REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT nomen_campus SICUT NUMERUS.\n    DECLARA idx_formae SICUT NUMERUS VALENS FORMA_ULTIMA_LEGE(descriptor).\n    SI idx_formae < 0 TUNC\n        REDDE 0.\n    FIN-SI.\n    DECLARA quantitas_camporum SICUT NUMERUS VALENS FORMA_LEGE(descriptor, idx_formae, 2).\n    DECLARA idx_campi SICUT NUMERUS VALENS 0.\n    DECLARA resultatum SICUT NUMERUS VALENS quantitas_camporum.\n    DUM idx_campi < quantitas_camporum PERFICE\n        SI CAMPUS_FORMA_LEGE(descriptor, idx_formae, idx_campi, 0) == nomen_campus TUNC\n            resultatum = idx_campi.\n        FIN-SI.\n        idx_campi = idx_campi + 1.\n    FIN-DUM.\n    REDDE resultatum.\nFIN-FUNCTIO.\n\nFUNCTIO INDEX_STRUCTURAE REDDENS NUMERUS.\n    ACCIPIT descriptor SICUT ACUS<NUMERUS>.\n    ACCIPIT nomen_forma SICUT NUMERUS.\n    DECLARA idx SICUT NUMERUS VALENS 0.\n    DECLARA resultatum SICUT NUMERUS VALENS 0 - 1.\n    DUM idx < FORMARUM_QUANTITAS(descriptor) PERFICE\n        SI FORMA_LEGE(descriptor, idx, 0) == nomen_forma TUNC\n            resultatum = idx.\n        FIN-SI.\n        idx = idx + 1.\n    FIN-DUM.\n    REDDE resultatum.\nFIN-FUNCTIO.\n\n"""
textus = textus[:start] + novus + textus[finis:]

# Adiutores camporum structuram descriptoris formarum accipiunt.
start = textus.index("FUNCTIO CAMPUS_STRUCTURAE_EST_FLUITANS REDDENS NUMERUS.")
finis = textus.index("FUNCTIO SIGNUM_AB_POSITIONE REDDENS NUMERUS.", start)
blocus = textus[start:finis]
blocus = blocus.replace("ACCIPIT tabula SICUT ORDO DE NUMERUS.", "ACCIPIT descriptor SICUT ACUS<NUMERUS>.")
blocus = blocus.replace("FORMA_LEGE(tabula,", "FORMA_LEGE(descriptor,")
blocus = blocus.replace("CAMPUS_FORMA_LEGE(tabula,", "CAMPUS_FORMA_LEGE(descriptor,")
textus = textus[:start] + blocus + textus[finis:]

# Adiutores mixti: descriptor formarum + contextus localium.
offset_start = textus.index("FUNCTIO OFFSET_PTR_CAMPUS_STRUCTA REDDENS NUMERUS.")
offset_end = textus.index("FUNCTIO INDEX_STRUCTURAE_INTERIOR_ACUS REDDENS NUMERUS.", offset_start)
offset = textus[offset_start:offset_end]
offset = offset.replace("ACCIPIT tabula SICUT ORDO DE NUMERUS.", "ACCIPIT descriptor_formarum SICUT ACUS<NUMERUS>.", 1)
offset = offset.replace("OFFSET_CUMULATIVUS_CAMPI(tabula,", "OFFSET_CUMULATIVUS_CAMPI(descriptor_formarum,")
offset = offset.replace("CAMPUS_STRUCTURAE_OFFSET(tabula,", "CAMPUS_STRUCTURAE_OFFSET(descriptor_formarum,")
textus = textus[:offset_start] + offset + textus[offset_end:]

start = textus.index("FUNCTIO INDEX_STRUCTURAE_INTERIOR_ACUS REDDENS NUMERUS.")
finis = textus.index("FUNCTIO COMPONE_VERIFICA_TAS REDDENS NUMERUS.", start)
blocus = textus[start:finis]
blocus = blocus.replace("ACCIPIT tabula SICUT ORDO DE NUMERUS.", "ACCIPIT descriptor SICUT ACUS<NUMERUS>.", 1)
blocus = blocus.replace("INDEX_STRUCTURAE(tabula,", "INDEX_STRUCTURAE(descriptor,")
textus = textus[:start] + blocus + textus[finis:]

start = textus.index("FUNCTIO OFFSET_CUMULATIVUS_CAMPI REDDENS NUMERUS.")
finis = textus.index("FUNCTIO MAGNITUDO_VARIABILIS REDDENS NUMERUS.", start)
blocus = textus[start:finis]
blocus = blocus.replace("ACCIPIT tabula SICUT ORDO DE NUMERUS.", "ACCIPIT descriptor SICUT ACUS<NUMERUS>.", 1)
blocus = blocus.replace("FORMA_ULTIMA_LEGE(tabula)", "FORMA_ULTIMA_LEGE(descriptor)")
blocus = blocus.replace("tabula[2993]", "FORMA_ULTIMA_LEGE(descriptor)")
blocus = blocus.replace("FORMA_LEGE(tabula,", "FORMA_LEGE(descriptor,")
blocus = blocus.replace("CAMPUS_FORMA_LEGE(tabula,", "CAMPUS_FORMA_LEGE(descriptor,")
textus = textus[:start] + blocus + textus[finis:]

start = textus.index("FUNCTIO NUMERUS_CAMPORUM_FORMAE REDDENS NUMERUS.")
finis = textus.index("FUNCTIO ANALYSA_EXPRESSIO REDDENS NUMERUS.", start)
blocus = textus[start:finis]
blocus = blocus.replace("ACCIPIT tabula SICUT ORDO DE NUMERUS.", "ACCIPIT descriptor SICUT ACUS<NUMERUS>.", 1)
blocus = blocus.replace("INDEX_STRUCTURAE(tabula,", "INDEX_STRUCTURAE(descriptor,")
blocus = blocus.replace("FORMA_LEGE(tabula,", "FORMA_LEGE(descriptor,")
textus = textus[:start] + blocus + textus[finis:]

# PROSPICE accipit descriptor formarum loco tabulae.
prospice_start = textus.index("FUNCTIO PROSPICE_EST_FLUITANS REDDENS NUMERUS.")
prospice_end = textus.index("FUNCTIO ANALYSA_TERMINUM REDDENS NUMERUS.", prospice_start)
prospice = textus[prospice_start:prospice_end]
prospice = prospice.replace("ACCIPIT tabula SICUT ORDO DE NUMERUS.", "ACCIPIT descriptor_formarum SICUT ACUS<NUMERUS>.", 1)
prospice = prospice.replace("CAMPUS_STRUCTURAE_EST_FLUITANS(tabula,", "CAMPUS_STRUCTURAE_EST_FLUITANS(descriptor_formarum,")
textus = textus[:prospice_start] + prospice + textus[prospice_end:]

D = "DESCRIPTOR_FORMARUM_LEGE(contextus_parseris)"
for nomen in (
    "FORMA_LEGE", "FORMA_SCRIBE", "INITIA_CAMPI_FORMA", "ASSECURA_CAMPI_FORMA",
    "CAMPUS_FORMA_LEGE", "CAMPUS_FORMA_SCRIBE", "INDEX_CAMPUS_ULTIMAE_FORMAE",
    "INDEX_STRUCTURAE", "CAMPUS_STRUCTURAE_EST_FLUITANS", "CAMPUS_STRUCTURAE_MAGNITUDO",
    "CAMPUS_STRUCTURAE_OFFSET", "OFFSET_CUMULATIVUS_CAMPI", "NUMERUS_CAMPORUM_FORMAE",
    "INDEX_STRUCTURAE_INTERIOR_ACUS", "OFFSET_PTR_CAMPUS_STRUCTA"
):
    textus = textus.replace(f"{nomen}(tabula,", f"{nomen}({D},")

textus = textus.replace("INITIA_FORMAS_DYNAMICA(tabula)", f"INITIA_FORMAS_DYNAMICA({D})")
textus = textus.replace(
    "PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, tabula, contextus_parseris)",
    f"PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, {D}, contextus_parseris)",
)
textus = textus.replace(
    "PROSPICE_EST_FLUITANS(fons, pos_ante_prospectum, n, tabula, contextus_parseris)",
    f"PROSPICE_EST_FLUITANS(fons, pos_ante_prospectum, n, {D}, contextus_parseris)",
)

# Lectiones/scripturae directae residuae in PRINCIPALIS.
textus = textus.replace("tabula[2992]", f"FORMARUM_QUANTITAS({D})")
textus = re.sub(
    r"(?m)^([ \t]*)tabula\[2993\] = ([^.]+)\.$",
    rf"\1FORMA_ULTIMA_SCRIBE({D}, \2).",
    textus,
)
textus = textus.replace("tabula[2993]", f"FORMA_ULTIMA_LEGE({D})")

if "PROSPICE_EST_FLUITANS(fons, CONTENTUM(pos_fontis), n, tabula" in textus:
    raise SystemExit("ERRATUM: PROSPICE formas adhuc per tabulam accipit")
for i in (2990, 2991, 2992, 2993):
    if f"tabula[{i}]" in textus:
        raise SystemExit(f"ERRATUM: tabula[{i}] post migrationem adhuc adest")

textus = textus.replace(
    "// Ordinatio tabulae historica ad metadata non-localia adhuc adhibetur.\n",
    "// Metadata compilationis descriptoribus explicitis servantur.\n",
)
textus = textus.replace(
    "// Descriptor formarum: 2990=basis, 2991=limen, 2992=quantitas, 2993=index ultimae formae.\n",
    "// Formae descriptore explicito extra tabulam utuntur.\n",
)
textus = textus.replace(
    "// Cursor pilae functionis in contextu explicito servatur; descriptores collectionum adhuc in tabula manent.\n",
    "// Cursor pilae et descriptores collectionum in contextu explicito servantur.\n",
)

FONS.write_text(textus, encoding="utf-8", newline="\n")

lineae = BASIS.read_text(encoding="utf-8").splitlines()
lineae = [linea for linea in lineae if linea.strip() not in {"2990", "2991", "2992", "2993"}]
lineae = [linea.replace("IV indices, XX accessus", "nulli indices, nullus accessus") for linea in lineae]
BASIS.write_text("\n".join(lineae) + "\n", encoding="utf-8", newline="\n")

if si_mutandum:
    print("RECTE: descriptor formarum e tabula in contextum explicitum translatus est.")
else:
    print("RECTE: descriptor formarum iam extra tabulam est.")
