#!/usr/bin/env bash
# LABORATORIUM SYLVIAE — una probatio QEMU automatica.
set -eu

RADIX="$(git rev-parse --show-toplevel)"
LAB="$RADIX/laboratorium/sylvia"
EXITUS="/tmp/sylvia-lab"
MONITOR="$EXITUS/qemu-monitor.sock"
VARS="$EXITUS/OVMF_VARS_TEST.fd"

command -v qemu-system-x86_64 >/dev/null
command -v python3 >/dev/null
command -v websockify >/dev/null

pkill -f 'qemu-system-x86_64.*SYLVIA LABORATORIUM' 2>/dev/null || true
pkill -f 'websockify --web=/usr/share/novnc/ 6080 127.0.0.1:5900' 2>/dev/null || true

bash <(sed 's/\r$//' "$LAB/construe.sh")
rm -f "$VARS" "$MONITOR" "$EXITUS/sylvia-ante.ppm" "$EXITUS/sylvia-post.ppm"
cp /usr/share/OVMF/OVMF_VARS_4M.fd "$VARS"

qemu-system-x86_64 \
  -name "SYLVIA LABORATORIUM" \
  -machine q35 \
  -m 256M \
  -vga std \
  -device qemu-xhci \
  -device usb-tablet \
  -display none \
  -audiodev none,id=noaudio \
  -drive if=pflash,format=raw,unit=0,readonly=on,file=/usr/share/OVMF/OVMF_CODE_4M.fd \
  -drive if=pflash,format=raw,unit=1,file="$VARS" \
  -drive if=ide,format=raw,file="$EXITUS/sylvia-laboratorium.img" \
  -boot order=c \
  -monitor unix:"$MONITOR",server,nowait \
  -vnc 127.0.0.1:0 \
  -daemonize

sleep 3
python3 "$LAB/probationes/proba_qemu.py" "$MONITOR" "$EXITUS" || true

nohup websockify --web=/usr/share/novnc/ 6080 127.0.0.1:5900 \
  >"$EXITUS/novnc.log" 2>&1 &
printf '%s\n' "NOVNC: http://localhost:6080/vnc.html"

if command -v powershell.exe >/dev/null 2>&1; then
  powershell.exe -NoProfile -Command "Start-Process 'http://localhost:6080/vnc.html'" >/dev/null 2>&1 || true
fi
