#!/usr/bin/env bash
# P16-XI-A: asseta premium PNG -> SIMG II -> FAT -> Graphica IX sub QEMU/OVMF.
set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
UEFI="$RADIX/systema/uefi"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-asseta-premium-i.XXXXXX")"
MORA_INITII="${MORA_INITII:-22}"
SERVA_CAPTURAS="${SERVA_CAPTURAS:-}"

purga() {
    if [ -n "$SERVA_CAPTURAS" ]; then
        mkdir -p "$SERVA_CAPTURAS" 2>/dev/null || true
        cp -f "$TEMPORARIUM"/*.ppm "$SERVA_CAPTURAS"/ 2>/dev/null || true
        cp -f "$TEMPORARIUM"/*.json "$SERVA_CAPTURAS"/ 2>/dev/null || true
        cp -f "$TEMPORARIUM"/constructio.log "$SERVA_CAPTURAS"/ 2>/dev/null || true
        cp -f "$TEMPORARIUM"/qemu.log "$SERVA_CAPTURAS"/ 2>/dev/null || true
        cp -f "$TEMPORARIUM"/generatio.log "$SERVA_CAPTURAS"/ 2>/dev/null || true
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
    printf '%s\n' 'OMISSUM: QEMU/OVMF deest; showroom Assetorum Premium I saltatur.'
    exit 0
fi

printf '%s\n' 'I. XII fontes PNG in SIMG II generantur...'
python3 "$RADIX/instrumenta/genera_asseta_premium_i.py" --destinatio "$TEMPORARIUM/simg" >"$TEMPORARIUM/generatio.log"
[ "$(find "$TEMPORARIUM/simg" -type f -name '*.simg' | wc -l)" -eq 12 ] || {
    printf '%s\n' 'DEFECIT: XII SIMG II non generata sunt.' >&2
    exit 1
}

printf '%s\n' 'II. Showroom P16-XI-A ut NUCLEUS.BIN construe...'
NUCLEUS_FONS="$RADIX/systema/showroom_asseta_premium_i_uefi.vindex" \
    bash "$UEFI/construe_uefi_purum.sh" "$TEMPORARIUM/systema.img" "$TEMPORARIUM/BOOTX64.EFI" \
    >"$TEMPORARIUM/constructio.log" 2>&1 || {
        cat "$TEMPORARIUM/constructio.log" >&2
        exit 2
    }

grep -qa 'NUCLEUS BIN' "$TEMPORARIUM/systema.img" || {
    printf '%s\n' 'DEFECIT: showroom NUCLEUS.BIN in imagine deest.' >&2
    exit 3
}

printf '%s\n' 'III. Derivata SIMG II realia in FAT inseruntur...'
python3 "$RADIX/instrumenta/adde_fasciculos_fat.py" "$TEMPORARIUM/systema.img" \
    "$TEMPORARIUM/simg/programmata@1x.simg=PRG1.SMG" \
    "$TEMPORARIUM/simg/programmata@1_5x.simg=PRG15.SMG" \
    "$TEMPORARIUM/simg/programmata@2x.simg=PRG2.SMG" \
    "$TEMPORARIUM/simg/tabula@2x.simg=TAB2.SMG" \
    "$TEMPORARIUM/simg/terminale@2x.simg=TRM2.SMG" \
    "$TEMPORARIUM/simg/officina@2x.simg=OFF2.SMG"
for signum in 'PRG1' 'PRG15' 'PRG2' 'TAB2' 'TRM2' 'OFF2'; do
    grep -qa "$signum" "$TEMPORARIUM/systema.img" || {
        printf 'DEFECIT: %s in imagine FAT deest.\n' "$signum" >&2
        exit 4
    }
done

cp -f "$OVMF_VARS" "$TEMPORARIUM/OVMF_VARS.fd"
chmod +w "$TEMPORARIUM/OVMF_VARS.fd"
MONITOR="$TEMPORARIUM/monitor.sock"

printf '%s\n' 'IV. Asseta Premium I sub QEMU/OVMF exerce...'
qemu-system-x86_64 -machine q35 -m 256 -vga std \
    -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
    -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/OVMF_VARS.fd" \
    -drive "if=ide,format=raw,file=$TEMPORARIUM/systema.img" \
    -display none \
    -monitor "unix:$MONITOR,server=on,wait=off" \
    -net none >"$TEMPORARIUM/qemu.log" 2>&1 &
PID=$!

if ! python3 "$RADIX/instrumenta/proba_showroom_asseta_premium_i.py" "$MONITOR" "$TEMPORARIUM" "$MORA_INITII"; then
    kill "$PID" 2>/dev/null || true
    wait "$PID" 2>/dev/null || true
    cat "$TEMPORARIUM/constructio.log" >&2 || true
    tail -80 "$TEMPORARIUM/qemu.log" >&2 || true
    exit 5
fi
wait "$PID" 2>/dev/null || true

printf '%s\n' '=== ASSETA PREMIUM I UEFI PROBATA ==='
printf '%s\n' 'PNG -> SIMG II -> FAT -> FS_* [VINDEX] -> Graphica IX -> framebuffer'
