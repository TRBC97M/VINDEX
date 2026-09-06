#!/usr/bin/env bash
# P16-XII-F9-III: primum SUBMIT_3D raster et readback pixel-equivalens.
set -euo pipefail
RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMP="$(mktemp -d "${TMPDIR:-/tmp}/vindex-virtio3d-raster.XXXXXX")"
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

echo 'I. Probatio nativa protocoli F9-III exercetur...'
(cd "$RADIX" && ./compilator_vindex probationes/virtio_gpu_3d_raster.vindex "$TEMP/native")
chmod +x "$TEMP/native"; "$TEMP/native" || fail 'probatio nativa F9-III'

echo 'II. Payload UEFI raster III-D compilatur...'
(cd "$RADIX" && ./compilator_vindex systema/proba_virtio_gpu_3d_raster.vindex "$TEMP/BOOTX64.EFI" uefi)
file "$TEMP/BOOTX64.EFI" | grep -q 'PE32+.*EFI application' || fail 'payload EFI invalidus'
mkdir -p "$TEMP/esp/EFI/BOOT"; cp "$TEMP/BOOTX64.EFI" "$TEMP/esp/EFI/BOOT/BOOTX64.EFI"

exspecta_lineam(){ local file="$1" pat="$2" finis=$((SECONDS+55)); while [ "$SECONDS" -lt "$finis" ]; do if [ -f "$file" ] && grep -aE "$pat" "$file" >/dev/null 2>&1; then return 0; fi; sleep 1; done; return 1; }
occide(){ if [ -n "$PID" ]; then kill -- -"$PID" 2>/dev/null || true; wait "$PID" 2>/dev/null || true; PID=""; fi; }

echo 'III. Apparatus II-D sine VIRGL raster III-D non fingit...'
cp "$OVMF_VARS" "$TEMP/vars2d.fd"; chmod +w "$TEMP/vars2d.fd"
setsid qemu-system-x86_64 -m 1024 -smp 1 -M q35 \
  -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
  -drive "if=pflash,format=raw,unit=1,file=$TEMP/vars2d.fd" \
  -drive "format=raw,file=fat:rw:$TEMP/esp" \
  -device pcie-root-port,id=rp0,bus=pcie.0,chassis=1 \
  -device virtio-gpu-pci,disable-legacy=on,bus=rp0 \
  -vga none -display none -net none -monitor none -serial "file:$TEMP/plain.log" >/tmp/f9iii-plain-qemu.log 2>&1 &
PID=$!
exspecta_lineam "$TEMP/plain.log" '^VIO11 ERR02' || { cat "$TEMP/plain.log" 2>/dev/null || true; cat /tmp/f9iii-plain-qemu.log >&2 || true; fail 'apparatus II-D viam III-D non recte recusavit'; }
occide
echo '   RECTE: backend II-D non simulat SUBMIT_3D.'

echo 'IV. VIRGL SUBMIT_3D superficiem mutat et VINDEX pixela retro legit...'
cp "$OVMF_VARS" "$TEMP/vars3d.fd"; chmod +w "$TEMP/vars3d.fd"
setsid xvfb-run -a env LIBGL_ALWAYS_SOFTWARE=1 SDL_AUDIODRIVER=dummy qemu-system-x86_64 -m 1024 -smp 1 -M q35 \
  -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
  -drive "if=pflash,format=raw,unit=1,file=$TEMP/vars3d.fd" \
  -drive "format=raw,file=fat:rw:$TEMP/esp" \
  -device pcie-root-port,id=rp0,bus=pcie.0,chassis=1 \
  -device virtio-gpu-gl-pci,disable-legacy=on,bus=rp0 \
  -vga none -display sdl,gl=on -net none -monitor none -serial "file:$TEMP/virgl.log" >/tmp/f9iii-virgl-qemu.log 2>&1 &
PID=$!
exspecta_lineam "$TEMP/virgl.log" '^VIO11 (B[0-9A-F]{8}|ERR[0-9A-F]{2})' || { cat "$TEMP/virgl.log" 2>/dev/null || true; cat /tmp/f9iii-virgl-qemu.log >&2 || true; fail 'raster III-D nullam probationem reddidit' 2; }
if grep -aE '^VIO11 ERR' "$TEMP/virgl.log" >/dev/null; then cat "$TEMP/virgl.log"; cat /tmp/f9iii-virgl-qemu.log >&2 || true; fail 'payload raster errorem reddidit' 3; fi
LINEA="$(grep -aE '^VIO11 B[0-9A-F]{8} ' "$TEMP/virgl.log" | head -1 | tr -d '\r')"
occide
read -r TIT B S P M F R <<<"$LINEA"
[ "$TIT" = VIO11 ] && [ "$R" = R ] || fail "telemetria invalida: $LINEA"
bd=$((16#${B#B})); sd=$((16#${S#S})); pd=$((16#${P#P})); md=$((16#${M#M})); fd=$((16#${F#F}))
(( bd == 0 )) || fail 'baseline resource non nigra fuit'
(( sd == 1 && pd == 128 && md == 0 )) || fail 'SUBMIT_3D non est pixel-equivalens oraculo software'
(( fd == 2 )) || fail 'fences submit/readback non exactae'
echo "   RECTE: $LINEA"
echo '   RECTE: CXXVIII pixela post SUBMIT_3D readback bit/pixel-equivalentia Graphica X sunt.'
echo '=== PRIMUM RASTER VIRTIO GPU III-D PROBATUM ==='