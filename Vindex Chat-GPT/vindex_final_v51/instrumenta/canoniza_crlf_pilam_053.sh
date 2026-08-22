#!/usr/bin/env bash
# VINDEX 0.53: correctionem CRLF et pilam functionum canonice componit et comprobat.

set -euo pipefail

RADIX="$(cd "$(dirname "$0")/.." && pwd)"
REPO="$(cd "$RADIX/../.." && pwd)"
FONS="$RADIX/src/compilator_vindex.vindex"
TEMPORARIUM="$(mktemp -d)"
trap 'rm -rf -- "$TEMPORARIUM"' EXIT HUP INT TERM

COMPILATOR_NOVUS="$TEMPORARIUM/compilator_vindex"
PROBATIO_FONS="$TEMPORARIUM/pila_magna_053.vindex"
PROBATIO_BIN="$TEMPORARIUM/pila_magna_053"
RELATIO="$RADIX/instrumenta/RELATIO-CANONICA-CRLF-PILA-053.md"
REL_RADIX="${RADIX#$REPO/}"

cd "$REPO"

printf '%s\n' '=== 0. SCRIPTURAS UNIX LF REDINTEGRA ==='
mapfile -d '' SCRIPTURAE_LF < <(
python3 - "$REPO" "$REL_RADIX" <<'PY'
from pathlib import Path
import subprocess
import sys

repo = Path(sys.argv[1])
radix = sys.argv[2]
res = subprocess.run(
    ["git", "-C", str(repo), "ls-files", "-z", "--", radix],
    check=True,
    stdout=subprocess.PIPE,
).stdout
for raw in res.split(b"\0"):
    if not raw:
        continue
    rel = raw.decode("utf-8", "surrogateescape")
    via = repo / rel
    if not via.is_file():
        continue
    data = via.read_bytes()
    prima = data.split(b"\n", 1)[0].rstrip(b"\r")
    if not prima.startswith(b"#!"):
        continue
    if b"bash" not in prima and not prima.endswith(b"/sh"):
        continue
    nova = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    if nova != data:
        via.write_bytes(nova)
        sys.stdout.buffer.write(raw + b"\0")
PY
)
printf 'RECTE: %s scripturae Unix ad LF redactae sunt.\n' "${#SCRIPTURAE_LF[@]}"

printf '%s\n' '=== I. CRLF CORRIGE ==='
python3 "$RADIX/instrumenta/corrige_spatia_crlf_053.py"

printf '%s\n' '=== II. PILAM APPLICA ==='
python3 "$RADIX/instrumenta/applica_pilam_functionum_053.py"

printf '%s\n' '=== III. PUNCTUM FIXUM AB AMORSA ==='
# Diagnostica integra hunc gradum intra fractionem secundae absolvit; X secundae
# satis sunt ut regressio pathologica cito sistatur neque usorem diu detineat.
timeout 10s bash "$RADIX/bootstrap/reconstruit.sh" "$COMPILATOR_NOVUS"
chmod 755 "$COMPILATOR_NOVUS"

printf '%s\n' '=== IV. PILA MAIOR UNO MIB ==='
python3 "$RADIX/instrumenta/genera_probationem_pilae_053.py" "$PROBATIO_FONS"
timeout 15s "$COMPILATOR_NOVUS" "$PROBATIO_FONS" "$PROBATIO_BIN"
chmod 755 "$PROBATIO_BIN"

MENSURAE="$(python3 - "$PROBATIO_BIN" <<'PY'
from pathlib import Path
import sys

data = Path(sys.argv[1]).read_bytes()
frames = []
for i in range(len(data) - 55):
    if (
        data[i:i+2] == b"\x49\xbb"
        and data[i+10:i+17] == b"\x49\x81\xfb\x00\x10\x00\x00"
        and data[i+17:i+19] == b"\x76\x1c"
    ):
        frames.append(int.from_bytes(data[i+2:i+10], "little"))
if not frames:
    raise SystemExit("ERRATUM: prologus probationis pilae non inventus")
if any(x % 16 for x in frames):
    raise SystemExit(f"ERRATUM: fasciculi non ordinati: {frames}")
if max(frames) < 1024 * 1024:
    raise SystemExit(f"ERRATUM: fasciculus maior uno MiB non inventus: {frames}")
