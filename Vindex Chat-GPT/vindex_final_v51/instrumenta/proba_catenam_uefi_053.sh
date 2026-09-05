#!/usr/bin/env bash
# VINDEX 0.53: catenam UEFI historicam automatice comprobat.
#
# Probat sub QEMU + OVMF quod:
#   I.   imago per constructionem OMNINO VINDEX producitur (sine gcc/ld/objcopy);
#   II.  imago autonoma est (nucleus, textus, forma vere in volumine FAT);
#   III. ponticulus VINDEX omnes gradus perficit (nuntius PONTOK);
#   IV.  NULLA exceptio nec defectus paginae accidit;
#   V.   Sylvia in schermo vere pingit (screendump inspectus).
#
# Rector PS/2 Fenestralis modernus separatim a proba_fenestrale_uefi_purum.sh
# in eodem workflow canonico certificatur. Probator muris 0.53 vetus hic non
# duplicatur, quia protocollum injectionis historicae iam auctoritas non est.
#
# Hoc scriptum probationem manualem in certificationem reproducibilem mutat.
# Exitus 0 si omnia recta; aliter numerus gradus qui defecit.

set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
UEFI="$RADIX/systema/uefi"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-probatio-uefi.XXXXXX")"
MORA_INITII="${MORA_INITII:-28}"

purga() {
    rm -rf "$TEMPORARIUM" 2>/dev/null || true
}
trap purga EXIT HUP INT TERM

nuntia() { printf '%s\n' "$*"; }
defecit() { printf 'DEFECIT: %s\n' "$*" >&2; exit "$2"; }

# --- Instrumenta ---
OVMF_CODE=""
for via in /usr/share/OVMF/OVMF_CODE_4M.fd /usr/share/OVMF/OVMF_CODE.fd \
           /usr/share/ovmf/OVMF.fd /usr/share/qemu/OVMF.fd; do
    if [ -f "$via" ]; then OVMF_CODE="$via"; break; fi
done
OVMF_VARS=""
for via in /usr/share/OVMF/OVMF_VARS_4M.fd /usr/share/OVMF/OVMF_VARS.fd; do
    if [ -f "$via" ]; then OVMF_VARS="$via"; break; fi
done

if ! command -v qemu-system-x86_64 >/dev/null 2>&1; then
    nuntia 'OMISSUM: qemu-system-x86_64 deest; probatio UEFI saltatur.'
    exit 0
fi
if [ -z "$OVMF_CODE" ] || [ -z "$OVMF_VARS" ]; then
    nuntia 'OMISSUM: firmware OVMF deest; probatio UEFI saltatur.'
    exit 0
fi

# --- I. Constructio omnino VINDEX ---
nuntia 'I. Constructio (sine gcc, ld, objcopy)...'
bash "$UEFI/construe_uefi_purum.sh" \
    "$TEMPORARIUM/systema.img" "$TEMPORARIUM/BOOTX64.EFI" >"$TEMPORARIUM/constructio.log" 2>&1 \
    || { cat "$TEMPORARIUM/constructio.log" >&2; defecit 'constructio' 1; }

if ! grep -q 'PE32+.*EFI application' <(file "$TEMPORARIUM/BOOTX64.EFI"); then
    defecit 'applicatio UEFI valida non est' 1
fi
nuntia '   RECTE: BOOTX64.EFI a compilatore VINDEX generatum.'

# --- II. Imago autonoma ---
nuntia 'II. Autonomia imaginis...'
for fasciculus in 'NUCLEUS BIN' 'TEXTUS  BIN' 'FORMA   BIN'; do
    grep -qa "$fasciculus" "$TEMPORARIUM/systema.img" \
        || defecit "fasciculus '$fasciculus' in imagine deest" 2
done
nuntia '   RECTE: nucleus, textus, forma vere in volumine FAT.'

# --- III/IV. Exsecutio sub QEMU ---
nuntia 'III. Exsecutio sub QEMU + OVMF...'
cp -f "$OVMF_VARS" "$TEMPORARIUM/OVMF_VARS.fd"
chmod +w "$TEMPORARIUM/OVMF_VARS.fd"

