#!/usr/bin/env bash

set -u

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
cd "$RADIX" || exit 1

TEMPORARIUM="$(mktemp -d)" || exit 1
trap 'rm -rf -- "$TEMPORARIUM"' EXIT HUP INT TERM

chmod 755 ./vindexc ./compilator_vindex 2>/dev/null || true

RECTA=0
ERRATA=0

recte() {
    RECTA=$((RECTA + 1))
    printf 'RECTE  %s\n' "$1"
}

erratum() {
    ERRATA=$((ERRATA + 1))
    printf 'ERRATUM  %s\n' "$1" >&2
    if [ -n "${2:-}" ]; then
        printf '          %s\n' "$2" >&2
    fi
}

exsequere_casum() {
    local nomen="$1"
    local fons="$2"
    local exspectatum="$3"
    shift 3
    local exsecutabile="$TEMPORARIUM/$nomen"
    local relatio="$TEMPORARIUM/$nomen.compilatio"

    if ! ./vindexc "$fons" -o "$exsecutabile" >"$relatio" 2>&1; then
        erratum "$nomen" "compilatio reiecta: $(tr '\n' ' ' <"$relatio")"
        return
    fi

    local productum
    productum=$("$exsecutabile" "$@")
    local status=$?
    if [ "$status" -ne 0 ]; then
        erratum "$nomen" "status exitus $status"
    elif [ "$productum" != "$exspectatum" ]; then
        erratum "$nomen" "exitus inexspectatus: [$productum] loco [$exspectatum]"
    else
        recte "$nomen"
    fi
}

respice_reiectionem() {
    local nomen="$1"
    local fons="$2"
    local fragmentum="$3"
    local exsecutabile="$TEMPORARIUM/$nomen"
    local relatio="$TEMPORARIUM/$nomen.erratum"

    ./vindexc "$fons" -o "$exsecutabile" >"$relatio" 2>&1
    local status=$?
    if [ "$status" -eq 0 ]; then
        erratum "$nomen" "fons invalidus acceptus est"
    elif [ -e "$exsecutabile" ]; then
        erratum "$nomen" "exsecutabile post erratum servatum est"
    elif ! grep -Fq "$fragmentum" "$relatio"; then
        erratum "$nomen" "diagnosticum inexspectatum: $(tr '\n' ' ' <"$relatio")"
    else
        recte "$nomen"
    fi
}

respice_reiectionem_nativam() {
    local nomen="$1"
    local fons="$2"
    local fragmentum="$3"
    local exsecutabile="$TEMPORARIUM/$nomen"
    local relatio="$TEMPORARIUM/$nomen.erratum"

    ./compilator_vindex "$fons" "$exsecutabile" >"$relatio" 2>&1
    local status=$?
    if [ "$status" -eq 0 ]; then
        erratum "$nomen" "compilator nativus fontem invalidum accepit"
    elif [ -e "$exsecutabile" ]; then
        erratum "$nomen" "compilator nativus exitum invalidum servavit"
    elif ! grep -Fq "$fragmentum" "$relatio"; then
        erratum "$nomen" "diagnosticum nativum inexspectatum: $(tr '\n' ' ' <"$relatio")"
    else
        recte "$nomen"
    fi
}

respice_auto_hospitium() {
    local gen2="$TEMPORARIUM/compilator_gen2"
    local gen3="$TEMPORARIUM/compilator_gen3"
    local relatio2="$TEMPORARIUM/gen2.log"
    local relatio3="$TEMPORARIUM/gen3.log"

    ./compilator_vindex src/compilator_vindex.vindex "$gen2" >"$relatio2" 2>&1
    local status2=$?
    chmod 755 "$gen2" 2>/dev/null || true
    "$gen2" src/compilator_vindex.vindex "$gen3" >"$relatio3" 2>&1
    local status3=$?
    chmod 755 "$gen3" 2>/dev/null || true

    if [ "$status2" -ne 0 ] || [ "$status3" -ne 0 ]; then
        erratum "auto-hospitium" "generatio2=$status2 generatio3=$status3"
    elif ! cmp -s "$gen2" "$gen3"; then
        erratum "auto-hospitium" "generationes G2 et G3 non sunt identicae"
    elif ! cmp -s ./compilator_vindex "$gen3"; then
        erratum "auto-hospitium" "binarium canonicum fonti non respondet"
    else
        recte "auto-hospitium"
    fi
}

