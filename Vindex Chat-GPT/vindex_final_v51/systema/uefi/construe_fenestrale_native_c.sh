#!/usr/bin/env bash
# Sylvia OS — Fenestrale II, Gradus C.
# Window manager minimum UEFI cum mure et cursore composito construit.

set -eu

RADIX="$(cd "$(dirname "$0")/../.." && pwd)"
UEFI="$RADIX/systema/uefi"
APPLICATIO="${1:-$RADIX/FENESTRALEC.EFI}"
IMAGO="${2:-$RADIX/fenestrale_c_uefi.img}"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/sylvia-fenestrale-c.XXXXXX")"

purga() {
    if [ -d "$TEMPORARIUM" ]; then
        find "$TEMPORARIUM" -type f -delete
        rmdir "$TEMPORARIUM"
    fi
}
trap purga EXIT HUP INT TERM

for instrumentum in gcc ld objcopy file objdump python3; do
    if ! command -v "$instrumentum" >/dev/null 2>&1; then
        printf 'ERRATUM: instrumentum necessarium deest: %s\n' "$instrumentum" >&2
        exit 69
    fi
done

gcc -c -std=c11 -O2 -Wall -Wextra -Werror -ffreestanding -fno-builtin \
    -fno-stack-protector -fno-pie -fno-ident -m64 -mno-red-zone \
    -maccumulate-outgoing-args -fshort-wchar \
    "$UEFI/fenestrale_native_c.c" -o "$TEMPORARIUM/fenestrale_native_c.o"

objcopy --remove-section .comment --remove-section .note.GNU-stack \
    "$TEMPORARIUM/fenestrale_native_c.o"

ld -mi386pep --subsystem 10 --entry efi_main --image-base 0x14000000 \
    --no-insert-timestamp --stack 0x200000 \
    --section-alignment 4096 --file-alignment 512 \
    "$TEMPORARIUM/fenestrale_native_c.o" -o "$TEMPORARIUM/FENESTRALEC.EFI"

if ! file "$TEMPORARIUM/FENESTRALEC.EFI" | grep -q 'PE32+.*EFI'; then
    printf '%s\n' 'ERRATUM: applicatio UEFI PE32+ valida non est.' >&2
    exit 65
fi
if ! objdump -p "$TEMPORARIUM/FENESTRALEC.EFI" | grep -q 'Subsystem.*EFI application'; then
    printf '%s\n' 'ERRATUM: subsystema UEFI deest.' >&2
    exit 65
fi

python3 "$UEFI/fac_imaginem_uefi.py" \
    "$TEMPORARIUM/FENESTRALEC.EFI" "$TEMPORARIUM/fenestrale_c_uefi.img"

mkdir -p "$(dirname "$APPLICATIO")" "$(dirname "$IMAGO")"
cp -f "$TEMPORARIUM/FENESTRALEC.EFI" "$APPLICATIO"
cp -f "$TEMPORARIUM/fenestrale_c_uefi.img" "$IMAGO"
chmod 0644 "$APPLICATIO" "$IMAGO"
printf '%s\n' 'RECTE: probatio Fenestralis II Gradus C constructa est.'
printf 'APPLICATIO: %s\n' "$APPLICATIO"
printf 'IMAGO: %s\n' "$IMAGO"
