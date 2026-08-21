#!/usr/bin/env bash
# VINDEX 0.53: diagnosin formarum dynamicarum per limites distinctos facit.

set -u

RADIX='Vindex Chat-GPT/vindex_final_v51'
FONS="$RADIX/src/compilator_vindex.vindex"
COMP="$RADIX/compilator_vindex"
RELATIO=/tmp/diagnosis_formae_053
: > "$RELATIO"

refice() {
  git checkout -- "$FONS" "$COMP" 2>/dev/null || true
}
trap refice EXIT

printf '%s\n' '== PRAEPARATIO ==' | tee -a "$RELATIO"
python3 "$RADIX/instrumenta/applica_formas_dynamicas_053.py" | tee -a "$RELATIO" || exit 1
chmod 755 "$COMP"
"$COMP" "$FONS" /tmp/g1_formae_diag >>"$RELATIO" 2>&1 || { cat "$RELATIO"; exit 1; }
chmod 755 /tmp/g1_formae_diag
printf '%s\n' 'RECTE: G1 ad diagnosin paratum est.' | tee -a "$RELATIO"

crea_casus() {
  MODUS="$1"
  N="$2"
  VIA="$3"
  python3 - "$MODUS" "$N" "$VIA" <<'PY'
from pathlib import Path
import sys
modus=sys.argv[1]
n=int(sys.argv[2])
via=Path(sys.argv[3])
L=[]
if modus == 'formae':
    for i in range(n):
        L += [f'FORMA Forma{i}.', '    CAMPUS valor SICUT NUMERUS.', 'FIN-FORMA.', '']
elif modus == 'campi':
    L += ['FORMA Magna.']
    for i in range(n):
        L += [f'    CAMPUS c{i} SICUT NUMERUS.']
    L += ['FIN-FORMA.', '']
else:
    raise SystemExit(2)
L += ['FUNCTIO PRINCIPALIS REDDENS NUMERUS.', '    REDDE 0.', 'FIN-FUNCTIO.', '']
via.write_text('\n'.join(L), encoding='utf-8')
PY
}

proba() {
  MODUS="$1"
  N="$2"
  VIA="/tmp/formae_diag_${MODUS}_${N}.vindex"
  EXE="/tmp/formae_diag_${MODUS}_${N}"
  crea_casus "$MODUS" "$N" "$VIA"
  INIT=$(date +%s)
  timeout 20s /tmp/g1_formae_diag "$VIA" "$EXE" >/tmp/formae_diag_stdout 2>/tmp/formae_diag_stderr
  S=$?
  FIN=$(date +%s)
  SEC=$((FIN-INIT))
  printf '%s %s: status=%s tempus=%ss\n' "$MODUS" "$N" "$S" "$SEC" | tee -a "$RELATIO"
  if [ -s /tmp/formae_diag_stdout ]; then sed 's/^/  stdout: /' /tmp/formae_diag_stdout | tee -a "$RELATIO"; fi
  if [ -s /tmp/formae_diag_stderr ]; then sed 's/^/  stderr: /' /tmp/formae_diag_stderr | tee -a "$RELATIO"; fi
}

printf '%s\n' '== NUMERUS FORMARUM, UNUS CAMPUS ==' | tee -a "$RELATIO"
for N in 8 15 16 17 24 32 40; do proba formae "$N"; done

printf '%s\n' '== NUMERUS CAMPORUM, UNA FORMA ==' | tee -a "$RELATIO"
for N in 8 16 25 26 27 40 64 80; do proba campi "$N"; done

printf '%s\n' '== FINIS DIAGNOSIS ==' | tee -a "$RELATIO"
cat "$RELATIO"