respice_logicam_brevem() {
    local exsecutabile="$TEMPORARIUM/logica_brevis"
    local relatio="$TEMPORARIUM/logica_brevis.log"
    if ! ./compilator_vindex probationes/logica_brevis.vindex "$exsecutabile" >"$relatio" 2>&1; then
        erratum "logica-brevis" "compilatio defecit: $(tr '\n' ' ' <"$relatio")"
        return
    fi
    chmod 755 "$exsecutabile" 2>/dev/null || true
    timeout 10s "$exsecutabile" >"$relatio" 2>&1
    local status=$?
    if [ "$status" -ne 0 ]; then
        erratum "logica-brevis" "status exitus $status: $(tr '\n' ' ' <"$relatio")"
    else
        recte "logica-brevis"
    fi
}

respice_pe() {
    local exsecutabile="$TEMPORARIUM/salve.exe"
    local relatio="$TEMPORARIUM/pe.log"
    if ! ./compilator_vindex tests/casus/salve.vindex "$exsecutabile" pe >"$relatio" 2>&1; then
        erratum "pe32-plus" "generatio PE defecit: $(tr '\n' ' ' <"$relatio")"
        return
    fi
    local magia
    magia=$(od -An -tx1 -N2 "$exsecutabile" 2>/dev/null | tr -d ' \n')
    if [ "$magia" != "4d5a" ]; then
        erratum "pe32-plus" "signum MZ deest"
    elif ! file "$exsecutabile" | grep -q 'PE32+'; then
        erratum "pe32-plus" "structura PE32+ non agnoscitur"
    else
        recte "pe32-plus"
    fi
}

respice_puritatem() {
    local relatio="$TEMPORARIUM/puritas.log"
    if python3 ../../instrumenta/verifica_puritatem_sylviae.py >"$relatio" 2>&1; then
        recte "puritas-sylviae"
    else
        erratum "puritas-sylviae" "$(tr '\n' ' ' <"$relatio")"
    fi
}

respice_applicationes() {
    local exsecutabile="$TEMPORARIUM/applicationes_iv"
    local relatio="$TEMPORARIUM/applicationes_iv.log"
    if ! ./compilator_vindex probationes/applicationes_registrum_iv.vindex "$exsecutabile" >"$relatio" 2>&1; then
        erratum "applicationes-xcvi" "compilatio probationis defecit: $(tr '\n' ' ' <"$relatio")"
        return
    fi
    chmod 755 "$exsecutabile" 2>/dev/null || true
    timeout 10s "$exsecutabile" >>"$relatio" 2>&1
    local status=$?
    if [ "$status" -ne 0 ]; then
        erratum "applicationes-xcvi" "status exitus $status: $(tr '\n' ' ' <"$relatio")"
    else
        recte "applicationes-xcvi"
    fi
}

respice_terminale() {
    local exsecutabile="$TEMPORARIUM/terminale_i"
    local relatio="$TEMPORARIUM/terminale_i.log"
    if ! ./compilator_vindex probationes/terminale_i.vindex "$exsecutabile" >"$relatio" 2>&1; then
        erratum "terminale-i" "compilatio probationis defecit: $(tr '\n' ' ' <"$relatio")"
        return
    fi
    chmod 755 "$exsecutabile" 2>/dev/null || true
    timeout 10s "$exsecutabile" >>"$relatio" 2>&1
    local status=$?
    if [ "$status" -ne 0 ]; then
        erratum "terminale-i" "status exitus $status: $(tr '\n' ' ' <"$relatio")"
    else
        recte "terminale-i"
    fi
}

respice_terminale_ii() {
    local exsecutabile="$TEMPORARIUM/terminale_ii"
    local relatio="$TEMPORARIUM/terminale_ii.log"
    if ! ./compilator_vindex probationes/terminale_ii.vindex "$exsecutabile" >"$relatio" 2>&1; then
        erratum "terminale-ii" "compilatio probationis defecit: $(tr '\n' ' ' <"$relatio")"
        return
    fi
    chmod 755 "$exsecutabile" 2>/dev/null || true
    timeout 10s "$exsecutabile" >>"$relatio" 2>&1
    local status=$?
    if [ "$status" -ne 0 ]; then
        erratum "terminale-ii" "status exitus $status: $(tr '\n' ' ' <"$relatio")"
    else
        recte "terminale-ii"
    fi
}

respice_officinam() {
    local exsecutabile="$TEMPORARIUM/officina_sylvia_i"
    local relatio="$TEMPORARIUM/officina_sylvia_i.log"
    if ! ./compilator_vindex probationes/officina_sylvia_i.vindex "$exsecutabile" >"$relatio" 2>&1; then
        erratum "officina-sylvia-i" "compilatio probationis defecit: $(tr '\n' ' ' <"$relatio")"
        return
    fi
    chmod 755 "$exsecutabile" 2>/dev/null || true
    timeout 10s "$exsecutabile" >>"$relatio" 2>&1
    local status=$?
    if [ "$status" -ne 0 ]; then
        erratum "officina-sylvia-i" "status exitus $status: $(tr '\n' ' ' <"$relatio")"
    else
        recte "officina-sylvia-i"
    fi
}

