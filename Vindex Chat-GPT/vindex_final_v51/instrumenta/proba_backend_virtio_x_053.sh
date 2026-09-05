#!/usr/bin/env bash
# P16-XII-F7: Graphica X per verum scanout VirtIO GPU sub QEMU probat.

set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-backend-virtio-x.XXXXXX")"
QEMU_PID=""
purga() {
    if [ -n "$QEMU_PID" ] && kill -0 "$QEMU_PID" 2>/dev/null; then
        kill "$QEMU_PID" 2>/dev/null || true
        wait "$QEMU_PID" 2>/dev/null || true
    fi
    rm -rf "$TEMPORARIUM" 2>/dev/null || true
}
trap purga EXIT HUP INT TERM

nuntia() { printf '%s\n' "$*"; }
defecit() { printf 'DEFECIT: %s\n' "$1" >&2; exit "$2"; }

nuntia 'I. Contractus backend VirtIO Graphica X nativus exercetur...'
( cd "$RADIX" && ./compilator_vindex probationes/backend_virtio_x.vindex "$TEMPORARIUM/backend-virtio-x" ) \
    >"$TEMPORARIUM/native-comp.log" 2>&1 \
    || { sed -n '1,240p' "$TEMPORARIUM/native-comp.log" >&2; defecit 'compilatio nativa' 1; }
chmod +x "$TEMPORARIUM/backend-virtio-x"
"$TEMPORARIUM/backend-virtio-x" || defecit 'contractus backend nativus' "$?"
nuntia '   RECTE: coda communis in target DMA exactum componit.'

OVMF_CODE=""
for v in /usr/share/OVMF/OVMF_CODE_4M.fd /usr/share/OVMF/OVMF_CODE.fd; do
    [ -f "$v" ] && { OVMF_CODE="$v"; break; }
done
OVMF_VARS=""
for v in /usr/share/OVMF/OVMF_VARS_4M.fd /usr/share/OVMF/OVMF_VARS.fd; do
    [ -f "$v" ] && { OVMF_VARS="$v"; break; }
done

if ! command -v qemu-system-x86_64 >/dev/null 2>&1 || [ -z "$OVMF_CODE" ] || [ -z "$OVMF_VARS" ]; then
    nuntia 'OMISSUM: QEMU vel OVMF deest; scanout VirtIO sub firmware saltatur.'
    exit 0
fi
if ! qemu-system-x86_64 -device help 2>&1 | grep -Eq 'name "virtio-gpu-pci"'; then
    defecit 'apparatus QEMU virtio-gpu-pci deest' 1
fi

nuntia 'II. Praesentator F7 in modo UEFI compilatur...'
( cd "$RADIX/systema" && "$RADIX/compilator_vindex" proba_backend_virtio_x.vindex \
    "$TEMPORARIUM/BOOTX64.EFI" uefi ) >"$TEMPORARIUM/comp.log" 2>&1 \
    || { sed -n '1,300p' "$TEMPORARIUM/comp.log" >&2; defecit 'compilatio UEFI' 1; }
file "$TEMPORARIUM/BOOTX64.EFI" | grep -q 'PE32+.*EFI application' \
    || defecit 'exsecutabile EFI invalidum' 1
nuntia '   RECTE: exsecutabile EFI generatum.'

mkdir -p "$TEMPORARIUM/esp/EFI/BOOT"
cp -f "$TEMPORARIUM/BOOTX64.EFI" "$TEMPORARIUM/esp/EFI/BOOT/BOOTX64.EFI"
cp -f "$OVMF_VARS" "$TEMPORARIUM/vars.fd"
chmod +w "$TEMPORARIUM/vars.fd"

nuntia 'III. Duo damna per coda et scanout VirtIO praesentantur...'
qemu-system-x86_64 -m 1024 -smp 1 -M q35 \
    -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
    -drive "if=pflash,format=raw,unit=1,file=$TEMPORARIUM/vars.fd" \
    -drive "format=raw,file=fat:rw:$TEMPORARIUM/esp" \
    -device pcie-root-port,id=rp0,bus=pcie.0,chassis=1 \
    -device virtio-gpu-pci,disable-legacy=on,bus=rp0 \
    -vga none -display vnc=127.0.0.1:99 -net none \
    -serial "file:$TEMPORARIUM/virtio.log" \
    -monitor "unix:$TEMPORARIUM/monitor.sock,server=on,wait=off" \
    >"$TEMPORARIUM/qemu.log" 2>&1 &
