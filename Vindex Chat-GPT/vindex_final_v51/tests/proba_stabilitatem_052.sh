#!/usr/bin/env bash
set -eu

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
PRAEPARATOR="$RADIX/instrumenta/vindex_praepara.py"
FONS="$RADIX/tests/casus/commentarium_intra_functionem.vindex"
TEMP_FONS="$(mktemp "${TMPDIR:-/tmp}/vindex-commentarium.XXXXXX")"
TEMP_EXE="$(mktemp "${TMPDIR:-/tmp}/vindex-commentarium-exe.XXXXXX")"

purga() {
    rm -f -- "$TEMP_FONS" "$TEMP_EXE"
}
trap purga EXIT HUP INT TERM

python3 "$PRAEPARATOR" "$FONS" "$TEMP_FONS"

MENSURA_ANTE="$(wc -c < "$FONS")"
MENSURA_POST="$(wc -c < "$TEMP_FONS")"
if [ "$MENSURA_ANTE" -ne "$MENSURA_POST" ]; then
    printf '%s\n' "ERRATUM: praeparator mensuram fontis mutavit." >&2
    exit 1
fi

if grep -q '// Hoc commentarium' "$TEMP_FONS"; then
    printf '%s\n' "ERRATUM: commentarium lineare mansit." >&2
    exit 1
fi

"$RADIX/vindexc" "$FONS" "$TEMP_EXE"
EXITUS="$($TEMP_EXE)"
if [ "$EXITUS" != "42" ]; then
    printf 'ERRATUM: exitus exspectatus 42, inventus %s.\n' "$EXITUS" >&2
    exit 1
fi

printf '%s\n' "RECTE: commentaria intra functionem praeparantur et programma exsequitur."
