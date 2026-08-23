#!/usr/bin/env bash
# Sylvia OS — Fenestrale II, Gradus I.
# PROGRAMMATA H et TABULA I ut clientes VINDEX distinctos in compositorium includit.

set -eu
RADIX="$(cd "$(dirname "$0")/../.." && pwd)"
UEFI="$RADIX/systema/uefi"
EXITUS="${1:-$RADIX/FENESTRALEI.EFI}"
IMAGO="${2:-$RADIX/fenestrale_i_uefi.img}"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/sylvia-fenestrale-i.XXXXXX")"
purga(){ if [ -d "$TEMPORARIUM" ]; then find "$TEMPORARIUM" -type f -delete; rmdir "$TEMPORARIUM"; fi; }
trap purga EXIT HUP INT TERM

for instrumentum in gcc ld objcopy python3 file objdump readelf stat; do
    command -v "$instrumentum" >/dev/null 2>&1 || { printf 'ERRATUM: deest %s\n' "$instrumentum" >&2; exit 69; }
done
[ -x "$RADIX/compilator_vindex" ] || { printf '%s\n' 'ERRATUM: compilator_vindex deest.' >&2; exit 66; }

compila_clientem(){
    fons="$1"; nomen="$2"
    python3 "$RADIX/instrumenta/vindex_verifica.py" "$fons"
    "$RADIX/compilator_vindex" "$fons" "$TEMPORARIUM/$nomen.elf"
    readelf -h "$TEMPORARIUM/$nomen.elf" | grep -q 'Class:.*ELF64'
    python3 - "$TEMPORARIUM/$nomen.elf" <<'PY'
from pathlib import Path
import struct, sys
data=Path(sys.argv[1]).read_bytes()
if data[:4] != b'\x7fELF' or len(data) < 32:
    raise SystemExit('ERRATUM: ELF invalidum.')
e=struct.unpack_from('<Q',data,24)[0]
if not (0x00400000 <= e < 0x00400000 + len(data)):
    raise SystemExit(f'ERRATUM: ingressus 0x{e:x} extra imaginem raw est.')
print(f'RECTE: {Path(sys.argv[1]).name} ingressus 0x{e:x}.')
PY
    (cd "$TEMPORARIUM" && objcopy -I binary -O pe-x86-64 -B i386:x86-64 "$nomen.elf" "$nomen.o")
}

compila_clientem "$RADIX/src/programmata_fenestrale_ii_h.vindex" programmata_h
compila_clientem "$RADIX/src/tabula_fenestrale_ii_i.vindex" tabula_i

gcc -c -std=c11 -O2 -Wall -Wextra -Werror -Wno-error=misleading-indentation \
    -ffreestanding -fno-builtin -fno-stack-protector -fno-pie -fno-ident \
    -m64 -mno-red-zone -maccumulate-outgoing-args -fshort-wchar \
    -I "$RADIX/systema" "$UEFI/fenestrale_native_i.c" \
    -o "$TEMPORARIUM/fenestrale_native_i.o"
objcopy --remove-section .comment --remove-section .note.GNU-stack "$TEMPORARIUM/fenestrale_native_i.o"

ld -mi386pep --subsystem 10 --entry efi_main --image-base 0x15000000 \
    --no-insert-timestamp --stack 0x200000 --section-alignment 4096 --file-alignment 512 \
    "$TEMPORARIUM/fenestrale_native_i.o" "$TEMPORARIUM/programmata_h.o" "$TEMPORARIUM/tabula_i.o" \
    -o "$TEMPORARIUM/FENESTRALEI.EFI"

file "$TEMPORARIUM/FENESTRALEI.EFI" | grep -q 'PE32+.*EFI'
objdump -p "$TEMPORARIUM/FENESTRALEI.EFI" | grep -q 'Subsystem.*EFI application'
python3 "$UEFI/fac_imaginem_uefi.py" "$TEMPORARIUM/FENESTRALEI.EFI" "$TEMPORARIUM/fenestrale_i_uefi.img"
mkdir -p "$(dirname "$EXITUS")" "$(dirname "$IMAGO")"
cp -f "$TEMPORARIUM/FENESTRALEI.EFI" "$EXITUS"
cp -f "$TEMPORARIUM/fenestrale_i_uefi.img" "$IMAGO"
chmod 0644 "$EXITUS" "$IMAGO"
printf '%s\n' 'RECTE: Fenestrale II Gradus I constructum est.'
printf 'APPLICATIO: %s\nIMAGO: %s\n' "$EXITUS" "$IMAGO"