print(",".join(map(str, frames)))
PY
)"
printf 'FASCICULI: %s\n' "$MENSURAE"

EXITUS="$({ timeout 5s "$PROBATIO_BIN"; } 2>&1)"
STATUS_EXECUTIONIS=$?
printf '%s\n' "$EXITUS"
printf 'STATUS EXECUTIONIS: %s\n' "$STATUS_EXECUTIONIS"
[ "$STATUS_EXECUTIONIS" -eq 0 ]
[ "$EXITUS" = "$(printf '39\n777')" ]

printf '%s\n' '=== V. COMPILATOREM CANONICUM INSTAURA ==='
cp "$COMPILATOR_NOVUS" "$RADIX/compilator_vindex"
chmod 755 "$RADIX/compilator_vindex"

printf '%s\n' '=== VI. OFFICINAM ET SALUTATIONEM REGENERA ==='
"$RADIX/compilator_vindex" "$RADIX/src/officina_vindex.vindex" "$TEMPORARIUM/officina_vindex"
"$RADIX/compilator_vindex" "$RADIX/src/salutatio_vindex.vindex" "$TEMPORARIUM/salutatio_vindex"
cp "$TEMPORARIUM/officina_vindex" "$RADIX/officina_vindex"
cp "$TEMPORARIUM/salutatio_vindex" "$RADIX/salutatio_vindex"
chmod 755 "$RADIX/officina_vindex" "$RADIX/salutatio_vindex"

printf '%s\n' '=== VII. SYSTEMA BIOS ET UEFI REGENERA ==='
bash "$RADIX/systema/construe_systema.sh"
bash "$RADIX/systema/uefi/construe_uefi.sh"

printf '%s\n' '=== VIII. PROBATIONES REGRESSIONALES ==='
bash "$RADIX/tests/run_tests.sh"

SIGILLUM="$(sha256sum "$RADIX/compilator_vindex" | cut -d' ' -f1)"
cat > "$RELATIO" <<EOF
# VINDEX 0.53 — Relatio canonica CRLF et pilae

Correctio CRLF et migratio pilae functionum simul canonice comprobatae sunt.

\`\`\`text
PUNCTUM FIXUM: RECTE
SHA-256 COMPILATORIS: $SIGILLUM
FASCICULI PILAE: $MENSURAE
EXECUTIO PILAE: status=$STATUS_EXECUTIONIS
EXITUS PILAE:
$EXITUS
PROBATIONES REGRESSIONALES: RECTE
SYSTEMA BIOS: REGENERATUM
SYSTEMA UEFI: REGENERATUM
\`\`\`

\`IGNORA_SPATIA\` nunc CR (\`13\`) agnoscit; fontes CRLF igitur recte tractantur. Fasciculi pilae ex usu reali computantur, ad XVI octeta ordinantur, et pagina quaeque IV KiB tangitur. Scripturae testae Unix ante probationes ad LF canonice rediguntur.

VINDEX Latine cogitat. Sylvia Latine loquitur.
EOF

printf '%s\n' '=== IX. MUTATIONES CANONICAS COMMITTE ==='
VIAE=(
  "$RADIX/src/compilator_vindex.vindex"
  "$RADIX/compilator_vindex"
  "$RADIX/officina_vindex"
  "$RADIX/salutatio_vindex"
  "$RADIX/nucleus_systema.elf"
  "$RADIX/systema_vindex.img"
  "$RADIX/BOOTX64.EFI"
  "$RADIX/systema_vindex_uefi.img"
  "$RELATIO"
)
for VIA in "${VIAE[@]}"; do
    if [ -e "$VIA" ]; then
        git add -- "$VIA"
    fi
done
if [ "${#SCRIPTURAE_LF[@]}" -gt 0 ]; then
    git add -- "${SCRIPTURAE_LF[@]}"
fi

if git diff --cached --quiet; then
    printf '%s\n' 'MONITUM: nulla mutatio nova ad committendum inventa est.'
else
    git commit -m 'VINDEX 0.53: CRLF et pilam canonice comproba'
    git push origin HEAD:chatgpt/vindex-053-compilator-dynamicus
fi

printf '%s\n' '=== VINDEX 0.53: CRLF ET PILA CANONICE RECTA ==='
