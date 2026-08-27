#!/usr/bin/env bash
# P19-I: idem discum duobus initii QEMU exercet.
# Primum initium P19TEST.TXT creat et flush facit; secundum idem contentum
# ex disco iam persistente invenire debet.
set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
UEFI="$RADIX/systema/uefi"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-p19-i.XXXXXX")"
MORA="${MORA_P19:-45}"
trap 'rm -rf "$TEMPORARIUM" 2>/dev/null || true' EXIT HUP INT TERM

OVMF_CODE=""
for via in /usr/share/OVMF/OVMF_CODE_4M.fd /usr/share/OVMF/OVMF_CODE.fd /usr/share/ovmf/OVMF.fd /usr/share/qemu/OVMF.fd; do
    if [ -f "$via" ]; then OVMF_CODE="$via"; break; fi
done
OVMF_VARS=""
for via in /usr/share/OVMF/OVMF_VARS_4M.fd /usr/share/OVMF/OVMF_VARS.fd; do
    if [ -f "$via" ]; then OVMF_VARS="$via"; break; fi
done
if ! command -v qemu-system-x86_64 >/dev/null 2>&1 || [ -z "$OVMF_CODE" ] || [ -z "$OVMF_VARS" ]; then
    printf '%s\n' 'OMISSUM: QEMU/OVMF deest; P19-I persistentia non exercetur.'
    exit 0
fi

printf '%s\n' 'I. Imaginem P19-I cum nucleo VINDEX construe...'
NUCLEUS_FONS="$RADIX/systema/proba_fasciculos_sylviae_i.vindex" \
    bash "$UEFI/construe_uefi_purum.sh" "$TEMPORARIUM/systema.img" "$TEMPORARIUM/BOOTX64.EFI" \
    >"$TEMPORARIUM/constructio.log" 2>&1 || {
        cat "$TEMPORARIUM/constructio.log" >&2
        exit 1
    }

if grep -qa 'SYLVIA PERSISTET' "$TEMPORARIUM/systema.img"; then
    printf '%s\n' 'DEFECIT: datum probationis iam ante primum initium in imagine adest.' >&2
    exit 2
fi

boot() {
    local numerus="$1"
    local exspectatum="$2"
    local monitor="$TEMPORARIUM/monitor-${numerus}.sock"
    local vars="$TEMPORARIUM/OVMF_VARS-${numerus}.fd"
    cp -f "$OVMF_VARS" "$vars"
    chmod +w "$vars"

    qemu-system-x86_64 -machine q35 -m 256 -vga std \
        -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
        -drive "if=pflash,format=raw,unit=1,file=$vars" \
        -drive "if=ide,format=raw,file=$TEMPORARIUM/systema.img" \
        -display none \
        -monitor "unix:$monitor,server=on,wait=off" \
        -net none >"$TEMPORARIUM/qemu-${numerus}.log" 2>&1 &
    local pid=$!

    if ! python3 "$RADIX/instrumenta/proba_fasciculos_persistentes_i.py" "$monitor" "$exspectatum" "$MORA"; then
        kill "$pid" 2>/dev/null || true
        wait "$pid" 2>/dev/null || true
        tail -80 "$TEMPORARIUM/qemu-${numerus}.log" >&2 || true
        return 1
    fi
    wait "$pid" 2>/dev/null || true
}

printf '%s\n' 'II. Primum initium: fasciculum crea, scribe, flush et relege...'
boot 1 1
if ! grep -qa 'SYLVIA PERSISTET' "$TEMPORARIUM/systema.img"; then
    printf '%s\n' 'DEFECIT: datum scriptum post primum initium in imagine non persistit.' >&2
    exit 3
fi
printf '%s\n' '   RECTE: primum initium datum in disco reliquit.'

printf '%s\n' 'III. Secundum initium eiusdem imaginis: datum vetus relege...'
boot 2 2
printf '%s\n' '   RECTE: secundum initium fasciculum a primo initio servatum legit.'

printf '%s\n' '=== P19-I PERSISTENTIA DUORUM INITIORUM PROBATA ==='
printf '%s\n' 'OVMF -> Sylvia [VINDEX] -> SimpleFileSystem UEFI -> fasciculus -> restart -> relectio'
printf '%s\n' 'Nulla copia memoriae inter initia transfertur.'
