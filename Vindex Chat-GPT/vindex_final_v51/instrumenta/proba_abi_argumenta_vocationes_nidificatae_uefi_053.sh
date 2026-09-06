#!/usr/bin/env bash
# Regressio ABI UEFI: vocationes functionum intra argumenta exteriora.
set -euo pipefail
RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMP="$(mktemp -d "${TMPDIR:-/tmp}/vindex-abi-uefi.XXXXXX")"
PID=""
purga(){ if [ -n "$PID" ]; then kill -- -"$PID" 2>/dev/null || true; wait "$PID" 2>/dev/null || true; fi; rm -rf "$TEMP" 2>/dev/null || true; }
trap purga EXIT HUP INT TERM
fail(){ echo "DEFECIT: $1" >&2; exit "${2:-1}"; }
OVMF_CODE=""; for f in /usr/share/OVMF/OVMF_CODE_4M.fd /usr/share/OVMF/OVMF_CODE.fd; do [ -f "$f" ] && { OVMF_CODE="$f"; break; }; done
OVMF_VARS=""; for f in /usr/share/OVMF/OVMF_VARS_4M.fd /usr/share/OVMF/OVMF_VARS.fd; do [ -f "$f" ] && { OVMF_VARS="$f"; break; }; done
command -v qemu-system-x86_64 >/dev/null || fail 'QEMU deest'
[ -n "$OVMF_CODE" ] && [ -n "$OVMF_VARS" ] || fail 'OVMF deest'

echo 'I. Payload ABI UEFI compilatur...'
(cd "$RADIX/systema" && "$RADIX/compilator_vindex" proba_abi_argumenta_vocationes_nidificatae.vindex "$TEMP/BOOTX64.EFI" uefi)
file "$TEMP/BOOTX64.EFI" | grep -q 'PE32+.*EFI application' || fail 'payload EFI invalidus'
mkdir -p "$TEMP/esp/EFI/BOOT"; cp "$TEMP/BOOTX64.EFI" "$TEMP/esp/EFI/BOOT/BOOTX64.EFI"
cp "$OVMF_VARS" "$TEMP/vars.fd"; chmod +w "$TEMP/vars.fd"

echo 'II. OVMF vocationes nidificatas exercet...'
setsid qemu-system-x86_64 -m 256 -smp 1 -M q35 \
  -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
  -drive "if=pflash,format=raw,unit=1,file=$TEMP/vars.fd" \
  -drive "format=raw,file=fat:rw:$TEMP/esp" \
  -display none -net none -monitor none -serial "file:$TEMP/abi.log" >/tmp/vindex-abi-uefi-qemu.log 2>&1 &
PID=$!
finis=$((SECONDS+45))
while [ "$SECONDS" -lt "$finis" ]; do
  if [ -f "$TEMP/abi.log" ] && grep -aE '^ABIU [0-9A-F]{2}' "$TEMP/abi.log" >/dev/null 2>&1; then break; fi
  sleep 1
done
[ -f "$TEMP/abi.log" ] || fail 'serialis ABI nulla'
LINEA="$(grep -aE '^ABIU [0-9A-F]{2}' "$TEMP/abi.log" | head -1 | tr -d '\r' || true)"
[ -n "$LINEA" ] || { cat "$TEMP/abi.log" >&2 || true; cat /tmp/vindex-abi-uefi-qemu.log >&2 || true; fail 'telemetria ABI nulla'; }
[ "$LINEA" = 'ABIU 00' ] || fail "ABI UEFI nidificata defecta: $LINEA"
echo "   RECTE: $LINEA"
echo '=== ABI UEFI ARGUMENTA NIDIFICATA PROBATA ==='
