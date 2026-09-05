#!/usr/bin/env bash
# P12-V2: paginas DMA physicas, limitem 32-bitorum et cache sub QEMU probat.

set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-paginae-dma.XXXXXX")"
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
    nuntia 'OMISSUM: QEMU vel OVMF deest; probatio paginarum DMA saltatur.'
    exit 0
fi

nuntia 'I. Probatio paginarum DMA in modo UEFI compilatur...'
( cd "$RADIX/systema" && "$RADIX/compilator_vindex" proba_paginae_dma.vindex \
    "$TEMPORARIUM/BOOTX64.EFI" uefi ) >"$TEMPORARIUM/comp.log" 2>&1 \
    || { sed -n '1,200p' "$TEMPORARIUM/comp.log" >&2; defecit 'compilatio' 1; }
file "$TEMPORARIUM/BOOTX64.EFI" | grep -q 'PE32+.*EFI application' \
    || defecit 'exsecutabile EFI invalidum' 1
nuntia '   RECTE: exsecutabile EFI generatum.'

mkdir -p "$TEMPORARIUM/esp/EFI/BOOT"
cp -f "$TEMPORARIUM/BOOTX64.EFI" "$TEMPORARIUM/esp/EFI/BOOT/BOOTX64.EFI"
cp -f "$OVMF_VARS" "$TEMPORARIUM/vars.fd"
chmod +w "$TEMPORARIUM/vars.fd"

nuntia 'II. AllocatePages, cache et FreePages sub OVMF exercentur...'
qemu-system-x86_64 -m 2048 -M q35 \
    -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
    -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/vars.fd" \
    -drive "format=raw,file=fat:rw:$TEMPORARIUM/esp" \
    -nographic -net none >"$TEMPORARIUM/dma.log" 2>&1 &
QEMU_PID="$!"
FINIS="$((SECONDS + 90))"
while kill -0 "$QEMU_PID" 2>/dev/null && [ "$SECONDS" -lt "$FINIS" ]; do
    if strings "$TEMPORARIUM/dma.log" | grep -E '^DMA2 ' >/dev/null; then
        break
    fi
    sleep 1
done
if kill -0 "$QEMU_PID" 2>/dev/null; then
    kill "$QEMU_PID" 2>/dev/null || true
fi
wait "$QEMU_PID" 2>/dev/null || true
QEMU_PID=""

strings "$TEMPORARIUM/dma.log" | grep -E '^DMA2 ' >"$TEMPORARIUM/dma.txt" || true
[ -s "$TEMPORARIUM/dma.txt" ] || {
    tail -60 "$TEMPORARIUM/dma.log" >&2
    defecit 'probatio firmware nullam probationem DMA reddidit' 2
}
LINEA="$(head -1 "$TEMPORARIUM/dma.txt")"
read -r TITULUS BASIS PAGINAE MENSURA CACHE OBSERVATA PURGATA SYNC LIBERATA RESTA <<<"$LINEA"

[ "$TITULUS" = "DMA2" ] || defecit 'titulus DMA invalidus' 3
[ "$PAGINAE" = "0003" ] || defecit "numerus paginarum invalidus: $PAGINAE" 3
[ "$MENSURA" = "0000000000003000" ] || defecit "mensura attributa invalida: $MENSURA" 3
[ "$OBSERVATA" = "O" ] || defecit 'attributa cache non observata sunt' 4
[ "$PURGATA" = "Z" ] || defecit 'paginae non purgatae sunt' 4
[ "$SYNC" = "0002" ] || defecit "numerus synchronizationum invalidus: $SYNC" 4
[ "$LIBERATA" = "F" ] || defecit 'paginae non liberatae sunt' 4

BASIS_DEC="$((16#${BASIS}))"
CACHE_DEC="$((16#${CACHE}))"
[ "$(( BASIS_DEC & 4095 ))" -eq 0 ] || defecit "basis non est pagina: $BASIS" 5
[ "$BASIS_DEC" -gt 0 ] && [ "$(( BASIS_DEC + 12287 ))" -le 4294967295 ] \
    || defecit "regio DMA limitem 32-bitorum excedit: $BASIS" 5
[ "$(( CACHE_DEC & 8 ))" -ne 0 ] || defecit "cache WB non observata est: $CACHE" 5

nuntia "   RECTE: tres paginae physicae ad 0x$BASIS infra 4 Gio possessae."
nuntia "   RECTE: attributa cache UEFI observata 0x$CACHE (WB)."
nuntia '   RECTE: memoria purgata, bis synchronizata et per FreePages liberata.'
nuntia ''
nuntia '=== PAGINAE DMA PROBATAE ==='
sed 's/^/   /' "$TEMPORARIUM/dma.txt"
