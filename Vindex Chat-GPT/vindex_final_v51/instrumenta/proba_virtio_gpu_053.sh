#!/usr/bin/env bash
# P12-V4: transportum VirtIO PCI et GET_DISPLAY_INFO sub QEMU probat.

set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-virtio-gpu.XXXXXX")"
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

nuntia 'I. Dispositio codae divisae nativa exercetur...'
( cd "$RADIX" && ./compilator_vindex probationes/virtio_pci.vindex "$TEMPORARIUM/virtio-pci" ) \
    >"$TEMPORARIUM/native-comp.log" 2>&1 \
    || { sed -n '1,240p' "$TEMPORARIUM/native-comp.log" >&2; defecit 'compilatio nativa' 1; }
chmod +x "$TEMPORARIUM/virtio-pci"
"$TEMPORARIUM/virtio-pci" || defecit 'coda divisa nativa' "$?"
nuntia '   RECTE: descriptoria, annuli, conversio indicum et termini DMA.'

OVMF_CODE=""
for v in /usr/share/OVMF/OVMF_CODE_4M.fd /usr/share/OVMF/OVMF_CODE.fd; do
    [ -f "$v" ] && { OVMF_CODE="$v"; break; }
done
OVMF_VARS=""
for v in /usr/share/OVMF/OVMF_VARS_4M.fd /usr/share/OVMF/OVMF_VARS.fd; do
    [ -f "$v" ] && { OVMF_VARS="$v"; break; }
done

if ! command -v qemu-system-x86_64 >/dev/null 2>&1 || [ -z "$OVMF_CODE" ] || [ -z "$OVMF_VARS" ]; then
    nuntia 'OMISSUM: QEMU vel OVMF deest; probatio VirtIO GPU sub firmware saltatur.'
    exit 0
fi
if ! qemu-system-x86_64 -device help 2>&1 | grep -Eq 'name "virtio-gpu-pci"'; then
    defecit 'apparatus QEMU virtio-gpu-pci deest' 1
fi

nuntia 'II. Probatio VirtIO GPU in modo UEFI compilatur...'
( cd "$RADIX/systema" && "$RADIX/compilator_vindex" proba_virtio_gpu.vindex \
    "$TEMPORARIUM/BOOTX64.EFI" uefi ) >"$TEMPORARIUM/comp.log" 2>&1 \
    || { sed -n '1,260p' "$TEMPORARIUM/comp.log" >&2; defecit 'compilatio UEFI' 1; }
file "$TEMPORARIUM/BOOTX64.EFI" | grep -q 'PE32+.*EFI application' \
    || defecit 'exsecutabile EFI invalidum' 1
nuntia '   RECTE: exsecutabile EFI generatum.'

mkdir -p "$TEMPORARIUM/esp/EFI/BOOT"
cp -f "$TEMPORARIUM/BOOTX64.EFI" "$TEMPORARIUM/esp/EFI/BOOT/BOOTX64.EFI"
cp -f "$OVMF_VARS" "$TEMPORARIUM/vars.fd"
chmod +w "$TEMPORARIUM/vars.fd"

nuntia 'III. VirtIO PCI modernus mandatum GET_DISPLAY_INFO consumit...'
qemu-system-x86_64 -m 1024 -smp 1 -M q35 \
    -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
    -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/vars.fd" \
    -drive "format=raw,file=fat:rw:$TEMPORARIUM/esp" \
    -device pcie-root-port,id=rp0,bus=pcie.0,chassis=1 \
    -device virtio-gpu-pci,disable-legacy=on,bus=rp0 \
    -vga none -nographic -net none -monitor none \
    >"$TEMPORARIUM/virtio.log" 2>&1 &
QEMU_PID="$!"
FINIS="$((SECONDS + 90))"
while kill -0 "$QEMU_PID" 2>/dev/null && [ "$SECONDS" -lt "$FINIS" ]; do
    if strings "$TEMPORARIUM/virtio.log" | grep -E '^VIO4 (1AF4:1050|ERR)' >/dev/null; then
        break
    fi
    sleep 1
done
if kill -0 "$QEMU_PID" 2>/dev/null; then
    kill "$QEMU_PID" 2>/dev/null || true
fi
wait "$QEMU_PID" 2>/dev/null || true
QEMU_PID=""

strings "$TEMPORARIUM/virtio.log" | grep -E '^VIO4 1AF4:1050 ' >"$TEMPORARIUM/virtio.txt" || true
[ -s "$TEMPORARIUM/virtio.txt" ] || {
    ERRATUM="$(strings "$TEMPORARIUM/virtio.log" | grep -E '^VIO4 ERR' | head -1 || true)"
    if [ -n "$ERRATUM" ]; then
        defecit "payload VINDEX rettulit: $ERRATUM" 2
    fi
    tail -100 "$TEMPORARIUM/virtio.log" >&2
    defecit 'transportus VirtIO nullam probationem reddidit' 2
}
LINEA="$(head -1 "$TEMPORARIUM/virtio.txt")"
read -r TITULUS IDENTITAS BUS APPARATUS FUNCTIO COMMUNIS NOTIFY OBLATA CODA ADHIBITA GENUS LATITUDO ALTITUDO ACTIVUS ISR RESTA <<<"$LINEA"

[ "$TITULUS" = "VIO4" ] && [ "$IDENTITAS" = "1AF4:1050" ] \
    || defecit "identitas invalida: $LINEA" 3
[ "$CODA" = "Q0008" ] || defecit "magnitudo codae invalida: $CODA" 3
[ "$ADHIBITA" = "U0001" ] || defecit "annulus adhibitus invalidus: $ADHIBITA" 4
[ "$GENUS" = "T00001101" ] || defecit "responsum GPU invalidum: $GENUS" 4
[ "$ACTIVUS" = "E00000001" ] || defecit "scanout non activus: $ACTIVUS" 4
[ "$RESTA" = "R" ] || defecit 'resetus VirtIO vel commandum PCI non restitutum est' 5

OBLATA_DEC="$((16#${OBLATA#O}))"
LATITUDO_DEC="$((16#${LATITUDO#W}))"
ALTITUDO_DEC="$((16#${ALTITUDO#H}))"
[ "$(( OBLATA_DEC & 1 ))" -ne 0 ] || defecit "VIRTIO_F_VERSION_1 deest: $OBLATA" 5
[ "$LATITUDO_DEC" -gt 0 ] && [ "$ALTITUDO_DEC" -gt 0 ] \
    || defecit "dimensio scanout invalida: $LATITUDO $ALTITUDO" 5

nuntia "   RECTE: ${BUS}/${APPARATUS}/${FUNCTIO}, BAR ${COMMUNIS}/${NOTIFY}, VERSION_1 oblata."
nuntia "   RECTE: coda VIII ingressuum reddidit scanout ${LATITUDO_DEC}x${ALTITUDO_DEC}."
nuntia '   RECTE: apparatus resetus, pagina DMA liberata et commandum PCI restitutum.'
nuntia ''
nuntia '=== TRANSPORTUS VIRTIO GPU PROBATUS ==='
sed 's/^/   /' "$TEMPORARIUM/virtio.txt"
