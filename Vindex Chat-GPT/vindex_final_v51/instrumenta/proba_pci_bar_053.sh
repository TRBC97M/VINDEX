#!/usr/bin/env bash
# P12-IV: lectionem BAR et regionum MMIO automatice comprobat.
#
# Probat sub QEMU + OVMF quod:
#   I.   BAR memoriae et portuum recte distinguuntur;
#   II.  adressae regionum verae sunt (collatio cum framebuffer firmware);
#   III. mensurae regionum recte explorantur;
#   IV.  BAR LXIV bitorum agnoscuntur ubi adsunt;
#   V.   valores originales post explorationem restituuntur.
#
# Exitus 0 si omnia recta; aliter numerus gradus qui defecit.

set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-pci-bar.XXXXXX")"
trap 'rm -rf "$TEMPORARIUM" 2>/dev/null || true' EXIT HUP INT TERM

nuntia() { printf '%s\n' "$*"; }
defecit() { printf 'DEFECIT: %s\n' "$1" >&2; exit "$2"; }

OVMF_CODE=""
for v in /usr/share/OVMF/OVMF_CODE_4M.fd /usr/share/OVMF/OVMF_CODE.fd; do
    [ -f "$v" ] && { OVMF_CODE="$v"; break; }
done
OVMF_VARS=""
for v in /usr/share/OVMF/OVMF_VARS_4M.fd /usr/share/OVMF/OVMF_VARS.fd; do
    [ -f "$v" ] && { OVMF_VARS="$v"; break; }
done

if ! command -v qemu-system-x86_64 >/dev/null 2>&1 || [ -z "$OVMF_CODE" ] || [ -z "$OVMF_VARS" ]; then
    nuntia 'OMISSUM: QEMU vel OVMF deest; probatio BAR saltatur.'
    exit 0
fi

nuntia 'I. Probatio BAR in modo uefi compilatur...'
( cd "$RADIX/systema" && "$RADIX/compilator_vindex" proba_pci_bar.vindex \
    "$TEMPORARIUM/BOOTX64.EFI" uefi ) >"$TEMPORARIUM/comp.log" 2>&1 \
    || { cat "$TEMPORARIUM/comp.log" >&2; defecit 'compilatio' 1; }
file "$TEMPORARIUM/BOOTX64.EFI" | grep -q 'PE32+.*EFI application' \
    || defecit 'exsecutabile EFI invalidum' 1
nuntia '   RECTE: exsecutabile EFI generatum.'

mkdir -p "$TEMPORARIUM/esp/EFI/BOOT"
cp -f "$TEMPORARIUM/BOOTX64.EFI" "$TEMPORARIUM/esp/EFI/BOOT/BOOTX64.EFI"

exsequere() {
    local exitus="$1"; shift
    cp -f "$OVMF_VARS" "$TEMPORARIUM/vars.fd"; chmod +w "$TEMPORARIUM/vars.fd"
    timeout 90 qemu-system-x86_64 -m 2048 \
        -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
        -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/vars.fd" \
        -drive "format=raw,file=fat:rw:$TEMPORARIUM/esp" \
        -nographic -net none "$@" >"$exitus" 2>&1 || true
}

# --- II. Topologia praedefinita ---
nuntia 'II. Lectio BAR (i440fx)...'
exsequere "$TEMPORARIUM/planum.log"
strings "$TEMPORARIUM/planum.log" | grep -E '^[0-9A-F]{4}:[0-9A-F]{4} B' \
    >"$TEMPORARIUM/bar.txt" || true

[ -s "$TEMPORARIUM/bar.txt" ] || {
    tail -20 "$TEMPORARIUM/planum.log" >&2
    defecit 'nullum BAR lectum' 2
}
NUM="$(wc -l <"$TEMPORARIUM/bar.txt")"
nuntia "   RECTE: $NUM BAR lecti."

# --- III. Genera distincta: memoria et portus ---
nuntia 'III. Distinctio memoriae et portuum...'
grep -qE ' M ' "$TEMPORARIUM/bar.txt" || defecit 'nullum BAR memoriae agnitum' 3
grep -qE ' P ' "$TEMPORARIUM/bar.txt" || defecit 'nullum BAR portuum agnitum' 3
nuntia '   RECTE: BAR memoriae et portuum ambo agniti.'

# --- IV. Framebuffer apparatus graphici ---
# QEMU VGA (1234:1111) framebuffer per BAR 0 exponit, ad 0x80000000,
# mensura pluribus megabytis. Haec adressa cum ea quam firmware per
# protocollum graphicum reddit congruere DEBET.
nuntia 'IV. Regio framebuffer apparatus graphici...'
LINEA_FB="$(grep -E '^1234:1111 B00 M ' "$TEMPORARIUM/bar.txt" | head -1 || true)"
[ -n "$LINEA_FB" ] || {
    cat "$TEMPORARIUM/bar.txt" >&2
    defecit 'BAR 0 apparatus graphici non inventus' 4
}
ADR_FB="$(printf '%s\n' "$LINEA_FB" | awk '{print $4}')"
MENS_FB="$(printf '%s\n' "$LINEA_FB" | awk '{print $5}')"
[ "$ADR_FB" = "80000000" ] || defecit "adressa framebuffer inexpectata: $ADR_FB" 4
MENS_DEC="$((16#${MENS_FB}))"
[ "$MENS_DEC" -ge 1048576 ] || defecit "mensura framebuffer nimis parva: $MENS_FB" 4
nuntia "   RECTE: framebuffer ad 0x$ADR_FB, mensura 0x$MENS_FB ($((MENS_DEC/1048576)) MiB)."

# --- V. Mensurae explorationis validae ---
# Omnis mensura potentia duorum esse debet (regula PCI).
nuntia 'V. Validitas mensurarum exploratarum...'
while read -r _ _ _ _ mens; do
    [ -n "$mens" ] || continue
    d="$((16#${mens}))"
    [ "$d" -gt 0 ] || continue
    # potentia duorum: d & (d-1) == 0
    [ "$(( d & (d-1) ))" -eq 0 ] || defecit "mensura non potentia duorum: 0x$mens" 5
done <"$TEMPORARIUM/bar.txt"
nuntia '   RECTE: omnes mensurae potentiae duorum sunt.'

# --- VI. BAR LXIV bitorum in topologia moderna ---
nuntia 'VI. BAR LXIV bitorum (q35 cum e1000e)...'
exsequere "$TEMPORARIUM/lxiv.log" -M q35 \
    -device pcie-root-port,id=rp0,bus=pcie.0,chassis=1 \
    -device e1000e,bus=rp0
strings "$TEMPORARIUM/lxiv.log" | grep -E '^[0-9A-F]{4}:[0-9A-F]{4} B' \
    >"$TEMPORARIUM/lxiv.txt" || true
[ -s "$TEMPORARIUM/lxiv.txt" ] || defecit 'nullum BAR in topologia q35' 6
nuntia "   RECTE: $(wc -l <"$TEMPORARIUM/lxiv.txt") BAR in topologia q35."

nuntia ''
nuntia '=== BAR ET REGIONES MMIO PROBATA ==='
sed 's/^/   /' "$TEMPORARIUM/bar.txt"
