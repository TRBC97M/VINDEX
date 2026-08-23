#!/usr/bin/env bash
# Sylvia OS UEFI: bootstrap minimus C, deinde runtime VINDEX purum.

set -eu

RADIX="$(cd "$(dirname "$0")/../.." && pwd)"
UEFI="$RADIX/systema/uefi"
IMAGO="${1:-$RADIX/systema_vindex_uefi.img}"
APPLICATIO="${2:-$RADIX/BOOTX64.EFI}"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-uefi.XXXXXX")"

purga() {
    if [ -d "$TEMPORARIUM" ]; then
        find "$TEMPORARIUM" -type f -delete
        rmdir "$TEMPORARIUM"
    fi
}
trap purga EXIT HUP INT TERM

for instrumentum in gcc ld objcopy python3 install file objdump; do
    if ! command -v "$instrumentum" >/dev/null 2>&1; then
        printf 'ERRATUM: instrumentum necessarium deest: %s\n' "$instrumentum" >&2
        exit 69
    fi
done

if [ ! -x "$RADIX/compilator_vindex" ]; then
    printf '%s\n' 'ERRATUM: compilator_vindex exsecutabilis deest.' >&2
    exit 66
fi
if [ ! -f "$RADIX/fenestrale_systema.bin" ]; then
    printf '%s\n' 'ERRATUM: data textuum Fenestralis desunt.' >&2
    exit 66
fi

# Nucleus ipse VINDEX est; nulla constructio BIOS/assembly antecedens requiritur.
"$RADIX/compilator_vindex" "$RADIX/systema/nucleus.vindex" "$TEMPORARIUM/nucleus.elf"
MAGNITUDO="$(stat -c '%s' "$TEMPORARIUM/nucleus.elf")"
if [ "$MAGNITUDO" -gt 122880 ]; then
    printf 'ERRATUM: nucleus %s octeta habet; limes est 122880.\n' "$MAGNITUDO" >&2
    exit 65
fi

install -m 0644 "$RADIX/fenestrale_systema.bin" "$TEMPORARIUM/textus.bin"
install -m 0644 "$UEFI/forma.bin" "$TEMPORARIUM/forma.bin"

(
    cd "$TEMPORARIUM"
    objcopy -I binary -O pe-x86-64 -B i386:x86-64 nucleus.elf nucleus.o
    objcopy -I binary -O pe-x86-64 -B i386:x86-64 textus.bin textus.o
    objcopy -I binary -O pe-x86-64 -B i386:x86-64 forma.bin forma.o
)

# Unica exceptio linguae non-VINDEX: bootstrap UEFI initii.
gcc -c -std=c11 -O2 -Wall -Wextra -Werror -ffreestanding -fno-builtin \
    -fno-stack-protector -fno-pie -fno-ident -m64 -mno-red-zone -maccumulate-outgoing-args \
    -fshort-wchar "$UEFI/bootstrap_uefi.c" -o "$TEMPORARIUM/bootstrap.o"
objcopy --remove-section .comment --remove-section .note.GNU-stack \
    "$TEMPORARIUM/bootstrap.o"

ld -mi386pep --subsystem 10 --entry efi_main --image-base 0x10000000 \
    --no-insert-timestamp \
    --stack 0x200000 --section-alignment 4096 --file-alignment 512 \
    "$TEMPORARIUM/bootstrap.o" "$TEMPORARIUM/nucleus.o" \
    "$TEMPORARIUM/textus.o" "$TEMPORARIUM/forma.o" \
    -o "$TEMPORARIUM/BOOTX64.EFI"

if ! file "$TEMPORARIUM/BOOTX64.EFI" | grep -q 'PE32+.*EFI application'; then
    printf '%s\n' 'ERRATUM: applicatio UEFI PE32+ valida non est.' >&2
    exit 65
fi
if ! objdump -p "$TEMPORARIUM/BOOTX64.EFI" | grep -q 'Subsystem.*EFI application'; then
    printf '%s\n' 'ERRATUM: subsystema UEFI deest.' >&2
    exit 65
fi

python3 "$UEFI/fac_imaginem_uefi.py" \
    "$TEMPORARIUM/BOOTX64.EFI" "$TEMPORARIUM/systema_vindex_uefi.img"

mkdir -p "$(dirname "$IMAGO")" "$(dirname "$APPLICATIO")"
cp -f "$TEMPORARIUM/BOOTX64.EFI" "$APPLICATIO"
cp -f "$TEMPORARIUM/systema_vindex_uefi.img" "$IMAGO"
chmod 0644 "$APPLICATIO" "$IMAGO"
printf '%s\n' 'RECTE: Sylvia OS UEFI constructa est; runtime post bootstrap VINDEX purum est.'
printf 'APPLICATIO: %s\n' "$APPLICATIO"
printf 'IMAGO: %s\n' "$IMAGO"