respice_fenestrale() {
    local probatio="$TEMPORARIUM/fenestrale_lxxx"
    local systema="$TEMPORARIUM/fenestrale_i.elf"
    local relatio="$TEMPORARIUM/fenestrale.log"

    if ! ./compilator_vindex probationes/fenestrale_purus_i_fenestrae.vindex "$probatio" >"$relatio" 2>&1; then
        erratum "fenestrale-lxxx" "compilatio probationis defecit: $(tr '\n' ' ' <"$relatio")"
        return
    fi
    chmod 755 "$probatio" 2>/dev/null || true
    timeout 10s "$probatio" >>"$relatio" 2>&1
    local status=$?
    if [ "$status" -ne 0 ]; then
        erratum "fenestrale-lxxx" "status exitus $status: $(tr '\n' ' ' <"$relatio")"
        return
    fi

    if ! ./compilator_vindex systema/fenestrale_ii_purus_i.vindex "$systema" >>"$relatio" 2>&1; then
        erratum "fenestrale-i-integrum" "compilatio systematis defecit: $(tr '\n' ' ' <"$relatio")"
        return
    fi
    if ! file "$systema" | grep -q 'ELF 64-bit'; then
        erratum "fenestrale-i-integrum" "ELF64 validum non generatum est"
        return
    fi
    recte "fenestrale-lxxx"
    recte "fenestrale-i-integrum"
}

exsequere_casum "salve" "tests/casus/salve.vindex" "Salve, VINDEX!"
exsequere_casum "calculus" "tests/casus/calculus.vindex" $'42\n1\n2\n3\n-42\n2'
exsequere_casum "fluitans" "tests/casus/fluitans.vindex" $'4.640000\n1'
exsequere_casum "importa" "tests/casus/importa.vindex" "49"
exsequere_casum "structura-acus" "tests/casus/structura_acus.vindex" $'150\n99'
exsequere_casum "recursio" "tests/casus/recursio.vindex" "720"
exsequere_casum "argumenta" "tests/casus/argumenta.vindex" $'2\n90' "Zeta"
exsequere_casum "vxnat-partem" "tests/casus/vxnat_partem.vindex" $'83\n65\n76\n86\n69'
exsequere_casum "collectiones-numerorum" "tests/casus/collectiones_numerorum.vindex" "COLLECTIONES RECTE"
exsequere_casum "series-numerorum" "tests/casus/series_numerorum.vindex" "SERIES RECTE"
exsequere_casum "segmenta-numerorum" "tests/casus/segmenta_numerorum.vindex" "SEGMENTA RECTE"
exsequere_casum "textus-unicode" "tests/casus/textus_unicode.vindex" "UNICODE RECTE"
exsequere_casum "textus-reditus" "tests/casus/textus_reditus.vindex" "TEXTUS REDITUS RECTE"
exsequere_casum "subtextus-unicode" "tests/casus/subtextus_unicode.vindex" "SUBTEXTUS RECTE"

respice_reiectionem "erratum-principalis" "tests/casus/erratum_principalis.vindex" "FUNCTIO PRINCIPALIS deest"
respice_reiectionem "erratum-functio" "tests/casus/erratum_functio.vindex" "functio 'FUNCTIO_IGNOTA' non definita"
respice_reiectionem "erratum-blocus" "tests/casus/erratum_blocus.vindex" "FIN-DUM blocum SI"
respice_reiectionem "erratum-punctum" "tests/casus/erratum_punctum.vindex" "punctum finale deest"
respice_reiectionem "erratum-importa" "tests/casus/erratum_importa.vindex" "archivum non inventum"
respice_reiectionem "erratum-importa-imbrique" "tests/casus/erratum_importa_imbrique.vindex" "IMPORTA inclusum"

respice_reiectionem_nativam "nativum-principalis" "tests/casus/erratum_principalis.vindex" "FUNCTIO PRINCIPALIS deest"
respice_reiectionem_nativam "nativum-functio" "tests/casus/erratum_functio.vindex" "functio vocata non inventa est"
respice_reiectionem_nativam "nativum-importa" "tests/casus/erratum_importa.vindex" "fons importatus aperiri non potest"

respice_auto_hospitium
respice_logicam_brevem
respice_pe
respice_puritatem
respice_applicationes
respice_terminale
respice_terminale_ii
respice_officinam
respice_fenestrale

printf '\n%s probationes rectae; %s errata.\n' "$RECTA" "$ERRATA"
if [ "$ERRATA" -ne 0 ]; then
    exit 1
fi