timeout 90 qemu-system-x86_64 -m 2048 \
    -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
    -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/OVMF_VARS.fd" \
    -drive "format=raw,file=$TEMPORARIUM/systema.img" \
    -nographic -net none >"$TEMPORARIUM/exitus.log" 2>&1 || true

if ! strings "$TEMPORARIUM/exitus.log" | grep -q 'PONTOK'; then
    tail -30 "$TEMPORARIUM/exitus.log" >&2
    defecit 'ponticulus gradus suos non perfecit (PONTOK abest)' 3
fi
nuntia '   RECTE: ponticulus omnes gradus perfecit (PONTOK).'

if strings "$TEMPORARIUM/exitus.log" | grep -qE 'X64 Exception Type|ASSERT'; then
    strings "$TEMPORARIUM/exitus.log" | grep -A 6 'X64 Exception Type' >&2
    defecit 'exceptio vel assertio accidit' 4
fi
nuntia '   RECTE: nulla exceptio, nullus defectus paginae.'

# --- V. Sylvia in schermo ---
nuntia 'V. Pictura Sylviae (screendump)...'
cp -f "$OVMF_VARS" "$TEMPORARIUM/OVMF_VARS2.fd"
chmod +w "$TEMPORARIUM/OVMF_VARS2.fd"

{
    sleep "$MORA_INITII"
    printf 'screendump %s\n' "$TEMPORARIUM/schermum.ppm"
    sleep 3
    printf 'quit\n'
} | timeout 120 qemu-system-x86_64 -m 2048 \
    -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
    -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/OVMF_VARS2.fd" \
    -drive "format=raw,file=$TEMPORARIUM/systema.img" \
    -display none -monitor stdio -net none >"$TEMPORARIUM/monitor.log" 2>&1 || true

[ -f "$TEMPORARIUM/schermum.ppm" ] || defecit 'screendump non factus est' 5

python3 - "$TEMPORARIUM/schermum.ppm" <<'PYTHON' || defecit 'Sylvia in schermo non apparet' 5
import sys
from collections import Counter

with open(sys.argv[1], 'rb') as f:
    data = f.read()

partes = data.split(b'\n', 3)
if partes[0] != b'P6':
    print('DEFECIT: forma PPM inexpectata', file=sys.stderr)
    raise SystemExit(1)

latitudo, altitudo = map(int, partes[1].split())
pixels = partes[3]

colores = Counter()
for y in range(0, altitudo, 8):
    for x in range(0, latitudo, 8):
        offset = (y * latitudo + x) * 3
        colores[pixels[offset:offset + 3]] += 1

# Schermum nigrum vel unicolor significat Sylviam non pinxisse.
distincti = len([c for c, n in colores.items() if n > 20])
dominans, quantum = colores.most_common(1)[0]
totum = sum(colores.values())

print(f'   Resolutio: {latitudo}x{altitudo}')
print(f'   Colores distincti: {distincti}')
print(f'   Color dominans: {tuple(dominans)} ({100 * quantum // totum}%)')

if distincti < 3:
    print('DEFECIT: schermum nimis uniforme; Sylvia non pinxit', file=sys.stderr)
    raise SystemExit(1)
if dominans == b'\x00\x00\x00' and quantum > totum * 0.9:
    print('DEFECIT: schermum nigrum', file=sys.stderr)
    raise SystemExit(1)
PYTHON

nuntia '   RECTE: Sylvia in schermo vere pingit.'
nuntia ''
nuntia '=== CATENA UEFI HISTORICA PROBATA ==='
nuntia 'OVMF -> BOOTX64.EFI [VINDEX] -> NUCLEUS [VINDEX] -> FRAMEBUFFER'
nuntia 'Rector PS/2 Fenestralis in gradu workflow sequenti separatim probatur.'
nuntia 'Nullum C in tota via.'
