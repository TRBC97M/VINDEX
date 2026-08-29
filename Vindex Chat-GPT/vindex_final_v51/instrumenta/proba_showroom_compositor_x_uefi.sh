#!/usr/bin/env bash
# P16-XII-B: scena Graphica X sub QEMU/OVMF probatur.
set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
UEFI="$RADIX/systema/uefi"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-compositor-x.XXXXXX")"
MORA_INITII="${MORA_INITII:-18}"
SERVA_CAPTURAS="${SERVA_CAPTURAS:-}"

purga() {
    if [ -n "$SERVA_CAPTURAS" ]; then
        mkdir -p "$SERVA_CAPTURAS" 2>/dev/null || true
        cp -f "$TEMPORARIUM"/*.ppm "$SERVA_CAPTURAS"/ 2>/dev/null || true
        cp -f "$TEMPORARIUM"/*.log "$SERVA_CAPTURAS"/ 2>/dev/null || true
    fi
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
    printf '%s\n' 'OMISSUM: QEMU/OVMF deest; showroom Compositor X saltatur.'
    exit 0
fi

printf '%s\n' 'I. Showroom scenae Graphica X ut NUCLEUS.BIN construe...'
NUCLEUS_FONS="$RADIX/systema/showroom_compositor_x_uefi.vindex" \
    bash "$UEFI/construe_uefi_purum.sh" "$TEMPORARIUM/systema.img" "$TEMPORARIUM/BOOTX64.EFI" \
    >"$TEMPORARIUM/constructio.log" 2>&1 || {
        cat "$TEMPORARIUM/constructio.log" >&2
        exit 1
    }

grep -qa 'NUCLEUS BIN' "$TEMPORARIUM/systema.img" || {
    printf '%s\n' 'DEFECIT: showroom Compositor X in imagine deest.' >&2
    exit 2
}

cp -f "$OVMF_VARS" "$TEMPORARIUM/OVMF_VARS.fd"
chmod +w "$TEMPORARIUM/OVMF_VARS.fd"
MONITOR="$TEMPORARIUM/monitor.sock"

printf '%s\n' 'II. Scena compositoris sub QEMU/OVMF exerce...'
qemu-system-x86_64 -machine q35 -m 256 -vga std \
    -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
    -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/OVMF_VARS.fd" \
    -drive "if=ide,format=raw,file=$TEMPORARIUM/systema.img" \
    -display none \
    -monitor "unix:$MONITOR,server=on,wait=off" \
    -net none >"$TEMPORARIUM/qemu.log" 2>&1 &
PID=$!

if ! python3 "$RADIX/instrumenta/proba_showroom_compositor_x.py" "$MONITOR" "$TEMPORARIUM" "$MORA_INITII"; then
    kill "$PID" 2>/dev/null || true
    wait "$PID" 2>/dev/null || true
    cat "$TEMPORARIUM/constructio.log" >&2 || true
    tail -80 "$TEMPORARIUM/qemu.log" >&2 || true
    exit 3
fi
wait "$PID" 2>/dev/null || true

printf '%s\n' '=== COMPOSITOR X UEFI PROBATUS ==='
printf '%s\n' 'OVMF -> VINDEX -> scena GX -> backbuffer -> damage-only -> framebuffer'
