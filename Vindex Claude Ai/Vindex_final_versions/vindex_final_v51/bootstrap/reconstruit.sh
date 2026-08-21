#!/usr/bin/env bash
# Compilatorem VINDEX ab amorsa Python restituit et punctum fixum verificat.

set -u

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
FONS="$RADIX/src/compilator_vindex.vindex"
TEMPORARIUM="$(mktemp -d)" || exit 1
trap 'rm -rf -- "$TEMPORARIUM"' EXIT HUP INT TERM

EXITUS="${1:-}"
AMORSA="$TEMPORARIUM/compilator_amorsa_python"
GENERATIO_1="$TEMPORARIUM/compilator_generatio_1"
GENERATIO_2="$TEMPORARIUM/compilator_generatio_2"

printf '%s\n' "I. Amorsa Python..."
python3 "$RADIX/bootstrap/python/compilateur.py" "$FONS" "$AMORSA" || exit 1

printf '%s\n' "II. Generatio nativa prima..."
"$AMORSA" "$FONS" "$GENERATIO_1" || exit 1
chmod 755 "$GENERATIO_1" || exit 1

printf '%s\n' "III. Verificatio puncti fixi..."
"$GENERATIO_1" "$FONS" "$GENERATIO_2" || exit 1
chmod 755 "$GENERATIO_2" || exit 1

if ! cmp -s "$GENERATIO_1" "$GENERATIO_2"; then
    printf '%s\n' "ERRATUM: generationes nativae non sunt identicae." >&2
    sha256sum "$GENERATIO_1" "$GENERATIO_2" >&2
    exit 1
fi

SIGILLUM="$(sha256sum "$GENERATIO_2" | cut -d' ' -f1)"
printf 'RECTE: punctum fixum SHA-256 %s\n' "$SIGILLUM"

if [ -f "$RADIX/compilator_vindex" ]; then
    if cmp -s "$GENERATIO_2" "$RADIX/compilator_vindex"; then
        printf '%s\n' "RECTE: binarium traditum reconstructioni omnino congruit."
    else
        printf '%s\n' "MONITUM: binarium traditum a reconstructione differt." >&2
    fi
fi

if [ -n "$EXITUS" ]; then
    cp "$GENERATIO_2" "$EXITUS" || exit 1
    chmod 755 "$EXITUS" || exit 1
    printf 'Compilator reconstructus: %s\n' "$EXITUS"
fi
