#!/usr/bin/env bash
# LABORATORIUM SYLVIAE — constructio experimentalis. Runtime post bootstrap VINDEX est.
set -eu

RADIX="$(git rev-parse --show-toplevel)"
VINDEX="$RADIX/Vindex Chat-GPT/vindex_final_v51"
LAB="$RADIX/laboratorium/sylvia"
EXITUS="${1:-/tmp/sylvia-lab}"

mkdir -p "$EXITUS"
rm -f "$EXITUS"/nucleus.elf "$EXITUS"/nucleus.o "$EXITUS"/textus.bin \
      "$EXITUS"/textus.o "$EXITUS"/forma.bin "$EXITUS"/forma.o \
      "$EXITUS"/bootstrap.o "$EXITUS"/BOOTX64.EFI \
      "$EXITUS"/sylvia-laboratorium.img

"$VINDEX/compilator_vindex" \
  "$LAB/systema/sylvia_laboratorium.vindex" \
  "$EXITUS/nucleus.elf"

cp "$VINDEX/fenestrale_systema.bin" "$EXITUS/textus.bin"
cp "$VINDEX/systema/uefi/forma.bin" "$EXITUS/forma.bin"

(
  cd "$EXITUS"
  objcopy -I binary -O pe-x86-64 -B i386:x86-64 nucleus.elf nucleus.o
  objcopy -I binary -O pe-x86-64 -B i386:x86-64 textus.bin textus.o
  objcopy -I binary -O pe-x86-64 -B i386:x86-64 forma.bin forma.o

  gcc -c -std=c11 -O2 -Wall -Wextra -Werror \
    -ffreestanding -fno-builtin -fno-stack-protector -fno-pie -fno-ident \
    -m64 -mno-red-zone -maccumulate-outgoing-args -fshort-wchar \
    "$LAB/bootstrap/bootstrap_uefi_lab.c" -o bootstrap.o

  objcopy --remove-section .comment --remove-section .note.GNU-stack bootstrap.o

  ld -mi386pep --subsystem 10 --entry efi_main --image-base 0x08000000 \
    --no-insert-timestamp --stack 0x200000 \
    --section-alignment 4096 --file-alignment 512 \
    bootstrap.o nucleus.o textus.o forma.o -o BOOTX64.EFI
)

python3 "$VINDEX/systema/uefi/fac_imaginem_uefi.py" \
  "$EXITUS/BOOTX64.EFI" "$EXITUS/sylvia-laboratorium.img"

file "$EXITUS/BOOTX64.EFI"
printf '%s\n' "RECTE: $EXITUS/sylvia-laboratorium.img"
