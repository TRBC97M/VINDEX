#!/usr/bin/env bash
# PE32+ VINDEX structuraliter probat sine Wine vel Windows exsequi.
set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMPUS="$(mktemp -d)"
trap 'rm -rf -- "$TEMPUS"' EXIT HUP INT TERM

FONS="$TEMPUS/minimum_pe.vindex"
EXE="$TEMPUS/minimum_pe.exe"

cat >"$FONS" <<'VINDEX'
FUNCTIO PRINCIPALIS REDDENS NUMERUS.
    REDDE 42.
FIN-FUNCTIO.
VINDEX

"$RADIX/compilator_vindex" "$FONS" "$EXE" pe
python3 "$RADIX/tests/proba_pe_structuram_053.py" "$EXE" \
    --requirit ExitProcess \
    --requirit VirtualAlloc

printf '%s\n' 'RECTE: minimum PE VINDEX structuraliter comprobatum est.'
