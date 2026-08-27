#!/usr/bin/env bash
# Fenestrale II Purus per ponticulum UEFI VINDEX purum et PS/2 nativum probat.
set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
UEFI="$RADIX/systema/uefi"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-fenestrale-uefi.XXXXXX")"
MORA_INITII="${MORA_INITII:-28}"
PROBATOR_FENESTRALIS="${PROBATOR_FENESTRALIS:-$RADIX/instrumenta/proba_fenestrale_uefi_purum.py}"
SERVA_CAPTURAS="${SERVA_CAPTURAS:-}"

serva_et_purga() {
    if [ -n "$SERVA_CAPTURAS" ]; then
        mkdir -p "$SERVA_CAPTURAS" 2>/dev/null || true
        cp -f "$TEMPORARIUM"/*.ppm "$SERVA_CAPTURAS"/ 2>/dev/null || true
    fi
    rm -rf "$TEMPORARIUM" 2>/dev/null || true
}
trap serva_et_purga EXIT HUP INT TERM

OVMF_CODE=""
for via in /usr/share/OVMF/OVMF_CODE_4M.fd /usr/share/OVMF/OVMF_CODE.fd /usr/share/ovmf/OVMF.fd /usr/share/qemu/OVMF.fd; do
    if [ -f "$via" ]; then OVMF_CODE="$via"; break; fi
done
OVMF_VARS=""
for via in /usr/share/OVMF/OVMF_VARS_4M.fd /usr/share/OVMF/OVMF_VARS.fd; do
    if [ -f "$via" ]; then OVMF_VARS="$via"; break; fi
done
if ! command -v qemu-system-x86_64 >/dev/null 2>&1 || [ -z "$OVMF_CODE" ] || [ -z "$OVMF_VARS" ]; then
    printf '%s\n' 'OMISSUM: QEMU/OVMF deest; probatio Fenestralis UEFI saltatur.'
    exit 0
fi

printf '%s\n' 'I. Fenestrale II Purus ut NUCLEUS.BIN construe...'
NUCLEUS_FONS="$RADIX/systema/fenestrale_ii_purus_i.vindex" \
    bash "$UEFI/construe_uefi_purum.sh" "$TEMPORARIUM/systema.img" "$TEMPORARIUM/BOOTX64.EFI" \
    >"$TEMPORARIUM/constructio.log" 2>&1 || {
        cat "$TEMPORARIUM/constructio.log" >&2
        exit 1
    }
grep -qa 'NUCLEUS BIN' "$TEMPORARIUM/systema.img" || {
    printf '%s\n' 'DEFECIT: Fenestrale NUCLEUS.BIN in imagine deest.' >&2
    exit 2
}
printf '%s\n' '   RECTE: Fenestrale II Purus in imagine UEFI inclusum.'

cp -f "$OVMF_VARS" "$TEMPORARIUM/OVMF_VARS.fd"
chmod +w "$TEMPORARIUM/OVMF_VARS.fd"
MONITOR="$TEMPORARIUM/monitor.sock"
QMP="$TEMPORARIUM/qmp.sock"

printf '%s\n' 'II. Fenestrale II + PS/2 sub QEMU/OVMF exerce...'
qemu-system-x86_64 -machine q35 -m 256 -vga std \
    -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
    -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/OVMF_VARS.fd" \
    -drive "if=ide,format=raw,file=$TEMPORARIUM/systema.img" \
    -display none \
    -monitor "unix:$MONITOR,server=on,wait=off" \
    -qmp "unix:$QMP,server=on,wait=off" \
    -net none >"$TEMPORARIUM/qemu.log" 2>&1 &
PID=$!

if ! python3 "$PROBATOR_FENESTRALIS" "$MONITOR" "$QMP" "$TEMPORARIUM" "$MORA_INITII"; then
    kill "$PID" 2>/dev/null || true
    wait "$PID" 2>/dev/null || true
    tail -60 "$TEMPORARIUM/qemu.log" >&2 || true
    exit 3
fi
wait "$PID" 2>/dev/null || true

printf '%s\n' '=== FENESTRALE II UEFI PURUM PROBATUM ==='
printf '%s\n' 'OVMF -> BOOTX64.EFI [VINDEX] -> FENESTRALE II [VINDEX] -> PS/2 [VINDEX] -> FRAMEBUFFER'
printf '%s\n' 'Nullum C in tota via.'
