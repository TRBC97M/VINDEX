#!/usr/bin/env bash
# Sylvia OS — Fenestrale II, Gradus H.
# Compositorium UEFI separatum cum cliente PROGRAMMATA VINDEX construit.

set -eu

RADIX="$(cd "$(dirname "$0")/../.." && pwd)"
UEFI="$RADIX/systema/uefi"
EXITUS="${1:-$RADIX/FENESTRALEH.EFI}"
IMAGO="${2:-$RADIX/fenestrale_h_uefi.img}"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/sylvia-fenestrale-h.XXXXXX")"

purga() {
    if [ -d "$TEMPORARIUM" ]; then
        find "$TEMPORARIUM" -type f -delete
        rmdir "$TEMPORARIUM"
    fi
}
trap purga EXIT HUP INT TERM

for instrumentum in gcc ld objcopy python3 file objdump readelf stat; do
    if ! command -v "$instrumentum" >/dev/null 2>&1; then
        printf 'ERRATUM: instrumentum necessarium deest: %s\n' "$instrumentum" >&2
        exit 69
    fi
done

if [ ! -x "$RADIX/compilator_vindex" ]; then
    printf '%s\n' 'ERRATUM: compilator_vindex deest aut non exsecutabilis est.' >&2
    exit 66
fi

# Gradus G contractum bibliothecarum definit. Gradus H clientem compactum
# eodem mailbox utentem habet, quia compilator 0.51 unitatem G amplam nondum
# robuste generat. Compilatorem canonicum hoc experimentum non mutat.
python3 "$RADIX/instrumenta/vindex_verifica.py" \
    "$RADIX/src/programmata_fenestrale_ii_h.vindex"

"$RADIX/compilator_vindex" \
    "$RADIX/src/programmata_fenestrale_ii_h.vindex" \
    "$TEMPORARIUM/programmata_g.elf"

if ! readelf -h "$TEMPORARIUM/programmata_g.elf" | grep -q 'Class:.*ELF64'; then
    printf '%s\n' 'ERRATUM: client PROGRAMMATA ELF64 non est.' >&2
    exit 65
fi

python3 - "$TEMPORARIUM/programmata_g.elf" <<'PY'
from pathlib import Path
import struct
import sys
p = Path(sys.argv[1])
data = p.read_bytes()
if data[:4] != b'\x7fELF' or len(data) < 32:
    raise SystemExit('ERRATUM: ELF clientis invalidum.')
entry = struct.unpack_from('<Q', data, 24)[0]
base = 0x00400000
if not (base <= entry < base + len(data)):
    raise SystemExit(f'ERRATUM: ingressus clientis 0x{entry:x} extra imaginem raw est.')
print(f'RECTE: ingressus PROGRAMMATA = 0x{entry:x}.')
PY

(
    cd "$TEMPORARIUM"
    objcopy -I binary -O pe-x86-64 -B i386:x86-64 \
        programmata_g.elf programmata_g.o
)

gcc -c -std=c11 -O2 -Wall -Wextra -Werror -Wno-error=misleading-indentation \
    -ffreestanding -fno-builtin -fno-stack-protector -fno-pie -fno-ident \
    -m64 -mno-red-zone -maccumulate-outgoing-args -fshort-wchar \
    -I "$RADIX/systema" \
    "$UEFI/fenestrale_native_h.c" -o "$TEMPORARIUM/fenestrale_native_h.o"

objcopy --remove-section .comment --remove-section .note.GNU-stack \
    "$TEMPORARIUM/fenestrale_native_h.o"

ld -mi386pep --subsystem 10 --entry efi_main --image-base 0x14000000 \
    --no-insert-timestamp --stack 0x200000 \
    --section-alignment 4096 --file-alignment 512 \
    "$TEMPORARIUM/fenestrale_native_h.o" "$TEMPORARIUM/programmata_g.o" \
    -o "$TEMPORARIUM/FENESTRALEH.EFI"

if ! file "$TEMPORARIUM/FENESTRALEH.EFI" | grep -q 'PE32+.*EFI'; then
    printf '%s\n' 'ERRATUM: applicatio UEFI PE32+ valida non est.' >&2
    exit 65
fi
if ! objdump -p "$TEMPORARIUM/FENESTRALEH.EFI" | grep -q 'Subsystem.*EFI application'; then
    printf '%s\n' 'ERRATUM: subsystema UEFI deest.' >&2
    exit 65
fi

python3 "$UEFI/fac_imaginem_uefi.py" \
    "$TEMPORARIUM/FENESTRALEH.EFI" "$TEMPORARIUM/fenestrale_h_uefi.img"

mkdir -p "$(dirname "$EXITUS")" "$(dirname "$IMAGO")"
cp -f "$TEMPORARIUM/FENESTRALEH.EFI" "$EXITUS"
cp -f "$TEMPORARIUM/fenestrale_h_uefi.img" "$IMAGO"
chmod 0644 "$EXITUS" "$IMAGO"
printf '%s\n' 'RECTE: Fenestrale II Gradus H constructum est.'
printf 'APPLICATIO: %s\n' "$EXITUS"
printf 'IMAGO: %s\n' "$IMAGO"
