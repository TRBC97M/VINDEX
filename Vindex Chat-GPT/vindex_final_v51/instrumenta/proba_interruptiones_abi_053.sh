#!/usr/bin/env bash
# P12-V3: ABI tractatoris, intrinseca privilegiata et IRETQ probantur.

set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-interruptiones-abi.XXXXXX")"
trap 'rm -rf "$TEMPORARIUM" 2>/dev/null || true' EXIT HUP INT TERM

nuntia() { printf '%s\n' "$*"; }
defecit() { printf 'DEFECIT: %s\n' "$1" >&2; exit "$2"; }

nuntia 'I. Fons ABI et payload UEFI verificantur...'
( cd "$RADIX" && python3 instrumenta/vindex_verifica.py probationes/interruptiones_abi.vindex ) \
    || defecit 'verificatio ABI' 1
( cd "$RADIX/systema" && python3 ../instrumenta/vindex_verifica.py proba_interruptiones_msi.vindex ) \
    || defecit 'verificatio payload MSI' 1

nuntia 'II. Calculi IDT/MSI et intrinseca non privilegiata native exercentur...'
( cd "$RADIX" && ./compilator_vindex probationes/interruptiones_abi.vindex \
    "$TEMPORARIUM/interruptiones-abi" ) >"$TEMPORARIUM/native.log" 2>&1 \
    || { cat "$TEMPORARIUM/native.log" >&2; defecit 'compilatio nativa' 2; }
chmod +x "$TEMPORARIUM/interruptiones-abi"
"$TEMPORARIUM/interruptiones-abi" || defecit 'probatio nativa' 2
nuntia '   RECTE: selector, RFLAGS, sedes RIP et calculi portae/MSI.'

nuntia 'III. Codex tractatoris x86-64 examinatur...'
( cd "$RADIX/systema" && ../compilator_vindex proba_interruptiones_msi.vindex \
    "$TEMPORARIUM/BOOTX64.EFI" uefi ) >"$TEMPORARIUM/uefi.log" 2>&1 \
    || { cat "$TEMPORARIUM/uefi.log" >&2; defecit 'compilatio UEFI' 3; }
file "$TEMPORARIUM/BOOTX64.EFI" | grep -q 'PE32+.*EFI application' \
    || defecit 'exsecutabile EFI invalidum' 3
python3 - "$TEMPORARIUM/BOOTX64.EFI" <<'PY'
from pathlib import Path
import sys

data = Path(sys.argv[1]).read_bytes()
patterns = {
    "SIDT": bytes.fromhex("0f 01 08"),
    "RFLAGS": bytes.fromhex("9c 58"),
    "CS": bytes.fromhex("31 c0 66 8c c8"),
    "SEDES_RIP": bytes.fromhex("48 8d 05"),
    "PROLOGUM": bytes.fromhex(
        "50 51 52 53 55 56 57 41 50 41 51 41 52 41 53 41 54 "
        "41 55 41 56 41 57 48 89 e5 48 83 e4 f0"
    ),
    "EPILOGUS": bytes.fromhex(
        "48 89 ec 41 5f 41 5e 41 5d 41 5c 41 5b 41 5a 41 59 "
        "41 58 5f 5e 5d 5b 5a 59 58 48 cf"
    ),
}
missing = [name for name, pattern in patterns.items() if pattern not in data]
if missing:
    raise SystemExit("DEFECIT: codex abest: " + ", ".join(missing))
if data.count(bytes.fromhex("48 cf")) < 2:
    raise SystemExit("DEFECIT: via REDDE et finis implicitus IRETQ non habent")
print("   RECTE: GPR servantur, pila coaequatur et IRETQ bis adest.")
PY

nuntia ''
nuntia '=== ABI INTERRUPTIONUM PROBATA ==='
