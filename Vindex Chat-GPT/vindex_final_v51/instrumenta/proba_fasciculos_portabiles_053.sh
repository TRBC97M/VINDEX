#!/usr/bin/env bash
# Contractum APERI/LEGE/MITTE/CLAUDE sub ELF custodit ante backend Win64.
set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMPUS="$(mktemp -d)"
trap 'rm -rf -- "$TEMPUS"' EXIT HUP INT TERM

EXE="$TEMPUS/fasciculi_portabiles"
"$RADIX/compilator_vindex" "$RADIX/tests/casus/fasciculi_portabiles.vindex" "$EXE"
chmod 755 "$EXE"
(
    cd "$TEMPUS"
    ./fasciculi_portabiles
)
STATUS=$?

if [ "$STATUS" -ne 0 ]; then
    printf 'ERRATUM: contractus fasciculorum status %s reddit.\n' "$STATUS" >&2
    exit "$STATUS"
fi

printf '%s\n' 'RECTE: APERI_SCRIBERE/MITTE/APERI_LEGERE/LEGE/CLAUDE sub ELF congruunt.'
