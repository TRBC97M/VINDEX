#!/usr/bin/env bash
# P12-V1: regionem MMIO e BAR et lectionem e1000e sub QEMU comprobat.

set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-pci-mmio.XXXXXX")"
trap 'rm -rf "$TEMPORARIUM" 2>/dev/null || true' EXIT HUP INT TERM

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
    nuntia 'OMISSUM: QEMU vel OVMF deest; probatio MMIO saltatur.'
    exit 0
fi

nuntia 'I. Probatio MMIO in modo UEFI compilatur...'
( cd "$RADIX/systema" && "$RADIX/compilator_vindex" proba_pci_mmio.vindex \
    "$TEMPORARIUM/BOOTX64.EFI" uefi ) >"$TEMPORARIUM/comp.log" 2>&1 \
    || { cat "$TEMPORARIUM/comp.log" >&2; defecit 'compilatio' 1; }
file "$TEMPORARIUM/BOOTX64.EFI" | grep -q 'PE32+.*EFI application' \
    || defecit 'exsecutabile EFI invalidum' 1
nuntia '   RECTE: exsecutabile EFI generatum.'

mkdir -p "$TEMPORARIUM/esp/EFI/BOOT"
cp -f "$TEMPORARIUM/BOOTX64.EFI" "$TEMPORARIUM/esp/EFI/BOOT/BOOTX64.EFI"
cp -f "$OVMF_VARS" "$TEMPORARIUM/vars.fd"
chmod +w "$TEMPORARIUM/vars.fd"

nuntia 'II. e1000e post pontem PCIe et regio MMIO...'
timeout 90 qemu-system-x86_64 -m 2048 -M q35 \
    -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
    -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/vars.fd" \
    -drive "format=raw,file=fat:rw:$TEMPORARIUM/esp" \
    -device pcie-root-port,id=rp0,bus=pcie.0,chassis=1 \
    -device e1000e,bus=rp0 -nographic -net none \
    >"$TEMPORARIUM/mmio.log" 2>&1 || true

strings "$TEMPORARIUM/mmio.log" | grep -E '^8086:10D3 M ' >"$TEMPORARIUM/mmio.txt" || true
[ -s "$TEMPORARIUM/mmio.txt" ] || {
    tail -40 "$TEMPORARIUM/mmio.log" >&2
    defecit 'lectio MMIO e1000e nihil reddidit' 2
}
LINEA="$(head -1 "$TEMPORARIUM/mmio.txt")"
read -r _ _ BASIS MENSURA STATUS1 STATUS2 RESTA <<<"$LINEA"

[ "$BASIS" != "0000000000000000" ] || defecit 'basis MMIO nulla' 3
MENS_DEC="$((16#${MENSURA}))"
[ "$MENS_DEC" -ge 131072 ] || defecit "regio e1000e nimis parva: $MENSURA" 3
[ "$(( MENS_DEC & (MENS_DEC-1) ))" -eq 0 ] || defecit "mensura non potentia duorum: $MENSURA" 3
nuntia "   RECTE: regio MMIO ad 0x$BASIS, mensura 0x$MENSURA."

[ "$STATUS1" != "FFFFFFFF" ] && [ "$STATUS2" != "FFFFFFFF" ] \
    || defecit 'registrum STATUS valorem bus vacui reddit' 4
[ "$RESTA" = "R" ] || defecit 'contractus regionis MMIO invalidus' 4
nuntia "   RECTE: STATUS e1000e bis lectus: 0x$STATUS1 / 0x$STATUS2."
nuntia '   RECTE: regio est identitatis, apparatus et sola lectio.'

nuntia ''
nuntia '=== MAPPATIO MMIO TYPATA PROBATA ==='
sed 's/^/   /' "$TEMPORARIUM/mmio.txt"
