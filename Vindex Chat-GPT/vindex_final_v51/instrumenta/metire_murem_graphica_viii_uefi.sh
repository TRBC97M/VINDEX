#!/usr/bin/env bash
# Graphica VIII: baseline responsivitatis muris PS/2 in catena UEFI canonica metitur.
set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
UEFI="$RADIX/systema/uefi"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-murus-gviii.XXXXXX")"

purga() {
    rm -rf "$TEMPORARIUM" 2>/dev/null || true
}
trap purga EXIT HUP INT TERM

OVMF_CODE=""
for via in /usr/share/OVMF/OVMF_CODE_4M.fd /usr/share/OVMF/OVMF_CODE.fd /usr/share/ovmf/OVMF.fd /usr/share/qemu/OVMF.fd; do
    if [ -f "$via" ]; then OVMF_CODE="$via"; break; fi
done
OVMF_VARS=""
for via in /usr/share/OVMF/OVMF_VARS_4M.fd /usr/share/OVMF/OVMF_VARS.fd; do
    if [ -f "$via" ]; then OVMF_VARS="$via"; break; fi
done
if ! command -v qemu-system-x86_64 >/dev/null 2>&1 || [ -z "$OVMF_CODE" ] || [ -z "$OVMF_VARS" ]; then
    printf '%s\n' 'OMISSUM: QEMU/OVMF deest; mensura PS/2 saltatur.'
    exit 0
fi

printf '%s\n' 'I. Sylviam canonicam pro baseline PS/2 construe...'
bash "$UEFI/construe_uefi_purum.sh" "$TEMPORARIUM/systema.img" "$TEMPORARIUM/BOOTX64.EFI" \
    >"$TEMPORARIUM/constructio.log" 2>&1 || {
        cat "$TEMPORARIUM/constructio.log" >&2
        exit 1
    }

cp -f "$OVMF_VARS" "$TEMPORARIUM/OVMF_VARS.fd"
chmod +w "$TEMPORARIUM/OVMF_VARS.fd"
MONITOR="$TEMPORARIUM/monitor.sock"
QMP="$TEMPORARIUM/qmp.sock"

printf '%s\n' 'II. OVMF/QEMU sine mora fixa accende; statum PS/2 activum exspecta...'
qemu-system-x86_64 -machine q35 -m 256 -vga std \
    -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
    -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/OVMF_VARS.fd" \
    -drive "if=ide,format=raw,file=$TEMPORARIUM/systema.img" \
    -display none \
    -monitor "unix:$MONITOR,server=on,wait=off" \
    -qmp "unix:$QMP,server=on,wait=off" \
    -net none >"$TEMPORARIUM/qemu.log" 2>&1 &
PID=$!

if ! python3 "$RADIX/instrumenta/metire_murem_graphica_viii.py" "$MONITOR" "$QMP"; then
    kill "$PID" 2>/dev/null || true
    wait "$PID" 2>/dev/null || true
    cat "$TEMPORARIUM/constructio.log" >&2 || true
    tail -80 "$TEMPORARIUM/qemu.log" >&2 || true
    exit 2
fi
wait "$PID" 2>/dev/null || true

printf '%s\n' '=== BASELINE PS/2 GRAPHICA VIII MENSURATUS ==='
printf '%s\n' 'QMP -> PS/2 QEMU -> rector VINDEX -> telemetria nuclei'
