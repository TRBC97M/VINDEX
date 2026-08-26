#!/usr/bin/env bash
# Sylvia OS UEFI: constructio OMNINO VINDEX, sine gcc, sine ld, sine C.
#
# Differentia a construe_uefi.sh: ille ponticulum C compilat et nucleum in
# ipsam imaginem PE per objcopy/ld inserit. Hic, ponticulus ipse VINDEX est
# (compilatus per modum 'uefi' compilatoris), et nucleus simpliciter ut
# fasciculus in volumine ESP ponitur, quem ponticulus per protocollum
# fasciculorum UEFI legit.
#
# Nulla exceptio linguae manet.

set -eu

RADIX="$(cd "$(dirname "$0")/../.." && pwd)"
UEFI="$RADIX/systema/uefi"
PONTICULUS="${PONTICULUS_FONS:-$RADIX/../../Vindex Claude Ai/uefi-vindex-backend/bootstrap_nucleus_realis.vindex}"
IMAGO="${1:-$RADIX/systema_vindex_uefi_purum.img}"
APPLICATIO="${2:-$RADIX/BOOTX64_PURUM.EFI}"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-uefi-purum.XXXXXX")"

purga() {
    if [ -d "$TEMPORARIUM" ]; then
        find "$TEMPORARIUM" -type f -delete 2>/dev/null || true
        rmdir "$TEMPORARIUM" 2>/dev/null || true
    fi
}
trap purga EXIT HUP INT TERM

# Instrumenta necessaria: solum python3 (pro imagine FAT) et compilator ipse.
# NEC gcc, NEC ld, NEC objcopy.
for instrumentum in python3 file; do
    if ! command -v "$instrumentum" >/dev/null 2>&1; then
        printf 'ERRATUM: instrumentum necessarium deest: %s\n' "$instrumentum" >&2
        exit 69
    fi
done

if [ ! -x "$RADIX/compilator_vindex" ]; then
    printf '%s\n' 'ERRATUM: compilator_vindex exsecutabilis deest.' >&2
    exit 66
fi
if [ ! -f "$PONTICULUS" ]; then
    printf 'ERRATUM: fons ponticuli VINDEX deest: %s\n' "$PONTICULUS" >&2
    exit 66
fi

# I. Ponticulum VINDEX in exsecutabile UEFI compila.
printf '%s\n' 'I. Ponticulus VINDEX -> BOOTX64.EFI (modus uefi)...'
"$RADIX/compilator_vindex" "$PONTICULUS" "$TEMPORARIUM/BOOTX64.EFI" uefi

if ! file "$TEMPORARIUM/BOOTX64.EFI" | grep -q 'PE32+.*EFI application'; then
    printf '%s\n' 'ERRATUM: applicatio UEFI PE32+ valida non est.' >&2
    exit 65
fi

# II. Nucleum VINDEX compila (ut fasciculum separatum, non insertum).
printf '%s\n' 'II. Nucleus VINDEX -> NUCLEUS.BIN...'
"$RADIX/compilator_vindex" "$RADIX/systema/nucleus.vindex" "$TEMPORARIUM/NUCLEUS.BIN"
MAGNITUDO="$(stat -c '%s' "$TEMPORARIUM/NUCLEUS.BIN")"
printf 'Nucleus: %s octeta\n' "$MAGNITUDO"

# III. Data Fenestralis, si adsunt.
if [ -f "$RADIX/fenestrale_systema.bin" ]; then
    cp -f "$RADIX/fenestrale_systema.bin" "$TEMPORARIUM/TEXTUS.BIN"
fi
if [ -f "$UEFI/forma.bin" ]; then
    cp -f "$UEFI/forma.bin" "$TEMPORARIUM/FORMA.BIN"
fi

# IV. Imaginem ESP construe, cum nucleo VERE in volumine incluso.
printf '%s\n' 'III. Imago ESP (cum NUCLEUS.BIN in radice voluminis)...'
python3 "$UEFI/fac_imaginem_uefi.py" \
    "$TEMPORARIUM/BOOTX64.EFI" "$TEMPORARIUM/imago.img" "$TEMPORARIUM/NUCLEUS.BIN"

# Verifica nucleum vere in imagine adesse, non solum iuxta eam.
if ! grep -qa 'NUCLEUS BIN' "$TEMPORARIUM/imago.img"; then
    printf '%s\n' 'ERRATUM: NUCLEUS.BIN in imagine non invenitur.' >&2
    exit 65
fi

mkdir -p "$(dirname "$IMAGO")" "$(dirname "$APPLICATIO")"
cp -f "$TEMPORARIUM/BOOTX64.EFI" "$APPLICATIO"
cp -f "$TEMPORARIUM/imago.img" "$IMAGO"

printf '%s\n' 'RECTE: Sylvia OS UEFI constructa est OMNINO in VINDEX.'
printf '%s\n' 'Nullum gcc, nullum ld, nullum objcopy, nullus C adhibitus est.'
printf 'APPLICATIO: %s\n' "$APPLICATIO"
printf 'IMAGO:      %s (nucleum inclusum continet)\n' "$IMAGO"
