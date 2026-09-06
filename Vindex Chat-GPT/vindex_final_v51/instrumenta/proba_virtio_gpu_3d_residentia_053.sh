#!/usr/bin/env bash
# P16-XII-F9-II: residentia Graphica X in resource VIRGL reali.
set -euo pipefail
RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMP="$(mktemp -d "${TMPDIR:-/tmp}/vindex-virtio3d-res.XXXXXX")"
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

echo 'I. Probatio nativa residentiae F9-II exercetur...'
(cd "$RADIX" && ./compilator_vindex probationes/virtio_gpu_3d_residentia.vindex "$TEMP/native")
chmod +x "$TEMP/native"; "$TEMP/native" || fail 'probatio nativa F9-II'

echo 'II. Payload UEFI residentiae III-D compilatur...'
(cd "$RADIX/systema" && "$RADIX/compilator_vindex" proba_virtio_gpu_3d_residentia.vindex "$TEMP/BOOTX64.EFI" uefi)
file "$TEMP/BOOTX64.EFI" | grep -q 'PE32+.*EFI application' || fail 'payload EFI invalidus'
mkdir -p "$TEMP/esp/EFI/BOOT"; cp "$TEMP/BOOTX64.EFI" "$TEMP/esp/EFI/BOOT/BOOTX64.EFI"

exspecta_lineam(){ local file="$1" pat="$2" finis=$((SECONDS+50)); while [ "$SECONDS" -lt "$finis" ]; do if [ -f "$file" ] && grep -aE "$pat" "$file" >/dev/null 2>&1; then return 0; fi; sleep 1; done; return 1; }
occide(){ if [ -n "$PID" ]; then kill -- -"$PID" 2>/dev/null || true; wait "$PID" 2>/dev/null || true; PID=""; fi; }

echo 'III. Graphica X resource III-D creat, uploadat, renovat et liberat...'
cp "$OVMF_VARS" "$TEMP/vars3d.fd"; chmod +w "$TEMP/vars3d.fd"
setsid xvfb-run -a env LIBGL_ALWAYS_SOFTWARE=1 SDL_AUDIODRIVER=dummy qemu-system-x86_64 -m 1024 -smp 1 -M q35 \
  -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
  -drive "if=pflash,format=raw,unit=1,file=$TEMP/vars3d.fd" \
  -drive "format=raw,file=fat:rw:$TEMP/esp" \
  -device pcie-root-port,id=rp0,bus=pcie.0,chassis=1 \
  -device virtio-gpu-gl-pci,disable-legacy=on,bus=rp0 \
  -vga none -display sdl,gl=on -net none -monitor none -serial "file:$TEMP/virgl.log" >/tmp/f9ii-virgl-qemu.log 2>&1 &
PID=$!
exspecta_lineam "$TEMP/virgl.log" '^VIO10 (C[0-9A-F]{8}|ERR[0-9A-F]{2})' || { cat "$TEMP/virgl.log" 2>/dev/null || true; cat /tmp/f9ii-virgl-qemu.log >&2 || true; fail 'residentia III-D nullam probationem reddidit' 2; }
if grep -aE '^VIO10 ERR' "$TEMP/virgl.log" >/dev/null; then cat "$TEMP/virgl.log"; cat /tmp/f9ii-virgl-qemu.log >&2 || true; fail 'payload residentiae errorem reddidit' 3; fi
LINEA="$(grep -aE '^VIO10 C[0-9A-F]{8} ' "$TEMP/virgl.log" | head -1 | tr -d '\r')"
occide
read -r TIT C U A D F I G H S R <<<"$LINEA"
[ "$TIT" = VIO10 ] && [ "$R" = R ] || fail "telemetria invalida: $LINEA"
cd=$((16#${C#C})); ud=$((16#${U#U})); ad=$((16#${A#A})); dd=$((16#${D#D})); fd=$((16#${F#F})); id=$((16#${I#I})); g0=$((16#${G#G})); g1=$((16#${H#H})); same=$((16#${S#S}))
(( cd == 1 && ud == 2 && ad == 1 && dd == 1 && fd == 1 )) || fail 'cycle vitae resource III-D non exactus'
(( id >= 4096 && g1 > g0 && same == 1 )) || fail 'identitas/generatio residentiae non congruit'
echo "   RECTE: $LINEA"
echo '   RECTE: eadem resource post mutationem Graphica X renovata, deinde contextu/backing/resource ordine liberata.'
echo '=== RESIDENTIA VIRTIO GPU III-D PROBATA ==='
