#!/usr/bin/env bash
# VINDEX 0.53: PROCLAMA sub modo PE (GetStdHandle + WriteFile) localiter comprobat.
# Requirit Wine 9.0 (wine64) in systemate. Non exspectat CI remotam.

set -u

RADIX="Vindex Chat-GPT/vindex_final_v51"
COMPILATOR="$RADIX/compilator_vindex"
EXEMPLA="$RADIX/examples"
TEMPUS=$(mktemp -d /tmp/proba-proclama-pe-053.XXXXXX)
SUCCESSUS=0

WINE=$(command -v wine64 || echo /usr/lib/wine/wine64)
if [ ! -x "$WINE" ]; then
    echo "ERRATUM: wine64 non inventus est. Instrumentum installandum: apt-get install wine64 wine"
    exit 2
fi
export WINEDEBUG=-all

si_erratum() {
    echo "ERRATUM: $1"
    SUCCESSUS=1
}

# --- probatio 1: catena litteralis, modus ELF ---
"$COMPILATOR" "$EXEMPLA/proclama_catena_pe_053.vindex" "$TEMPUS/catena_elf" || si_erratum "compilatio ELF (catena) defecit"
chmod +x "$TEMPUS/catena_elf"
SORTIE_ELF=$("$TEMPUS/catena_elf")
CODEX_ELF=$?
if [ "$SORTIE_ELF" != "Salve ex PE!" ] || [ "$CODEX_ELF" != "33" ]; then
    si_erratum "ELF catena: exspectatum 'Salve ex PE!' + exitus 33, inventum '$SORTIE_ELF' + exitus $CODEX_ELF"
else
    echo "RECTE: ELF catena -- '$SORTIE_ELF', exitus $CODEX_ELF"
fi

# --- probatio 2: catena litteralis, modus PE, sub Wine ---
"$COMPILATOR" "$EXEMPLA/proclama_catena_pe_053.vindex" "$TEMPUS/catena_pe.exe" pe || si_erratum "compilatio PE (catena) defecit"
SORTIE_PE=$("$WINE" "$TEMPUS/catena_pe.exe" 2>/dev/null)
if [[ "$SORTIE_PE" == *"Salve ex PE!"* ]]; then
    echo "RECTE: PE catena -- 'Salve ex PE!' scriptum correcte (terminatio limpida non exspectatur, vide RELATIO-PE-WINDOWS.md)"
else
    si_erratum "PE catena: 'Salve ex PE!' non inventum in exitu"
fi

# --- probatio 3: numeri et vocationes multiplices, modus ELF ---
"$COMPILATOR" "$EXEMPLA/proclama_multi_pe_053.vindex" "$TEMPUS/multi_elf" || si_erratum "compilatio ELF (multi) defecit"
chmod +x "$TEMPUS/multi_elf"
SORTIE_MULTI_ELF=$("$TEMPUS/multi_elf")
CODEX_MULTI_ELF=$?
ATTENDU_MULTI=$'Premier\n999\nDernier'
if [ "$SORTIE_MULTI_ELF" != "$ATTENDU_MULTI" ] || [ "$CODEX_MULTI_ELF" != "7" ]; then
    si_erratum "ELF multi: exspectatum '$ATTENDU_MULTI' + exitus 7, inventum '$SORTIE_MULTI_ELF' + exitus $CODEX_MULTI_ELF"
else
    echo "RECTE: ELF multi -- exitus $CODEX_MULTI_ELF"
fi

# --- probatio 4: numeri et vocationes multiplices, modus PE ---
"$COMPILATOR" "$EXEMPLA/proclama_multi_pe_053.vindex" "$TEMPUS/multi_pe.exe" pe || si_erratum "compilatio PE (multi) defecit"
SORTIE_MULTI_PE=$("$WINE" "$TEMPUS/multi_pe.exe" 2>/dev/null)
if [[ "$SORTIE_MULTI_PE" == *"Premier"* ]] && [[ "$SORTIE_MULTI_PE" == *"999"* ]] && [[ "$SORTIE_MULTI_PE" == *"Dernier"* ]]; then
    echo "RECTE: PE multi -- omnes tres partes scriptae correcte"
else
    si_erratum "PE multi: una vel plures partes absunt ab exitu"
fi

# --- probatio 5: auto-hospitium punctum fixum post has mutationes ---
"$COMPILATOR" "$RADIX/src/compilator_vindex.vindex" "$TEMPUS/gen1" || si_erratum "auto-hospitium G1 defecit"
chmod +x "$TEMPUS/gen1"
"$TEMPUS/gen1" "$RADIX/src/compilator_vindex.vindex" "$TEMPUS/gen2" || si_erratum "auto-hospitium G2 defecit"
chmod +x "$TEMPUS/gen2"
"$TEMPUS/gen2" "$RADIX/src/compilator_vindex.vindex" "$TEMPUS/gen3" || si_erratum "auto-hospitium G3 defecit"
SUMMA_G2=$(sha256sum "$TEMPUS/gen2" | cut -d' ' -f1)
SUMMA_G3=$(sha256sum "$TEMPUS/gen3" | cut -d' ' -f1)
if [ "$SUMMA_G2" != "$SUMMA_G3" ]; then
    si_erratum "punctum fixum non servatum: G2=$SUMMA_G2 G3=$SUMMA_G3"
else
    echo "RECTE: punctum fixum servatum (G2=G3=$SUMMA_G2)"
fi

rm -rf "$TEMPUS"

if [ "$SUCCESSUS" = 0 ]; then
    echo "=== OMNES PROBATIONES RECTAE ==="
else
    echo "=== ALIQUAE PROBATIONES DEFECERUNT ==="
fi
exit $SUCCESSUS
