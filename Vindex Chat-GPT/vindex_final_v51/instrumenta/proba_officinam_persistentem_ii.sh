#!/usr/bin/env bash
# P19-II: OFFICINAM in bureau completo duobus initiis eiusdem imaginis probat.
# Primum initium documentum editat et F2 servat; secundum idem documentum
# reaperit, mutat et iterum servat. Nulla memoria inter initia transfertur.
set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
UEFI="$RADIX/systema/uefi"
TEMPORARIUM="$(mktemp -d "${TMPDIR:-/tmp}/vindex-p19-ii.XXXXXX")"
MORA="${MORA_P19_II:-45}"
SERVA_CAPTURAS="${SERVA_CAPTURAS:-}"

purga() {
    if [ -n "$SERVA_CAPTURAS" ]; then
        mkdir -p "$SERVA_CAPTURAS" 2>/dev/null || true
        cp -f "$TEMPORARIUM"/*.ppm "$SERVA_CAPTURAS"/ 2>/dev/null || true
    fi
    rm -rf "$TEMPORARIUM" 2>/dev/null || true
}
trap purga EXIT HUP INT TERM

OVMF_CODE=""
for via in /usr/share/OVMF/OVMF_CODE_4M.fd /usr/share/OVMF/OVMF_CODE.fd /usr/share/ovmf/OVMF.fd /usr/share/qemu/OVMF.fd; do
    if [ -f "$via" ]; then OVMF_CODE="$via"; break; fi
done
OVMF_VARS=""
for via in /usr/share/OVMF/OVMF_VARS_4M.fd /usr/share/OVMF/OVMF_VARS.fd; do
    if [ -f "$via" ]; then OVMF_VARS="$via"; break; fi
done
if ! command -v qemu-system-x86_64 >/dev/null 2>&1 || [ -z "$OVMF_CODE" ] || [ -z "$OVMF_VARS" ]; then
    printf '%s\n' 'OMISSUM: QEMU/OVMF deest; P19-II persistentia OFFICINAE non exercetur.'
    exit 0
fi

printf '%s\n' 'I. Imaginem Sylviae plenam cum OFFICINA P19-II construe...'
NUCLEUS_FONS="$RADIX/systema/fenestrale_ii_purus_i.vindex" \
    bash "$UEFI/construe_uefi_purum.sh" "$TEMPORARIUM/systema.img" "$TEMPORARIUM/BOOTX64.EFI" \
    >"$TEMPORARIUM/constructio.log" 2>&1 || {
        cat "$TEMPORARIUM/constructio.log" >&2
        exit 1
    }

python3 - "$TEMPORARIUM/systema.img" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
data = p.read_bytes()
if b"ZEPHYR72941\nNOVAPERSISTET" in data:
    raise SystemExit("DEFECIT: documentum probationis ante primum initium iam in imagine adest")
PY

boot() {
    local numerus="$1"
    local modus="$2"
    local monitor="$TEMPORARIUM/monitor-${numerus}.sock"
    local qmp="$TEMPORARIUM/qmp-${numerus}.sock"
    local vars="$TEMPORARIUM/OVMF_VARS-${numerus}.fd"
    cp -f "$OVMF_VARS" "$vars"
    chmod +w "$vars"

    qemu-system-x86_64 -machine q35 -m 256 -vga std \
        -drive "if=pflash,format=raw,unit=0,readonly=on,file=$OVMF_CODE" \
        -drive "if=pflash,format=raw,unit=1,file=$vars" \
        -drive "if=ide,format=raw,file=$TEMPORARIUM/systema.img" \
        -display none \
        -monitor "unix:$monitor,server=on,wait=off" \
        -qmp "unix:$qmp,server=on,wait=off" \
        -net none >"$TEMPORARIUM/qemu-${numerus}.log" 2>&1 &
    local pid=$!

    # Capturae directe in TEMPORARIUM ponuntur ut etiam defectus praecox eas servet.
    if ! python3 "$RADIX/instrumenta/proba_officinam_persistentem_ii.py" \
        "$monitor" "$qmp" "$TEMPORARIUM" "$MORA" "$modus"; then
        kill "$pid" 2>/dev/null || true
        wait "$pid" 2>/dev/null || true
        tail -80 "$TEMPORARIUM/qemu-${numerus}.log" >&2 || true
        return 1
    fi
    wait "$pid" 2>/dev/null || true
}

printf '%s\n' 'II. Primum initium: OFFICINA documentum scribit et F2 servat...'
boot 1 1
python3 - "$TEMPORARIUM/systema.img" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
data = p.read_bytes()
expectatum = b"ZEPHYR72941\nNOVAPERSISTET"
if expectatum not in data:
    raise SystemExit("DEFECIT: primum initium documentum OFFICINAE in disco non reliquit")
print(f"OFFICINA-P19-II: primum_documentum_octeta={len(expectatum)}")
PY
printf '%s\n' '   RECTE: primum initium OFFICINA documentum in disco reliquit.'

printf '%s\n' 'III. Secundum initium: OFFICINA documentum reaperit, X addit et iterum servat...'
boot 2 2
python3 - "$TEMPORARIUM/systema.img" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
data = p.read_bytes()
expectatum = b"ZEPHYR72941\nNOVAPERSISTETX"
if expectatum not in data:
    raise SystemExit("DEFECIT: secundum initium documentum re-apertum et mutatum non servavit")
print(f"OFFICINA-P19-II: secundum_documentum_octeta={len(expectatum)}")
PY
printf '%s\n' '   RECTE: secundum initium documentum re-apertum mutavit et iterum servavit.'

printf '%s\n' '=== P19-II OFFICINA PERSISTENS DUOBUS INITIIS PROBATA ==='
printf '%s\n' 'OVMF -> Sylvia [VINDEX] -> OFFICINA -> FS_* -> restart -> OFFICINA -> FS_*'
printf '%s\n' 'Nulla copia memoriae inter initia transfertur.'
