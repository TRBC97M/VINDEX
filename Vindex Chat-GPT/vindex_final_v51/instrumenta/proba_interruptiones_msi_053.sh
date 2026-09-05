#!/usr/bin/env bash
# P12-V3: interruptio MSI vera ex apparatu PCI EDU sub QEMU comprobatur.

set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-interruptiones-msi.XXXXXX")"
QEMU_PID=""
purga() {
    if [ -n "$QEMU_PID" ] && kill -0 "$QEMU_PID" 2>/dev/null; then
        kill "$QEMU_PID" 2>/dev/null || true
        wait "$QEMU_PID" 2>/dev/null || true
    fi
    rm -rf "$TEMPORARIUM" 2>/dev/null || true
}
trap purga EXIT HUP INT TERM

nuntia() { printf '%s\n' "$*"; }
defecit() { printf 'DEFECIT: %s\n' "$1" >&2; exit "$2"; }

OVMF_CODE=""
for v in /usr/share/OVMF/OVMF_CODE_4M.fd /usr/share/OVMF/OVMF_CODE.fd; do
    [ -f "$v" ] && { OVMF_CODE="$v"; break; }
done
OVMF_VARS=""
for v in /usr/share/OVMF/OVMF_VARS_4M.fd /usr/share/OVMF/OVMF_VARS.fd; do
    [ -f "$v" ] && { OVMF_VARS="$v"; break; }
done

if ! command -v qemu-system-x86_64 >/dev/null 2>&1 || [ -z "$OVMF_CODE" ] || [ -z "$OVMF_VARS" ]; then
    nuntia 'OMISSUM: QEMU vel OVMF deest; probatio MSI saltatur.'
    exit 0
fi
if ! qemu-system-x86_64 -device help 2>&1 | grep -Eq 'name "edu"'; then
    defecit 'apparatus QEMU EDU deest' 1
fi

nuntia 'I. Probatio MSI in modo UEFI compilatur...'
( cd "$RADIX/systema" && "$RADIX/compilator_vindex" proba_interruptiones_msi.vindex \
    "$TEMPORARIUM/BOOTX64.EFI" uefi ) >"$TEMPORARIUM/comp.log" 2>&1 \
    || { sed -n '1,240p' "$TEMPORARIUM/comp.log" >&2; defecit 'compilatio' 1; }
file "$TEMPORARIUM/BOOTX64.EFI" | grep -q 'PE32+.*EFI application' \
    || defecit 'exsecutabile EFI invalidum' 1
nuntia '   RECTE: exsecutabile EFI generatum.'

mkdir -p "$TEMPORARIUM/esp/EFI/BOOT"
cp -f "$TEMPORARIUM/BOOTX64.EFI" "$TEMPORARIUM/esp/EFI/BOOT/BOOTX64.EFI"
cp -f "$OVMF_VARS" "$TEMPORARIUM/vars.fd"
chmod +w "$TEMPORARIUM/vars.fd"

nuntia 'II. EDU post pontem PCIe MSI ad tractatorem VINDEX mittit...'
qemu-system-x86_64 -m 1024 -smp 1 -M q35 \
    -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
    -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/vars.fd" \
    -drive "format=raw,file=fat:rw:$TEMPORARIUM/esp" \
    -device pcie-root-port,id=rp0,bus=pcie.0,chassis=1 \
    -device edu,bus=rp0 -nographic -net none -monitor none \
    >"$TEMPORARIUM/msi.log" 2>&1 &
QEMU_PID="$!"
FINIS="$((SECONDS + 90))"
while kill -0 "$QEMU_PID" 2>/dev/null && [ "$SECONDS" -lt "$FINIS" ]; do
    if strings "$TEMPORARIUM/msi.log" | grep -E '^MSI 1234:11E8 ' >/dev/null; then
        break
    fi
    sleep 1
done
if kill -0 "$QEMU_PID" 2>/dev/null; then
    kill "$QEMU_PID" 2>/dev/null || true
fi
wait "$QEMU_PID" 2>/dev/null || true
QEMU_PID=""

strings "$TEMPORARIUM/msi.log" | grep -E '^MSI 1234:11E8 ' >"$TEMPORARIUM/msi.txt" || true
[ -s "$TEMPORARIUM/msi.txt" ] || {
    tail -80 "$TEMPORARIUM/msi.log" >&2
    defecit 'tractator MSI nullam probationem reddidit' 2
}
LINEA="$(head -1 "$TEMPORARIUM/msi.txt")"
read -r TITULUS APPARATUS VECTOR NUMERUS CAUSA PENDENS RESTA <<<"$LINEA"

[ "$TITULUS" = "MSI" ] && [ "$APPARATUS" = "1234:11E8" ] \
    || defecit "apparatus invalidus: $LINEA" 3
[ "$VECTOR" = "V00F1" ] || defecit "vector invalidus: $VECTOR" 3
[ "$NUMERUS" = "C00000001" ] || defecit "numerus IRQ invalidus: $NUMERUS" 4
[ "$CAUSA" = "S00000040" ] || defecit "causa EDU invalida: $CAUSA" 4
[ "$PENDENS" = "P00000000" ] || defecit "IRQ EDU non agnita: $PENDENS" 4
[ "$RESTA" = "R" ] || defecit 'IDT, MSI vel PCI non restituta sunt' 5

nuntia '   RECTE: vector 0xF1 per MSI semel receptus et causa 0x40 agnita.'
nuntia '   RECTE: porta IDT, capacitas MSI et commandum PCI restituta.'
nuntia ''
nuntia '=== INTERRUPTIO MSI VERA PROBATA ==='
sed 's/^/   /' "$TEMPORARIUM/msi.txt"