QEMU_PID="$!"
FINIS="$((SECONDS + 90))"
while kill -0 "$QEMU_PID" 2>/dev/null && [ "$SECONDS" -lt "$FINIS" ]; do
    if strings "$TEMPORARIUM/virtio.log" 2>/dev/null | grep -E '^VIO7 (T|ERR)' >/dev/null; then
        break
    fi
    sleep 1
done

LINEA="$(strings "$TEMPORARIUM/virtio.log" 2>/dev/null | grep -E '^VIO7 (T|ERR)' | tail -1 || true)"
case "$LINEA" in
    'VIO7 ERR'*) defecit "payload VINDEX rettulit: $LINEA" 2 ;;
    'VIO7 T'*) ;;
    *) tail -100 "$TEMPORARIUM/qemu.log" >&2; defecit 'praesentator nullam probationem reddidit' 2 ;;
esac

read -r TITULUS GENUS PRAESENTATAE DAMNUM SEPES VITATA RESTA <<<"$LINEA"
[ "$TITULUS" = "VIO7" ] && [ "$GENUS" = "T02" ] \
    || defecit "backend GPU invalidus: $LINEA" 3
[ "$PRAESENTATAE" = "P00000002" ] || defecit "numerus praesentiarum invalidus: $PRAESENTATAE" 3
[ "$DAMNUM" = "D000FB000" ] || defecit "numerus pixelorum invalidus: $DAMNUM" 3
[ "$SEPES" = "F00000007" ] || defecit "sepes hardware invalida: $SEPES" 3
[ "$VITATA" = "Z000FB000" ] || defecit "copiae praesentiae non vitatae sunt: $VITATA" 3
[ "$RESTA" = "R" ] || defecit 'signum finale deest' 3

[ -S "$TEMPORARIUM/monitor.sock" ] || defecit 'monitor QEMU deest' 4
python3 - "$TEMPORARIUM/monitor.sock" "$TEMPORARIUM/scanout.ppm" <<'PY'
import socket
import sys
import time

sock_path, image_path = sys.argv[1:]
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.settimeout(5)
s.connect(sock_path)
s.sendall((f"screendump {image_path}\n").encode())
deadline = time.monotonic() + 10
response = bytearray()
while time.monotonic() < deadline:
    try:
        data = s.recv(4096)
    except socket.timeout:
        break
    response.extend(data)
    if b"Error" in response:
        break
    if response.count(b"(qemu)") >= 2:
        break
s.close()
print(response.decode(errors="replace"))
PY

FINIS_IMAGO="$((SECONDS + 10))"
while [ ! -s "$TEMPORARIUM/scanout.ppm" ] && [ "$SECONDS" -lt "$FINIS_IMAGO" ]; do sleep 1; done
[ -s "$TEMPORARIUM/scanout.ppm" ] || defecit 'captura scanout deest' 4

python3 - "$TEMPORARIUM/scanout.ppm" <<'PY'
import sys

path = sys.argv[1]
with open(path, "rb") as f:
    magic = f.readline().strip()
    dims = f.readline().strip()
    while dims.startswith(b"#"):
        dims = f.readline().strip()
    maximum = f.readline().strip()
    pixels = f.read()
if magic != b"P6" or maximum != b"255":
    raise SystemExit("captura PPM invalida")
w, h = map(int, dims.split())
if (w, h) != (1280, 800) or len(pixels) != w * h * 3:
    raise SystemExit(f"dimensio captura invalida: {w}x{h}, {len(pixels)}")
def rgb(x, y):
    i = (y * w + x) * 3
    return tuple(pixels[i:i+3])
expected = {
    (100, 100): (255, 0, 0),
    (1180, 100): (0, 255, 0),
    (100, 700): (0, 0, 255),
    (1180, 700): (255, 255, 255),
    (640, 400): (255, 255, 0),
}
for point, color in expected.items():
    actual = rgb(*point)
    if actual != color:
        raise SystemExit(f"pixel {point} invalidus: {actual} != {color}")
print("   RECTE: scanout 1280x800 et quinque colores canonici exacti.")
PY

if kill -0 "$QEMU_PID" 2>/dev/null; then kill "$QEMU_PID" 2>/dev/null || true; fi
wait "$QEMU_PID" 2>/dev/null || true
QEMU_PID=""

nuntia '   RECTE: prima praesentatio totum scanout, secunda tantum 64x64 transfert.'
nuntia '   RECTE: backbuffer DMA directus omnes copias praesentiae vitat.'
nuntia '   RECTE: septem fences hardware consummatae sine mutatione semantica.'
nuntia ''
nuntia '=== BACKEND VIRTIO GRAPHICA X PROBATUS ==='
nuntia "   $LINEA"
