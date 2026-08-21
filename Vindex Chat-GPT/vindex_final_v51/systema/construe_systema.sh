#!/usr/bin/env bash
# Imaginem BIOS VINDEX Systema sine Linux in tempore executionis construit.

set -eu

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
IMAGO="${1:-$RADIX/systema_vindex.img}"
NUCLEUS="${2:-$RADIX/nucleus_systema.elf}"
BOOT="${3:-$RADIX/boot_systema.bin}"
TEXTUS="${4:-$RADIX/fenestrale_systema.bin}"
RECTORES="${5:-$RADIX/rectores_systema.bin}"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-systema.XXXXXX")"

purga() {
    if [ -d "$TEMPORARIUM" ]; then
        find "$TEMPORARIUM" -type f -delete
        rmdir "$TEMPORARIUM"
    fi
}
trap purga EXIT HUP INT TERM

for instrumentum in as ld objcopy dd truncate; do
    if ! command -v "$instrumentum" >/dev/null 2>&1; then
        printf 'ERRATUM: instrumentum necessarium deest: %s\n' "$instrumentum" >&2
        exit 69
    fi
done

"$RADIX/compilator_vindex" "$RADIX/systema/nucleus.vindex" "$TEMPORARIUM/nucleus.elf"
MAGNITUDO="$(stat -c '%s' "$TEMPORARIUM/nucleus.elf")"
if [ "$MAGNITUDO" -gt 122880 ]; then
    printf 'ERRATUM: nucleus %s octeta habet; limes est 122880.\n' "$MAGNITUDO" >&2
    exit 65
fi

as --64 "$RADIX/systema/fenestrale_textus.S" -o "$TEMPORARIUM/textus.o"
objcopy -O binary -j .rodata "$TEMPORARIUM/textus.o" "$TEMPORARIUM/textus.bin"
if [ "$(stat -c '%s' "$TEMPORARIUM/textus.bin")" -gt 4096 ]; then
    printf '%s\n' "ERRATUM: textus Fenestralis quattuor KiB excedit." >&2
    exit 65
fi

as --64 "$RADIX/systema/rectores.S" -o "$TEMPORARIUM/rectores.o"
ld -m elf_x86_64 -Ttext 0x41f000 -e _start --oformat binary \
    "$TEMPORARIUM/rectores.o" -o "$TEMPORARIUM/rectores.bin"
if [ "$(stat -c '%s' "$TEMPORARIUM/rectores.bin")" -gt 4096 ]; then
    printf '%s\n' "ERRATUM: rectores quattuor KiB excedunt." >&2
    exit 65
fi

as --64 "$RADIX/systema/boot.S" -o "$TEMPORARIUM/boot.o"
ld -m elf_x86_64 -T "$RADIX/systema/boot.ld" \
    "$TEMPORARIUM/boot.o" -o "$TEMPORARIUM/boot.bin"
if [ "$(stat -c '%s' "$TEMPORARIUM/boot.bin")" -ne 512 ]; then
    printf '%s\n' "ERRATUM: sector initialis non est 512 octetorum." >&2
    exit 65
fi
SIGNUM="$(od -An -tx1 -j510 -N2 "$TEMPORARIUM/boot.bin" | tr -d ' \n')"
if [ "$SIGNUM" != "55aa" ]; then
    printf '%s\n' "ERRATUM: signum BIOS 55aa deest." >&2
    exit 65
fi

truncate -s 1048576 "$TEMPORARIUM/systema.img"
truncate -s 131072 "$TEMPORARIUM/payload.bin"
dd if="$TEMPORARIUM/nucleus.elf" of="$TEMPORARIUM/payload.bin" \
    bs=1 seek=0 conv=notrunc status=none
dd if="$TEMPORARIUM/textus.bin" of="$TEMPORARIUM/payload.bin" \
    bs=1 seek=122880 conv=notrunc status=none
dd if="$TEMPORARIUM/rectores.bin" of="$TEMPORARIUM/payload.bin" \
    bs=1 seek=126976 conv=notrunc status=none
dd if="$TEMPORARIUM/boot.bin" of="$TEMPORARIUM/systema.img" \
    bs=512 seek=0 conv=notrunc status=none
dd if="$TEMPORARIUM/payload.bin" of="$TEMPORARIUM/systema.img" \
    bs=512 seek=1 conv=notrunc status=none

mkdir -p "$(dirname "$IMAGO")" "$(dirname "$NUCLEUS")" \
    "$(dirname "$BOOT")" "$(dirname "$TEXTUS")" "$(dirname "$RECTORES")"
install -m 0644 "$TEMPORARIUM/systema.img" "$IMAGO"
install -m 0644 "$TEMPORARIUM/nucleus.elf" "$NUCLEUS"
install -m 0644 "$TEMPORARIUM/boot.bin" "$BOOT"
install -m 0644 "$TEMPORARIUM/textus.bin" "$TEXTUS"
install -m 0644 "$TEMPORARIUM/rectores.bin" "$RECTORES"
printf '%s\n' "RECTE: VINDEX Systema constructum est."
printf 'IMAGO: %s\n' "$IMAGO"
