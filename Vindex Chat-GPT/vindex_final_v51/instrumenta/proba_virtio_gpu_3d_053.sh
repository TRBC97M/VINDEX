#!/usr/bin/env bash
# P16-XII-F9-I: VIRGL, capsets et contextus III-D reales.
set -euo pipefail
RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMP="$(mktemp -d "${TMPDIR:-/tmp}/vindex-virtio3d.XXXXXX")"
PID=""
purga(){ if [ -n "$PID" ]; then kill -- -"$PID" 2>/dev/null || true; wait "$PID" 2>/dev/null || true; fi; rm -rf "$TEMP" 2>/dev/null || true; }
trap purga EXIT HUP INT TERM
fail(){ echo "DEFECIT: $1" >&2; exit "${2:-1}"; }
OVMF_CODE=""; for f in /usr/share/OVMF/OVMF_CODE_4M.fd /usr/share/OVMF/OVMF_CODE.fd; do [ -f "$f" ] && { OVMF_CODE="$f"; break; }; done
OVMF_VARS=""; for f in /usr/share/OVMF/OVMF_VARS_4M.fd /usr/share/OVMF/OVMF_VARS.fd; do [ -f "$f" ] && { OVMF_VARS="$f"; break; }; done
command -v qemu-system-x86_64 >/dev/null || fail 'QEMU deest'
command -v xvfb-run >/dev/null || fail 'Xvfb deest'
[ -n "$OVMF_CODE" ] && [ -n "$OVMF_VARS" ] || fail 'OVMF deest'
qemu-system-x86_64 -device help 2>&1 | grep -q 'virtio-gpu-gl-pci' || fail 'virtio-gpu-gl-pci deest'

echo 'I. Probatio nativa F9 exercetur...'
(cd "$RADIX" && ./compilator_vindex probationes/virtio_gpu_3d.vindex "$TEMP/native")
chmod +x "$TEMP/native"; "$TEMP/native" || fail 'probatio nativa F9'

echo 'II. Payload UEFI III-D compilatur...'
(cd "$RADIX/systema" && "$RADIX/compilator_vindex" proba_virtio_gpu_3d.vindex "$TEMP/BOOTX64.EFI" uefi)
file "$TEMP/BOOTX64.EFI" | grep -q 'PE32+.*EFI application' || fail 'payload EFI invalidus'
mkdir -p "$TEMP/esp/EFI/BOOT"; cp "$TEMP/BOOTX64.EFI" "$TEMP/esp/EFI/BOOT/BOOTX64.EFI"

exspecta_lineam(){ local file="$1" pat="$2" finis=$((SECONDS+45)); while [ "$SECONDS" -lt "$finis" ]; do if [ -f "$file" ] && grep -aE "$pat" "$file" >/dev/null 2>&1; then return 0; fi; sleep 1; done; return 1; }
occide(){ if [ -n "$PID" ]; then kill -- -"$PID" 2>/dev/null || true; wait "$PID" 2>/dev/null || true; PID=""; fi; }

echo 'III. Apparatus II-D sine VIRGL falsum positivum non facit...'
cp "$OVMF_VARS" "$TEMP/vars2d.fd"; chmod +w "$TEMP/vars2d.fd"
setsid qemu-system-x86_64 -m 1024 -smp 1 -M q35 \
  -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
  -drive "if=pflash,format=raw,unit=1,file=$TEMP/vars2d.fd" \
  -drive "format=raw,file=fat:rw:$TEMP/esp" \
  -device pcie-root-port,id=rp0,bus=pcie.0,chassis=1 \
  -device virtio-gpu-pci,disable-legacy=on,bus=rp0 \
  -vga none -display none -net none -monitor none -serial "file:$TEMP/plain.log" >/tmp/f9plain-qemu.log 2>&1 &
PID=$!
exspecta_lineam "$TEMP/plain.log" '^VIO9 ERR02' || { cat "$TEMP/plain.log" 2>/dev/null || true; fail 'apparatus II-D non VIRGL recte reiectus'; }
occide
echo '   RECTE: backend II-D non fingitur III-D.'

echo 'IV. virtio-gpu-gl per virglrenderer contextum III-D verum creat...'
cp "$OVMF_VARS" "$TEMP/vars3d.fd"; chmod +w "$TEMP/vars3d.fd"
setsid xvfb-run -a env LIBGL_ALWAYS_SOFTWARE=1 SDL_AUDIODRIVER=dummy qemu-system-x86_64 -m 1024 -smp 1 -M q35 \
  -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
  -drive "if=pflash,format=raw,unit=1,file=$TEMP/vars3d.fd" \
  -drive "format=raw,file=fat:rw:$TEMP/esp" \
  -device pcie-root-port,id=rp0,bus=pcie.0,chassis=1 \
  -device virtio-gpu-gl-pci,disable-legacy=on,bus=rp0 \
  -vga none -display sdl,gl=on -net none -monitor none -serial "file:$TEMP/virgl.log" >/tmp/f9virgl-qemu.log 2>&1 &
PID=$!
exspecta_lineam "$TEMP/virgl.log" '^VIO9 O[0-9A-F]{8} ' || { cat "$TEMP/virgl.log" 2>/dev/null || true; cat /tmp/f9virgl-qemu.log >&2 || true; fail 'VIRGL nullam probationem reddidit' 2; }
LINEA="$(grep -aE '^VIO9 O[0-9A-F]{8} ' "$TEMP/virgl.log" | head -1 | tr -d '\r')"
occide
read -r TIT O A N S M I Q R <<<"$LINEA"
[ "$TIT" = VIO9 ] && [ "$R" = R ] || fail "telemetria invalida: $LINEA"
od=$((16#${O#O})); ad=$((16#${A#A})); nd=$((16#${N#N})); sd=$((16#${S#S})); md=$((16#${M#M})); id=$((16#${I#I})); qd=$((16#${Q#Q}))
(( (od & 1) != 0 )) || fail 'VIRGL non oblatum'
(( ad == (1 | (od & 16)) )) || fail 'facultates acceptae non subset optionalis recta'
(( nd > 0 && (sd == 1 || sd == 2) && md > 0 && qd >= 4 )) || fail 'capset/contextus telemetria invalida'
if (( (ad & 16) != 0 )); then (( id == sd )) || fail 'CONTEXT_INIT capset non congruit'; else (( id == 0 )) || fail 'context_init debet esse zero'; fi
echo "   RECTE: $LINEA"
echo '   RECTE: capset realis lectus, contextus III-D creatus et deletus, status PCI restitutus.'
echo '=== FUNDAMENTUM VIRTIO GPU III-D PROBATUM ==='
