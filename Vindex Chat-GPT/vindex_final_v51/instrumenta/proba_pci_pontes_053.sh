#!/usr/bin/env bash
# P12-III: enumerationem PCI per pontes automatice comprobat.
#
# Probat sub QEMU + OVMF quod:
#   I.   enumeratio plana antiqua adhuc functionat (nulla regressio);
#   II.  pontes PCI-ad-PCI recte agnoscuntur (classis 06, subclassis 04);
#   III. bus secundarii post pontes vere percurruntur;
#   IV.  nullus apparatus bis numeratur;
#   V.   registrum vere dynamice crescit (capacitas initialis II).
#
# Topologia cum pontibus per configurationem QEMU construitur (machina
# q35 cum pcie-root-port et apparatibus post eos): nihil in runtime
# fingitur, apparatus veri a firmware enumerantur.
#
# Exitus 0 si omnia recta; aliter numerus gradus qui defecit.

set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-pci-pontes.XXXXXX")"

purga() { rm -rf "$TEMPORARIUM" 2>/dev/null || true; }
trap purga EXIT HUP INT TERM

nuntia() { printf '%s\n' "$*"; }
defecit() { printf 'DEFECIT: %s\n' "$1" >&2; exit "$2"; }

OVMF_CODE=""
for via in /usr/share/OVMF/OVMF_CODE_4M.fd /usr/share/OVMF/OVMF_CODE.fd; do
    [ -f "$via" ] && { OVMF_CODE="$via"; break; }
done
OVMF_VARS=""
for via in /usr/share/OVMF/OVMF_VARS_4M.fd /usr/share/OVMF/OVMF_VARS.fd; do
    [ -f "$via" ] && { OVMF_VARS="$via"; break; }
done

if ! command -v qemu-system-x86_64 >/dev/null 2>&1 || [ -z "$OVMF_CODE" ] || [ -z "$OVMF_VARS" ]; then
    nuntia 'OMISSUM: QEMU vel OVMF deest; probatio PCI saltatur.'
    exit 0
fi

# --- Constructio exsecutabilis probationis ---
nuntia 'I. Probatio PCI in modo uefi compilatur...'
( cd "$RADIX/systema" && "$RADIX/compilator_vindex" proba_pci_pontes.vindex \
    "$TEMPORARIUM/BOOTX64.EFI" uefi ) >"$TEMPORARIUM/compilatio.log" 2>&1 \
    || { cat "$TEMPORARIUM/compilatio.log" >&2; defecit 'compilatio probationis' 1; }

file "$TEMPORARIUM/BOOTX64.EFI" | grep -q 'PE32+.*EFI application' \
    || defecit 'exsecutabile EFI invalidum' 1
nuntia '   RECTE: exsecutabile EFI generatum.'

mkdir -p "$TEMPORARIUM/esp/EFI/BOOT"
cp -f "$TEMPORARIUM/BOOTX64.EFI" "$TEMPORARIUM/esp/EFI/BOOT/BOOTX64.EFI"

exsequere() {
    # $1 = nomen exitus, reliqua = argumenta QEMU addita
    local exitus="$1"; shift
    cp -f "$OVMF_VARS" "$TEMPORARIUM/vars.fd"
    chmod +w "$TEMPORARIUM/vars.fd"
    timeout 90 qemu-system-x86_64 -m 2048 \
        -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
        -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/vars.fd" \
        -drive "format=raw,file=fat:rw:$TEMPORARIUM/esp" \
        -nographic -net none "$@" >"$exitus" 2>&1 || true
}

# --- II. Topologia plana (nulla regressio) ---
nuntia 'II. Topologia plana (i440fx, sine pontibus)...'
exsequere "$TEMPORARIUM/planum.log"
strings "$TEMPORARIUM/planum.log" | grep -E '^PCIP=' >"$TEMPORARIUM/planum.txt" || true
strings "$TEMPORARIUM/planum.log" | grep -E '^[0-9A-F]{2}:[0-9A-F]{2}\.' >>"$TEMPORARIUM/planum.txt" || true

grep -q '^PCIP=' "$TEMPORARIUM/planum.txt" || defecit 'enumeratio plana nihil reddidit' 2
NUM_PLANUM="$(grep -cE '^[0-9A-F]{2}:' "$TEMPORARIUM/planum.txt" || true)"
[ "$NUM_PLANUM" -ge 4 ] || defecit "topologia plana: solum $NUM_PLANUM apparatus" 2
nuntia "   RECTE: $NUM_PLANUM apparatus in topologia plana."

