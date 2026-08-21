#!/usr/bin/env bash
set -eu

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
PRAEPARATOR="$RADIX/instrumenta/vindex_praepara.py"
TUTELA="$RADIX/instrumenta/vindex_tutela_052.py"
FONS_COMMENTARII="$RADIX/tests/casus/commentarium_intra_functionem.vindex"
FONS_MAIUSCULI="$RADIX/tests/casus/variabilis_maiuscula.vindex"
TEMP_FONS="$(mktemp "${TMPDIR:-/tmp}/vindex-commentarium.XXXXXX")"
TEMP_EXE="$(mktemp "${TMPDIR:-/tmp}/vindex-commentarium-exe.XXXXXX")"
TEMP_ERR="$(mktemp "${TMPDIR:-/tmp}/vindex-tutela.XXXXXX")"

purga() {
    rm -f -- "$TEMP_FONS" "$TEMP_EXE" "$TEMP_ERR"
}
trap purga EXIT HUP INT TERM

python3 "$PRAEPARATOR" "$FONS_COMMENTARII" "$TEMP_FONS"

MENSURA_ANTE="$(wc -c < "$FONS_COMMENTARII")"
MENSURA_POST="$(wc -c < "$TEMP_FONS")"
if [ "$MENSURA_ANTE" -ne "$MENSURA_POST" ]; then
    printf '%s\n' "ERRATUM: praeparator mensuram fontis mutavit." >&2
    exit 1
fi

if grep -q '// Hoc commentarium' "$TEMP_FONS"; then
    printf '%s\n' "ERRATUM: commentarium lineare mansit." >&2
    exit 1
fi

"$RADIX/vindexc" "$FONS_COMMENTARII" "$TEMP_EXE"
EXITUS="$($TEMP_EXE)"
if [ "$EXITUS" != "42" ]; then
    printf 'ERRATUM: exitus exspectatus 42, inventus %s.\n' "$EXITUS" >&2
    exit 1
fi

if python3 "$TUTELA" "$FONS_MAIUSCULI" 2>"$TEMP_ERR"; then
    printf '%s\n' "ERRATUM: tutela identificatorem maiusculum non intercepit." >&2
    exit 1
fi
if ! grep -q "IMAGE_BASE" "$TEMP_ERR"; then
    printf '%s\n' "ERRATUM: tutela nomen identificatoris in diagnostico non retulit." >&2
    exit 1
fi
if ! grep -q "compilator non vocatur" "$TEMP_ERR"; then
    printf '%s\n' "ERRATUM: tutela causam interruptionis non exposuit." >&2
    exit 1
fi

printf '%s\n' "RECTE: commentaria praeparantur et defectus identificatorum maiusculorum ante compilatorem intercipitur."
