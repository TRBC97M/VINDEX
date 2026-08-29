#!/usr/bin/env bash
# Sylvia OS UEFI: constructio OMNINO VINDEX, sine gcc, sine ld, sine C.
#
# Differentia a construe_uefi.sh: ille ponticulum C compilat et nucleum in
# ipsam imaginem PE per objcopy/ld inserit. Hic, ponticulus ipse VINDEX est
# (compilatus per modum 'uefi' compilatoris), et nucleus simpliciter ut
# fasciculus in volumine ESP ponitur, quem ponticulus per protocollum
# fasciculorum UEFI legit.
#
# Si payload est Fenestrale II Purus I, familia JL-UX Premium I automatice
# ex fontibus PNG in SIMG II convertitur et in radicem ESP inseritur. Haec
# conversio est instrumentum constructionis; runtime Sylviae manet VINDEX purus.
# Nulla exceptio linguae runtime manet.

set -eu

RADIX="$(cd "$(dirname "$0")/../.." && pwd)"
UEFI="$RADIX/systema/uefi"
PONTICULUS="${PONTICULUS_FONS:-$RADIX/systema/uefi/ponticulus_uefi_purus.vindex}"
NUCLEUS_FONS="${NUCLEUS_FONS:-$RADIX/systema/nucleus.vindex}"
ASSETA_PREMIUM_I="${ASSETA_PREMIUM_I:-auto}"
IMAGO="${1:-$RADIX/systema_vindex_uefi_purum.img}"
APPLICATIO="${2:-$RADIX/BOOTX64_PURUM.EFI}"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-uefi-purum.XXXXXX")"

purga() {
    if [ -d "$TEMPORARIUM" ]; then
        find "$TEMPORARIUM" -type f -delete 2>/dev/null || true
        find "$TEMPORARIUM" -depth -type d -empty -delete 2>/dev/null || true
    fi
}
trap purga EXIT HUP INT TERM

# Instrumenta necessaria: python3 pro imagine FAT/pipeline artis et compilator ipse.
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
"$RADIX/compilator_vindex" "$NUCLEUS_FONS" "$TEMPORARIUM/NUCLEUS.BIN"
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
ARGS_IMAGINIS="$TEMPORARIUM/BOOTX64.EFI $TEMPORARIUM/imago.img $TEMPORARIUM/NUCLEUS.BIN"
if [ -f "$TEMPORARIUM/TEXTUS.BIN" ]; then
    ARGS_IMAGINIS="$ARGS_IMAGINIS $TEMPORARIUM/TEXTUS.BIN"
    if [ -f "$TEMPORARIUM/FORMA.BIN" ]; then
        ARGS_IMAGINIS="$ARGS_IMAGINIS $TEMPORARIUM/FORMA.BIN"
    fi
fi
python3 "$UEFI/fac_imaginem_uefi.py" $ARGS_IMAGINIS

# Verifica nucleum vere in imagine adesse, non solum iuxta eam.
if ! grep -qa 'NUCLEUS BIN' "$TEMPORARIUM/imago.img"; then
    printf '%s\n' 'ERRATUM: NUCLEUS.BIN in imagine non invenitur.' >&2
    exit 65
fi

# V. Fenestrale canonicum familiam premium runtime secum portat.
# ASSETA_PREMIUM_I=0 hanc additionem tantum ad diagnostica/fallback vetus vetat.
if [ "$ASSETA_PREMIUM_I" != "0" ] && [ "$(basename "$NUCLEUS_FONS")" = "fenestrale_ii_purus_i.vindex" ]; then
    printf '%s\n' 'IV. Asseta JL-UX Premium I -> SIMG II -> radicem ESP...'
    ASSETA_DIR="$TEMPORARIUM/asseta-premium-i"
    mkdir -p "$ASSETA_DIR"
    python3 "$RADIX/instrumenta/genera_asseta_premium_i.py" --destinatio "$ASSETA_DIR" --quietum
    python3 "$RADIX/instrumenta/adde_fasciculos_fat.py" "$TEMPORARIUM/imago.img" \
        "$ASSETA_DIR/programmata@1x.simg=PRG1.SMG" \
        "$ASSETA_DIR/programmata@1_5x.simg=PRG15.SMG" \
        "$ASSETA_DIR/programmata@2x.simg=PRG2.SMG" \
        "$ASSETA_DIR/tabula@1x.simg=TAB1.SMG" \
        "$ASSETA_DIR/tabula@1_5x.simg=TAB15.SMG" \
        "$ASSETA_DIR/tabula@2x.simg=TAB2.SMG" \
        "$ASSETA_DIR/terminale@1x.simg=TRM1.SMG" \
        "$ASSETA_DIR/terminale@1_5x.simg=TRM15.SMG" \
        "$ASSETA_DIR/terminale@2x.simg=TRM2.SMG" \
        "$ASSETA_DIR/officina@1x.simg=OFF1.SMG" \
        "$ASSETA_DIR/officina@1_5x.simg=OFF15.SMG" \
        "$ASSETA_DIR/officina@2x.simg=OFF2.SMG"
    printf '%s\n' '   RECTE: XII asseta SIMG II in imagine Sylviae inclusa.'
fi

mkdir -p "$(dirname "$IMAGO")" "$(dirname "$APPLICATIO")"
cp -f "$TEMPORARIUM/BOOTX64.EFI" "$APPLICATIO"
cp -f "$TEMPORARIUM/imago.img" "$IMAGO"

printf '%s\n' 'RECTE: Sylvia OS UEFI constructa est OMNINO in VINDEX ad runtime.'
printf '%s\n' 'Nullum gcc, nullum ld, nullum objcopy, nullus C adhibitus est.'
printf 'APPLICATIO: %s\n' "$APPLICATIO"
printf 'IMAGO:      %s (nucleum et, pro Fenestrali, asseta premium continet)\n' "$IMAGO"
