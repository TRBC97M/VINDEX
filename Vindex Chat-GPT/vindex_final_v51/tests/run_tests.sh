#!/usr/bin/env bash

set -u

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
cd "$RADIX" || exit 1

TEMPORAIRE="$(mktemp -d)" || exit 1
trap 'rm -rf -- "$TEMPORAIRE"' EXIT HUP INT TERM

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
    local exsecutabile="$TEMPORAIRE/$nomen"
    local relatio="$TEMPORAIRE/$nomen.compilatio"

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
    local exsecutabile="$TEMPORAIRE/$nomen"
    local relatio="$TEMPORAIRE/$nomen.erratum"

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
    local exsecutabile="$TEMPORAIRE/$nomen"
    local relatio="$TEMPORAIRE/$nomen.erratum"

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
    local fons="$TEMPORAIRE/compilator_auto.vindex"
    local gen2="$TEMPORAIRE/compilator_gen2"
    local gen3="$TEMPORAIRE/compilator_gen3"
    cp src/compilator_vindex.vindex "$fons"
    ./compilator_vindex "$fons" "$gen2" >"$TEMPORAIRE/gen2.log" 2>&1
    local status2=$?
    chmod 755 "$gen2" 2>/dev/null
    "$gen2" "$fons" "$gen3" >"$TEMPORAIRE/gen3.log" 2>&1
    local status3=$?
    if [ "$status2" -ne 0 ] || [ "$status3" -ne 0 ]; then
        erratum "auto-hospitium" "generatio2=$status2 generatio3=$status3"
    elif ! cmp -s "$gen2" "$gen3"; then
        erratum "auto-hospitium" "generationes non sunt identicae"
    else
        recte "auto-hospitium"
    fi
}

respice_amorsam() {
    local relatio="$TEMPORAIRE/amorsa.log"
    if ./bootstrap/reconstruit.sh >"$relatio" 2>&1; then
        recte "amorsa-python"
    else
        erratum "amorsa-python" "$(tr '\n' ' ' <"$relatio")"
    fi
}

respice_officinam() {
    local relatio="$TEMPORAIRE/officina.log"
    if python3 -m unittest discover -s tests -p 'test_officina.py' -v >"$relatio" 2>&1; then
        recte "officina"
    else
        erratum "officina" "$(tr '\n' ' ' <"$relatio")"
    fi
}

respice_systema() {
    local relatio="$TEMPORAIRE/systema.log"
    if python3 -m unittest discover -s tests -p 'test_systema.py' -v >"$relatio" 2>&1; then
        recte "systema"
    else
        erratum "systema" "$(tr '\n' ' ' <"$relatio")"
    fi
}

exsequere_casum "salve" "tests/casus/salve.vindex" "Salve, VINDEX!"
exsequere_casum "calculus" "tests/casus/calculus.vindex" $'42\n1\n2\n3\n-42\n2'
exsequere_casum "fluitans" "tests/casus/fluitans.vindex" $'4.640000\n1'
exsequere_casum "importa" "tests/casus/importa.vindex" "49"
exsequere_casum "structura-acus" "tests/casus/structura_acus.vindex" $'150\n99'
exsequere_casum "recursio" "tests/casus/recursio.vindex" "720"
exsequere_casum "argumenta" "tests/casus/argumenta.vindex" $'2\n90' "Zeta"
exsequere_casum "vxnat-partem" "tests/casus/vxnat_partem.vindex" $'83\n65\n76\n86\n69'
exsequere_casum "vocationes-nullae" "tests/casus/vocationes_nullae.vindex" "7168"

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
respice_amorsam
respice_officinam
respice_systema

printf '\n%s probationes rectae; %s errata.\n' "$RECTA" "$ERRATA"
if [ "$ERRATA" -ne 0 ]; then
    exit 1
fi