# --- III. Topologia cum pontibus ---
nuntia 'III. Topologia cum duobus pontibus (q35 + pcie-root-port)...'
exsequere "$TEMPORARIUM/pontes.log" -M q35 \
    -device pcie-root-port,id=rp0,bus=pcie.0,chassis=1 \
    -device pcie-root-port,id=rp1,bus=pcie.0,chassis=2 \
    -device e1000e,bus=rp0 -device e1000e,bus=rp1
strings "$TEMPORARIUM/pontes.log" | grep -E '^PCIP=' >"$TEMPORARIUM/pontes.txt" || true
strings "$TEMPORARIUM/pontes.log" | grep -E '^[0-9A-F]{2}:[0-9A-F]{2}\.' >>"$TEMPORARIUM/pontes.txt" || true

grep -q '^PCIP=' "$TEMPORARIUM/pontes.txt" || defecit 'enumeratio cum pontibus nihil reddidit' 3

# Pontes agnoscendi sunt: classis 06, subclassis 04, cum bus secundario.
NUM_PONTIUM="$(grep -cE '06/04 P=[0-9A-F]{2} PONS>' "$TEMPORARIUM/pontes.txt" || true)"
[ "$NUM_PONTIUM" -ge 2 ] || defecit "pontes non agniti (inventi: $NUM_PONTIUM)" 3
nuntia "   RECTE: $NUM_PONTIUM pontes agniti cum bus secundario."

# --- IV. Bus secundarii percursi ---
nuntia 'IV. Apparatus post pontes...'
POST_PONTEM="$(grep -cE '^(0[1-9]|[1-9A-F][0-9A-F]):' "$TEMPORARIUM/pontes.txt" || true)"
[ "$POST_PONTEM" -ge 2 ] || defecit "apparatus post pontes non inventi (inventi: $POST_PONTEM)" 4
nuntia "   RECTE: $POST_PONTEM apparatus in bus secundariis inventi."

# --- V. Nullus apparatus bis numeratus ---
nuntia 'V. Unicitas apparatuum...'
GEMINI="$(grep -E '^[0-9A-F]{2}:' "$TEMPORARIUM/pontes.txt" | sort | uniq -d | wc -l)"
[ "$GEMINI" -eq 0 ] || {
    grep -E '^[0-9A-F]{2}:' "$TEMPORARIUM/pontes.txt" | sort | uniq -d >&2
    defecit "apparatus gemini inventi: $GEMINI" 5
}
nuntia '   RECTE: nullus apparatus bis numeratus.'

# --- VI. Registrum vere dynamicum ---
nuntia 'VI. Crescentia registri...'
CAPACITAS="$(grep -oE 'CAP=[0-9A-F]{4}' "$TEMPORARIUM/pontes.txt" | head -1 | cut -d= -f2)"
CAP_DEC="$((16#${CAPACITAS}))"
[ "$CAP_DEC" -gt 2 ] || defecit "registrum non crevit (capacitas $CAP_DEC, initialis 2)" 6
nuntia "   RECTE: capacitas ex II ad $CAP_DEC crevit (duplicatio vera)."

# --- VII. Profunditas vera in topologia nidificata ---
nuntia 'VII. Topologia nidificata (pons in ponte)...'
exsequere "$TEMPORARIUM/nidus.log" -M q35 \
    -device pcie-root-port,id=rp0,bus=pcie.0,chassis=1 \
    -device x3130-upstream,id=up0,bus=rp0 \
    -device xio3130-downstream,id=dn0,bus=up0,chassis=2,slot=0 \
    -device e1000e,bus=dn0
strings "$TEMPORARIUM/nidus.log" | grep -E '^[0-9A-F]{2}:[0-9A-F]{2}\.' >"$TEMPORARIUM/nidus.txt" || true

# Profunditas vera: apparatus in fine catenae profunditatem III habere debet.
grep -qE 'P=03' "$TEMPORARIUM/nidus.txt" \
    || { cat "$TEMPORARIUM/nidus.txt" >&2; defecit 'profunditas vera non computata (P=03 abest)' 7; }
nuntia '   RECTE: profunditas vera arboris computata (0 -> 1 -> 2 -> 3).'

# Numeri bus primarius/secundarius/subordinatus expliciti.
grep -qE 'PONS>0[0-9]/0[0-9]/0[0-9]' "$TEMPORARIUM/nidus.txt" \
    || defecit 'numeri bus primarius/secundarius/subordinatus non expliciti' 7
nuntia '   RECTE: bus primarius/secundarius/subordinatus expliciti.'

nuntia ''
nuntia '=== ENUMERATIO PCI PER PONTES PROBATA ==='
nuntia 'Topologia plana:'
sed 's/^/   /' "$TEMPORARIUM/pontes.txt"
nuntia 'Topologia nidificata:'
sed 's/^/   /' "$TEMPORARIUM/nidus.txt"
