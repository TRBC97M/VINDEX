#!/usr/bin/env bash
# VINDEX 0.53: diagnosin coniunctionis formarum, camporum et accessus camporum facit.

set -u

RADIX='Vindex Chat-GPT/vindex_final_v51'
FONS="$RADIX/src/compilator_vindex.vindex"
COMP="$RADIX/compilator_vindex"
RELATIO=/tmp/diagnosis_usus_formarum_053
: > "$RELATIO"

refice() {
  git checkout -- "$FONS" "$COMP" 2>/dev/null || true
}
trap refice EXIT

printf '%s\n' '== PRAEPARATIO ==' | tee -a "$RELATIO"
python3 "$RADIX/instrumenta/applica_formas_dynamicas_053.py" | tee -a "$RELATIO" || exit 1
chmod 755 "$COMP"
"$COMP" "$FONS" /tmp/g1_usus_formarum >>"$RELATIO" 2>&1 || exit 1
chmod 755 /tmp/g1_usus_formarum
printf '%s\n' 'RECTE: G1 ad diagnosin paratum est.' | tee -a "$RELATIO"

crea_casus() {
  FORMAE="$1"
  CAMPI="$2"
  USUS="$3"
  VIA="$4"
  python3 - "$FORMAE" "$CAMPI" "$USUS" "$VIA" <<'PY'
from pathlib import Path
import sys

formae = int(sys.argv[1])
campi = int(sys.argv[2])
usus = sys.argv[3]
via = Path(sys.argv[4])
L = []

for i in range(formae):
    L += [f'FORMA Forma{i}.', '    CAMPUS valor SICUT NUMERUS.', 'FIN-FORMA.', '']

if campi > 0:
    L += ['FORMA Magna.']
    for i in range(campi):
        L += [f'    CAMPUS c{i} SICUT NUMERUS.']
    L += ['FIN-FORMA.', '']

L += ['FUNCTIO PRINCIPALIS REDDENS NUMERUS.']

if usus in ('ultima', 'ambo'):
    if formae < 1:
        raise SystemExit('usus ultima sine forma ordinaria')
    L += [f'    DECLARA ultima SICUT Forma{formae - 1}.',
          '    valor DE ultima = 39.',
          '    PROCLAMA valor DE ultima.']

if usus in ('magna', 'ambo'):
    if campi < 1:
        raise SystemExit('usus magna sine campis')
    L += ['    DECLARA magna SICUT Magna.',
          f'    c{campi - 1} DE magna = 777.',
          f'    PROCLAMA c{campi - 1} DE magna.']

L += ['    REDDE 0.', 'FIN-FUNCTIO.', '']
via.write_text('\n'.join(L), encoding='utf-8')
PY
}

proba() {
  FORMAE="$1"
  CAMPI="$2"
  USUS="$3"
  NOMEN="f${FORMAE}_c${CAMPI}_${USUS}"
  VIA="/tmp/${NOMEN}.vindex"
  EXE="/tmp/${NOMEN}"
  crea_casus "$FORMAE" "$CAMPI" "$USUS" "$VIA"
  INIT=$(date +%s)
  timeout 15s /tmp/g1_usus_formarum "$VIA" "$EXE" >/tmp/usus_formarum_stdout 2>/tmp/usus_formarum_stderr
  S=$?
  FIN=$(date +%s)
  SEC=$((FIN-INIT))
  printf 'formae=%s campi=%s usus=%s: status=%s tempus=%ss\n' "$FORMAE" "$CAMPI" "$USUS" "$S" "$SEC" | tee -a "$RELATIO"
  if [ -s /tmp/usus_formarum_stdout ]; then sed 's/^/  stdout: /' /tmp/usus_formarum_stdout | tee -a "$RELATIO"; fi
  if [ -s /tmp/usus_formarum_stderr ]; then sed 's/^/  stderr: /' /tmp/usus_formarum_stderr | tee -a "$RELATIO"; fi
}

printf '%s\n' '== LIMES FORMARUM PURUS ==' | tee -a "$RELATIO"
for N in 40 41 48 64; do proba "$N" 0 nullus; done

printf '%s\n' '== CONIUNCTIO SINE ACCESSU ==' | tee -a "$RELATIO"
proba 1 80 nullus
proba 16 80 nullus
proba 32 80 nullus
proba 40 80 nullus

printf '%s\n' '== ACCESSUS CAMPI ==' | tee -a "$RELATIO"
proba 40 80 ultima
proba 40 80 magna
proba 40 80 ambo

printf '%s\n' '== CASUS MINORES CUM ACCESSU ==' | tee -a "$RELATIO"
proba 1 1 ambo
proba 16 27 ambo
proba 32 40 ambo
proba 40 40 ambo

printf '%s\n' '== FINIS DIAGNOSIS ==' | tee -a "$RELATIO"
