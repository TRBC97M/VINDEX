#!/usr/bin/env bash
# Sylvia OS — Fenestrale II, Gradus A.
# Probationem UEFI resolutionis nativae construit sine nucleo 0.51 mutando.

set -eu

RADIX="$(cd "$(dirname "$0")/../.." && pwd)"
UEFI="$RADIX/systema/uefi"
EXITUS="${1:-$RADIX/FENESTRALEA.EFI}"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/sylvia-fenestrale-a.XXXXXX")"

purga() {
    if [ -d "$TEMPORARIUM" ]; then
        find "$TEMPORARIUM" -type f -delete
        rmdir "$TEMPORARIUM"
    fi
}
trap purga EXIT HUP INT TERM

for instrumentum in gcc ld objcopy file objdump; do
    if ! command -v "$instrumentum" >/dev/null 2>&1; then
        printf 'ERRATUM: instrumentum necessarium deest: %s\n' "$instrumentum" >&2
        exit 69
    fi
done

gcc -c -std=c11 -O2 -Wall -Wextra -Werror -ffreestanding -fno-builtin \
    -fno-stack-protector -fno-pie -fno-ident -m64 -mno-red-zone \
    -maccumulate-outgoing-args -fshort-wchar \
    "$UEFI/fenestrale_native_a.c" -o "$TEMPORARIUM/fenestrale_native_a.o"

objcopy --remove-section .comment --remove-section .note.GNU-stack \
    "$TEMPORARIUM/fenestrale_native_a.o"

ld -mi386pep --subsystem 10 --entry efi_main --image-base 0x12000000 \
    --no-insert-timestamp --stack 0x200000 \
    --section-alignment 4096 --file-alignment 512 \
    "$TEMPORARIUM/fenestrale_native_a.o" -o "$TEMPORARIUM/FENESTRALEA.EFI"

if ! file "$TEMPORARIUM/FENESTRALEA.EFI" | grep -q 'PE32+.*EFI'; then
    printf '%s\n' 'ERRATUM: applicatio UEFI PE32+ valida non est.' >&2
    exit 65
fi
if ! objdump -p "$TEMPORARIUM/FENESTRALEA.EFI" | grep -q 'Subsystem.*EFI application'; then
    printf '%s\n' 'ERRATUM: subsystema UEFI deest.' >&2
    exit 65
fi

mkdir -p "$(dirname "$EXITUS")"
cp -f "$TEMPORARIUM/FENESTRALEA.EFI" "$EXITUS"
chmod 0644 "$EXITUS"
printf '%s\n' 'RECTE: probatio Fenestralis II Gradus A constructa est.'
printf 'APPLICATIO: %s\n' "$EXITUS"
